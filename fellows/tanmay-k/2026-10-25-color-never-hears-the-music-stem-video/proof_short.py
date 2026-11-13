#!/usr/bin/env python3
"""PROOF: the Shorts production gate, MEASURED on the compiled file (11 checks). Adapted from Week 27's proof_short.py.
Reads short/color-never-hears-the-music-short.mp4 (pixels, audio), _qc/render_log.json (the text the builder drew in every
frame), mp3/timings_short.json (word times) and SHORT-SCRIPT.md. Writes VIDEO-GATE-SHORT.md and extracts review frames
to _qc/frames/.
Run: /opt/homebrew/bin/python3.12 short/proof_short.py"""
import importlib.util
import io
import json
import re
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).parent
MASTER = HERE / "color-never-hears-the-music-short.mp4"
QC = HERE / "_qc"
(QC / "frames").mkdir(parents=True, exist_ok=True)
spec = importlib.util.spec_from_file_location("bshort", HERE / "build_short.py")
bsh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bsh)
L, _src = bsh.line_starts()
RL = json.loads((QC / "render_log.json").read_text())
LOG = {int(k): v for k, v in RL["log"].items()}
TM = json.loads((HERE / "mp3" / "timings_short.json").read_text())
PAGE = np.array([0xFA, 0xF9, 0xF5])
results = []
lines_out = []


def ok(name, passed, detail):
    results.append(passed)
    msg = f"{'PASS' if passed else 'FAIL'}  {name}: {detail}"
    print(msg)
    lines_out.append(msg)


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def frames_raw(vf, w, h, pix="rgb24", ss=None):
    cmd = ["ffmpeg", "-loglevel", "error", "-i", str(MASTER), "-vf", vf, "-f", "rawvideo", "-pix_fmt", pix, "-"]
    out = subprocess.run(cmd, capture_output=True).stdout
    bpp = 3 if pix == "rgb24" else 1
    n = len(out) // (w * h * bpp)
    return np.frombuffer(out[: n * w * h * bpp], dtype=np.uint8).reshape(n, h, w, bpp if bpp == 3 else 1)


def frame_png(t, name, size=None):
    vf = f"scale={size[0]}:{size[1]}:flags=area" if size else "null"
    out = subprocess.run(["ffmpeg", "-loglevel", "error", "-ss", f"{t:.3f}", "-i", str(MASTER), "-frames:v", "1", "-vf", vf,
                          "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
    im = Image.open(io.BytesIO(out)).convert("RGB")
    im.save(QC / "frames" / f"{name}.png")
    return im


# 1. resolution, fps, frame count, first frame is the opening state (never black)
pj = json.loads(run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,r_frame_rate,nb_frames,pix_fmt,codec_name",
                     "-of", "json", str(MASTER)]).stdout)["streams"][0]
f0 = np.asarray(frame_png(0.0, "t000_first", (1080, 1920))).astype(int)
sky0 = f0[500:560, 200:700].reshape(-1, 3).mean(axis=0)
grey = np.array([0xB9, 0xB8, 0xB2])
ok("1 resolution and first frame", pj["width"] == 2160 and pj["height"] == 3840 and np.abs(sky0 - grey).max() < 14 and f0.mean() > 150,
   f"{pj['width']}x{pj['height']} @ {pj['r_frame_rate']} fps, {pj['nb_frames']} frames, {pj['codec_name']}/{pj['pix_fmt']}; frame 0 sky colour "
   f"{tuple(int(v) for v in sky0)} (opening grey {tuple(int(v) for v in grey)}, distance {np.abs(sky0 - grey).max():.0f}); not black: mean {f0.mean():.0f}")

# 2. ink zones on pixels, every 0.5 s
fr = frames_raw("fps=2,scale=1080:1920:flags=area", 1080, 1920)
xmin, xmax, ymin, ymax, rail = 9999, 0, 9999, 0, 0
for im in fr:
    m = np.abs(im.astype(int) - PAGE).sum(axis=2) > 60
    ys, xs = np.where(m)
    if len(xs):
        xmin, xmax, ymin, ymax = min(xmin, xs.min()), max(xmax, xs.max()), min(ymin, ys.min()), max(ymax, ys.max())
        rail = max(rail, int(m[960:, 921:].sum()))
ok("2 ink zones", xmin >= 57 and xmax <= 903 and ymin >= 224 and ymax <= 1443 and rail == 0,
   f"{len(fr)} frames sampled every 0.5 s: ink x {xmin}..{xmax} (safe 60..900), y {ymin}..{ymax} (safe 230..1440); right-rail pixels {rail}")

