# FACTCHECK — vox-subgroup-hidden

Source: `computational-skepticism-for-ai/chapters/11-communicating-uncertainty-calibrating-claims-to-evidence.md`

## Terms table

| Term | Definition used in video | Chapter reference |
|---|---|---|
| Aggregate calibration | A global metric computed across all patients — a size-weighted average of subgroup calibration values | Lines 187–189 |
| Subgroup calibration | Calibration computed separately for a defined patient population (demographic, severity, etc.) | Lines 193, 195–199 |
| Size-weighting / absorption | Small subgroups contribute little to the global ECE, so their miscalibration is masked | Lines 187–189 |
| Global ECE | Expected Calibration Error averaged across all cases — low value does not guarantee subgroup calibration | Lines 189, 199 |
| Reliability diagram | Plot of mean confidence vs mean accuracy per bin; subgroup deviations visible only when plotted separately | Line 193 |

## Claim-by-claim check

| Beat | Claim | Chapter support | Status |
|---|---|---|---|
| B02 | Hospital model passes global calibration; subgroup check reveals elderly ECE is more than 2× global | Lines 201–206 (elderly subgroup ECE 0.044 vs global 0.018; flag criterion > 2×) | PASS |
| B04 | Aggregate = size-weighted average; large group drowns small; global ECE can be low while subgroup fails | Lines 187–189 | PASS |
| B05 | On reliability diagram, small group's curve dissolves into aggregate | Lines 170, 189, 193 | PASS |
| B07 | Rare-disease subgroup (95 cases) outnumbered — tiny weight, high ECE stays invisible in aggregate | Lines 200–206: rare-disease N=95, subgroup ECE 0.103 vs global 0.018 | PASS |
| B08 | Quote verbatim | Line 189: "The single most important limitation of aggregate calibration metrics is that they are aggregate..." | PASS |
| B09 | Fix: separate reliability diagram and ECE per named subgroup | Line 193 | PASS |
| B10 | Quote verbatim | Line 193: "The aggregate metric is evidence the model is calibrated on average. It is not evidence the model is calibrated for the patient in front of you." | PASS |
| B11 | If max subgroup ECE substantially exceeds global ECE, aggregate conceals a real problem | Lines 199–200 | PASS |

| B12 | Insurance model: overall ECE 0.03 hides elderly rural subgroup (8%) ECE 0.21; claims 18% over-prediction | ILLUSTRATIVE — numbers invented to demonstrate mechanism; labeled illustrative | ILLUSTRATIVE |

## VERDICT: PASS
