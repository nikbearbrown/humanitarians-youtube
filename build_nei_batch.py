#!/usr/bin/env python3
"""
NEI Batch builder — 30 claude-liam explainer reels for @HumanitariansAI.
Usage: python3 humanitarians_html/youtube/build_nei_batch.py [--start C01] [--end C30]
Run from: books/
"""
import subprocess, sys, json, os, re
from pathlib import Path
from datetime import datetime

BOOKS = Path(__file__).parent.parent.parent  # books/
ART   = BOOKS / "brutalist-art"
KOKORO = ART / "runtime/scripts/generate_audio_kokoro.py"
REMOTION_PY = ART / "runtime/scripts/remotion_scenes.py"
COMPILE_PY  = ART / "runtime/scripts/compile.py"
OUT_BASE = Path(__file__).parent  # humanitarians_html/youtube/
LOG_FILE = OUT_BASE / "NEI-BATCH-LOG.md"

SLUGS = [
    "claude-liam-spotify-recommender",    # C01
    "claude-liam-coop-vs-internship",     # C02
    "claude-liam-gps-fingerprint",        # C03
    "claude-liam-multi-model-sync",       # C04
    "claude-liam-ai-speed-paradox",       # C05
    "claude-liam-llm-sycophancy",         # C06
    "claude-liam-hub-tax-graph-ai",       # C07
    "claude-liam-ai-hiring-bias",         # C08
    "claude-liam-tinyml-chasm",           # C09
    "claude-liam-ai-five-things",         # C10
    "claude-liam-digital-twin-authority", # C11
    "claude-liam-token-cost-economics",   # C12
    "claude-liam-pipeline-bias",          # C13
    "claude-liam-firmware-accountability",# C14
    "claude-liam-engineering-education-gap", # C15
    "claude-liam-arm-business-model",     # C16
    "claude-liam-edge-ai-50-dollar",      # C17
    "claude-liam-factory-predictive-asymmetry", # C18
    "claude-liam-smart-building-waste",   # C19
    "claude-liam-vada-pav-ppp",           # C20
    "claude-liam-ai-research-tools-fail", # C21
    "claude-liam-edge-ai-latency",        # C22
    "claude-liam-peer-review-decoded",    # C23
    "claude-liam-counting-cars-state-machine", # C24
    "claude-liam-ai-dual-use",            # C25
    "claude-liam-spotify-contamination-window", # C26
    "claude-liam-education-mismatch",     # C27
    "claude-liam-physical-world-not-software",  # C28
    "claude-liam-anomaly-detection-factory",    # C29
    "claude-liam-body-in-loop",           # C30
]

def run(cmd, cwd=None, timeout=600):
    """Run a command, return (returncode, stdout, stderr)."""
    result = subprocess.run(
        cmd, shell=True, capture_output=True, text=True,
        cwd=cwd or BOOKS, timeout=timeout
    )
    return result.returncode, result.stdout, result.stderr

def probe_mp4(mp4_path):
    """Return duration string if valid 1080p mp4, else None."""
    rc, out, err = run(
        f'ffprobe -v quiet -select_streams v:0 '
        f'-show_entries stream=width,height,duration '
        f'-of default=noprint_wrappers=1 "{mp4_path}"'
    )
    if rc != 0:
        return None
    height = None
    duration = None
    for line in out.splitlines():
        if line.startswith("height="):
            height = int(line.split("=")[1])
        if line.startswith("duration="):
            try:
                duration = float(line.split("=")[1])
            except ValueError:
                pass
    if height and height >= 1080 and duration:
        mins = int(duration // 60)
        secs = int(duration % 60)
        return f"{mins}:{secs:02d}"
    return None

def log_row(slug, status, duration="—", notes=""):
    """Append a row to the batch log."""
    row = f"| {slug} | {status} | {duration} | {notes} |\n"
    with open(LOG_FILE, "a") as f:
        f.write(row)
    print(row.strip())

def build_slug(slug):
    reel = OUT_BASE / slug
    # compile.py writes the master to <reel>/<slug>.mp4 (reel root, not mp4/ subdir)
    mp4  = reel / f"{slug}.mp4"

    # Idempotent: skip if valid 1080p mp4 already exists
    if mp4.exists():
        d = probe_mp4(mp4)
        if d:
            log_row(slug, "SKIP (exists)", d, "already built")
            return True

    # Create dirs
    for sub in ["mp3", "media", "mp4", "_qc"]:
        (reel / sub).mkdir(parents=True, exist_ok=True)

    beat_sheet = reel / "beat_sheet.json"
    if not beat_sheet.exists():
        log_row(slug, "FAIL", "—", "beat_sheet.json missing — run write_beat_sheets.py first")
        return False

    # 1. Kokoro audio
    print(f"\n[{slug}] generating audio…")
    rc, out, err = run(
        f'python3 "{KOKORO}" "{reel}" --no-gate',
        timeout=600
    )
    if rc != 0:
        log_row(slug, "FAIL (audio)", "—", err[:120].replace("\n"," "))
        return False

    # 2. Remotion scenes
    print(f"[{slug}] rendering Remotion scenes…")
    rc, out, err = run(
        f'RIFF_PROJECT="{reel}" python3 "{REMOTION_PY}" "{reel}" --force',
        timeout=900
    )
    if rc != 0:
        log_row(slug, "FAIL (remotion)", "—", err[:120].replace("\n"," "))
        return False

    # 3. Compile (--allow-slates: Manim concept beats render as slates on first pass;
    #    a separate Manim-scene build pass will fill them)
    print(f"[{slug}] compiling…")
    rc, out, err = run(
        f'python3 "{COMPILE_PY}" "{reel}" --height 1080 --fps 30 --force --allow-slates',
        timeout=600
    )
    if rc != 0:
        log_row(slug, "FAIL (compile)", "—", err[:120].replace("\n"," "))
        return False

    # 4. Probe result
    dur = probe_mp4(mp4)
    if dur:
        log_row(slug, "DONE", dur)
        return True
    else:
        log_row(slug, "FAIL (probe)", "—", "mp4 missing or not 1080p after compile")
        return False


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", default="C01", help="First card to build, e.g. C01")
    parser.add_argument("--end",   default="C30", help="Last card to build, e.g. C30")
    args = parser.parse_args()

    start_idx = int(args.start[1:]) - 1
    end_idx   = int(args.end[1:])

    slugs_to_build = SLUGS[start_idx:end_idx]

    # Write log header if file is new
    if not LOG_FILE.exists():
        with open(LOG_FILE, "w") as f:
            f.write("# NEI Batch Build Log\n\n")
            f.write(f"Started: {datetime.now().isoformat()}\n\n")
            f.write("| Slug | Status | Duration | Notes |\n")
            f.write("|------|--------|----------|-------|\n")

    ok = 0
    fail = 0
    for slug in slugs_to_build:
        try:
            success = build_slug(slug)
        except Exception as e:
            log_row(slug, "FAIL (exception)", "—", str(e)[:120])
            success = False
        if success:
            ok += 1
        else:
            fail += 1

    with open(LOG_FILE, "a") as f:
        f.write(f"\n**Completed:** {datetime.now().isoformat()}  OK={ok}  FAIL={fail}\n")
    print(f"\nDone. OK={ok}  FAIL={fail}")

if __name__ == "__main__":
    main()
