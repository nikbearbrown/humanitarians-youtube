"""Compute every number the video shows, from lakshdhamija/rl-autoscaler.

Run from the rl-autoscaler checkout, in its venv:
  cd rl-autoscaler && PYTHONPATH=scripts:src .venv/bin/python <reel>/evidence/make_evidence.py
Reads results/stress-hpa.json and results/ppo-hpa/*.json (no training, no re-run of the stress test), checks
every number against the values the script was written for, writes evidence.json next to this file and embeds
it into ../scenes.py and ../vertical/scenes.py between the EVIDENCE markers. Any mismatch stops with an error.
"""

import json
import re
import subprocess
from pathlib import Path

import numpy as np

from frontier import WEEKLY_PANELS, rule_late_at
from stress import SCENARIOS, Change
from rl_autoscaler.data import episodes
from rl_autoscaler.env import AutoscaleEnv
from rl_autoscaler.train import ALL_DATA, HEADROOM_TARGETS, WEEKLY, real_traffic

HERE = Path(__file__).resolve().parent
REPO = Path.home() / "code" / "rl-autoscaler"
CHANGES = [s for s in SCENARIOS if s != "normal"]
GROUPS = {0.0: "normal", 0.3: "misleading"}   # bad_days share in each model's json -> agent

# The numbers the narration was written for (per change: summed over the 4 test sets, out of 60).
EXPECTED = {"normal": {"yesterday quiet": 37, "yesterday spike": 37, "yesterday missing": 32, "last week quiet": 32,
                       "last week spike": 48, "last week missing": 22, "total": 208, "normal": 53, "worst_pct": 93},
            "misleading": {"yesterday quiet": 48, "yesterday spike": 51, "yesterday missing": 42, "last week quiet": 43,
                           "last week spike": 48, "last week missing": 41, "total": 273, "normal": 55, "worst_pct": 64}}


def stress_counts():
    rows = json.loads((REPO / "results/stress-hpa.json").read_text())
    meta = {p.stem: json.loads(p.read_text()) for p in (REPO / "results/ppo-hpa").glob("*.json")}
    agent = {m: GROUPS[r.get("bad_days", 0.0)] for m, r in meta.items()}
    order = sorted(meta, key=lambda m: (meta[m]["penalty"], meta[m]["seed"]))   # 15 runs per agent
    by = {(r["scenario"], r["panel"]): r for r in rows}
    out = {g: {"cases": 0, "better": 0, "worst_pct": None, "grid": {}, "per_change": {}} for g in GROUPS.values()}
    for g in out.values():
        g["normal"] = 0
    for s in SCENARIOS:
        for g in out:
            bits = ""
            for p in WEEKLY_PANELS:   # panel-major: 4 test sets x 15 runs
                row = by[(s, p)]
                for m in order:
                    if agent[m] != g:
                        continue
                    r = row["ppo"][m]
                    ref = rule_late_at(r["cost_per_day"], [row["hpa"]])
                    assert ref is not None, f"{s} {p} {m}: PPO cost outside HPA's cost range"
                    pct = 100 * (r["late_pct"] / ref - 1)
                    if s != "normal" and pct > (out[g]["worst_pct"] or -1e9):
                        out[g]["worst_pct"], out[g]["worst_case"] = pct, {"change": s, "index": len(bits), "test_set": p, "run": m}
                    bits += "1" if pct < 0 else "0"
            assert len(bits) == 60, (s, g, len(bits))
            if s == "normal":
                out[g]["normal"] = bits.count("1")
                out[g]["normal_grid"] = bits
            else:
                out[g]["grid"][s] = bits
                out[g]["per_change"][s] = bits.count("1")
                out[g]["cases"] += 60
                out[g]["better"] += bits.count("1")
    for g, o in out.items():
        o["runs"] = sum(1 for m in agent if agent[m] == g)
        o["pct"] = round(100 * o["better"] / o["cases"])
        o["worst_pct_exact"] = round(o["worst_pct"], 2)
        o["worst_pct"] = round(o["worst_pct"])
        got = {**o["per_change"], "total": o["better"], "normal": o["normal"], "worst_pct": o["worst_pct"]}
        diff = {k: (got[k], v) for k, v in EXPECTED[g].items() if got[k] != v}
        assert not diff, f"STOP: {g} agent differs from the expected numbers (computed, expected): {diff}"
        assert o["cases"] == 360 and o["runs"] == 15, (g, o["cases"], o["runs"])
    # HPA reads only the last minute of load: a changed last week never reaches it, a changed yesterday only through
    # the last minutes before midnight (the day starts with servers sized for yesterday's last minute; stress.py).
    for s in CHANGES:
        for p in WEEKLY_PANELS:
            same = all(a == b for a, b in zip(by[(s, p)]["hpa"], by[("normal", p)]["hpa"]))
            assert same == s.startswith("last week"), (s, p)
    return out


def observation():
    trace = episodes("test_days", "azure", 7)[0][1]
    size = AutoscaleEnv(trace, WEEKLY).observation_space.shape[0]
    groups = [WEEKLY.window, WEEKLY.yesterday_window, WEEKLY.lastweek_window, size - 30]
    assert size == 35 and groups == [10, 10, 10, 5], (size, groups)
    return {"size": size, "groups": groups, "boot_minutes": WEEKLY.boot_delay,
            "capacity_per_server": WEEKLY.capacity_per_server,
            "targets_pct": [round(100 * t) for t in HEADROOM_TARGETS]}


