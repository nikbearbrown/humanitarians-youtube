# Stills QC, Week 27 (2026-10-16)

18 review stills in `_stills/` (`B01-16x9.png` to `B18-16x9.png`), each 3840×2160, drawn by `build_slates.py` (standalone Pillow; house palette and the bundled EB Garamond and Inter fonts, both OFL). One still per beat, at the moment of assertion. 16:9 only; there is no Short for this film.

## Built vs. checked

| Check | Result |
|---|---|
| Every number on a slate computed from the data files or exact formulas, not typed | **Yes.** `checks()` in `build_slates.py` asserts the slate values against every figure the narration speaks (50.7 / 50.8, 12 / 71 / 97 / 99, 253, 5.9, +12%, 25%, 51 / 77 / 95 / 99, 23 / 12 / 10 / 7 / 5 / 4, 43 / 62, 53 / 45) and passes |
| Math laid out structurally (real radical, fraction bar, sized parentheses) | **Yes** in B03, B13, B15, B16, B17, B18. Not the toolkit's `typeset_math.py`: it needs matplotlib, which is not installed here (`ModuleNotFoundError` in every Python on this machine). The slates use a small structural layout in Pillow instead of a text fallback. Algebra checked separately by `sqrt_rule.py`. If you prefer the toolkit renderer, install matplotlib and I will swap it in |
| Source line on every figure-bearing beat | **Yes** (bottom-left, 22 px at 1080p scale). B06 also carries the NCHS/SSA credit as a held line; B18 repeats it in the end card |
| Side-by-side at the moment of comparison | B05, B07, B09 (95.4% beside full year 50.8%), B12 (95.44 vs 95.40), B15 (43% vs 62%), B17 (53% vs 45%, 25 struck) |
| Library-first rule (toolkit CLAUDE.md rule 8) | `./art scenes` was run for the calendar grid and for typeset math. No component covers the grid, dots, curve or tables; `TypesetMath` exists but needs matplotlib. So the grid, dots, curve, tables and cards are bespoke. Precedent: Weeks 20–22 built bespoke pipelines |
| Brand strings | none: no handle, no toolkit scene component, no default props |
| Defects found by looking, fixed | strip text touching the card border (all strip beats); B02 duplicated strip; B01 duplicated caption; B04 labels crossing the curve and each other; B06 callout on top of a label; B08 bar drawing error; B12 layout; B13 formula overlapping label and "round halves up", missing check glyphs (drawn instead), unsized parentheses; B14 label on the big number; B15 text running off the page; B17 53.5% vs spoken "fifty three" (whole percents now) |

## Not done (needs the next stage)

- **No motion.** These are the assertion-moment frames only. Reveals (dots dropping, counter climbing, band shrinking) are not animated yet.
- **Not yet checked on frames:** equation states at 15% / 50% / 85% of each beat (the toolkit math rule), phone-width legibility, and the 8 s hold in B16 (a static start state is shown).
- **B01 and B09 dot layouts** are illustrations from fixed seeds (2701, 2702), labelled "Not data" on screen.
- **Kokoro audio not generated.** Phonemes checked only (`PHONEMES-CHECK.md`).

## Rebuild

```bash
/opt/homebrew/bin/python3.12 build_slates.py          # all 18
/opt/homebrew/bin/python3.12 build_slates.py B13 B16  # some
```

## Review round 1 (Tanmay, 2026-10-16): three fixes, all applied
1. **B03** denominator "2" moved lower, away from the fraction bar. Applied to every fraction (B13, B15, B16, B17, B18 changed with it); caption spacing below it adjusted (B03, B16).
2. **B04** the 99% label sat under the 97% label. The plot now has headroom above 100%; both labels sit above their dots, 50 people on the left and 57 people on the right, in reading order.
3. **B12** the small captions ("even days → real calendar", etc.) were tight against the big readings. Cards are taller and the captions sit lower; the three verdict lines moved down to match.
Everything else was marked fine by Tanmay.

## PROOF round 1 on the stills: three MAJOR flags fixed
1. **Type size:** every sans label is now ≥24 px (1080p scale); source lines are 26 px. Month labels 17→24, axis ticks 19→24, table headers and chapter labels 20–22→24. Left chart margins and several layouts were adjusted to fit.
2. **Source-line position:** source baselines now keep the text at least 100 px from the bottom edge (was 52). B06's credit line, B13's tally, B16's countdown bar and B18's end card moved up to match.
3. **Accent contrast:** small accent text uses `#B5532F` (4.7:1 on cream); large accent numerals and verdicts use `#C6613F` (3.85:1); inactive chapter-card text uses the soft ink (4.7:1). Borders, bars and fills keep the house accent.
`check_onscreen.py` now enforces all of this on every run (min type, contrast per text colour, bottom margin ≥ 90 px) plus the spoken-figures check: 0 violations, all spoken figures present.
