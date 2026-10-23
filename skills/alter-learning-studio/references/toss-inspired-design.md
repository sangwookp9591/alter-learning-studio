# Default HTML visual language — Toss-inspired, original implementation

**Mandatory default when the user has not chosen another visual direction.** This is an original educational UI **inspired by** the broad clarity of Korean fintech product design; it is **not** an official Toss product, Toss Design System implementation, or a license to copy proprietary assets.

## Design intent

- **Toss-like atmosphere:** calm, trustworthy, fresh, bright; enormous attention to hierarchy and immediate comprehension.
- Base: clean off-white canvas and true-white elevated surfaces. Dark hero dashboards, terminal-themed dashboards, noisy gradients, neon glow, cyberpunk colors and glass-heavy surfaces are **not** acceptable defaults.
- Compose large, natural Korean headlines with short readable body copy. Show one concept per scene. Hide supporting details until relevant.
- Original iconography only: CSS/SVG primitive icons or properly licensed icon libraries. Do not use Toss logo, illustrations, proprietary components, screenshots, official animations or copyrighted brand assets unless separately authorized.

## Default design tokens (not a claim of official Toss tokens)

| Token | Value | Usage |
|---|---|---|
| canvas | `#F5F7FA` | page background |
| surface | `#FFFFFF` | cards / story panels |
| stage | `#EAF2FF`–`#F4F8FF` | main teaching stage |
| blue | `#3182F6` | primary action, causality, active targets |
| text | `#191F28` | headlines / key facts |
| secondary text | `#6B7684` | annotations, metadata |
| border | `#E7EBF1` | soft division |
| orange | `#F59E0B` | warning or alternate agent; not dominant |
| negative | `#F04452` | failures only |
| radius | 14–26 px | inputs/cards |
| spacing | 8 px system | page rhythm |
| headline | 36–64 px | responsive hero |

- Prefer system Korean font stack (no requirement to download or embed proprietary fonts).
- High-contrast text and buttons; verify contrast rather than relying on these sample hex values for every context.
- Main stage 16:9-ish on desktop, horizontal scroll for diagrams that cannot fit mobile without breaking causality. Explanations must remain readable at 390 px.
- Use semantic headings, labelled controls, actual progress feedback, visible keyboard focus and reduced-motion mode.

## Component language

1. Oversized simple title + a single purpose sentence.
2. Motion stage: unambiguous actors, cause/change/result, sequenced movement, one dominant attention point.
3. Playback strip: previous, play/pause, next, continuous scrub, speed. Never decorative nonworking controls.
4. Explanatory sidebar: what, why, misconception, prompt. Do not obscure the visual with wall-of-text panels.
5. Hands-on controls: move actual model inputs, display correctly computed outcomes and assumptions.
6. Practice panel: answer, feedback, next move.

## Motion identity

- Product microinteraction: about 150–320 ms, subtle ease-out/spring for click and state feedback.
- Educational process: 4–7 seconds per scene with **four visual beats**: cause → state change → movement/consequence → readable resolution. Viewer must be able to pause, rewind, scrub deterministically.
- Animate **subject matter**, not the chrome. Examples: packets move along routes; cache paths diverge into hit/miss; probability mass changes shape; neurons transmit signals; grammar chunks re-order; historical sequence appears chronologically.
- Prefer transform/opacity for decorative motion; use SVG path reveal / motion along path for causal diagrams, real-time model recomputation for simulations.
- If the visual is merely a static diagram with floating particles or animated cards, **fail the visual quality gate** and revise the subject animation.

## Attribution / research

- Toss Tech, [인터랙션, 꼭 넣어야 해요?](https://toss.tech/article/interaction): interactions should improve understanding/usability; uses easing tokens, spring and timeline concepts.
- Toss Tech, [토스 디자이너가 제품에만 집중할 수 있는 방법](https://toss.tech/article/toss-design-system): consistency, lightweight surfaces and tactile feedback.
- Toss Tech, [토스가 디자인 직무를 2개로 줄인 이유](https://toss.tech/article/47067): graphics, interaction, design system boundaries and integrated visual practice.
- These sources inform broad experience principles only; the tokens and player visuals above are **independently authored examples**.
