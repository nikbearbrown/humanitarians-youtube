"""Compute every number and curve the video shows, from lakshdhamija/rl-autoscaler.

Run inside the rl-autoscaler venv, from the repo:
  cd rl-autoscaler && PYTHONPATH=scripts:src .venv/bin/python <reel>/evidence/make_evidence.py
Records the repo commit (and refuses to run on uncommitted changes). Reads results/stress-hpa.json, results/ppo-hpa/*.json, data/*.json and the processed traces; writes nothing
inside the repo. Writes evidence.json next to this file and embeds it into ../scenes.py between the EVIDENCE
markers. Every number the video speaks or shows is asserted against EXPECT below: if one differs, the script
stops with the difference instead of writing anything.
"""

import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

from frontier import rule_late_at
from rl_autoscaler.data import HUAWEI, episodes, load, train_series
from rl_autoscaler.env import AutoscaleEnv, ClusterConfig
from rl_autoscaler.policies import ThresholdPolicy, rollout
from rl_autoscaler.traffic import find_bursts
from rl_autoscaler.train import HEADROOM_TARGETS, WEEKLY

HERE = Path(__file__).resolve().parent
REPO = Path.home() / "code" / "rl-autoscaler"
PANELS = ("huawei/test_apps", "huawei/test_days", "azure/test_days", "azure/test_apps")
VARIANTS = {"normal": "hpa-3M_", "misleading": "hpa-baddays-3M_"}  # trained on normal / with misleading history

# The numbers the brief and the README state. Score: (runs better of 15, rounded % change in late requests
# against HPA at equal cost: most negative, largest).
EXPECT = {
    "score": {"huawei/test_apps": {"normal": (15, -57, -15), "misleading": (15, -60, -5)},
              "huawei/test_days": {"normal": (15, -36, -15), "misleading": (15, -40, -8)},
              "azure/test_days": {"normal": (15, -29, -7), "misleading": (15, -29, -2)},
              "azure/test_apps": {"normal": (8, -29, 33), "misleading": (10, -32, 45)}},
    # (cases better, cases, % better, worst % more late than HPA, runs better on normal history of 60)
    "stress": {"normal": (208, 360, 58, 93, 53), "misleading": (273, 360, 76, 64, 55)},
    "sizes": {"azure": (19, 14, 14, 5), "huawei-public": (8, 26, 6, 2), "huawei-private": (26, 33, 18, 8)},
    "train_days": {"azure": 42, "huawei": 414, "total": 456},
    "runs": 30, "steps": 3_000_000, "penalties": [0.01, 0.03, 0.1, 0.3, 1.0], "seeds": [0, 1, 2], "bad_days": 0.3,
    "targets": [0.4, 0.5, 0.6, 0.7, 0.8, 0.9], "capacity": 600, "boot": 3, "test_share": 0.3,
    "burst_first_minute_azure_pct": 72,
    "burstiness_heldout": [0.033, 0.140, 0.196, 0.248, 0.267], "burstiness_median": {"azure": 0.065, "huawei": 0.048},
}


def rel(run, curve):
    """% change in late requests against HPA at this run's own cost (frontier.rule_late_at, linear between targets)."""
    ref = rule_late_at(run["cost_per_day"], [curve])
    return None if ref is None else 100 * (run["late_pct"] / ref - 1)


def check(name, got, want):
    if got != want:
        sys.exit(f"STOP: {name}: computed {got!r}, the brief says {want!r}")


def apps_of(split, data):
    g = defaultdict(list)
    for name, tr in episodes(split, data, 7):
        g[name.split(" day ")[0]].append(tr)
    return g


def burstiness(traces):
    """Mean absolute minute-to-minute change over mean load, on the served day of each episode."""
    x = np.concatenate([t[7 * 1440:] for t in traces])
    return float(np.abs(np.diff(x)).mean() / x.mean())