# 3. type size across every rendered frame
sizes = [e[1] for v in LOG.values() for e in v]
ok("3 type size", min(sizes) >= 34, f"{len(LOG)} frames, {len(sizes)} text draws (alpha > 0.3): smallest {min(sizes)} px logical (floor 34); sizes in use {sorted(set(sizes))}")

# 4. spoken figures on screen when spoken
words = TM["words"]
sents = TM["sentences"]
by_line = {}
for s in sents:
    by_line.setdefault(s["line"], []).append(s)
span = {k: (v[0]["start"], v[-1]["end"]) for k, v in by_line.items()}


def word_time(line, pred):
    a, b = span[line]
    for w, s0, e0 in words:
        if a - 0.05 <= s0 <= b + 0.05 and pred(re.sub(r"[^a-z0-9.']", "", w.lower())):
            return s0
    return None


def on_screen(t, token):
    i = min(max(int(t * 30), 0), max(LOG) )
    return any(token in e[0] for e in LOG[i])


checks = [("S03 spoken '97' (ninety seven)", "S03", lambda w: w in ("97", "ninety"), 0.5, "97 listeners"),
          ("S03 spoken 'Bach'", "S03", lambda w: w.startswith("bach"), 0.9, "Bach"),
          ("S03 spoken 'Brahms'", "S03", lambda w: w.startswith("brahms"), 1.4, "Brahms"),
          ("S05 spoken 'Bach's' example", "S05", lambda w: w.startswith("bach"), 0.9, "Bach"),
          ("S05 spoken 'Brahms's' example", "S05", lambda w: w.startswith("brahms"), 0.9, "Brahms"),
          ("S04 'closely' (0.99 counter has landed)", "S04", lambda w: w.startswith("closely"), 0.0, "0.99"),
          ("S04 source 0.89-0.99 while the ratings are spoken", "S04", lambda w: w.startswith("rated"), 0.3, "0.89"),
          ("S08 title spoken", "S08", lambda w: w.startswith("color"), 1.0, "Color Never Hears")]
miss, det = [], []
for name, line, pred, dt, tok in checks:
    wt = word_time(line, pred)
    if wt is None:
        miss.append((name, "word not found"))
        continue
    good = on_screen(wt + dt, tok)
    det.append(f"{name} @ {wt + dt:.1f}s {'ok' if good else 'MISSING'}")
    if not good:
        miss.append((name, tok))
ok("4 figures on screen when spoken", not miss, "; ".join(det) + (f"; missing {miss}" if miss else ""))

# 5. sources inside the safe area, every line
have = []
for k in sorted(span):
    a, b = L[k], (L[sorted(x for x in L if x.startswith('S'))[sorted(x for x in L if x.startswith('S')).index(k) + 1]] if k != "S08" else L["END"])
    t = (a + b) / 2
    i = int(t * 30)
    src = [e for e in LOG[i] if e[1] >= 34 and e[2] > 0.5 and 1335 <= e[4] <= 1440 and re.search(r"Illustration|Palmer|Emotion ratings|paper|Correlation", e[0])]
    have.append((k, bool(src)))
ok("5 sources in the safe area", all(h for _, h in have), f"{sum(h for _, h in have)}/{len(have)} lines show a source line (34 px, y 1335..1440) at mid-line: {have}")

# 6 / 7. consecutive-frame difference (540x960 gray)
g = frames_raw("scale=540:960:flags=area", 540, 960, pix="gray")[..., 0].astype(np.int16)
means = np.abs(g[1:] - g[:-1]).mean(axis=(1, 2))
moved = (np.abs(g[1:] - g[:-1]) > 10).sum(axis=(1, 2))
order = np.argsort(means)[::-1][:3]
ok("6 no hard cuts", means.max() < 3.0,
   f"{len(g)} frames; largest frame-to-frame mean change {means.max():.2f} grey levels (threshold 3.0: a full-scene cut is 20+, a sky colour wash between frames is under 1); "
   f"three largest at {[round(float(i + 1) / 30, 2) for i in order]} s = {[round(float(means[i]), 2) for i in order]}")
run_len = best = at = 0
for i, mv in enumerate(moved):
    run_len = run_len + 1 if mv < 10 else 0
    if run_len > best:
        best, at = run_len, i
gap = 75  # 2.5 s at 30 fps
pair = [(np.abs(g[i + gap] - g[i]) > 12).mean() * 100 for i in range(0, len(g) - gap, 15)]
ok("7 no static stretch over 3 s", best / 30 <= 3.0 and min(pair) >= 0.3,
   f"longest run with fewer than 10 pixels changing between frames {best / 30:.2f} s (ends {at / 30:.1f} s); change between frames 2.5 s apart: min {min(pair):.2f}%, median {float(np.median(pair)):.2f}%")

