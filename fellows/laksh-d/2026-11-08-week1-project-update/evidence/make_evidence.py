"""Compute every number and curve the video shows, from lakshdhamija/rl-autoscaler @ 8b126bd.

Run inside the rl-autoscaler venv (Python 3.11, package rl_autoscaler installed):
    cd rl-autoscaler && source .venv/bin/activate
    python <reel>/evidence/make_evidence.py
Writes evidence.json next to this file, then embeds it into ../scenes.py between the
EVIDENCE markers (scenes.py must be self-contained: the QC gates copy it to a temp dir).
Reads only the repo's processed data; writes nothing inside the repo.
"""

import json
import re
from pathlib import Path

import numpy as np

from rl_autoscaler.data import episodes, load, train_series, TRAIN_MINUTES
from rl_autoscaler.env import AutoscaleEnv
from rl_autoscaler.policies import SeasonalPolicy, ThresholdPolicy, rollout
from rl_autoscaler.traffic import REPEAT_WINDOW, FittedTraffic, find_bursts, measure

HERE = Path(__file__).resolve().parent
apps, meta = load()
r = lambda a, k=0: [round(float(v), k) if k else int(round(float(v))) for v in a]

# 19 apps, hourly means over 14 days, each scaled to its own max (shape only)
grid = []
for name in meta["train_apps"] + meta["test_apps"]:
    hourly = apps[name].reshape(-1, 60).mean(axis=1)
    grid.append({"id": name, "split": "train" if name in meta["train_apps"] else "test",
                 "shape": r(hourly / hourly.max(), 3)})

# one app with a clear daily cycle, 14 days of 10-minute means (requests per minute, unscaled)
HERO = "9aba8d35"
hero14 = r(apps[HERO].reshape(-1, 10).mean(axis=1))

# the held-out day the repo's demo plots (8c2b9304 day 10), minutes 896-917 around its largest burst
trace = dict(episodes("test_apps"))["8c2b9304 day 10"]
runs = {"threshold": rollout(AutoscaleEnv(trace), ThresholdPolicy()),
        "yesterday": rollout(AutoscaleEnv(trace), SeasonalPolicy())}
cap = AutoscaleEnv(trace).config.capacity_per_server
W0, W1 = 896, 918
burst = {"minutes": list(range(W0, W1)),
         "today": r(trace[1440 + W0:1440 + W1]), "yesterday": r(trace[W0:W1])}
for k, rows in runs.items():
    burst[f"running_{k}"] = [rows[m]["running"] for m in range(W0, W1)]
    burst[f"booting_{k}"] = [rows[m]["booting"] for m in range(W0, W1)]
    burst[f"late_{k}"] = r([rows[m]["late"] for m in range(W0, W1)])
    burst[f"cap_{k}"] = [rows[m]["running"] * cap for m in range(W0, W1)]

# minutes left for each booting server after every step of the threshold run (rollout() does not keep them)
env, pol = AutoscaleEnv(trace), ThresholdPolicy()
pol.reset(); env.reset()
boot_left = []
for _ in range(W1):
    env.step(pol.act(env))
    boot_left.append(list(env.booting))
burst["boot_left_threshold"] = boot_left[W0:W1]
assert [len(b) for b in burst["boot_left_threshold"]] == burst["booting_threshold"]

# bursts on the training days of the 14 training apps (the repo's own find_bursts)
events = np.concatenate([find_bursts(x)[0] for x in train_series()])
to_peak = np.bincount(events[:, 3].astype(int))
peak_dist = r([to_peak[0], to_peak[1], to_peak[2], to_peak[3], to_peak[4:].sum()] / to_peak.sum(), 3)

# burst starts of the hero app on its 10 training days, and the share that repeat on another day
ev, base, hot = find_bursts(apps[HERO][:TRAIN_MINUTES])
starts = ev[:, 0].astype(int)
minute, day = starts % 1440, starts // 1440
repeat = float(np.mean([np.any((day != d) & (np.abs(minute - mi) <= REPEAT_WINDOW)) for mi, d in zip(minute, day)]))
rng = np.random.default_rng(0)
random_minutes = rng.integers(0, 1440, len(starts))  # constructed comparison: same days, random times

