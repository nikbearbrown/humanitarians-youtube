"""The Backtest Mirage -- executable evidence for Boopesh M.'s explainer.

SYNTHETIC NOISE DATA. The "market" is pure random noise: independent daily returns, mean 0, 1% daily
volatility. Every trading rule below only looks at PAST returns, and tomorrow's return is independent of the
past with mean 0, so every rule has a true edge (expected return, true Sharpe ratio) of exactly ZERO by
construction. Any Sharpe ratio a rule shows is luck.

Setup: 5 years in-sample (252 trading days/yr -> 1,260 days) that the search may look at, then 2 years
out-of-sample (504 days) that it never touches. A simple automated "strategy search" tries N random rules:
    rule k picks a lookback L_k (2..20 days) and random weights w_k;
    position_t = sign( sum_i w_k,i * r_{t-i} )   (+1 = long, -1 = short), pnl_t = position_t * r_t.
No trading costs (a limit: costs would only make the out-of-sample result worse).

Outputs:
  * main world (seed 42): 10,000 rules -> in-sample / out-of-sample Sharpe of each, the in-sample winner,
    the best in-sample Sharpe among the first N rules for N = 1, 10, 100, 1,000, 10,000, equity curves;
  * 200 fresh noise worlds (seeds spawned from 42): the same search each time -> median best in-sample
    Sharpe vs N, the winner's average out-of-sample Sharpe, and the 95th percentile ("the bar to beat");
  * theory for N INDEPENDENT trials: expected best Sharpe = E[max of N standard normals] / sqrt(years),
    and the standard error of an annualised Sharpe ratio near zero, about 1 / sqrt(years).

Run:  python backtest_mirage.py > run.log     -> results.json, curves.npz
"""
import json
import math
import time
from pathlib import Path
from statistics import NormalDist

import numpy as np

SEED = 42
YEAR = 252
DAYS_IS, DAYS_OOS = 5 * YEAR, 2 * YEAR
MAXLAG = 20
VOL = 0.01
N_RULES = 10_000
N_WORLDS = 200
N_GRID = [1, 3, 10, 30, 45, 100, 300, 1000, 3000, 10_000]
N_SHOW = [1, 10, 100, 1000, 10_000]
HERE = Path(__file__).resolve().parent


def make_world(rng):
    r = rng.normal(0.0, VOL, MAXLAG + DAYS_IS + DAYS_OOS)          # pure noise, zero edge
    lags = rng.integers(2, MAXLAG + 1, N_RULES)                       # each rule's lookback
    W = rng.normal(0.0, 1.0, (MAXLAG, N_RULES))
    W[np.arange(MAXLAG)[:, None] >= lags[None, :]] = 0.0              # only the last L_k days count
    return r, lags, W


def sharpes(r, W, chunk=2500):
    """Annualised in-sample and out-of-sample Sharpe ratio of every rule (columns of W)."""
    T = DAYS_IS + DAYS_OOS
    X = np.stack([r[MAXLAG - i: MAXLAG - i + T] for i in range(1, MAXLAG + 1)], axis=1)   # X[t, i-1] = r_{t-i}
    y = r[MAXLAG:]
    s_is, s_oos = np.empty(W.shape[1]), np.empty(W.shape[1])
    for a in range(0, W.shape[1], chunk):
        pos = np.sign(X @ W[:, a:a + chunk])
        pos[pos == 0] = 1.0
        pnl = pos * y[:, None]
        for out, part in ((s_is, pnl[:DAYS_IS]), (s_oos, pnl[DAYS_IS:])):
            out[a:a + chunk] = part.mean(0) / part.std(0, ddof=1) * math.sqrt(YEAR)
    return s_is, s_oos


def pnl_of(r, w):
    T = DAYS_IS + DAYS_OOS
    X = np.stack([r[MAXLAG - i: MAXLAG - i + T] for i in range(1, MAXLAG + 1)], axis=1)
    pos = np.sign(X @ w)
    pos[pos == 0] = 1.0
    return pos * r[MAXLAG:]


def best_of_first(s_is, s_oos, n):
    k = int(np.argmax(s_is[:n]))
    return k, float(s_is[k]), float(s_oos[k])


