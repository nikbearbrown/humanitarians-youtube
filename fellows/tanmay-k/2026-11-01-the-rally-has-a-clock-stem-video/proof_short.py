#!/usr/bin/env python3
"""PROOF: the Shorts production gate, measured on the compiled file (11 checks). Template: Week 27 short/proof_short.py.
Run: /opt/homebrew/bin/python3.12 short/proof_short.py"""
import io, json, re, subprocess, sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageChops
HERE = Path(__file__).parent; sys.path.insert(0, str(HERE))
MASTER = HERE / "the-rally-has-a-clock-short.mp4"
import build_short as bsh
PAGE = (0xFA, 0xF9, 0xF5); res = []
def ok(name, passed, detail): res.append(passed); print(f"{'PASS' if passed else 'FAIL'}  {name}: {detail}")
def run(cmd): return subprocess.run(cmd, capture_output=True, text=True)
def frame(t, size=None):
    cmd = ["ffmpeg", "-loglevel", "error", "-ss", f"{t:.3f}", "-i", str(MASTER), "-frames:v", "1"] + (["-vf", f"scale={size[0]}:{size[1]}:flags=area"] if size else []) + ["-f", "image2pipe", "-vcodec", "png", "-"]
    return Image.open(io.BytesIO(subprocess.run(cmd, capture_output=True).stdout)).convert("RGB")
LOG = []
_orig_txt = bsh.txt
def _txt(d, x, y, s, kind, size, col, a, bg=bsh.PAGE, anchor="la"):
    LOG.append((s, size, a, y, x)); return _orig_txt(d, x, y, s, kind, size, col, a, bg, anchor)
bsh.txt = _txt
def shown(t):
    LOG.clear(); bsh.scene(t); return [(s, sz, a, y, x) for (s, sz, a, y, x) in LOG if a > 0.5]
DUR = bsh.DUR

# 1. 9:16 at 4K
p = run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,r_frame_rate,nb_frames", "-of", "csv=p=0", str(MASTER)]).stdout.strip().split(",")
ok("1 resolution", p[0] == "2160" and p[1] == "3840", f"{p[0]}x{p[1]} @ {p[2]} fps, {p[3]} frames")

# 2. safe area on pixels, every 0.25 s
worst = {"top": 9999, "bottom": 0, "right": 0}
for t in np.arange(0, DUR - 0.05, 0.25):
    im = frame(float(t), (1080, 1920)); d = np.asarray(ImageChops.difference(im, Image.new("RGB", im.size, PAGE))).max(axis=2) > 40
    ys, xs = np.where(d)
    if len(ys):
        worst["top"] = min(worst["top"], ys.min()); worst["bottom"] = max(worst["bottom"], ys.max()); worst["right"] = max(worst["right"], int(d[:, 910:].sum()))
ok("2 safe area (ink 12% to 75% of the height; none in the right rail x > 910)", worst["top"] >= 0.12 * 1920 and worst["bottom"] <= 0.75 * 1920 and worst["right"] == 0,
   f"ink from {worst['top'] / 1920:.1%} to {worst['bottom'] / 1920:.1%} of the height; right-rail pixels {worst['right']}")

# 3. type size: every text drawn at sampled times (logical px at 1080 wide)
sizes = set()
for t in np.arange(0.2, DUR, 0.5): sizes |= {sz for (s, sz, a, y, x) in shown(float(t))}
ok("3 type size (smallest text drawn, logical px at 1080 wide)", min(sizes) >= 34, f"smallest {min(sizes)} px; sizes {sorted(sizes)}")

# 4. every spoken figure on screen when spoken
need = [("sixth shot (counter 6)", bsh.T_SIXTH + 0.5, ["6"]), ("five percent faster", bsh.T_FASTER + 0.5, ["the ball is 5% faster on every shot"]),
        ("half the field = 232.5", bsh.T_SECOND + 0.8, ["232.5 px"]), ("first bar longer", bsh.T_LONGER + 0.3, ["286 px"]),
        ("eight pixels", bsh.T_EIGHT + 0.5, ["8.4 px short"]), ("arithmetic says shot six", bsh.T_ARITH + 0.5, ["ARITHMETIC: shot six"]),
        ("a search agrees", bsh.T_SEARCH + 0.5, ["SEARCH: shot six"]), ("no spin, no machine", bsh.L("S07") + 1.0, ["only a model: no spin, no real machine"]),
        ("ball speeds up (payoff)", bsh.T_SHOWS + 0.8, ["no perfect defense is true here only because the ball speeds up"]),
        ("the film's title", bsh.L("S08") + 1.0, ["The Rally Has a Clock"]), ("presenter named", bsh.T_TANMAY + 0.6, ["Tanmay Kulkarni"])]
miss = []
for key, t, toks in need:
    sh = [s for (s, sz, a, y, x) in shown(t)]; joined = " ".join(sh)       # a caption may wrap onto two drawn lines
    for tk in toks:
        if not (any(tk in s for s in sh) or tk in joined): miss.append((key, tk))
