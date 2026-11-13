#!/usr/bin/env python3
"""PROOF: the Shorts production gate, MEASURED on the compiled file (11 checks), work-video Short. Adapted from the topic
video's proof_short.py. Reads short/the-sum-behind-the-number-short.mp4 (pixels, audio), _qc/render_log.json (the text the
builder drew in every frame), mp3/timings_short.json (word times) and ../SHORT-SCRIPT.md. Writes VIDEO-GATE-SHORT.md and
extracts review frames to _qc/frames/.
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
MASTER = HERE / "the-sum-behind-the-number-short.mp4"
QC = HERE / "_qc"
(QC / "frames").mkdir(parents=True, exist_ok=True)
spec = importlib.util.spec_from_file_location("bshort", HERE / "build_short.py")
bsh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bsh)
L, _src = bsh.line_starts()
bsh.anchor_windows(L)
RL = json.loads((QC / "render_log.json").read_text())
LOG = {int(k): v for k, v in RL["log"].items()}
TM = json.loads((HERE / "mp3" / "timings_short.json").read_text())
WORDS = TM["words"]
PAGE = np.array([0xFA, 0xF9, 0xF5])
results, lines_out = [], []


def ok(name, passed, detail):
    results.append(passed)
    msg = f"{'PASS' if passed else 'FAIL'}  {name}: {detail}"
    print(msg)
    lines_out.append(msg)


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def frames_raw(vf, w, h, pix="rgb24"):
    out = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", str(MASTER), "-vf", vf, "-f", "rawvideo", "-pix_fmt", pix, "-"], capture_output=True).stdout
    bpp = 3 if pix == "rgb24" else 1
    n = len(out) // (w * h * bpp)
    return np.frombuffer(out[: n * w * h * bpp], dtype=np.uint8).reshape(n, h, w, bpp)


def frame_png(t, name, size=None):
    vf = f"scale={size[0]}:{size[1]}:flags=area" if size else "null"
    out = subprocess.run(["ffmpeg", "-loglevel", "error", "-ss", f"{t:.3f}", "-i", str(MASTER), "-frames:v", "1", "-vf", vf,
                          "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
    im = Image.open(io.BytesIO(out)).convert("RGB")
    im.save(QC / "frames" / f"{name}.png")
    return im


# 1. resolution, fps, frame count, frame 0 is the opening state (cream page, never black)
pj = json.loads(run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,r_frame_rate,nb_frames,pix_fmt,codec_name",
                     "-of", "json", str(MASTER)]).stdout)["streams"][0]
f0 = np.asarray(frame_png(0.0, "t000_first", (1080, 1920))).astype(int)
corner = f0[1700:1900, 900:1060].reshape(-1, 3).mean(axis=0)
ink0 = bool((np.abs(f0[330:480, 60:900] - PAGE).sum(axis=2) > 120).any())      # the headline number's ink is on frame 0
ok("1 resolution and first frame", pj["width"] == 2160 and pj["height"] == 3840 and np.abs(corner - PAGE).max() < 6 and f0.mean() > 200 and ink0,
   f"{pj['width']}x{pj['height']} @ {pj['r_frame_rate']} fps, {pj['nb_frames']} frames, {pj['codec_name']}/{pj['pix_fmt']}; frame 0 page colour "
   f"{tuple(int(v) for v in corner)} (cream {tuple(int(v) for v in PAGE)}), mean {f0.mean():.0f} (not black), the opening number is drawn: {ink0}")

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


# 4. spoken figures on screen when spoken (at the word's time + 0.4 s)
def on_screen(t, token):
    i = min(max(int(t * 30), 0), max(LOG))
    return any(token in e[0] for e in LOG[i])


def wt(alts, lo):
    return bsh._wt(WORDS, alts, lo)


S = lambda k: L[k]
w_names = wt("names", S("S03"))
checks = [("S01 '78' (the number)", wt(["78", "seventy"], S("S01")), "78"),
          ("S03 'market' -15%", wt(["15"], wt("market", w_names)), "−15%"), ("S03 '35'", wt(["35"], wt("semi", S("S03"))), "−35%"),
          ("S03 '40'", wt(["40"], wt("ai", S("S03") + 8)), "−40%"), ("S03 '30'", wt(["30"], wt("technology", S("S03"))), "−30%"),
          ("S04 '15'", wt(["15"], S("S04") + 6), "−15"), ("S04 '35' (running total 50)", wt(["35"], S("S04") + 6), "−50"),
          ("S04 '90'", wt(["90"], S("S04") + 6), "−90"), ("S05 '90'", wt(["90"], S("S05")), "−90"),
          ("S05 '50'", wt(["50"], S("S05") + 2), "−50"), ("S06 '36'", wt(["36"], S("S06")), "36"),
          ("S06 '27'", wt(["27"], S("S06")), "+ 27"), ("S06 '15'", wt(["15"], S("S06") + 4), "+ 15"), ("S06 '78'", wt(["78"], S("S06")), "= 78"),
          ("S07 '24'", wt(["24"], S("S07")), "of 24"), ("S08 title spoken", wt("the", wt("is", wt("film", S("S08")))), "The")]
miss, det = [], []
for name, t0, tok in checks:
    good = on_screen(t0 + 0.4, tok)
    det.append(f"{name} @ {t0 + 0.4:.1f}s {'ok' if good else 'MISSING'}")
    if not good:
        miss.append((name, tok))
# the closing card carries the exact title while it is spoken
title_ok = on_screen(S("S08") + 6.0, "The Sum Behind the Number") or on_screen(S("END") - 1.5, "The Sum Behind the Number")
ok("4 figures on screen when spoken", not miss and title_ok, "; ".join(det) + f"; the exact title on the closing card: {title_ok}" + (f"; missing {miss}" if miss else ""))

# 5. sources inside the safe area, on every line
keys = sorted(k for k in L if k.startswith("S"))
have = []
for k in keys:
    a_ = L[k]
    b_ = L[keys[keys.index(k) + 1]] if k != "S08" else L["END"] - 1.2
    t = (a_ + b_) / 2
    src = [e for e in LOG[int(t * 30)] if e[1] >= 34 and e[2] > 0.5 and 1335 <= e[4] <= 1440 and e[0] == bsh.SOURCES[k].split("\n")[0][:len(e[0])]]
    have.append((k, bool(src)))
ok("5 sources in the safe area", all(h for _, h in have), f"{sum(h for _, h in have)}/{len(have)} lines show their source line (34 px, y 1335..1440) at mid-line: {have}")

# 6 / 7. consecutive-frame difference (540x960 gray)
g = frames_raw("scale=540:960:flags=area", 540, 960, pix="gray")[..., 0].astype(np.int16)
means = np.abs(g[1:] - g[:-1]).mean(axis=(1, 2))
moved = (np.abs(g[1:] - g[:-1]) > 10).sum(axis=(1, 2))
order = np.argsort(means)[::-1][:3]
ok("6 no hard cuts", means.max() < 3.0,
   f"{len(g)} frames; largest frame-to-frame mean change {means.max():.2f} grey levels (threshold 3.0: a full-scene cut is 20+); "
   f"three largest at {[round(float(i + 1) / 30, 2) for i in order]} s = {[round(float(means[i]), 2) for i in order]}")
run_len = best = at = 0
for i, mv in enumerate(moved):
    run_len = run_len + 1 if mv < 10 else 0
    if run_len > best:
        best, at = run_len, i
gap = 75
pair = [(np.abs(g[i + gap] - g[i]) > 12).mean() * 100 for i in range(0, len(g) - gap, 15)]
ok("7 no static stretch over 3 s", best / 30 <= 3.0 and min(pair) >= 0.3,
   f"longest run with fewer than 10 pixels changing between frames {best / 30:.2f} s (ends {at / 30:.1f} s); change between frames 2.5 s apart: min {min(pair):.3f}%, median {float(np.median(pair)):.3f}%")

# 8. loop-friendly: the last frame returns to the opening state
d = np.abs(g[0] - g[-1]) > 12
ys, xs = np.where(d)
frame_png(L["END"] - 0.04, "t_last", (1080, 1920))
ok("8 loop-friendly last frame", d.mean() * 100 < 1.0,
   f"last frame differs from frame 0 in {d.mean() * 100:.3f}% of pixels (a closing 1.0 s ease returns the number, the chips and the empty stack to the opening state); "
   f"bbox x {xs.min() if len(xs) else '-'}..{xs.max() if len(xs) else '-'}, y {ys.min() if len(ys) else '-'}..{ys.max() if len(ys) else '-'} at 540x960")

# 9. audio
ap = run(["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=codec_name,sample_rate,channels", "-of", "csv=p=0", str(MASTER)]).stdout.strip()
ln = run(["ffmpeg", "-i", str(MASTER), "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"]).stderr
j = json.loads(re.search(r"\{[^{}]*input_i[^{}]*\}", ln, re.S).group(0))
I, TPk = float(j["input_i"]), float(j["input_tp"])
sil = run(["ffmpeg", "-i", str(MASTER), "-af", "silencedetect=noise=-50dB:d=0.7", "-f", "null", "-"]).stderr
starts, ends = re.findall(r"silence_start: ([\d.]+)", sil), re.findall(r"silence_end: ([\d.]+)", sil)
lens = [float(e) - float(s_) for s_, e in zip(starts, ends)]
tail = (float(starts[-1]), TM["duration_s"] - float(starts[-1])) if len(starts) > len(ends) else None
ok("9 audio", ap == "aac,48000,1" and -15 <= I <= -13 and TPk <= -1.45 and (not lens or max(lens) < 1.0) and (tail is None or tail[1] < 1.0),
   f"{ap}; {I:.1f} LUFS (target -14); true peak {TPk:.1f} dBTP (limit -1.5); silences >= 0.7 s inside the track: {[round(x, 2) for x in lens] or 'none'}; "
   f"end tail {('%.2f s of silence from %.2f s' % (tail[1], tail[0])) if tail else 'none'}")

# 10. no foreign text: every word drawn on screen appears in SHORT-SCRIPT.md
vocab = set(re.findall(r"[a-z']+", (HERE.parent / "SHORT-SCRIPT.md").read_text().lower()))
# typed text passes through partial strings for a frame or two each; the check is on strings that stay on screen >= 6 frames
from collections import Counter
cnt = Counter(e[0] for v in LOG.values() for e in v)
drawn = {k for k, c in cnt.items() if c >= 6 and not any(o != k and o.startswith(k) for o in cnt)}
unknown = sorted({w for s_ in drawn for w in re.findall(r"[a-z']+", s_.lower()) if w not in vocab})
handles = [s_ for s_ in drawn if "@" in s_]
ok("10 no foreign text or handle", not unknown and not handles,
   f"{len(drawn)} distinct strings on screen >= 6 frames ({len(cnt)} including typing partials); words not in SHORT-SCRIPT.md: {unknown or 'none'}; handles: {handles or 'none'}")

# 11. duration
vd = float(run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=duration", "-of", "csv=p=0", str(MASTER)]).stdout)
ad = float(run(["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=duration", "-of", "csv=p=0", str(MASTER)]).stdout)
ok("11 duration", abs(vd - ad) <= 0.05 and abs(vd - TM["duration_s"]) <= 0.05 and vd <= 180,
   f"video {vd:.3f} s, audio {ad:.3f} s (difference {abs(vd - ad) * 1000:.0f} ms); narration track {TM['duration_s']:.3f} s; Shorts limit 180 s")

# review frames
mid = lambda a_, b_, f: a_ + (b_ - a_) * f
review = [("S01_mid", mid(L["S01"], L["S02"], 0.85)), ("S03_rows", bsh.xt(L, "S03", "tv") + 0.8), ("S04_blocks", bsh.xt(L, "S04", "t90") + 0.4),
          ("S05_bars", bsh.xt(L, "S05", "n50") + 0.8), ("S06_arithmetic", bsh.xt(L, "S06", "a78") + 0.8), ("S07_columns", mid(L["S07"], L["S08"], 0.92)),
          ("S08_card", L["END"] - bsh.LOOP_FADE - 0.3)]
for name, t in review:
    frame_png(t, name, (1080, 1920))
print(f"\nGATE: {sum(results)}/{len(results)} checks pass")
(HERE / "VIDEO-GATE-SHORT.md").write_text(
    "# Video gate: work-video Short (9:16), measured on the compiled file\n\n"
    f"File: `{MASTER.name}`. Measured by `short/proof_short.py` (pixels from the compiled mp4, the builder's text log of every frame, the Whisper word clock). Voice: Kokoro `am_onyx`.\n\n"
    + "\n".join(f"- {m}" for m in lines_out) + f"\n\n**GATE: {sum(results)}/{len(results)}**\n")
