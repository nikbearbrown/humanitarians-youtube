#!/usr/bin/env python3
"""execution_rl.py -- "How an AI Sells a Big Order" (Boopesh M., 2026-11-22).

A SYNTHETIC toy market, numpy only, seed-locked. Nothing here is real market data.

The problem: sell X = 10,000 shares within N = 10 time steps.

Market (the linear model of Almgren & Chriss, "Optimal Execution of Portfolio
Transactions", Dec 2000 author version, eqs. 1, 2, 7, with no permanent impact,
no fixed cost and tau = 1 step):
  * the price is an arithmetic random walk:   S[k+1] = S[k] + SIGMA * xi[k],  xi ~ N(0, 1)
  * selling n shares in step k gets the price S[k] - ETA * n per share
    (temporary impact: the bigger the child order, the worse its price; it does
    not carry over to the next step).
Cost = implementation shortfall = X * S0 - cash received (Perold's measure, as
A&C section 1.4 calls it), reported in dollars and in basis points of X * S0.

Strategies compared on the SAME held-out simulated days:
  1. dump  -- sell everything in the first step
  2. TWAP  -- ten equal slices
  3. RL    -- a tabular Q-learning agent.
              state  = (time steps left, shares left in lots of 250)
              action = fraction of the shares left to sell now (0%, 5%, ..., 100%)
              reward = cash received vs the arrival price, minus a small risk penalty
                       LAMBDA * SIGMA^2 * (shares still held)^2 per step.
              At the last step whatever is left is sold.
  4. AC    -- the Almgren-Chriss closed form for the same objective
              (expected cost + LAMBDA * variance):
                 x_j = X * sinh(kappa * (N - j)) / sinh(kappa * N)
                 2 * (cosh(kappa) - 1) = LAMBDA * SIGMA^2 / ETA        (A&C eq. 16-17)
  5. grid  -- exact dynamic programming on the agent's own grid (a check on how
              close Q-learning got to the best it could possibly do).

Run:  python3 execution_rl.py            -> results.json + run.log next to this file
"""
import hashlib
import json
import math
import platform
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent

# ---- synthetic market + task --------------------------------------------------------
SEED_TRAIN = 20261122          # training days
SEED_TEST = 7                  # held-out days (never seen in training)
X = 10_000                     # shares to sell
S0 = 50.00                     # arrival price, $ (synthetic)
N = 10                         # time steps
LOT = 250                      # shares per lot -> 40 lots
Q_LOTS = X // LOT
SIGMA = 0.10                   # $ per share, std of one step's price move
ETA = 5e-5                     # $ per share, per share sold in that step (temporary impact)
LAMBDA = 3e-4                  # risk penalty, 1/$ (how much we dislike uncertainty)
FRACTIONS = np.round(np.linspace(0.0, 1.0, 21), 2)   # 0%, 5%, ..., 100%
A = len(FRACTIONS)

# ---- Q-learning settings ------------------------------------------------------------
# Off-policy tabular Q-learning. Behaviour: exploring starts (a random time step and a
# random number of shares left) and random actions, so every cell of the table gets
# practice; the greedy (max-Q) policy is what gets evaluated. Days run in parallel
# batches (DAYS_PER_BATCH at a time); each table cell's value is the running mean of its
# Q-learning targets  r + max_a' Q(next state, a').
DAYS_PER_BATCH = 4_000
BATCHES = 10_000
EPISODES = DAYS_PER_BATCH * BATCHES      # simulated practice days
TEST_DAYS = 20_000

NOTIONAL = X * S0
BPS = 1e4 / NOTIONAL


def lots_to_sell(q, a):
    """Shares-left q (lots), action index a -> lots sold now (rounded to the lot)."""
    return int(round(FRACTIONS[a] * q))


def expected_step_reward(q, n):
    """E[reward] of selling n lots out of q: -impact cost - risk penalty on what is left."""
    sh = n * LOT
    left = (q - n) * LOT
    return -(ETA * sh * sh) - LAMBDA * SIGMA ** 2 * left * left


