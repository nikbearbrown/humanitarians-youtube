"""Executable evidence for "Overfitting, When a Perfect Score Lies".

Every number shown on screen in this film comes from this file's output
(demo/RUN-LOG.txt + demo/evidence.json). Pure Python + numpy, seeded, no ML libraries.
Run:  python demo/overfit_demo.py

Model family: polynomials of degree d (d+1 coefficients), fitted by ordinary least squares.
Basis: numpy's Legendre series on the data domain [-1, 1]. It spans exactly the same
polynomials as 1, x, ..., x^d but is far better conditioned, so the degree-15 fit is
numerically trustworthy. Error measure: mean squared error (MSE).
"""
import hashlib
import json
import platform
import sys
import warnings
from pathlib import Path

import numpy as np
from numpy.polynomial import Legendre

OUT = Path(__file__).resolve().parent
ev = {"python": sys.version.split()[0], "numpy": np.__version__, "platform": platform.platform()}

SEED = 15            # the film's one dataset (chosen before looking at results; logged in SOURCES.md)
SIGMA = 0.2          # noise standard deviation -> irreducible test MSE = SIGMA**2 = 0.04
N_TRAIN = 16         # 16 points: a degree-15 polynomial (16 coefficients) can pass through all of them
N_TEST = 1000
DEGREES = list(range(16))


def truth(x):
    return np.sin(np.pi * x)


def draw(rng, n):
    x = rng.uniform(-1, 1, n)
    return x, truth(x) + rng.normal(0, SIGMA, n)


def fit(x, y, d):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return Legendre.fit(x, y, d, domain=[-1, 1])


def mse(p, x, y):
    return float(np.mean((p(x) - y) ** 2))


def r(v, nd=4):
    return round(float(v), nd)


ev["setup"] = {"truth": "sin(pi*x)", "domain": [-1, 1], "noise_sd": SIGMA, "noise_floor_mse": SIGMA ** 2,
               "n_train": N_TRAIN, "n_test": N_TEST, "seed": SEED, "basis": "Legendre (same span as 1..x^d)"}

# ---- 1. The one dataset --------------------------------------------------------------
rng = np.random.default_rng(SEED)
xtr, ytr = draw(rng, N_TRAIN)
xte, yte = draw(rng, N_TEST)
ev["data"] = {"train": [[r(a), r(b)] for a, b in zip(xtr, ytr)],
              "test_preview": [[r(a), r(b)] for a, b in zip(xte[:60], yte[:60])],
              "hash_train": hashlib.sha256(np.round(np.c_[xtr, ytr], 12).tobytes()).hexdigest()[:16],
              "hash_test": hashlib.sha256(np.round(np.c_[xte, yte], 12).tobytes()).hexdigest()[:16]}
# noise actually present in this test set (what even the true curve scores)
ev["setup"]["truth_test_mse"] = r(np.mean((truth(xte) - yte) ** 2))
ev["setup"]["truth_train_mse"] = r(np.mean((truth(xtr) - ytr) ** 2))

# ---- 2. Worked example: degree 1, 3, 15 ----------------------------------------------
grid = np.linspace(-1, 1, 201)
ev["grid"] = [r(g, 3) for g in grid]
ev["truth_curve"] = [r(v) for v in truth(grid)]
ev["worked"] = {}
for d in (1, 3, 15):
    p = fit(xtr, ytr, d)
    ev["worked"][str(d)] = {"degree": d, "coefficients": d + 1,
                            "train_mse": r(mse(p, xtr, ytr), 6), "test_mse": r(mse(p, xte, yte)),
                            "curve": [r(v) for v in p(grid)],
                            "max_abs_on_grid": r(np.max(np.abs(p(grid))))}
assert ev["worked"]["15"]["train_mse"] < 1e-9, "degree 15 should interpolate 16 points"

# One term of the MSE sum, worked by hand: the degree-1 line at its worst-missed training point.
p1 = fit(xtr, ytr, 1)
gaps = ytr - p1(xtr)
i0 = int(np.argmax(np.abs(gaps)))           # the line's worst miss (easy to see on screen)
ev["mse_example"] = {"degree": 1, "index": i0, "x": r(xtr[i0]), "y": r(ytr[i0]), "guess": r(p1(xtr[i0])),
                     "gap": r(gaps[i0]), "gap_squared": r(gaps[i0] ** 2),
                     "sum_squared": r(np.sum(gaps ** 2)), "n": N_TRAIN, "mse": r(np.mean(gaps ** 2), 6)}
