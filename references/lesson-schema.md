# Self-contained HTML lesson — JSON contract (v1)

`python3 scripts/build_lesson.py --input path/to/lesson.json --output path/to/lesson.html`

Top-level required:

- `id`: a short lowercase slug.
- `title`, `subtitle`, `domain`, `level`: clear Korean/English text.
- `outcome`: one observable learning goal.
- `assumptions`: list of 1–5 statements marking toy-model limits.
- `nodes`: 2–10 records `{id,label,detail,x,y,kind}`, x/y in `[8..92]` representing percent center coordinates. Kind in `source|process|target|control|observe`.
- `edges`: up to 16 records `{id,from,to,label}`, from/to are valid node IDs.
- `scenes`: 3–7 records `{phase,title,lead,detail,activeNodes,activeEdges,insight,question}`. `phase` is `A|L|T|E|R`; activeNodes / activeEdges are arrays of valid IDs. State is visible even without animation. Each scene drives highlighted graph elements, progressive path drawing, directional packet transfer and destination emphasis across four beats. For physics, grammar, distributions and other non-flow subjects, create a domain-specific motion scene rather than forcing a flow diagram.
- `model`: `{title,description,inputs,outputs}`. `inputs`: 1–3 records `{id,label,min,max,step,value,unit}` with finite numeric bounds; `outputs`: 1–4 records `{id,label,unit,precision,expr}`. Expressions are **structured trees** (not JavaScript): a number, `{"var":"inputId"}`, or `{"op":"add|subtract|multiply|divide|min|max|ceil|floor|round|clamp", "args":[expr...]}`. Divide by zero emits an em dash rather than infinity. No `eval`.
- `quiz`: `{question,options:[string,string,...],answer:0-based-index,explanation:string}`.
- `sources`: 1–6 records `{title,url}` linking to primary or verified sources. No invented URLs. Links must begin with HTTPS.
- Optional: `analogy`: `{domain,works,fails}`, `footnote`: plain text.

Example fragment:

```json
{
  "model": {
    "title": "Tiny teaching model",
    "description": "Assume evenly distributed independent requests",
    "inputs": [{"id":"requests","label":"Requests","min":0,"max":100,"step":10,"value":50,"unit":"r/s"}],
    "outputs": [{"id":"half","label":"Half","unit":"r/s","precision":1,"expr":{"op":"divide","args":[{"var":"requests"},2]}}]
  }
}
```

## Why JSON rather than pasted HTML?

- Source of truth for scenes and math; prevents visual explanation and quiz from drifting.
- Safety: text-only DOM updates; no arbitrary JS snippets, `eval`, or model-defined code.
- Agent can author and review data separately from renderer implementation.

## Story direction

At least 3 scenes should tell a causal story, not repeat identical diagram highlighting. Use first scene for baseline, second for disturbance, third for changed consequence, fourth for qualification, fifth for transfer (or A–L–T–E–R progression). Simplified models must explain why they differ from real systems.

## v2 default motion and style

Bundled player now defaults to **Toss-inspired original light styling** and a continuous 4-beat per-scene timeline (cause / change / transfer / result). Motion is seekable and reduced-motion users see stable explanatory states. This does not change the v1 lesson JSON schema. See `references/toss-inspired-design.md` and `references/motion-graphics-contract.md`.
