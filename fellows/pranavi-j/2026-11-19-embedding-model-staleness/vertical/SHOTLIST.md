# SHOTLIST — Embedding Model Staleness: The Index That Quietly Split in Two
## Total: 202.238s measured (Kokoro audio + real silent B00 track) · 10 beats · all Manim, no
## pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | B00_TitleCard (scenes.py) | 4.128s | Silent title card: "Embedding Model Staleness: The Index That Quietly Split in Two" + @HumanitariansAI, no narration |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | B01_ExecSummary (scenes.py) | 17.78s | Personal-intro card: name + role + one-line plain-language summary, spoken |
| B02 | HOOK | manim | GRAPHIC | B02_SplitGeometryHook (scenes.py) | 24.67s | A generic vector-index panel showing docs from Model A and Model B at the same dimensionality, then an overlay: "Two geometries. Did anything notice?" |
| B03 | FRAMEWORK | manim | GRAPHIC | B03_ThreeQuestionsFramework (scenes.py) | 29.23s | All 3 tests shown together, before any example (Check the Checkpoint / Audit the Whole Index / Watch for Silence) |
| B04 | WORKED-EXAMPLE | manim | GRAPHIC | B04_SilentSplit (scenes.py) | 32.47s | A corpus split across two embedding models, a query against the whole index, and the old document's rank quietly falling — tagged SPLIT GEOMETRY — SILENTLY |
| B05 | FALSIFIABILITY | manim | GRAPHIC | B05_FullReembedHolds (scenes.py) | 23.11s | Identical corpus and switch event — but every old document is fully re-embedded before serving, so nothing splits — tagged FULLY RE-EMBEDDED — NOTHING TO MIX |
| B06 | REAL-WORLD-NOTE | manim | GRAPHIC | B06_MycroftRealWorldNote (scenes.py) | 32.02s | Verbatim-quoted lines from mycroft's real rag.py/config.py, framed as an honest design-choice illustration, not a bug report |
| B07 | SCAFFOLDED-TASK | manim | GRAPHIC | B07_AuditChecklist (scenes.py) | 24.22s | The 3-question rubric restated as a concrete, actionable checklist, distinct from B03's framework card |
| B08 | TAKEAWAY | manim | GRAPHIC | B08_Statement (scenes.py) | 13.1s | Statement card: an embedding model's geometry isn't portable |
| B09 | SIGN-OFF | manim | GRAPHIC | B09_BrandOutro (scenes.py) | 1.51s | @HumanitariansAI brand card, "explained with Claude Code", "in for Sai Pranavi J." |

## Lane summary
- MANIM: all 10 beats, self-contained in this reel's own `scenes.py`. No pantry stills, no
  Remotion components, no `brutalist/` toolkit changes.
- Style/palette/helpers (PALETTE, `T()`, `fit()`, `panel()`, `box_around()`, `stat_row()`,
  `metric_panel()`) copied from this fellow's sibling reels
  `2026-11-13-context-window-limits` and `2026-11-04-goodharts-law-proxy-metrics` for house-style
  consistency. The "LABEL : VALUE" stat-row idiom fits this reel's mechanism directly (a
  model/dimension/rank fact shown as a label + its current value), reused across B02/B04/B05 for
  vector-space and rank rows.
- This is a general AI/STEM topic explainer, not a report of real engineering work on a live
  incident — the worked example (B04's corpus-split scenario) and its falsifiability case (B05's
  identical scenario with a full re-embed instead) are both fully generic/hypothetical, no real
  model's production accuracy is claimed as universal (see FACTCHECK.md, SOURCES.md). The ONE
  quantified figures used anywhere in this video come from this build's own real, reproducible
  local demo in `verification/`, using two real, named, open sentence-transformer models — reported
  as a single real run, not a benchmark claim.
- B03 is this reel's most legibility-critical beat: all 3 tests must read as a real, checklist-
  shaped rubric (not just asserted in narration) before any example appears.
- B04/B05 share the exact same corpus size (1,000 documents) and the exact same switch event, so
  the worked example and its falsifiability resolution are visually comparable at a glance — only
  whether a full re-embed happened before serving (and the old document's resulting search rank)
  differs, isolating precisely the one variable the rubric's own test (#2, Audit the Whole Index)
  actually names.
- B06 is a distinct beat from this fellow's usual pattern of keeping real-world tie-ins fully
  generic (see CWL's house rule) — this video's build brief explicitly directed naming mycroft's
  `rag.py` and quoting its real source verbatim, framed strictly as a design-choice illustration,
  never a bug report (confirmed no bug exists there — see FACTCHECK.md #6).
- B07's checklist is a concrete action (3 checkbox rows, distinct composition), not a second copy
  of B03's framework card.

## Vertical companion
`vertical/scenes.py` holds the native-portrait redesign of all 10 beats, built for `./art vertical`
— see that file's module docstring for the per-beat side-by-side -> stacked notes.

## QC status
See `BUILD-LOG.md` for GATE A/V results and per-beat visual-inspection findings from the render
pipeline.
