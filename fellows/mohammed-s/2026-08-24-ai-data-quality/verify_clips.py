#!/usr/bin/env python3
"""verify_clips.py — prove every rendered clip is the length its beat expects.

WHY THIS EXISTS — the silent-wrong-length failure

`remotion_scenes.render_beat()` finishes each beat by calling
`extend_clip_to_duration()`, which writes `media/_ext_<BID>.mp4` and then MOVES
it over `media/<BID>.mp4`. Between those two steps the slot holds the RAW
composition render — full composition length, not the beat length.

Kill a render in that window (Ctrl-C, a taskkill, an OOM) and you are left with
a wrong-length clip sitting in the slot, plus an orphaned `_ext_` file. The
trap is what happens next: `render_beat()` skips any beat whose output already
exists, so a re-run does NOT repair it. The wrong-length clip then flows
straight into `compile.py`, which center-cuts anything longer than its beat —
so the beat loses its opening AND its payoff, symmetrically, and the cut still
looks superficially fine. Nothing in the pipeline flags it.

The mp4 probe is not visual QC, but it is exactly the right tool for THIS
class of defect, which no amount of looking at frames would catch.

Run it after any interrupted render, and always before compiling:

    python3 verify_clips.py            # both lanes
    python3 verify_clips.py --fix      # delete the bad clips so they re-render

Exit 0 clean, 1 if anything is wrong.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOLERANCE_S = 0.15   # generous: ffmpeg rounds to a frame boundary


def probe(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(path)],
        capture_output=True, text=True)
    try:
        return float(out.stdout.strip())
    except ValueError:
        return -1.0


def check(folder: Path, fix: bool) -> tuple[int, int, int]:
    sheet_path = folder / "beat_sheet.json"
    if not sheet_path.exists():
        return 0, 0, 0
    sheet = json.loads(sheet_path.read_text(encoding="utf-8"))
    label = sheet["metadata"].get("slug", folder.name)
    print(f"\n[verify] {label}")

    orphans = sorted((folder / "media").glob("_ext_*.mp4"))
    for o in orphans:
        print(f"[verify]   ORPHAN {o.name} — a render died mid-move")
        if fix:
            o.unlink()
            print(f"[verify]     deleted {o.name}")

    ok = bad = missing = 0
    for beat in sheet["beats"]:
        bid = beat["beat_id"]
        clip = folder / "media" / f"{bid}.mp4"
        want = float(beat.get("actual_duration_s") or 0)
        if not clip.exists():
            missing += 1
            continue
        got = probe(clip)
        if got < 0:
            print(f"[verify]   {bid}  UNREADABLE — truncated mp4")
            bad += 1
            if fix:
                clip.unlink()
            continue
        if abs(got - want) > TOLERANCE_S:
            print(f"[verify]   {bid}  WRONG LENGTH  clip={got:.2f}s "
                  f"beat={want:.2f}s  (raw composition left in the slot)")
            bad += 1
            if fix:
                clip.unlink()
                print(f"[verify]     deleted {bid}.mp4 — it will re-render")
        else:
            ok += 1
    print(f"[verify]   {ok} ok · {bad} bad · {missing} not yet rendered"
          + (f" · {len(orphans)} orphan(s)" if orphans else ""))
    return ok, bad, missing


def check_masters(fix: bool) -> int:
    """The COMPILED masters, not just the beat clips.

    Same failure, one level up: a compile killed during the final mux leaves a
    plausible-looking mp4 with no moov atom. `ls` shows a file, the build log
    shows a "wrote ..." line from the previous successful run, and nothing
    downstream complains — but the deliverable is garbage. This happened twice
    on this reel, so the masters get probed explicitly and their duration is
    reconciled against the sum of the beat durations.
    """
    print()
    print("[verify] compiled masters")
    bad = 0
    for folder, name in ((HERE, "ai-data-quality.mp4"),
                         (HERE / "916", "ai-data-quality-916.mp4")):
        sheet_path = folder / "beat_sheet.json"
        mp4 = folder / name
        if not sheet_path.exists():
            continue
        if not mp4.exists():
            print(f"[verify]   {name}  NOT BUILT")
            continue
        sheet = json.loads(sheet_path.read_text(encoding="utf-8"))
        want = sum(float(b.get("actual_duration_s") or 0) for b in sheet["beats"])
        got = probe(mp4)
        if got < 0:
            print(f"[verify]   {name}  CORRUPT — no moov atom (compile died mid-mux)")
            bad += 1
            if fix:
                mp4.unlink()
                print(f"[verify]     deleted {name} — recompile it")
            continue
        if abs(got - want) > 0.5:
            print(f"[verify]   {name}  WRONG LENGTH  {got:.2f}s vs expected {want:.2f}s")
            bad += 1
        else:
            print(f"[verify]   {name}  OK  {got:.2f}s")
    return bad


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true",
                    help="delete bad clips and orphans so the next render pass rebuilds them")
    a = ap.parse_args()

    total_bad = total_missing = 0
    for folder in (HERE, HERE / "916"):
        _, bad, missing = check(folder, a.fix)
        total_bad += bad
        total_missing += missing
    total_bad += check_masters(a.fix)

    print()
    if total_bad:
        print(f"[verify] {total_bad} artefact(s) are bad — "
              f"re-run with --fix, then re-render before compiling.")
        return 1
    if total_missing:
        print(f"[verify] all rendered clips are correct; "
              f"{total_missing} beat(s) still to render.")
        return 0
    print("[verify] every clip matches its beat. Safe to compile.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
