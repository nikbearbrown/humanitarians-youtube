# SHOTLIST — How Facial Recognition Actually Works (And When It Shouldn't)
## Estimated ~2:17 (pre-audio-lock estimate) · 8 beats · all Manim, no pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Est. Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | HOOK | manim | GRAPHIC | B00_EverywhereHook (scenes.py) | 15s | Phone/Airport/Store/Policing chips, then debate framing |
| B01 | MECHANISM | manim | GRAPHIC | B01_PipelineMechanism (scenes.py) | 25s | Face -> Detect -> Embedding -> Compare -> Score gauge (98%) |
| B02 | BENEFITS | manim | GRAPHIC | B02_LegitimateUses (scenes.py) | 13s | List-reveal, sage checks: accessibility, unlock, missing persons, medical |
| B03 | HARMS | manim | GRAPHIC | B03_HarmfulUses (scenes.py) | 14s | List-reveal, crimson marks: surveillance, retail tracking, biometric risk |
| B04 | EVIDENCE | manim | GRAPHIC | B04_NistEvidence (scenes.py) | 37s | Bar chart: most-algorithms gap vs. best-performing near-zero gap; industry dissent line |
| B05 | FRAMEWORK | manim | GRAPHIC | B05_FluencyTrap (scenes.py) | 18s | Split panel: fluent paragraph vs. match score, both "looks certain" |
| B06 | TAKEAWAY | manim | GRAPHIC | B06_ScrutinyScale (scenes.py) | 10s | Low-to-high-stakes scrutiny gradient bar |
| B07 | SIGN-OFF | manim | GRAPHIC | B07_BrandOutro (scenes.py) | 5s | @HumanitariansAI, in for Sai Pranavi Jeedigunta |

## QC plan
- Pre-flight (before first render): `runtime/qc/static_scene_check.py` and
  `runtime/qc/wcag_margin_check.py` per scene, per the lesson from the prior
  reel — catches shape-distinctness and margin/off-frame issues before
  spending a render.
- Post-render: `runtime/qc/manim_layout_audit.py` (per-scene) and
  `runtime/qc/final_frame_check.py` (whole compiled reel) — check the true
  clean master, not just the `-slate.mp4` review cut, which carries a
  review-only timecode watermark that produces a known false-positive
  "edge-bleed" BLOCKER on every frame.
