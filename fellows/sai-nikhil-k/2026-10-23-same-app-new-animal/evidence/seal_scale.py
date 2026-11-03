#!/usr/bin/env python3
"""seal_scale.py — how big is a seal by the time Gavia's model sees it?

Gavia's model looks at 640 x 640 pixels. A whole photo is shrunk to fit; with
tiling on, the photo is cut into overlapping square tiles first, and each tile
is shrunk to 640. `plan_tiles()` below is a line-for-line Python copy of
`plan_tiles` in desktop/src-tauri/src/detection/preprocess.rs at v0.3.1
(defaults: overlap 0.2, at most 64 tiles; tiles grow x1.5 until they fit).

Seal sizes come from the 20-frame NOAA sample in evidence/data/seals/ (labels
written by seal_split.py from NOAA's own boxes): the longer side of each box.

Run:  python3 evidence/seal_scale.py > evidence/seal_scale.out
"""
import statistics
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
SEALS = HERE / "data" / "seals"
MODEL = 640


def window_starts(extent, window, stride):
    if extent <= window:
        return [0]
    last = extent - window
    starts = list(range(0, last + 1, stride))
    if starts[-1] != last:
        starts.append(last)
    return starts


def plan_tiles(width, height, model_size=MODEL, overlap=0.2, max_tiles=64, threshold=1.5):
    if width <= model_size * threshold and height <= model_size * threshold:
        return 1, max(width, height)
    tile = model_size
    while True:
        stride = max(1, int(tile * (1 - overlap)))
        xs, ys = window_starts(width, tile, stride), window_starts(height, tile, stride)
        if len(xs) * len(ys) <= max_tiles:
            return len(xs) * len(ys), tile
        tile = int(tile * 1.5)


sides, sizes = [], set()
for label in sorted((SEALS / "labels").glob("*.txt")):
    w, h = Image.open(SEALS / "images" / (label.stem + ".jpg")).size
    sizes.add((w, h))
    for line in label.read_text().split("\n"):
        if line.strip():
            _, _, _, bw, bh = map(float, line.split())
            sides.append(max(bw * w, bh * h))

(w, h), = sizes                      # every sampled frame is the same size
n_tiles, tile = plan_tiles(w, h)
s = statistics.median(sides)
print(f"frames        {len(list((SEALS / 'labels').glob('*.txt')))} NOAA colour frames, all {w} x {h}")
print(f"seals         {len(sides)}")
print(f"seal size     median {s:.0f} px (longer box side), range {min(sides):.0f}-{max(sides):.0f}")
print(f"tile plan     {n_tiles} tiles of {tile} px (Gavia v0.3.1 defaults)")
print(f"whole photo   {s:.0f} x {MODEL} / {w} = {s * MODEL / w:.1f} px at the model")
print(f"one tile      {s:.0f} x {MODEL} / {tile} = {s * MODEL / tile:.1f} px at the model")
