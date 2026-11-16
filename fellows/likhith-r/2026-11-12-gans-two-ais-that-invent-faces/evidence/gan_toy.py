"""gan_toy.py — a real, seeded numpy GAN behind every number in claude-hai-gans.

Task: learn a 1-D bell curve. "Real" data are samples from N(MU, SIGMA). The generator (the forger)
turns random noise z ~ N(0, 1) into a number; the discriminator (the detective) outputs the
probability that a number is real.

  G: x = W3 · tanh(W2 · tanh(W1 z + b1) + b2) + b3      (1 → 16 → 16 → 1)
  D: p = sigmoid(V3 · lrelu(V2 · lrelu(V1 x + c1) + c2) + c3)   (1 → 32 → 32 → 1)

Training is the standard alternating game from Goodfellow et al. 2014: K_D D steps on a batch of real +
fake (binary cross-entropy), then one G step with the non-saturating loss −log D(G(z)). Adam on both,
hand-written backprop (no autograd). Hyperparameters were fixed before the first full run.

Logged at EVERY step on a fixed, held-out evaluation set (EVAL real samples + EVAL fakes from a fixed
noise draw): the detective's accuracy (real called real when p > 0.5, fake called fake when p < 0.5),
the generator's sample mean and standard deviation. Histograms of the fakes are saved at a few steps.

Writes gan_toy.json (curves + histograms for the scenes), gan_toy_steps.npz (every step) and
gan_toy.out.txt (summary). Every number on screen is copied from those files.
"""
import json
import pathlib
import sys
import time

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
SEED = 2026
MU, SIGMA = 4.0, 1.25
STEPS = int(sys.argv[1]) if len(sys.argv) > 1 else 6000
BATCH, EVAL = 256, 4000
LR_D, LR_G, B1, B2, EPS = 1e-3, 2e-4, 0.5, 0.999, 1e-8
K_D = 5  # detective steps per forger step (the k of Goodfellow et al. 2014, Algorithm 1)
GH, DH = 16, 32
SNAPS = [0, 100, 300, 1000, 3000, STEPS]
BINS = np.linspace(-1.0, 9.0, 41)


def lrelu(x):
    return np.where(x > 0, x, 0.2 * x)


def dlrelu(x):
    return np.where(x > 0, 1.0, 0.2)


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-np.clip(x, -40, 40)))


def init(rng):
    n = lambda *s: rng.standard_normal(s)
    G = {"W1": n(1, GH), "b1": np.zeros(GH), "W2": n(GH, GH) / np.sqrt(GH), "b2": np.zeros(GH),
         "W3": n(GH, 1) / np.sqrt(GH), "b3": np.zeros(1)}
    D = {"V1": n(1, DH), "c1": np.zeros(DH), "V2": n(DH, DH) / np.sqrt(DH), "c2": np.zeros(DH),
         "V3": n(DH, 1) / np.sqrt(DH), "c3": np.zeros(1)}
    return G, D


def g_fwd(G, z):
    a1 = z @ G["W1"] + G["b1"]; h1 = np.tanh(a1)
    a2 = h1 @ G["W2"] + G["b2"]; h2 = np.tanh(a2)
    x = h2 @ G["W3"] + G["b3"]
    return x, (z, h1, h2)


def g_bwd(G, cache, dx):
    z, h1, h2 = cache
    gr = {"W3": h2.T @ dx, "b3": dx.sum(0)}
    d2 = (dx @ G["W3"].T) * (1 - h2 ** 2)
    gr["W2"] = h1.T @ d2; gr["b2"] = d2.sum(0)
    d1 = (d2 @ G["W2"].T) * (1 - h1 ** 2)
    gr["W1"] = z.T @ d1; gr["b1"] = d1.sum(0)
    return gr


def d_fwd(D, x):
    a1 = x @ D["V1"] + D["c1"]; h1 = lrelu(a1)
    a2 = h1 @ D["V2"] + D["c2"]; h2 = lrelu(a2)
    logit = h2 @ D["V3"] + D["c3"]
    return logit, (x, a1, h1, a2, h2)


def d_bwd(D, cache, dlogit):
    """returns (param grads, grad wrt input x)"""
    x, a1, h1, a2, h2 = cache
    gr = {"V3": h2.T @ dlogit, "c3": dlogit.sum(0)}
    d2 = (dlogit @ D["V3"].T) * dlrelu(a2)
    gr["V2"] = h1.T @ d2; gr["c2"] = d2.sum(0)
    d1 = (d2 @ D["V2"].T) * dlrelu(a1)
    gr["V1"] = x.T @ d1; gr["c1"] = d1.sum(0)
    return gr, d1 @ D["V1"].T


