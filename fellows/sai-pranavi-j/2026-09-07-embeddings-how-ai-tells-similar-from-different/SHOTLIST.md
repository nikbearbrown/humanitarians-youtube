# SHOTLIST — Embeddings: How AI Tells Similar From Different (When Keyword Matching Can't)
## ~147s target (pre-audio-lock estimate) · 9 beats · all Manim, no pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Est. Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | B00_TitleCard (scenes.py) | 4s | Silent title card: video title + @HumanitariansAI |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | B01_ExecSummary (scenes.py) | 15s | Personal-intro card: fellow's name + one-line summary, spoken |
| B02 | HOOK | manim | GRAPHIC | B02_KeywordMissHook (scenes.py) | 16s | Document tagging rule matches "Investment Adviser Disclosure" but misses a doc titled "RIA" |
| B03 | FRAMEWORK | manim | GRAPHIC | B03_ThreeQuestionsFramework (scenes.py) | 24s | 3-question rubric graphic (Wording Varies / Context Flips Meaning / Exactness Is The Point), shown before any example |
| B04 | WORKED-EXAMPLE | manim | GRAPHIC | B04_MeaningSpaceDiagram (scenes.py) | 26s | "Meaning space" scatter: RIA / investment adviser / advisor plotted close together, "quarterly earnings" plotted far away |
| B05 | FALSIFIABILITY | manim | GRAPHIC | B05_ExactnessFalsifiability (scenes.py) | 26s | Same diagram style, "Section 4.12"/"Section 4.13" (fictional placeholders) plotted close together — a warning, not a win |
| B06 | SCAFFOLDED-TASK | manim | GRAPHIC | B06_AuditChecklist (scenes.py) | 20s | 3 questions restated as a checkbox checklist, visually distinct from B03's rubric card |
| B07 | TAKEAWAY | manim | GRAPHIC | B07_Statement (scenes.py) | 15s | Statement card |
| B08 | SIGN-OFF | manim | GRAPHIC | B08_BrandOutro (scenes.py) | 5s | @HumanitariansAI, in for Sai Pranavi Jeedigunta |

## Open items
- None — all 9 beats are self-contained Manim scenes; no pantry stills, no Remotion assets.

## QC plan
- Pre-flight (before first render): `runtime/qc/static_scene_check.py` and
  `runtime/qc/wcag_margin_check.py --palette humanitarians` per scene — catches
  shape-distinctness and margin/off-frame issues before spending a render.
- Real-manim bounds check: B02's document-card/rule-box side-by-side layout and
  B04/B05's meaning-space cluster labels were measured directly (real Manim
  `get_left()`/`get_right()`/`get_top()`/`get_bottom()`, not the render-free
  static-check stub) to confirm no overlap before rendering — see BUILD-LOG.md.
- Post-render: `runtime/qc/final_frame_check.py` (whole compiled reel) — check
  the true clean master, not just the `-slate.mp4` review cut, which carries a
  review-only timecode watermark that produces a known false-positive
  "edge-bleed" BLOCKER on every frame.
