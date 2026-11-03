#!/usr/bin/env python3
"""seal_labels.py — measure the NOAA Arctic seals set a seal-counting Gavia could train on.

Source: LILA "NOAA Arctic Seals 2019" (lila.science/datasets/noaa-arctic-seals-2019),
Alaska Fisheries Science Center, released under CDLA-Permissive 1.0. LILA's page
says "around 80,000 color and IR (thermal) images" and "around 28,000 bounding
boxes (14,000 on color images, 14,000 on thermal images)". This counts both
from the published files: the detections CSV (one row = one seal, boxed on the
colour image and on the paired thermal image) and the full file list.

Run:  python3 evidence/seal_labels.py > evidence/seal_labels.out
      (downloads both files into evidence/data/ first if they are missing)
"""
import collections
import csv
import datetime
import hashlib
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = "https://storage.googleapis.com/public-datasets-lila/noaa-kotz/"
DET = HERE / "data" / "surv_test_kamera_detections_20210212_full_paths.csv"
FILES = HERE / "data" / "surv_test_kamera_files.txt"

for path, url in ((DET, BASE + "Detections/" + DET.name), (FILES, BASE + FILES.name)):
    if not path.exists():
        path.parent.mkdir(exist_ok=True)
        path.write_bytes(urllib.request.urlopen(url).read())

print(f"date      {datetime.datetime.now().isoformat(timespec='seconds')}")
for p in (DET, FILES):
    print(f"file      {p.name}  {p.stat().st_size:,} bytes  "
          f"sha256 {hashlib.sha256(p.read_bytes()).hexdigest()}")
print("licence   CDLA-Permissive 1.0 (LILA page; JSON-LD license https://cdla.io/permissive-1-0/)")
print()

rows = list(csv.DictReader(DET.open(newline="", encoding="utf-8")))
files = [l.strip() for l in FILES.open(encoding="utf-8") if l.strip()]
rgb = [f for f in files if f.lower().endswith(".jpg")]
ir = [f for f in files if f.lower().endswith(".tif")]
rgb_boxes = sum(1 for r in rows if r["rgb_left"] not in ("", "NA"))
ir_boxes = sum(1 for r in rows if r["ir_left"] not in ("", "NA"))

print("WHAT IS IN THE RELEASE")
print(f"  detections (seals)        {len(rows):,}")
print(f"  boxes on colour images    {rgb_boxes:,}")
print(f"  boxes on thermal images   {ir_boxes:,}")
print(f"  boxes, both kinds         {rgb_boxes + ir_boxes:,}")
print(f"  files listed              {len(files):,}  (colour .jpg {len(rgb):,} · thermal .tif {len(ir):,} "
      f"· other {len(files) - len(rgb) - len(ir):,})")
print(f"  colour images with a seal {len({r['rgb_image_name'] for r in rows}):,}")
print()
print("DETECTION TYPES")
for k, v in collections.Counter(r["detection_type"] for r in rows).most_common():
    print(f"  {k:22} {v:6,}")
