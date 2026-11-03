#!/usr/bin/env python3
"""Production gate, measured on the compiled masters (both films). Short: the 11-point Shorts gate; long: the same measures that apply.
Run: /opt/homebrew/bin/python3.12 proof_motion.py"""
import io, json, re, subprocess, sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageChops
HERE = Path(__file__).parent; sys.path.insert(0, str(HERE))
import build_slates as bs
CUES = json.loads((HERE / "CUES.json").read_text())
PAGE = (0xFA, 0xF9, 0xF5)
FILES = {"long": HERE / "two-customers-one-run-mycroft.mp4", "short": HERE / "short" / "two-customers-one-run-mycroft-short.mp4"}
res = {"long": [], "short": []}
def ok(fmt, name, passed, detail): res[fmt].append(passed); print(f"{'PASS' if passed else 'FAIL'}  [{fmt}] {name}: {detail}")
def run(cmd): return subprocess.run(cmd, capture_output=True, text=True)
def frame(path, t, size=None):
    cmd = ["ffmpeg", "-loglevel", "error", "-ss", f"{t:.3f}", "-i", str(path), "-frames:v", "1"] + (["-vf", f"scale={size[0]}:{size[1]}:flags=area"] if size else []) + ["-f", "image2pipe", "-vcodec", "png", "-"]
    out = subprocess.run(cmd, capture_output=True).stdout
    return Image.open(io.BytesIO(out)).convert("RGB") if out else None
def starts(fmt):
    t = 0.0; out = {}
    for b, v in CUES[fmt].items(): out[b] = t; t += v["duration"]
    return out
