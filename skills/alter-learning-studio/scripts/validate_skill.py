#!/usr/bin/env python3
"""Dependency-free structural, content and generated lesson regression checks."""
import json
import re
import sys
import tempfile
import importlib.util
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('alter_builder',ROOT/'scripts'/'build_lesson.py')
builder=importlib.util.module_from_spec(spec);spec.loader.exec_module(builder)

def check(cond, msg):
    if not cond:raise AssertionError(msg)

def main():
    skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
    check(skill.startswith('---\n'),'SKILL.md must start with YAML frontmatter')
    parts=skill.split('---',2)
    check(len(parts)==3,'frontmatter closing fence absent')
    fm=parts[1]
    name=re.search(r'^name:\s*(.+)$',fm,re.M)
    desc=re.search(r'^description:\s*(.+)$',fm,re.M)
    check(bool(name),'frontmatter name missing');check(bool(desc),'frontmatter description missing')
    check(name.group(1)=='alter-learning-studio','name must match folder')
    check(1<=len(desc.group(1))<=1024,'description length out of bounds')
    check(len(skill.splitlines())<500,'skill instructions exceed 500 lines')
    for p in ['references/alter-framework.md','references/lesson-schema.md','references/visualization-playbook.md','references/motion-production.md','references/quality-gates.md','references/sources.md','references/toss-inspired-design.md','references/motion-graphics-contract.md','assets/tokens-toss-inspired.json','assets/player/player.html','assets/plan-template.md','assets/progress-template.md']:
        check((ROOT/p).is_file(),p+' missing')
    lesson_files=sorted((ROOT/'assets'/'examples').glob('*.json'))
    check(len(lesson_files)>=3,'need cross-domain examples')
    with tempfile.TemporaryDirectory() as td:
        for f in lesson_files:
            data=builder.validate(json.loads(f.read_text(encoding='utf-8')))
            out=Path(td)/(f.stem+'.html');builder.build(f,out)
            html=out.read_text(encoding='utf-8')
            check('/*__ALTER_LESSON_JSON__*/' not in html,'lesson data marker was not replaced')
            check('https://' not in html.split('<style>')[0],'unexpected external stylesheet')
            check('<script src=' not in html,'must have no external scripts')
            check('prefers-reduced-motion' in html,'missing reduced motion support')
            check('id="timeline"' in html and 'id="play"' in html,'player navigation incomplete')
            check('id="quizQuestion"' in html and 'id="metrics"' in html,'learning interaction incomplete')
            check('id="stageBeats"' in html and 'id="stageCaption"' in html,'motion storyboard elements missing')
            check('renderMotion(raw)' in html and 'strokeDashoffset' in html,'causal frame-by-frame animation missing')
            check('#3182f6' in html.lower(),'light Toss-inspired blue palette missing')
            check(data['title'] in html,'generated data missing from output')
            print(f"  PASS: {f.stem} — {len(data['scenes'])} scenes, {len(data['nodes'])} nodes, {len(data['model']['outputs'])} metrics")
        # Reject arbitrary code or unknown symbol injection in model.
        malicious=json.loads(lesson_files[0].read_text(encoding='utf-8'))
        malicious['model']['outputs'][0]['expr']={'op':'eval','args':[1]}
        try:builder.validate(malicious)
        except ValueError:pass
        else:raise AssertionError('code injection via expressions accepted')
        malicious=json.loads(lesson_files[0].read_text(encoding='utf-8'))
        malicious['sources'][0]['url']='javascript:alert(1)'
        try:builder.validate(malicious)
        except ValueError:pass
        else:raise AssertionError('unsafe source scheme accepted')
    print('PASS: skill metadata, references, cross-domain lessons, safe expressions and offline player checks')

if __name__=='__main__':
    try:main()
    except Exception as err:
        print('FAILED:',err,file=sys.stderr)
        sys.exit(1)
