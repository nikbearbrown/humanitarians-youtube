#!/usr/bin/env python3
"""make_916.py — derive the FULL-LENGTH 9:16 cut of this reel.

WHY NOT `./art shorts`?

`shorts.py` builds a *Short*: it enforces YouTube's hard 3:00 cap by dropping
the longest unprotected beats and rewriting the outro to point at the long. It
also wires the derived folder together with symlinks. Neither fits here:

  1. The ask was for the SAME video in both aspect ratios, not a trimmed
     teaser. This reel measures 2:06 — `shorts.py` would silently drop a body
     beat to get under the cap, so the 9:16 viewer would lose an argument the
     16:9 viewer gets.
  2. Symlink creation on Windows needs Developer Mode or an elevated shell.
     Real copies cost a few MB of mp3 and always work.

So this does the one thing that IS shared with shorts.py — its ONDA CHECK,
the rule that a Remotion beat is never center-cropped but re-rendered from a
portrait composition registered as `<pattern>916` — and skips the cutting.
Every beat survives; only the geometry changes.

What it writes into ./916:
  beat_sheet.json   same beats, aspect_ratio 9:16, every pattern → <pattern>916
  mp3/              copies of the parent's narration (audio is NOT regenerated:
                    same script, same voice, same clock — that is the whole
                    point of a derivative cut)
  scenes.py         the same "no Manim here" stub
  media/            left empty on purpose, so remotion_scenes.py renders each
                    beat portrait rather than reusing a 16:9 render

Any pattern with no registered `<pattern>916` is reported and the run exits
non-zero — that is the ONDA CHECK failing loudly instead of shipping a cut
with a chopped-off beat.

    python3 make_916.py [--force]
"""
import argparse
import json
import re
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT_TSX = (HERE.parents[2] / "brutalist.art" / "runtime" / "remotion"
            / "src" / "Root.tsx")


def registered(tsx: str, comp_id: str) -> bool:
    """True if Root.tsx registers a composition under exactly this id."""
    return re.search(rf'id="{re.escape(comp_id)}"', tsx) is not None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true",
                    help="overwrite an existing 916/beat_sheet.json and re-copy mp3s")
    a = ap.parse_args()

    sheet = json.loads((HERE / "beat_sheet.json").read_text(encoding="utf-8"))
    tsx = ROOT_TSX.read_text(encoding="utf-8")

    out = HERE / "916"
    for sub in ("media", "manim", "mp3", "pantry", "images", "mp4"):
        (out / sub).mkdir(parents=True, exist_ok=True)

    # ── the ONDA CHECK ────────────────────────────────────────────────────
    blocked = []
    for beat in sheet["beats"]:
        rem = (beat.get("shot") or {}).get("remotion") or {}
        pattern = rem.get("pattern")
        if not pattern:
            continue
        p916 = f"{pattern}916"
        if not registered(tsx, p916):
            blocked.append((beat["beat_id"], pattern))
            continue
        rem["pattern"] = p916
        rem["rendered"] = {"out": f"media/{beat['beat_id']}.mp4", "at": ""}

    if blocked:
        print("[916] ONDA CHECK FAILED — no portrait composition for:")
        for bid, pat in blocked:
            print(f"[916]   {bid}: needs `{pat}916` registered in Root.tsx")
        print("[916] Nothing written. Add the compositions, then re-run.")
        return 2

    # ── metadata: same reel, different geometry ───────────────────────────
    meta = sheet["metadata"]
    meta["aspect_ratio"] = "9:16"
    meta["fit"] = "contain"
    meta["slug"] = f"{meta['slug']}-916"
    meta["derived_from"] = "data-contract-simulation"
    meta["kind"] = "vertical-full"
    meta["note"] = (
        "FULL-LENGTH 9:16 derivative of data-contract-simulation — every beat kept, no "
        "outro rewrite. Patterns rewired to their 916 compositions per the ONDA "
        "CHECK (a Remotion beat is re-rendered portrait, never center-cropped). "
        "Narration is the parent's, byte for byte. Longer than the 3:00 Shorts "
        "cap by design: this is the vertical cut of the video, not a Short. "
        + meta.get("note", ""))

    target = out / "beat_sheet.json"
    if target.exists() and not a.force:
        print(f"[916] {target.relative_to(HERE)} exists — pass --force to overwrite")
    else:
        tmp = target.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(sheet, indent=1, ensure_ascii=False), encoding="utf-8")
        tmp.replace(target)
        print(f"[916] wrote {target.relative_to(HERE)} "
              f"({len(sheet['beats'])} beats, all kept)")

    # ── narration: copied, never regenerated ──────────────────────────────
    copied = 0
    for mp3 in sorted((HERE / "mp3").glob("*.mp3")):
        dst = out / "mp3" / mp3.name
        if a.force or not dst.exists():
            shutil.copy2(mp3, dst)
            copied += 1
    timings = HERE / "mp3" / "timings.json"
    if timings.exists():
        shutil.copy2(timings, out / "mp3" / "timings.json")
    print(f"[916] copied {copied} narration file(s) — audio is NOT regenerated")

    # the Manim guard stub travels too, for the same reason it exists upstream
    stub = HERE / "scenes.py"
    if stub.exists():
        shutil.copy2(stub, out / "scenes.py")

    # GATE P is inherited: same script, same pedagogy review
    ped = HERE / "PEDAGOGY.md"
    if ped.exists():
        shutil.copy2(ped, out / "PEDAGOGY.md")

    total = sum(float(b.get("actual_duration_s") or 0) for b in sheet["beats"])
    print(f"[916] ready · {total:.1f}s ({int(total // 60)}:{total % 60:04.1f})")
    print("[916] next:")
    print("[916]   1. python3 sync_durations.py 916")
    print("[916]   2. python3 <toolkit>/runtime/scripts/remotion_scenes.py <reel>/916")
    print("[916]   3. python3 <toolkit>/runtime/scripts/compile.py <reel>/916 --height 3840")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
