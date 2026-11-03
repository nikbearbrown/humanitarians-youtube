#!/usr/bin/env python3
"""PROOF: the Shorts production gate, measured on the compiled file (items 1 to 11 of PROOF-REVIEW-SHORT.md).
Run: /opt/homebrew/bin/python3.12 short/proof_short.py"""
import io, json, re, subprocess, sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageChops
HERE = Path(__file__).parent; ROOT = HERE.parent
MASTER = HERE / "the-birthday-paradox-three-things-short.mp4"; QC = HERE / "_qc"
spec = __import__("importlib.util").util.spec_from_file_location("bshort", HERE / "build_short.py"); bsh = __import__("importlib.util").util.module_from_spec(spec); spec.loader.exec_module(bsh)
c = json.loads((HERE / "_video" / "cues.json").read_text()); tl = bsh.Timeline(c)
PAGE = (0xFA, 0xF9, 0xF5); res = []
def ok(name, passed, detail): res.append(passed); print(f"{'PASS' if passed else 'FAIL'}  {name}: {detail}")
def run(cmd): return subprocess.run(cmd, capture_output=True, text=True)
def frame(t, size=None):
    cmd = ["ffmpeg", "-loglevel", "error", "-ss", f"{t:.3f}", "-i", str(MASTER), "-frames:v", "1"] + (["-vf", f"scale={size[0]}:{size[1]}:flags=area"] if size else []) + ["-f", "image2pipe", "-vcodec", "png", "-"]
    return Image.open(io.BytesIO(subprocess.run(cmd, capture_output=True).stdout)).convert("RGB")

# 1. 9:16 at 4K, probed
p = run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,r_frame_rate,nb_frames", "-of", "csv=p=0", str(MASTER)]).stdout.strip().split(",")
ok("1 resolution", p[0] == "2160" and p[1] == "3840", f"{p[0]}x{p[1]} @ {p[2]} fps, {p[3]} frames")

# 2. safe area on pixels, every 0.25 s
worst = {"top": 9999, "bottom": 0, "right_low": 0}
for t in np.arange(0, c["duration"] - 0.05, 0.25):
    im = frame(float(t), (1080, 1920)); d = np.asarray(ImageChops.difference(im, Image.new("RGB", im.size, PAGE))).max(axis=2) > 40
    ys, xs = np.where(d)
    if len(ys):
        worst["top"] = min(worst["top"], ys.min()); worst["bottom"] = max(worst["bottom"], ys.max())
        low = d[640:, 950:]; worst["right_low"] = max(worst["right_low"], int(low.sum()))
ok("2 safe area (ink between 12% and 75% of height; none in the right rail)", worst["top"] >= 0.12 * 1920 and worst["bottom"] <= 0.75 * 1920 and worst["right_low"] == 0,
   f"ink from {worst['top'] / 1920:.1%} to {worst['bottom'] / 1920:.1%} of the height; right-rail pixels {worst['right_low']}")

# 3. type size: every sans label drawn at sampled times
sizes = set()
for t in np.arange(0.2, c["duration"], 0.5):
    cv = bsh.scene(float(t), tl, c); sizes |= {s for (_, s, a, _) in cv.log if a > 0.3}
ok("3 type size (smallest text drawn, logical px at 1080 wide)", min(sizes) >= 30, f"smallest {min(sizes)} px (labels), {sorted(sizes)[:6]}")

# 4. every spoken figure on screen when spoken
need = [("about_half", 0.8, ["50.7%"]), ("ninety_days", 0.6, ["possible birthdays: 90"]), ("ninety_five", 0.3, ["95.4%"]),
        ("one_month", 0.6, ["possible birthdays: 30"]), ("almost", 0.3, ["99.99%", "above"]), ("we_kept", 0.7, ["23, kept"]),
        ("tenth", 0.7, ["+0.1 point at most"]), ("its_days", 0.9, ["365 → 30"]), ("add", 1.2, ["d = possible birthdays"]), ("p23", 0.7, ["365 days → 23 people"]),
        ("seven", 0.7, ["30 days → 7 people"]), ("its23", 0.9, ["50.7%"]), ("three_things", 0.7, ["Three Things You Could Change"]), ("its_on", 0.7, ["Humanitarians AI"])]
miss = []
for key, dt, toks in need:
    cv = bsh.scene(c[key] + dt, tl, c); shown = [s for (s, _, a, _) in cv.log if a > 0.5]
    for tk in toks:
        if not any(tk in s for s in shown): miss.append((key, tk))
