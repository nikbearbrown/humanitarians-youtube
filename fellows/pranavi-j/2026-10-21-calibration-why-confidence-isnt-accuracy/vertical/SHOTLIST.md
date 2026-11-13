# SHOTLIST — Calibration: Why Confidence Isn't Accuracy
## Total: 147.28s (measured Kokoro audio, B00 silent) · 9 beats · all Manim, no pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | B00_TitleCard (scenes.py) | 4.05s | Silent title card: "Calibration: Why Confidence Isn't Accuracy" + @HumanitariansAI, no narration |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | B01_ExecSummary (scenes.py) | 14.33s | Personal-intro card: name + role + one-line plain-language summary, spoken |
| B02 | HOOK | manim | GRAPHIC | B02_SameConfidenceHook (scenes.py) | 15.94s | Two answer cards, identically confident in tone, one correct one wrong — then an overlay: "Sounding sure isn't the same as being right" |
| B03 | FRAMEWORK | manim | GRAPHIC | B03_ThreeTestsFramework (scenes.py) | 29.35s | All 3 tests shown together, before any example (Bucket the Claims / Count the Cases / Spot the Bluff) |
| B04 | WORKED-EXAMPLE | manim | GRAPHIC | B04_OverconfidentBucket (scenes.py) | 25.63s | A "~90% confident" bucket of 10 answer chips (6 correct/4 wrong); STATED (90%) vs ACTUAL (60%) bars with the gap highlighted |
| B05 | FALSIFIABILITY | manim | GRAPHIC | B05_WellCalibratedFalsifiability (scenes.py) | 23.66s | Same bucket-and-bars layout, 9/10 correct (90%); STATED and ACTUAL bars nearly match — a checkmark where B04 had a gap |
| B06 | SCAFFOLDED-TASK | manim | GRAPHIC | B06_AuditChecklist (scenes.py) | 21.17s | The 3-question rubric restated as a concrete, actionable checklist, distinct from B03's framework card |
| B07 | TAKEAWAY | manim | GRAPHIC | B07_Statement (scenes.py) | 11.64s | Statement card: sounding sure and being right are different claims; check whether confidence tracks real accuracy |
| B08 | SIGN-OFF | manim | GRAPHIC | B08_BrandOutro (scenes.py) | 1.51s | @HumanitariansAI brand card, "explained with Claude Code", "in for Sai Pranavi J." |

## Lane summary
- MANIM: all 9 beats, self-contained in this reel's own `scenes.py`. No pantry stills, no
  Remotion components, no `brutalist/` toolkit changes.
- Style/palette/helpers (PALETTE, `T()`, `fit()`, `panel()`, `box_around()`) copied from this
  fellow's closest siblings `2026-10-15-chain-of-thought-why-the-reasoning-isnt-always-the-reason`
  and `2026-10-06-lost-in-the-middle-why-more-context-isnt-better` (same fellow, same voice, same
  series) for house-style consistency. The confidence-bucket helpers (`answer_chip()`,
  `chip_row()`, `stat_bar()`, `confidence_card()`) are new to this reel, built for its specific
  mechanism (a bucket of answer chips, a stated-vs-actual bar pair), and reused across B02/B04/B05.
- This is a general AI/STEM topic explainer, not a report of real engineering work — the worked
  example (B04's 90%-stated/60%-actual overconfident bucket) and its falsifiability case (B05's
  90%-stated/90%-actual well-calibrated bucket) are both fully generic/hypothetical, no real model,
  vendor, or disclosed benchmark is named or resembled (see FACTCHECK.md, SOURCES.md). No real
  statistic is shown anywhere — all percentages are illustrative round numbers chosen for teaching
  clarity.
- B03 is this reel's most legibility-critical beat: all 3 tests must read as a real, checklist-
  shaped rubric (not just asserted in narration) before any example appears.
- B04/B05 share the exact same bucket-and-bars composition so the worked example and its
  falsifiability resolution are visually comparable at a glance — a real STATED/ACTUAL gap in B04
  (teal bar visibly shorter than the gold bar), bars that nearly match in B05.
- B06's checklist is a concrete action (3 checkbox rows, distinct composition), not a second copy
  of B03's framework card.

## Vertical companion
`vertical/scenes.py` holds the native-portrait redesign of all 9 beats, built for `./art vertical`
— see that file's module docstring for the per-beat side-by-side -> stacked notes.

## QC status
See `BUILD-LOG.md` for GATE A/V results and per-beat visual-inspection findings from the render
pipeline.
