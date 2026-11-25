"""Executable evidence for "Gradient Descent, One Step at a Time".

Every number shown on screen in this film comes from this file's output
(demo/RUN-LOG.txt + demo/evidence.json). Pure Python + numpy, seeded, no ML libraries.
Run:  python demo/gd_demo.py
"""
import json, platform, sys
from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parent
ev = {"python": sys.version.split()[0], "numpy": np.__version__, "platform": platform.platform()}


def gd_1d(grad, theta0, lr, steps):
    path = [theta0]
    for _ in range(steps):
        path.append(path[-1] - lr * grad(path[-1]))
    return path


# ---- 1. Worked example: L(θ) = θ², dL/dθ = 2θ, θ0 = 3, η = 0.1 -------------------
L = lambda t: t * t
dL = lambda t: 2 * t
path = gd_1d(dL, 3.0, 0.1, 5)
ev["worked"] = {"loss": "theta^2", "grad": "2*theta", "theta0": 3.0, "lr": 0.1,
                "steps": [{"t": i, "theta": round(th, 4), "slope": round(dL(th), 4), "loss": round(L(th), 4)}
                          for i, th in enumerate(path)]}
# closed form: θ_t = θ0 (1 - 2η)^t  -> factor 0.8 per step
ev["worked"]["factor_per_step"] = 1 - 2 * 0.1
assert all(abs(th - 3.0 * 0.8 ** i) < 1e-12 for i, th in enumerate(path)), "closed form mismatch"

# ---- 2. Learning-rate sweep on the same bowl -------------------------------------
sweep = {}
for lr in (0.01, 0.1, 1.1):
    p = gd_1d(dL, 3.0, lr, 10)
    sweep[str(lr)] = {"factor": round(1 - 2 * lr, 4), "theta": [round(x, 4) for x in p]}
ev["sweep"] = sweep
ev["sweep_rule"] = "theta_t = theta0*(1-2*lr)^t ; converges iff |1-2*lr| < 1  <=>  0 < lr < 1"

# ---- 3. Non-convex: L(θ) = θ⁴ − 3θ² + θ  (two valleys) --------------------------
Lnc = lambda t: t ** 4 - 3 * t ** 2 + t
dLnc = lambda t: 4 * t ** 3 - 6 * t + 1
roots = np.roots([4, 0, -6, 1])
crit = sorted(float(r.real) for r in roots if abs(r.imag) < 1e-12)
minima = [c for c in crit if 12 * c * c - 6 > 0]            # L'' > 0
ev["nonconvex"] = {"loss": "theta^4 - 3 theta^2 + theta",
                   "critical_points": [round(c, 4) for c in crit],
                   "minima": [{"theta": round(m, 4), "loss": round(Lnc(m), 4)} for m in minima]}
for start in (2.0, -2.0):
    p = gd_1d(dLnc, start, 0.02, 200)
    ev["nonconvex"][f"start_{start}"] = {"lr": 0.02, "steps": 200,
                                          "path_head": [round(x, 4) for x in p[:12]],
                                          "end_theta": round(p[-1], 4), "end_loss": round(Lnc(p[-1]), 4)}

# ---- 4. Scale: fit y = w x + b on noisy data; full-batch GD vs mini-batch SGD -----
rng = np.random.default_rng(7)
n = 200
x = rng.uniform(-2, 2, n)
y = 1.5 * x - 0.5 + rng.normal(0, 0.4, n)
def grad_wb(w, b, idx):
    r = (w * x[idx] + b) - y[idx]
    return 2 * np.mean(r * x[idx]), 2 * np.mean(r)
def mse(w, b):
    return float(np.mean((w * x + b - y) ** 2))
w_ls, b_ls = np.polyfit(x, y, 1)
full, sgd = [(-1.0, 2.0)], [(-1.0, 2.0)]
for _ in range(60):
    w, b = full[-1]; gw, gb = grad_wb(w, b, np.arange(n)); full.append((w - 0.1 * gw, b - 0.1 * gb))
    w, b = sgd[-1]; gw, gb = grad_wb(w, b, rng.choice(n, 8, replace=False)); sgd.append((w - 0.1 * gw, b - 0.1 * gb))
ev["scale"] = {"model": "y = w*x + b", "true": {"w": 1.5, "b": -0.5}, "n": n, "seed": 7, "lr": 0.1,
               "batch": 8, "steps": 60,
               "least_squares": {"w": round(float(w_ls), 4), "b": round(float(b_ls), 4), "mse": round(mse(w_ls, b_ls), 4)},
               "full_end": {"w": round(full[-1][0], 4), "b": round(full[-1][1], 4), "mse": round(mse(*full[-1]), 4)},
               "sgd_end": {"w": round(sgd[-1][0], 4), "b": round(sgd[-1][1], 4), "mse": round(mse(*sgd[-1]), 4)},
               "full_path": [[round(a, 4), round(c, 4)] for a, c in full],
               "sgd_path": [[round(a, 4), round(c, 4)] for a, c in sgd]}

(OUT / "evidence.json").write_text(json.dumps(ev, indent=1), encoding="utf-8")

lines = [f"python {ev['python']} numpy {ev['numpy']} on {ev['platform']}", ""]
lines.append("1) worked example  L=θ², θ0=3, η=0.1")
for s in ev["worked"]["steps"]:
    lines.append(f"   t={s['t']}  θ={s['theta']:>7}  slope={s['slope']:>7}  L={s['loss']:>7}")
lines.append(f"   factor per step = {ev['worked']['factor_per_step']}")
lines.append("2) learning-rate sweep (θ after 10 steps)")
for lr, d in sweep.items():
    lines.append(f"   η={lr:<5} factor={d['factor']:>6}  θ10={d['theta'][-1]}")
lines.append("3) non-convex L=θ⁴−3θ²+θ  minima: " + ", ".join(f"θ={m['theta']} L={m['loss']}" for m in ev["nonconvex"]["minima"]))
for k in ("start_2.0", "start_-2.0"):
    d = ev["nonconvex"][k]; lines.append(f"   {k}: ends θ={d['end_theta']} L={d['end_loss']}")
sc = ev["scale"]
lines.append(f"4) line fit, n={n}, seed=7: least-squares w={sc['least_squares']['w']} b={sc['least_squares']['b']} mse={sc['least_squares']['mse']}")
lines.append(f"   full-batch GD 60 steps: w={sc['full_end']['w']} b={sc['full_end']['b']} mse={sc['full_end']['mse']}")
lines.append(f"   mini-batch(8) SGD 60 steps: w={sc['sgd_end']['w']} b={sc['sgd_end']['b']} mse={sc['sgd_end']['mse']}")
(OUT / "RUN-LOG.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
