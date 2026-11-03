# Carry-Out

## The Carry-Out Sentence
"An aggregate calibration score doesn't tell you the model is safe for every patient — it tells you the majority is drowning out the vulnerable."

## Wrong Guess Defeated
"If a predictive AI model demonstrates low Expected Calibration Error across the entire evaluation cohort, its predicted probabilities can be trusted for any individual patient."

## Falsifying Case
The Epic Sepsis Model — a proprietary clinical alert system deployed across hundreds of hospitals — showed acceptable aggregate calibration and developer-reported AUC between 0.76 and 0.83 across the broad population.

When Wong et al. (2021) independently validated the system at Michigan Medicine across 27,697 patients and 38,455 hospitalizations:
- AUC dropped to 0.63
- Positive Predictive Value was only 12% (88% false alarm rate)
- The model missed 67% of sepsis cases (1,709 of 2,552 patients who developed sepsis)

Because calibration metrics are size-weighted sums, the healthy majority and routine cases mathematically drown out severe miscalibration in smaller, vulnerable clinical subgroups. The aggregate score looked acceptable while the model was failing two out of three septic patients.
