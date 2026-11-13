# Shot list

- B00: A score needs a fair test — flow; Prediction-time information; Keep future information out; Evaluate unseen cases
- B01: Seeing the answers — compare; Test answers: 0  1  0  1; Always-zero: 2 of 4 correct; Leaked lookup: 4 of 4 correct
- B02: Leakage can hide in preparation — flow; Split raw records; Fit on training only; Transform held-out records
- B03: Three different jobs — flow; TRAIN: fit; VALIDATION: choose; TEST: final estimate
- B04: Could this exist at prediction time? — timeline; Before dispatch: known inputs; Prediction happens here; After delivery: delay reason
- B05: Match the split to the task — flow; Duplicate cases: investigate; New people: group-aware split; Forecasts: respect time
- B06: Inspect the whole path — flow; Inputs, split, then fit; Check feature availability; Review surprising scores
- B07: Keep unseen data unseen — outro; When was the feature known?; Which data influenced fitting?; Keep the final test independent

Landscape compares stages across the canvas. Portrait reflows and connects the stages vertically. Timing follows measured audio; no crop derivative.
