"""
Small replication of the Deep Hedging idea (Buehler, Gonon, Teichmann & Wood,
Quantitative Finance 19(8), 2019; arXiv:1802.03042) for the Boopesh M. explainer.

NumPy implementation with hand-written backpropagation-through-time (PyTorch was
not installable in the build container in time; deep_hedge_torch_reference.py is the
original PyTorch draft of the same experiment, kept for reference, NOT run).
The analytic gradient is checked against finite differences before training
(`python deep_hedge.py --gradcheck`).

Setting (deliberately small, CPU-only, seed-locked):
  * Black-Scholes world: S0 = 100, sigma = 20%, r = 0, 30 trading days, daily rebalancing.
  * We SELL one at-the-money call (K = 100) and receive its Black-Scholes price.
  * Trading the stock costs a proportional fee gamma * |trade| * S (gamma = 0.5%).
  * Final P&L = premium - payoff + sum(delta_t * (S_{t+1} - S_t)) - costs.

Hedges compared on the same out-of-sample paths:
  1. no hedge
  2. Black-Scholes delta, rebalanced every day (the textbook answer, cost-blind)
  3. a small neural network trained the Deep Hedging way: it chooses the position
     from (time left, log-moneyness, current position) and is trained to maximise
     the entropic utility  U(X) = -(1/lambda) log E[exp(-lambda X)]  of the P&L
     INCLUDING trading costs (the paper's objective, entropic risk measure).

Sanity check: with gamma = 0 the network should rediscover Black-Scholes delta.

Writes results.json (numbers quoted in the film) and arrays.npz (for the charts).
"""
import json
import math
import sys
import time
from pathlib import Path

import numpy as np
from scipy.special import ndtr, logsumexp, expit

OUT = Path(__file__).resolve().parent
SEED = 7

S0, K, SIGMA, DAYS = 100.0, 100.0, 0.20, 30
T = DAYS / 252.0
DT = T / DAYS
LAMBDA = 1.0          # entropic risk aversion
N_TRAIN, N_TEST = 40_000, 40_000
EPOCHS, BATCH, LR = 60, 2_000, 3e-3
WIDTH = 32


def bs_call(s, k, tau, sigma):
    tau = np.maximum(tau, 1e-12)
    d1 = (np.log(s / k) + 0.5 * sigma ** 2 * tau) / (sigma * np.sqrt(tau))
    d2 = d1 - sigma * np.sqrt(tau)
    return s * ndtr(d1) - k * ndtr(d2), ndtr(d1)


def paths(n, seed):
    rng = np.random.default_rng(seed)
    z = rng.standard_normal((n, DAYS))
    logret = -0.5 * SIGMA ** 2 * DT + SIGMA * math.sqrt(DT) * z
    s = S0 * np.exp(np.cumsum(logret, axis=1))
    return np.concatenate([np.full((n, 1), S0), s], axis=1)          # (n, DAYS+1)


PREMIUM = float(bs_call(S0, K, T, SIGMA)[0])


def pnl(s, positions, gamma):
    """positions: (n, DAYS) shares held over [t, t+1]. Position is closed at expiry (cash-settled
    payoff, no final liquidation cost) and opened from zero at t = 0."""
    gains = (positions * (s[:, 1:] - s[:, :-1])).sum(1)
    prev = np.concatenate([np.zeros((s.shape[0], 1)), positions[:, :-1]], axis=1)
    cost = (gamma * np.abs(positions - prev) * s[:, :-1]).sum(1)
    payoff = np.maximum(s[:, -1] - K, 0.0)
    return PREMIUM - payoff + gains - cost, cost


def bs_positions(s):
    tau = T - DT * np.arange(DAYS)
    return bs_call(s[:, :-1], K, tau[None, :], SIGMA)[1]


# ---------------------------------------------------------------- policy network
def silu(x):
    return x * expit(x)


def dsilu(x):
    sg = expit(x)
    return sg * (1.0 + x * (1.0 - sg))


def init_params(rng, width=WIDTH):
    def lin(fan_in, fan_out):   # PyTorch nn.Linear default init
        b = 1.0 / math.sqrt(fan_in)
        return rng.uniform(-b, b, (fan_in, fan_out)), rng.uniform(-b, b, fan_out)
    W1, b1 = lin(3, width)
    W2, b2 = lin(width, width)
    W3, b3 = lin(width, 1)
    return {"W1": W1, "b1": b1, "W2": W2, "b2": b2, "W3": W3, "b3": b3}