def expected_max_normal(n):
    """E[max of n independent N(0,1)] by numerical integration (numpy + math.erf only)."""
    x = np.linspace(-8, 8, 160_001)
    pdf = np.exp(-x * x / 2) / math.sqrt(2 * math.pi)
    cdf = 0.5 * (1 + np.vectorize(math.erf)(x / math.sqrt(2)))
    dens = n * pdf * cdf ** (n - 1)
    return float(np.sum(x * dens) * (x[1] - x[0]))


def main():
    t0 = time.time()
    years_is = DAYS_IS / YEAR
    print(f"numpy {np.__version__}  seed {SEED}  SYNTHETIC NOISE DATA: iid N(0, {VOL}) daily returns, zero edge")
    print(f"in-sample {DAYS_IS} days ({years_is:.0f} y)  out-of-sample {DAYS_OOS} days ({DAYS_OOS / YEAR:.0f} y)  "
          f"rules {N_RULES}  lookback 2..{MAXLAG}  worlds {N_WORLDS}")

    # ---------------- main world -------------------------------------------------------------------
    ss = np.random.SeedSequence(SEED)
    main_ss, *world_ss = ss.spawn(1 + N_WORLDS)
    rng = np.random.default_rng(main_ss)
    r, lags, W = make_world(rng)
    s_is, s_oos = sharpes(r, W)
    win, win_is, win_oos = best_of_first(s_is, s_oos, N_RULES)
    pnl = pnl_of(r, W[:, win])
    market_is_sr = float(r[MAXLAG:MAXLAG + DAYS_IS].mean() / r[MAXLAG:MAXLAG + DAYS_IS].std(ddof=1) * math.sqrt(YEAR))
    print(f"\nMAIN WORLD  market buy-and-hold in-sample Sharpe {market_is_sr:+.3f}")
    print(f"  all {N_RULES} rules: in-sample Sharpe mean {s_is.mean():+.3f} sd {s_is.std():.3f}  "
          f"out-of-sample mean {s_oos.mean():+.3f} sd {s_oos.std():.3f}")
    corr = float(np.corrcoef(s_is, s_oos)[0, 1])
    print(f"  correlation(in-sample Sharpe, out-of-sample Sharpe) over {N_RULES} rules: {corr:+.3f}")
    print(f"  rules with in-sample Sharpe >= 1: {(s_is >= 1).sum()}   >= 1.5: {(s_is >= 1.5).sum()}")
    print(f"  WINNER rule #{win} (lookback {lags[win]} days): in-sample Sharpe {win_is:+.3f}  "
          f"out-of-sample Sharpe {win_oos:+.3f}")
    print(f"  winner return: in-sample {pnl[:DAYS_IS].sum():+.1%} (5 y, simple sum)  "
          f"out-of-sample {pnl[DAYS_IS:].sum():+.1%} (2 y)")
    main_grid = []
    for n in N_GRID:
        k, a, b = best_of_first(s_is, s_oos, n)
        main_grid.append({"n": n, "rule": k, "best_is_sharpe": a, "its_oos_sharpe": b})
        print(f"  best of first {n:>6}: rule #{k:<5} in-sample {a:+.3f}  out-of-sample {b:+.3f}")

    # ---------------- 200 fresh noise worlds ----------------------------------------------------------
    best_is = np.empty((N_WORLDS, len(N_GRID)))
    best_oos = np.empty((N_WORLDS, len(N_GRID)))
    sd_is = np.empty(N_WORLDS)
    corr_w = np.empty(N_WORLDS)
    for w_i, wss in enumerate(world_ss):
        rr, _, WW = make_world(np.random.default_rng(wss))
        a_is, a_oos = sharpes(rr, WW)
        sd_is[w_i] = a_is.std()
        corr_w[w_i] = np.corrcoef(a_is, a_oos)[0, 1]
        for j, n in enumerate(N_GRID):
            _, best_is[w_i, j], best_oos[w_i, j] = best_of_first(a_is, a_oos, n)
    print(f"\n{N_WORLDS} FRESH NOISE WORLDS (same search each time)")
    print(f"  spread (sd) of in-sample Sharpe across rules, averaged over worlds: {sd_is.mean():.3f}  "
          f"(theory 1/sqrt({years_is:.0f}) = {1 / math.sqrt(years_is):.3f})")
    print(f"  correlation(in-sample, out-of-sample Sharpe) across rules: mean over worlds {corr_w.mean():+.3f}  "
          f"(5-95%: {np.quantile(corr_w, 0.05):+.2f}..{np.quantile(corr_w, 0.95):+.2f})")
    allw = best_oos[:, -1]
    print(f"  10,000-rule winner, out-of-sample: mean {allw.mean():+.3f}, below zero in {(allw < 0).mean():.0%} of worlds; "
          f"mean over all N values {best_oos.mean():+.3f}")
    se = 1 / math.sqrt(years_is)
    worlds = []
    for j, n in enumerate(N_GRID):
        th = expected_max_normal(n) * se
        bar_ind = NormalDist().inv_cdf(0.95 ** (1 / n)) * se
        row = {"n": n,
               "best_is_median": float(np.median(best_is[:, j])),
               "best_is_mean": float(best_is[:, j].mean()),
               "best_is_p05": float(np.quantile(best_is[:, j], 0.05)),
               "best_is_p95": float(np.quantile(best_is[:, j], 0.95)),
               "winner_oos_mean": float(best_oos[:, j].mean()),
               "winner_oos_median": float(np.median(best_oos[:, j])),
               "winner_oos_se": float(best_oos[:, j].std(ddof=1) / math.sqrt(N_WORLDS)),
               "share_winner_oos_below_zero": float((best_oos[:, j] < 0).mean()),
               "theory_independent_expected_best": th,
               "theory_independent_bar95": bar_ind}
        worlds.append(row)
        print(f"  N {n:>6}: best in-sample median {row['best_is_median']:+.3f} (5-95%: {row['best_is_p05']:+.2f}.."
              f"{row['best_is_p95']:+.2f})  winner out-of-sample mean {row['winner_oos_mean']:+.3f} "
              f"(se {row['winner_oos_se']:.3f})  | independent-trials theory: expected best {th:.3f}, "
              f"95% bar {bar_ind:.3f}")

    res = {"setup": {"synthetic_noise_data": True, "seed": SEED, "numpy_version": np.__version__,
                     "daily_vol": VOL, "true_edge": 0.0, "days_per_year": YEAR,
                     "days_in_sample": DAYS_IS, "days_out_of_sample": DAYS_OOS,
                     "years_in_sample": years_is, "years_out_of_sample": DAYS_OOS / YEAR,
                     "n_rules": N_RULES, "lookback_days": [2, MAXLAG], "n_worlds": N_WORLDS,
                     "rule": "position_t = sign(sum_i w_i r_{t-i}), i = 1..L, random w ~ N(0,1), L ~ U{2..20}",
                     "costs": "none", "sharpe": "mean/sd of daily pnl x sqrt(252)",
                     "sharpe_se_theory": se},
           "main_world": {"market_is_sharpe": market_is_sr, "is_sharpe_mean": float(s_is.mean()),
                          "is_sharpe_sd": float(s_is.std()), "oos_sharpe_mean": float(s_oos.mean()),
                          "oos_sharpe_sd": float(s_oos.std()), "corr_is_oos": corr,
                          "n_is_sharpe_ge_1": int((s_is >= 1).sum()),
                          "n_is_sharpe_ge_1_5": int((s_is >= 1.5).sum()),
                          "winner": {"rule": win, "lookback": int(lags[win]), "is_sharpe": win_is,
                                     "oos_sharpe": win_oos, "is_return_sum": float(pnl[:DAYS_IS].sum()),
                                     "oos_return_sum": float(pnl[DAYS_IS:].sum())},
                          "best_of_first": main_grid},
           "worlds": worlds,
           "worlds_is_sharpe_sd_mean": float(sd_is.mean()),
           "worlds_corr_is_oos_mean": float(corr_w.mean()),
           "worlds_corr_is_oos_p05_p95": [float(np.quantile(corr_w, 0.05)), float(np.quantile(corr_w, 0.95))],
           "worlds_winner_oos_mean_all_n": float(best_oos.mean()),
           "n_show": N_SHOW}
    np.savez_compressed(HERE / "curves.npz", is_sharpe=s_is, oos_sharpe=s_oos, market=r[MAXLAG:],
                        winner_pnl=pnl, best_is_worlds=best_is, best_oos_worlds=best_oos,
                        n_grid=np.array(N_GRID))
    res["runtime_s"] = round(time.time() - t0, 1)
    (HERE / "results.json").write_text(json.dumps(res, indent=2) + "\n")
    print(f"\nwrote results.json, curves.npz in {res['runtime_s']} s")


if __name__ == "__main__":
    main()
