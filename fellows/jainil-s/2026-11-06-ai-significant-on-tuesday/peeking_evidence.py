"""
Evidence for "Significant On Tuesday" — what repeated significance testing
does to an A/B test's false-positive rate.

Every number quoted in the reel comes from this file. Run it and the numbers
reproduce exactly: one seeded Generator, no hidden state, no wall clock.

    python peeking_evidence.py

The design, in one line: simulate A/A tests where the two arms are IDENTICAL
by construction, then count how often each stopping rule declares a winner.
Any "winner" is a false positive, because there is nothing to win.
"""

import json
import numpy as np

SEED = 20261106
RNG = np.random.default_rng(SEED)

N_SIM = 20_000       # simulated experiments per condition
N_MAX = 2_000        # visitors per arm at the full horizon
LOOK_EVERY = 100     # a peek every 100 visitors per arm -> 20 looks
BASE_RATE = 0.10     # conversion rate, identical in both arms (the null)
ALPHA = 0.05
Z_CRIT = 1.959963985 # two-sided 5%

LOOKS = np.arange(LOOK_EVERY, N_MAX + 1, LOOK_EVERY)   # 100, 200, ... 2000


def simulate_cumulative(n_sim, n_max, look_every, rate_a, rate_b, rng):
    """Conversions per arm at each look point.

    Drawn in chunks so memory stays flat: we never hold all n_sim x n_max
    Bernoulli draws at once, only the running totals at the look points.
    Returns two (n_sim, n_looks) int arrays of CUMULATIVE conversions.
    """
    n_looks = n_max // look_every
    cum_a = np.empty((n_sim, n_looks), dtype=np.int32)
    cum_b = np.empty((n_sim, n_looks), dtype=np.int32)
    run_a = np.zeros(n_sim, dtype=np.int32)
    run_b = np.zeros(n_sim, dtype=np.int32)
    for k in range(n_looks):
        run_a += rng.binomial(look_every, rate_a, size=n_sim)
        run_b += rng.binomial(look_every, rate_b, size=n_sim)
        cum_a[:, k] = run_a
        cum_b[:, k] = run_b
    return cum_a, cum_b


def z_scores(cum_a, cum_b, looks):
    """Two-proportion z at every look. Equal arm sizes, pooled variance.

    A look with zero conversions in both arms has no variance and no
    information; it yields z = 0 rather than a divide-by-zero, which is the
    honest reading (such a look can never be significant anyway).
    """
    n = looks[None, :].astype(np.float64)
    pa = cum_a / n
    pb = cum_b / n
    pooled = (cum_a + cum_b) / (2.0 * n)
    var = pooled * (1.0 - pooled) * (2.0 / n)
    se = np.sqrt(var)
    z = np.zeros_like(pa)
    ok = se > 0
    z[ok] = (pa[ok] - pb[ok]) / se[ok]
    return z, pa, pb


def first_crossing(sig):
    """Index of the first True per row, or -1 if a row never crosses."""
    any_sig = sig.any(axis=1)
    first = np.where(any_sig, sig.argmax(axis=1), -1)
    return first, any_sig


def rate_ci(k, n):
    """Wilson 95% interval — the honest error bar on a simulated rate."""
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    z = Z_CRIT
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return (max(0.0, centre - half), min(1.0, centre + half))


results = {}
print(f"seed={SEED}  sims={N_SIM:,}  arm size={N_MAX:,}  looks every {LOOK_EVERY}")
print(f"both arms converting at {BASE_RATE:.0%} — there is NO real difference\n")

# ---------------------------------------------------------------- the null
cum_a, cum_b = simulate_cumulative(N_SIM, N_MAX, LOOK_EVERY, BASE_RATE, BASE_RATE, RNG)
z, pa, pb = z_scores(cum_a, cum_b, LOOKS)
sig = np.abs(z) > Z_CRIT

# 1. One look at the end — the test as designed.
fixed_fp = sig[:, -1].mean()
results["fixed_horizon_fpr"] = float(fixed_fp)
lo, hi = rate_ci(int(sig[:, -1].sum()), N_SIM)
print(f"1. ONE look, at n={N_MAX}        false positives: {fixed_fp:6.2%}  [{lo:.2%}, {hi:.2%}]")

# 2. Peek at all 20 looks, stop the moment it crosses.
first, any_sig = first_crossing(sig)
peek_fp = any_sig.mean()
results["peeking_20_looks_fpr"] = float(peek_fp)
lo, hi = rate_ci(int(any_sig.sum()), N_SIM)
print(f"2. {len(LOOKS)} looks, stop at first  false positives: {peek_fp:6.2%}  [{lo:.2%}, {hi:.2%}]")
print(f"   -> {peek_fp / fixed_fp:.1f}x the advertised rate\n")

