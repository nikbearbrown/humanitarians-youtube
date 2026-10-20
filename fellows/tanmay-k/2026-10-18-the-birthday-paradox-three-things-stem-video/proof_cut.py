#!/usr/bin/env python3
"""PROOF mechanical pass on the compiled cut. Run: /opt/homebrew/bin/python3.12 proof_cut.py"""
import json, re, subprocess
from pathlib import Path
import numpy as np
from PIL import Image
HERE = Path(__file__).parent; QC = HERE / "_qc"
MASTER = HERE / "the-birthday-paradox-three-things.mp4"
plan = json.loads((HERE / "_motion" / "plan.json").read_text())
starts = json.loads((HERE / "_beats" / "beat_starts.json").read_text())
timings = json.loads((HERE / "mp3" / "timings.json").read_text())

def grab(t, size=None):
    cmd = ["ffmpeg", "-loglevel", "error", "-ss", f"{t:.3f}", "-i", str(MASTER), "-frames:v", "1"]
    if size: cmd += ["-vf", f"scale={size[0]}:{size[1]}:flags=area"]
    cmd += ["-f", "image2pipe", "-vcodec", "png", "-"]
    import io; return Image.open(io.BytesIO(subprocess.run(cmd, capture_output=True).stdout)).convert("RGB")

# 1. frames at 15 / 50 / 85 % of each beat (review set)
for b, p in plan.items():
    for pct in (15, 50, 85):
        t = starts[b] + p["duration_s"] * pct / 100
        if not (QC / f"{b}_{pct}.png").exists(): grab(t).resize((1920, 1080), Image.LANCZOS).save(QC / f"{b}_{pct}.png")
print("frames saved:", len(list(QC.glob('B*_*.png'))))

# 2. does the cut show the intended reveal state at each cue (+0.5 s) and not before (-0.4 s)?
SZ = (480, 270)
def small(path): return np.asarray(Image.open(path).convert("L").resize(SZ, Image.LANCZOS), dtype=np.float32)
bad = []; base = []; n = 0
for b, p in plan.items():
    cues = p["cues"]
    for i, (stage, t) in enumerate(cues):
        if i == 0: continue
        target = small(HERE / "_motion" / f"{b}_s{stage}.png"); prev = small(HERE / "_motion" / f"{b}_s{cues[i-1][0]}.png")
        t_after = min(t + 0.5, (cues[i + 1][1] - 0.15) if i + 1 < len(cues) else p["duration_s"] - 0.1)
        if t_after <= t + 0.1: t_after = t + 0.15
        after = np.asarray(grab(starts[b] + t_after, SZ).convert("L"), dtype=np.float32)
        before = np.asarray(grab(starts[b] + max(0, t - 0.4), SZ).convert("L"), dtype=np.float32)
        d_at, d_ap = np.abs(after - target).mean(), np.abs(after - prev).mean()      # after the cue: nearer the new state
        d_bp, d_bt = np.abs(before - prev).mean(), np.abs(before - target).mean()    # before the cue: nearer the old state
        gap = np.abs(target - prev).mean(); n += 1
        if gap > 0.15 and not (d_at < d_ap and d_bp < d_bt):
            bad.append((b, stage, round(t, 2), round(float(d_at), 2), round(float(d_ap), 2), round(float(d_bp), 2), round(float(d_bt), 2)))
base.append(float(np.abs(np.asarray(grab(starts["B01"] + 8.0, SZ).convert("L"), dtype=np.float32) - small(HERE / "_motion" / "B01_s4.png")).mean()))
print(f"stage timing: {n} reveals checked, {len(bad)} mistimed", bad[:10], f"(mean-abs gray offset of an unchanged frame vs its PNG, from yuv420 conversion: {base[0]:.2f})")

# 3. holds: time each comparison is fully on screen
holds = {"B05": 2, "B07": 1, "B09": 4, "B12": 5, "B13": 5, "B15": 6, "B17": 4}
print("holds (all items of the comparison on screen, until the next change or the end of the beat):")
for b, st in holds.items():
    cues = plan[b]["cues"]; i = next(i for i, (s, _) in enumerate(cues) if s == st)
    end = cues[i + 1][1] if i + 1 < len(cues) else plan[b]["duration_s"]
    print(f"  {b}: stage {st} from {cues[i][1]:.2f}s, held {end - cues[i][1]:.2f}s  {'OK' if end - cues[i][1] >= 2 else 'SHORT'}")

# 4. silence map of the master (>=0.5 s): the B16 hold and any gaps inside narration
r = subprocess.run(["ffmpeg", "-i", str(MASTER), "-af", "silencedetect=noise=-45dB:d=0.5", "-f", "null", "-"], capture_output=True, text=True).stderr
sil = [(float(a), float(b)) for a, b in zip(re.findall(r"silence_start: ([\d.]+)", r), re.findall(r"silence_end: ([\d.]+)", r))]
order = sorted(starts, key=starts.get)
def which(t):
    return max((b for b in order if starts[b] <= t + 1e-3), key=lambda b: starts[b])
print("silences >= 0.5 s inside beats (excluding the 0.6 s beat joins and the B16 hold):")
for a, b in sil:
    bid = which(a + 0.01); rel = a - starts[bid]; ln = b - a
    lastw = timings[bid]["words"][-1][2]   # Kokoro ends a beat with its own trailing silence: judge against the last heard word
    kind = "B16 hold" if bid == "B16" and rel > lastw - 0.05 else ("end hold" if rel >= lastw - 0.05 else ("beat join" if ln < 0.9 and rel < 0.3 else "INSIDE NARRATION"))
    print(f"  {bid} at {rel:6.2f}s  length {ln:5.2f}s  {kind}")
b16 = [(a, b) for a, b in sil if which(a + .01) == "B16" and a - starts["B16"] > timings["B16"]["narration_end_s"] - 0.5]
print("B16 hold measured:", f"{max(b - a for a, b in b16):.2f} s" if b16 else "none")

# 5. black / frozen-start frames and resolution
r = subprocess.run(["ffmpeg", "-i", str(MASTER), "-vf", "blackdetect=d=0.05:pix_th=0.05", "-an", "-f", "null", "-"], capture_output=True, text=True).stderr
print("black segments:", re.findall(r"black_start:[\d.]+ black_end:[\d.]+", r) or "none")
print(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=width,height,r_frame_rate,duration", "-of", "csv=p=0", str(MASTER)], capture_output=True, text=True).stdout.strip())
