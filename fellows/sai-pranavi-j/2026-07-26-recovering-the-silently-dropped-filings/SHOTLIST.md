# SHOTLIST — The Pipeline That Was Lying to Me
## Total: 88.5s (measured, audio-locked 2026-07-26) · 7 beats · all Manim, no pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | HOOK | manim | GRAPHIC | B00_CalmDashboard (scenes.py) | 9.70s | Calm feed log — SEC/FINRA/CFTC/FedReg rows ticking in, cursor dot tracking down; nothing looks wrong |
| B01 | SETUP | manim | GRAPHIC | B01_PipelineDiagram (scenes.py) | 26.81s | 5 feeds (SEC, FINRA, CFTC, FedReg-Sec., FedReg-CFTC) -> normalize -> score -> Postgres -> email alert; filter callout |
| B02 | DISCOVERY | manim | GRAPHIC | B02_ClaudeCodeDiff (scenes.py) | 18.79s | Dark code panel, diff view highlighting the removed `content isNotEmpty` filter node |
| B03 | PROOF | manim | GRAPHIC | B03_RecoveredFilings (scenes.py) | 8.23s | List-reveal: Cboe Clear U.S. / MEMX LLC / Nasdaq GEMX SRO notice / US v. Edwards LifeSciences |
| B04 | FIX | manim | GRAPHIC | B04_BeforeAfterCount (scenes.py) | 11.74s | 297 -> 370 count-up; +73 recovered |
| B05 | TAKEAWAY | manim | GRAPHIC | B05_Statement (scenes.py) | 8.18s | "Silent filters don't fail loudly. They fail invisibly." |
| B06 | SIGN-OFF | manim | GRAPHIC | B06_BrandOutro (scenes.py) | 5.04s | @HumanitariansAI brand card, "Fixed with Claude Code" |

## Lane summary
- MANIM: all 7 beats, built in this reel's own `scenes.py`. No pantry stills, no
  Remotion components, no `brutalist/` toolkit changes.
- The original plan had B00 as a vox still and B02/B06 as Remotion patterns
  (`ClaudeCodeDiffView`, `HumanitariansResearchReport`) that turned out not to
  exist in the installed toolkit; B03/B05 were planned as toolkit "card"
  beats, which also turned out to need a pantry/Remotion fill rather than
  being auto-rendered. All 5 were rebuilt as Manim scenes instead — see
  `BUILD-LOG.md`.

## QC status (2026-07-26, against the clean master, not the review cut)
- GATE V (frame-level visual QC): **0 BLOCKER**. One real issue found and
  fixed (B01's rightmost stage box sat just past the title-safe margin).
- Remaining: 11 MAJOR `underfill` notes (B00, B03, B04, B05, B06 read as
  visually sparse relative to the frame) and a mild `low-contrast` note on
  B01. Cosmetic polish, not correctness — optional follow-up.