assert abs(ev["mse_example"]["mse"] - ev["worked"]["1"]["train_mse"]) < 1e-6

# ---- 3. Degree sweep: the U ----------------------------------------------------------
sweep = []
for d in DEGREES:
    p = fit(xtr, ytr, d)
    sweep.append({"degree": d, "train_mse": r(mse(p, xtr, ytr), 6),
                  "test_mse": r(mse(p, xte, yte))})
ev["sweep"] = sweep
tr = [s["train_mse"] for s in sweep]
assert all(b <= a + 1e-9 for a, b in zip(tr, tr[1:])), "training error must never rise (nested models)"
best = min(sweep, key=lambda s: s["test_mse"])
ev["sweep_best"] = best

# Same sweep averaged over 500 independent datasets: is this seed's U typical?
TRIALS = 500
acc_tr = np.zeros(len(DEGREES)); acc_te = np.zeros(len(DEGREES)); med_te = [[] for _ in DEGREES]
rng_avg = np.random.default_rng(1000)
for _ in range(TRIALS):
    a, b = draw(rng_avg, N_TRAIN); c, e = draw(rng_avg, N_TEST)
    for i, d in enumerate(DEGREES):
        p = fit(a, b, d)
        acc_tr[i] += mse(p, a, b); te = mse(p, c, e); acc_te[i] += te; med_te[i].append(te)
ev["sweep_500"] = {"trials": TRIALS, "seed": 1000,
                   "mean_train_mse": [r(v / TRIALS, 6) for v in acc_tr],
                   "median_test_mse": [r(np.median(m)) for m in med_te],
                   "best_degree_by_median_test": int(np.argmin([np.median(m) for m in med_te]))}

# ---- 4. Falsifiability: more data tames degree 15 ------------------------------------
# Nested training sets: the film's own 16 points, then more points from the same source.
rng_more = np.random.default_rng(SEED + 1)
xa, ya = draw(rng_more, 984)
pool_x, pool_y = np.r_[xtr, xa], np.r_[ytr, ya]
more = []
for n in (16, 20, 30, 50, 100, 200, 1000):
    a, b = pool_x[:n], pool_y[:n]
    p = fit(a, b, 15)
    more.append({"n_train": n, "train_mse": r(mse(p, a, b), 6), "test_mse": r(mse(p, xte, yte)),
                 "curve": [r(v) for v in p(grid)]})          # drawn by B06 as the model refits
ev["more_data"] = more
ev["pool_preview"] = [[r(u), r(v)] for u, v in zip(pool_x, pool_y)]   # first n = the n-point training set
assert more[0]["test_mse"] == ev["worked"]["15"]["test_mse"], "n=16 must be the worked example"
a200, b200 = pool_x[:200], pool_y[:200]
p200 = fit(a200, b200, 15)
ev["more_data_200"] = {"n_train": 200, "train_preview": [[r(u), r(v)] for u, v in zip(a200, b200)],
                       "curve": [r(v) for v in p200(grid)],
                       "train_mse": r(mse(p200, a200, b200)), "test_mse": r(mse(p200, xte, yte))}
# where the U bottoms out at n = 200
sweep200 = []
for d in DEGREES:
    p = fit(a200, b200, d)
    sweep200.append({"degree": d, "train_mse": r(mse(p, a200, b200), 6), "test_mse": r(mse(p, xte, yte))})
ev["sweep_200"] = sweep200

# ---- 5. Falsifiability 2: a held-out score you chose by is no longer honest ----------
# Each trial: 30 training points; a 20-point VALIDATION set; a separate 20-point TEST set;
# 5000 fresh points measure each model's real error.
#   A) pick the degree by validation MSE, REPORT that same validation MSE   (the peek)
#   B) pick the degree by validation MSE, REPORT the untouched test MSE     (the fix)
#   C) control: degree 3 fixed in advance, report its validation MSE        (no choosing)
# "Optimistic" = reported score below the chosen model's real error.
TR2, N_FIT, N_HOLD, N_FRESH = 1000, 30, 20, 5000
rng_sel = np.random.default_rng(2024)
A, B, C = [], [], []
picks = []
for _ in range(TR2):
    a, b = draw(rng_sel, N_FIT); v, vy = draw(rng_sel, N_HOLD); t, ty = draw(rng_sel, N_HOLD)
    f, fy = draw(rng_sel, N_FRESH)
    fits = [fit(a, b, d) for d in DEGREES]
    val = [mse(p, v, vy) for p in fits]
    k = int(np.argmin(val)); picks.append(k)
    real_k = mse(fits[k], f, fy)
    A.append((val[k], real_k)); B.append((mse(fits[k], t, ty), real_k)); C.append((val[3], mse(fits[3], f, fy)))


