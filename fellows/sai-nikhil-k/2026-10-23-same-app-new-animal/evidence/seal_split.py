#!/usr/bin/env python3
"""seal_split.py — a seal test set in the format Gavia's own evaluator reads.

Gavia's `examples/evaluate.rs` scores its detector on a YOLO-format split: one
image path per line, labels in a sibling `labels/` folder as `class cx cy w h`
(normalised). This builds such a split from NOAA's public Arctic seal survey
(LILA "NOAA Arctic Seals 2019", CDLA-Permissive):

  - a seeded random sample (seed 20261026) of 20 colour frames that contain at
    least one boxed seal — not the frames with the most seals, not hand-picked
  - each frame downloaded from LILA's public bucket
  - NOAA's own colour-image boxes converted to YOLO labels

Writes evidence/data/seals/{images,labels}/ and evidence/data/seals/split.txt,
and prints what it chose. The detections CSV is the one seal_labels.py uses in
2026-10-19-wildlife-beyond-loons/ (downloaded here if missing).

Run:  python3 evidence/seal_split.py > evidence/seal_split.out
"""
import csv
import collections
import hashlib
import random
import urllib.request
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
BASE = "https://storage.googleapis.com/public-datasets-lila/noaa-kotz/"
DET = HERE / "data" / "surv_test_kamera_detections_20210212_full_paths.csv"
OUT = HERE / "data" / "seals"
SEED, N = 20261026, 20

if not DET.exists():
    DET.parent.mkdir(parents=True, exist_ok=True)
    DET.write_bytes(urllib.request.urlopen(BASE + "Detections/" + DET.name).read())

rows = list(csv.DictReader(DET.open(newline="", encoding="utf-8")))
by_image = collections.defaultdict(list)
for r in rows:
    by_image[r["rgb_image_path"]].append(r)
frames = sorted(by_image)
pick = random.Random(SEED).sample(frames, N)

(OUT / "images").mkdir(parents=True, exist_ok=True)
(OUT / "labels").mkdir(parents=True, exist_ok=True)
lines, total = [], 0
print(f"frames with a seal: {len(frames):,}   sampled: {N}   seed: {SEED}")
for rel in pick:
    img = OUT / "images" / Path(rel).name
    if not img.exists():
        img.write_bytes(urllib.request.urlopen(BASE + rel).read())
    w, h = Image.open(img).size
    labels = []
    for r in by_image[rel]:
        x0, x1 = sorted((float(r["rgb_left"]), float(r["rgb_right"])))
        y0, y1 = sorted((float(r["rgb_top"]), float(r["rgb_bottom"])))
        labels.append(f"0 {(x0 + x1) / 2 / w:.6f} {(y0 + y1) / 2 / h:.6f} "
                      f"{(x1 - x0) / w:.6f} {(y1 - y0) / h:.6f}")
    (OUT / "labels" / (img.stem + ".txt")).write_text("\n".join(labels) + "\n")
    lines.append(str(img))
    total += len(labels)
    sizes = [max(abs(float(r["rgb_right"]) - float(r["rgb_left"])),
                 abs(float(r["rgb_bottom"]) - float(r["rgb_top"]))) for r in by_image[rel]]
    print(f"  {img.name}  {w}x{h}  seals {len(labels):3}  box side px "
          f"min {min(sizes):.0f} max {max(sizes):.0f}  "
          f"sha256 {hashlib.sha256(img.read_bytes()).hexdigest()[:16]}")
(OUT / "split.txt").write_text("\n".join(lines) + "\n")
print(f"seals in the sample: {total}")