if __name__ == "__main__":
    git = lambda *a: subprocess.run(["git", "-C", str(REPO), *a], capture_output=True, text=True, check=True).stdout.strip()
    commit, subject = git("rev-parse", "--short", "HEAD"), git("log", "-1", "--format=%s")
    dirty = git("status", "--porcelain", "--", "results", "data", "scripts", "src", "tests")
    assert not dirty, f"uncommitted changes in the repo, the evidence would not match {commit}:\n{dirty}"
    stress = json.loads((REPO / "results" / "stress-hpa.json").read_text())
    normal = {r["panel"]: r for r in stress if r["scenario"] == "normal"}
    runs = {p.stem: json.loads(p.read_text()) for p in sorted((REPO / "results" / "ppo-hpa").glob("*.json"))}
    check("runs", len(runs), EXPECT["runs"])
    check("steps", sorted({r["steps"] for r in runs.values()}), [EXPECT["steps"]])
    check("penalties", sorted({r["penalty"] for r in runs.values()}), EXPECT["penalties"])
    check("seeds", sorted({r["seed"] for r in runs.values()}), EXPECT["seeds"])
    check("misleading share", sorted({r["bad_days"] for r in runs.values()}), [0.0, EXPECT["bad_days"]])
    check("kind", sorted({r["kind"] for r in runs.values()}), ["hpa"])
    for stem, r in runs.items():  # the result files and stress.py's "normal" scenario are the same runs
        for p in PANELS:
            a, b = r[p], normal[p]["ppo"][stem]
            assert abs(a["cost_per_day"] - b["cost_per_day"]) < 1e-6 and abs(a["late_pct"] - b["late_pct"]) < 1e-9, (stem, p)

    def variant(stem):
        return "misleading" if stem.startswith(VARIANTS["misleading"]) else "normal"

    # chart: the HPA curve per test set (targets 40-90%) and every PPO run as a point
    curves = {p: [[round(h["cost_per_day"]), round(h["late_pct"], 3)] for h in normal[p]["hpa"]] for p in PANELS}
    points = {p: {v: [[round(r[p]["cost_per_day"]), round(r[p]["late_pct"], 3), r["penalty"]]
                      for s, r in runs.items() if variant(s) == v] for v in VARIANTS} for p in PANELS}

    # score card: each run against HPA at its own cost
    score, by_penalty = {}, {}
    for p in PANELS:
        score[p] = {}
        for v in VARIANTS:
            vs = [rel(r[p], normal[p]["hpa"]) for s, r in runs.items() if variant(s) == v]
            assert None not in vs, (p, v)
            score[p][v] = {"better": sum(x < 0 for x in vs), "runs": len(vs), "lo": round(min(vs)), "hi": round(max(vs))}
            check(f"score {p} {v}", (score[p][v]["better"], score[p][v]["lo"], score[p][v]["hi"]), EXPECT["score"][p][v])
    p = "azure/test_apps"  # lean (lowest late penalty) against spare-keeping (highest late penalty) runs
    for pen in (min(EXPECT["penalties"]), max(EXPECT["penalties"])):
        sel = [r for r in runs.values() if r["penalty"] == pen]
        by_penalty[str(pen)] = {"better": sum(rel(r[p], normal[p]["hpa"]) < 0 for r in sel), "runs": len(sel),
                                "mean_cost": round(float(np.mean([r[p]["cost_per_day"] for r in sel])))}
    check("lean runs on Azure held-out apps, runs better", by_penalty["0.01"]["better"], 0)
    check("spare-keeping runs on Azure held-out apps, runs better", by_penalty["1.0"]["better"], by_penalty["1.0"]["runs"])
    assert by_penalty["1.0"]["mean_cost"] > by_penalty["0.01"]["mean_cost"]

    # misleading history: the six changed scenarios, every run against HPA under the same change
    stressed = {}
    for v, prefix in VARIANTS.items():
        vs = [rel(x, r["hpa"]) for r in stress if r["scenario"] != "normal" for s, x in r["ppo"].items() if s.startswith(prefix)]
        assert None not in vs, v
        better = sum(x < 0 for x in vs)
        stressed[v] = {"better": better, "cases": len(vs), "pct": round(100 * better / len(vs)), "worst": round(max(vs)),
                       "normal_better": sum(score[q][v]["better"] for q in PANELS),
                       "normal_runs": sum(score[q][v]["runs"] for q in PANELS)}
        s = stressed[v]
        check(f"stress {v}", (s["better"], s["cases"], s["pct"], s["worst"], s["normal_better"]), EXPECT["stress"][v])
    scenarios = sorted({r["scenario"] for r in stress} - {"normal"})
    check("changed scenarios", len(scenarios), 6)

    # data and training
    sizes = {}
    for d in ("azure",) + HUAWEI:
        apps, m = load(d)
        sizes[d] = {"apps": len(apps), "days": m["test_days"][1], "train_apps": len(m["train_apps"]),
                    "test_apps": len(m["test_apps"]), "unseen_days": m["test_days"][1] - m["test_days"][0] + 1}
        check(f"sizes {d}", (sizes[d]["apps"], sizes[d]["days"], sizes[d]["train_apps"], sizes[d]["test_apps"]), EXPECT["sizes"][d])
    prep = (REPO / "scripts" / "prepare_huawei.py").read_text()
    test_share = float(re.search(r"^TEST_SHARE = ([\d.]+)", prep, re.M).group(1))
    check("Huawei held-out share (prepare_huawei.TEST_SHARE)", test_share, EXPECT["test_share"])
    check("Huawei unseen days", (sizes["huawei-public"]["unseen_days"], sizes["huawei-private"]["unseen_days"]), (7, 7))
    hw_held = {"functions": sum(sizes[d]["test_apps"] for d in HUAWEI), "of": sum(sizes[d]["apps"] for d in HUAWEI), "share": test_share}
    train_days = {"azure": len(episodes("train", "azure", 7)), "huawei": len(episodes("train", HUAWEI, 7))}
    train_days["total"] = train_days["azure"] + train_days["huawei"]
    check("train days", train_days, EXPECT["train_days"])
    c = ClusterConfig()
    check("targets", list(HEADROOM_TARGETS), EXPECT["targets"])
    check("capacity, boot, windows", (c.capacity_per_server, c.boot_delay, c.window, WEEKLY.yesterday_window,
                                      WEEKLY.lastweek_window), (EXPECT["capacity"], EXPECT["boot"], 10, 10, 10))

    # bursts: share that peak in their first minute, Azure training days (README "Data")
    ev = np.concatenate([find_bursts(x)[0] for x in train_series("azure")])
    first_minute = round(100 * float(np.mean(ev[:, 3] == 0)))
    check("bursts peaking in their first minute (Azure training days)", first_minute, EXPECT["burst_first_minute_azure_pct"])

    # burstiness of the Azure held-out apps against the training apps
    held = {a: burstiness(t) for a, t in apps_of("test_apps", "azure").items()}
    tr_az = [burstiness(t) for t in apps_of("train", "azure").values()]
    tr_hw = [burstiness(t) for t in apps_of("train", HUAWEI).values()]
    med = {"azure": float(np.median(tr_az)), "huawei": float(np.median(tr_hw)), "all": float(np.median(tr_az + tr_hw))}
    check("held-out burstiness", sorted(round(v, 3) for v in held.values()), EXPECT["burstiness_heldout"])
    check("training medians", {k: round(med[k], 3) for k in ("azure", "huawei")}, EXPECT["burstiness_median"])
    ratios = {k: sorted(round(v / med[k], 2) for v in held.values()) for k in ("azure", "all")}
    for k in ratios:  # "4 of the 5 are 2 to 4 times burstier than the typical training app", either median
        check(f"held-out apps 2 to 4 times burstier ({k} median)", [round(r) for r in ratios[k] if round(r) >= 2], [2, 3, 4, 4])

    # one held-out Huawei function, 18:50-19:20, under HPA at 70%: a burst at 19:00 that repeats each day
    tr = dict(episodes("test_apps", "huawei-private", 7))["pri-60 day 12"]
    rows = rollout(AutoscaleEnv(tr, WEEKLY), ThresholdPolicy(target=0.7))
    w0, w1, day = 1130, 1161, 7 * 1440  # rows[i] is minute i of the served day
    window = {"function": "pri-60", "day": 12, "start_minute": w0, "target": 0.7,
              "load": [round(r["load"]) for r in rows[w0:w1]],
              "capacity": [int(r["running"] * c.capacity_per_server) for r in rows[w0:w1]],
              "late": [round(r["late"]) for r in rows[w0:w1]],
              "yesterday": [round(float(x)) for x in tr[day - 1440 + w0:day - 1440 + w1]],
              "last_week": [round(float(x)) for x in tr[w0:w1]]}
    assert all(abs(a - b) <= 1 for a, b in zip(window["load"], tr[day + w0:day + w1]))
    jump = window["load"][10] / window["load"][9]
    first_ready = next(i for i in range(10, 31) if window["capacity"][i] > window["capacity"][9])
    assert jump > 1.6 and window["late"][9] == 0 and window["late"][10] > 0, (jump, window["late"][9:11])
    assert window["yesterday"][10] / window["yesterday"][9] > 1.6 and window["last_week"][10] / window["last_week"][9] > 1.6
    check("first new server serves after the jump (minutes)", first_ready - 10, EXPECT["boot"])
    window["jump"] = round(jump, 2)
    window["late_minutes"] = sum(x > 0 for x in window["late"])

    pytest = (HERE / "pytest_stdout.txt").read_text()
    m = re.search(r"(\d+) passed", pytest)
    check("pytest", (int(m.group(1)) if m else None, " failed" in pytest), (21, False))

    evidence = {
        "source": f"lakshdhamija/rl-autoscaler @ {commit}; Azure Functions Trace 2019 (CC-BY 4.0); Huawei Cloud traces 2023 (CC BY 4.0)",
        "panels": list(PANELS), "targets": EXPECT["targets"], "curves": curves, "points": points, "score": score,
        "azure_apps_by_penalty": by_penalty, "stress": stressed, "stress_scenarios": scenarios,
        "sizes": sizes, "huawei_held_out": hw_held, "train_days": train_days,
        "training": {"runs": len(runs), "variants": len(VARIANTS), "penalties": EXPECT["penalties"], "seeds": len(EXPECT["seeds"]),
                     "steps": EXPECT["steps"], "misleading_share": EXPECT["bad_days"]},
        "cluster": {"capacity": c.capacity_per_server, "boot": c.boot_delay, "window": c.window},
        "burst_first_minute_pct": {"azure": first_minute},
        "burstiness": {"held_out": [round(v, 3) for v in sorted(held.values())],
                       "median": {k: round(v, 3) for k, v in med.items()}, "ratios": ratios},
        "window": window, "pytest": f"{m.group(1)} passed", "commit": commit, "commit_subject": subject,
    }
    (HERE / "evidence.json").write_text(json.dumps(evidence, indent=1))
    scenes = HERE.parent / "scenes.py"
    if scenes.exists():
        block = "# >>> EVIDENCE (generated by evidence/make_evidence.py; do not edit)\nEVIDENCE = json.loads(r'''" + \
                json.dumps(evidence, separators=(",", ":")) + "''')\n# <<< EVIDENCE"
        text = scenes.read_text()
        if "# >>> EVIDENCE" in text:
            scenes.write_text(re.sub(r"# >>> EVIDENCE.*?# <<< EVIDENCE", lambda _: block, text, flags=re.S))
    print(json.dumps({k: evidence[k] for k in ("score", "stress", "train_days", "huawei_held_out", "burstiness",
                                                "azure_apps_by_penalty", "burst_first_minute_pct")}, indent=1))
    print(f"window: jump {window['jump']}x at 19:00, {window['late_minutes']} late minutes; every expected number matches")