def example_day(name="ec941895 day 12", lo=200, hi=320):
    """A real Azure test day (an unseen day of a training app) whose bursts repeat yesterday's minute."""
    trace = dict(episodes("test_days", "azure", 7))[name]
    D = trace.reshape(8, 1440)
    out = {"name": name, "lo": lo, "hi": hi, "corr_day": round(float(np.corrcoef(D[7], D[6])[0, 1]), 2),
           "today": [int(round(v)) for v in D[7][lo:hi + 1]], "yesterday": [int(round(v)) for v in D[6][lo:hi + 1]],
           "last_week": [int(round(v)) for v in D[0][lo:hi + 1]]}
    burst = lo + int(np.argmax(out["today"]))
    assert burst == lo + int(np.argmax(out["yesterday"])) == 240, burst   # same minute both days
    out["burst_minute"] = burst
    for s in ("yesterday quiet", "yesterday spike", "yesterday missing"):   # stress.py's own change
        changed = Change(s)(trace).reshape(8, 1440)[6][lo:hi + 1]
        assert np.allclose(changed, D[6][lo:hi + 1] * SCENARIOS[s][1])
    return out


def training_draws(n=10, share=0.3):
    """Mirror of train.real_traffic's draw, checked against the real function; returns example draws."""
    draw = real_traffic(ALL_DATA, 7, share)
    real = [t for _, t in episodes("train", ALL_DATA, 7)]

    def mirror(rng):
        i = rng.integers(len(real))
        if rng.random() >= share:
            return i, None, None
        lag = rng.choice([1, 7])
        factor = 0.0 if rng.random() < 0.25 else float(np.exp(rng.uniform(np.log(0.1), np.log(5.0))))
        return i, ("yesterday" if lag == 1 else "last week"), factor

    changed, factors = 0, []
    rng_a, rng_b = np.random.default_rng(0), np.random.default_rng(0)
    for _ in range(3000):
        t = draw(rng_a)
        i, which, f = mirror(rng_b)
        if which is None:
            assert np.array_equal(t, real[i])
            continue
        day = 6 if which == "yesterday" else 0
        expect = real[i].copy()
        expect[day * 1440:(day + 1) * 1440] *= f
        assert np.array_equal(t, expect)
        changed += 1
        factors.append(f)
    nz = [f for f in factors if f > 0]
    assert abs(changed / 3000 - share) < 0.03 and min(nz) >= 0.1 and max(nz) <= 5.0 and 0.0 in factors
    # example cards: the first seed whose first n draws change exactly 30% of them, with both days and a zero
    for seed in range(100):
        rng = np.random.default_rng(seed)
        ex = [mirror(rng)[1:] for _ in range(n)]
        hit = [e for e in ex if e[0]]
        if len(hit) == round(share * n) and {e[0] for e in hit} == {"yesterday", "last week"}:
            break
    cards = [None if w is None else {"day": w, "factor": round(f, 2)} for w, f in ex]
    dots = [round(f, 3) for f in factors[:40]]   # the first 40 changed draws of seed 0, for the number line
    return {"share_pct": round(100 * share), "factor_lo": 0.1, "factor_hi": 5.0, "seed": seed, "cards": cards,
            "dots": dots, "checked_draws": 3000, "checked_share": round(changed / 3000, 3)}


if __name__ == "__main__":
    commit = subprocess.run(["git", "-C", str(REPO), "rev-parse", "--short", "HEAD"], capture_output=True,
                            text=True).stdout.strip()
    dirty = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain", "--untracked-files=no"],
                           capture_output=True, text=True).stdout.strip()
    assert commit and not dirty, f"rl-autoscaler must be a clean checkout (commit {commit!r}, changes {dirty!r})"
    evidence = {"source": f"https://github.com/lakshdhamija/rl-autoscaler @ {commit}; Azure Functions Trace 2019 "
                          "(CC-BY 4.0); Huawei Cloud traces 2023 (CC BY 4.0)",
                "test_sets": list(WEEKLY_PANELS.values()), "changes": CHANGES,
                "observation": observation(), "example": example_day(), "training": training_draws(),
                "stress": stress_counts()}
    (HERE / "evidence.json").write_text(json.dumps(evidence, indent=1))
    block = "# >>> EVIDENCE (generated by evidence/make_evidence.py; do not edit)\nEVIDENCE = json.loads(r'''" + \
            json.dumps(evidence, separators=(",", ":")) + "''')\n# <<< EVIDENCE"
    for scenes in (HERE.parent / "scenes.py", HERE.parent / "vertical" / "scenes.py"):
        if scenes.exists():
            scenes.write_text(re.sub(r"# >>> EVIDENCE.*?# <<< EVIDENCE", lambda _: block, scenes.read_text(), flags=re.S))
    s = evidence["stress"]
    for g in s:
        print(g, s[g]["per_change"], "total", s[g]["better"], "of", s[g]["cases"], f"({s[g]['pct']}%)",
              "worst", s[g]["worst_pct_exact"], "normal", s[g]["normal"], "of 60")
    print("example", evidence["example"]["name"], "corr", evidence["example"]["corr_day"],
          "training cards", evidence["training"]["cards"], "seed", evidence["training"]["seed"])