def train_q(log):
    """Tabular (double) Q-learning on simulated days of the synthetic market.

    Reward of one step = change in mark-to-market value of (cash + shares still held)
    minus the risk penalty:  r = -ETA*n^2 + x'*SIGMA*xi - LAMBDA*SIGMA^2*x'^2,
    where n = shares sold now, x' = shares still held, xi = the next random price move.
    Summed over a day this is minus (implementation shortfall + risk penalty).

    Two tables (double Q-learning, van Hasselt 2010): each update picks one table at
    random, chooses the next action with it and scores that action with the other one.
    This removes the optimistic bias that taking a max over noisy estimates creates.
    The agent's policy is the argmax of the sum of the two tables.
    """
    rng = np.random.default_rng(SEED_TRAIN)
    S = N * (Q_LOTS + 1) * A
    Qs = [np.zeros(S), np.zeros(S)]      # flat tables: index (k * (Q_LOTS+1) + q) * A + a
    cnts = [np.zeros(S), np.zeros(S)]
    curve = []
    M = DAYS_PER_BATCH
    for batch in range(BATCHES):
        k = rng.integers(0, N, M)                       # exploring starts: time step ...
        q = rng.integers(1, Q_LOTS + 1, M)              # ... and shares left (lots)
        active = np.ones(M, bool)
        while active.any():
            a = rng.integers(0, A, M)                   # random behaviour action
            xi = rng.standard_normal(M)
            coin = rng.random(M) < 0.5                  # which table learns from this step
            last = k >= N - 1
            n = np.where(last, q, np.rint(FRACTIONS[a] * q).astype(int))
            a = np.where(last, A - 1, a)
            left = q - n
            sh, held = n * LOT, left * LOT
            r = -ETA * sh * sh + held * SIGMA * xi - LAMBDA * SIGMA ** 2 * held * held
            kn = np.minimum(k + 1, N - 1)
            rows = [Qx.reshape(N, Q_LOTS + 1, A)[kn, left] for Qx in Qs]
            idx = np.arange(M)
            for t in (0, 1):
                pick = rows[t].argmax(axis=1)           # choose with table t ...
                val = rows[1 - t][idx, pick]            # ... score with the other table
                # the last step is forced (sell everything): its value is that action's
                val = np.where(kn == N - 1, rows[1 - t][:, A - 1], val)
                nxt = np.where(last | (left == 0), 0.0, val)
                sel = active & (coin if t == 0 else ~coin)
                fi = ((k * (Q_LOTS + 1) + q) * A + a)[sel]
                err = (r + nxt)[sel] - Qs[t][fi]
                m = np.bincount(fi, minlength=S)
                e = np.bincount(fi, weights=err, minlength=S)
                hit = m > 0
                cnts[t][hit] += m[hit]
                Qs[t][hit] += e[hit] / cnts[t][hit]     # running mean of the targets
            k, q = k + 1, left
            active &= (k < N) & (q > 0)
        if (batch + 1) % 500 == 0:
            Qt = (Qs[0] + Qs[1]).reshape(N, Q_LOTS + 1, A)
            E, V = analytic(greedy_schedule(Qt))
            visits = (cnts[0] + cnts[1]).reshape(N, Q_LOTS + 1, A)[:N - 1, 1:, :]
            curve.append([(batch + 1) * M, round((E + LAMBDA * V) * BPS, 3)])
            log(f"  practice days {(batch + 1) * M:>10,}   greedy schedule: expected cost + "
                f"risk penalty {(E + LAMBDA * V) * BPS:7.3f} bps   min visits/cell "
                f"{int(visits.min()):,}")
    return (Qs[0] + Qs[1]).reshape(N, Q_LOTS + 1, A), curve


def greedy_schedule(Q):
    q, sched = Q_LOTS, []
    for k in range(N):
        n = q if k == N - 1 else lots_to_sell(q, int(np.argmax(Q[k, q])))
        sched.append(n * LOT)
        q -= n
    return sched


