#!/usr/bin/env python3
"""Export the toy-diffusion evidence into the Remotion data module the scenes read.

    python export_toy_data.py

Reads   evidence/weights.npz + evidence/toy_diffusion.json (from train_toy_diffusion.py)
Writes  <toolkit>/runtime/remotion/src/scenes/diffusion/toyData.ts   (generated — do not hand-edit)
        evidence/export.log

Nothing is re-trained. The sampling runs are REPLAYED from the saved weights with
the same seeds, recording a snapshot every 20 steps instead of 11 keyframes so
the reverse process animates smoothly; the replay is checked against the final
pictures recorded at training time and the export refuses to write if any
differs. The B03 equations are typeset with the toolkit's own
runtime/scripts/typeset_math.py (MathText -> outlined SVG), and each term's
horizontal span is measured with matplotlib's MathText parser so the scene can
point at the exact glyphs a label describes.
"""
import hashlib, importlib.util, json, math, os, sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
EV = os.path.join(HERE, "evidence")
TOOLKIT = os.environ.get("ART_HOME", "D:/Rohan/Claude/HAI/RohanClaudeHAIbrutalist.art")
OUT_TS = os.path.join(TOOLKIT, "runtime/remotion/src/scenes/diffusion/toyData.ts")
LOG = open(os.path.join(EV, "export.log"), "w", encoding="utf-8")


