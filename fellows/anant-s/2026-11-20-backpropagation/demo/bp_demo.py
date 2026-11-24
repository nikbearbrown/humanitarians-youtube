"""Executable evidence for "Backpropagation, One Error at a Time".

Network: x -> z = w1*x -> h = tanh(z) -> y = w2*h -> L = (y - t)^2
Every on-screen number comes from demo/evidence.json written by this file.
Pure Python + numpy, deterministic. Run:  python demo/bp_demo.py
"""
import json, math, platform, sys
from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parent
ev = {"python": sys.version.split()[0], "numpy": np.__version__, "platform": platform.platform()}

X, T = 1.0, 0.2          # input and target
W1, W2 = 0.5, 2.0        # starting weights
LR = 0.1


def forward(w1, w2, x=X, t=T):
    z = w1 * x
    h = math.tanh(z)
    y = w2 * h
    L = (y - t) ** 2
    return {"z": z, "h": h, "y": y, "L": L}


def backward(w1, w2, x=X, t=T):
    f = forward(w1, w2, x, t)
    dL_dy = 2 * (f["y"] - t)          # local slope of the loss
    dy_dw2 = f["h"]                   # y = w2*h
    dy_dh = w2
    dh_dz = 1 - f["h"] ** 2           # tanh'
    dz_dw1 = x                        # z = w1*x
    dL_dw2 = dL_dy * dy_dw2
    dL_dh = dL_dy * dy_dh
    dL_dz = dL_dh * dh_dz
    dL_dw1 = dL_dz * dz_dw1
    return f, {"dL_dy": dL_dy, "dy_dh": dy_dh, "dh_dz": dh_dz, "dz_dw1": dz_dw1,
               "dL_dw2": dL_dw2, "dL_dh": dL_dh, "dL_dz": dL_dz, "dL_dw1": dL_dw1}


r = lambda v, n=4: round(float(v), n)

# ---- 1. forward + backward at the starting weights --------------------------------
f, g = backward(W1, W2)
ev["setup"] = {"x": X, "t": T, "w1": W1, "w2": W2, "lr": LR,
               "net": "z = w1*x ; h = tanh(z) ; y = w2*h ; L = (y - t)^2"}
ev["forward"] = {k: r(v) for k, v in f.items()}
ev["backward"] = {k: r(v) for k, v in g.items()}
# chain rule assembled explicitly, factor by factor
chain = [g["dL_dy"], g["dy_dh"], g["dh_dz"], g["dz_dw1"]]
assert abs(np.prod(chain) - g["dL_dw1"]) < 1e-12
ev["chain_w1"] = {"factors": [r(c) for c in chain], "product": r(g["dL_dw1"])}

# ---- 2. one gradient-descent step ---------------------------------------------------
w1n, w2n = W1 - LR * g["dL_dw1"], W2 - LR * g["dL_dw2"]
fn = forward(w1n, w2n)
ev["step"] = {"w1": r(w1n), "w2": r(w2n), "L_before": r(f["L"]), "L_after": r(fn["L"])}

# ---- 3. finite-difference check (what backprop saves you from) ----------------------
eps = 1e-5
fd_w1 = (forward(W1 + eps, W2)["L"] - forward(W1 - eps, W2)["L"]) / (2 * eps)
fd_w2 = (forward(W1, W2 + eps)["L"] - forward(W1, W2 - eps)["L"]) / (2 * eps)
ev["fd_check"] = {"eps": eps,
                  "w1": {"backprop": r(g["dL_dw1"], 8), "finite_diff": r(fd_w1, 8), "abs_diff": float(f"{abs(fd_w1 - g['dL_dw1']):.2e}")},
                  "w2": {"backprop": r(g["dL_dw2"], 8), "finite_diff": r(fd_w2, 8), "abs_diff": float(f"{abs(fd_w2 - g['dL_dw2']):.2e}")}}
assert abs(fd_w1 - g["dL_dw1"]) < 1e-6 and abs(fd_w2 - g["dL_dw2"]) < 1e-6
# cost: central differences need 2 extra forward passes per weight; backprop ~ one backward pass
ev["cost"] = {"note": "central differences: 2 forward passes per weight; backprop: 1 forward + 1 backward for all weights",
              "weights_1e6_forward_passes_fd": 2 * 10 ** 6}

# ---- 4. vanishing gradient: a deep chain of sigmoids --------------------------------
sig = lambda u: 1 / (1 + math.exp(-u))
depth, a, wdeep = 10, 0.5, 1.0
acts, local = [a], []
for _ in range(depth):
    s = sig(wdeep * acts[-1])
    local.append(s * (1 - s) * wdeep)      # d(layer out)/d(layer in), never above 0.25*w
    acts.append(s)
grad_at_layer = []                         # gradient reaching each layer, from the top (layer 10 = 1)
run = 1.0
for d in reversed(local):
    grad_at_layer.append(run)
    run *= d
grad_at_layer = list(reversed(grad_at_layer))
ev["vanishing"] = {"depth": depth, "activation": "sigmoid", "w": wdeep, "x0": a,
                   "max_sigmoid_slope": 0.25,
                   "local_slopes": [r(v) for v in local],
                   "grad_reaching_layer": [float(f"{v:.3e}") for v in grad_at_layer],
                   "grad_at_input": float(f"{run:.3e}")}

# ---- 5. saturation case used by the Your Turn rubric: w1 = 5 -----------------------
fs, gs = backward(5.0, W2)
ev["saturated_w1_5"] = {"h": r(fs["h"], 6), "tanh_slope": float(f"{gs['dh_dz']:.3e}"),
                        "dL_dw1": float(f"{gs['dL_dw1']:.3e}")}

(OUT / "evidence.json").write_text(json.dumps(ev, indent=1), encoding="utf-8")

L = [f"python {ev['python']} numpy {ev['numpy']} on {ev['platform']}", "",
     f"net: {ev['setup']['net']}   x={X} t={T} w1={W1} w2={W2}",
     "1) forward: " + "  ".join(f"{k}={v}" for k, v in ev["forward"].items()),
     "   backward: " + "  ".join(f"{k}={v}" for k, v in ev["backward"].items()),
     f"   chain for w1: {' x '.join(str(c) for c in ev['chain_w1']['factors'])} = {ev['chain_w1']['product']}",
     f"2) step lr={LR}: w1 {W1}->{ev['step']['w1']}  w2 {W2}->{ev['step']['w2']}  loss {ev['step']['L_before']} -> {ev['step']['L_after']}",
     f"3) finite-diff check eps={eps}: w1 bp={ev['fd_check']['w1']['backprop']} fd={ev['fd_check']['w1']['finite_diff']} diff={ev['fd_check']['w1']['abs_diff']}",
     f"   w2 bp={ev['fd_check']['w2']['backprop']} fd={ev['fd_check']['w2']['finite_diff']} diff={ev['fd_check']['w2']['abs_diff']}",
     f"4) vanishing: {depth} sigmoid layers, local slopes {ev['vanishing']['local_slopes']}",
     f"   gradient reaching input = {ev['vanishing']['grad_at_input']}"]
(OUT / "RUN-LOG.txt").write_text("\n".join(L) + "\n", encoding="utf-8")
print("\n".join(L))
