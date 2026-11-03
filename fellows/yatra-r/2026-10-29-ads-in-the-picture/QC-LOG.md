# VISUAL QC — Ads in the Picture.

`yatra-ads-in-the-picture` · frame-level pass per VISUAL QC LAW. The mp4 probe is a FILE
check and does not count — every entry below comes from reading rendered PNGs.

Master: `yatra-ads-in-the-picture.mp4` · 3840×2160 · 173.96 s · 13/13 slots filled.

## Defects found at preview (stills) and fixed before the 4K render

| # | Beat | Defect | Severity | Fix |
|---|---|---|---|---|
| 1 | B01 AdpBluf (16:9) | top rail's bend cut through the "T" of "The helper is getting agents." | MAJOR | rail lines set at 76px so the right-aligned line starts clear of the centre bend |
| 2 | B01 AdpBluf916 | bend crossed "is" in the second line | MAJOR | both lines set first; rails run beneath them, so no bend crosses text |
| 3 | B06 AdpDots (both) | dot label sat under the pulse ring and the wires/connector ran through it | MAJOR | label moved above the dot (16:9) / beside it above the wire (9:16) |
| 4 | B08 AdpChannel | "?" clipped the final "s" of "AI conversations"; dead space under row | MAJOR / MINOR | "?" moved up and down-sized; slots 330→390px |
| 5 | B04 AdpCanvas916 | two-line title ran into the window | MAJOR | window starts 76px lower, image 440→380px |
| 6 | B05 AdpRoom916 | dead space under the reframe | MINOR | frame 560→480px, reframe lines 84→100px |
| 7 | B06 (both) | lit tile field read as a heavy dark block | MINOR | lit fill 0.5→0.3 |

## Master — frames read

Every beat at 15 / 50 / 92% of its span (`_qc/frames/B??[abc].png`, sheets `_qc/sheet0-3.png`).

| # | Check | Result |
|---|---|---|
| 1 | Edge bleed / clipping | PASS |
| 2 | Title-safe margins | PASS — all Adp* scenes positioned from `SAFE` |
| 3 | Container overflow | PASS — B04 ad label wraps inside its column |
| 4 | Collision | PASS after fixes 1–4 |
| 5 | Offscreen anchors | PASS |
| 6 | Legibility | PASS — smallest type 22px eyebrow / 24–25px source & caption lines at 1080p (×2 in 4K) |
| 7 | Brand bug | PASS — `@Yatra` lower-right on every Adp* beat; composer footer chip `@Yatra`; outro handle `@Yatra` |
| 8 | Aspect | PASS — 3840×2160 native (`--scale=2`), not upscaled |
| 9 | Canvas fill | PASS |

**Zero BLOCKER, zero MAJOR remaining.**

Citation audit on the frames: "Source: Jumpfly, October 2026" renders in muted ink on B02,
B04, B06, B09 and inside every verdict line (B10). B04 shows its "Redrawn (simplified)…
not OpenAI's design" caption; B05 its "Illustrative messages" caption; B06 its "Tiles
illustrative — not to count." note. The only figure on any frame is "over 4,000".

Note: the shared composer component shows its default model chip ("Fable 5 · High") — same
as every prior reel in this series; left as is.

GATE T: `scripts/type_check.py` is not shipped in this tree — substituted by the inspection
above and the numeral sweep in FACTCHECK.md. GATE V: not used (false BLOCKERs in this tree,
per prior reels). Logged, not silently passed.

## 9:16 cut — `short/yatra-ads-in-the-picture-short.mp4`

2160×3840 native · 178.46 s (13 beats + 4.5 s silent endcard, under the 3:00 cap) · every
beat re-rendered from its `*916` composition, no centre-crops. END.png regenerated at
2160×3840 (shorts.py writes 1080×1920). Frames read at 92% of each beat
(`short/_qc/sheet.png`): all content above y≈1440 and left of x≈960, `@Yatra` lower-left,
no collisions, citations intact. **Zero BLOCKER, zero MAJOR.**
