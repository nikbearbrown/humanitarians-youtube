#!/usr/bin/env python3
"""drone_mix.py — rebuild loonet's drone-noise test clips, and score them the Python way.

loonet's notebook (looncall_v1.ipynb, cell 6, commit 76a6c41) mixes each of
the 65 looncall val windows with the drone's propeller noise at falling SNR
and asks: is the call still heard? This script repeats that mixing step for
step — same val.csv order, same noise file, same RNG (default_rng(0)), same
gain formula, same peak normalisation — and writes every clip as a 48 kHz
WAV, plus a manifest, so Gavia's own Rust code can score the identical audio
(see noise_check.rs).

It also scores the clips the Python way, with the formula from loonet's
models/looncall/v1/README.md applied to BirdNET 2.4 embeddings:

    p = sigmoid(((embedding - mean) / scale) . coef + intercept)

using the arrays in weights.npz. If that reproduces the notebook's recall,
the formula on screen is the model.

Run (loonet's audio venv: birdnet 1.3.1, soundfile, numpy):
    ~/.venvs/loonet-audio/bin/python drone_mix.py <out_dir>
"""
import csv
import sys
from importlib.metadata import version
from pathlib import Path

import numpy as np
import soundfile as sf

LOONET = Path.home() / "Documents/loonet"
DS = LOONET / "data/annotated/looncall_v1"
RAW = LOONET / "data/looncall_raw"
SR = 48000
SNRS = ["clean", 10, 5, 0, -5]
THRESH = 0.5


def rms(x):
    return np.sqrt(np.mean(x ** 2)) + 1e-9


def main():
    out = Path(sys.argv[1]).resolve()
    out.mkdir(parents=True, exist_ok=True)
    val = list(csv.DictReader(open(DS / "val.csv")))
    noise, nsr = sf.read(RAW / "drone/drone_footage.mp3", dtype="float32")
    assert nsr == SR, nsr
    rng = np.random.default_rng(0)

    rows = []
    for snr in SNRS:
        for i, r in enumerate(val):
            a, _ = sf.read(RAW / r["file"], start=int(float(r["start_s"]) * SR),
                           frames=int(3 * SR), dtype="float32")
            if snr != "clean":
                o = rng.integers(0, len(noise) - len(a))
                n = noise[o:o + len(a)]
                a = a + n * (rms(a) / rms(n)) / 10 ** (snr / 20)
                a = a / max(1.0, float(np.abs(a).max()))
            path = out / f"{snr}_{i}.wav"
            sf.write(path, a, SR)
            rows.append({"wav": path.name, "snr": snr, "label": r["label"],
                         "source": r["source"], "file": r["file"], "start_s": r["start_s"]})
    with open(out / "manifest.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    print(f"python {sys.version.split()[0]}  numpy {np.__version__}  soundfile "
          f"{sf.__version__} (libsndfile {sf.__libsndfile_version__})  birdnet {version('birdnet')}")
    print(f"{len(val)} val windows ({sum(int(r['label']) for r in val)} loon) x {len(SNRS)} "
          f"conditions = {len(rows)} clips -> {out}")

    if "--no-birdnet" in sys.argv:
        return
    import birdnet
    W = np.load(LOONET / "models/looncall/v1/weights.npz")
    model = birdnet.load("acoustic", "2.4", "tf", library="litert")
    clips = [str(out / r["wav"]) for r in rows]
    emb = {r["input"]: r["embedding"] for r in model.encode(
        clips, n_workers=4, batch_size=8).to_structured_array() if r["start_time"] == 0}
    E = np.stack([emb[c] for c in clips]).astype(np.float64)
    z = ((E - W["mean"]) / W["scale"]) @ W["coef"].ravel() + float(W["intercept"].ravel()[0])
    p = 1 / (1 + np.exp(-z))
    snr = np.array([r["snr"] for r in rows], dtype=object)
    lab = np.array([int(r["label"]) for r in rows])
    print(f"weights.npz threshold {float(W['threshold']):.2f} · formula applied to BirdNET 2.4 embeddings")
    print(f"{'SNR dB':>7} | loon recall      | false alarms")
    for s in SNRS:
        m = snr == s
        hit = int((p[m & (lab == 1)] >= THRESH).sum())
        fa = int((p[m & (lab == 0)] >= THRESH).sum())
        print(f"{str(s):>7} | {hit:2d}/{int((m & (lab == 1)).sum())} = "
              f"{hit / (m & (lab == 1)).sum():.2f}  | {fa}/{int((m & (lab == 0)).sum())}")
    with open(out / "python_scores.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["wav", "snr", "label", "p_python"])
        for r, pv in zip(rows, p):
            w.writerow([r["wav"], r["snr"], r["label"], f"{pv:.6f}"])


if __name__ == "__main__":
    main()