def grid_dp():
    """Exact best schedule on the agent's grid, using expected rewards (a check only)."""
    V = np.zeros((N + 1, Q_LOTS + 1))
    V[N, 1:] = -np.inf
    pol = np.zeros((N, Q_LOTS + 1), dtype=int)
    for k in range(N - 1, -1, -1):
        for q in range(Q_LOTS + 1):
            best, best_a = -np.inf, 0
            acts = [A - 1] if k == N - 1 else range(A)
            for a in acts:
                n = q if k == N - 1 else lots_to_sell(q, a)
                v = expected_step_reward(q, n) + V[k + 1, q - n]
                if v > best + 1e-12:
                    best, best_a = v, a
            V[k, q], pol[k, q] = best, best_a
    q, sched = Q_LOTS, []
    for k in range(N):
        n = q if k == N - 1 else lots_to_sell(q, pol[k, q])
        sched.append(n * LOT)
        q -= n
    return sched


def almgren_chriss():
    kt2 = LAMBDA * SIGMA ** 2 / ETA                  # kappa-tilde^2 (tau = 1, gamma = 0)
    kappa = math.acosh(1.0 + kt2 / 2.0)              # 2 (cosh kappa - 1) = kappa-tilde^2
    x = [X * math.sinh(kappa * (N - j)) / math.sinh(kappa * N) for j in range(N + 1)]
    n = [x[j - 1] - x[j] for j in range(1, N + 1)]
    return kappa, x, n


def holdings(sched):
    x, h = X, []
    for n in sched:
        x -= n
        h.append(x)
    return h                                          # after each step's sale; last = 0


def analytic(sched):
    """Expected cost E and variance V of a static schedule (A&C eqs. 4-5, linear impact)."""
    E = ETA * sum(n * n for n in sched)
    V = SIGMA ** 2 * sum(x * x for x in holdings(sched)[:-1])
    return E, V


def simulate(sched, xi):
    """Implementation shortfall ($) of a static schedule on each held-out day."""
    sched = np.asarray(sched, float)
    price = S0 + SIGMA * np.concatenate([np.zeros((xi.shape[0], 1)), np.cumsum(xi[:, :-1], axis=1)], axis=1)
    cash = (sched[None, :] * (price - ETA * sched[None, :])).sum(axis=1)
    return NOTIONAL - cash


def summary(is_dollars):
    b = is_dollars * BPS
    return {"mean_usd": round(float(is_dollars.mean()), 2),
            "std_usd": round(float(is_dollars.std()), 2),
            "mean_bps": round(float(b.mean()), 2),
            "std_bps": round(float(b.std()), 2),
            "p05_bps": round(float(np.percentile(b, 5)), 2),
            "p95_bps": round(float(np.percentile(b, 95)), 2)}


