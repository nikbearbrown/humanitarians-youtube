#!/usr/bin/env python3
"""
pacing_pass.py — add a hold before every cut, then re-concat.

WHY THIS EXISTS
    `compile.py` has no transition or pause mechanism at all: it is a hard-cut
    concat, full stop. Reviewer feedback on the CommBank and Klarna reels was
    that beats cut straight into each other with no room to read the frame.
    The fix that worked is a HOLD — the last frame frozen, with silence — and
    then a clean hard cut. Not a crossfade: a dissolve only softens the cut, it
    doesn't give the viewer time to process (PLAYBOOK §5).

    On both prior reels this was done ad hoc and thrown away, so it had to be
    reinvented each time. This is that pass, kept.

WHAT IT DOES
    For every beat except the last:
        video  = clips/<BID>.mp4  + `hold` seconds of frozen last frame
        audio  = mp3/beat-<BID>.mp3 + silence, padded to the exact video length
    Then concatenates the paced beats and writes <slug>-paced.mp4.

    Audio is padded to the *measured* padded-video duration per beat rather
    than to a computed one, so rounding can't accumulate drift across 14 cuts.

USAGE
    python3 pacing_pass.py <reel-folder> [--hold 1.0] [--out NAME.mp4]

    Re-run this after ANY recompile — compile.py overwrites the unpaced master
    and knows nothing about this pass.
"""
import argparse, json, shutil, subprocess, sys
from pathlib import Path

FFMPEG = shutil.which("ffmpeg") or "ffmpeg"
FFPROBE = shutil.which("ffprobe") or "ffprobe"


def probe_duration(p: Path) -> float:
    r = subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", str(p)], capture_output=True, text=True)
    return float(r.stdout.strip())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("reel", type=Path)
    ap.add_argument("--hold", type=float, default=1.0,
                    help="seconds of frozen last frame before each cut (default 1.0)")
    ap.add_argument("--out", default="", help="output filename (default <slug>-paced.mp4)")
    a = ap.parse_args()

    reel = a.reel.resolve()
    sheet = json.loads((reel / "beat_sheet.json").read_text())
    slug = sheet.get("metadata", {}).get("slug", reel.name)
    out = reel / (a.out or f"{slug}-paced.mp4")

    work = reel / "_paced"
    work.mkdir(exist_ok=True)

    beats = sheet["beats"]
    paced = []
    for i, b in enumerate(beats):
        bid = b["beat_id"]
        clip = reel / "clips" / f"{bid}.mp4"
        mp3 = reel / (b.get("audio_file") or f"mp3/beat-{bid}.mp3")
        if not clip.exists():
            sys.exit(f"[pacing] missing {clip} — run compile.py first")
        if not mp3.exists():
            sys.exit(f"[pacing] missing {mp3} — run generate_audio_kokoro.py first")

        last = (i == len(beats) - 1)
        hold = 0.0 if last else a.hold
        target = probe_duration(clip) + hold
        dst = work / f"{bid}.mp4"

        vf = (f"[0:v]tpad=stop_mode=clone:stop_duration={hold:.3f}[v]"
              if hold > 0 else "[0:v]copy[v]")
        cmd = [FFMPEG, "-y", "-i", str(clip), "-i", str(mp3),
               "-filter_complex", f"{vf};[1:a]apad[a]",
               "-map", "[v]", "-map", "[a]", "-t", f"{target:.3f}",
               "-c:v", "libx264", "-preset", "medium", "-crf", "16",
               "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
               "-movflags", "+faststart", str(dst)]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode != 0:
            sys.exit(f"[pacing] FAILED on {bid}\n{r.stderr[-800:]}")
        print(f"[pacing] {bid:6} {probe_duration(dst):6.2f}s  (+{hold:.1f}s hold)"
              if not last else f"[pacing] {bid:6} {probe_duration(dst):6.2f}s  (last — no hold)")
        paced.append(dst)

    listing = work / "concat.txt"
    listing.write_text("".join(f"file '{p.as_posix()}'\n" for p in paced))
    cmd = [FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", str(listing),
           "-c", "copy", "-movflags", "+faststart", str(out)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"[pacing] concat FAILED\n{r.stderr[-800:]}")

    total = probe_duration(out)
    print(f"[pacing] wrote {out}  ({total:.1f}s, {len(beats)} beats, "
          f"{len(beats)-1} holds of {a.hold:.1f}s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
