"""
Turns the simulation into the exact arrays the beat sheet puts on screen.

Nothing here invents a number: every value is read off the same seeded run as
peeking_evidence.py. Written separately so the evidence script stays readable
as an argument, and so the on-screen data has one obvious origin.
"""

import json
import numpy as np

SEED = 20261106
RNG = np.random.default_rng(SEED)
N_SIM = 20_000
N_MAX = 2_000
LOOK_EVERY = 100
BASE_RATE = 0.10
Z_CRIT = 1.959963985
LOOKS = np.arange(LOOK_EVERY, N_MAX + 1, LOOK_EVERY)

run_a = np.zeros(N_SIM, dtype=np.int32)
run_b = np.zeros(N_SIM, dtype=np.int32)
cum_a = np.empty((N_SIM, len(LOOKS)), dtype=np.int32)
cum_b = np.empty((N_SIM, len(LOOKS)), dtype=np.int32)
for k in range(len(LOOKS)):
    run_a += RNG.binomial(LOOK_EVERY, BASE_RATE, size=N_SIM)
    run_b += RNG.binomial(LOOK_EVERY, BASE_RATE, size=N_SIM)
    cum_a[:, k] = run_a
    cum_b[:, k] = run_b

n = LOOKS[None, :].astype(float)
pa, pb = cum_a / n, cum_b / n
pooled = (cum_a + cum_b) / (2.0 * n)
se = np.sqrt(pooled * (1 - pooled) * (2.0 / n))
z = np.where(se > 0, (pa - pb) / np.where(se > 0, se, 1), 0.0)
sig = np.abs(z) > Z_CRIT
any_sig = sig.any(axis=1)
first = np.where(any_sig, sig.argmax(axis=1), -1)

out = {}

# ---- B02: the hero run -----------------------------------------------------
crossed_early = sig[:, :10].any(axis=1)
settled = np.abs(z[:, -1]) < 1.0
hero = int(np.where(crossed_early & settled)[0][0])
hero_first = int(np.argmax(sig[hero]))
out["hero"] = {
    "index": hero,
    "z": [round(float(v), 2) for v in z[hero]],
    "looks": [int(v) for v in LOOKS],
    "cross_at_n": int(LOOKS[hero_first]),
    "cross_z": round(float(z[hero, hero_first]), 2),
    "final_z": round(float(z[hero, -1]), 2),
    "n_crossings_naive": int(sig[hero].sum()),
    "n_crossings_calibrated": int((np.abs(z[hero]) > 2.67).sum()),
}

# ---- B03: false positives by number of looks -------------------------------
by_looks = []
for n_looks in (1, 2, 5, 10, 20):
    step = len(LOOKS) // n_looks
    cols = np.arange(step - 1, len(LOOKS), step)[:n_looks]
    r = float(sig[:, cols].any(axis=1).mean())
    by_looks.append({"label": f"{n_looks} look" + ("s" if n_looks > 1 else ""),
                     "value": round(r * 100, 1)})
out["fpr_by_looks"] = by_looks

# ---- B04: the winner's curse ----------------------------------------------
# SIGNED measured difference at the moment each run stopped. The hole at zero
# is the finding: a run never stops early with a small measured effect, because
# a small effect is not significant at a small n.
stopped = first >= 0
rows = np.arange(N_SIM)[stopped]
idx = first[stopped]
signed = (pa[rows, idx] - pb[rows, idx]) * 100          # percentage points
# Range chosen to hold the tails, not to flatter the shape: at +/-8pp a sixth
# of the mass fell outside and np.histogram DROPS it, so both lobes rendered
# as if they ended where the axis did. +/-15pp holds 99.8%, and the remainder
# is clipped into the end bins rather than discarded.
LIMIT = 15.0
edges = np.linspace(-LIMIT, LIMIT, 41)
hist, _ = np.histogram(np.clip(signed, -LIMIT, LIMIT), bins=edges)
assert hist.sum() == len(signed), "histogram dropped mass"
curve = hist / hist.max()
out["curse"] = {
    "curve": [round(float(v), 3) for v in curve],
    "x_left": f"-{LIMIT:.0f} pp",
    "x_right": f"+{LIMIT:.0f} pp",
    "outside_range_pct": round(float((np.abs(signed) > LIMIT).mean()) * 100, 2),
    "n_bins": len(curve),
    "median_abs_pp": round(float(np.median(np.abs(signed))), 2),
    "min_abs_pp": round(float(np.min(np.abs(signed))), 2),
    "share_above_2pp": round(float((np.abs(signed) >= 2).mean()) * 100, 1),
    "median_stop_n": int(np.median(LOOKS[idx])),
    "truth_pp": 0.0,
    # where zero sits as a fraction of the x axis, for the mark
    "zero_frac": round(float((0 - edges[0]) / (edges[-1] - edges[0])), 3),
}
# the empty middle, measured rather than eyeballed
near_zero = (np.abs(signed) < 1.5).mean()
out["curse"]["share_within_1_5pp"] = round(float(near_zero) * 100, 2)

# ---- B05: the three boundaries ---------------------------------------------
from scipy.stats import norm
z_bonf = float(-norm.ppf(0.05 / (2 * len(LOOKS))))
cal_a = np.zeros(N_SIM, dtype=np.int32)
cal_b = np.zeros(N_SIM, dtype=np.int32)
zc = np.empty((N_SIM, len(LOOKS)))
for k in range(len(LOOKS)):
    cal_a += RNG.binomial(LOOK_EVERY, BASE_RATE, size=N_SIM)
    cal_b += RNG.binomial(LOOK_EVERY, BASE_RATE, size=N_SIM)
    nn = LOOKS[k]
    ppa, ppb = cal_a / nn, cal_b / nn
    pl = (cal_a + cal_b) / (2.0 * nn)
    s = np.sqrt(pl * (1 - pl) * (2.0 / nn))
    zc[:, k] = np.where(s > 0, (ppa - ppb) / np.where(s > 0, s, 1), 0.0)
z_pocock = float(np.quantile(np.abs(zc).max(axis=1), 0.95))
out["boundaries"] = [
    {"label": "z > 1.96", "note": "the textbook line",
     "value": round(float(any_sig.mean()) * 100, 1)},
    {"label": f"z > {z_bonf:.2f}", "note": "Bonferroni",
     "value": round(float((np.abs(z) > z_bonf).any(axis=1).mean()) * 100, 1)},
    {"label": f"z > {z_pocock:.2f}", "note": "calibrated for 20 looks",
     "value": round(float((np.abs(z) > z_pocock).any(axis=1).mean()) * 100, 1)},
]
out["z_pocock"] = round(z_pocock, 2)
out["z_bonf"] = round(z_bonf, 2)

with open("beat_data.json", "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=2)

print(json.dumps(out, indent=2)[:2600])