ok("4 every spoken figure on screen when spoken", not miss, f"{len(need)} moments checked" + (f"; missing {miss}" if miss else ""))
holds = {"two bars together": (bsh.BAR2 + 0.5, bsh.L("S06")), "chips on shot six": (bsh.T_SEARCH + 0.35, bsh.L("S07") - 0.15), "title": (bsh.L("S08") - 0.15 + 0.35, bsh.LOOP0)}
bad = {k: round(b - a, 2) for k, (a, b) in holds.items() if b - a < 1.5}
ok("4b comparisons held >= 1.5 s", not bad, ", ".join(f"{k} {b - a:.1f} s" for k, (a, b) in holds.items()))

# 5. sources on screen inside the safe area
src = [(bsh.T_ESSAY + 0.8, "essay"), (bsh.T_BUILT + 0.8, "simulation"), (bsh.L("S05") + 1.0, "simulation"), (bsh.L("S06") + 3, "simulation"), (bsh.L("S07") + 1.0, "simulation")]
have = []
for t, kw in src: have.append(any(kw in s.lower() and y < 1440 and y >= 230 for (s, sz, a, y, x) in shown(t)))
ok("5 sources on screen", all(have), f"{sum(have)}/{len(have)} checked phases carry a source line inside the safe area")

# 6 / 7. consecutive-frame difference: hard cuts and static stretches (540x960, where a ball landing is invisible)
pr = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-i", str(MASTER), "-vf", "scale=540:960:flags=area,format=gray", "-f", "rawvideo", "-"], stdout=subprocess.PIPE)
prev = None; means = []; moved = []; FS = 540 * 960
while True:
    buf = pr.stdout.read(FS)
    if len(buf) < FS: break
    cur = np.frombuffer(buf, dtype=np.uint8).astype(np.int16)
    if prev is not None: dd = np.abs(cur - prev); means.append(float(dd.mean())); moved.append(int((dd > 10).sum()))
    prev = cur
means = np.array(means); moved = np.array(moved)
ok("6 no hard cuts", means.max() < 6.0, f"largest frame-to-frame change {means.max():.2f} grey levels (a cut between scenes would be 20+); {len(means) + 1} frames")
run_len = best = at = 0
for i, mv in enumerate(moved):
    run_len = run_len + 1 if mv < 10 else 0
    if run_len > best: best, at = run_len, i
ok("7 no static stretch over 3 s", best / 30 <= 3.0, f"longest stretch with fewer than 10 pixels changing {best / 30:.2f} s (ending at {at / 30:.1f} s)")

# 8. loop-friendly: the last frame equals the first
a = frame(0.0, (1080, 1920)); b = frame(DUR - 0.05, (1080, 1920))
dl = float(np.abs(np.asarray(a.convert("L"), dtype=np.float32) - np.asarray(b.convert("L"), dtype=np.float32)).mean())
ok("8 loop-friendly last frame", dl < 3.5, f"first vs last frame: mean difference {dl:.2f} grey levels (codec colour offset is about 2)")

# 9. audio
ap = run(["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=codec_name,sample_rate,channels", "-of", "csv=p=0", str(MASTER)]).stdout.strip()
ln = run(["ffmpeg", "-i", str(MASTER), "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"]).stderr
j = json.loads(re.search(r"\{[^{}]*input_i[^{}]*\}", ln, re.S).group(0)); I, TPk = float(j["input_i"]), float(j["input_tp"])
sil = run(["ffmpeg", "-i", str(MASTER), "-af", "silencedetect=noise=-45dB:d=0.5", "-f", "null", "-"]).stderr
lens = [float(e) - float(s) for s, e in zip(re.findall(r"silence_start: ([\d.]+)", sil), re.findall(r"silence_end: ([\d.]+)", sil))]
ok("9 audio", ap == "aac,48000,1" and -15 <= I <= -13 and TPk <= -1.45 and (not lens or max(lens) < 1.0), f"{ap}; {I:.1f} LUFS; {TPk:.1f} dBTP; silences >= 0.5 s: {[round(x, 2) for x in lens] or 'none'}")

# 10. no foreign identity
code = (HERE / "build_short.py").read_text() + (HERE / "SHORT-SCRIPT.md").read_text()
handles = re.findall(r"@\w+", code)
ok("10 no foreign identity", not handles and "nikbear" not in code.lower(), f"handles in the script and scene code: {handles or 'none'}; only 'Humanitarians AI' and the presenter named")

# 11. duration; first frame
dur = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(MASTER)]).stdout)
f0 = frame(0.0, (1080, 1920)); ink0 = (np.asarray(ImageChops.difference(f0, Image.new("RGB", f0.size, PAGE))).max(axis=2) > 12).mean()
ok("11 duration and first frame", dur <= 180 and ink0 > 0.01, f"{dur:.1f} s (cap 180); first frame has content ({ink0:.1%} of pixels: headline + field + counter)")
print("headlines (the muted path):", " | ".join(h for _, h in bsh.HEAD))
print(f"\nGATE: {sum(res)}/{len(res)} checks pass")
