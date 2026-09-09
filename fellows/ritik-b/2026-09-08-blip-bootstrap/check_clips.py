#!/usr/bin/env python3
"""check_clips.py — assert every rendered clip is the length its beat asked for.

WHY THIS EXISTS: GATE V reads frames, so it cannot see a clip that is the wrong LENGTH —
every frame of a too-long clip is perfectly legible. On this build, one beat's clip survived
a crashed extend step at the composition's full 30.06s instead of the beat's 11.88s, and
`compile.py` rescued it by centre-cutting: it kept the middle 11.9s and threw away the
front-loaded typing animation. The frames were fine. The beat was gutted.

`remotion_scenes.py`'s retry logic checks whether a clip EXISTS, not whether it is right, so
"filled already (skip)" is not the same as "correct". Run this after any render pass, and
especially after any pass that crashed part-way.

Usage:  python3 check_clips.py [reel_dir ...]      (defaults to both cuts of this reel)
Exit:   1 if any clip is missing or off by more than the tolerance.
"""
import json, os, subprocess, sys
from pathlib import Path

FFPROBE = "/opt/homebrew/bin/ffprobe" if Path("/opt/homebrew/bin/ffprobe").exists() else "ffprobe"
TOL_S = 0.6   # generous: extend/conform round to frame boundaries


def probe(path: Path) -> float:
    r = subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", str(path)], capture_output=True, text=True)
    return float(r.stdout.strip())


def check(folder: Path) -> int:
    sheet = json.loads((folder / "beat_sheet.json").read_text())
    bad = 0
    for b in sheet["beats"]:
        bid = b["beat_id"]
        want = b.get("actual_duration_s") or b.get("estimated_duration_s")
        for kind in ("media", "clips"):
            f = folder / kind / f"{bid}.mp4"
            if not f.exists():
                if kind == "media":
                    print(f"  {bid} {kind}: MISSING")
                    bad += 1
                continue
            got = probe(f)
            if abs(got - float(want)) > TOL_S:
                why = ("clip is LONGER — compile.py will centre-cut it and drop a "
                       "front-loaded animation" if got > float(want) else
                       "clip is SHORTER — compile.py will stretch it into slow motion")
                print(f"  {bid} {kind}: {got:.2f}s but the beat is {float(want):.2f}s  ({why})")
                bad += 1
    print(f"{folder.name}: {'all clips match their beats ✓' if not bad else f'{bad} mismatch(es)'}")
    return bad


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    targets = [Path(a) for a in sys.argv[1:]] or [here, here.parent / "blip-bootstrap-916"]
    sys.exit(1 if sum(check(t) for t in targets) else 0)
