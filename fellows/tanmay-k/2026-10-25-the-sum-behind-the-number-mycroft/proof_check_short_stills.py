#!/usr/bin/env python3
"""Pixel check of the work-video Short's review stills (read-only).

All ink inside the safe box (x 60..900, y 230..1440 logical = x 120..1800, y 460..2880 px at 2160x3840); nothing in the
right rail (x > 920 logical in the lower half, y > 960); the file is 2160x3840. Prints one line per still and a summary.
Run: /opt/homebrew/bin/python3.12 short/proof_check_short_stills.py
"""
from pathlib import Path
import numpy as np
from PIL import Image

HERE = Path(__file__).parent
BG = np.array([250, 249, 245])
S = 2
TOL = 2     # px of anti-aliasing at the box edge


def main():
    bad = 0
    files = sorted((HERE / "_stills").glob("S*-9x16.png"))
    for p in files:
        im = Image.open(p)
        a = np.asarray(im.convert("RGB")).astype(int)
        m = np.abs(a - BG).sum(axis=2) > 14
        safe = np.zeros_like(m)
        safe[(230 * S - TOL): (1440 * S + TOL), (60 * S - TOL): (900 * S + TOL)] = True
        outside = int((m & ~safe).sum())
        rail = int(m[960 * S:, 920 * S:].sum())
        ys, xs = np.where(m)
        ok = im.size == (2160, 3840) and outside == 0 and rail == 0
        bad += not ok
        print(f"{p.stem:12s} {im.size[0]}x{im.size[1]} outside={outside:5d} rail={rail:3d} "
              f"bbox x{xs.min() / S:.0f}-{xs.max() / S:.0f} y{ys.min() / S:.0f}-{ys.max() / S:.0f} {'OK' if ok else '<-- CHECK'}")
    print(f"{len(files)} stills, {bad} flagged")


if __name__ == "__main__":
    main()
