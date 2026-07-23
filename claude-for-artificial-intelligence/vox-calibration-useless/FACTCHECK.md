# FACTCHECK — vox-calibration-useless

Source: `computational-skepticism-for-ai/chapters/11-communicating-uncertainty-calibrating-claims-to-evidence.md`

## Terms table

| Term | Definition used in video | Chapter reference |
|---|---|---|
| Calibration | Agreement between stated confidence and observed frequency — when the model says 60%, it's right 60% of the time | Lines 120, 158, 304 |
| Discrimination (resolution) | Whether the model predicts different values for different cases; captures whether the model is useful for individual decisions | Lines 138, 140, 304 |
| Base-rate predictor | A model that returns the overall outcome rate for every case — perfectly calibrated but unable to differentiate patients | Lines 140, 304 |
| Reliability diagram | A calibration plot showing mean confidence on x-axis vs mean accuracy on y-axis — a perfectly calibrated model falls on the diagonal | Lines 170–171 |
| ECE (Expected Calibration Error) | Weighted average gap between predicted confidence and actual accuracy across bins; 0 = perfect calibration | Lines 152, 158 |

## Claim-by-claim check

| Beat | Claim | Chapter support | Status |
|---|---|---|---|
| B02 | A model that always returns the base rate achieves perfect calibration but is useless for individual decisions | Lines 140, 304 | PASS |
| B04 | Calibration measures stated confidence vs observed frequency; constant base-rate predictor passes this test | Line 120, 304 | PASS |
| B05 | Calibration does not measure whether outputs are useful for decisions; discrimination is a separate axis | Lines 138, 140 | PASS |
| B07 | On reliability diagram, perfect calibration = on diagonal; base-rate predictor piles all dots on one point | Lines 170, 304 | PASS |
| B08 | Quote (condensed) | Line 304: "A model with perfect calibration but no resolution (predicting the base rate for every instance) has ECE = 0 and is completely useless for triage." | PASS |
| B09 | Need both calibration and discrimination; a single aggregate score collapses both | Lines 138–140, 304 | PASS |
| B10 | Quote verbatim | Line 140: exact | PASS |
| B11 | Plot reliability diagram, check whether predictions spread across range | Lines 170–177, 193 | PASS |

## B12 — THE EXAMPLE beat (illustrative)

| Claim | Status |
|---|---|
| Bank fraud detection model assigned to flag suspicious transactions | illustrative — made-up instance |
| Model outputs 2.1% for every transaction (the base rate) | illustrative |
| ECE = 0 (perfectly calibrated) | illustrative |
| $5 coffee purchase and $10,000 international wire receive identical output | illustrative |
| Fraud team cannot flag anything useful | illustrative |

All numbers and scenario in B12 are invented and illustrative. They demonstrate the calibration-without-discrimination failure (ECE = 0, no signal for individual decisions) without claiming any specific financial institution or model.

## VERDICT: PASS
