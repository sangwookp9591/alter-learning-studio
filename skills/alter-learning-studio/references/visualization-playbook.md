# Visualization selection and stagecraft

## Choose visual by learning mechanism

- **Process/routing/control loops:** Nodes + directed edges + moving packet/marker. Use bundled player.
- **Continuous or quantitative:** Axes, units, thresholds, parametric curve; prefer plot over network nodes. Provide source and domains of input variables.
- **Comparisons:** Side-by-side synchronized states, constant scale, highlighted deltas.
- **History/time:** Timeline with causal sequence; avoid visually implying certainty where disputed.
- **Spatial/physical:** SVG for 2D, three.js/WebGL only when 3D fundamentally changes understanding; always supply flat fallback.
- **Language/semantics:** Sentence segmentation, dependency tree, draggable choices; skip gratuitous particles.
- **Proof/math:** Stepwise symbolic changes with preserved invariants; avoid animation that obscures algebra.

## Required interaction and clarity

- At least three pedagogically distinct scenes when teaching a mechanism: baseline → disturbance → consequence/correction.
- Play/pause and scene step controls; scrub to explore causality; visible narration and labels.
- Visually distinguish *current* paths, absent paths, conditional paths; clearly label hypothetical values.
- Color conveys meaning only in combination with labels/shapes/legend.
- Changes must remain visible after motion; no infinite meaningless background animations.
- Keyboard accessibility: buttons, labels, focus styles; avoid traps. `prefers-reduced-motion` respected.
- Support narrow viewports without horizontal scrolling through the full page; diagrams can adapt or locally scroll if essential.
- Require static textual explanation; the motion is supplemental.

## Motion grammar

- Reveal in cause-first order: source → transformation → output → exception.
- Favor transform/opacity over expensive layout-thrashing properties.
- Motion durations 250–850ms for UI events, 1.5–4s for explanatory packet journeys depending on narration. Easing and pauses serve comprehension.
- Scrubbing should select the precise scene or time segment; speed should change animation speed consistently.
- Reduced motion mode must maintain all meaningful state and labels but remove movement.
- High-stakes topics: minimize motion and make data provenance prominent.

## Model discipline

An interactive slider is valuable only if it changes a legitimate relationship. Mark all unknown coefficients; distinguish hypothetical illustrations from measurements; show units. Add counterexamples (e.g. “more Pods doesn't move existing requests”). Don't imply that a toy model is an operational forecast.

## Visual direction (mandatory default)

See `toss-inspired-design.md` and `motion-graphics-contract.md`: white/soft gray, blue focus, Korean-readable hierarchy, animated subject causality, not decorative UI movement. For charts use a moving data mark; for language animate token grouping; for networks animate requests flowing. The graph-first shared player is only a starting point.