# 3. How the damage scales with the number of looks.
print("3. false positives by number of looks (evenly spaced, same horizon)")
by_looks = {}
for n_looks in (1, 2, 4, 5, 10, 20):
    step = len(LOOKS) // n_looks
    cols = np.arange(step - 1, len(LOOKS), step)[:n_looks]
    r = float(sig[:, cols].any(axis=1).mean())
    by_looks[n_looks] = r
    bar = "#" * int(round(r * 120))
    print(f"   {n_looks:2d} look{'s' if n_looks > 1 else ' '}  {r:6.2%}  {bar}")
results["fpr_by_n_looks"] = by_looks

# 4. Peeking every 10 visitors, the "live dashboard" case.
cum_a2, cum_b2 = simulate_cumulative(N_SIM, N_MAX, 10, BASE_RATE, BASE_RATE, RNG)
looks2 = np.arange(10, N_MAX + 1, 10)
z2, _, _ = z_scores(cum_a2, cum_b2, looks2)
# ignore the first 500 visitors/arm: the normal approximation is not usable there
usable = looks2 >= 500
daily_fp = float((np.abs(z2[:, usable]) > Z_CRIT).any(axis=1).mean())
results["dashboard_peeking_fpr"] = daily_fp
results["dashboard_n_looks"] = int(usable.sum())
print(f"\n4. a dashboard refreshing every 10 visitors ({int(usable.sum())} looks from n=500)")
print(f"   false positives: {daily_fp:6.2%}\n")

# ---------------------------------------------------------- winner's curse
# Among the runs that DID stop "significant", how big did the effect look?
stopped = first >= 0
idx = first[stopped]
rows = np.arange(N_SIM)[stopped]
lift = np.abs(pa[rows, idx] - pb[rows, idx])          # absolute pp difference
rel = lift / BASE_RATE                                 # as a % of baseline
stop_n = LOOKS[idx]
results["curse_median_abs_lift_pp"] = float(np.median(lift) * 100)
results["curse_median_rel_lift_pct"] = float(np.median(rel) * 100)
results["curse_median_stop_n"] = int(np.median(stop_n))
results["curse_share_stopping_by_half"] = float((stop_n <= N_MAX / 2).mean())
print("5. the winner's curse — among the runs that stopped 'significant',")
print("   with a TRUE difference of exactly zero:")
print(f"   median measured lift : {np.median(lift) * 100:.2f} pp "
      f"({np.median(rel) * 100:.0f}% of baseline)")
print(f"   median stopping point: n={int(np.median(stop_n))} per arm")
print(f"   {(stop_n <= N_MAX / 2).mean():.0%} of them stopped in the first half of the test\n")

# ------------------------------------------------------------- the repairs
# Bonferroni: split alpha across the looks. Simple, and over-corrects.
z_bonf = float(-__import__("scipy.stats", fromlist=["norm"]).norm.ppf(
    ALPHA / (2 * len(LOOKS))))
bonf_fp = float((np.abs(z) > z_bonf).any(axis=1).mean())
results["bonferroni_z"] = z_bonf
results["bonferroni_fpr"] = bonf_fp

# Pocock-style: ONE constant boundary, calibrated by simulation so that the
# whole 20-look procedure spends exactly 5%. Found on a separate sample so the
# boundary is not fitted to the data it is then scored on.
cal_a, cal_b = simulate_cumulative(N_SIM, N_MAX, LOOK_EVERY, BASE_RATE, BASE_RATE, RNG)
z_cal, _, _ = z_scores(cal_a, cal_b, LOOKS)
peak_cal = np.abs(z_cal).max(axis=1)
z_pocock = float(np.quantile(peak_cal, 1 - ALPHA))
pocock_fp = float((np.abs(z) > z_pocock).any(axis=1).mean())
results["pocock_z"] = z_pocock
results["pocock_fpr"] = pocock_fp
print("6. two repairs, both scored on the held-out null runs")
print(f"   naive         z > {Z_CRIT:.2f}   false positives {peek_fp:6.2%}")
print(f"   Bonferroni    z > {z_bonf:.2f}   false positives {bonf_fp:6.2%}  (over-corrected)")
print(f"   calibrated    z > {z_pocock:.2f}   false positives {pocock_fp:6.2%}  (on target)\n")

