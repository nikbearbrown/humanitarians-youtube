"""Executable evidence for "Why Neural Networks Need a Bend" (claude-liam-nonlinearity).

Every number shown on screen in this film comes from this file's output
(demo/RUN-LOG.txt + demo/evidence.json). Pure Python + numpy, seeded, no ML libraries.
Run:  python demo/nonlinearity_demo.py

Sections
  1. collapse   — two linear layers W2(W1 x) equal one matrix (W2 W1) x  (seed 0, small integers)
  2. scale      — 1,000 random inputs, a ten-layer linear stack, and biases: still one affine map
  3. xor_line   — no single line separates XOR (exhaustive line sweep + least-squares best line)
  4. deep_lin   — a 2-2-1 network with NO activation, trained by gradient descent: stuck at loss 1/4
  5. relu_hand  — the hand-set 2-unit ReLU network (Goodfellow et al. 2016, sec. 6.1) solves XOR exactly
  6. seeds      — the same 2-unit ReLU net TRAINED from 100 seeds: necessary, not sufficient
  7. kinks      — the hand-set net along the diagonal: straight pieces, kinks, straight again outside
"""
import json, platform, sys
from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parent
ev = {"python": sys.version.split()[0], "numpy": np.__version__, "platform": platform.platform()}

relu = lambda z: np.maximum(z, 0.0)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)   # XOR inputs
Y = np.array([0, 1, 1, 0], dtype=float)                        # XOR targets

# ---- 1. Collapse: W2(W1 x) == (W2 W1) x  ------------------------------------------
# Seed 0 is the first seed tried; entries are small integers so the arithmetic reads on screen.
rng = np.random.default_rng(0)
W1 = rng.integers(-2, 4, (2, 2))
W2 = rng.integers(-2, 4, (2, 2))
x = rng.integers(-2, 4, 2)
h = W1 @ x
two_step = W2 @ h
W21 = W2 @ W1
one_step = W21 @ x
assert np.array_equal(two_step, one_step), "collapse failed"
ev["collapse"] = {"seed": 0, "W1": W1.tolist(), "W2": W2.tolist(), "x": x.tolist(),
                  "W1x": h.tolist(), "W2_W1x": two_step.tolist(),
                  "W2W1": W21.tolist(), "W2W1_x": one_step.tolist(), "identical": True}

# ---- 2. Not a coincidence: random floats, 1,000 inputs, 10 layers, biases -------------
rng = np.random.default_rng(1)
A1, A2 = rng.normal(size=(2, 2)), rng.normal(size=(2, 2))
P = rng.normal(size=(2, 1000))
d2 = np.max(np.abs(A2 @ (A1 @ P) - (A2 @ A1) @ P))
layers = [rng.normal(size=(2, 2)) for _ in range(10)]
seq = P.copy()
for L in layers:
    seq = L @ seq
M = np.eye(2)
for L in layers:
    M = L @ M
d10 = np.max(np.abs(seq - M @ P))
rel10 = d10 / np.max(np.abs(seq))
b1, b2 = rng.normal(size=(2, 1)), rng.normal(size=(2, 1))
aff = A2 @ (A1 @ P + b1) + b2
aff_one = (A2 @ A1) @ P + (A2 @ b1 + b2)
dab = np.max(np.abs(aff - aff_one))
ev["scale"] = {"seed": 1, "n_inputs": 1000,
               "two_layer_max_abs_diff": float(f"{d2:.3g}"),
               "ten_layer_matrix": np.round(M, 4).tolist(),
               "ten_layer_max_abs_diff": float(f"{d10:.3g}"),
               "ten_layer_max_rel_diff": float(f"{rel10:.3g}"),
               "with_bias_max_abs_diff": float(f"{dab:.3g}"),
               "note": "differences are float64 rounding (machine epsilon 2.2e-16 x magnitude), not structure"}
assert d2 < 1e-12 and rel10 < 1e-12 and dab < 1e-12