# noise: one hour of an app whose calm-minute noise is about 15%, with its trailing median
NOISY = "38ee9fad"
nx = apps[NOISY][:TRAIN_MINUTES]
_, nbase, nhot = find_bursts(nx)
H0 = 2 * 1440 + 14 * 60  # day 3, 14:00
noise_hour = {"app": NOISY, "noise": round(measure(nx)["noise"], 3),
              "load": r(nx[H0:H0 + 60]), "median": r(nbase[H0:H0 + 60])}

# three real one-minute bursts (peak in the first minute), 10 minutes either side, normalized to the baseline
examples = []
for name in ("e7a26f46", "e8cb71e1", "ec941895"):
    x = apps[name][:TRAIN_MINUTES]
    e, b, _ = find_bursts(x)
    first = e[(e[:, 3] == 0) & (e[:, 2] == 1) & (e[:, 0] > 1440) & (e[:, 1] > 1.7) & (e[:, 1] < 2.6)]
    t = int(first[0, 0])
    examples.append({"app": name, "t": t, "rel": r(x[t - 10:t + 11] / b[t], 3), "height": round(float(first[0, 1]), 2)})

# made-up vs real vs fitted, one day each, divided by the day's mean
real_day = apps[HERO][3 * 1440:4 * 1440]
slow = np.convolve(np.concatenate([real_day[-30:], real_day, real_day[:30]]), np.ones(60) / 60, "valid")[:1440]
made = slow * (1 + 0.05 * np.random.default_rng(1).standard_normal(1440))  # constructed: 5% noise
t0 = 13 * 60
made[t0:t0 + 10] += slow[t0] * 0.9 * np.arange(1, 11) / 10  # constructed: a burst that ramps up over 10 minutes
made[t0 + 10:t0 + 20] += slow[t0] * 0.9
fitted = FittedTraffic(train_series())(np.random.default_rng(3))[1440:]
compare = {k: r(v / v.mean(), 3) for k, v in (("made_up", made), ("real", real_day), ("fitted", fitted))}

stdout = (HERE / "demo_stdout.txt").read_text()
nums = lambda label: [float(v) for v in re.search(re.escape(label) + r"\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+(\d+)%", stdout).groups()]
held = stdout.split("real, unseen apps (5 held-out apps): 65 days")[1]
row = lambda label: [float(v) for v in re.search(re.escape(label) + r"\s+([\d.]+)\s+([\d.]+)", held).groups()]
results = {"fixed": row("fixed (sized for the day's peak)"), "threshold": row("threshold (Kubernetes HPA)"),
           "linear": row("linear forecast"), "yesterday": row("same time yesterday"),
           "threshold50": [float(v) for v in re.search(r"cost against late requests, real, unseen apps.*?threshold\s+target 50%\s+(\d+) server-min/day\s+([\d.]+)% late", stdout, re.S).groups()]}

evidence = {
    "source": "lakshdhamija/rl-autoscaler @ 8b126bd; Azure Functions Trace 2019 (Shahrad et al., USENIX ATC 2020), CC-BY 4.0",
    "grid": grid, "hero": HERO, "hero14_10min": hero14,
    "burst": burst, "peak_dist": peak_dist, "n_bursts": int(len(events)),
    "raster": {"app": HERO, "day": day.tolist(), "minute": minute.tolist(),
               "random_minute": random_minutes.tolist(), "repeat_share": round(repeat, 3)},
    "noise_hour": noise_hour, "burst_examples": examples, "compare": compare,
    "realism": {"real": nums("real (training days)"), "fitted": nums("fitted synthetic")},
    "results": results,
}
(HERE / "evidence.json").write_text(json.dumps(evidence, separators=(",", ":")))

scenes = HERE.parent / "scenes.py"
if scenes.exists():
    src = scenes.read_text()
    block = "# >>> EVIDENCE (generated by evidence/make_evidence.py; do not edit)\nEVIDENCE = json.loads(r'''" + \
            json.dumps(evidence, separators=(",", ":")) + "''')\n# <<< EVIDENCE"
    src = re.sub(r"# >>> EVIDENCE.*?# <<< EVIDENCE", lambda _: block, src, flags=re.S)
    scenes.write_text(src)
print("repeat share", round(repeat, 3), "bursts", len(starts), "peak dist", peak_dist,
      "noise", noise_hour["noise"], "examples", [(e["app"], e["t"], e["height"]) for e in examples], "results", results)
