# -*- coding: utf-8 -*-
"""Derive the native-portrait 9:16 cut from the signed 16:9 beat sheet.

THIS IS NOT A CROP. Every beat is re-rendered from a portrait composition whose
component REFLOWS its layout (the scenes branch on `height > width`), so the
9:16 master is a first-class layout, not a centre-cut of the widescreen one.
That is why this script exists instead of `runtime/scripts/shorts.py`:

  * shorts.py builds a DERIVATIVE cut — it may drop beats to fit the 3:00
    Shorts cap, rewrites the outro to point at the parent long, and appends a
    silent endcard. None of that is wanted here: the brief asked for a full
    9:16 version of the same video, beat for beat.
  * shorts.py links its audio with POSIX symlinks, which need elevation or
    Developer Mode on Windows. This copies instead.

What it does:
  1. every `shot.remotion.pattern` -> `<pattern>916` (asserting the portrait
     composition is actually registered in Root.tsx, so a missing one is a
     hard error rather than a silent centre-cut),
  2. metadata.aspect_ratio -> "9:16",
  3. the measured mp3s are COPIED into 916/mp3/ — audio is identical between
     the two cuts, because audio is the master clock for both.

Rerunnable: safe to run again after the parent sheet changes.
"""
import json
import pathlib
import shutil

HERE = pathlib.Path(__file__).resolve().parent
ROOT_TSX = (HERE.parents[2] / "brutalist.art" / "runtime" / "remotion" / "src" / "Root.tsx")

parent = json.loads((HERE / "beat_sheet.json").read_text(encoding="utf-8"))
tsx = ROOT_TSX.read_text(encoding="utf-8")

out_dir = HERE / "916"
(out_dir / "mp3").mkdir(parents=True, exist_ok=True)
(out_dir / "media").mkdir(parents=True, exist_ok=True)

meta = dict(parent["metadata"])
meta.update({
    "slug": meta["slug"] + "-916",
    "aspect_ratio": "9:16",
    "kind": "vertical-master",
    "derived_from": parent["metadata"]["slug"],
    "reformat": ("NATIVE PORTRAIT — every beat re-rendered from a <pattern>916 "
                 "composition whose component reflows for the taller frame. No "
                 "centre-cutting, no scaling of the 16:9 render. Portrait type is "
                 "LARGER than landscape type, not smaller."),
    "aspect_pair": "../beat_sheet.json is the 16:9 sibling cut",
})
meta.pop("build", None)

beats = json.loads(json.dumps(parent["beats"]))   # deep copy
missing = []
for b in beats:
    b.pop("build", None)
    rem = (b.get("shot") or {}).get("remotion")
    if not rem:
        continue
    pattern = rem["pattern"]
    p916 = pattern if pattern.endswith("916") else pattern + "916"
    if f'id="{p916}"' not in tsx:
        missing.append((b["beat_id"], pattern))
        continue
    rem["pattern"] = p916
    rem.pop("rendered", None)

    # copy the measured narration across — same clock, both cuts
    src = HERE / (b.get("audio_file") or f"mp3/beat-{b['beat_id']}.mp3")
    dst = out_dir / "mp3" / src.name
    if src.exists():
        shutil.copyfile(src, dst)

if missing:
    raise SystemExit(
        "REFUSED — no portrait composition registered for:\n" +
        "\n".join(f"  {bid}: needs {pat}916 in Root.tsx" for bid, pat in missing))

(out_dir / "beat_sheet.json").write_text(
    json.dumps({"metadata": meta, "beats": beats}, indent=1, ensure_ascii=False),
    encoding="utf-8")

total = sum(b["actual_duration_s"] for b in beats)
print(f"916/beat_sheet.json — {len(beats)} beats · {total:.2f}s "
      f"({int(total // 60)}:{total % 60:05.2f}) · aspect 9:16")
for b in beats:
    print("  %s  %-26s %5.2fs" % (b["beat_id"],
                                  (b.get("shot", {}).get("remotion") or {}).get("pattern", "-"),
                                  b["actual_duration_s"]))
