#!/usr/bin/env python3
"""demo_mix.py — one whole recording, clean and under the drone, for the app screenshots.

Takes loon_2081153.mp3 (iNaturalist, Mount Desert, Maine, CC0; a looncall
*val* recording, so the model never trained on it) and writes:

    loon_maine_clean.wav       the recording as is (48 kHz mono)
    loon_maine_drone5db.wav    the same recording with the drone's propeller
                               noise mixed in at 5 dB SNR, window by window,
                               exactly the way loonet's test mixes (drone_mix.py):
                               each 3 s window gets noise scaled to its own RMS,
                               then is peak-normalised.

Both files are opened in Gavia's "Check an audio" for the B06 plate, and
scored by listen.rs so the screenshot can be checked against the code.

Run:  ~/.venvs/loonet-audio/bin/python demo_mix.py <out_dir>
"""
import sys
from pathlib import Path

import numpy as np
import soundfile as sf

RAW = Path.home() / "Documents/loonet/data/looncall_raw"
SR, WIN, SNR = 48000, 3 * 48000, 5


def rms(x):
    return np.sqrt(np.mean(x ** 2)) + 1e-9


def main():
    out = Path(sys.argv[1]).resolve()
    out.mkdir(parents=True, exist_ok=True)
    a, sr = sf.read(RAW / "loon/loon_2081153.mp3", dtype="float32")
    assert sr == SR and a.ndim == 1, (sr, a.shape)
    noise, _ = sf.read(RAW / "drone/drone_footage.mp3", dtype="float32")
    rng = np.random.default_rng(20261030)
    mixed = []
    for s in range(0, len(a), WIN):
        w = a[s:s + WIN]
        o = rng.integers(0, len(noise) - len(w))
        n = noise[o:o + len(w)]
        w = w + n * (rms(w) / rms(n)) / 10 ** (SNR / 20)
        mixed.append(w / max(1.0, float(np.abs(w).max())))
    sf.write(out / "loon_maine_clean.wav", a, SR)
    sf.write(out / "loon_maine_drone5db.wav", np.concatenate(mixed), SR)
    print(f"loon_2081153.mp3: {len(a) / SR:.1f} s at {SR} Hz -> {out}/loon_maine_clean.wav, "
          f"loon_maine_drone5db.wav ({len(mixed)} windows mixed at {SNR} dB, seed 20261030)")


if __name__ == "__main__":
    main()
