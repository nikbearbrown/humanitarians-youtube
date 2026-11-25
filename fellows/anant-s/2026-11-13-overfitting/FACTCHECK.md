# FACTCHECK — Overfitting, When a Perfect Score Lies

Verdicts: ✓ verified · minor (true with a qualifier) · CORRECTED (was wrong in draft, fixed) · WRONG.
"Executed" means the number was produced by `demo/overfit_demo.py`; the run is in `demo/RUN-LOG.txt`.
Script hash: sha256 `ae1c6faf…3069`. Evidence hash: `4c615e57…2113` (two consecutive runs byte-identical).
Data hashes (from RUN-LOG): train `bc87dff8cdf7bbff`, test `ff1b37a661e82694`.

| # | Beat | Claim | Verdict | Source / check | Fix |
|---|---|---|---|---|---|
| 1 | B01, BVDT | A perfect training score **can** mean memorized noise | CORRECTED | The draft verdict line said "usually means". A zero training error is not proof of overfitting: noise-free data, or very large models that interpolate and still generalize ("benign overfitting", double descent; Belkin et al. 2019), are real counter-cases. | Verdict line now reads "can mean", matching B01's correction, which never claimed more |
| 2 | B00, B04 | A degree-15 polynomial (16 coefficients) can pass through 16 points | ✓ executed | Unique interpolating polynomial through n points with distinct x has degree ≤ n−1. The demo asserts that training MSE is below 1e-9; the logged value is 0. | — |
| 3 | B02 | Data: true curve sin(πx) on [−1, 1], Gaussian noise sd 0.2, 16 train / 1,000 test, same distribution | ✓ executed | `setup` block in evidence.json; seed 15 | — |
| 4 | B02, B05 | The noise floor is 0.04: no model can beat it on average | ✓ | Expected test MSE = σ² + (bias² + variance) ≥ σ² = 0.04. Executed: the true curve itself scores 0.0402 on this test set. | — |
| 5 | B03 | MSE = (1/n) Σ (yᵢ − f̂(xᵢ))². Squaring makes misses above and below both count, and big misses count most. | ✓ | Standard definition (Hastie, Tibshirani & Friedman, *ESL* §2.4; James et al., *ISL* §2.2.1) | — |
| 6 | B03 | Worked term: the line's worst miss has gap −1.032, squared 1.065; sum 4.546 ÷ 16 = 0.284 | ✓ executed | `mse_example`. The demo asserts that it equals the degree-1 training MSE. That one point is 23% of the sum, which illustrates "big misses count most". | — |
| 7 | B04 | Degree 1: about 0.28 training, 0.27 test | ✓ executed | 0.2841 / 0.2728 | — |
| 8 | B04 | Degree 3: about 0.06 training, 0.047 test | ✓ executed | 0.0586 / 0.0471 | — |
| 9 | B04 | Degree 15: training 0, test "almost ten thousand" | ✓ executed | 0 / 9,882.6. `make_sheet.py` asserts 9,500 ≤ value < 10,000. | — |
| 10 | B05 | Training error only ever goes down as the degree rises | ✓ executed + proof | Nested least-squares models on the same data can't fit worse; the demo asserts it. Flat steps at 1→2 and 8→9 are real, because sin(πx) is odd and the even terms add almost nothing. "Never goes up" is literally true. | Narration says "only ever goes down"; the flat steps are visible on screen. Reviewer may prefer "never goes up". |
| 11 | B05 | Test error bottoms out "around degree three to six, just above" the floor | ✓ executed | Seed 15: degrees 3/4/5/6 = 0.0471/0.0489/0.0466/0.0467, minimum at degree 5. Across 500 fresh datasets the median-best is degree 3. Degrees 3, 5 and 6 are a near-tie, so the narration names a range rather than a winner. | — |
| 12 | B05 | The test curve "leaves the chart" | ✓ executed | Y axis 0–0.6; degree 11 = 1.83, then 26.4, 5,807.1, 8,251.1, 9,882.6 | — |
| 13 | B05 | "same shape across 500 fresh datasets" (on-screen chip) | ✓ executed | `sweep_500` median test MSE falls to degree 3 and then rises monotonically. Degree 14–15 values above 10⁶ come from near-singular fits and are not shown. | — |
| 14 | B06 | At 20 points, degree-15 test error is "about twenty-nine"; at 100, 0.048; at 1,000, 0.041 | ✓ executed | 28.776 / 0.0476 / 0.0413. Training sets are nested: n = 16 is exactly the B04 dataset, and the demo asserts it. | — |
| 15 | B06 | Training error "has risen from zero to meet it" | ✓ executed | Training MSE 0 → 0.0414 at n = 1,000, against test 0.0413 | — |
| 16 | B06 | The degree-15 ladder improves monotonically with n | minor | True for this nested draw (9,882.6 → 28.8 → 0.130 → 0.098 → 0.048 → 0.047 → 0.041). For other draws the small-n steps can wobble. The narration speaks only the n = 20 / 100 / 1,000 rungs. | — |
| 17 | B06 | "Complexity alone isn't the problem. Complexity the data can't pin down is." | ✓ (framing) | Estimation variance grows with parameters per data point (*ESL* §7.3, bias–variance). This is a standard framing, not a measured claim. | — |
| 18 | B07 | Picking by validation score and then reporting it: optimistic "seven times in ten" | ✓ executed | 69.6% of 1,000 trials; median reported 0.0439 vs real 0.0508. Selection-induced optimism: Cawley & Talbot 2010; *ESL* §7.10. | — |
| 19 | B07 | Reporting on an untouched test set lands "about half and half, as an honest score should" | minor | 55.2% optimistic, and the medians match (0.0506 vs 0.0508). It isn't exactly 50% because a 20-point MSE is right-skewed (median below mean). The control, a model fixed in advance, shows the same skew at 53.3% and is on screen as a reference chip. | Kept the wording; the chip shows the control. |
| 20 | B07 | Draft said the peeked score "beat the noise floor four times in ten" | CORRECTED | Dropped. An honest 20-point score also dips below 0.04 about half the time, so that statistic shows skew, not selection bias. | Replaced with the controlled optimistic-share comparison |
| 21 | BHTF | Rubric: "Training error should never go up as the degree rises" | ✓ checked | A naive `np.polyfit` version over 200 seeds shows 0 seeds with a rise above 1e-6. | — |
| 22 | BHTF | Rubric: degree 15 "should score essentially zero in training and something enormous on test" | CORRECTED | With naive `np.polyfit`, training MSE has median 1e-18 but reaches 0.0047 on an ill-conditioned seed. Test MSE is at least 15.8 across 200 seeds. | Draft said "zero"; now "essentially zero", and the on-screen check reads "≈ 0" |

## Algebra checks (MATH-TYPESETTING.md)
- **Bound index:** i runs from 1 to n inside the sum. Nothing outside the sum carries i. n is the number of points in whichever set is being graded: 16 for training, 1,000 for test.
- **Sign:** (yᵢ − f̂(xᵢ))² is symmetric in sign, so reading it as "real minus guess" is harmless. The worked gap is negative (−1.032) and its square is positive (1.065).
- **Hat:** f̂ is the fitted model, not the true f. The true curve is never written as f̂.
- **"=" is a definition** here. Narration reads it as "is".
- **Numeric case:** Σ = 4.5461 and 4.5461 / 16 = 0.28413 = the degree-1 training MSE ✓ (asserted in code).
- **Degree vs coefficients:** degree d has d + 1 coefficients, so degree 15 has 16 ✓.
- **Basis note:** fits use numpy's Legendre series, which spans exactly the polynomials of degree ≤ d. That makes the least-squares fit identical to the monomial one but well conditioned. Polynomials are never written in Legendre form on screen.