ORDER = {f: list(CUES[f]) for f in CUES}
for fmt in ("long", "short"):
    M = FILES[fmt]; W0, H0 = (3840, 2160) if fmt == "long" else (2160, 3840); sm = (960, 540) if fmt == "long" else (540, 960)
    p = run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,r_frame_rate,nb_frames", "-of", "csv=p=0", str(M)]).stdout.strip().split(",")
    ok(fmt, "1 resolution (4K)", (int(p[0]), int(p[1])) == (W0, H0), f"{p[0]}x{p[1]} @ {p[2]} fps, {p[3]} frames")
    dur = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(M)]).stdout)
    if fmt == "short":
        worst = {"top": 9999, "bottom": 0, "right": 0}
        for t in np.arange(0, dur - 0.05, 0.25):
            im = frame(M, float(t), (1080, 1920))
            if im is None: continue
            d = np.asarray(ImageChops.difference(im, Image.new("RGB", im.size, PAGE))).max(axis=2) > 40
            ys, xs = np.where(d)
            if len(ys): worst["top"] = min(worst["top"], ys.min()); worst["bottom"] = max(worst["bottom"], ys.max()); worst["right"] = max(worst["right"], int(d[:, 925:].sum()))
        ok(fmt, "2 safe area (ink 12% to 75% of the height, none right of x 925: a 3% push-in grows the 905 edge to about 925)", worst["top"] >= 0.12 * 1920 * 0.97 and worst["bottom"] <= 0.75 * 1920 * 1.03 and worst["right"] == 0, f"ink from {worst['top'] / 1920:.1%} to {worst['bottom'] / 1920:.1%} of the height; right-rail pixels {worst['right']}")
    # 3. type size: smallest text drawn on any frame of the film
    fr = bs.long_frames(99) if fmt == "long" else bs.short_frames(99); mins = min(size for c in fr.values() for (_, kind, size, *_r) in c.log)
    ok(fmt, "3 type size (logical px at the frame's own width)", mins >= (30 if fmt == "short" else 24), f"smallest {mins} px at {1080 if fmt == 'short' else 1920} wide")
    # 4. figures on screen when spoken (stage active at the phrase time carries the string)
    need = {"long": [("B00b", 0.5, "12"), ("B05", "twelve requests read", "12 request(s) read"), ("B06", "word for word", "weights total 0.0: rescaling by a zero total gives NaN weights (gate addition)"), ("B07", "on the clean run", "YES"),
                     ("B09", "the report says", "Stop conditions: 0 of 4 triggered"), ("B12", "that built", "pull request 81"), ("B12", "the correction", "pull request 82"), ("B13", "signing off", "signing off")],
            "short": [("S-1", 1.0, "Every run of a pipeline needs two different pages"), ("S2", "records seen", '"records_seen": 12'), ("S3", "in its first section", "12 request(s) read"), ("S6", "now it says", "Stop conditions: 0 of 4 triggered"), ("S8", "two customers", "Two Customers"), ("S9", "signing off", "signing off")]}[fmt]
    T = json.loads((HERE / ("short/mp3" if fmt == "short" else "mp3") / "timings.json").read_text()); miss = []
    from cues import tokens, find
    for b, ph, s in need:
        t = ph if isinstance(ph, float) else find(tokens([tuple(w) for w in T[b]["words"]]), ph, 0) + 0.6
        st = CUES[fmt][b]["stages"]; k = max(i for i, x in enumerate(st) if t >= x + bs_fade if False) if False else max(i for i, x in enumerate(st) if t >= x + 0.35)
        c = (bs.long_frames(k, b) if fmt == "long" else bs.short_frames(k, b))[b]; shown = " ".join(x[0] for x in c.log)
        if s not in shown: miss.append((b, s))
    ok(fmt, "4 every spoken figure on screen when spoken", not miss, f"{len(need)} moments checked" + (f"; missing {miss}" if miss else ""))
    # 6/7: frame-to-frame change
    pr = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-i", str(M), "-vf", f"scale={sm[0]}:{sm[1]}:flags=area,format=gray", "-f", "rawvideo", "-"], stdout=subprocess.PIPE)
    prev = None; means = []; moved = []; FS = sm[0] * sm[1]
    while True:
        buf = pr.stdout.read(FS)
        if len(buf) < FS: break
        cur = np.frombuffer(buf, dtype=np.uint8).astype(np.int16)
        if prev is not None: dd = np.abs(cur - prev); means.append(float(dd.mean())); moved.append(int((dd > 10).sum()))
        prev = cur
    means = np.array(means); moved = np.array(moved)
    ok(fmt, "6 no hard cuts", means.max() < 6.0, f"largest frame-to-frame change {means.max():.2f} grey levels (a cut would be 20+); {len(means) + 1} frames")
    rl = best = at = 0
    for i, mv in enumerate(moved):
        rl = rl + 1 if mv < 10 else 0
        if rl > best: best, at = rl, i
    lim = 3.0 if fmt == "short" else 8.0
    ok(fmt, f"7 no static stretch over {lim:.0f} s", best / 30 <= lim, f"longest stretch with fewer than 10 pixels changing {best / 30:.2f} s (ending at {at / 30:.1f} s)")
    # 8 loop
    if fmt == "short":
        a = frame(M, 0.0, (1080, 1920)); b2 = frame(M, dur - 0.1, (1080, 1920))
        dl = float(np.abs(np.asarray(a.convert("L"), dtype=np.float32) - np.asarray(b2.convert("L"), dtype=np.float32)).mean())
        ok(fmt, "8 loop-friendly last frame", dl < 3.5, f"first vs last frame: mean difference {dl:.2f} grey levels")
    # 9 audio
    ap = run(["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=codec_name,sample_rate,channels", "-of", "csv=p=0", str(M)]).stdout.strip()
    ln = run(["ffmpeg", "-i", str(M), "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"]).stderr
    j = json.loads(re.search(r"\{[^{}]*input_i[^{}]*\}", ln, re.S).group(0)); I, TPk = float(j["input_i"]), float(j["input_tp"])
    sil = run(["ffmpeg", "-i", str(M), "-af", "silencedetect=noise=-45dB:d=0.5", "-f", "null", "-"]).stderr
    lens = [float(e) - float(s) for s, e in zip(re.findall(r"silence_start: ([\d.]+)", sil), re.findall(r"silence_end: ([\d.]+)", sil))]
    ok(fmt, "9 audio", ap == "aac,48000,1" and -15 <= I <= -13 and TPk <= -1.45 and (fmt == "long" or not lens or max(lens) < 1.0), f"{ap}; {I:.1f} LUFS; {TPk:.1f} dBTP; silences >= 0.5 s: {[round(x, 2) for x in lens] or 'none'}")
    # 10 identity
    code = (HERE / ("READ-ALOUD-signed.md" if fmt == "long" else "short/READ-ALOUD-SHORT-signed.md")).read_text(); handles = re.findall(r"@\w+", code)
    ok(fmt, "10 no foreign identity", not handles, f"handles in the signed script: {handles or 'none'}")
    # 11 duration + first frame
    f0 = frame(M, 0.0, sm); ink0 = (np.asarray(ImageChops.difference(f0, Image.new("RGB", f0.size, PAGE))).max(axis=2) > 12).mean()
    ok(fmt, "11 duration and first frame", dur <= (180 if fmt == "short" else 900) and ink0 > 0.005, f"{dur:.1f} s; first frame has content ({ink0:.1%} of pixels)")
for f in res: print(f"\nGATE {f}: {sum(res[f])}/{len(res[f])} checks pass")
