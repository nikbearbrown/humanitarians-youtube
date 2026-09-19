#!/usr/bin/env python3
"""
make_vertical.py — derive the 9:16 companion reel from the 16:9 beat sheet.

The vertical cut is a RE-LAYOUT, not a crop. Every beat is re-rendered from a portrait
composition (`<pattern>916`), so nothing is cut off the sides and no type is squeezed.
The narration is NOT regenerated: the same mp3s are copied across, so both masters are
literally the same edit and no number can differ between them.

What changes between the two sheets:
  - metadata.aspect_ratio  16:9 -> 9:16   (compile.py reads this to size the canvas)
  - metadata.slug          gains a -916 suffix so the two masters never collide
  - shot.remotion.pattern  <pattern> -> <pattern>916
Everything else — narration, props, measured durations — is copied byte for byte.

Every pattern used here MUST have a 916 registration in Root.tsx; this script refuses
rather than silently falling back to a landscape render.

Usage:  python make_vertical.py
Then:   python3 runtime/scripts/remotion_scenes.py <reel>/vertical
        ./art final <reel>/vertical --height 3840
"""
import json, re, shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLKIT = Path("E:/NEU/Jobs/Humanitarians_AI/brutalist.art")
ROOT_TSX = TOOLKIT / "runtime" / "remotion" / "src" / "Root.tsx"

VERT = HERE / "vertical"
VERT.mkdir(exist_ok=True)

sheet = json.loads((HERE / "beat_sheet.json").read_text(encoding="utf-8"))

# ── every portrait composition must actually be registered ────────────────────
registry = ROOT_TSX.read_text(encoding="utf-8")
explicit = set(re.findall(r'<Composition\s+id="([A-Za-z0-9]+)"', registry))
# the reel-local folders register their portrait ids as `id + '916'` over a list
generated = {f"{m}916" for m in re.findall(r"\['(W\d[A-Za-z]+)',", registry)}
known = explicit | generated

missing = []
for b in sheet["beats"]:
    rem = (b.get("shot") or {}).get("remotion")
    if not rem:
        continue
    p916 = f"{rem['pattern']}916"
    if p916 not in known:
        missing.append((b["beat_id"], rem["pattern"], p916))

if missing:
    for bid, pat, want in missing:
        print(f"[vertical] {bid}: no portrait composition {want} for {pat}")
    sys.exit("[vertical] REFUSED — add the 916 compositions to Root.tsx. "
             "A landscape render centre-cut into a portrait frame is not a vertical cut.")

# ── rewire ────────────────────────────────────────────────────────────────────
meta = sheet["metadata"]
meta["aspect_ratio"] = "9:16"
meta["slug"] = meta["slug"] + "-916"
meta["companion_landscape"] = "../ — the 16:9 master, same audio, same props, same edit"
meta["note"] = meta["note"] + (
    " VERTICAL CUT: every beat re-renders from a <pattern>916 portrait composition — a "
    "re-layout, never a crop. The narration mp3s are copied from the 16:9 reel, not "
    "regenerated, so the two masters are the same edit."
)

for b in sheet["beats"]:
    rem = (b.get("shot") or {}).get("remotion")
    if rem:
        rem["pattern"] = f"{rem['pattern']}916"
        rem.pop("rendered", None)
    b.pop("build", None)

(VERT / "beat_sheet.json").write_text(
    json.dumps(sheet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# ── the SAME audio, copied not regenerated ────────────────────────────────────
src_mp3, dst_mp3 = HERE / "mp3", VERT / "mp3"
dst_mp3.mkdir(exist_ok=True)
n = 0
for f in sorted(src_mp3.glob("*.mp3")):
    shutil.copy2(f, dst_mp3 / f.name)
    n += 1

print(f"[vertical] wrote {VERT / 'beat_sheet.json'}")
print(f"[vertical] {len(sheet['beats'])} beats rewired to portrait compositions")
print(f"[vertical] {n} narration mp3(s) copied — audio is NOT regenerated")
