# VISUAL QC — Film the Impossible.

`yatra-film-the-impossible` · frame-level pass per VISUAL QC LAW. Every entry comes from reading rendered PNGs.

Masters:
- `yatra-film-the-impossible.mp4` · 3840×2160 · 134.43 s · 11/11 slots filled
- `short/yatra-film-the-impossible-short.mp4` · 2160×3840 · 138.93 s · 12/12 slots (incl. 4.5 s silent endcard, regenerated natively at 2160×3840)

Both native 4K via `--scale=2` — not upscaled (`_qc/crop4k.png`).

## Defects found at preview (stills) and fixed before the 4K render

| # | Beat | Aspect | Defect | Severity | Fix |
|---|---|---|---|---|---|
| 1 | B02 FtAnatomy | 16:9 | "You" label clipped off the first card (art area overflowed) | MAJOR | art area gets `minHeight: 0` + overflow hidden |
| 2 | B02 FtAnatomy916 | 9:16 | output phone frame ran into the closer line | MINOR | phone moved up and shortened |
| 3 | B04 FtScenes | both | wolf silhouettes too small to read | MINOR | wolves scaled up ~35% |
| 4 | B01 FtBluf | 16:9 | dead space under an undersized film strip | MINOR | strip and type enlarged |

## Frames read
16:9: every beat at 15/50/92% (`_qc/sheet0-2.png`). 9:16: every beat at 50/93% (`short/_qc/sheetP0-2.png`).

| # | Check | Result |
|---|---|---|
| 1 | Edge bleed / clipping | PASS |
| 2 | Title-safe margins | PASS — all Ft* scenes positioned from `SAFE` / `SAFE916` |
| 3 | Container overflow | PASS after fix 1 |
| 4 | Collision | PASS after fix 2 |
| 5 | Offscreen anchors | PASS |
| 6 | Legibility | PASS — smallest type 18px chip (scene frames) / 25px source at 1080p (×2 in 4K) |
| 7 | Brand bug | PASS — `@Yatra` on every Ft* beat (lower-right 16:9, lower-left 9:16), composer chip, outro, endcard |
| 8 | Aspect | PASS — native 3840×2160 and 2160×3840 |
| 9 | Canvas fill | PASS — open space under B05/B07 lists judged acceptable; verdict card (B08) standard |

**Zero BLOCKER, zero MAJOR remaining.** No review markers visible in either master.

Citation audit: Remake the Trend, November 17, 2026 on B04, B05, B07 and every verdict line (B08). No figures anywhere.

Build note: renders stalled mid-session because iCloud had offloaded ~13,400 toolkit files (low disk). Files were
re-downloaded and orphaned headless-Chrome processes cleared before the final render.

GATE T not shipped in this tree — substituted by the inspection above and the numeral sweep in FACTCHECK.md.
