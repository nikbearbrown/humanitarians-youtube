# SHOTLIST — Lost in the Middle: Why More Context Doesn't Guarantee a Better Answer
## Total: 140.14s (measured Kokoro audio, B00 silent) · 9 beats · all Manim, no pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | B00_TitleCard (scenes.py) | 4.06s | Silent title card: "Lost in the Middle: Why More Context Doesn't Guarantee a Better Answer" + @HumanitariansAI, no narration |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | B01_ExecSummary (scenes.py) | 16.90s | Personal-intro card: name + role + one-line plain-language summary, spoken |
| B02 | HOOK | manim | GRAPHIC | B02_TwoDocumentsHook (scenes.py) | 16.97s | A short paragraph (fact found every time) vs a long document (same fact, buried, missed) — both labeled with the same question |
| B03 | MECHANISM | manim | GRAPHIC | B03_AttentionCurveDiagram (scenes.py) | 24.00s | Real U-shaped attention-strength curve plotted over a horizontal context bar — high at both ends, dipping in the middle; no numeric values |
| B04 | WORKED-EXAMPLE | manim | GRAPHIC | B04_BuriedFactMiss (scenes.py) | 21.60s | A long onboarding document, key fact highlighted in the middle section; model's answer shown as a miss; mini attention-curve inset with a red marker at the low middle |
| B05 | FALSIFIABILITY | manim | GRAPHIC | B05_RepositionedFactFound (scenes.py) | 15.60s | Same document, same fact, moved to the start; model's answer now correct; mini attention-curve inset with a sage marker at a high end |
| B06 | SCAFFOLDED-TASK | manim | GRAPHIC | B06_AuditChecklist (scenes.py) | 28.27s | The 3-question rubric (context length / where the fact sits / would moving it change the answer) restated as an actionable checklist, distinct from B03's diagram |
| B07 | TAKEAWAY | manim | GRAPHIC | B07_Statement (scenes.py) | 11.23s | Statement card: a model missing a buried fact isn't failing to understand it — it's reading unevenly |
| B08 | SIGN-OFF | manim | GRAPHIC | B08_BrandOutro (scenes.py) | 1.51s | @HumanitariansAI brand card, "explained with Claude Code", "in for Sai Pranavi J." — short card matching this beat's short approved narration |

## Lane summary
- MANIM: all 9 beats, self-contained in this reel's own `scenes.py`. No
  pantry stills, no Remotion components, no `brutalist/` toolkit changes.
- Style/palette/helpers (PALETTE, `T()`, `fit()`, `panel()`, `box_around()`)
  copied from this fellow's closest siblings
  `2026-09-22-hallucination-why-sounding-sure-isnt-being-right` and
  `2026-09-29-tokenization-why-ai-cant-count-its-own-letters` (same fellow,
  same voice, same series) for house-style consistency. The attention-curve
  helpers (`curve_y`, `attention_curve_mobject`, `curve_point`,
  `curve_fill_area`) and `document_stack()` are new to this reel, built for
  its specific mechanism (a plotted U-shaped curve, a stack-of-lines
  document illustration), and reused across B03/B04/B05.
- This is a general AI/STEM topic explainer, not a report of real engineering
  work — the worked example (B04's buried-fact onboarding-document scenario)
  and its falsifiability case (B05) are both fully generic/hypothetical, no
  real model, vendor, or disclosed benchmark is named or resembled (see
  FACTCHECK.md, SOURCES.md). No fabricated percentage/statistic is shown
  anywhere — the attention curve has no numeric axis values.
- B03 is this reel's most legibility-critical beat: the U-shaped curve must
  read as a real, clearly-shaped diagram (high-low-high), not just an
  assertion in narration.
- B04/B05 tie back to B03 via a small reusable "mini curve" inset — a red
  marker at the low middle point in B04, a sage marker at a high end point
  in B05 — so the worked example and its resolution are visually anchored
  to the mechanism, not just restated in text.
- B06's checklist is a concrete action (3 checkbox rows, distinct
  composition), not a second copy of B03's diagram.

## Vertical companion
`vertical/scenes.py` holds the native-portrait redesign of all 9 beats,
built for `./art vertical` — see that file's module docstring for the
per-beat side-by-side -> stacked notes (B02, B04, B05's side-by-side
document/Q&A layouts restacked top/bottom for the narrow canvas).

## QC status
See `BUILD-LOG.md` for GATE A/V results and per-beat visual-inspection
findings from the render pipeline.
