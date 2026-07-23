# FACTCHECK — vox-calibration-curve

Source chapter: `02-probability-uncertainty-and-the-confidence-illusion.md`

## Claim-by-claim audit

| Beat | Claim | Verdict | Source / Note |
|------|-------|---------|---------------|
| B02 | "ninety-four percent accurate" | ✓ illustrative | Ch.02 exercise 11 uses exactly 94% as the example accuracy figure |
| B03 | model says 99% confident | ✓ | Ch.02: "A net will say '99%' when it should say '85%'" — 99% is the book's own example |
| B04 | accuracy and confidence are distinct claims | ✓ | Ch.02: "a model can be very accurate without being calibrated, and the difference matters" |
| B05 | 99% confidence means 99 of 100 positives | ✓ | Ch.02 calibration definition: stated probability = frequency of positives in long run |
| B06 | run held-out set, check outcomes | ✓ | Ch.02: "bin the model's stated confidences, let outcomes pile up in each bin" |
| B07 | reliability diagram axes: stated confidence vs. actual frequency | ✓ | Ch.02: "Put the model's stated probability on the horizontal axis. Put the actual frequency of positives on the vertical axis." (verbatim) |
| B07 | perfect calibration = diagonal | ✓ | Ch.02: "A perfectly calibrated model traces the diagonal — where stated and actual are equal." |
| B08 | sort predictions into confidence bins | ✓ | Ch.02: "bin the model's stated confidences, let outcomes pile up in each bin" |
| B09 | 70% → 700 of 1000 positive (calibration contract) | ✓ | Ch.02 verbatim: "If the model says 'seventy percent confident' on a thousand cases, you want roughly seven hundred of those cases to turn out positive." |
| B10 | high-confidence bins fall short of stated rate | ✓ | Ch.02: "at the extremes, especially toward the high end, it is badly overconfident" |
| B11 | curve peels away from diagonal at high end | ✓ | Ch.02: "the empirical curve peels away from the diagonal exactly where the model overclaims" |
| B12 | "A net will say '99%' when it should say '85%,' and it will say it fluently." | ✓ exact | Ch.02, calibration section (verbatim quote) |
| B13 | recap: accuracy ≠ calibration | ✓ | Summarizes ch.02 core distinction |

## Exclusion check
- ECE (expected calibration error) formula: absent ✓
- Brier score formula: absent ✓
- Temperature scaling / softmax mechanics: absent ✓
- Human-forecaster calibration: absent ✓
- Multiple models: absent ✓ (one model throughout)

## Terms table

| Term | Debuts | Need created by |
|------|--------|-----------------|
| accuracy | B02 | pre-existing viewer knowledge ✓ |
| confidence (model) | B03 (THE QUESTION) | B02 shows the accuracy score → viewer naturally wonders "how certain?" |
| calibration | B07 (mechanism) | B04–B06 establish the gap between stated confidence and actual outcomes |
| reliability diagram | B07 (mechanism) | B06–B07 establish the need for a diagnostic to see the gap |

## Numbers verification
- 94%: Ch.02 exercise 11 — vendor presents "accuracy figure of 94%". Used as motivating number ✓
- 99% / 85%: Ch.02 verbatim — "A net will say '99%' when it should say '85%'" ✓
- 70% → 700/1000: Ch.02 verbatim (calibration definition) ✓
- 5-bin visualization (0-20%, 20-40%, 40-60%, 60-80%, 80-100%): illustrative, labeled as such ✓

All numbers verified or explicitly illustrative. No unsupported claims.

## B13 — THE EXAMPLE beat (illustrative)

| Claim | Status |
|---|---|
| Medical risk model, 400 patients labeled 99% confident | illustrative — made-up instance |
| 310 of 400 actually have the condition (77%) | illustrative |
| Model said "essentially certain" — reality said less than 4 in 5 | illustrative |

All numbers in B13 are invented and illustrative. They demonstrate the calibration mechanism (high stated confidence, lower actual frequency) without claiming any specific medical study or model.