def forward(p, s, keep=False):
    """Recurrent-in-position policy: delta_t = f(time left, log(S/K), delta_{t-1})."""
    n = s.shape[0]
    pos = np.zeros(n)
    out, cache = [], []
    for t in range(DAYS):
        x = np.stack([np.full(n, (DAYS - t) / DAYS), np.log(s[:, t] / K), pos], axis=1)
        h1 = x @ p["W1"] + p["b1"]; a1 = silu(h1)
        h2 = a1 @ p["W2"] + p["b2"]; a2 = silu(h2)
        o = (a2 @ p["W3"] + p["b3"])[:, 0]
        sg = expit(o)
        pos = sg * 1.2 - 0.1                                          # positions in [-0.1, 1.1]
        out.append(pos)
        if keep:
            cache.append((x, h1, a1, h2, a2, sg))
    return np.stack(out, axis=1), cache


def entropic(x):
    return float(-(1.0 / LAMBDA) * (logsumexp(-LAMBDA * x) - math.log(x.shape[0])))


def loss_and_grad(p, s, gamma):
    """loss = -U(P&L) (entropic); returns loss and dloss/dparams via BPTT."""
    pos, cache = forward(p, s, keep=True)
    x_pnl, _ = pnl(s, pos, gamma)
    loss = -entropic(x_pnl)
    # dloss/dX_i = -softmax(-lambda X)_i
    w = -np.exp(-LAMBDA * x_pnl - logsumexp(-LAMBDA * x_pnl))
    n = s.shape[0]
    prev = np.concatenate([np.zeros((n, 1)), pos[:, :-1]], axis=1)
    sgn = np.sign(pos - prev)                                         # (n, DAYS)
    dX = (s[:, 1:] - s[:, :-1]) - gamma * s[:, :-1] * sgn             # dX/dpos_t, own trade
    dX[:, :-1] += gamma * s[:, 1:-1] * sgn[:, 1:]                     # dX/dpos_t via next trade
    g_direct = w[:, None] * dX
    grads = {k: np.zeros_like(v) for k, v in p.items()}
    carry = np.zeros(n)
    for t in range(DAYS - 1, -1, -1):
        x, h1, a1, h2, a2, sg = cache[t]
        gpos = g_direct[:, t] + carry
        go = gpos * 1.2 * sg * (1.0 - sg)                             # (n,)
        grads["W3"] += a2.T @ go[:, None]; grads["b3"] += go.sum()
        ga2 = go[:, None] * p["W3"][:, 0][None, :]
        gh2 = ga2 * dsilu(h2)
        grads["W2"] += a1.T @ gh2; grads["b2"] += gh2.sum(0)
        ga1 = gh2 @ p["W2"].T
        gh1 = ga1 * dsilu(h1)
        grads["W1"] += x.T @ gh1; grads["b1"] += gh1.sum(0)
        gx = gh1 @ p["W1"].T
        carry = gx[:, 2]                                              # into pos_{t-1}
    return loss, grads


class Adam:
    def __init__(self, p, lr, b1=0.9, b2=0.999, eps=1e-8):
        self.lr, self.b1, self.b2, self.eps, self.t = lr, b1, b2, eps, 0
        self.m = {k: np.zeros_like(v) for k, v in p.items()}
        self.v = {k: np.zeros_like(v) for k, v in p.items()}

    def step(self, p, g):
        self.t += 1
        for k in p:
            self.m[k] = self.b1 * self.m[k] + (1 - self.b1) * g[k]
            self.v[k] = self.b2 * self.v[k] + (1 - self.b2) * g[k] ** 2
            mh = self.m[k] / (1 - self.b1 ** self.t)
            vh = self.v[k] / (1 - self.b2 ** self.t)
            p[k] -= self.lr * mh / (np.sqrt(vh) + self.eps)


def gradcheck():
    rng = np.random.default_rng(0)
    p = init_params(rng)
    s = paths(64, 99)
    worst = 0.0
    for gamma in (0.0, 0.005):
        _, g = loss_and_grad(p, s, gamma)
        for k in p:
            for idx in [tuple(rng.integers(0, d) for d in p[k].shape) for _ in range(4)]:
                old = p[k][idx]; e = 1e-6
                p[k][idx] = old + e; lp = -entropic(pnl(s, forward(p, s)[0], gamma)[0])
                p[k][idx] = old - e; lm = -entropic(pnl(s, forward(p, s)[0], gamma)[0])
                p[k][idx] = old
                num = (lp - lm) / (2 * e)
                rel = abs(num - g[k][idx]) / max(1e-8, abs(num) + abs(g[k][idx]))
                worst = max(worst, rel)
    print(f"gradcheck: worst relative error {worst:.2e}")
    return worst


