# FACTCHECK — The Birthday Paradox: Three Tests of One Claim

Status: draft 1, checked against `BEATS-DRAFT.md` (712 words). Every spoken figure and factual claim is listed. Sources are `RESULTS.md`, `match-rates.json` (from `compute_match_rates.py`, seed 2701) and `cluster-rates.json` (from `cluster_rates.py`), plus direct arithmetic re-run on 2026-10-16.

Verdicts: **OK** (matches the source), **OK-ROUNDED** (matches after rounding stated), **FRAMING** (not a number; a characterisation to keep honest), **FIXED** (wording changed in the draft because of this check).

## 1. Figures spoken

| Beat | Spoken | Source value | Verdict |
|---|---|---|---|
| B01 | twenty three people | n = 23 | OK |
| B01 | "about half" of the time | uniform P(23) = 50.73% | OK-ROUNDED |
| B03 | twenty three people make two hundred and fifty three pairs | 23 × 22 / 2 = 253 (exact) | OK |
| B03 | "pile up faster than your gut expects" | pairs are not independent, so the chance is not a sum of pair chances | FRAMING: informal; do not show an addition on screen |
| B04 | four hundred thousand groups | 400,000 trials per cell in `compute_match_rates.py` | OK |
| B04 | fifty point seven percent | uniform exact 0.5073; simulated 0.5071–0.5085 across cells | OK-ROUNDED |
| B04 | "the exact calculation says the same" | exact vs simulated agree to about 0.1 point in every cell | OK |
| B04b | ten people: about twelve percent | uniform P(10) = 11.69% | OK-ROUNDED. **FIXED:** was "one chance in eight" (12.5%) |
| B04b | thirty: seventy one percent | 0.7063 | OK-ROUNDED |
| B04b | fifty: ninety seven | 0.9704 | OK-ROUNDED |
| B04b | by fifty seven the odds pass ninety nine percent | n for 99% = 57; P(57) = 0.9901 | OK |
| B12b | across a whole year, twenty three | `n_for_50pct` = 23 (uniform and real) | OK |
| B12b | 90 / 60 / 30 / 14 / 7-day windows: twelve / ten / seven / five / four | `people_for_50pct_range` in `cluster-rates.json`: [12,12], [10,10], [7,7], [5,5], [4,4] (sampled at every 15th start day) | OK. Note: sampled starts, not all 365; the range is a single value at every width tested |
| B05 | two hundred and fifty three other people for even odds of matching *you* | ln 0.5 / ln(364/365) = 252.65, so 253 others | OK-ROUNDED. **FIXED:** added "other" |
| B05 | with twenty two others, under six percent | 1 − (364/365)^22 = 5.86% | OK |
| B06 | years two thousand to two thousand fourteen | SSA file covers 2000–2014 | OK |
| B06 | "busiest day about twelve percent above average" | SSA 1.124 (with Feb 29), 1.122 (without); NCHS 1.117 / 1.115 | OK-ROUNDED |
| B06 | "February twenty ninth about a quarter of a normal day" | SSA 0.246; NCHS 0.206 (about a fifth) | OK for SSA; if NCHS is also named on screen, say "a fifth to a quarter" |
| B08 | fifty point eight percent | real calendars: 50.79–50.84% | OK-ROUNDED |
| B08 | "up from fifty point seven" | uniform 50.73% | OK-ROUNDED |
| B08 | "a tenth of a point at most" | real minus uniform = 0.06–0.11 point | **FIXED** (was "about a tenth"; one cell is 0.11) |
| B07→B08 | call "a few tenths", result "one" | see above | FRAMING: reword both together if the call changes |
| B10 | ninety days | window W = 90 | OK |
| B10 | "above ninety percent" (the call) | a prediction, not a claim | OK |
| B11 | ninety five point four percent | 0.9544 real; 0.9540 uniform | OK |
| B11 | "a quarter of the calendar" | 90 / 365 = 24.7% | OK-ROUNDED |
| B11 | "coin flip to nearly certain" | 50.8% → 95.4% | FRAMING: fair; avoid "certain" |
| B12 | full year: fifty point eight | 0.5084 | OK |
| B12 | half a year: seventy seven | 180 days = 49.3% of a year; 0.7705 | OK-ROUNDED (180 days is "about half a year") |
| B12 | ninety days: ninety five | 0.9544 | OK-ROUNDED |
| B12 | sixty days: ninety nine | 0.9924 | OK-ROUNDED |
| B12 | same month: better than ninety nine point nine percent (spoken; true value above 99.999%) | no-match probability for 23 people: 28 days 1.3e-6, 30 days 5.6e-6, 31 days 1.0e-5, so match ≥ 99.999% in every real month length (uniform within month) | OK |
| B12 | seven-day window, 23 people can't avoid sharing | 23 > 7 (pigeonhole) | OK |
| B13 | real calendar inside windows adds "a tenth of a point at most" | differences: 180 d 0.09, 90 d 0.04, 60 d 0.01 point | OK. **FIXED:** was "about a tenth" |
| B14 | school year with a cutoff still contains every day once, so about fifty point eight | a 365-day window = 0.5084; the model, not a study | OK as a property of the calendar. See §3 |

