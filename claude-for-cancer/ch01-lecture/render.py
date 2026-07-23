#!/usr/bin/env python3
"""render.py — screenshot each slide (headless chromium) and assemble the MP4.
Audio-first: slide hold = measured audio duration if present, else estimated from word count.

Usage:
  python3 render.py <lecture_folder>
  python3 render.py <lecture_folder> beat_sheet.nbb.json   # named variant
"""
import json, subprocess, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

if len(sys.argv) < 2:
    sys.exit("Usage: render.py <lecture_folder> [beat_sheet_filename]")
HERE = Path(sys.argv[1]).resolve()
BS_NAME = sys.argv[2] if len(sys.argv) > 2 else "beat_sheet.json"

W, H, FPS = 1280, 720, 30
sheet = json.loads((HERE / BS_NAME).read_text())
segs = sheet["segments"]
sdir = HERE / "slides"; sdir.mkdir(exist_ok=True)
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

def est(words): return max(3.2, round(words / 2.6 + 0.9, 2))

# 1) screenshots
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME if Path(CHROME).exists() else None,
                          args=["--no-sandbox", "--force-color-profile=srgb"])
    pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
    url = (HERE / "deck.html").as_uri()
    for i, s in enumerate(segs):
        pg.goto(f"{url}#{i+1}", wait_until="networkidle")
        pg.wait_for_timeout(500)
        pg.screenshot(path=str(sdir / f"{s['id']}.png"))
        print(f"  shot {s['id']}")
    b.close()

# 2) per-slide durations + audio presence
have_audio = all((HERE / "audio" / f"{s['id']}.mp3").exists() for s in segs)
durs = []
for s in segs:
    beat = s["beats"][0]
    d = beat.get("actual_duration_s") if have_audio else None
    text = beat.get("text") or beat.get("narration_text", "")
    durs.append(d if d else est(len(text.split())))

# 3) build per-slide clips (image + audio or silence), then concat
clips = []
tail = 0.6
for i, s in enumerate(segs):
    png = sdir / f"{s['id']}.png"
    dur = durs[i] + tail
    clip = HERE / f"_clip_{s['id']}.mp4"
    if have_audio:
        amp3 = HERE / "audio" / f"{s['id']}.mp3"
        cmd = ["ffmpeg", "-y", "-loop", "1", "-i", str(png), "-i", str(amp3),
               "-f", "lavfi", "-t", f"{dur}", "-i", "anullsrc=r=44100:cl=stereo",
               "-filter_complex", "[1:a][2:a]amix=inputs=2:duration=longest:normalize=0[a]",
               "-map", "0:v", "-map", "[a]",
               "-t", f"{dur}", "-r", str(FPS), "-vf", f"scale={W}:{H},format=yuv420p",
               "-c:v", "libx264", "-preset", "medium", "-crf", "18",
               "-c:a", "aac", "-b:a", "160k", str(clip)]
    else:
        cmd = ["ffmpeg", "-y", "-loop", "1", "-i", str(png),
               "-f", "lavfi", "-t", f"{dur}", "-i", "anullsrc=r=44100:cl=stereo",
               "-t", f"{dur}", "-r", str(FPS), "-vf", f"scale={W}:{H},format=yuv420p",
               "-c:v", "libx264", "-preset", "medium", "-crf", "18",
               "-c:a", "aac", "-b:a", "128k", str(clip)]
    result = subprocess.run(cmd, capture_output=True)
    if result.returncode != 0:
        print(f"[err] clip {s['id']} failed:", result.stderr.decode('utf-8','ignore')[-500:], file=sys.stderr)
        sys.exit(result.returncode)
    clips.append(clip)
    print(f"  clip {s['id']}  {dur:.1f}s")

concat = HERE / "_concat.txt"
concat.write_text("".join(f"file '{c}'\n" for c in clips))
suffix = "" if have_audio else "-silent"
out = HERE / f"{sheet['slug']}{suffix}.mp4"
subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat),
                "-c:v", "copy", "-c:a", "aac", "-b:a", "160k",
                "-movflags", "faststart", str(out)], check=True, capture_output=True)
for c in clips: c.unlink()
concat.unlink()
total = sum(durs) + tail * len(segs)
print(f"[ok] {out.name} · {len(segs)} slides · {total:.0f}s ({total/60:.1f} min) · audio={'REAL' if have_audio else 'SILENT previz'}")
