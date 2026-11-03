#!/usr/bin/env python3
"""qc_frames.py — pull the frames a human (or a model) actually LOOKS at.

VISUAL QC LAW: the mp4 probe is a file check and never counts as QC. This
samples each beat at ~15 / 50 / 85% of its own span — the three moments that
catch the three common failure shapes:

    15%  something enters wrong (offscreen anchor, clipped entry)
    50%  the steady state (collision, overflow, illegible type)
    85%  the payoff lands wrong (a counter still at 0, a reveal that never came)

Sampling from the beat sheet's measured durations rather than at a flat fps is
what makes the frames comparable across beats and across the two aspect ratios.

    python3 qc_frames.py <reel_dir> [--mp4 path] [--out _qc/beats]
"""
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

FFMPEG = shutil.which("ffmpeg") or "ffmpeg"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("reel", type=Path)
    ap.add_argument("--mp4", type=Path, default=None)
    ap.add_argument("--out", default="_qc/beats")
    ap.add_argument("--at", nargs="*", type=float, default=[0.15, 0.50, 0.85])
    a = ap.parse_args()

    reel = a.reel.resolve()
    sheet = json.loads((reel / "beat_sheet.json").read_text(encoding="utf-8"))
    slug = sheet["metadata"]["slug"]

    mp4 = a.mp4
    if mp4 is None:
        for cand in (reel / f"{slug}.mp4", reel / f"{slug}-slate.mp4"):
            if cand.exists():
                mp4 = cand
                break
    if mp4 is None or not Path(mp4).exists():
        sys.exit(f"[qc] no compiled mp4 found in {reel} — compile first")

    out = reel / a.out
    out.mkdir(parents=True, exist_ok=True)

    t0 = 0.0
    made = []
    for beat in sheet["beats"]:
        bid = beat["beat_id"]
        dur = float(beat.get("actual_duration_s")
                    or beat.get("estimated_duration_s") or 6.0)
        for frac in a.at:
            # clamp inside the beat so a seek never lands on the neighbour's
            # first frame (an off-by-one here reads as a phantom defect)
            ts = t0 + min(max(dur * frac, 0.05), dur - 0.05)
            png = out / f"{bid}-{int(frac * 100):02d}.png"
            subprocess.run([FFMPEG, "-y", "-v", "error", "-ss", f"{ts:.3f}",
                            "-i", str(mp4), "-frames:v", "1", str(png)],
                           check=True)
            made.append(png.name)
        t0 += dur

    print(f"[qc] {len(made)} frames → {out}")
    print(f"[qc] source: {Path(mp4).name} · {t0:.1f}s across {len(sheet['beats'])} beats")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
