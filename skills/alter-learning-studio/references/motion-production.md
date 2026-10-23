# Motion graphics production workflows

## Tier 0: offline interactive HTML (default)

Use bundled `assets/player/player.html`, inline CSS/SVG/JS, fixed layout coordinates and keyed scene states. Scene-internal four-beat choreography + traced causal path + packet/object transfer + target arrival + continuous seek and playback controls. A static flowchart with a moving ornament does not pass. Default UI uses original Toss-inspired light visual tokens. Avoid CDN/runtime dependencies. Static final state must make sense with all animation disabled.

## Tier 1: advanced interactive scene

Use HTML/SVG/Canvas with an explicit storyboard and output-verifying controls, Web Animations API, optionally GSAP or Motion when complex timeline orchestration justifies a dependency. Keep dependency explicit, pin versions, ensure license compliance and offline fallback. For React apps, use component-based state, but preserve semantic labels and keyboard access.

## Tier 2: narrated explainer video

Prepare storyboard: shot, duration, camera/path, visual cue, narration, source, assertion, subtitle, transition. Build in Remotion (React/video), Blender (3D), After Effects, or another available renderer based on user needs. Record actual render and verify duration, resolution, audio, captions and media outputs. Do **not** call an HTML animation an MP4. If software/tool access is missing, produce a storyboard and the working HTML; say video export wasn't completed.

## Review checklist

- Narration references exactly what the graphic shows; no contradicting labels.
- Motion reveals causality instead of merely sliding everything around.
- Video and HTML use consistent numbers, units and assumptions.
- Do not fabricate benchmarks, screenshots, integrations or rendering success.
- Captions readable at 9:16 and desktop sizes when video is requested.
- Avoid flashing, full-screen rapid scaling, and unnecessary loop motion.
