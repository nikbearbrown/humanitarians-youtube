# SHOTLIST — In-Context Learning: What the Prompt Can (and Can't) Teach
## Total: 173.14s (measured Kokoro audio, B00 silent) · 9 beats · all Manim, no pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | B00_TitleCard (scenes.py) | 4.104s | Silent title card: "In-Context Learning: What the Prompt Can (and Can't) Teach" + @HumanitariansAI, no narration |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | B01_ExecSummary (scenes.py) | 14.64s | Personal-intro card: name + role + one-line plain-language summary, spoken |
| B02 | HOOK | manim | GRAPHIC | B02_LearningOrLocatingHook (scenes.py) | 21.26s | A prompt panel of example pairs, a new query resolving correctly, then an overlay: "Learning, or locating?" |
| B03 | FRAMEWORK | manim | GRAPHIC | B03_ThreeTestsFramework (scenes.py) | 35.21s | All 3 tests shown together, before any example (Spot the Mapping / Shuffle the Set / Push Past the Window) |
| B04 | WORKED-EXAMPLE | manim | GRAPHIC | B04_ToyMappingWorkedExample (scenes.py) | 28.49s | A made-up rule shown only as 4 example pairs; a new, unseen query resolves correctly, tagged "LOCATED, NOT LEARNED" |
| B05 | FALSIFIABILITY | manim | GRAPHIC | B05_ReorderedFlippedFalsifiability (scenes.py) | 27.17s | Same 4 examples, reordered, one mapping flipped; the identical new query now resolves wrong, tagged "MISMATCH" |
| B06 | SCAFFOLDED-TASK | manim | GRAPHIC | B06_AuditChecklist (scenes.py) | 27.70s | The 3-question rubric restated as a concrete, actionable checklist, distinct from B03's framework card |
| B07 | TAKEAWAY | manim | GRAPHIC | B07_Statement (scenes.py) | 13.06s | Statement card: ICL is pattern-location, bounded by what's latent and by what fits the prompt |
| B08 | SIGN-OFF | manim | GRAPHIC | B08_BrandOutro (scenes.py) | 1.51s | @HumanitariansAI brand card, "explained with Claude Code", "in for Sai Pranavi J." |

## Lane summary
- MANIM: all 9 beats, self-contained in this reel's own `scenes.py`. No pantry stills, no
  Remotion components, no `brutalist/` toolkit changes.
- Style/palette/helpers (PALETTE, `T()`, `fit()`, `panel()`, `box_around()`) copied from this
  fellow's closest sibling `2026-10-21-calibration-why-confidence-isnt-accuracy` (same fellow,
  same voice, same series) for house-style consistency. The example-pair helpers (`pair_row()`,
  `example_panel()`) are new to this reel, built for its specific mechanism (a toy rule shown only
  as input/output example pairs in a "prompt"), and reused across B02/B04/B05.
- This is a general AI/STEM topic explainer, not a report of real engineering work — the worked
  example (B04's Caesar-shift-by-3 toy rule, 4 example pairs, a new query resolved correctly) and
  its falsifiability case (B05's reordered + one-flipped-mapping version of the identical task,
  the same new query now resolving wrong) are both fully generic/hypothetical, no real model,
  vendor, or disclosed benchmark is named or resembled (see FACTCHECK.md, SOURCES.md).
- B03 is this reel's most legibility-critical beat: all 3 tests must read as a real, checklist-
  shaped rubric (not just asserted in narration) before any example appears.
- B04/B05 share the exact same example-panel composition so the worked example and its
  falsifiability resolution are visually comparable at a glance — a clean "LOCATED, NOT LEARNED"
  resolution in B04, a visibly marked "FLIPPED" example and a "MISMATCH" resolution in B05.
- B06's checklist is a concrete action (3 checkbox rows, distinct composition), not a second copy
  of B03's framework card.

## Vertical companion
`vertical/scenes.py` holds the native-portrait redesign of all 9 beats, built for `./art vertical`
— see that file's module docstring for the per-beat side-by-side -> stacked notes.

## QC status
See `BUILD-LOG.md` for GATE A/V results and per-beat visual-inspection findings from the render
pipeline.
