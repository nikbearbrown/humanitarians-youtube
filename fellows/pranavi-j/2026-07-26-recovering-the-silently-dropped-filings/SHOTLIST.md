# SHOTLIST — The Pipeline That Was Lying to Me
## Total: 106.46s (measured, 4K 3840x2160, rebuilt 2026-08-26) · 9 beats · all Manim, no pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | B00_TitleCard (scenes.py) | 4.23s | NEW 2026-08-26. Silent title card: "The Pipeline That Was Lying to Me" + @HumanitariansAI, no narration |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | B01_ExecSummary (scenes.py) | 13.87s | NEW 2026-08-26. Personal-intro card: name + role + one-line summary, spoken (narration text fixed by program feedback) |
| B02 | HOOK | manim | GRAPHIC | B02_CalmDashboard (scenes.py) | 9.70s | [was B00] Calm feed log — SEC/FINRA/CFTC/FedReg rows ticking in, cursor dot tracking down; nothing looks wrong |
| B03 | SETUP | manim | GRAPHIC | B03_PipelineDiagram (scenes.py) | 26.81s | [was B01] 5 feeds (SEC, FINRA, CFTC, FedReg-Sec., FedReg-CFTC) -> normalize -> score -> Postgres -> email alert; filter callout |
| B04 | DISCOVERY | manim | GRAPHIC | B04_ClaudeCodeDiff (scenes.py) | 18.79s | [was B02] Dark code panel, diff view highlighting the removed `content isNotEmpty` filter node |
| B05 | PROOF | manim | GRAPHIC | B05_RecoveredFilings (scenes.py) | 8.23s | [was B03] List-reveal: Cboe Clear U.S. / MEMX LLC / Nasdaq GEMX SRO notice / US v. Edwards LifeSciences |
| B06 | FIX | manim | GRAPHIC | B06_BeforeAfterCount (scenes.py) | 11.74s | [was B04] 297 -> 370 count-up; +73 recovered |
| B07 | TAKEAWAY | manim | GRAPHIC | B07_Statement (scenes.py) | 8.18s | [was B05] "Silent filters don't fail loudly. They fail invisibly." |
| B08 | SIGN-OFF | manim | GRAPHIC | B08_BrandOutro (scenes.py) | 5.04s | [was B06] @HumanitariansAI brand card, "Fixed with Claude Code" |

## Lane summary
- MANIM: all 9 beats, built in this reel's own `scenes.py`. No pantry stills, no
  Remotion components, no `brutalist/` toolkit changes.
- The original plan had B00 (now B02) as a vox still and old-B02/B06
  (now B04/B08) as Remotion patterns (`ClaudeCodeDiffView`,
  `HumanitariansResearchReport`) that turned out not to exist in the
  installed toolkit; old-B03/B05 (now B05/B07) were planned as toolkit
  "card" beats, which also turned out to need a pantry/Remotion fill rather
  than being auto-rendered. All 5 were rebuilt as Manim scenes instead — see
  `BUILD-LOG.md`.
- B00/B01 added 2026-08-26 per program feedback, following the pattern
  proven in the sibling reel `2026-08-17-why-ai-generated-code-still-needs-a-human`'s
  v3 rebuild (its own `B00_TitleCard` + renumbering) — see `BUILD-LOG.md`.

## QC status (2026-08-26, against the true clean 4K master, not the review cut)
- GATE V (frame-level visual QC): **0 BLOCKER, 11 MAJOR** — identical
  count/category to the pre-rebuild 7-beat master's accepted list (5
  `underfill` beats + 1 `low-contrast` beat), now under the shifted beat IDs
  (underfill: B02/B05/B06/B07/B08; low-contrast: B03). No new defects in the
  renumbered body.
- The 2 new beats (B00, B01) initially measured `underfill` at 50%/23% of
  the safe area — genuinely new, caught before shipping. Fixed by widening
  inter-element spacing (and, for B01, font sizes) measured offline against
  real Manim text metrics; re-verified clean (0 BLOCKER, 0 MAJOR) on both
  before being folded into the full render.
- Self-assessment against `PROOF.md`'s rubric: see `SELF-ASSESSMENT.md`.
