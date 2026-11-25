# VISUAL QC — Be the Sentence.

`yatra-be-the-sentence` · frame-level pass per VISUAL QC LAW. The mp4 probe is a FILE check and
does not count — every entry below comes from reading rendered PNGs.

Master: `yatra-be-the-sentence.mp4` · 3840×2160 · 172.29 s · 14/14 slots filled.

## Defects found at preview (stills) and fixed before the 4K render

| # | Beat | Defect | Severity | Fix |
|---|---|---|---|---|
| 1 | B04 GeoGap (both aspects) | bracket's dashed drop line from the 43% bar end cut through row two's label | MAJOR | drop line now starts at row two's track, below the label |
| 2 | B09 GeoSplit (9:16) | single connector ran through the stacked chips | MINOR | portrait draws one connector to the first chip only |

## Master — frames read

Every beat at 15 / 50 / 92% of its span (`_qc/frames/B??[abc].png`, sheets `_qc/sheet0-2.png`),
plus a full-resolution crop (`_qc/crop4k.png`) confirming native 4K edges.

| # | Check | Result |
|---|---|---|
| 1 | Edge bleed / clipping | PASS |
| 2 | Title-safe margins | PASS — all Geo* scenes positioned from `SAFE` |
| 3 | Container overflow | PASS — long labels wrap inside their columns |
| 4 | Collision | PASS after fix 1 |
| 5 | Offscreen anchors | PASS |
| 6 | Legibility | PASS — smallest type 22px eyebrow / 25px source lines at 1080p (×2 in 4K) |
| 7 | Brand bug | PASS — `@Yatra` lower-right on every Geo* beat; composer chip and outro handle `@Yatra` |
| 8 | Aspect | PASS — 3840×2160 native (`--scale=2`), not upscaled |
| 9 | Canvas fill | PASS — minor open space under B08 strip / B10 lists, judged acceptable |

**Zero BLOCKER, zero MAJOR remaining.**

Citation audit: each figure beat shows its own source in muted ink — Peec AI, April 2026 (B02);
Peec AI (B03); ConvertMate/QuickSEO, 2026 (B04); Mersel/Marketing.chat, 2026 (B05); GEO research
paper — Princeton, Georgia Tech, Allen Institute for AI (KDD 2024) (B07); Seer
Interactive/ConvertMate, 2026 (B08); Erlin, 2026 (B09); all six on B10 and in the verdict (B11).
B04 prints no gap number; B09 kind chips carry no numbers.

GATE T not shipped in this tree — substituted by the inspection above and the numeral sweep in
FACTCHECK.md. Logged, not silently passed.

## 9:16 cut — `short/yatra-be-the-sentence-short.mp4`

2160×3840 native · 176.79 s (14 beats + 4.5 s silent endcard, under the 3:00 cap) · every beat
re-rendered from its `*916` composition (Geo* scenes re-band to a stacked layout), no centre-crops.
END.png regenerated at 2160×3840. Frames read at 92% of each beat (`short/_qc/sheet.png`): all
content above y≈1440 and left of x≈960, `@Yatra` lower-left, no collisions, citations intact.
**Zero BLOCKER, zero MAJOR.**
