# VISUAL QC — No Default Winner.

`yatra-no-default-winner` · frame-level pass per VISUAL QC LAW. The mp4 probe is a FILE check
and does not count — every entry below comes from reading rendered PNGs.

Master: `yatra-no-default-winner.mp4` · 3840×2160 · 162.37 s · 13/13 slots filled.

## Defects found at preview (stills) and fixed before the 4K render

| # | Beat | Defect | Severity | Fix |
|---|---|---|---|---|
| 1 | B08 CtrCall (both) | person icon read as a frowning face — editorialises customer and rep | MAJOR | redrawn as a neutral filled head-and-shoulders silhouette |
| 2 | B07 CtrSharpen | sharpened bubble ended nearly empty (one line) | MINOR | two crisp lines kept; narrow width 560→640 |
| 3 | B02 CtrUse | dead space under the two rows | MINOR | rows 250→300px apart |

## Master — frames read

Every beat at 15 / 50 / 92% of its span (`_qc/frames/B??[abc].png`, sheets `_qc/sheet0-3.png`).

| # | Check | Result |
|---|---|---|
| 1 | Edge bleed / clipping | PASS |
| 2 | Title-safe margins | PASS — all Ctr* scenes positioned from `SAFE` |
| 3 | Container overflow | PASS — long labels wrap inside their columns |
| 4 | Collision | PASS after fix 1 |
| 5 | Offscreen anchors | PASS — scale pans stay on canvas through the rock |
| 6 | Legibility | PASS — smallest type 22px eyebrow / 25px source lines at 1080p (×2 in 4K) |
| 7 | Brand bug | PASS — `@Yatra` lower-right on every Ctr* beat; composer chip and outro handle `@Yatra` |
| 8 | Aspect | PASS — 3840×2160 native (`--scale=2`), not upscaled |
| 9 | Canvas fill | PASS |

**Zero BLOCKER, zero MAJOR remaining.**

Citation audit on the frames: "Source: Capacity, October 2026" in muted ink on B02, B03, B05,
B07, B08, and in every verdict line (B10). B05 prints NO percentage — "Equally likely to
trust either one." only. B06 shows "Our read of the finding — not a survey figure."; B09 the
falsifier "'Companies haven't caught up' is interpretation, not data."

GATE T not shipped in this tree — substituted by the inspection above and the numeral sweep
in FACTCHECK.md. GATE V not used (false BLOCKERs in this tree). Logged, not silently passed.

## 9:16 cut — `short/yatra-no-default-winner-short.mp4`

2160×3840 native · 166.87 s (13 beats + 4.5 s silent endcard, under the 3:00 cap) · every
beat re-rendered from its `*916` composition, no centre-crops. END.png regenerated at
2160×3840. Render note: B08, B09 and B11 timed out on the first pass (orphaned headless
Chrome + machine load ~20); B09/B08 re-rendered after clearing processes, B11 at
concurrency 1 — frame 114 rendered in 6 s standalone, so the hang was environmental, not the
scene. Frames read at 92% of each beat (`short/_qc/sheet.png`): all content above y≈1440
and left of x≈960, `@Yatra` lower-left, no collisions, citations intact.
**Zero BLOCKER, zero MAJOR.**
