# VISUAL QC — Paid to Be Quoted.

`yatra-paid-to-be-quoted` · frame-level pass per VISUAL QC LAW. Every entry comes from reading rendered PNGs.

Masters:
- `yatra-paid-to-be-quoted.mp4` · 3840×2160 · 163.29 s · 12/12 slots filled
- `short/yatra-paid-to-be-quoted-short.mp4` · 2160×3840 · 167.79 s · 13/13 slots (incl. 4.5 s silent endcard, regenerated natively at 2160×3840)

Both native 4K via `--scale=2` — not upscaled. Full-resolution crop (`_qc/crop4k.png`) confirms clean type edges.

## Defects found at preview (stills) and fixed before the 4K render

| # | Beat | Aspect | Defect | Severity | Fix |
|---|---|---|---|---|---|
| 1 | B05 PqLicense | 16:9 | "one blanket license" label crowded the AI-companies box | MINOR | label moved below the line, wrapped to the hub–box gap |
| 2 | B05 PqLicense916 | 9:16 | converging lines ran through the "more than 3,000" label; NONPROFIT chip sat on the license line | MAJOR | count block moved above the field; chip moved left of the hub |
| 3 | B08 PqLimits916 | 9:16 | title wrapped to an orphaned "yet" | MINOR | title shortened to "What we know so far" (both aspects) |

## Frames read
16:9: every beat at 15/50/90% (`_qc/sheet_B00.png`, `_qc/sheet_B04.png`, `_qc/sheet_B08.png`). 9:16: every beat at 50/93% (`short/_qc/sheetP0-2.png`).

| # | Check | Result |
|---|---|---|
| 1 | Edge bleed / clipping | PASS |
| 2 | Title-safe margins | PASS — all Pq* scenes positioned from `SAFE` / `SAFE916` |
| 3 | Container overflow | PASS — long labels wrap inside their boxes |
| 4 | Collision | PASS after fixes 1–3 |
| 5 | Offscreen anchors | PASS |
| 6 | Legibility | PASS — smallest type 22px eyebrow / 25px source lines at 1080p (×2 in 4K) |
| 7 | Brand bug | PASS — `@Yatra` on every Pq* beat (lower-right 16:9, lower-left 9:16), composer chip, outro, endcard |
| 8 | Aspect | PASS — native 3840×2160 and 2160×3840 |
| 9 | Canvas fill | PASS — open space under B04's left column and right of B05's labels judged acceptable; verdict card (B09) mid-frame, standard |

**Zero BLOCKER, zero MAJOR remaining.** No review markers visible in either master.

Citation audit: The AI Marketers, November 19, 2026 on B04 and B05; BrightEdge, via Agile Brand Guide, November 19, 2026 on B06; per-layer sources on B07; both on B08 and in the verdict (B09).

GATE T not shipped in this tree — substituted by the inspection above and the numeral sweep in FACTCHECK.md. Logged, not silently passed.
Advisory: compile.py `graphic` 12/12 over the ~40% pantry cap — same as every @Yatra episode.