def log(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


spec = importlib.util.spec_from_file_location("toy", os.path.join(HERE, "train_toy_diffusion.py"))
toy = importlib.util.module_from_spec(spec)
sys.argv = [sys.argv[0]]
# train_toy_diffusion.py opens evidence/run.log for writing at import time; keep
# the training run's log intact across this import (the script itself is left
# byte-identical, because its SHA-256 is recorded in toy_diffusion.json).
_runlog = os.path.join(os.path.dirname(os.path.abspath(__file__)), "evidence", "run.log")
_saved = open(_runlog, "rb").read() if os.path.isfile(_runlog) else None
spec.loader.exec_module(toy)            # defines functions only; main() is guarded
if _saved is not None:
    toy.LOG.close()
    open(_runlog, "wb").write(_saved)
sys.path.insert(0, os.path.join(TOOLKIT, "runtime/scripts"))
# matplotlib (the house math renderer's one dependency) lives in <toolkit>/.pydeps,
# installed with `pip install --target` so nothing lands on C:. APPENDED, so the
# system numpy/Pillow the model was trained with always win.
sys.path.append(os.path.join(TOOLKIT, ".pydeps"))
from typeset_math import typeset        # noqa: E402  the house renderer

W = dict(np.load(os.path.join(EV, "weights.npz")))
REC = json.load(open(os.path.join(EV, "toy_diffusion.json"), encoding="utf-8"))
KEEP = tuple(range(0, 1001, 20))


def hexpx(a):
    return "".join(f"{v:02x}" for v in toy.to_u8(np.clip(np.asarray(a), -1, 1)))


runs = []
for rec in REC["runs"]:
    prompt = toy.PROMPTS.index(rec["prompt"])
    start, frames, guesses = toy.sample(W, prompt, rec["seed"], keep=KEEP)
    final = toy.to_u8(frames[0])
    if final != rec["final"]:
        raise SystemExit(f"replay mismatch: {rec['prompt']} seed {rec['seed']} — refusing to export")
    runs.append({
        "prompt": rec["prompt"], "seed": rec["seed"],
        "frames": [hexpx(frames[t]) for t in sorted(frames, reverse=True)],   # t = 1000 … 0
        "guesses": [hexpx(guesses.get(t, frames[t])) for t in sorted(frames, reverse=True)],
    })
    log(f"replayed {rec['prompt']:>10} seed {rec['seed']:>3}: {len(frames)} snapshots, final matches")

# a sample of the REAL training set, rebuilt with the same seeded draws train() used
trng = np.random.default_rng(0)
TX = np.stack([toy.draw(p, trng) for p in (0, 1) for _ in range(6000)])
train_samples = [hexpx(TX[i]) for i in list(range(0, 8)) + list(range(6000, 6008))]
if hexpx(TX[3]) != "".join(f"{v:02x}" for v in REC["forward"][0]["px"]):
    raise SystemExit("training-set rebuild does not match the recorded forward picture — refusing to export")
log(f"rebuilt training set: {len(TX)} pictures; sample of 8 hearts + 8 notes exported; matches the record")

# B05's fork: the seed chosen by scan_seeds.py's logged rule (not by eye). These two
# runs were not part of the training-time record, so they are sampled fresh here —
# deterministic from the seed — and their finals are logged with their scan scores.
SCAN = json.load(open(os.path.join(EV, "seed_scan.json"), encoding="utf-8"))
FORK = SCAN["chosen_seed"]
have = {(r["prompt"], r["seed"]) for r in runs}
for name in toy.PROMPTS:
    if (name, FORK) in have:
        continue
    start, frames, guesses = toy.sample(W, toy.PROMPTS.index(name), FORK, keep=KEEP)
    runs.append({
        "prompt": name, "seed": FORK,
        "frames": [hexpx(frames[t]) for t in sorted(frames, reverse=True)],
        "guesses": [hexpx(guesses.get(t, frames[t])) for t in sorted(frames, reverse=True)],
    })
    log(f"fork run {name:>10} seed {FORK}: scan score {SCAN['chosen'][name]['score']}")

# the forward process: the clean picture and the fixed noise it is mixed with
x0 = np.asarray(REC["forward"][0]["px"], np.float32) / 127.5 - 1
rng = np.random.default_rng(11)                       # the same draw train_toy_diffusion.py used
eps = rng.standard_normal(toy.D).astype(np.float32)
eps_q = [round(float(v), 3) for v in eps]

# ── the typeset equations (house renderer) + per-term spans ─────────────────
from matplotlib.mathtext import MathTextParser     # noqa: E402
from matplotlib.font_manager import FontProperties  # noqa: E402
import matplotlib                                   # noqa: E402

parser = MathTextParser("path")


def width(expr):
    with matplotlib.rc_context({"mathtext.fontset": "stix"}):
        return parser.parse("$" + expr + "$", prop=FontProperties(size=48)).width


EQ_TERMS = [r"x_t", r"\sqrt{\bar{\alpha}_t}\,x_0", r"\sqrt{1-\bar{\alpha}_t}\,\epsilon"]
EQ = r"x_t = \sqrt{\bar{\alpha}_t}\,x_0 + \sqrt{1-\bar{\alpha}_t}\,\epsilon"
prefixes = [r"x_t", r"x_t = \sqrt{\bar{\alpha}_t}\,x_0", EQ]
full_w = width(EQ)
spans = []
for pre, term in zip(prefixes, EQ_TERMS):
    end = width(pre)
    spans.append([round((end - width(term)) / full_w, 4), round(end / full_w, 4)])
log("equation term spans (fraction of width):", spans)

share_end = math.sqrt(float(toy.ABAR[-1]))
rows = {
    "mix": typeset(EQ),
    "end": typeset(r"\sqrt{\bar{\alpha}_{1000}} \approx " + f"{share_end:.4f}"),
    "loss": typeset(r"\mathcal{L} = \left\| \epsilon - \epsilon_\theta(x_t,\ t) \right\|^2"),
}
log(f"picture share at step 1000: {share_end:.6f}  (under one percent: {share_end < 0.01})")

data = {
    "side": toy.S, "T": toy.T, "beta": [1e-4, 0.02], "guidance": REC["guidance"],
    "params": REC["params"], "trainPictures": REC["train_pictures"],
    "trainSteps": REC["train_steps"], "trainSeconds": REC["train_seconds"],
    "rerunIdentical": REC["rerun_identical"], "gridMeanPixelDiff": REC["grid_mean_pixel_diff"],
    "nearestTrainingDiff": REC["nearest_training_diff"],
    "lossCurve": REC["loss_curve"],
    "keepEvery": 20, "runs": runs, "trainSamples": train_samples, "forkSeed": FORK,
    "seedScan": {"rule": SCAN["rule"], "recognisable": SCAN["both_prompts_recognisable"], "of": SCAN["of"]},
    "x0": hexpx(x0), "eps": eps_q,
    "shareEnd": round(share_end, 6),
    "eq": {"mix": rows["mix"], "end": rows["end"], "loss": rows["loss"], "spans": spans},
    "evidenceSha256": hashlib.sha256(open(os.path.join(EV, "toy_diffusion.json"), "rb").read()).hexdigest(),
}
os.makedirs(os.path.dirname(OUT_TS), exist_ok=True)
with open(OUT_TS, "w", encoding="utf-8", newline="\n") as f:
    f.write("/* GENERATED by export_toy_data.py in the reel folder\n"
            " * (books/humanitarians-ai/youtube/week-05/2026-09-25-how-ai-image-generators-turn-noise-into-a-picture).\n"
            " * Every picture and number here comes from a real run of train_toy_diffusion.py — a toy DDPM\n"
            " * trained from scratch in numpy. Do not hand-edit; re-run the exporter. */\n")
    f.write("export const TOY = " + json.dumps(data, separators=(",", ":")) + ";\n")
log(f"wrote {OUT_TS}  ({os.path.getsize(OUT_TS)/1024:.0f} KB)")
