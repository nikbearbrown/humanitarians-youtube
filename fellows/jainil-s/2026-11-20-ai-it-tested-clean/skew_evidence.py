"""
Evidence for "It Tested Clean" — what happens when a feature is computed one
way in training and another way at serving.

The model is never wrong here. It is fit once, on correct data, converges, and
is never retrained or touched again. The ONLY thing that changes is how one
feature is computed at the moment of prediction. Nothing raises, nothing logs,
and the offline test set keeps reporting the same score forever.

numpy only, one seed, no wall clock:

    python skew_evidence.py
"""

import json
import numpy as np

SEED = 20261120
RNG = np.random.default_rng(SEED)
N = 40_000
TRAIN_FRAC = 0.70
THRESHOLD = 0.50          # the threshold the product ships with


# ----------------------------------------------------------- tiny ML, by hand
def sigmoid(z):
    # clipped: an un-clipped exp overflows the moment a skew pushes a feature
    # far outside the range the model was fit on, which is precisely the case
    # under test.
    return 1.0 / (1.0 + np.exp(-np.clip(z, -40, 40)))


def fit_logistic(X, y, epochs=4000, lr=0.5):
    """Batch gradient descent on STANDARDISED features. Deterministic."""
    Xb = np.hstack([np.ones((len(X), 1)), X])
    w = np.zeros(Xb.shape[1])
    for _ in range(epochs):
        w -= lr * (Xb.T @ (sigmoid(Xb @ w) - y)) / len(y)
    return w


def predict(w, X):
    return sigmoid(np.hstack([np.ones((len(X), 1)), X]) @ w)


def auc(y, s):
    """Rank-based AUC, ties averaged. No sklearn."""
    order = np.argsort(s, kind="mergesort")
    ranks = np.empty(len(s), dtype=float)
    ranks[order] = np.arange(1, len(s) + 1)
    uniq, inv, counts = np.unique(s, return_inverse=True, return_counts=True)
    sums = np.zeros(len(uniq))
    np.add.at(sums, inv, ranks)
    ranks = (sums / counts)[inv]
    pos, neg = y == 1, y == 0
    return float((ranks[pos].sum() - pos.sum() * (pos.sum() + 1) / 2)
                 / (pos.sum() * neg.sum()))


def logloss(y, p):
    p = np.clip(p, 1e-9, 1 - 1e-9)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))


def psi(expected, actual, bins=10):
    """Population Stability Index — the standard 'has my input drifted?' check.
    Field rule of thumb: <0.1 no action, 0.1-0.25 investigate, >0.25 act."""
    cuts = np.quantile(expected, np.linspace(0, 1, bins + 1))
    cuts[0], cuts[-1] = -np.inf, np.inf
    e = np.clip(np.histogram(expected, cuts)[0] / len(expected), 1e-6, None)
    a = np.clip(np.histogram(actual, cuts)[0] / len(actual), 1e-6, None)
    return float(np.sum((a - e) * np.log(a / e)))


# --------------------------------------------------------------- the data
tenure = RNG.gamma(2.0, 180.0, N)                       # days
recency = RNG.gamma(1.5, 9.0, N)                        # days since last visit
spend_30d = RNG.gamma(1.2, 2.2, N) * 30 * RNG.lognormal(0, 0.35, N)   # dollars

RAW = np.column_stack([tenure, recency, spend_30d])
SPEND = 2                                               # the column that skews


def z(col):
    return (col - col.mean()) / col.std()


# The truth the label is drawn from. Written on standardised scales so the
# signal strength is explicit rather than an accident of units.
logit = -0.4 + 0.55 * z(tenure) - 0.85 * z(recency) + 1.25 * z(spend_30d)
y = (RNG.random(N) < sigmoid(logit)).astype(int)

cut = int(N * TRAIN_FRAC)
raw_tr, raw_te = RAW[:cut], RAW[cut:]
ytr, yte = y[:cut], y[cut:]

# The standardiser is fitted on TRAIN and frozen — this is the correct thing to
# do, and it is applied identically at serving. The skew is upstream of it.
mu, sd = raw_tr.mean(axis=0), raw_tr.std(axis=0)
std = lambda R: (R - mu) / sd

w = fit_logistic(std(raw_tr), ytr)
base = predict(w, std(raw_te))

offline = {
    "base_rate": float(yte.mean()),
    "majority_class_acc": float(max(yte.mean(), 1 - yte.mean())),
    "auc": auc(yte, base),
    "acc": float(((base >= THRESHOLD).astype(int) == yte).mean()),
    "logloss": logloss(yte, base),
    "mean_score": float(base.mean()),
}

