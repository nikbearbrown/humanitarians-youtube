# Script — Why Data Leakage Can Make a Model Look Better Than It Really Is

Narrator: Liam / Kokoro `am_onyx`, speed 1.0. New revision; human narration review pending.

## B00 — A score needs a fair test

An impressive score can be a warning. Data leakage happens when model development uses information that should be unavailable for the prediction being evaluated. This is Liam, narrating for Deepa. Let us see why a model can look excellent on paper and still disappoint on genuinely new cases.

## B01 — Seeing the answers

Imagine four fictional test cases. Their answers are zero, one, zero, one. A deliberately simple predictor always says zero, so it gets two right. Now let a lookup see the test answers and repeat them. It gets all four right, but that is memorization of the test, not evidence of generalization.

## B02 — Leakage can hide in preparation

The same problem can hide in preprocessing. If you learn an imputation value, a scaling rule, or which features to keep from the entire dataset, your held-out data influence development. Split first, then fit learned transformations within the training portion. Apply the fitted transformation to held-out data without fitting it again.

## B03 — Three different jobs

Training data fit the model. Validation data help compare choices and tune settings. The final test set estimates performance after those decisions are settled. Repeatedly tuning against the test set turns it into another development set. Cross-validation also needs preprocessing fitted separately inside each training fold.

## B04 — Could this exist at prediction time?

Suppose a fictional model predicts whether a delivery will be late. A field recorded after delivery, such as a final delay reason, would reveal information the live prediction could not know. Check when every feature becomes available, not just whether it appears in the spreadsheet.

## B05 — Match the split to the task

Related records can also undermine a split. Copies of the same case in training and testing make the test less independent. For predictions about new people, consider separating people into groups. For forecasting, respect time order. The right split depends on the intended use; random splitting is not always appropriate.

## B06 — Inspect the whole path

A pipeline helps keep fitted transformations together with the model. It does not automatically repair future-derived features or a poorly chosen split. Document data sources, feature availability, split rules, and tuning decisions. A surprising score should trigger investigation, rather than an automatic celebration or an automatic accusation of leakage.

## B07 — Keep unseen data unseen

Try this on your next project: choose one feature and ask when it became available. Then trace which records influenced preprocessing, tuning, and the final test. Why Data Leakage Can Make a Model Look Better Than It Really Is: a trustworthy score needs a trustworthy evaluation. Liam, narrating for Deepa, for Humanitarians AI.
