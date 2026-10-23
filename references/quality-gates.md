# Quality gates before delivering any learner artifact

## Correctness

- [ ] Each scene maps to a fact, documented simulation, or clearly flagged analogy.
- [ ] Every numerical output includes units, input domain and named assumptions.
- [ ] Quiz answer is unique; explanation is consistent with visual state.
- [ ] Source links resolve when online research was possible; versions and dates noted for time-sensitive subjects.
- [ ] Learner's existing progress wasn't overwritten.

## Behavior

- [ ] Generated HTML loads offline without exceptions.
- [ ] Prev/Next, play/pause, timeline, speed, input sliders, answer feedback work.
- [ ] Edges connect to actual nodes and animate only for active scene.
- [ ] Same output shown after seeking and after autoplay; no stale scene displays.
- [ ] Reduced-motion preference leaves text and controls usable.
- [ ] Mobile width and desktop width keep labels legible.

## Evidence and handoff

- [ ] Run `python3 scripts/validate_skill.py` and report result.
- [ ] Prefer browser smoke test: read title and manipulate 1–2 controls; check console errors and screenshot if available.
- [ ] Record which checks actually ran and list any untested behavior.
- [ ] Deliver SKILL.md, example HTML, transferable lesson data; explain install path and first command.

## Coordinator / multi-agent integration

One coordinator owns model/spec. Librarian returns verified references; Tutor returns misconception/quiz plan; Animator returns storyboard; Implementer builds runtime; Editor independently validates. Reconcile conflicts and test full execution path before declaring completion.

## Required v2 visual and interaction checks

- [ ] Light original Toss-inspired aesthetic (not a dark dashboard), no proprietary Toss assets.
- [ ] Four meaningful motion beats per scene; animated concept not just interface chrome.
- [ ] Continuous deterministic timeline scrub across all scenes, including reverse seeking.
- [ ] `prefers-reduced-motion` reveals readable static concept state.
- [ ] Compare 1440px and 390px captures; no overlap in primary learning story.
- [ ] At least one quantitative or stateful manipulation visibly agrees with the explanation.
- [ ] No dark styling in newly generated galleries or lesson player.
