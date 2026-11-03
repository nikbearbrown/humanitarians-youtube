#!/usr/bin/env python3
"""Pre-compile checks on the per-beat mp4s: duration vs audio, fades on pixels (stepped, not popped), cue-to-frame sync, last frame vs approved still."""
import json, subprocess, sys
import numpy as np
from pathlib import Path
from PIL import Image
HERE = Path(__file__).parent
CUES = json.loads((HERE / "CUES.json").read_text()); TIM = json.loads((HERE / "mp3" / "timings.json").read_text())
FPS = 30
def frames_small(bid, w=480, h=270):
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", str(HERE / "_beats" / f"{bid}.mp4"), "-vf", f"scale={w}:{h}:flags=area,format=gray", "-f", "rawvideo", "-"], capture_output=True)
    return np.frombuffer(p.stdout, dtype=np.uint8).reshape(-1, h, w).astype(np.float32)
ok = True; rows = []
for bid in sorted(CUES):
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(HERE / "_beats" / f"{bid}.mp4")], capture_output=True, text=True).stdout)
    a = TIM[bid]["duration_s"]; fr = frames_small(bid)
    ev = CUES[bid]["events"]
    chg = (np.abs(np.diff(fr, axis=0)) > 6).mean(axis=(1, 2))          # fraction of pixels that changed by > 6/255 between frames
    active = chg > 1.5e-4; onsets = [i + 1 for i in range(len(chg)) if active[i] and (i == 0 or not active[i - 1])]
    onset_t = [o / FPS for o in onsets]
    runs = []; i = 0
    while i < len(chg):
        if active[i]:
            j = i
            while j < len(chg) and (active[j] or (j + 1 < len(chg) and active[j + 1])): j += 1
            runs.append((i, j - i)); i = j
        else: i += 1
    short = []; pops = []
    for st, n in runs:
        seg = chg[st:st + n]; cum = np.array([(np.abs(fr[min(st + k + 1, len(fr) - 1)] - fr[st]) > 6).mean() for k in range(n)])
        top = cum.max() if len(cum) else 0
        if top < 5e-4: continue                                        # sub-visible
        steps = np.diff(np.concatenate([[0.0], cum]))
        if n < 3 and st > 8: short.append((round(st / FPS, 2), n))
        if steps.max() > 0.6 * top and n >= 1 and top > 3e-3: pops.append((round(st / FPS, 2), round(float(steps.max() / top), 2)))
    cue_ts = [e["t"] for e in ev]
    unmatched = [round(t, 2) for t in cue_ts if t > 0.3 and not any(abs(t - o) <= 2 / FPS for o in onset_t)]
    still = np.asarray(Image.open(HERE / "_stills" / f"{bid}-16x9.png").convert("L").resize((480, 270), Image.BOX), dtype=np.float32)
    last = fr[-1]; diff_last = float(np.abs(last - still).mean())
    rows.append((bid, round(dur, 3), a, round(dur - a, 3), len(runs), short, pops, unmatched, round(diff_last, 2)))
print(f"{'beat':5} {'video':>8} {'audio':>8} {'d':>7} {'fades':>5}  short-runs  pops  cues-without-onset  last-frame-vs-still(mean gray diff)")
for r in rows: print(f"{r[0]:5} {r[1]:8.3f} {r[2]:8.3f} {r[3]:7.3f} {r[4]:5d}  {r[5]}  {r[6]}  {r[7]}  {r[8]}")
