# SHOTLIST — Goodhart's Law: When the Proxy Stops Being the Target
## Total: 169.06s (measured Kokoro audio, B00 silent) · 9 beats · all Manim, no pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | B00_TitleCard (scenes.py) | 4.128s | Silent title card: "Goodhart's Law: When the Proxy Stops Being the Target" + @HumanitariansAI, no narration |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | B01_ExecSummary (scenes.py) | 13.78s | Personal-intro card: name + role + one-line plain-language summary, spoken |
| B02 | HOOK | manim | GRAPHIC | B02_ProxyUpTargetUpHook (scenes.py) | 20.14s | A generic dashboard metric panel ticking upward week over week, then an overlay: "Proxy up. Target up too?" |
| B03 | FRAMEWORK | manim | GRAPHIC | B03_ThreeQuestionsFramework (scenes.py) | 29.06s | All 3 tests shown together, before any example (Name the Target / Find the Lever / Watch the Coupling) |
| B04 | WORKED-EXAMPLE | manim | GRAPHIC | B04_HandleTimeDivergence (scenes.py) | 27.74s | A call-center proxy (average handle time) improves on schedule while the real target (problems resolved), never tracked, quietly worsens — tagged DIVERGED |
| B05 | FALSIFIABILITY | manim | GRAPHIC | B05_CounterbalancedCheckHolds (scenes.py) | 26.93s | Identical scenario, identical numbers, identical gaming pressure — but the real target is now a tracked counterbalancing check, so the same worsening is caught immediately — tagged CAUGHT — STAYS HONEST |
| B06 | SCAFFOLDED-TASK | manim | GRAPHIC | B06_AuditChecklist (scenes.py) | 28.44s | The 3-question rubric restated as a concrete, actionable checklist, distinct from B03's framework card |
| B07 | TAKEAWAY | manim | GRAPHIC | B07_Statement (scenes.py) | 17.33s | Statement card: Goodhart's Law is about good metrics in changed conditions, not bad metrics |
| B08 | SIGN-OFF | manim | GRAPHIC | B08_BrandOutro (scenes.py) | 1.51s | @HumanitariansAI brand card, "explained with Claude Code", "in for Sai Pranavi J." |

## Lane summary
- MANIM: all 9 beats, self-contained in this reel's own `scenes.py`. No pantry stills, no
  Remotion components, no `brutalist/` toolkit changes.
- Style/palette/helpers (PALETTE, `T()`, `fit()`, `panel()`, `box_around()`) copied from this
  fellow's sibling reels `2026-10-21-calibration-why-confidence-isnt-accuracy` and
  `2026-10-28-in-context-learning-limits` (same fellow, same voice, same series) for house-style
  consistency. The metric helpers (`stat_row()`, `metric_panel()`) are new to this reel, built for
  its specific mechanism (a tracked number and its real target shown as labeled stat rows inside a
  bordered panel), and reused across B02/B04/B05.
- This is a general AI/STEM topic explainer, not a report of real engineering work — the worked
  example (B04's call-center average-handle-time scenario) and its falsifiability/counterbalance
  case (B05's identical scenario with a tracked counterbalancing check added) are both fully
  generic/hypothetical, no real company, vendor, or disclosed benchmark is named or resembled (see
  FACTCHECK.md, SOURCES.md).
- B03 is this reel's most legibility-critical beat: all 3 tests must read as a real, checklist-
  shaped rubric (not just asserted in narration) before any example appears.
- B04/B05 share the exact same metric-panel composition, the exact same before/after numbers, and
  the exact same gaming pressure so the worked example and its falsifiability resolution are
  visually comparable at a glance — only whether the real target is framed as "ON THE SCOREBOARD"
  (tracked) differs, isolating precisely the one variable the rubric's own test (#2/#3) names.
- B06's checklist is a concrete action (3 checkbox rows, distinct composition), not a second copy
  of B03's framework card.

## Vertical companion
`vertical/scenes.py` holds the native-portrait redesign of all 9 beats, built for `./art vertical`
— see that file's module docstring for the per-beat side-by-side -> stacked notes.

## QC status
See `BUILD-LOG.md` for GATE A/V results and per-beat visual-inspection findings from the render
pipeline.
