# Motion graphics contract — every visually taught lesson

Motion graphics are **required** for a requested visual lesson, not an optional enhancement to a static HTML page. Use this as a production and acceptance contract.

## Design before implementing

Create a 4-beat storyboard for each scene in the lesson:

| Beat | Time in a 5.6s example | Question answered | Visual action |
|---|---|---|---|
| 1. Cause | 0–1.0 s | What starts it? | reveal source, focus cue and initial state |
| 2. Change | 1.0–2.5 s | What changed? | threshold crossing, object creation, transform, split or comparison |
| 3. Transfer | 2.5–4.4 s | Where did it go? | trace path, transport, particle/packet transition or transformation |
| 4. Result | 4.4–5.6 s | What does that mean? | settle destination, show correct result, hold long enough to read |

Durations are defaults, not fixed prescriptions. Use a `storyboard.md` per lesson for visuals, labels, narration/reading cues, interpretation and evidence.

## Mandatory mechanics

- [ ] At least 3 causally different scenes (baseline, perturbation, new outcome).
- [ ] Subject movement: show at least one domain event (packet delivery, transformation, quantity change, branching or time-dependent state) with meaningful start and finish.
- [ ] Clear scene-internal beats; beginning and end states visibly different, not just camera zooms, opacity and hover.
- [ ] Deterministic seek, pause, play, replay, speed setting, next/previous and visual timeline.
- [ ] Inputs alter true outputs; if an input should alter an animation, update the animation too rather than showing disconnected numbers.
- [ ] End holds for comprehension; no endless over-stimulation, excessive wobble or unreadable effects.
- [ ] A reduced-motion alternative preserves the **meaningful final states and captions**.
- [ ] Verify desktop and 390px mobile; keyboard navigation and labels.
- [ ] Clearly distinguish simulation from measured reality, document numeric assumptions, do not hallucinate observable system telemetry.
- [ ] No generic title sequences, intro splash, demo watermark, irrelevant badges or “cinematic” effects obstructing learning.

## Choose the correct visualization engine

- Network / architecture: SVG vector paths, target actors, animated request/response packets, queue lengths, color-coded healthy vs failed.
- Probability / statistics: moving dots / bars / distribution shape that reflects the modeled value; deterministic seed if randomness is shown.
- Math / physics: axes + moving point/vector/field with correct time integration or analytic solution.
- Biology / chemistry: schematized molecule/cell state transitions; clearly mark what is simplified.
- Language: animated token chunks, morphemes, syntax grouping, error correction, with accessible text readout.
- Economics / business: flow of goods/stock/price along quantities and time, coherent legends, no fabricated empirical data.
- History: chronologically sequenced events, map movement only if geography supported by sources.

Default shared player is a **safe diagram-first renderer**, not a license to force every subject into nodes and arrows. For domain-specific concepts, implement a specialized semantic SVG/Canvas/DOM scene while retaining the playback/learning contract.

## Implementation levels

**Tier 1 — self-contained offline HTML (default):** CSS/SVG/Canvas + deterministic `requestAnimationFrame` playhead, authored timeline for events and values. Existing bundled player supports route reveal, packet transfer, arrival emphasis and 4 internal beats. No network dependency.

**Tier 2 — complex choreography:** GSAP Timeline/ScrollTrigger (if dependency is installed and license/asset use clear) or Web Animations API, with synchronized playback and reduced-motion fallback. Avoid adding dependencies to otherwise offline lessons without permission.

**Tier 3 — standalone video:** Remotion / Blender / After Effects or an accessible encoder only if MP4/GIF is actually requested. Verify render, audio/subtitles and aspect ratio, and deliver video only after producing it.

## Motion review checklist (mandatory E/Editor visual QA)

1. Freeze the first, middle and last frames: can a learner infer the causal story?
2. Scrub backward: do objects and labels return to the correct previous state?
3. Change the primary input: does the visual consequence agree with displayed calculations?
4. Disable animations: are final states, evidence and explanations accessible?
5. Separate brand and instructional signals: is the interface quiet while the concept moves?
6. Visually inspect 1440px and 390px, and capture one screenshot/video clip as proof.
7. If an object/quantity is shown, prove it matches the lesson JSON or derived model; otherwise label it *conceptual illustration*.

## Technical references

- [Web Animations API — MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API): timing, animation model, accessibility.
- [GSAP Timeline](https://gsap.com/docs/v3/GSAP/Timeline/): choreographed and seekable timelines.
- [GSAP ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/): scroll-linked progression when relevant, not automatically for every lesson.
