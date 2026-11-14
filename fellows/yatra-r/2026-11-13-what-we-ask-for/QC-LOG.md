# VISUAL QC — What We Ask For.

`yatra-what-we-ask-for` · frame-level pass per VISUAL QC LAW. The mp4 probe is a FILE check and
does not count — every entry below comes from reading rendered PNGs.

Masters:
- `yatra-what-we-ask-for.mp4` · 3840×2160 · 253.72 s · 18/18 slots filled
- `short/yatra-what-we-ask-for-short.mp4` · 2160×3840 · 253.72 s · 18/18 slots filled (no endcard)

Both native 4K via `--scale=2` — not upscaled.

## Defects found and fixed (re-rendered, re-read)

| # | Beat | Aspect | Defect | Severity | Fix |
|---|---|---|---|---|---|
| 1 | B08 WwaPremium | 16:9 | "20–40% more" ran past the right title-safe edge | MAJOR | unit 720, value placed beside bar end, nowrap |
| 2 | B03 WwaEarnings | 16:9 | in-chart labels collided with the dashed "expected" line | MAJOR | labels moved to a legend under the axis; dashed path clipped to the plot |
| 3 | B14 WwaLimits | 16:9 | list type undersized for 4K viewing | MINOR | item font 38, wider columns |
| 4 | B04 WwaAdoption | 9:16 | people rows overlapped label and note | MAJOR | smaller figures, row spacing 450, note/source moved down |
| 5 | B09 WwaDisclose | 9:16 | italic note overlapped the Article 50 card | MAJOR | note 1290 / source 1380 |
| 6 | B10 WwaLoop | 9:16 | bypass arc cut through "Some workflows" label | MAJOR | nodes dropped 30px, label raised 10px |
| 7 | B13 WwaFork | 9:16 | closer overlapped the second IF card | MAJOR | closer moved to 1190 |

## Frames read

16:9: every beat at 15/50/92% (`_qc/sheet0-2.png`). 9:16: every beat at 50/92%
(`short/_qc/sheetA.png`, `sheetP0-2.png`, `sheetFix.png`), plus compiled-master spot frame
(`short/_qc/master120.png`) confirming no review markers.

| # | Check | Result |
|---|---|---|
| 1 | Edge bleed / clipping | PASS |
| 2 | Title-safe margins | PASS — Wwa* scenes laid out from `SAFE` / `SAFE916` |
| 3 | Container overflow | PASS after fixes 1, 5 |
| 4 | Collision | PASS after fixes 2, 4, 6, 7 |
| 5 | Offscreen anchors | PASS |
| 6 | Legibility | PASS after fix 3 |
| 7 | Brand bug | PASS — `@Yatra` lower-right (16:9) / lower-left above the platform keep-out (9:16); composer chip and outro handle `@Yatra` |
| 8 | Aspect | PASS — native 3840×2160 and 2160×3840 |
| 9 | Canvas fill | PASS — some open space below 9:16 content kept clear of the platform UI keep-out (y > 1440) |

**Zero BLOCKER, zero MAJOR remaining.**

## Advisories (logged, not acted on)

- compile.py motion histogram: `graphic` 18/18 beats, over the ~40% pantry cap. Same as prior
  @Yatra ai-explainer episodes — every body beat is a bespoke data scene by design.
- 9:16 SKIN LINT flags `ClaudeComposerAsk916` / `ClaudeTitleOutro916` as not matching the
  16:9 law names — expected: shorts.py rewires to the 916 twin of the same pattern.

Citation audit: every figure beat carries its source in muted ink — Gallup, May 2026 (B03–B05);
AI Buzz, 2026 (B08); Envato 2026, via AI Buzz (B09); Creativepool, 2026 (B10, B12);
RI Study Post, 2026 (B13); all on B14 and in the verdict (B15).