def stats(x, cost):
    q = np.quantile(x, 0.05)
    return {"mean": float(x.mean()), "std": float(x.std()),
            "cvar5": float(x[x <= q].mean()),
            "entropic_utility": entropic(x),
            "mean_cost": float(cost.mean())}


def train(gamma, s_train, s_test, label, rng):
    p = init_params(rng)
    opt = Adam(p, LR)
    t0 = time.time()
    log = []
    for ep in range(EPOCHS):
        perm = rng.permutation(s_train.shape[0])
        for i in range(0, s_train.shape[0], BATCH):
            sb = s_train[perm[i:i + BATCH]]
            _, g = loss_and_grad(p, sb, gamma)
            opt.step(p, g)
        if ep % 10 == 0 or ep == EPOCHS - 1:
            u = entropic(pnl(s_test, forward(p, s_test)[0], gamma)[0])
            log.append({"epoch": ep, "test_entropic_utility": u})
            print(f"[{label}] epoch {ep:3d}  test entropic utility {u:+.4f}  ({time.time() - t0:.0f}s)", flush=True)
    return p, log


def main():
    if "--gradcheck" in sys.argv:
        sys.exit(0 if gradcheck() < 1e-4 else 1)
    worst = gradcheck()
    assert worst < 1e-4, "analytic gradient disagrees with finite differences"
    rng = np.random.default_rng(SEED)
    s_train, s_test = paths(N_TRAIN, 1), paths(N_TEST, 2)
    results = {"setup": {"S0": S0, "K": K, "sigma": SIGMA, "days": DAYS, "rebalance": "daily",
                         "premium_bs": PREMIUM, "lambda_entropic": LAMBDA,
                         "n_train": N_TRAIN, "n_test": N_TEST, "epochs": EPOCHS, "batch": BATCH,
                         "lr": LR, "optimizer": "Adam (hand-written)",
                         "network": "MLP 3-32-32-1, SiLU, inputs (time left, log S/K, previous position)",
                         "framework": "numpy + hand-written backprop through time",
                         "gradcheck_worst_rel_err": worst, "seed": SEED}}
    arrays = {}
    for gamma in (0.0, 0.005):
        tag = f"gamma_{gamma}"
        zero = np.zeros((N_TEST, DAYS))
        nh, nh_c = pnl(s_test, zero, gamma)
        bpos = bs_positions(s_test)
        bs, bs_c = pnl(s_test, bpos, gamma)
        p, log = train(gamma, s_train, s_test, tag, rng)
        dpos = forward(p, s_test)[0]
        dh, dh_c = pnl(s_test, dpos, gamma)
        results[tag] = {"no_hedge": stats(nh, nh_c), "bs_delta": stats(bs, bs_c), "deep_hedge": stats(dh, dh_c),
                        "mean_abs_gap_to_bs_delta": float(np.abs(dpos - bpos).mean()),
                        "training_log": log}
        arrays[f"{tag}_pnl_none"] = nh
        arrays[f"{tag}_pnl_bs"] = bs
        arrays[f"{tag}_pnl_deep"] = dh
        # one illustrative path for the "what did it learn" chart (path index 3 of the test set)
        arrays[f"{tag}_path_S"] = s_test[3]
        arrays[f"{tag}_path_bs"] = bpos[3]
        arrays[f"{tag}_path_deep"] = dpos[3]
        # daily turnover (shares traded) averaged over paths
        prev_b = np.concatenate([np.zeros((N_TEST, 1)), bpos[:, :-1]], 1)
        prev_d = np.concatenate([np.zeros((N_TEST, 1)), dpos[:, :-1]], 1)
        results[tag]["turnover_bs"] = float(np.abs(bpos - prev_b).sum(1).mean())
        results[tag]["turnover_deep"] = float(np.abs(dpos - prev_d).sum(1).mean())
        arrays[f"{tag}_turnover_bs_per_day"] = np.abs(bpos - prev_b).mean(0)
        arrays[f"{tag}_turnover_deep_per_day"] = np.abs(dpos - prev_d).mean(0)
    (OUT / "results.json").write_text(json.dumps(results, indent=2) + "\n")
    np.savez_compressed(OUT / "arrays.npz", **arrays)
    print(json.dumps({k: v for k, v in results.items()}, indent=2))


if __name__ == "__main__":
    main()