## 2. Sources and licences

| Item | Source | Licence / terms | Risk to the channel |
|---|---|---|---|
| Births by day, 1994–2003 | US NCHS (CDC), redistributed in `fivethirtyeight/data`, `births/US_births_1994-2003_CDC_NCHS.csv` | US federal statistics; repo-wide licence CC BY 4.0 (top-level `LICENSE`) | Low. Credit required if the repo licence applies. |
| Births by day, 2000–2014 | US SSA, same repo, `US_births_2000-2014_SSA.csv` | same | Low. Same credit. |
| Simulations and closed-form probabilities | our own `compute_match_rates.py`, `cluster_rates.py` | ours | None |
| Graphics | generated by us (grid, dots, counters) | ours | None. No third-party images, text, rosters or footage |
| Political or personal content | none | n/a | None. No real individuals named |

**Caveat to keep honest:** the `births/` folder README states no terms of its own. The top-level `LICENSE` is CC BY 4.0. The underlying counts are US government statistics. Safest practice is to credit as below and not to host or redistribute the CSVs in the channel's assets.

**Description line (required):** "Births data: US National Center for Health Statistics and Social Security Administration, via FiveThirtyEight (CC BY 4.0). Simulations by the author."

## 3. Claims that need care

1. **B14 (school year).** True of the calendar model: a window that spans the whole year has the same day weights as the full calendar. It is not a finding about real schools, whose births also depend on cutoffs and enrolment. Keep the phrasing about "a cohort with a cutoff date still contains every day of the calendar".
2. **"Same month" in B12.** The result is for a window of 30 days with real weights (and 28–31 uniform). It applies to a group whose members are all born in one calendar month. We have not sourced a real group like that and the film must not imply one exists.
3. **B13 "the real calendar adds a tenth of a point at most."** Holds for random draws within a window using national weights. It does not cover groups with other kinds of clustering (twins, family structure, scheduled births).
4. **Feb 29.** Dropped in `cluster_rates.py` (365-day year); kept in `compute_match_rates.py`. The film's B12 values come from the dropped version, B04/B08 from either. Both round to the same spoken figures.
5. **Seed and reproducibility.** `compute_match_rates.py` uses a fixed seed; exact DP values do not depend on it.

## 4. Re-run commands (from `Week 27/topic-video/`)

```bash
python3 -I compute_match_rates.py
python3 -I cluster_rates.py
```

## 5. Not covered by this file

Repo uniqueness for the "predict before running" form (BEATS-DRAFT open item 5), the read-aloud style pass, PROOF, and any on-screen graphics checks.
