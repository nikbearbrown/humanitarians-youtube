# FACTCHECK — The Birthday Paradox: Three Things You Could Change

Status: **draft 2**, checked against `BEATS-DRAFT.md` as of 2026-10-16. Every spoken figure and factual claim is listed. Sources are `RESULTS.md`, `match-rates.json` (`compute_match_rates.py`, seed 2701), `cluster-rates.json` (`cluster_rates.py`), `sqrt-rule.json` (`sqrt_rule.py`), plus direct arithmetic re-run on 2026-10-16. The draft 1 table is kept in `FACTCHECK-v1.md`.

Verdicts: **OK** (matches the source), **OK-ROUNDED** (matches after the rounding stated), **FRAMING** (not a number; a characterisation to keep honest).

## 1. Figures spoken

| Beat | Spoken | Source value | Verdict |
|---|---|---|---|
| B01 | twenty three people; "about half" | uniform P(23) = 50.73% | OK-ROUNDED |
| B03 | 253 pairs | 23 × 22 / 2 = 253 | OK |
| B03 | "pile up faster than your gut expects" | pair events are not independent; do not animate as a sum | FRAMING |
| B04 | four hundred thousand groups | 400,000 trials per cell | OK |
| B04 | fifty point seven percent; exact agrees | exact 0.5073; simulated 0.5071–0.5085 | OK-ROUNDED |
| B04 | ten people about twelve percent | 11.69% | OK-ROUNDED |
| B04 | thirty: seventy one percent | 70.63% | OK-ROUNDED |
| B04 | fifty: ninety seven percent | 97.04% | OK-ROUNDED |
| B04 | fifty seven people, past ninety nine percent | n for 99% = 57; P(57) = 99.01% | OK |
| B05 | 253 other people for even odds of matching *you* | ln 0.5 / ln(364/365) = 252.65, so 253 others | OK-ROUNDED |
| B05 | with twenty two others, under six percent | 1 − (364/365)^22 = 5.86% | OK |
| B06 | years two thousand to two thousand fourteen | SSA file covers 2000–2014 | OK |
| B06 | busiest day about twelve percent above average | SSA 1.124 (with Feb 29), 1.122 (without) | OK-ROUNDED |
| B06 | Feb 29 about a quarter of a normal day, because it exists one year in four | SSA 0.246 | OK. The "one year in four" clause explains the artefact |
| B07 | fifty point eight against fifty point seven | real 50.79–50.84%; uniform 50.73% | OK-ROUNDED |
| B07 | "by a tenth of a point at most" | real minus uniform = 0.06–0.11 point | OK |
| B08 | **about ninety six percent of days sit within ten percent of average** | `sqrt-rule.json` spread: 96.4% of 365 days (Feb 29 excluded) within 0.9–1.1 of the mean | OK-ROUNDED. Replaces draft 1's "within a few percent", which was **not supported** (lowest day is 0.567 of average) |
| B09 | ninety days, ninety five point four percent | 0.9544 | OK |
| B09 | "a quarter of the calendar" | 90 / 365 = 24.7% | OK-ROUNDED |
| B09 | "coin flip to nearly certain" | 50.8% → 95.4% | FRAMING: fair |
| B10 | full year fifty point eight; half a year seventy seven; ninety days ninety five; sixty days ninety nine | 0.5084, 0.7705, 0.9544, 0.9924 | OK-ROUNDED. 180 days is "about half a year" (49.3%) |
| B10 | same month, better than ninety nine point nine percent | no-match probability 1.3e-6 (28 days) to 1.0e-5 (31 days) | OK |
| B10 | seven-day window, 23 can't avoid sharing | 23 > 7 | OK |
| B11 | 23 / 12 / 10 / 7 / 5 / 4 people for even odds at 365 / 90 / 60 / 30 / 14 / 7 days | exact smallest n with P ≥ 50% (uniform): 23, 12, 10, 7, 5, 4; real weights give the same in `cluster-rates.json` (sampled starts) | OK |
| B12 | real calendar adds "a tenth of a point at most" inside windows | differences 0.09 (180 d), 0.04 (90 d), 0.01 (60 d) | OK |
| B12 | head count moves the odds as expected; evenness barely; days decide almost everything | 12%→99% (people); 50.7%→50.8% (evenness); 50.8%→95.4% (days) | FRAMING from the numbers |
| B13 | rule: round half up of (1.2 × √days + 0.5) | `sqrt_rule.py` | defined here |
| B13 | a year gives twenty three; ninety days twelve; thirty days seven; a week four | rule 23, 12, 7, 4 = exact 23, 12, 7, 4 | OK |
| B13 | "right for every window in this film" | all seven windows (365, 180, 90, 60, 30, 14, 7) match exact | OK |
| B13 | "never more than one person off anywhere from two slots to two thousand" | `rule_vs_exact`: range 2–2000, max miss 1 (838 of 1,999 slot counts differ by one, 1,161 exact) | OK. **Do not say "always exact"** |
| B14 | school-year cohort ≈ full year, fifty point eight | a 365-day window = 0.5084 | OK as a property of the calendar model |
| B15 | twelve slots; √12 ≈ 3.46 ("about three and a half"); 1.2 × 3.46 + 0.5 = 4.66, rounds to five | `sqrt-rule.json` raw 4.66 | OK |
| B15 | four people forty three percent; five people sixty two percent (equal months) | 0.4271, 0.6181 | OK-ROUNDED |
| B16 | "half the slots, twenty five" as a tempting wrong answer | the slot count is 50 | FRAMING: a tempting error, not a sourced survey; do not say "most people" |
| B17 | √50 ≈ 7.07 ("about seven"); 1.2 × 7.07 + 0.5 = 8.99, rounds to nine | `sqrt-rule.json` raw 8.99 | OK |
| B17 | nine people fifty three percent; eight forty five percent | 0.5345, 0.4458 | OK-ROUNDED |
| B17 | "the slots set the scale, and their square root sets the crowd" | the rule | FRAMING |
| B18 | "the square root of that number is about how many it takes" | the rule is "about 1.2 times" | OK-ROUNDED. Phrase as "about"; do not drop the 1.2 on screen |

