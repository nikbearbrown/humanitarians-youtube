#!/usr/bin/env python3
"""PROOF on the FINAL file: one frame per timed claim, taken at (beat start in the paced timeline + cue
+ 0.7 s), so 'on screen when said' is checked on what ships, not on stills. B10 also at 15/50/85%
(MATH-TYPESETTING.md). Beat starts come from the compiled clips' own durations plus each 0.3 s hold."""
import json, subprocess, sys
from pathlib import Path

HOLD = 0.3


def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                                capture_output=True, text=True).stdout)


def run(reel, final, out):
    reel = Path(reel); out = Path(out); out.mkdir(parents=True, exist_ok=True)
    sheet = json.loads((reel / "beat_sheet.json").read_text())
    t0, jobs = 0.0, []
    for i, b in enumerate(sheet["beats"]):
        bid = b["beat_id"]; d = dur(reel / "clips" / f"{bid}.mp4")
        p = b["shot"]["remotion"]["props"]
        cues = [("caption", p.get("captionAt")), ("walk", p.get("walkAt")), ("peak", p.get("peakAt") if p.get("showPeak") else None)]
        cues += [(f"marker:{m['label']}", m.get("at")) for m in p.get("markers", [])]
        cues += [(f"strip:{m['label']}", m.get("at")) for m in (p.get("scoreline") or {}).get("markers", [])]
        cues += [(f"row:{o['label'][:24]}", o.get("at")) for o in p.get("outcomes", [])]
        cues = [(n, t) for n, t in cues if isinstance(t, (int, float))]
        if not cues:
            cues = [("settled", d * 0.85)]
        if bid == "B10":
            cues += [(f"eq{int(f*100)}", d * f) for f in (0.15, 0.5, 0.85)]
        for n, t in cues:
            tt = min(t + 0.7, d - 0.05) if not n.startswith(("eq", "settled")) else t
            jobs.append((bid, n, round(t0 + tt, 2)))
        t0 += d + (HOLD if i < len(sheet["beats"]) - 1 else 0)
    for k, (bid, n, t) in enumerate(jobs):
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t}", "-i", final, "-frames:v", "1",
                        "-vf", "scale=-2:540", str(out / f"{k:03d}-{bid}.png")], check=True)
    (out / "index.json").write_text(json.dumps(jobs, indent=1))
    print(f"{len(jobs)} assertion frames from {final} (timeline {t0:.1f}s)")


if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2], sys.argv[3])
