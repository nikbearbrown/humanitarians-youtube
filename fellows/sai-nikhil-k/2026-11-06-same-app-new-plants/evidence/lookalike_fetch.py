#!/usr/bin/env python3
"""lookalike_fetch.py — native North American plants that look like Vegnet's four invasives.

Gavia's ROADMAP (v0.5.0) says Vegnet still needs "the native plants they're
confused with". This fetches a fixed sample of research-grade iNaturalist
photos of natives commonly mistaken for each target, so Gavia's own detector
can be asked about them (lookalike_check.rs):

    purple loosestrife  <- fireweed (Chamaenerion angustifolium),
                           blue vervain (Verbena hastata)
    common reed         <- native American reed (Phragmites australis americanus)
    yellow flag iris    <- blue flag iris (Iris versicolor)
    water chestnut      <- watershield (Brasenia schreberi)

Only photos licensed CC0, CC BY or CC BY-SA. Reproducible: observations in
North America (place 97394), research grade, newest first below a fixed id,
the first photo of each, N per taxon. Every photo gets a sidecar with author,
licence and observation URL.

Run:  python3 lookalike_fetch.py <out_dir> [--n 8]
"""
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ID_BELOW = 330_000_000          # fixes the sample: observations created before ~Nov 2025
PLACE = 97394                   # North America
UA = {"User-Agent": "brutalist-art-evidence/1.0 (reproducible look-alike sample)"}
TAXA = [
    ("fireweed", "Chamaenerion angustifolium", "purple loosestrife"),
    ("blue_vervain", "Verbena hastata", "purple loosestrife"),
    ("native_reed", "Phragmites australis americanus", "common reed"),
    ("blue_flag_iris", "Iris versicolor", "yellow flag iris"),
    ("watershield", "Brasenia schreberi", "water chestnut"),
]
OK = {"cc0", "cc-by", "cc-by-sa"}


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def main():
    out = Path(sys.argv[1]).resolve()
    n = int(sys.argv[sys.argv.index("--n") + 1]) if "--n" in sys.argv else 8
    manifest = []
    for slug, name, mimics in TAXA:
        q = urllib.parse.urlencode({
            "taxon_name": name, "quality_grade": "research", "place_id": PLACE,
            "photo_license": ",".join(sorted(OK)), "id_below": ID_BELOW,
            "order_by": "id", "order": "desc", "per_page": 30})
        data = json.loads(get(f"https://api.inaturalist.org/v1/observations?{q}"))
        time.sleep(1.2)
        got = 0
        (out / slug).mkdir(parents=True, exist_ok=True)
        for obs in data["results"]:
            if got == n:
                break
            if obs["taxon"]["name"] != name:
                continue
            ph = next((p for p in obs.get("photos", []) if (p.get("license_code") or "") in OK), None)
            if not ph:
                continue
            url = ph["url"].replace("square", "large")
            dest = out / slug / f"{slug}_{ph['id']}.jpg"
            if not dest.exists():
                dest.write_bytes(get(url))
                time.sleep(0.4)
            side = {"species": name, "mimics": mimics, "observation": obs["uri"],
                    "photo_id": ph["id"], "license": ph["license_code"],
                    "attribution": ph["attribution"], "observed_on": obs.get("observed_on"),
                    "place": obs.get("place_guess"), "url": url}
            dest.with_suffix(".json").write_text(json.dumps(side, indent=2) + "\n")
            manifest.append({"file": f"{slug}/{dest.name}", **side})
            got += 1
        print(f"{slug:15s} {name:34s} mimics {mimics:20s} {got} photos")
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"{len(manifest)} photos -> {out}")


if __name__ == "__main__":
    main()
