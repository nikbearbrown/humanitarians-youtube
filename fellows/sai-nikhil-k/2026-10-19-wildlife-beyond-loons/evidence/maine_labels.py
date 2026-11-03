#!/usr/bin/env python3
"""maine_labels.py — measure the Maine seabird label release that a next Gavia would train on.

Source: Kline, Lewis, Maher & Loftin (2023), "Point locations and species and
behavioral identifications of colonial nesting seabirds on Maine's coastal
islands interpreted from 2019 plane-based imagery", USGS data release
doi:10.5066/P92SL92P (ScienceBase 642d7360d34ee8d4add393cb). The release is one
CSV of bird points plus metadata: the imagery itself is not in it.

What it measures, from the CSV alone: how many birds were labelled, on how
many islands, the reconciled species split, and how often the observers who
looked at a bird agreed on its species before reconciling.

Run:  python3 evidence/maine_labels.py > evidence/maine_labels.out
      (downloads the CSV into evidence/data/ first if it is missing)
"""
import collections
import csv
import datetime
import hashlib
import json
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
ITEM = "https://www.sciencebase.gov/catalog/item/642d7360d34ee8d4add393cb?format=json"
CSV = HERE / "data" / "GOM2019SeabirdImageryCounts_FINAL.csv"

if not CSV.exists():
    item = json.load(urllib.request.urlopen(ITEM))
    url = next(f["url"] for f in item["files"] if f["name"] == CSV.name)
    CSV.parent.mkdir(exist_ok=True)
    CSV.write_bytes(urllib.request.urlopen(url).read())

rows = list(csv.DictReader(CSV.open(newline="", encoding="utf-8-sig")))
print(f"date      {datetime.datetime.now().isoformat(timespec='seconds')}")
print(f"file      {CSV.name}  {CSV.stat().st_size:,} bytes  "
      f"sha256 {hashlib.sha256(CSV.read_bytes()).hexdigest()}")
print(f"release   doi:10.5066/P92SL92P  (ScienceBase 642d7360d34ee8d4add393cb)")
print()

ids = {r["Unique_Bird_ID_Num"] for r in rows}
islands = {r["IslandName"] for r in rows}
print("WHAT IS IN THE RELEASE")
print(f"  bird points (rows)        {len(rows):,}")
print(f"  unique bird ids           {len(ids):,}")
print(f"  islands with a bird       {len(islands):,}")
print(f"  photo dates               {sorted({r['PhotoDate'] for r in rows})}")
item = json.load(urllib.request.urlopen(ITEM))
names = [f["name"] for f in item.get("files", [])]
IMG = (".jpg", ".jpeg", ".tif", ".tiff", ".png", ".jp2", ".ecw", ".img", ".zip")
print(f"  files in the release      {len(names)}  {names}")
print(f"  image files in release    {sum(n.lower().endswith(IMG) for n in names)}")

print()
print("RECONCILED SPECIES (Final_Manual_Species_ID)")
sp = collections.Counter(r["Final_Manual_Species_ID"] for r in rows)
for k, v in sp.most_common():
    print(f"  {k:8} {v:7,}  {100 * v / len(rows):5.1f}%")

print()
print("OBSERVERS PER BIRD (Num_Observers_Counted_Raster)")
for k, v in sorted(collections.Counter(r["Num_Observers_Counted_Raster"] for r in rows).items()):
    print(f"  {k:3} observers  {v:7,}")


def species_calls(r):
    return [r[f"Observer_{i}_Species_ID"] for i in (1, 2, 3)
            if r[f"Observer_{i}_Species_ID"] not in ("", "NA")]


print()
print("DID THE OBSERVERS AGREE ON SPECIES? (birds seen by 2+ observers)")
multi = [r for r in rows if len(species_calls(r)) >= 2]
agree = [r for r in multi if len(set(species_calls(r))) == 1]
print(f"  birds with 2+ species calls   {len(multi):,}")
print(f"  all calls identical           {len(agree):,}  ({100 * len(agree) / len(multi):.1f}%)")
print(f"  at least one disagreement     {len(multi) - len(agree):,}  "
      f"({100 * (len(multi) - len(agree)) / len(multi):.1f}%)")
