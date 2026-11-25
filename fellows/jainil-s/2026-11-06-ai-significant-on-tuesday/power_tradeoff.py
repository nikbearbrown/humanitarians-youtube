"""
Addendum to peeking_evidence.py §7.

The first pass compared a group-sequential test to a fixed test at matched
power and found sequential spending MORE visitors on average (2189 vs 2000).
That contradicts the usual "sequential testing saves sample size" claim, so
it gets checked properly rather than quietly dropped.

Hypothesis: the saving depends on POWER. When power is low most runs never
cross and pay the full (larger) cap; when power is high most runs cross early
and the average falls below the fixed test's fixed cost.

Same seed discipline as the main script.
"""

import numpy as np
from scipy.stats import norm

SEED = 20261106
RNG = np.random.default_rng(SEED + 1)
N_SIM = 20_000
N_LOOKS = 20
BASE = 0.10
ALPHA = 0.05
Z_CRIT = 1.959963985
Z_POCOCK = 2.67          # calibrated in peeking_evidence.py §6 for 20 looks


def run(horizon, rate_b, rng, n_sim=N_SIM):
    """Cumulative z at N_LOOKS evenly spaced looks over `horizon`."""
    step = horizon // N_LOOKS
    looks = np.arange(step, step * N_LOOKS + 1, step)
    run_a = np.zeros(n_sim, dtype=np.int64)
    run_b = np.zeros(n_sim, dtype=np.int64)
    zs = np.empty((n_sim, N_LOOKS))
    for k in range(N_LOOKS):
        run_a += rng.binomial(step, BASE, size=n_sim)
        run_b += rng.binomial(step, rate_b, size=n_sim)
        n = looks[k]
        pa, pb = run_a / n, run_b / n
        pooled = (run_a + run_b) / (2.0 * n)
        se = np.sqrt(pooled * (1 - pooled) * (2.0 / n))
        zs[:, k] = np.where(se > 0, (pa - pb) / np.where(se > 0, se, 1), 0.0)
    return zs, looks


def fixed_n_for_power(p1, p2, power):
    """Textbook two-proportion sample size, used only to pick a horizon."""
    za = norm.ppf(1 - ALPHA / 2)
    zb = norm.ppf(power)
    pbar = (p1 + p2) / 2
    n = (za * np.sqrt(2 * pbar * (1 - pbar)) +
         zb * np.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p1 - p2) ** 2
    return int(np.ceil(n / N_LOOKS) * N_LOOKS)


print(f"{'target':>7} {'effect':>14} {'fixed n':>9} {'fixed pw':>9} "
      f"{'seq cap':>9} {'seq pw':>8} {'seq avg n':>10} {'vs fixed':>10}")
print("-" * 84)

rows = []
for rate_b in (0.12, 0.13):
    for target in (0.50, 0.65, 0.80, 0.90, 0.95):
        n_fixed = fixed_n_for_power(BASE, rate_b, target)
        zf, looks_f = run(n_fixed, rate_b, np.random.default_rng(SEED + 7))
        fixed_pw = float((np.abs(zf[:, -1]) > Z_CRIT).mean())

        # grow the sequential cap until it matches the fixed test's power
        best = None
        for mult in np.arange(1.0, 2.01, 0.05):
            cap = int(np.ceil(n_fixed * mult / N_LOOKS) * N_LOOKS)
            zs, looks = run(cap, rate_b, np.random.default_rng(SEED + 99))
            sig = np.abs(zs) > Z_POCOCK
            any_sig = sig.any(axis=1)
            pw = float(any_sig.mean())
            if pw >= fixed_pw:
                stops = np.where(any_sig, looks[sig.argmax(axis=1)], looks[-1])
                best = (cap, pw, float(stops.mean()))
                break
        if best is None:
            print(f"{target:>7.0%} {BASE:.0%} vs {rate_b:.0%}  "
                  f"{n_fixed:>9} {fixed_pw:>8.1%}   (no match within 2x)")
            continue
        cap, pw, avg = best
        delta = 100 * (avg / n_fixed - 1)
        rows.append((target, rate_b, n_fixed, fixed_pw, cap, pw, avg, delta))
        print(f"{target:>7.0%} {BASE:>6.0%} vs {rate_b:<5.0%} {n_fixed:>9,} "
              f"{fixed_pw:>8.1%} {cap:>9,} {pw:>7.1%} {avg:>10,.0f} "
              f"{delta:>+9.0f}%")

print()
wins = [r for r in rows if r[-1] < 0]
if wins:
    first = min(wins, key=lambda r: r[0])
    print(f"Sequential starts paying for itself at ~{first[0]:.0%} power "
          f"({first[-1]:+.0f}% visitors).")
else:
    print("Sequential never spends fewer visitors in this range.")
print("At low power most runs never cross, so they pay the larger cap in full.")