print(f"seed={SEED}  n={N:,}  train={cut:,}  test={N-cut:,}")
print("\nThe model is fit ONCE, on correct data, and never touched again.")
print(f"  offline AUC      {offline['auc']:.4f}")
print(f"  offline accuracy {offline['acc']:.4f}   (threshold {THRESHOLD})")
print(f"  offline log loss {offline['logloss']:.4f}")
print("\nNow serve it. Same weights, same standardiser. One feature computed"
      " differently.\n")

spend_te = raw_te[:, SPEND].copy()


# ------------------------------------------------------- the skews
# Ordinary ways two pipelines disagree. None of them raises: every one
# produces a perfectly plausible number.
def serve_window():
    """Serving aggregates a 7-day window where training used 30."""
    return spend_te * (7.0 / 30.0)

def serve_units():
    """Serving passes cents; training was fitted on dollars."""
    return spend_te * 100.0

def serve_late():
    """Late-arriving events: at prediction time the aggregate is 70-90%
    complete. It is complete again by the time the warehouse backfills — and
    the warehouse is what the offline test reads."""
    return spend_te * RNG.uniform(0.70, 0.90, len(spend_te))

def serve_missing_fill():
    """12% of feature-store lookups miss at serving and are filled with 0,
    where training imputed the median. A miss returns a number, not an error."""
    v = spend_te.copy()
    v[RNG.random(len(v)) < 0.12] = 0.0
    return v


SKEWS = [
    ("30-day window served as 7-day", serve_window),
    ("dollars served as cents", serve_units),
    ("aggregate only 80% complete", serve_late),
    ("12% of lookups filled with 0", serve_missing_fill),
]

rows = []
print(f"  {'what changed at serving':<32}{'acc':>8}{'lost':>8}{'AUC':>8}{'PSI':>8}  drift check")
print("  " + "-" * 80)
for label, fn in SKEWS:
    served_raw = raw_te.copy()
    served_raw[:, SPEND] = fn()
    p = predict(w, std(served_raw))
    acc = float(((p >= THRESHOLD).astype(int) == yte).mean())
    a = auc(yte, p)
    ps = psi(raw_tr[:, SPEND], served_raw[:, SPEND])
    verdict = ("ALARM" if ps > 0.25 else "investigate" if ps > 0.10 else "looks fine")
    rows.append({"label": label, "acc": acc, "acc_lost_pts": (offline["acc"] - acc) * 100,
                 "auc": a, "auc_lost_pts": (offline["auc"] - a) * 100,
                 "logloss": logloss(yte, p), "psi": ps,
                 "mean_score": float(p.mean()), "drift_verdict": verdict})
    print(f"  {label:<32}{acc:>8.4f}{(offline['acc']-acc)*100:>7.1f}{'pts':<1}"
          f"{a:>8.4f}{ps:>8.3f}  {verdict}")

# ------------------------------------- where the monitoring is pointed
# PSI above was computed on the values the model ACTUALLY RECEIVED. Most
# monitoring is not wired that way: it reads the warehouse table, which is the
# same place the offline test reads. The warehouse never saw the skew, so the
# drift check it feeds is blind to every one of these by construction.
warehouse_psi = psi(raw_tr[:, SPEND], raw_te[:, SPEND])
out_monitoring = {"warehouse_psi": warehouse_psi,
                  "warehouse_verdict": "looks fine" if warehouse_psi <= 0.10 else "investigate",
                  "serving_psi": {r["label"]: r["psi"] for r in rows}}
print("\n  WHERE THE DRIFT CHECK IS POINTED")
print(f"    reading the warehouse table : PSI {warehouse_psi:.3f}  "
      f"-> same answer for ALL FOUR skews, because the warehouse never saw them")
print(f"    reading the serving log     : PSI "
      + ", ".join(f"{r['psi']:.2f}" for r in rows)
      + "  -> catches the two big ones")

worst_acc = max(rows, key=lambda r: r["acc_lost_pts"])
quietest = min(rows, key=lambda r: r["psi"])

print(f"\n  Worst accuracy loss        : {worst_acc['label']}")
print(f"                               {worst_acc['acc_lost_pts']:.1f} points, "
      f"PSI {worst_acc['psi']:.3f} ({worst_acc['drift_verdict']})")
print(f"  Quietest on the drift check: {quietest['label']}")
print(f"                               PSI {quietest['psi']:.3f} "
      f"({quietest['drift_verdict']}), and {quietest['acc_lost_pts']:.1f} points lost")

print(f"\n  Mean predicted probability, offline: {offline['mean_score']:.4f}")
for r in rows:
    print(f"    {r['label']:<34}{r['mean_score']:.4f}  "
          f"({r['mean_score']-offline['mean_score']:+.4f})")

out = {"seed": SEED, "n": N, "threshold": THRESHOLD, "offline": offline,
       "monitoring": out_monitoring,
       "skews": rows, "worst_accuracy": worst_acc, "quietest_drift": quietest}
with open("skew_results.json", "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=2)
print("\nwrote skew_results.json")