# ---- 3. XOR: no single line separates it ---------------------------------------------
# (a) exhaustive sweep of lines w.x + b = 0: angle in 1-degree steps, offset in 0.01 steps
best = 0
for deg in range(360):
    th = np.deg2rad(deg)
    w = np.array([np.cos(th), np.sin(th)])
    for b in np.arange(-1.6, 1.6001, 0.01):
        pred = (X @ w + b > 0).astype(float)
        best = max(best, int(np.sum(pred == Y)))
n_lines = 360 * len(np.arange(-1.6, 1.6001, 0.01))
# (b) least-squares best affine fit y ~ w.x + b
Xa = np.hstack([X, np.ones((4, 1))])
coef, *_ = np.linalg.lstsq(Xa, Y, rcond=None)
ls_pred = Xa @ coef
ev["xor_line"] = {"points": X.astype(int).tolist(), "targets": Y.astype(int).tolist(),
                  "lines_tried": int(n_lines), "best_correct": best,
                  "least_squares": {"w1": round(float(coef[0]), 6) + 0.0, "w2": round(float(coef[1]), 6) + 0.0,
                                    "b": round(float(coef[2]), 6),
                                    "pred": [round(float(p), 6) for p in ls_pred],
                                    "mse": round(float(np.mean((ls_pred - Y) ** 2)), 6)},
                  "proof": "b<=0, w2+b>0, w1+b>0, w1+w2+b<=0; adding the middle two gives "
                           "w1+w2+2b>0, so w1+w2+b > -b >= 0, contradicting the last"}
assert best == 3

# ---- 4. Deep LINEAR network (2-2-1, no activation) trained on XOR ---------------------
def train(n_hidden, act, seed, steps=5000, lr=0.1):
    r = np.random.default_rng(seed)
    W = r.normal(0, 1, (n_hidden, 2)); c = np.zeros(n_hidden)
    v = r.normal(0, 1, n_hidden); d = 0.0
    curve = []
    for t in range(steps + 1):
        z = X @ W.T + c                      # (4, n_hidden)
        hh = act(z)
        yhat = hh @ v + d
        err = yhat - Y
        loss = float(np.mean(err ** 2))
        if t % 250 == 0:
            curve.append(round(loss, 5))
        if t == steps:
            break
        g = 2 * err / 4                      # dL/dyhat
        gv = hh.T @ g; gd = g.sum()
        gh = np.outer(g, v)
        gz = gh * (z > 0) if act is relu else gh
        gW = gz.T @ X; gc = gz.sum(0)
        W -= lr * gW; c -= lr * gc; v -= lr * gv; d -= lr * gd
    acc = int(np.sum((yhat > 0.5) == (Y > 0.5)))
    dead = int(np.sum(np.all(z <= 0, axis=0))) if act is relu else 0
    return {"loss": round(loss, 5), "correct": acc, "pred": [round(float(p), 4) for p in yhat],
            "dead_units": dead, "curve": curve, "W": np.round(W, 4).tolist(), "c": np.round(c, 4).tolist(),
            "v": np.round(v, 4).tolist(), "d": round(d, 4)}

identity = lambda z: z
lin = train(2, identity, seed=0)
lin_all = [train(2, identity, seed=s) for s in range(100)]
ev["deep_linear"] = {"arch": "2-2-1, no activation", "lr": 0.1, "steps": 5000, "seed": 0,
                     "run": lin,
                     "over_100_seeds": {"min_loss": min(r["loss"] for r in lin_all),
                                        "max_correct": max(r["correct"] for r in lin_all),
                                        "reached_4_of_4": sum(r["correct"] == 4 for r in lin_all)}}
assert ev["deep_linear"]["over_100_seeds"]["reached_4_of_4"] == 0

