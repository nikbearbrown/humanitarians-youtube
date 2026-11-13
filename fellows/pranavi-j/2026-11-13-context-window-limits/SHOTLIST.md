# SHOTLIST — Context Window Limits: The Budget That Doesn't Grow
## Total: 177.54s (B00 as actually used by the pipeline, 4.0s — see FRICTIONAL.md for a harmless
## duplicate-JSON-key bug that substituted this for the originally-measured 4.128s silent track;
## both final masters measure 177.625s after frame-rounding) · 9 beats · all Manim, no pantry/
## toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | B00_TitleCard (scenes.py) | 4.0s | Silent title card: "Context Window Limits: The Budget That Doesn't Grow" + @HumanitariansAI, no narration |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | B01_ExecSummary (scenes.py) | 16.49s | Personal-intro card: name + role + one-line plain-language summary, spoken |
| B02 | HOOK | manim | GRAPHIC | B02_FixedPoolHook (scenes.py) | 22.61s | A generic context-window budget panel filling up row by row, then an overlay: "Full. Did it tell you?" |
| B03 | FRAMEWORK | manim | GRAPHIC | B03_ThreeQuestionsFramework (scenes.py) | 34.10s | All 3 tests shown together, before any example (Count the Tokens / Share the Pool / Watch the Edge) |
| B04 | WORKED-EXAMPLE | manim | GRAPHIC | B04_SilentTruncation (scenes.py) | 31.75s | A fixed budget, its competing consumers, and the oldest conversation turns quietly dropped — tagged TRUNCATED — SILENTLY |
| B05 | FALSIFIABILITY | manim | GRAPHIC | B05_ExplicitRejectionHolds (scenes.py) | 24.79s | Identical budget, numbers, and overflow — but the system checks the total and refuses outright instead — tagged CAUGHT IMMEDIATELY |
| B06 | SCAFFOLDED-TASK | manim | GRAPHIC | B06_AuditChecklist (scenes.py) | 28.13s | The 3-question rubric restated as a concrete, actionable checklist, distinct from B03's framework card |
| B07 | TAKEAWAY | manim | GRAPHIC | B07_Statement (scenes.py) | 14.16s | Statement card: a context window is a fixed budget, not an elastic resource |
| B08 | SIGN-OFF | manim | GRAPHIC | B08_BrandOutro (scenes.py) | 1.51s | @HumanitariansAI brand card, "explained with Claude Code", "in for Sai Pranavi J." |

## Lane summary
- MANIM: all 9 beats, self-contained in this reel's own `scenes.py`. No pantry stills, no
  Remotion components, no `brutalist/` toolkit changes.
- Style/palette/helpers (PALETTE, `T()`, `fit()`, `panel()`, `box_around()`, `stat_row()`,
  `metric_panel()`) copied from this fellow's sibling reels
  `2026-11-04-goodharts-law-proxy-metrics` and `2026-10-28-in-context-learning-limits` (same
  fellow, same voice, same series) for house-style consistency. The "LABEL : VALUE" stat-row idiom
  fits this reel's mechanism directly (a tracked token count shown as a label + its current
  value), reused across B02/B04/B05 for budget rows instead of metric rows.
- This is a general AI/STEM topic explainer, not a report of real engineering work — the worked
  example (B04's fixed-budget/document/history scenario) and its falsifiability case (B05's
  identical scenario with an explicit-error system instead) are both fully generic/hypothetical,
  no real model, vendor, or disclosed benchmark is named or resembled (see FACTCHECK.md,
  SOURCES.md).
- B03 is this reel's most legibility-critical beat: all 3 tests must read as a real, checklist-
  shaped rubric (not just asserted in narration) before any example appears.
- B04/B05 share the exact same budget panel composition, the exact same token counts, and the
  exact same overflow condition so the worked example and its falsifiability resolution are
  visually comparable at a glance — only whether the system checks the total before answering
  (and what it does about the overflow) differs, isolating precisely the one variable the
  rubric's own test (#3, Watch the Edge) actually names.
- B06's checklist is a concrete action (3 checkbox rows, distinct composition), not a second copy
  of B03's framework card.

## Vertical companion
`vertical/scenes.py` holds the native-portrait redesign of all 9 beats, built for `./art vertical`
— see that file's module docstring for the per-beat side-by-side -> stacked notes.

## QC status
See `BUILD-LOG.md` for GATE A/V results and per-beat visual-inspection findings from the render
pipeline.
