# Carry-Out Law

## The Carry-Out Line
> "Calibrating scores across groups with different base rates forces their error rates apart — the conflict is Bayes' rule, not a tooling gap."

## Wrong Guess Defeated
The naive belief that when two fairness audits reach contradictory conclusions on the same risk model, one of them made a statistical error, collected corrupted data, or used a biased machine learning tool.

## The Distinction That Matters
- **Statistical Conflict vs Epistemic Impossibility**: The mathematical divergence between calibration parity and equalized odds is not caused by poor engineering or unrepresentative training data. By Bayes' theorem, precision odds equal base-rate odds multiplied by error-rate ratios.
- **Forced Trade-Off**: When underlying group base rates differ, setting scores to mean the same probability across groups mathematically tilts the balance, forcing true-positive and false-positive rates to diverge.
