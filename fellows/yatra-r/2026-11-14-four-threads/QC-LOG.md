# VISUAL QC — Four Threads.

`yatra-four-threads` · frame-level pass per VISUAL QC LAW. Every entry comes from reading rendered PNGs.

Masters:
- `yatra-four-threads.mp4` · 3840×2160 · 159.81 s · 12/12 slots filled
- `short/yatra-four-threads-short.mp4` · 2160×3840 · 164.31 s · 13/13 slots (incl. 4.5 s endcard)

Both native 4K via `--scale=2` — not upscaled.

## Defects found and fixed (re-rendered, re-read)

| # | Beat | Aspect | Defect | Severity | Fix |
|---|---|---|---|---|---|
| 1 | B01 WkBluf | 16:9 | a fourth line (scene is built for three) landed at the very end and collided with the closer | MAJOR | merged to three lines: "Explainer built · new project discussed"; closer "Two closed. One under way." |
| 2 | B02, B07 WkShip916 | 9:16 | connector wire ran through the MADE / NEXT chip; chip centred only for one word length | MINOR | `WeekGordy916.tsx`: chip gets a stage-colour backing and is centred with translateX(-50%) |

## Frames read
16:9: every beat at 20/55/92% (`_qc/sheet0-2.png`, `_qc/B01_fix.png`). 9:16: every beat at 50/93%
(`short/_qc/sheetP0-2.png`), chip crops (`short/_qc/chips.png`), compiled-master spot frames
(`short/_qc/masterSpot.png`) confirming no review markers and the @Yatra endcard.

| # | Check | Result |
|---|---|---|
| 1 | Edge bleed / clipping | PASS |
| 2 | Title-safe margins | PASS |
| 3 | Container overflow | PASS |
| 4 | Collision | PASS after fixes 1, 2 |
| 5 | Offscreen anchors | PASS |
| 6 | Legibility | PASS |
| 7 | Brand bug | PASS — `@Yatra` on every Wk* beat, composer chip, outro and endcard |
| 8 | Aspect | PASS — native 3840×2160 and 2160×3840 |
| 9 | Canvas fill | PASS — verdict card (B09) sits mid-frame with open space, standard for ClaudeVerdictArtifact |

**Zero BLOCKER, zero MAJOR remaining.**

Advisory: compile.py `graphic` 12/12 beats over the ~40% pantry cap — same as every @Yatra weekly.
