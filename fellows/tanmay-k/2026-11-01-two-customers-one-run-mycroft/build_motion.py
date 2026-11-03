#!/usr/bin/env python3
"""Week 29 work-video motion. Each beat = reveal STAGES (the slate drawn with elements up to step k), cross-faded on the cue times in CUES.json
(true Image.blend: old = 1 - e, new = e, one eased progress), plus a slow push-in over the whole beat so no frame is ever dead. Each beat opens with a
short dissolve from the previous beat's last frame. The Short carries a progress rail (eleven dots, the current one lit) so the state carries
across the cuts. Frames are piped straight to ffmpeg (no frame files). Output: _beats/<ID>.mp4 and short/_beats/<ID>.mp4 (silent, 30 fps).
Run: /opt/homebrew/bin/python3.12 build_motion.py [long|short] [IDS...]"""
import json, subprocess, sys
from multiprocessing import Pool
from pathlib import Path
from PIL import Image, ImageDraw
import build_slates as bs

HERE = Path(__file__).parent
CUES = json.loads((HERE / "CUES.json").read_text())
FPS, FADE = 30, 0.35
ZOOM = {"long": 0.022, "short": 0.030}
DISSOLVE = {"long": 0.25, "short": 0.40}
ORDER = {"long": ["B00", "B00b", "B01", "B02", "B03", "B04", "B05", "B06", "B07", "B08", "B09", "B10", "B11", "B12", "B13"],
         "short": ["S-1", "S0", "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9"]}
SIZE = {"long": (3840, 2160), "short": (2160, 3840)}

def ease(x): x = min(1.0, max(0.0, x)); return x * x * (3 - 2 * x)

def stage_images(fmt, bid):
    n = len(CUES[fmt][bid]["stages"]); fr = bs.long_frames if fmt == "long" else bs.short_frames
    full = fr(99, bid)[bid]; shift = full.shift_value(); imgs = []
    for k in range(n):
        c = fr(k, bid)[bid]; im = c.final(shift).convert("RGB")
        if fmt == "short": rail(im, ORDER["short"].index(bid))
        imgs.append(im)
    if fmt == "short" and bid == "S9":   # loop-friendly: the last stage is the Short's own first frame
        first = bs.short_frames(0, "S-1")["S-1"]; im0 = first.final(0).convert("RGB"); rail(im0, 0); imgs.append(im0); return imgs
    assert list(imgs[-1].getdata())[::997] == list(full.final(shift).convert("RGB").getdata())[::997] or fmt == "short", f"{bid}: last stage differs from the full slate"
    return imgs

def rail(im, idx):
    d = ImageDraw.Draw(im); W, H = im.size; n = len(ORDER["short"]); gap = 56; x0 = W / 2 - gap * (n - 1) / 2; y = int(H * 1410 / 1920)  # inside the safe area (73% of the height)
    for i in range(n):
        r = 12 if i == idx else 8
        d.ellipse((x0 + i * gap - r, y - r, x0 + i * gap + r, y + r), fill=bs.SEND if i == idx else bs.BORDER)

def compose(imgs, stages, t):
    """Stage blend at time t (before the push-in)."""
    k = 0
    for i, s in enumerate(stages):
        if t >= s: k = i
    if k == 0: return imgs[0]
    e = ease((t - stages[k]) / FADE)
    return imgs[k] if e >= 1 else Image.blend(imgs[k - 1], imgs[k], e)

def push(im, t, T, fmt):
    z = 1 + ZOOM[fmt] * (t / T); W, H = im.size; w, h = W / z, H / z; x0, y0 = (W - w) / 2, (H - h) / 2
    return im.resize((W, H), Image.BICUBIC, box=(x0, y0, x0 + w, y0 + h))

def frame_at(fmt, imgs, cue, t):
    return push(compose(imgs, cue["stages"], t), t, cue["duration"], fmt)

def render(args):
    fmt, bid = args; cue = CUES[fmt][bid]; imgs = stage_images(fmt, bid); T = cue["duration"]; n = round(T * FPS); W, H = SIZE[fmt]
    outdir = HERE / ("short" if fmt == "short" else "") / "_beats"; outdir.mkdir(exist_ok=True); out = outdir / f"{bid}.mp4"
    prev = None
    i = ORDER[fmt].index(bid)
    if i > 0:
        pb = ORDER[fmt][i - 1]; pc = CUES[fmt][pb]; prev = frame_at(fmt, stage_images(fmt, pb), pc, pc["duration"])
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                           "-c:v", "libx264", "-crf", "16", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-threads", "3", str(out)], stdin=subprocess.PIPE)
    for f in range(n):
        t = f / FPS; im = frame_at(fmt, imgs, cue, t)
        if prev is not None and t < DISSOLVE[fmt]: im = Image.blend(prev, im, ease(t / DISSOLVE[fmt]))
        ff.stdin.write(im.tobytes())
    ff.stdin.close(); ff.wait()
    return bid, n

if __name__ == "__main__":
    fmts = [a for a in sys.argv[1:] if a in ("long", "short")] or ["long", "short"]; only = set(a for a in sys.argv[1:] if a not in ("long", "short"))
    jobs = [(f, b) for f in fmts for b in ORDER[f] if not only or b in only]
    with Pool(4) as p:
        for bid, n in p.imap_unordered(render, jobs): print(f"{bid}: {n} frames", flush=True)
