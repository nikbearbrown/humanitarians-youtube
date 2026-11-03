#!/usr/bin/env python3
"""Reproduce every number used in this reel. Primary evidence, not a citation.

Demonstrates that permutation importance understates a feature whenever a
correlated twin is present, and that with enough twins the RANKING inverts —
a genuinely weaker feature is reported as the most important one.

Pure numpy and a ridge fit, so it runs anywhere. No scikit-learn needed.
Fixed seed: the same numbers every run.

    python3 importance_evidence.py
"""
import numpy as np

RNG = np.random.default_rng(0)
N = 6000


def z(a):
    """Standardise. Without this, scale rather than information decides the split."""
    return (a - a.mean()) / a.std()


def fit(X, y, lam=1.0):
    Xb = np.column_stack([X, np.ones(len(X))])
    return np.linalg.solve(Xb.T @ Xb + lam * np.eye(Xb.shape[1]), Xb.T @ y)


def r2(w, X, y):
    pred = np.column_stack([X, np.ones(len(X))]) @ w
    return 1 - ((y - pred) ** 2).sum() / ((y - y.mean()) ** 2).sum()


def permutation_importance(X, y, names, repeats=12):
    """Shuffle each column; importance = how much R^2 falls."""
    w = fit(X, y)
    base = r2(w, X, y)
    out = []
    for j, name in enumerate(names):
        drops = []
        for _ in range(repeats):
            Xp = X.copy()
            Xp[:, j] = RNG.permutation(Xp[:, j])
            drops.append(base - r2(w, Xp, y))
        out.append((name, float(np.mean(drops))))
    return base, out


# ── the world ───────────────────────────────────────────────────────────────
# temperature drives y two and a half times as hard as day_of_week does.
temp = RNG.normal(0, 1, N)
day = RNG.normal(0, 1, N)
y = 3.0 * temp + 1.2 * day + RNG.normal(0, 0.5, N)


def twin(i):
    """Temperature recorded again — different units, same information."""
    return z(temp * 1.8 + 32 + RNG.normal(0, 0.01, i))


print("TRUE MODEL:  y = 3.0*temp + 1.2*day + noise")
print("             temperature matters 2.5x more than day_of_week\n")

print("EXPERIMENT 1 — one twin halves the weight and quarters the importance")
for k in (1, 2):
    X = np.column_stack([twin(N) for _ in range(k)] + [z(day)])
    names = [f"temp_copy{i+1}" for i in range(k)] + ["day_of_week"]
    base, imps = permutation_importance(X, y, names)
    w = fit(X, y)
    print(f"  {k} copy(s):  each temp importance {dict(imps)[names[0]]:.4f}"
          f"   weight per copy {float(w[0]):.3f}")

print("\nEXPERIMENT 2 — enough twins and the RANKING inverts")
for k in (1, 2, 3, 4, 5):
    X = np.column_stack([twin(N) for _ in range(k)] + [z(day)])
    names = [f"temp_copy{i+1}" for i in range(k)] + ["day_of_week"]
    base, imps = permutation_importance(X, y, names)
    d = dict(imps)
    top = max(imps, key=lambda t: t[1])[0]
    flag = "   <-- WRONG FEATURE ON TOP" if top == "day_of_week" else ""
    print(f"  {k} copies: each temp {d[names[0]]:.4f}   "
          f"day_of_week {d['day_of_week']:.4f}   top = {top}{flag}")

print("\nThe real driver is temperature in every single run above.")
print("Trim the bottom of the ranking at 3 copies and you delete it.")
