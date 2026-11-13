#!/usr/bin/env python3
"""make_survey_crops.py — one NOAA survey frame, as the model would see it two ways.

From the seal_split.py sample, the frame with the most seals inside a single
960 px window (Gavia's tile size for these 6576 x 4384 frames, see
seal_scale.out). Writes, unaltered except for cropping and downscaling:

  images/src/noaa_frame.jpg   the whole frame, downscaled to 2400 px wide
  images/src/noaa_tile.jpg    one 960 x 960 crop around those seals, full resolution
  images/src/noaa_tile_boxed.jpg   the same crop with NOAA's label boxes outlined
  + .json sidecars (source URL, licence, crop box, sha256 of the original)

Run:  python3 evidence/make_survey_crops.py
"""
import datetime
import hashlib
import json
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
REEL = HERE.parent
FRAME = "polar_bear_2019_fl07_C_20190512_002916.093618_rgb"
SRC = HERE / "data" / "seals" / "images" / f"{FRAME}.jpg"
LABELS = HERE / "data" / "seals" / "labels" / f"{FRAME}.txt"
TILE = 960

im = Image.open(SRC)
w, h = im.size
pts = [(float(a) * w, float(b) * h)
       for _, a, b, _, _ in (l.split() for l in LABELS.read_text().split("\n") if l.strip())]
cx, cy = sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts)
x0 = int(min(max(0, cx - TILE / 2), w - TILE))
y0 = int(min(max(0, cy - TILE / 2), h - TILE))
box = (x0, y0, x0 + TILE, y0 + TILE)
inside = sum(box[0] <= x < box[2] and box[1] <= y < box[3] for x, y in pts)

out = REEL / "images" / "src"
im.resize((2400, round(2400 * h / w)), Image.LANCZOS).save(out / "noaa_frame.jpg", quality=92)
tile = im.crop(box)
tile.save(out / "noaa_tile.jpg", quality=95)
# The same tile with NOAA's own boxes outlined (their labels, not a model's).
from PIL import ImageDraw
boxed = tile.copy(); d = ImageDraw.Draw(boxed)
for _, a, b, bw, bh in (l.split() for l in LABELS.read_text().split("\n") if l.strip()):
    x, y = float(a) * w - box[0], float(b) * h - box[1]
    hw, hh = float(bw) * w / 2 + 10, float(bh) * h / 2 + 10
    if 0 <= x < TILE and 0 <= y < TILE:
        d.rectangle((x - hw, y - hh, x + hw, y + hh), outline=(217, 119, 87), width=4)
boxed.save(out / "noaa_tile_boxed.jpg", quality=95)
common = {
    "title": f"NOAA Arctic Seals 2019 — {FRAME}.jpg",
    "author": "NOAA Alaska Fisheries Science Center",
    "source": "LILA, NOAA Arctic Seals 2019 — https://lila.science/datasets/noaa-arctic-seals-2019/",
    "file": f"https://storage.googleapis.com/public-datasets-lila/noaa-kotz/Images/fl07/CENT/{FRAME}.jpg",
    "license": "CDLA-Permissive-1.0",
    "license_url": "https://cdla.dev/permissive-1-0/",
    "original_size": [w, h],
    "original_sha256": hashlib.sha256(SRC.read_bytes()).hexdigest(),
    "seals_in_frame": len(pts),
    "fetched": datetime.date.today().isoformat(),
}
json.dump({**common, "derived": "whole frame, downscaled to 2400 px wide (Lanczos)"},
          open(out / "noaa_frame.json", "w"), indent=2)
json.dump({**common, "derived": f"crop {box} of the original, no scaling",
           "seals_in_crop": inside}, open(out / "noaa_tile.json", "w"), indent=2)
json.dump({**common, "derived": f"crop {box} of the original, no scaling, with NOAA's own "
           "label boxes outlined in orange (10 px padding)", "seals_in_crop": inside},
          open(out / "noaa_tile_boxed.json", "w"), indent=2)
print(f"{FRAME}: {w}x{h}, {len(pts)} seals; tile {box} holds {inside}")