# ---- 5. Hand-set ReLU network (Goodfellow, Bengio & Courville 2016, sec. 6.1) ---------
Wh = np.array([[1, 1], [1, 1]], dtype=float); ch = np.array([0, -1], dtype=float)
wo = np.array([1, -2], dtype=float); bo = 0.0
Z = X @ Wh.T + ch
H = relu(Z)
out = H @ wo + bo
assert np.array_equal(out, Y), "hand-set ReLU net does not solve XOR"
# The same weights WITHOUT the ReLU: collapses to one line.
out_lin = Z @ wo + bo
ev["relu_hand"] = {"W": Wh.astype(int).tolist(), "c": ch.astype(int).tolist(),
                   "w": wo.astype(int).tolist(), "b": 0,
                   "rows": [{"x": X[i].astype(int).tolist(), "z": Z[i].astype(int).tolist(),
                             "h": H[i].astype(int).tolist(), "y": int(out[i]), "target": int(Y[i])}
                            for i in range(4)],
                   "hidden_points": sorted({tuple(r) for r in H.astype(int).tolist()}),
                   "separating_line_in_h": "h1 - 2*h2 = 0.5",
                   "without_relu_out": out_lin.astype(int).tolist(),
                   "without_relu_collapsed": {"w": (wo @ Wh).astype(int).tolist(), "b": int(wo @ ch + bo)}}

# ---- 6. Necessary, not sufficient: train the 2-unit ReLU net from 100 seeds -----------
SEEDS = range(100)
r2 = [train(2, relu, seed=s) for s in SEEDS]
r8 = [train(8, relu, seed=s) for s in SEEDS]
ok2 = [s for s, r in zip(SEEDS, r2) if r["correct"] == 4 and r["loss"] < 0.01]
ok8 = [s for s, r in zip(SEEDS, r8) if r["correct"] == 4 and r["loss"] < 0.01]
fail2 = [s for s in SEEDS if s not in ok2]
dead_fail2 = [s for s in fail2 if r2[s]["dead_units"] > 0]
ev["seeds"] = {"arch": "2-2-1 ReLU", "init": "W,v ~ N(0,1); c,d = 0", "lr": 0.1, "steps": 5000,
               "seeds": "0..99", "success_rule": "4 of 4 correct (threshold 0.5) and loss < 0.01",
               "two_units": {"solved": len(ok2), "failed": len(fail2),
                             "failed_with_dead_unit": len(dead_fail2),
                             "failed_losses": sorted({r2[s]["loss"] for s in fail2}),
                             "solved_mask": [int(s in ok2) for s in SEEDS],
                             "example_fail_seed": fail2[0] if fail2 else None,
                             "example_fail": r2[fail2[0]] if fail2 else None,
                             "example_ok_seed": ok2[0], "example_ok": r2[ok2[0]]},
               "eight_units": {"solved": len(ok8), "failed": 100 - len(ok8),
                               "solved_mask": [int(s in ok8) for s in SEEDS]}}

# ---- 7. Kinks: the hand-set net along the diagonal x = (t, t) --------------------------
f = lambda p: float(relu(Wh @ p + ch) @ wo + bo)
ts = [-1.0, -0.5, 0.0, 0.25, 0.5, 0.75, 1.0, 2.0, 3.0]
diag = [{"t": t, "y": round(f(np.array([t, t])), 4)} for t in ts]
ev["kinks"] = {"path": "x = (t, t)", "formula": "y = relu(2t) - 2 relu(2t - 1)",
               "kinks_at_t": [0.0, 0.5], "samples": diag,
               "pieces": ["t<=0: y = 0", "0<=t<=0.5: y = 2t", "t>=0.5: y = 2 - 2t"],
               "far": {"(3,3)": f(np.array([3., 3.])), "(10,10)": f(np.array([10., 10.])),
                       "(5,0)": f(np.array([5., 0.]))}}
for d_ in diag:
    t = d_["t"]
    want = 0.0 if t <= 0 else (2 * t if t <= 0.5 else 2 - 2 * t)
    assert abs(d_["y"] - want) < 1e-9