class Adam:
    def __init__(self, params, lr):
        self.lr, self.t = lr, 0
        self.m = {k: np.zeros_like(v) for k, v in params.items()}
        self.v = {k: np.zeros_like(v) for k, v in params.items()}

    def step(self, params, grads):
        self.t += 1
        for k in params:
            self.m[k] = B1 * self.m[k] + (1 - B1) * grads[k]
            self.v[k] = B2 * self.v[k] + (1 - B2) * grads[k] ** 2
            mh = self.m[k] / (1 - B1 ** self.t); vh = self.v[k] / (1 - B2 ** self.t)
            params[k] -= self.lr * mh / (np.sqrt(vh) + EPS)


def main():
    t0 = time.time()
    rng = np.random.default_rng(SEED)
    G, D = init(rng)
    oG, oD = Adam(G, LR_G), Adam(D, LR_D)
    ev_real = rng.normal(MU, SIGMA, (EVAL, 1))
    ev_z = rng.standard_normal((EVAL, 1))

    acc, acc_real, acc_fake, gmean, gstd = [], [], [], [], []
    hists = {}

    def evaluate(step):
        fake, _ = g_fwd(G, ev_z)
        pr = sigmoid(d_fwd(D, ev_real)[0]); pf = sigmoid(d_fwd(D, fake)[0])
        ar, af = float((pr > 0.5).mean()), float((pf < 0.5).mean())
        acc.append((ar + af) / 2); acc_real.append(ar); acc_fake.append(af)
        gmean.append(float(fake.mean())); gstd.append(float(fake.std()))
        if step in SNAPS:
            hists[step] = np.histogram(fake[:, 0], BINS)[0].tolist()

    evaluate(0)
    for step in range(1, STEPS + 1):
        # --- K_D detective steps: real → 1, fake → 0 ---
        for _ in range(K_D):
            xr = rng.normal(MU, SIGMA, (BATCH, 1))
            xf, _ = g_fwd(G, rng.standard_normal((BATCH, 1)))
            x = np.vstack([xr, xf]); y = np.vstack([np.ones((BATCH, 1)), np.zeros((BATCH, 1))])
            logit, cache = d_fwd(D, x)
            grD, _ = d_bwd(D, cache, (sigmoid(logit) - y) / len(x))
            oD.step(D, grD)
        # --- forger step: non-saturating loss −log D(G(z)) ---
        xf, gc = g_fwd(G, rng.standard_normal((BATCH, 1)))
        logit, dc = d_fwd(D, xf)
        _, dx = d_bwd(D, dc, (sigmoid(logit) - 1.0) / BATCH)
        oG.step(G, g_bwd(G, gc, dx))
        evaluate(step)

    acc = np.array(acc)
    # smoothed (100-step trailing mean) for the "finish line" read-out
    k = 100
    sm = np.convolve(acc, np.ones(k) / k, mode="valid")
    first_near_half = next((i + k - 1 for i, v in enumerate(sm) if v < 0.55), None)
    last = acc[-500:]
    summary = {
        "seed": SEED, "k_d": K_D, "lr_d": LR_D, "lr_g": LR_G, "steps": STEPS, "batch": BATCH, "eval": EVAL, "mu": MU, "sigma": SIGMA,
        "acc_step0": round(float(acc[0]), 4), "acc_max": round(float(acc.max()), 4), "acc_max_step": int(acc.argmax()),
        "acc_final": round(float(acc[-1]), 4), "acc_last500_mean": round(float(last.mean()), 4),
        "acc_last500_min": round(float(last.min()), 4), "acc_last500_max": round(float(last.max()), 4),
        "first_smoothed_below_55_step": first_near_half,
        "gen_mean_step0": round(gmean[0], 3), "gen_std_step0": round(gstd[0], 3),
        "gen_mean_final": round(gmean[-1], 3), "gen_std_final": round(gstd[-1], 3),
        "runtime_s": round(time.time() - t0, 1), "numpy": np.__version__,
    }
    # log-spaced + linear samples of the accuracy curve for the scenes
    idx = sorted(set(np.unique(np.round(np.geomspace(1, STEPS, 120)).astype(int)).tolist()
                     + list(range(0, STEPS + 1, 50))))
    curve = [[i, round(float(acc[i]), 4), round(gmean[i], 3), round(gstd[i], 3)] for i in idx]
    out = {**summary, "curve": curve, "bins": BINS.tolist(), "hists": {str(s): h for s, h in hists.items()},
           "real_hist": np.histogram(ev_real[:, 0], BINS)[0].tolist()}
    (HERE / "gan_toy.json").write_text(json.dumps(out))
    np.savez_compressed(HERE / "gan_toy_steps.npz", acc=acc, acc_real=np.array(acc_real),
                        acc_fake=np.array(acc_fake), gen_mean=np.array(gmean), gen_std=np.array(gstd))
    lines = [f"{k}: {v}" for k, v in summary.items()]
    lines += [f"acc @ step {s}: {acc[s]:.4f}  (real {acc_real[s]:.3f}, fake {acc_fake[s]:.3f})  gen mean {gmean[s]:.3f} sd {gstd[s]:.3f}"
              for s in [0, 10, 50, 100, 300, 1000, 2000, 3000, 4000, 5000, STEPS]]
    (HERE / "gan_toy.out.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
