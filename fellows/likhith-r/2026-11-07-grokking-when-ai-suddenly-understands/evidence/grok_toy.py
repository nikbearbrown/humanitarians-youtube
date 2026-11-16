"""grok_toy.py — a real, seeded numpy grokking run behind every number in claude-hai-grokking.

Task: (a + b) mod P, P = 97, as in Power et al. 2022. The 97 x 97 answer table has 9,409 cells;
the network sees TRAIN_FRAC of them and is tested on the rest.

Model: token embeddings E (P x D) for a and b (shared), hidden h = relu(E[a] W1a + E[b] W1b + b1),
logits = h W2. Full-batch AdamW, cross-entropy. Two runs with the SAME seed and data split:
  wd    — weight decay WD (the grokking run)
  nowd  — weight decay 0  (control: memorises, never generalises in the budget)
Logs train and test accuracy at every step, the total weight norm, and at the end a Fourier
analysis of the learned embeddings: how much of each embedding's energy sits in a handful of
cos/sin frequencies (the "waves" Nanda et al. 2023 found).

Writes grok_toy.json (curves for the scenes) and grok_toy.out.txt (summary). Every number on
screen is copied from those files.
"""
import json
import pathlib
import sys
import time

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
P = 97
TRAIN_FRAC = 0.4
D, HID = 128, 256
LR, B1, B2, EPS = 1e-3, 0.9, 0.98, 1e-8
WD = 1.0
STEPS = int(sys.argv[1]) if len(sys.argv) > 1 else 30000
SEED = 2026


def init(rng):
    s = lambda *shape: rng.standard_normal(shape).astype(np.float32)
    return {
        "E": s(P, D) * (1 / np.sqrt(D)),
        "W1a": s(D, HID) * (1 / np.sqrt(D)),
        "W1b": s(D, HID) * (1 / np.sqrt(D)),
        "b1": np.zeros(HID, np.float32),
        "W2": s(HID, P) * (1 / np.sqrt(HID)),
    }


def forward(p, a, b):
    ea, eb = p["E"][a], p["E"][b]
    z = ea @ p["W1a"] + eb @ p["W1b"] + p["b1"]
    h = np.maximum(z, 0)
    return ea, eb, z, h, h @ p["W2"]


def acc(p, a, b, y):
    return float((forward(p, a, b)[4].argmax(1) == y).mean())


def run(wd, a_tr, b_tr, y_tr, a_te, b_te, y_te, steps):
    rng = np.random.default_rng(SEED)
    p = init(rng)
    m = {k: np.zeros_like(v) for k, v in p.items()}
    v = {k: np.zeros_like(v) for k, v in p.items()}
    n = len(y_tr)
    tr_acc, te_acc, norm, loss_log = [], [], [], []
    t0 = time.time()
    for step in range(1, steps + 1):
        ea, eb, z, h, logits = forward(p, a_tr, b_tr)
        logits = logits - logits.max(1, keepdims=True)
        ex = np.exp(logits)
        pr = ex / ex.sum(1, keepdims=True)
        loss = float(-np.log(pr[np.arange(n), y_tr] + 1e-12).mean())
        tr_acc.append(float((pr.argmax(1) == y_tr).mean()))
        te_acc.append(acc(p, a_te, b_te, y_te))
        norm.append(float(np.sqrt(sum((w.astype(np.float64) ** 2).sum() for w in p.values()))))
        loss_log.append(loss)
        g = pr
        g[np.arange(n), y_tr] -= 1
        g /= n
        grads = {"W2": h.T @ g}
        dh = g @ p["W2"].T
        dz = dh * (z > 0)
        grads["b1"] = dz.sum(0)
        grads["W1a"] = ea.T @ dz
        grads["W1b"] = eb.T @ dz
        dea, deb = dz @ p["W1a"].T, dz @ p["W1b"].T
        gE = np.zeros_like(p["E"])
        np.add.at(gE, a_tr, dea)
        np.add.at(gE, b_tr, deb)
        grads["E"] = gE
        for k in p:
            m[k] = B1 * m[k] + (1 - B1) * grads[k]
            v[k] = B2 * v[k] + (1 - B2) * grads[k] ** 2
            mh = m[k] / (1 - B1 ** step)
            vh = v[k] / (1 - B2 ** step)
            p[k] -= LR * (mh / (np.sqrt(vh) + EPS) + wd * p[k])   # AdamW: decoupled decay
        if step % 2000 == 0:
            print(f"  wd={wd} step {step:6d} loss {loss:.4f} train {tr_acc[-1]:.3f} test {te_acc[-1]:.3f} "
                  f"norm {norm[-1]:.1f} ({time.time() - t0:.0f}s)", flush=True)
    return p, np.array(tr_acc), np.array(te_acc), np.array(norm), np.array(loss_log)


def first(arr, thr):
    idx = np.nonzero(arr >= thr)[0]
    return int(idx[0]) + 1 if len(idx) else None


