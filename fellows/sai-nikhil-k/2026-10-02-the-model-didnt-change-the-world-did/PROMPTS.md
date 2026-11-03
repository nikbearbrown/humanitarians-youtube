# PROMPTS — The Model Didn't Change. The World Did.

**There are no open generation slots in this reel.** All nine beats are
registered Remotion compositions. No image model, no stock, no paid call. A
Fellow Tier build end to end.

## B00 — the on-screen typed ask

> We shipped a model that tested well, and nobody has touched it since. Why would it be wrong a year later, and how would I know before the right answers come in?

## B07 — the handoff prompt (typed on screen and discussed in narration)

> I have a model in production. Which of its right answers won't I see for weeks? List what I can monitor today without labels — the input distributions and the model's own scores against training — and for each alarm, tell me whether to retrain, roll back, or wait.

## The executed script

| Script | Produces | Deps |
|---|---|---|
| `evidence/drift_run.py` | `drift_run.out`, `drift_run.csv` → B00, B02–B06 | Python 3.11, numpy, pandas, SciPy 1.11, scikit-learn 1.8; `data/electricity.arff` from OpenML 151 |
| `curl` + verbatim search (see `sources_check.out`) | the Huyen quotes on B01/B03 | network |
