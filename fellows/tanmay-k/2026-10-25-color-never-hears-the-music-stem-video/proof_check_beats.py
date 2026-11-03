#!/usr/bin/env python3
"""Measured checks for the PROOF review of the rendered beats (stills + audio). Independent of the two builders.

LONG  (_stills/B*-16x9.png): size 3840x2160; ink margin >= 60 px (30 logical); a source/footer line present in the
      bottom band (every beat except B13, the sign-off card, which carries its source in the text column);
      palette contrast ratios for every text/background pair the film uses.
SHORT (short/_stills/S*-9x16.png): size 2160x3840; ALL ink inside the safe area (x 60..900, y 230..1440 logical, i.e.
      x 120..1800, y 460..2880 px); nothing in the right rail (x > 920 logical, y > 960 logical); then, from the mixed
      audio, silent runs of 1 s or more and the speech rate per line.
Run: /opt/homebrew/bin/python3.12 proof_check_beats.py
"""
import json
import subprocess
from pathlib import Path
import numpy as np
from PIL import Image

HERE = Path(__file__).parent
BG = np.array([250, 249, 245])


def lum(c):
    c = np.array(c) / 255.0
    c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def contrast(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def hexrgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))


def ink_mask(im, thr=14):
    a = np.asarray(im.convert("RGB")).astype(int)
    return np.abs(a - BG).sum(axis=2) > thr


def bbox(mask):
    ys, xs = np.where(mask)
    return (xs.min(), ys.min(), xs.max(), ys.max()) if len(xs) else None


def long_checks():
    out = []
    for p in sorted((HERE / "_stills").glob("B*-16x9.png")):
        im = Image.open(p)
        m = ink_mask(im)
        bb = bbox(m)
        W, H = im.size
        band = m[int(H * 0.90): int(H * 0.985), :]
        has_src = bool(band.sum() > 200)
        ok_margin = bb[0] >= 60 and bb[1] >= 60 and bb[2] <= W - 60 and bb[3] <= H - 60
        out.append((p.stem, im.size == (3840, 2160), ok_margin, has_src, bb))
    return out


def short_checks():
    out = []
    for p in sorted((HERE / "short" / "_stills").glob("S*-9x16.png")):
        im = Image.open(p)
        m = ink_mask(im)
        bb = bbox(m)
        # ink pixels outside the safe box
        S = 2
        safe = np.zeros_like(m)
        safe[230 * S: 1440 * S, 60 * S: 900 * S] = True
        outside = int((m & ~safe).sum())
        rail = int(m[960 * S:, 920 * S:].sum())
        out.append((p.stem, im.size == (2160, 3840), outside, rail, bb))
    return out


def silent_runs(path, win=0.1, thr_db=-50, min_s=1.0):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-f", "f32le", "-ac", "1", "-ar", "48000", "-"],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(raw, dtype="<f4")
    n = int(win * 48000)
    k = len(x) // n
    r = np.sqrt((x[: k * n].reshape(k, n) ** 2).mean(axis=1) + 1e-12)
    db = 20 * np.log10(r)
    runs, start = [], None
    for i, v in enumerate(db):
        if v < thr_db and start is None:
            start = i
        if v >= thr_db and start is not None:
            if (i - start) * win >= min_s:
                runs.append((round(start * win, 1), round(i * win, 1)))
            start = None
    if start is not None and (k - start) * win >= min_s:
        runs.append((round(start * win, 1), round(k * win, 1)))
    return runs, len(x) / 48000


def main():
    print("PALETTE CONTRAST (WCAG ratio; text >= 4.5)")
    pairs = {"INK on cream": ("#3D3929", "#FAF9F5"), "INK_SOFT on cream": ("#73705F", "#FAF9F5"),
             "SPARK_TEXT on cream": ("#B5532F", "#FAF9F5"), "INK on white chip": ("#3D3929", "#FFFFFF"),
             "INK_SOFT on white": ("#73705F", "#FFFFFF"), "SPARK_TEXT on white": ("#B5532F", "#FFFFFF"),
             "INK on yellow sky": ("#3D3929", "#F2C230"), "white on blue-grey sky": ("#FFFFFF", "#5E7690")}
    for k, (a, b) in pairs.items():
        print(f"  {k:26s} {contrast(hexrgb(a), hexrgb(b)):5.2f}")
    print("\nLONG stills: (name, 4K size, ink margin >= 60 px, source band has ink, ink bbox)")
    bad = 0
    for name, ok_size, ok_margin, has_src, bb in long_checks():
        flag = "" if (ok_size and ok_margin and (has_src or name == "B13-16x9")) else "   <-- CHECK"
        bad += bool(flag)
        print(f"  {name:12s} {ok_size!s:5s} {ok_margin!s:5s} {has_src!s:5s} {tuple(int(v) for v in bb)}{flag}")
    print(f"  long flags: {bad}")
    print("\nSHORT stills: (name, 4K portrait, ink px outside safe box, ink px in right rail, bbox)")
    bad = 0
    for name, ok_size, outside, rail, bb in short_checks():
        flag = "" if (ok_size and outside == 0 and rail == 0) else "   <-- CHECK"
        bad += bool(flag)
        print(f"  {name:12s} {ok_size!s:5s} {outside:7d} {rail:5d} {tuple(int(v) for v in bb)}{flag}")
    print(f"  short flags: {bad}")
    print("\nSHORT audio (short/mp3/short.mix.wav)")
    runs, dur = silent_runs(HERE / "short" / "mp3" / "short.mix.wav")
    print(f"  duration {dur:.2f} s; silent runs >= 1 s (below -50 dB): {runs or 'none'}")
    t = json.loads((HERE / "short" / "mp3" / "timings_short.json").read_text())
    by = {}
    for s in t["sentences"]:
        by.setdefault(s["line"], []).append(s)
    words = {l["id"]: len(l["text"].split()) for l in t["lines"]}
    for lid in sorted(by):
        a, b = by[lid][0]["start"], by[lid][-1]["end"]
        print(f"  {lid}: {a:5.1f}-{b:5.1f} s, {words[lid]:2d} words, {words[lid] / (b - a):.2f} wps")
    gaps = []
    ids = sorted(by)
    for i in range(len(ids) - 1):
        gaps.append((ids[i], round(by[ids[i + 1]][0]["start"] - by[ids[i]][-1]["end"], 2)))
    print("  gap after each line:", gaps)
    print("\nLONG audio (mp3/beat-*.mix.wav): per-beat duration, words per second of narration")
    tim = json.loads((HERE / "mp3" / "timings.json").read_text())
    for b, v in tim.items():
        n = len(v["text"].split())
        print(f"  {b}: narration {v['narration_end_s']:.1f} s, hold {v['hold_s']:.0f} s, total {v['duration_s']:.1f} s, {n / v['narration_end_s']:.2f} wps")


if __name__ == "__main__":
    main()
