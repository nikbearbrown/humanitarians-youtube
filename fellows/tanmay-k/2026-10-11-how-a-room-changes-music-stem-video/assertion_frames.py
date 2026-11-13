#!/usr/bin/env python3
"""PROOF on the FINAL files: frames taken from the compiled masters at the moment each claim is SAID.

For every beat, frames at:
  - each timed reveal (activeAt, captionAt, drySideAt, statAt, answersAt) + 0.7 s
  - each quote / figure the narration states (proof_check.py's QUOTES and NUMBERS phrases), at the
    moment cue_align.spoken_at says the phrase begins, + 0.7 s
  - 85% of the beat (steady state)
Beat starts come from the paced clips' own durations (_paced/<ID>.mp4), so the per-beat holds
(B18, B19) are counted exactly. (W26 version of W25's assertion_frames.py.)

  python3 assertion_frames.py <reel-dir> <final.mp4> <out-dir>
"""
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from cue_align import spoken_at          # noqa: E402

TIMED = ("activeAt", "captionAt", "drySideAt", "statAt", "answersAt")


def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of",
                                 "csv=p=0", str(p)], capture_output=True, text=True).stdout)


def claim_phrases():
    src = (HERE / "proof_check.py").read_text()
    ns = {}
    start = src.index("QUOTES = {")
    end = src.index("TIMED = (")
    exec(src[start:end], ns)          # just the two tables (QUOTES, NUMBERS + the Short's updates)
    out = {}
    for bid, qs in ns["QUOTES"].items():
        out.setdefault(bid, []).extend(("quote", q) for q in qs)
    for bid, pairs in ns["NUMBERS"].items():
        out.setdefault(bid, []).extend(("figure", spoken) for spoken, _ in pairs)
    return out


def main(reel, final, outdir):
    reel, out = Path(reel), Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    sheet = json.loads((reel / "beat_sheet.json").read_text())
    phrases = claim_phrases()
    t0, jobs = 0.0, []
    for b in sheet["beats"]:
        bid, text = b["beat_id"], b["narration_text"]
        d = dur(reel / "_paced" / f"{bid}.mp4")
        p = b["shot"]["remotion"]["props"]
        marks = [(k, p[k]) for k in TIMED if isinstance(p.get(k), (int, float))]
        mp3 = reel / "mp3" / f"beat-{bid}.mp3"
        for kind, ph in phrases.get(bid, []):
            hit = next((c for c in (ph, ph.capitalize()) if c in text), None)
            if hit:
                marks.append((f"{kind}:{ph[:24]}", spoken_at(text, str(mp3), hit)))
        marks.append(("steady85", 0.85 * b.get("actual_duration_s", b["estimated_duration_s"])))
        for tag, t in marks:
            at = min(t0 + t + (0.7 if tag != "steady85" else 0), t0 + d - 0.05)
            safe = "".join(c if c.isalnum() else "-" for c in tag)[:30]
            jobs.append((bid, tag, round(at, 2), out / f"{bid}__{safe}.png"))
        t0 += d
    for bid, tag, at, f in jobs:
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{at}", "-i", str(final), "-frames:v", "1",
                        "-vf", "scale='if(gt(iw,ih),1920,1080)':-2", str(f)], check=True)
    (out / "index.json").write_text(json.dumps([{"beat": b, "tag": t, "at_s": a, "file": f.name}
                                                for b, t, a, f in jobs], indent=1))
    print(f"{len(jobs)} frames from {Path(final).name} → {out}  (timeline {t0:.1f}s vs file {dur(final):.1f}s)")


if __name__ == "__main__":
    main(*sys.argv[1:4])
