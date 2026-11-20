# FACTCHECK — The Patients Who Left Early

Source of record: `github.com/Kenny0bi/cancer-survival-prediction` at commit `9528c10`.
Every figure was **computed in this session** (docs/EXECUTABLE-EVIDENCE.md) by
`evidence_run.py` in this folder; results in `evidence.json`.

How: the repo's `SyntheticCancerDataset(n_patients=5000, seed=42)` generates the cohort.
Its `_generate_outcomes` computes each patient's true Weibull event time, then keeps only
the observed time and event flag. `evidence_run.py` subclasses it with an identical copy
of that method that also stores the true time, and **asserts the subclass's observed
times and flags equal the repo's, element for element**, before using it.

| # | Claim | Beat | Verdict | Measured |
|---|---|---|---|---|
| 1 | 5,000 synthetic patients | B02 | TRUE | n = 5000 |
| 2 | 1,458 leave before their outcome is observed, 29 percent | B02 | TRUE | 1,458 censored, 0.2916 |
| 3 | The generator knows every true survival time | B02 | TRUE | `true_time` in `_generate_outcomes` |
| 4 | True median survival 51.4 months | B03 | TRUE | median of all 5,000 true times |
| 5 | Dropping the censored gives 32.8 | B03 | TRUE | median observed time among events |
| 6 | That is a year and a half too low | B03 | TRUE | 51.4 - 32.8 = 18.6 months |
| 7 | Counting them as deaths gives 43.4 | B03 | TRUE | median of all observed times |
| 8 | Kaplan-Meier gives 51.1, 0.3 from the truth | B03 | TRUE | product-limit median |
| 9 | A patient can only be censored while still alive | B04 | TRUE | event = true_time <= censor_time |
| 10 | 425 left before five years; 286 of them were alive at five years | B04 | TRUE | counted against true times |
| 11 | Five-year survival: truth 45.2%, KM 45.0%, dropped 26.5%, as-death 39.5% | (FACTCHECK only) | TRUE | evidence.json |

## Algebra check (MATH-TYPESETTING.md)
On screen: S-hat(t) = product over event times t_i <= t of (1 - d_i / n_i), with d_i the
deaths at t_i and n_i the patients still followed (at risk) at t_i. Censored patients are
at risk at their own censoring time. Numerical check in `evidence_run.py`: times 1, 2, 3,
4, 5 with time 2 censored give S = 4/5, then 4/5 x 2/3, then x 1/2, then 0, matched exactly.

## Deliberately not claimed
- Not that Kaplan-Meier is always unbiased; it assumes independent censoring, true here by design.
- No real patient data.

## First-person claims added in the script revision (18 Nov 2026)

The narration was rewritten to describe what I did. Each new claim about my own work traces to the record:

| Claim | Source |
|---|---|
| I built the project on synthetic patients so models could be checked against known answers | Repo README: hazard ratios embedded by the author |
