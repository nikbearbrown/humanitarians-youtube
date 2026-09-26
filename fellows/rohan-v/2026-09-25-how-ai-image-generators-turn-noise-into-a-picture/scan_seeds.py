#!/usr/bin/env python3
"""Scan seeds 1-40 under both prompts with the trained toy model, and score every
result — so the seed shown in B05 is chosen by a logged, reproducible rule, not
by eye.

    python scan_seeds.py

Score = mean absolute pixel difference (0-255) between the generated picture and
its NEAREST picture of the requested prompt in the real training set. Lower means
a cleaner example of that prompt. Also records which class the nearest training
picture overall belongs to (a crude "does it look like what was asked" check).

Writes evidence/seed_scan.json and evidence/seed_scan.log. Every result is kept.
"""
import importlib.util, json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
EV = os.path.join(HERE, "evidence")
spec = importlib.util.spec_from_file_location("toy", os.path.join(HERE, "train_toy_diffusion.py"))
toy = importlib.util.module_from_spec(spec)
sys.argv = [sys.argv[0]]
# train_toy_diffusion.py opens evidence/run.log for writing at import time; keep
# the training run's log intact across this import (the script itself is left
# byte-identical, because its SHA-256 is recorded in toy_diffusion.json).
_runlog = os.path.join(os.path.dirname(os.path.abspath(__file__)), "evidence", "run.log")
_saved = open(_runlog, "rb").read() if os.path.isfile(_runlog) else None
spec.loader.exec_module(toy)
if _saved is not None:
    toy.LOG.close()
    open(_runlog, "wb").write(_saved)
LOG = open(os.path.join(EV, "seed_scan.log"), "w", encoding="utf-8")

W = dict(np.load(os.path.join(EV, "weights.npz")))
rng = np.random.default_rng(0)
X = np.stack([toy.draw(p, rng) for p in (0, 1) for _ in range(6000)])
Y = np.repeat([0, 1], 6000)
Xu = (X + 1) * 127.5


def score(img_u8, prompt):
    d = np.abs(Xu - np.asarray(img_u8, np.float32)[None]).mean(1)
    own = float(d[Y == prompt].min())
    nearest_class = int(Y[int(d.argmin())])
    return round(own, 2), nearest_class


rows = []
for seed in range(1, 41):
    row = {"seed": seed}
    for p, name in enumerate(toy.PROMPTS):
        final = toy.to_u8(toy.sample(W, p, seed, keep=(0,))[1][0])
        s, nc = score(final, p)
        row[name] = {"score": s, "nearest_is_asked": nc == p}
    row["worst"] = max(row["heart"]["score"], row["music note"]["score"])
    rows.append(row)
    line = (f"seed {seed:2d}  heart {row['heart']['score']:6.2f}{'' if row['heart']['nearest_is_asked'] else ' (x)'}"
            f"  note {row['music note']['score']:6.2f}{'' if row['music note']['nearest_is_asked'] else ' (x)'}")
    print(line); LOG.write(line + "\n"); LOG.flush()

ok = [r for r in rows if r["heart"]["nearest_is_asked"] and r["music note"]["nearest_is_asked"]]
best = min(ok or rows, key=lambda r: r["worst"])
notes = sorted(r["music note"]["score"] for r in rows)
summary = {
    "rule": "among seeds 1-40 whose results are nearest to the asked class under BOTH prompts, "
            "the seed with the best worse-of-two score",
    "chosen_seed": best["seed"], "chosen": best,
    "both_prompts_recognisable": len(ok), "of": len(rows),
    "note_score_median": float(np.median(notes)), "rows": rows,
}
json.dump(summary, open(os.path.join(EV, "seed_scan.json"), "w", encoding="utf-8"), indent=1)
msg = (f"\nboth prompts land in the asked class for {len(ok)}/{len(rows)} seeds; "
       f"chosen seed {best['seed']} (heart {best['heart']['score']}, note {best['music note']['score']}); "
       f"median note score {np.median(notes):.2f}")
print(msg); LOG.write(msg + "\n")
