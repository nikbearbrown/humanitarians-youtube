"""
Small replication of the Deep Hedging idea (Buehler, Gonon, Teichmann & Wood,
Quantitative Finance 19(8), 2019; arXiv:1802.03042) for the Boopesh M. explainer.

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
import time
from pathlib import Path

import numpy as np
import torch

OUT = Path(__file__).resolve().parent
torch.manual_seed(7)
np.random.seed(7)
torch.set_num_threads(2)

S0, K, SIGMA, DAYS = 100.0, 100.0, 0.20, 30
T = DAYS / 252.0
DT = T / DAYS
LAMBDA = 1.0          # entropic risk aversion
N_TRAIN, N_TEST = 40_000, 40_000
EPOCHS, BATCH = 60, 2_000


def norm_cdf(x):
    return 0.5 * (1.0 + torch.erf(x / math.sqrt(2.0)))


def bs_call(s, k, tau, sigma):
    tau = torch.clamp(tau, min=1e-12)
    d1 = (torch.log(s / k) + 0.5 * sigma ** 2 * tau) / (sigma * torch.sqrt(tau))
    d2 = d1 - sigma * torch.sqrt(tau)
    return s * norm_cdf(d1) - k * norm_cdf(d2), norm_cdf(d1)


def paths(n, seed):
    g = torch.Generator().manual_seed(seed)
    z = torch.randn(n, DAYS, generator=g)
    logret = -0.5 * SIGMA ** 2 * DT + SIGMA * math.sqrt(DT) * z
    s = S0 * torch.exp(torch.cumsum(logret, dim=1))
    return torch.cat([torch.full((n, 1), S0), s], dim=1)          # (n, DAYS+1)


PREMIUM = float(bs_call(torch.tensor(S0), torch.tensor(K), torch.tensor(T), SIGMA)[0])


def pnl(s, positions, gamma):
    """positions: (n, DAYS) shares held over [t, t+1]. Position is closed at expiry (cash-settled
    payoff, no final liquidation cost) and opened from zero at t = 0."""
    gains = (positions * (s[:, 1:] - s[:, :-1])).sum(1)
    prev = torch.cat([torch.zeros(s.shape[0], 1), positions[:, :-1]], dim=1)
    cost = (gamma * (positions - prev).abs() * s[:, :-1]).sum(1)
    payoff = torch.clamp(s[:, -1] - K, min=0.0)
    return PREMIUM - payoff + gains - cost, cost


def bs_positions(s):
    tau = T - DT * torch.arange(DAYS, dtype=torch.float32)
    return bs_call(s[:, :-1], torch.tensor(K), tau.expand(s.shape[0], -1), SIGMA)[1]


class Hedger(torch.nn.Module):
    """Recurrent-in-position policy: delta_t = f(time left, log(S/K), delta_{t-1})."""

    def __init__(self, width=32):
        super().__init__()
        self.net = torch.nn.Sequential(
            torch.nn.Linear(3, width), torch.nn.SiLU(),
            torch.nn.Linear(width, width), torch.nn.SiLU(),
            torch.nn.Linear(width, 1))

    def forward(self, s):
        n = s.shape[0]
        pos, out = torch.zeros(n), []
        for t in range(DAYS):
            tau = torch.full((n,), (DAYS - t) / DAYS)
            x = torch.stack([tau, torch.log(s[:, t] / K), pos], dim=1)
            pos = torch.sigmoid(self.net(x).squeeze(1)) * 1.2 - 0.1     # positions in [-0.1, 1.1]
            out.append(pos)
        return torch.stack(out, dim=1)


def entropic(x):
    return -(1.0 / LAMBDA) * (torch.logsumexp(-LAMBDA * x, dim=0) - math.log(x.shape[0]))


def stats(x, cost):
    x = x.detach().numpy()
    q = np.quantile(x, 0.05)
    return {"mean": float(x.mean()), "std": float(x.std()),
            "cvar5": float(x[x <= q].mean()),
            "entropic_utility": float(entropic(torch.tensor(x))),
            "mean_cost": float(cost.detach().mean())}


def train(gamma, s_train, s_test, label):
    model = Hedger()
    opt = torch.optim.Adam(model.parameters(), lr=3e-3)
    t0 = time.time()
    for ep in range(EPOCHS):
        perm = torch.randperm(s_train.shape[0])
        for i in range(0, s_train.shape[0], BATCH):
            sb = s_train[perm[i:i + BATCH]]
            loss = -entropic(pnl(sb, model(sb), gamma)[0])
            opt.zero_grad()
            loss.backward()
            opt.step()
        if ep % 10 == 0 or ep == EPOCHS - 1:
            with torch.no_grad():
                u = entropic(pnl(s_test, model(s_test), gamma)[0])
            print(f"[{label}] epoch {ep:3d}  test entropic utility {float(u):+.4f}  ({time.time() - t0:.0f}s)")
    return model


def main():
    s_train, s_test = paths(N_TRAIN, 1), paths(N_TEST, 2)
    results = {"setup": {"S0": S0, "K": K, "sigma": SIGMA, "days": DAYS, "rebalance": "daily",
                         "premium_bs": PREMIUM, "lambda_entropic": LAMBDA,
                         "n_train": N_TRAIN, "n_test": N_TEST, "epochs": EPOCHS,
                         "network": "MLP 3-32-32-1, SiLU, inputs (time left, log S/K, previous position)",
                         "seed": 7}}
    arrays = {}
    for gamma in (0.0, 0.005):
        tag = f"gamma_{gamma}"
        with torch.no_grad():
            zero = torch.zeros(N_TEST, DAYS)
            nh, nh_c = pnl(s_test, zero, gamma)
            bpos = bs_positions(s_test)
            bs, bs_c = pnl(s_test, bpos, gamma)
        model = train(gamma, s_train, s_test, tag)
        with torch.no_grad():
            dpos = model(s_test)
            dh, dh_c = pnl(s_test, dpos, gamma)
        results[tag] = {"no_hedge": stats(nh, nh_c), "bs_delta": stats(bs, bs_c), "deep_hedge": stats(dh, dh_c),
                        "mean_abs_gap_to_bs_delta": float((dpos - bpos).abs().mean())}
        arrays[f"{tag}_pnl_none"] = nh.numpy()
        arrays[f"{tag}_pnl_bs"] = bs.numpy()
        arrays[f"{tag}_pnl_deep"] = dh.numpy()
        # one illustrative path for the "what did it learn" chart (path index 3 of the test set)
        arrays[f"{tag}_path_S"] = s_test[3].numpy()
        arrays[f"{tag}_path_bs"] = bpos[3].numpy()
        arrays[f"{tag}_path_deep"] = dpos[3].numpy()
        # daily turnover (shares traded) averaged over paths
        prev_b = torch.cat([torch.zeros(N_TEST, 1), bpos[:, :-1]], 1)
        prev_d = torch.cat([torch.zeros(N_TEST, 1), dpos[:, :-1]], 1)
        results[tag]["turnover_bs"] = float((bpos - prev_b).abs().sum(1).mean())
        results[tag]["turnover_deep"] = float((dpos - prev_d).abs().sum(1).mean())
    (OUT / "results.json").write_text(json.dumps(results, indent=2) + "\n")
    np.savez_compressed(OUT / "arrays.npz", **arrays)
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