(OUT / "evidence.json").write_text(json.dumps(ev, indent=1), encoding="utf-8")

# ---- run log ------------------------------------------------------------------------
c = ev["collapse"]; s = ev["scale"]; xl = ev["xor_line"]; dl = ev["deep_linear"]
rh = ev["relu_hand"]; sd = ev["seeds"]; k = ev["kinks"]
lines = [f"python {ev['python']} numpy {ev['numpy']} on {ev['platform']}", ""]
lines.append(f"1) collapse (seed 0)  W1={c['W1']}  W2={c['W2']}  x={c['x']}")
lines.append(f"   W1x={c['W1x']}  W2(W1x)={c['W2_W1x']}  |  W2W1={c['W2W1']}  (W2W1)x={c['W2W1_x']}  identical={c['identical']}")
lines.append(f"2) scale (seed 1)  1000 inputs: 2-layer max|diff|={s['two_layer_max_abs_diff']}  "
             f"10-layer max|diff|={s['ten_layer_max_abs_diff']} (rel {s['ten_layer_max_rel_diff']})  "
             f"with bias={s['with_bias_max_abs_diff']}")
lines.append(f"   10 layers multiply to one matrix {s['ten_layer_matrix']}")
lines.append(f"3) XOR, {xl['lines_tried']} lines tried: best = {xl['best_correct']} of 4 correct")
lines.append(f"   least-squares line: w=({xl['least_squares']['w1']}, {xl['least_squares']['w2']}) "
             f"b={xl['least_squares']['b']}  predicts {xl['least_squares']['pred']}  mse={xl['least_squares']['mse']}")
lines.append(f"4) deep linear 2-2-1, seed 0, 5000 steps: loss={dl['run']['loss']} pred={dl['run']['pred']} "
             f"correct={dl['run']['correct']}/4")
lines.append(f"   over 100 seeds: min loss={dl['over_100_seeds']['min_loss']} max correct={dl['over_100_seeds']['max_correct']} "
             f"reached 4/4: {dl['over_100_seeds']['reached_4_of_4']}")
lines.append(f"5) hand-set ReLU  W={rh['W']} c={rh['c']} w={rh['w']}")
for r in rh["rows"]:
    lines.append(f"   x={r['x']}  z={r['z']}  h=relu(z)={r['h']}  y={r['y']}  target={r['target']}")
lines.append(f"   hidden points {rh['hidden_points']}; separating line {rh['separating_line_in_h']}")
lines.append(f"   same weights without ReLU -> {rh['without_relu_out']} = one line w={rh['without_relu_collapsed']['w']} b={rh['without_relu_collapsed']['b']}")
lines.append(f"6) 2-unit ReLU trained, seeds 0-99: solved {sd['two_units']['solved']}/100, "
             f"failed {sd['two_units']['failed']} ({sd['two_units']['failed_with_dead_unit']} with a dead unit), "
             f"failed losses {sd['two_units']['failed_losses']}")
lines.append(f"   e.g. seed {sd['two_units']['example_fail_seed']}: pred={sd['two_units']['example_fail']['pred']} "
             f"loss={sd['two_units']['example_fail']['loss']} dead={sd['two_units']['example_fail']['dead_units']}")
lines.append(f"   e.g. seed {sd['two_units']['example_ok_seed']}: pred={sd['two_units']['example_ok']['pred']} "
             f"loss={sd['two_units']['example_ok']['loss']}")
lines.append(f"   8-unit ReLU trained, seeds 0-99: solved {sd['eight_units']['solved']}/100")
lines.append(f"7) kinks along {k['path']}: {k['formula']}; kinks at t={k['kinks_at_t']}")
lines.append("   " + "  ".join(f"t={d['t']}:{d['y']}" for d in k["samples"]))
lines.append(f"   far away: {k['far']}")
(OUT / "RUN-LOG.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