def fourier(E):
    """Energy of the embedding table (over the token axis) per frequency k = 1..48 (cos+sin pooled)."""
    x = np.arange(P)
    energy = []
    Ec = E - E.mean(0)
    for k in range(1, P // 2 + 1):
        c, s = np.cos(2 * np.pi * k * x / P), np.sin(2 * np.pi * k * x / P)
        energy.append(float(((c @ Ec) ** 2).sum() + ((s @ Ec) ** 2).sum()))
    energy = np.array(energy)
    return energy / energy.sum()


def main():
    rng = np.random.default_rng(SEED)
    pairs = np.array([(a, b) for a in range(P) for b in range(P)])
    perm = rng.permutation(len(pairs))
    ntr = int(TRAIN_FRAC * len(pairs))
    tr, te = pairs[perm[:ntr]], pairs[perm[ntr:]]
    a_tr, b_tr, y_tr = tr[:, 0], tr[:, 1], (tr[:, 0] + tr[:, 1]) % P
    a_te, b_te, y_te = te[:, 0], te[:, 1], (te[:, 0] + te[:, 1]) % P
    print(f"P={P} cells={len(pairs)} train={ntr} test={len(te)} steps={STEPS}")

    out = {"P": P, "cells": len(pairs), "train": ntr, "test": len(te), "train_frac": TRAIN_FRAC,
           "D": D, "hidden": HID, "lr": LR, "wd": WD, "steps": STEPS, "seed": SEED, "numpy": np.__version__}
    runs = {}
    for name, wd in (("wd", WD), ("nowd", 0.0)):
        p, tra, tea, nrm, lss = run(wd, a_tr, b_tr, y_tr, a_te, b_te, y_te, STEPS)
        f = fourier(p["E"])
        top = np.argsort(f)[::-1]
        runs[name] = dict(p=p, tra=tra, tea=tea, nrm=nrm, f=f)
        out[name] = {
            "wd": wd,
            "train_99_step": first(tra, 0.99), "train_100_step": first(tra, 1.0),
            "test_50_step": first(tea, 0.5), "test_99_step": first(tea, 0.99),
            "final_train": float(tra[-1]), "final_test": float(tea[-1]),
            "test_at_train_100": float(tea[first(tra, 1.0) - 1]) if first(tra, 1.0) else None,
            "max_test_before_10x": None,
            "norm_start": float(nrm[0]), "norm_at_train_100": float(nrm[first(tra, 1.0) - 1]) if first(tra, 1.0) else None,
            "norm_end": float(nrm[-1]),
            "fourier_top_k": [int(k + 1) for k in top[:8]],
            "fourier_top5_share": float(f[top[:5]].sum()),
            "fourier_energy": [round(float(x), 5) for x in f],
        }
    # log-spaced samples for plotting (every step is kept in the npz)
    idx = np.unique(np.round(np.logspace(0, np.log10(STEPS), 160)).astype(int)) - 1
    for name in runs:
        out[name]["curve"] = [[int(i + 1), round(float(runs[name]["tra"][i]), 4), round(float(runs[name]["tea"][i]), 4),
                               round(float(runs[name]["nrm"][i]), 2)] for i in idx]
    np.savez_compressed(HERE / "grok_toy_steps.npz", **{f"{n}_{k}": runs[n][k] for n in runs for k in ("tra", "tea", "nrm")})
    # the embedding's strongest wave, for the "clock" scene: (cos, sin) of token x at the top frequency
    k = out["wd"]["fourier_top_k"][0]
    out["wd"]["top_wave_k"] = k
    w = out["wd"]
    s100 = w["train_100_step"]; s99 = w["test_99_step"]
    w["gap_ratio"] = round(s99 / s100, 1) if (s100 and s99) else None
    (HERE / "grok_toy.json").write_text(json.dumps(out, indent=1) + "\n")

    lines = [
        f"grok_toy.py · numpy {np.__version__} · seed {SEED}",
        f"task: (a + b) mod {P}; table {len(pairs)} cells; train {ntr} ({TRAIN_FRAC:.0%}), test {len(te)}",
        f"model: embed {D}, hidden {HID} relu, AdamW lr {LR}, full batch, {STEPS} steps",
    ]
    for name in ("wd", "nowd"):
        o = out[name]
        lines += [
            f"[{name}] weight decay {o['wd']}",
            f"  train acc first 100%: step {o['train_100_step']}   (99%: {o['train_99_step']})",
            f"  test acc at that step: {o['test_at_train_100']}",
            f"  test acc first 50%: step {o['test_50_step']}   first 99%: step {o['test_99_step']}",
            f"  final train {o['final_train']:.4f}  final test {o['final_test']:.4f}",
            f"  weight norm: start {o['norm_start']:.1f}, at train 100% {o['norm_at_train_100']}, end {o['norm_end']:.1f}",
            f"  embedding Fourier: top frequencies {o['fourier_top_k'][:5]}, top-5 share of energy {o['fourier_top5_share']:.3f} (uniform would be {5 / (P // 2):.3f})",
        ]
    lines.append(f"gap: test 99% step / train 100% step = {out['wd']['gap_ratio']}")
    (HERE / "grok_toy.out.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