def summ(pairs):
    rep, real = np.array(pairs).T
    return {"share_optimistic": r(np.mean(rep < real), 3), "median_reported": r(np.median(rep)),
            "median_real": r(np.median(real)), "median_ratio_reported_over_real": r(np.median(rep / real), 3)}


ev["selection"] = {"trials": TR2, "seed": 2024, "n_train": N_FIT, "n_validation": N_HOLD, "n_test": N_HOLD,
                   "n_fresh": N_FRESH, "candidates": "degrees 0-15",
                   "peek": summ(A), "untouched_test": summ(B), "control_fixed_degree_3": summ(C),
                   "most_picked_degree": int(np.bincount(picks).argmax()),
                   # per-trial outcomes of the first 100 trials (B07's 10x10 grids): 1 = reported < real
                   "grid100_peek": [int(a < b) for a, b in A[:100]],
                   "grid100_untouched": [int(a < b) for a, b in B[:100]]}

(OUT / "evidence.json").write_text(json.dumps(ev, indent=1), encoding="utf-8")

# ---- human-readable log ---------------------------------------------------------------
L = [f"python {ev['python']} numpy {ev['numpy']} on {ev['platform']}", ""]
s = ev["setup"]
L.append(f"setup: truth sin(pi x) on [-1,1], noise sd {SIGMA} (floor MSE {SIGMA**2:.2f}), "
         f"{N_TRAIN} train / {N_TEST} test, seed {SEED}")
L.append(f"   true curve itself scores: train {s['truth_train_mse']}  test {s['truth_test_mse']}")
L.append(f"   data hashes: train {ev['data']['hash_train']}  test {ev['data']['hash_test']}")
L.append("1) worked example (same 16 points)")
for d, w in ev["worked"].items():
    L.append(f"   degree {d:>2} ({w['coefficients']:>2} coefs): train MSE {w['train_mse']:<12g} "
             f"test MSE {w['test_mse']:<10g} max|f| on grid {w['max_abs_on_grid']}")
L.append("2) degree sweep, seed 15 (train MSE | test MSE)")
for q in sweep:
    L.append(f"   d={q['degree']:>2}  {q['train_mse']:<12g} {q['test_mse']:g}")
L.append(f"   lowest test MSE at degree {best['degree']}: {best['test_mse']}")
sa = ev["sweep_500"]
L.append(f"   500-dataset check: median test MSE by degree = {sa['median_test_mse']}")
L.append(f"   best degree by median: {sa['best_degree_by_median_test']}")
L.append("3) degree 15, more training data (test MSE on the same 1000 test points)")
for q in more:
    L.append(f"   n={q['n_train']:>4}  train {q['train_mse']:<12g} test {q['test_mse']:g}")
b2 = min(sweep200, key=lambda q: q["test_mse"])
L.append(f"   n=200 sweep: lowest test MSE at degree {b2['degree']} ({b2['test_mse']}); "
         f"degree 15 = {sweep200[15]['test_mse']}")
se = ev["selection"]
L.append(f"4) choosing by a held-out score, {TR2} trials (30 train, 20 validation, 20 test, 5000 fresh)")
for key, name in (("peek", "pick by validation, report validation"),
                  ("untouched_test", "pick by validation, report untouched test"),
                  ("control_fixed_degree_3", "control: degree 3 fixed, report validation")):
    q = se[key]
    L.append(f"   {name:<44} optimistic {q['share_optimistic']:.1%}  median reported {q['median_reported']} "
             f"vs real {q['median_real']}  median ratio {q['median_ratio_reported_over_real']}")
L.append(f"   most picked degree {se['most_picked_degree']}")
(OUT / "RUN-LOG.txt").write_text("\n".join(L) + "\n", encoding="utf-8")
print("\n".join(L))
