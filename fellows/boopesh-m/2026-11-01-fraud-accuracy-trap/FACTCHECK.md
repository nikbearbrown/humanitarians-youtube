# FACTCHECK — The 99.9% Accuracy Trap (Boopesh M., AI fraud detection)

Sources and how strongly each claim is backed:

- **[KAGGLE-DESC]** = the Kaggle dataset description of "Credit Card Fraud Detection" (`kaggle.com/datasets/mlg-ulb/creditcardfraud`).
  Kaggle itself is **blocked** in the build container. The description was read verbatim from a public copy,
  `raw.githubusercontent.com/SetCodesToFire/fraud-detection/master/README.md` (fetched 2026-11-01): *"collected and
  analysed during a research collaboration of Worldline and the Machine Learning Group (http://mlg.ulb.ac.be) of ULB
  (Université Libre de Bruxelles) … transactions made by credit cards in September 2013 by european cardholders …
  occurred in two days, where we have 492 frauds out of 284,807 transactions … the positive class (frauds) account
  for 0.172% of all transactions."* The same figures appeared in WebSearch summaries of a Zenodo copy of the dataset.
- **[IEEE]** = WebSearch result for the IEEE Xplore record (document 7376606) of the paper. The page itself was not opened.
- **[RUN]** = output of `code/fraud_trap.py` in this folder (`code/results.json`, `code/curves.npz`, `code/run.log`).
  **Synthetic data**, said on screen (B00 composer, B30, B50, B60, B70, outro) and in narration (B00, B30, B50, B70).
- **[MATH]** = arithmetic checked below.

| Beat | Claim | Source | Status |
|---|---|---|---|
| B00 | 492 frauds in 284,807 card transactions; ULB + Worldline dataset | [KAGGLE-DESC] | ✅ (read from a verbatim copy, not from kaggle.com) |
| B00/B30 | "a model that always says legit scores 99.8% and catches nothing" | [RUN] always_legit accuracy 0.99827, caught 0/148 | ✅ |
| B10 | "fraud is 1 in 580" | [MATH] 284,807 / 492 = 578.9 → "about 1 in 580" | ✅ (rounded to nearest ten) |
| B20 | real card transactions, European cardholders, Sept 2013, two days | [KAGGLE-DESC] | ✅ |
| B20 | 0.172 % | [KAGGLE-DESC] 0.172 %; [MATH] 492/284,807 = 0.17275 % (shown truncated, as in the description) | ✅ |
| B20 | dataset associated with Dal Pozzolo, Caelen, Johnson & Bontempi, "Calibrating Probability with Undersampling for Unbalanced Classification", IEEE Symposium Series on Computational Intelligence (SSCI), Cape Town, Dec 2015 | [IEEE] title, authors, venue confirmed by search result for the IEEE Xplore record; the Kaggle page asks users to cite this paper (from memory of the Kaggle page + search summaries listing Dal Pozzolo et al. among the dataset's references) | ⚠️ citation link Kaggle→paper not read directly; one slide deck labels it "IEEE CIDM 2015" (CIDM is a symposium inside SSCI) |
| B30 | synthetic data, same size and fraud rate as the real dataset | [RUN] make_classification n=284,807, 492 positives (0.17275 %), seed 42 | ✅ |
| B30 | test set: 85,443 transactions, 148 frauds (stratified 30 %) | [RUN] | ✅ |
| B40 | four boxes for the lazy model: caught 0, false alarms 0, missed 148, legit let through 85,295 | [RUN] | ✅ |
| B40 | recall = caught/(caught+missed); precision = caught/(caught+false alarms) | standard definitions (TP/(TP+FN), TP/(TP+FP)) | ✅ |
| B40 | lazy model precision is undefined (no alarms) | [RUN] sklearn returns 0 with zero_division=0; film shows "n/a" in B50 | ✅ |
| B50 | logistic regression: 99.90 % accurate, catches 66 of 148, 2 false alarms, recall 45 %, precision 97 % | [RUN] 0.99902 / 66 / 2 / 0.446 / 0.971 | ✅ |
| B50 | gradient boosting: 99.90 % accurate, catches 127, 68 false alarms, recall 86 %, precision 65 % | [RUN] 0.99896 / 127 / 68 / 0.858 / 0.651 | ✅ |
| B50 | "nearly twice the fraud" | [MATH] 127/66 = 1.92 (shown "1.9×") | ✅ |
| B60 | PR curves of both models | [RUN] curves.npz (sklearn precision_recall_curve on test scores); average precision 0.779 (boosted), 0.589 (logistic) — not spoken | ✅ |
| B60 | cutoff 0.9 → 126 caught, 49 false alarms; 0.01 → 136 caught, 189 false alarms | [RUN] threshold_sweep_boosted | ✅ |
| B60 | if a miss costs 50× a false alarm, cheapest cutoff 0.015 → 136 caught, 173 false alarms (cost 773 vs 1,118 at 0.5 vs 7,400 for "always legit") | [RUN] cost grid 0.005…0.95 step 0.005; **the 50:1 cost ratio is an illustrative assumption, labelled on screen** | ✅ (assumption) |
| B70 | real systems use far more signals; fraudsters change their tricks over time | general domain knowledge / editorial (concept drift is a well-known fraud-detection issue) | opinion, labelled as a limit |
| B80 | prompt asks the viewer to rerun with a 10:1 cost ratio | not answered in the film | — |

Not used (⚠️): search summaries say the Kaggle description recommends the Area Under the Precision–Recall Curve over
confusion-matrix accuracy. That sentence was not in the copy read, so it is not claimed on screen.

## Arithmetic checks
- 492 / 284,807 = 0.0017275 = 0.17275 %; 1 / 0.0017275 = 578.9.
- Lazy model accuracy = 85,295 / 85,443 = 0.998268 → 99.8 % (B30), 99.83 % (B50).
- Logistic: (66 + 85,293) / 85,443 = 0.999017 → 99.90 %. Boosted: (127 + 85,227) / 85,443 = 0.998958 → 99.90 %.
- Boosted at 0.5: precision 127/195 = 0.651; recall 127/148 = 0.858. Cost at 0.5 = 50·21 + 68 = 1,118; at 0.015 = 50·12 + 173 = 773.

## Experiment details (all [RUN])
sklearn 1.9.1 `make_classification(n_samples=284807, n_features=10, n_informative=4, n_redundant=2,
n_clusters_per_class=2, weights=[1−492/284807], flip_y=0, class_sep=2.0, random_state=42)`; stratified 70/30 split
(seed 42). Models: always-legit; StandardScaler + LogisticRegression (max_iter 2000); HistGradientBoostingClassifier
(200 iterations, lr 0.1, 15 leaves, seed 42). Also logged, not shown: logistic with balanced class weights at 0.5
catches 123 but raises 8,775 false alarms (accuracy 89.7 %). A first run with class_sep = 1.0 is kept in
`code/run_first_try_class_sep_1.0.log` (much harder data: the boosted model caught 54 of 148).