# --------------------------------------------------- what the repair costs
# Now give the test a REAL effect and measure power + sample size.
#
# The comparison that matters is NOT "same horizon, who wins" — a stricter
# boundary at a fixed horizon is strictly worse, and quoting that alone would
# make the correct procedure look like a pure penalty. The real choice is
# between two procedures RUN AT THE SAME POWER. So: hold power fixed, and
# compare how many visitors each one actually spends.
TRUE_B = 0.12
pw_a, pw_b = simulate_cumulative(N_SIM, N_MAX, LOOK_EVERY, BASE_RATE, TRUE_B, RNG)
z_pw, _, _ = z_scores(pw_a, pw_b, LOOKS)
fixed_power = float((np.abs(z_pw[:, -1]) > Z_CRIT).mean())

# Same horizon, stricter boundary — the naive framing, reported for honesty.
seq_sig = np.abs(z_pw) > z_pocock
seq_first, seq_any = first_crossing(seq_sig)
same_horizon_power = float(seq_any.mean())
same_horizon_avg_n = float(np.where(seq_any, LOOKS[seq_first], N_MAX).mean())

# Matched power: extend the sequential horizon until it reaches the fixed
# test's power, then ask what it SPENDS. The Pocock-style boundary depends on
# the number of looks, not the horizon, so 20 looks keeps z* = z_pocock.
matched = None
for horizon in range(N_MAX, 4 * N_MAX + 1, 100):
    step = horizon // len(LOOKS)
    ha, hb = simulate_cumulative(N_SIM, step * len(LOOKS), step,
                                 BASE_RATE, TRUE_B, RNG)
    hlooks = np.arange(step, step * len(LOOKS) + 1, step)
    hz, _, _ = z_scores(ha, hb, hlooks)
    hfirst, hany = first_crossing(np.abs(hz) > z_pocock)
    hpower = float(hany.mean())
    if hpower >= fixed_power:
        stops = np.where(hany, hlooks[hfirst], hlooks[-1])
        matched = {
            "horizon": int(hlooks[-1]),
            "power": hpower,
            "avg_n": float(stops.mean()),
            "median_n_when_detected": int(np.median(hlooks[hfirst][hany])),
        }
        break

results["true_effect"] = [BASE_RATE, TRUE_B]
results["fixed_power"] = fixed_power
results["fixed_avg_n"] = N_MAX
results["same_horizon_power"] = same_horizon_power
results["same_horizon_avg_n"] = same_horizon_avg_n
results["matched_power_sequential"] = matched
print(f"7. with a REAL effect ({BASE_RATE:.0%} vs {TRUE_B:.0%})")
print(f"   fixed, one look at n={N_MAX}     : power {fixed_power:.1%}, "
      f"always n={N_MAX}")
print(f"   sequential, SAME horizon      : power {same_horizon_power:.1%}, "
      f"avg n={same_horizon_avg_n:.0f}   (strictly worse — the naive framing)")
if matched:
    results["matched_n_saved_pct"] = float(100 * (1 - matched["avg_n"] / N_MAX))
    print(f"   sequential, MATCHED power     : power {matched['power']:.1%}, "
          f"avg n={matched['avg_n']:.0f}, cap n={matched['horizon']}")
    print(f"   -> same error rate, same power, "
          f"{100 * (1 - matched['avg_n'] / N_MAX):.0f}% fewer visitors on average;")
    print(f"      when the effect is real it is called at a median of "
          f"n={matched['median_n_when_detected']}\n")
else:
    print("   sequential never matched the fixed test's power within 4x horizon\n")

# ------------------------------------------------------- one hero trajectory
# A single A/A run that crosses the line early and comes back: the picture the
# reel is built on. Picked as the FIRST run (lowest index) that is significant
# at some look and clearly not significant at the horizon.
crossed_early = sig[:, :10].any(axis=1)
settled = np.abs(z[:, -1]) < 1.0
cand = np.where(crossed_early & settled)[0]
hero = int(cand[0])
results["hero_index"] = hero
results["hero_z"] = [round(float(v), 3) for v in z[hero]]
results["hero_looks"] = [int(v) for v in LOOKS]
hero_first = int(np.argmax(sig[hero]))
results["hero_cross_n"] = int(LOOKS[hero_first])
results["hero_cross_z"] = float(z[hero, hero_first])
results["hero_final_z"] = float(z[hero, -1])
print(f"8. hero run #{hero}: crosses at n={LOOKS[hero_first]} "
      f"(z={z[hero, hero_first]:+.2f}), "
      f"ends at n={N_MAX} with z={z[hero, -1]:+.2f}")
print("   z by look:", " ".join(f"{v:+.2f}" for v in z[hero]))

with open("peeking_results.json", "w", encoding="utf-8") as fh:
    json.dump(results, fh, indent=2)
print("\nwrote peeking_results.json")
