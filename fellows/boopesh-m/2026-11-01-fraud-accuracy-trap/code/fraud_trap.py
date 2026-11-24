"""The 99.9% Accuracy Trap -- executable evidence for Boopesh M.'s explainer.

SYNTHETIC data: sklearn make_classification, seed-locked, with the SAME size and fraud rate as the
widely used Kaggle / ULB credit-card dataset (492 frauds in 284,807 transactions = 0.172%).
The real dataset is not used (Kaggle is not reachable from the build container).

Models: (1) "always legit" baseline, (2) logistic regression, (3) small gradient-boosted trees.
Reports on a held-out stratified 30% test set: accuracy, precision, recall, frauds caught/missed,
false alarms; the precision-recall curve; and a threshold sweep with an illustrative cost rule.

Run:  python fraud_trap.py      -> results.json, curves.npz, run.log (stdout)
"""
import json
import time
from pathlib import Path

import numpy as np
import sklearn
from sklearn.datasets import make_classification
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, average_precision_score, confusion_matrix,
                             precision_recall_curve, precision_score, recall_score)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

SEED = 42
N = 284_807                      # same size as the real dataset
REAL_FRAUDS = 492
FRAUD_RATE = REAL_FRAUDS / N     # 0.001727...
MISS_COST, ALARM_COST = 50.0, 1.0   # illustrative: a missed fraud costs 50x a false alarm
HERE = Path(__file__).resolve().parent


def report(name, y, pred):
    tn, fp, fn, tp = confusion_matrix(y, pred, labels=[0, 1]).ravel()
    r = {"model": name,
         "accuracy": accuracy_score(y, pred),
         "precision": precision_score(y, pred, zero_division=0),
         "recall": recall_score(y, pred, zero_division=0),
         "caught": int(tp), "missed": int(fn), "false_alarms": int(fp), "true_legit": int(tn),
         "flagged": int(tp + fp)}
    print(f"{name:34s} acc {r['accuracy']:.5f}  prec {r['precision']:.3f}  rec {r['recall']:.3f}  "
          f"caught {tp:4d}  missed {fn:4d}  false alarms {fp:5d}")
    return r


def main():
    t0 = time.time()
    X, y = make_classification(
        n_samples=N, n_features=10, n_informative=4, n_redundant=2, n_repeated=0,
        n_clusters_per_class=2, weights=[1 - FRAUD_RATE], flip_y=0.0, class_sep=2.0,
        random_state=SEED)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=SEED)
    print(f"sklearn {sklearn.__version__}  rows {N}  frauds {int(y.sum())}  rate {y.mean():.5%}")
    print(f"train {len(ytr)} rows / {int(ytr.sum())} frauds   test {len(yte)} rows / {int(yte.sum())} frauds")

    res = {"setup": {
        "synthetic": True, "generator": "sklearn.datasets.make_classification",
        "sklearn_version": sklearn.__version__, "seed": SEED, "n_rows": N,
        "n_frauds": int(y.sum()), "fraud_rate": float(y.mean()),
        "real_dataset_reference": {"rows": N, "frauds": REAL_FRAUDS, "rate": FRAUD_RATE,
                                   "one_in": N / REAL_FRAUDS},
        "params": {"n_features": 10, "n_informative": 4, "n_redundant": 2, "n_clusters_per_class": 2,
                   "class_sep": 2.0, "flip_y": 0.0, "weights": [1 - FRAUD_RATE]},
        "test_size": 0.3, "test_rows": int(len(yte)), "test_frauds": int(yte.sum()),
        "train_rows": int(len(ytr)), "train_frauds": int(ytr.sum()),
        "cost_rule": {"miss_cost": MISS_COST, "false_alarm_cost": ALARM_COST,
                      "note": "illustrative assumption, not from any bank"}}}

    # (1) the lazy model
    res["always_legit"] = report("always legit", yte, np.zeros_like(yte))

    # (2) logistic regression, default threshold 0.5
    lr = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))
    lr.fit(Xtr, ytr)
    p_lr = lr.predict_proba(Xte)[:, 1]
    res["logistic"] = report("logistic regression @0.5", yte, (p_lr >= 0.5).astype(int))
    res["logistic"]["average_precision"] = average_precision_score(yte, p_lr)

    # (2b) logistic regression with balanced class weights
    lrw = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000, class_weight="balanced"))
    lrw.fit(Xtr, ytr)
    p_lrw = lrw.predict_proba(Xte)[:, 1]
    res["logistic_balanced"] = report("logistic, balanced weights @0.5", yte, (p_lrw >= 0.5).astype(int))
    res["logistic_balanced"]["average_precision"] = average_precision_score(yte, p_lrw)

    # (3) small gradient-boosted trees
    hgb = HistGradientBoostingClassifier(max_iter=200, learning_rate=0.1, max_leaf_nodes=15,
                                         random_state=SEED)
    hgb.fit(Xtr, ytr)
    p_hgb = hgb.predict_proba(Xte)[:, 1]
    res["boosted"] = report("gradient boosting @0.5", yte, (p_hgb >= 0.5).astype(int))
    res["boosted"]["average_precision"] = average_precision_score(yte, p_hgb)
    print(f"average precision  logistic {res['logistic']['average_precision']:.3f}  "
          f"balanced {res['logistic_balanced']['average_precision']:.3f}  "
          f"boosted {res['boosted']['average_precision']:.3f}")

    # threshold sweep + cost rule on the boosted model's scores
    sweep = []
    for th in [0.9, 0.7, 0.5, 0.3, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005]:
        r = report(f"gradient boosting @{th}", yte, (p_hgb >= th).astype(int))
        r["threshold"] = th
        r["cost"] = MISS_COST * r["missed"] + ALARM_COST * r["false_alarms"]
        sweep.append(r)
    res["threshold_sweep_boosted"] = sweep
    grid = np.round(np.arange(0.005, 0.951, 0.005), 3)
    costs = [MISS_COST * int(((p_hgb < th) & (yte == 1)).sum()) + ALARM_COST * int(((p_hgb >= th) & (yte == 0)).sum())
             for th in grid]
    best = float(grid[int(np.argmin(costs))])
    res["cost_best"] = report(f"gradient boosting @{best} (min cost)", yte, (p_hgb >= best).astype(int))
    res["cost_best"]["threshold"] = best
    res["cost_best"]["cost"] = float(min(costs))
    res["cost_at_0.5"] = float(MISS_COST * res["boosted"]["missed"] + ALARM_COST * res["boosted"]["false_alarms"])
    res["cost_always_legit"] = float(MISS_COST * res["always_legit"]["missed"])
    print(f"cost rule (miss={MISS_COST}, alarm={ALARM_COST}): best threshold {best}  cost {min(costs):.0f}  "
          f"vs @0.5 {res['cost_at_0.5']:.0f}  vs always-legit {res['cost_always_legit']:.0f}")

    arrays = {}
    for key, p in (("logistic", p_lr), ("boosted", p_hgb)):
        pr, rc, th = precision_recall_curve(yte, p)
        arrays[f"{key}_precision"], arrays[f"{key}_recall"], arrays[f"{key}_thresholds"] = pr, rc, th
    arrays["cost_grid"], arrays["cost_values"] = grid, np.array(costs, dtype=float)
    np.savez_compressed(HERE / "curves.npz", **arrays)
    res["runtime_s"] = round(time.time() - t0, 1)
    (HERE / "results.json").write_text(json.dumps(res, indent=2) + "\n")
    print(f"wrote results.json, curves.npz in {res['runtime_s']} s")


if __name__ == "__main__":
    main()
