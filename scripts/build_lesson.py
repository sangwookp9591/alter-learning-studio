#!/usr/bin/env python3
"""Validate a declarative A.L.T.E.R. lesson and build fully offline HTML.

No third-party packages. The lesson contains only data, not executable JavaScript.
"""
from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "assets" / "player" / "player.html"
MARKER = "/*__ALTER_LESSON_JSON__*/"
ID = re.compile(r"^[a-z][a-z0-9-]{1,63}$")
KINDS = {"source", "process", "target", "control", "observe"}
PHASES = set("ALTER")
OPS = {"add":(1,8),"subtract":(2,2),"multiply":(1,8),"divide":(2,2),"min":(1,8),"max":(1,8),"ceil":(1,1),"floor":(1,1),"round":(1,1),"clamp":(3,3)}


def error(msg):
    raise ValueError(msg)


def text_field(d, name, where, maxlen=1200):
    v = d.get(name)
    if not isinstance(v, str) or not v.strip() or len(v) > maxlen:
        error(f"{where}.{name} must be nonempty text <= {maxlen} chars")
    return v


def array(d, name, where, low, high):
    v = d.get(name)
    if not isinstance(v, list) or not low <= len(v) <= high:
        error(f"{where}.{name} must be an array with {low}..{high} elements")
    return v


def number(v, where):
    if isinstance(v, bool) or not isinstance(v,(int,float)) or not math.isfinite(v):
        error(f"{where} must be a finite number")
    return v


def unique_ids(items, where):
    ids=[]
    for i,item in enumerate(items):
        if not isinstance(item, dict): error(f"{where}[{i}] must be object")
        ident=text_field(item,"id",f"{where}[{i}]",64)
        if not ID.fullmatch(ident):error(f"{where}[{i}].id: must be lowercase slug")
        ids.append(ident)
    if len(ids)!=len(set(ids)):error(f"{where} ids must be unique")
    return set(ids)


def validate_expr(expr, inputs, where, depth=0):
    if depth>20: error(f"{where}: max expression depth 20")
    if isinstance(expr,(float,int)) and not isinstance(expr,bool): number(expr,where);return
    if not isinstance(expr,dict):error(f"{where}: expression must be numeric literal, variable or op")
    if set(expr)=={"var"}:
        if expr["var"] not in inputs:error(f"{where}: unknown variable {expr['var']}")
        return
    if set(expr)!={"op","args"} or expr["op"] not in OPS or not isinstance(expr["args"],list):error(f"{where}: unsupported op expression")
    low,high=OPS[expr["op"]]
    if not low<=len(expr["args"])<=high:error(f"{where}: wrong arg count for {expr['op']}")
    for i,arg in enumerate(expr["args"]):validate_expr(arg,inputs,f"{where}.args[{i}]",depth+1)


def validate(data):
    if not isinstance(data,dict):error("lesson must be JSON object")
    if not ID.fullmatch(text_field(data,"id","lesson",64)):error("lesson.id must be slug")
    for k in ("title","subtitle","domain","level","outcome"):text_field(data,k,"lesson")
    for x in array(data,"assumptions","lesson",1,8):
        if not isinstance(x,str) or not x.strip():error("assumptions must be strings")
    nodes=array(data,"nodes","lesson",2,10);node_ids=unique_ids(nodes,"nodes")
    for n in nodes:
        for k in ("label","detail"):text_field(n,k,"node")
        for k in ("x","y"):
            if not 8<=number(n.get(k),f"node.{k}")<=92:error(f"node.{k} out of range")
        if n.get("kind") not in KINDS:error("bad node.kind")
    edges=array(data,"edges","lesson",1,16);edge_ids=unique_ids(edges,"edges")
    for e in edges:
        text_field(e,"label","edge")
        if e.get("from") not in node_ids or e.get("to") not in node_ids:error("edge references missing node")
        if e["from"]==e["to"]:error("self edge not supported")
    scenes=array(data,"scenes","lesson",3,7)
    for idx,s in enumerate(scenes):
        if not isinstance(s,dict):error(f"scenes[{idx}] must be object")
        if s.get("phase") not in PHASES:error("scene.phase must be A/L/T/E/R")
        for k in ("title","lead","detail","insight","question"):text_field(s,k,"scene",1800)
        if not set(array(s,"activeNodes","scene",1,10))<=node_ids:error("scene references unknown node")
        if not set(array(s,"activeEdges","scene",0,16))<=edge_ids:error("scene references unknown edge")
    model=data.get("model")
    if not isinstance(model,dict):error("model must be object")
    text_field(model,"title","model");text_field(model,"description","model")
    inputs=array(model,"inputs","model",1,3);input_ids=unique_ids(inputs,"model.inputs")
    for inp in inputs:
        for k in ("label","unit"):text_field(inp,k,"model.input")
        lo,hi,step,val=(number(inp.get(k),"input."+k) for k in ("min","max","step","value"))
        if not lo<hi or not step>0 or not lo<=val<=hi:error("input bounds/step/value invalid")
    outputs=array(model,"outputs","model",1,4);unique_ids(outputs,"model.outputs")
    for out in outputs:
        for k in ("label","unit"):text_field(out,k,"model.output")
        if not isinstance(out.get("precision"),int) or not 0<=out["precision"]<=4:error("precision must be 0..4")
        validate_expr(out.get("expr"),input_ids,"model.output.expr")
    quiz=data.get("quiz")
    if not isinstance(quiz,dict):error("quiz must be object")
    text_field(quiz,"question","quiz");text_field(quiz,"explanation","quiz")
    choices=array(quiz,"options","quiz",2,5)
    for c in choices:
        if not isinstance(c,str) or not c.strip():error("empty quiz option")
    if len(set(choices))!=len(choices):error("quiz options must be distinct")
    if not isinstance(quiz.get("answer"),int) or isinstance(quiz["answer"],bool) or not 0<=quiz["answer"]<len(choices):error("quiz.answer invalid")
    sources=array(data,"sources","lesson",1,6)
    for s in sources:
        if not isinstance(s,dict):error("source object required")
        text_field(s,"title","source");u=text_field(s,"url","source")
        if not re.match(r"^https://[^\s/]+(?:/[^\s]*)?$",u):error("source links must be HTTPS")
    if "analogy" in data:
        a=data["analogy"]
        if not isinstance(a,dict):error("analogy must be object")
        for k in ("domain","works","fails"):text_field(a,k,"analogy")
    if "footnote" in data:text_field(data,"footnote","lesson")
    return data


def build(source:Path, output:Path):
    data=validate(json.loads(source.read_text(encoding="utf-8")))
    template=TEMPLATE.read_text(encoding="utf-8")
    if template.count(MARKER)!=1:error("player template injection marker mismatch")
    payload=json.dumps(data,ensure_ascii=False,separators=(",",":"),allow_nan=False)
    payload=payload.replace("<","\\u003c").replace(">","\\u003e").replace("&","\\u0026").replace("\u2028","\\u2028").replace("\u2029","\\u2029")
    result=template.replace(MARKER,payload)
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(result,encoding="utf-8")
    print(f"Built: {output} ({output.stat().st_size:,} bytes; {len(data['scenes'])} scenes)")


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input",required=True,type=Path)
    parser.add_argument("--output",type=Path)
    parser.add_argument("--validate-only",action="store_true")
    args=parser.parse_args()
    if args.validate_only:
        validate(json.loads(args.input.read_text(encoding="utf-8")))
        print(f"Valid lesson: {args.input}")
    else:
        if args.output is None:parser.error("--output is required unless --validate-only")
        build(args.input,args.output)

if __name__=="__main__":main()
