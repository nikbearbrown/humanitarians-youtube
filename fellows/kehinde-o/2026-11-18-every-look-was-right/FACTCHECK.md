# FACTCHECK — Every Look Was Right

Source of record: `github.com/Kenny0bi/product-analytics-engine` at commit `0b141e1`.
Every figure **computed in this session** by `evidence_run.py` (this folder), results in
`evidence.json`. The run uses the repo's own `ABTestAnalyzer.frequentist_test` and
`SequentialTester.compute_sprt`, unmodified, against an in-memory DuckDB holding the two
tables they read (`experiments`, `experiment_assignments`). duckdb 1.5.6 was installed in
a throwaway virtual environment only.

Design: 1,000 A/A experiments (seed 7), both arms convert at 10 percent, 200 users per arm
added per look, 10 looks (2,000 per arm). alpha 0.05, beta 0.20, delta 0.02 (repo defaults).
Each sequential test stops at its first boundary crossing, either side.

| # | Claim | Beat | Verdict | Measured |
|---|---|---|---|---|
| 1 | 1,000 experiments, both versions at 10 percent, checked 10 times, 2,000 per arm | B02 | TRUE | design above |
| 2 | Check once at the end: 4.0 percent false alarms | B03 | TRUE | 40 of 1,000 |
| 3 | Check ten times, stop at first significant: 18.7 percent | B03 | TRUE | 187 of 1,000 |
| 4 | That is nearly four times the promised 5 percent | B03 | TRUE | 18.7 / 5 = 3.74 |
| 5 | Wald walls at -1.56 and 2.77 for alpha 0.05, beta 0.20 | B04 | TRUE | ln(0.2/0.95) = -1.5581; ln(0.8/0.05) = 2.7726; repo logs [-1.5581, 2.7726] |
| 6 | The repo's sequential test: 12.9 percent false alarms | B05 | TRUE | 129 of 1,000 |
| 7 | It re-estimates the control rate from the same experiment at every look | B05 | TRUE | `compute_sprt`: `theta_0 = np.mean(control_outcomes)` |
| 8 | With the control rate fixed in advance: 3.2 percent | B05 | TRUE | 32 of 1,000, theta_0 = 0.10 |

## Algebra check
On screen: Lambda_n = sum of ln P(x_i | theta_1) / P(x_i | theta_0), and
ln(beta / (1 - alpha)) < Lambda_n < ln((1 - beta) / alpha). For a binary outcome the
summand is x ln(theta_1 / theta_0) + (1 - x) ln((1 - theta_1) / (1 - theta_0)), exactly
the repo's `log_ratio_1` and `log_ratio_0`. Walls verified numerically (row 5).

## A defect in the source repository
`compute_sprt`'s docstring promises "mathematically guaranteed error-rate control". With
theta_0 re-estimated from the experiment's own control arm at each look, the measured
false-alarm rate is 12.9 percent against a 5 percent target. Reported to the author;
not changed in this reel.

## Deliberately not claimed
- Not that fixing theta_0 in advance is always possible; here it is fixed at the known true rate.
- Not that sequential testing is unreliable; the textbook version holds at 3.2 percent.

## First-person claims added in the script revision (18 Nov 2026)

The narration was rewritten to describe what I did. Each new claim about my own work traces to the record:

| Claim | Source |
|---|---|
| I checked the walls first, and they were right | Row 5 above |
| Since then, I have fixed my engine. It now compares users in pairs | product-analytics-engine `src/statistics/sequential.py`, paired two-sample SPRT on discordant pairs, fixed 18 Nov 2026 |
| On the same thousand experiments it raised false alarms 1.7 percent of the time | `python scripts/simulate_sequential.py` in that repo, Part 1 (same seed and draw order as `evidence_run.py`, which it also reproduces: 4.0, 18.7, 12.9) |
| Rebuilt to test pairs of users: 1.7 percent (on-screen, B07) | Same as above |