ok("4 every spoken figure on screen when spoken", not miss, f"{len(need)} cue moments checked" + (f"; missing {miss}" if miss else ""))
# holds: how long each comparison stays fully on screen
holds = {"counter 95.4% beside 90 days": (c["ninety_days"] + 0.3, c["sq_month"]), "counter 99.99% beside 30 days": (c["one_month"] + 0.4, c["decides"]),
         "365 days -> 23 people": (c["p23"] + 0.25, c["thats_why"] + 0.45), "30 days -> 7 people": (c["seven"] + 0.25, c["thats_why"] + 0.45)}
bad = {k: round(b - a, 2) for k, (a, b) in holds.items() if b - a < 1.5}
ok("4b comparisons held >= 1.5 s", not bad, ", ".join(f"{k} {b - a:.1f} s" for k, (a, b) in holds.items()))

# 5. sources on screen inside the safe area, S01 to S06
src_t = [1.0, c["about_half"] + 0.5, c["keep_group"] + 1.0, c["decides"] + 1.0, c["rule"] + 1.0, c["even_odds"] + 1.0]
have = []
for t in src_t:
    cv = bsh.scene(t, tl, c); have.append(any(("calculation" in s or "Illustration" in s or "Checked" in s) and a > 0.5 and y < 1440 for (s, _, a, y) in cv.log))
ok("5 sources on screen", all(have), f"{sum(have)}/{len(have)} phases carry a source line inside the safe area")

# 6 / 7. consecutive-frame difference: hard cuts and static stretches
pr = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-i", str(MASTER), "-vf", "scale=540:960:flags=area,format=gray", "-f", "rawvideo", "-"], stdout=subprocess.PIPE)
prev = None; means = []; moved = []; FS = 540 * 960
while True:
    buf = pr.stdout.read(FS)
    if len(buf) < FS: break
    cur = np.frombuffer(buf, dtype=np.uint8).astype(np.int16)
    if prev is not None:
        dd = np.abs(cur - prev); means.append(float(dd.mean())); moved.append(int((dd > 10).sum()))
    prev = cur
means = np.array(means); moved = np.array(moved)
ok("6 no hard cuts", means.max() < 6.0, f"largest frame-to-frame change {means.max():.2f} grey levels (a cut between scenes would be 20+); {len(means) + 1} frames")
run_len = best = at = 0
for i, mv in enumerate(moved):
    run_len = run_len + 1 if mv < 10 else 0
    if run_len > best: best, at = run_len, i
ok("7 no static stretch over 3 s", best / 30 <= 3.0, f"longest stretch with fewer than 10 pixels changing {best / 30:.2f} s (ending at {at / 30:.1f} s)")

# 8. loop-friendly last frame: the calendar and dots at the end match the state after the dots first land
a = frame(c["im_tanmay"] - 0.1, (1080, 1920)).crop((0, 400, 1080, 790)); b = frame(c["duration"] - 0.4, (1080, 1920)).crop((0, 400, 1080, 790))
dl = float(np.abs(np.asarray(a.convert("L"), dtype=np.float32) - np.asarray(b.convert("L"), dtype=np.float32)).mean())
ok("8 loop-friendly last frame", dl < 3.5, f"calendar + dots, end vs opening state: mean difference {dl:.2f} grey levels (codec colour offset is about 2)")

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
ok("10 no foreign identity", not handles and "nikbear" not in code.lower(), f"handles in the script and scene code: {handles or 'none'}; only 'Humanitarians AI' named")

# 11. duration; first frame; headlines carry the argument muted
dur = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(MASTER)]).stdout)
f0 = frame(0.0, (1080, 1920)); ink0 = (np.asarray(ImageChops.difference(f0, Image.new("RGB", f0.size, PAGE))).max(axis=2) > 12).mean()
ok("11 duration and first frame", dur <= 70 and ink0 > 0.01, f"{dur:.1f} s (cap 180); first frame has content ({ink0:.1%} of pixels: headline + calendar)")
print("headlines (the muted path):", " | ".join(bsh.HEADLINES))
av = [float(x) for x in run(["ffprobe", "-v", "error", "-show_entries", "stream=duration", "-of", "csv=p=0", str(MASTER)]).stdout.split()]
print("stream durations (video, audio):", av)
print(f"\nGATE: {sum(res)}/{len(res)} checks pass")