## 2. Sources and licences

| Item | Source | Licence / terms | Risk to the channel |
|---|---|---|---|
| Births by day, 1994–2003 | US NCHS (CDC), redistributed in `fivethirtyeight/data`, `births/US_births_1994-2003_CDC_NCHS.csv` | US federal statistics; repo-wide licence CC BY 4.0 (top-level `LICENSE`) | Low. Credit required if the repo licence applies |
| Births by day, 2000–2014 | US SSA, same repo, `US_births_2000-2014_SSA.csv` | same | Low. Same credit |
| Simulations, closed forms, the rule | our own `compute_match_rates.py`, `cluster_rates.py`, `sqrt_rule.py` | ours | None |
| Graphics | generated by us (grid, dots, counter, cards) | ours | None. No third-party images, text or footage |
| Political or personal content | none | n/a | None. No real individuals named |

**Caveat:** the `births/` README states no terms of its own. The top-level `LICENSE` is CC BY 4.0. The underlying counts are US government statistics. Credit as below; do not host or redistribute the CSVs in channel assets.

**Description line (required):** "Births data: US National Center for Health Statistics and Social Security Administration, via FiveThirtyEight (CC BY 4.0). Simulations and the rule check by the author."

**The rule itself.** The usual textbook form is n ≈ 1.1774 √d (+½). We use 1.2 √d + ½, rounded half up, because it is easy to say aloud and we tested it. We make no claim to have discovered it; the film calls it "a rule", and the description may add "a standard approximation".

## 3. Claims that need care

1. **B13 range claim** rests on our own check over 2–2,000 slots with equally likely slots. It says nothing about uneven slots beyond what B12 tests (a tenth of a point at most for national births).
2. **B14 (school year)** is a property of the calendar model, not a finding about real schools.
3. **B10 "same month"** is a 30-day window (28–31 uniform also above 99.99%). We have not sourced a real group with that property.
4. **B15 and B17** assume equally likely slots. Say so on screen ("equal months assumed", "random picks, equally likely").
5. **B16's wrong answer** (25) is presented as a tempting mistake, not as a measured one.
6. **Feb 29** is dropped in `cluster_rates.py` and `sqrt_rule.py` (365-day year) and kept in `compute_match_rates.py`. Both round to the same spoken figures.
7. **Seed and reproducibility.** Exact DP and closed-form values do not depend on the seed.

## 4. Re-run commands (from `Week 27/topic-video/`)

```bash
python3 -I compute_match_rates.py
python3 -I cluster_rates.py
python3 -I sqrt_rule.py
python3 -I make_read_sheet.py
```

## 5. Not covered by this file

Kokoro phonemes, graphics checks on stills, PROOF re-run on frames.
