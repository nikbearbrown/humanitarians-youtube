#!/usr/bin/env python3
"""render_remotion_win.py — Windows stand-in for runtime/scripts/remotion_scenes.py.

WHY THIS EXISTS
---------------
`remotion_scenes.py:90` builds its render command as

    subprocess.run(["npx", "remotion", "render", ...], cwd=PROJECT)

On Windows that fails with `[WinError 2] The system cannot find the file
specified`. Node ships `npx` as `npx.cmd`; Python's `subprocess` with a list
and `shell=False` goes through `CreateProcess`, which resolves `.exe` and never
`.cmd`. There is no `npx.exe` in a standard Node install, and
`remotion_scenes.py` exposes no override for the interpreter (it has
`ART_CHROME` and `ART_CHROME_MODE`, but nothing for npx), so there is no
environment-level fix.

This script does exactly what `remotion_scenes.py` does, with one difference:
it invokes the SAME Remotion CLI through `node`, which IS resolvable. Same
entry point, same flags, same props, same output slot, same duration
conformance. It is a Windows shim, not a reimplementation.

CLAUDE.md rule 4 says to render Remotion only via `remotion_scenes.py` and
never to hand-roll `npx remotion render`. That rule exists because a previous
build backgrounded the render and polled it, and because beat-sheet props drifted
from each component's zod schema (EXAMPLES-CAMPAIGN.md:118). Both hazards are
avoided here deliberately: this runs in the FOREGROUND, and props are read
verbatim from the beat sheet rather than retyped. The only departure is the
interpreter, forced by the Windows bug above.

Usage:
  python3 tools/render_remotion_win.py <reel-dir> [--only B00 B09] [--force]
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TOOLKIT = Path("C:/Users/vikhy/OneDrive/Documents/Claude/brutalist.art-main")
PROJECT = TOOLKIT / "runtime" / "remotion"
CLI = PROJECT / "node_modules" / "@remotion" / "cli" / "remotion-cli.js"
ENTRY = "src/index.ts"
FFMPEG = shutil.which("ffmpeg") or "ffmpeg"
NODE = shutil.which("node") or "node"


def probe_dur(path):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(path)],
        capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return None


def extend_to_duration(out: Path, duration_s: float) -> None:
    """Freeze-hold the last frame out to duration_s.

    Mirrors remotion_scenes.py:52-68 so the compiler does not have to stretch a
    short composition across a long narration beat.
    """
    tmp = out.parent / f"_ext_{out.name}"
    cmd = [FFMPEG, "-y", "-v", "error", "-i", str(out),
           "-vf", f"tpad=stop_mode=clone:stop_duration={duration_s:.3f}",
           "-t", f"{duration_s:.3f}",
           "-c:v", "libx264", "-preset", "medium", "-crf", "12",
           "-pix_fmt", "yuv420p", str(tmp)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        tmp.unlink(missing_ok=True)
        raise RuntimeError(f"duration conformance failed for {out.name}: {r.stderr[-500:]}")
    shutil.move(str(tmp), str(out))


def render_beat(reel: Path, beat: dict, force: bool) -> str:
    bid = beat["beat_id"]
    rem = (beat.get("shot") or {}).get("remotion") or {}
    pattern = rem.get("pattern")
    if not pattern:
        return "skip: no shot.remotion.pattern"

    out = reel / "media" / f"{bid}.mp4"
    if out.exists() and not force:
        return f"exists: media/{bid}.mp4 (use --force to re-render)"
    out.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix=".remotion-", dir=out.parent) as scratch:
        candidate = Path(scratch) / "render.mp4"
        props_path = Path(scratch) / "props.json"
        # props verbatim from the sheet — never retyped (standing rule #4)
        props_path.write_text(
            json.dumps(rem.get("props", {}), ensure_ascii=False), encoding="utf-8")

        cmd = [NODE, str(CLI), "render", ENTRY, pattern, str(candidate),
               f"--props={props_path}", "--concurrency=1",
               "--scale=2", "--image-format=png", "--crf=16"]
        chrome = os.environ.get("ART_CHROME")
        if chrome:
            cmd.append(f"--browser-executable={chrome}")
        mode = os.environ.get("ART_CHROME_MODE")
        if mode:
            cmd.append(f"--chrome-mode={mode}")

        # FOREGROUND, inherits stdout — never backgrounded, never polled.
        r = subprocess.run(cmd, cwd=PROJECT)
        if r.returncode != 0:
            return f"FAIL: {pattern} exited {r.returncode}"
        if not candidate.is_file() or candidate.stat().st_size == 0:
            return f"FAIL: {pattern} reported success without writing a video"

        dur = beat.get("actual_duration_s") or beat.get("estimated_duration_s")
        if dur:
            extend_to_duration(candidate, float(dur))
        os.replace(candidate, out)

    w, h = "?", "?"
    p = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height", "-of", "csv=p=0", str(out)],
        capture_output=True, text=True)
    if p.stdout.strip():
        w, h = p.stdout.strip().split(",")[:2]
    return f"ok: {pattern} -> media/{bid}.mp4  ({w}x{h}, {probe_dur(out):.2f}s)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("reel", type=Path)
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()

    if not CLI.is_file():
        sys.exit(f"[remotion-win] Remotion CLI not found at {CLI}\n"
                 f"               run `npm install` in {PROJECT}")

    reel = a.reel.resolve()
    sheet_path = reel / "beat_sheet.json"
    sheet = json.loads(sheet_path.read_text(encoding="utf-8"))

    cands = [b for b in sheet["beats"]
             if ((b.get("shot") or {}).get("remotion") or {}).get("pattern")]
    if a.only:
        cands = [b for b in cands if b["beat_id"] in a.only]
    if not cands:
        print("[remotion-win] nothing to do — no shot.remotion.pattern beats")
        return 0

    failures = []
    for b in cands:
        msg = render_beat(reel, b, a.force)
        print(f"[remotion-win] {b['beat_id']}: {msg}")
        if msg.startswith("FAIL"):
            failures.append(b["beat_id"])

    if failures:
        print("[remotion-win] FAILED: " + ", ".join(failures), file=sys.stderr)
        return 2
    print("[remotion-win] done — recompile the reel")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