# 8. loop-friendly: last frame vs frame 0
a, b = g[0], g[-1]
d = np.abs(a - b) > 12
ys, xs = np.where(d)
lx0, ly0, lx1, ly1 = bsh.LX0 / 2, bsh.LY0 / 2, bsh.LX1 / 2, 1240 / 2     # the opening landscape runs down to y 1240 logical
inside = (not len(xs)) or (xs.min() >= lx0 - 3 and xs.max() <= lx1 + 3 and ys.min() >= ly0 - 3 and ys.max() <= ly1 + 3)
frame_png(L["END"] - 0.15, "t_last", (1080, 1920))
ok("8 loop-friendly last frame", d.mean() * 100 < 8 and inside,
   f"last frame differs from frame 0 in {d.mean() * 100:.2f}% of pixels, all inside the landscape box: {inside} (clouds only); bbox x {xs.min() if len(xs) else '-'}..{xs.max() if len(xs) else '-'}, y {ys.min() if len(ys) else '-'}..{ys.max() if len(ys) else '-'} at 540x960")

# 9. audio
ap = run(["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=codec_name,sample_rate,channels", "-of", "csv=p=0", str(MASTER)]).stdout.strip()
ln = run(["ffmpeg", "-i", str(MASTER), "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"]).stderr
j = json.loads(re.search(r"\{[^{}]*input_i[^{}]*\}", ln, re.S).group(0))
I, TPk = float(j["input_i"]), float(j["input_tp"])
sil = run(["ffmpeg", "-i", str(MASTER), "-af", "silencedetect=noise=-50dB:d=0.7", "-f", "null", "-"]).stderr
lens = [float(e) - float(s) for s, e in zip(re.findall(r"silence_start: ([\d.]+)", sil), re.findall(r"silence_end: ([\d.]+)", sil))]
ok("9 audio", ap == "aac,48000,1" and -15 <= I <= -13 and TPk <= -1.45 and (not lens or max(lens) < 1.0),
   f"{ap}; {I:.1f} LUFS (target -14); true peak {TPk:.1f} dBTP (limit -1.5); silences >= 0.7 s: {[round(x, 2) for x in lens] or 'none'}")

# 10. no foreign text: every word drawn on screen appears in SHORT-SCRIPT.md
vocab = set(re.findall(r"[a-z']+", (HERE / "SHORT-SCRIPT.md").read_text().lower()))
drawn = {e[0] for v in LOG.values() for e in v}
unknown = sorted({w for s in drawn for w in re.findall(r"[a-z']+", s.lower()) if w not in vocab})
handles = [s for s in drawn if "@" in s]
ok("10 no foreign text or handle", not unknown and not handles,
   f"{len(drawn)} distinct strings drawn; words not in SHORT-SCRIPT.md: {unknown or 'none'}; handles: {handles or 'none'}")

# 11. duration
vd = float(run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=duration", "-of", "csv=p=0", str(MASTER)]).stdout)
ad = float(run(["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=duration", "-of", "csv=p=0", str(MASTER)]).stdout)
ok("11 duration", abs(vd - ad) <= 0.05 and 74 <= vd <= 77 and vd <= 180,
   f"video {vd:.3f} s, audio {ad:.3f} s (difference {abs(vd - ad) * 1000:.0f} ms); target about 75.5 s; Shorts limit 180 s")

# review frames (mid-transition moments)
for name, t in [("S01_mid", (L["S01"] + L["S02"]) / 2), ("S03_sky_cooling", L["S03"] + (L["S04"] - L["S03"]) * 0.78), ("S04_dots", L["S04"] + (L["S05"] - L["S04"]) * 0.6),
                ("S06_swap", L["S06"] + 4), ("S08_title", L["S08"] + 4.0), ("S08_loop_fade", L["END"] - 0.35)]:
    frame_png(t, name, (1080, 1920))
print(f"\nGATE: {sum(results)}/{len(results)} checks pass")
(HERE / "VIDEO-GATE-SHORT.md").write_text(
    "# Video gate — Short (9:16), measured on the compiled file\n\n"
    f"File: `{MASTER.name}`. Measured by `short/proof_short.py` (pixels from the compiled mp4, the builder's text log of every frame, the Whisper word clock). Voice: Kokoro `am_onyx`.\n\n"
    + "\n".join(f"- {m}" for m in lines_out) + f"\n\n**GATE: {sum(results)}/{len(results)}**\n")