def main():
    t0 = time.time()
    lines = []

    def log(s):
        print(s, flush=True)
        lines.append(s)

    log("execution_rl.py -- SYNTHETIC market (random walk + temporary impact). Not real data.")
    log(f"python {platform.python_version()}  numpy {np.__version__}")
    log(f"X={X} shares  S0=${S0}  N={N} steps  lot={LOT}  sigma=${SIGMA}/step  "
        f"eta={ETA} $/share/share  lambda={LAMBDA} 1/$")
    log(f"seeds: train {SEED_TRAIN}, held-out test {SEED_TEST}; practice days {EPISODES:,}; "
        f"held-out days {TEST_DAYS:,}")

    Q, curve = train_q(log)
    rl = greedy_schedule(Q)
    grid = grid_dp()
    kappa, ac_x, ac_n = almgren_chriss()
    dump = [X] + [0] * (N - 1)
    twap = [X // N] * N
    assert sum(rl) == X and sum(grid) == X and abs(sum(ac_n) - X) < 1e-6

    xi = np.random.default_rng(SEED_TEST).standard_normal((TEST_DAYS, N))
    strategies = {"dump": dump, "twap": twap, "rl": rl, "ac": ac_n, "grid": grid}
    out = {}
    for name, sched in strategies.items():
        E, V = analytic(sched)
        s = summary(simulate(sched, xi))
        s.update({"schedule": [round(float(v), 1) for v in sched],
                  "expected_cost_usd": round(E, 2), "expected_cost_bps": round(E * BPS, 2),
                  "std_cost_usd_analytic": round(math.sqrt(V), 2),
                  "std_cost_bps_analytic": round(math.sqrt(V) * BPS, 2),
                  "objective_bps": round((E + LAMBDA * V) * BPS, 3)})
        out[name] = s

    # 40 held-out days for the on-screen price fan (B30): price at each step boundary
    SAMPLE = 40
    paths = S0 + SIGMA * np.concatenate([np.zeros((SAMPLE, 1)), np.cumsum(xi[:SAMPLE], axis=1)], axis=1)
    twap_cost_sample = simulate(twap, xi[:SAMPLE]) * BPS
    sample_days = {"n": SAMPLE, "price_paths": np.round(paths, 4).tolist(),
                   "twap_cost_bps": np.round(twap_cost_sample, 2).tolist(),
                   "worst_twap_day": int(np.argmax(twap_cost_sample))}

    rl_vs_ac = [round(r - a, 1) for r, a in zip(rl, ac_n)]
    results = {
        "title": "How an AI Sells a Big Order -- synthetic market",
        "synthetic": True,
        "params": {"X": X, "S0": S0, "N": N, "lot": LOT, "sigma": SIGMA, "eta": ETA,
                   "lambda": LAMBDA, "fractions": FRACTIONS.tolist(), "episodes": EPISODES,
                   "test_days": TEST_DAYS, "seed_train": SEED_TRAIN, "seed_test": SEED_TEST,
                   "notional_usd": NOTIONAL},
        "ac": {"kappa": round(kappa, 6), "x": [round(v, 1) for v in ac_x],
               "n": [round(v, 1) for v in ac_n]},
        "strategies": out,
        "rl_minus_ac_shares": rl_vs_ac,
        "rl_max_abs_dev_shares": max(abs(v) for v in rl_vs_ac),
        "rl_matches_grid_optimum": rl == grid,
        "rl_objective_gap_vs_ac_pct": round(100 * (out["rl"]["objective_bps"] / out["ac"]["objective_bps"] - 1), 3),
        "training_curve_days_vs_objective_bps": curve,
        "sample_days": sample_days,
        "headline": {
            "dump_cost_bps": out["dump"]["mean_bps"],
            "twap_cost_bps": out["twap"]["mean_bps"],
            "rl_cost_bps": out["rl"]["mean_bps"],
            "twap_p95_bps": out["twap"]["p95_bps"],
            "rl_p95_bps": out["rl"]["p95_bps"],
            "twap_std_bps": out["twap"]["std_bps"],
            "rl_std_bps": out["rl"]["std_bps"],
            "dump_over_rl": round(out["dump"]["mean_bps"] / out["rl"]["mean_bps"], 2),
        },
    }

    log("")
    log(f"Almgren-Chriss kappa = {kappa:.4f} per step  (kappa*N = {kappa * N:.3f})")
    log("step:      " + " ".join(f"{k + 1:>6}" for k in range(N)))
    for name in ("dump", "twap", "rl", "grid", "ac"):
        log(f"{name:<10} " + " ".join(f"{v:>6.0f}" for v in strategies[name]))
    log(f"RL - AC (shares): {rl_vs_ac}   max |dev| = {results['rl_max_abs_dev_shares']}")
    log(f"RL schedule == exact grid optimum: {results['rl_matches_grid_optimum']}")
    log("")
    log(f"held-out simulated days: {TEST_DAYS:,} (seed {SEED_TEST}); cost = implementation shortfall")
    log(f"{'strategy':<8} {'mean bps':>9} {'std bps':>8} {'p95 bps':>8} {'mean $':>9} {'E+lam*V bps':>12}")
    for name in ("dump", "twap", "rl", "ac", "grid"):
        s = out[name]
        log(f"{name:<8} {s['mean_bps']:>9.2f} {s['std_bps']:>8.2f} {s['p95_bps']:>8.2f} "
            f"{s['mean_usd']:>9.0f} {s['objective_bps']:>12.3f}")
    log(f"RL objective vs AC closed form: {results['rl_objective_gap_vs_ac_pct']:+.3f}%")

    canon = json.dumps(results, sort_keys=True, separators=(",", ":"))
    results["results_sha256"] = hashlib.sha256(canon.encode()).hexdigest()
    log(f"results sha256 (canonical, before this field): {results['results_sha256']}")
    print(f"runtime {time.time() - t0:.1f}s (stdout only; not in run.log or results.json)")

    (HERE / "results.json").write_text(json.dumps(results, indent=2) + "\n")
    (HERE / "run.log").write_text("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
