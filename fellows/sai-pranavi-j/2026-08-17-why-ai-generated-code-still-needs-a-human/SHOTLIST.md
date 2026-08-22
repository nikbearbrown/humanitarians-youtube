# SHOTLIST — Why AI-Generated Code Still Needs a Human Who Understands the System
## Estimated ~2:10 (pre-audio-lock estimate) · 7 beats · all Manim, no pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Est. Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | HOOK | manim | GRAPHIC | B00_HookCrashLog (scenes.py, not yet authored) | 15s | Split screen: escaped-quotes diff vs. crash log, both held ≥2s |
| B01 | FRAMEWORK | manim | GRAPHIC | B01_FrameworkRubric (scenes.py, not yet authored) | 20s | 3-question rubric graphic (Trace/Consequence/Why), shown before any example |
| B02 | WORKED-EXAMPLE | manim | GRAPHIC | B02_WorkedExampleDiff (scenes.py, not yet authored) | 40s | Illustrative before/after code diff, both versions legible simultaneously, rubric walked through live |
| B03 | FALSIFIABILITY | manim | GRAPHIC | B03_FalsifiabilityCase (scenes.py, not yet authored) | 20s | Date-formatter function next to rubric, "low stakes" annotation |
| B04 | CTA | manim | GRAPHIC | B04_ScaffoldedTask (scenes.py, not yet authored) | 20s | 3-step checklist as copyable text, held ≥3s |
| B05 | CLOSE | manim | GRAPHIC | B05_Close (scenes.py, not yet authored) | 10s | Callback to B00's crash log, now with a correction checkmark |
| B06 | SIGN-OFF | manim | GRAPHIC | B06_BrandOutro (scenes.py, not yet authored) | 5s | @HumanitariansAI, in for Sai Pranavi Jeedigunta |

## Open items
- ~~No channel/fellow sign-off beat~~ RESOLVED 2026-08-17 — B06 added per fellow decision.
- `scenes.py` has not been authored — all scene names above are planned, not built.

## QC plan (once scenes.py exists)
- Pre-flight (before first render): `runtime/qc/static_scene_check.py` and
  `runtime/qc/wcag_margin_check.py` per scene — catches shape-distinctness and
  margin/off-frame issues before spending a render, per the lesson from this
  fellow's prior reels.
- Post-render: `runtime/qc/manim_layout_audit.py` (per-scene) and
  `runtime/qc/final_frame_check.py` (whole compiled reel) — check the true
  clean master, not just the `-slate.mp4` review cut, which carries a
  review-only timecode watermark that produces a known false-positive
  "edge-bleed" BLOCKER on every frame.
