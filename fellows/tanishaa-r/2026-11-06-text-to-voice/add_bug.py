"""add_bug.py — LOGO LAW for the library scenes that don't draw the HAI mark themselves.

Draws the Humanitarians AI mark (the three polygons of logos/humanitarians/
humanitarians-logo-1.svg) to a transparent PNG and composites it lower-right,
inside the 5% title-safe area at 32% opacity, matching HaiBug in RagScenes.tsx.
Rewrites media/<BID>.mp4 in place, once (a .bugged marker prevents doubling).

Run inside the brutalist env:  python add_bug.py B00 B01 B07 B08
                               python add_bug.py --dir vertical B00 B01 B07 B08   (9:16)
"""
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
MEDIA = HERE / "media"
LOGO = HERE / "_qc" / "hai-bug.png"

# SVG viewBox 0 0 311 368; paths copied verbatim from the logo file.
POLYS = [
    [(0, 0), (74, 0), (74, 148), (178, 148), (206, 218), (74, 218), (74, 368), (0, 368)],
    [(81, 1), (153, 1), (302, 367), (228, 367)],
    [(237, 0), (311, 0), (311, 368), (237, 368)],
]


def make_logo(height_px):
    s = height_px / 368
    im = Image.new("RGBA", (round(311 * s) + 2, height_px + 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for poly in POLYS:
        d.polygon([(x * s, y * s) for x, y in poly], fill=(23, 23, 23, round(255 * 0.32)))
    LOGO.parent.mkdir(exist_ok=True)
    im.save(LOGO)


def main(bids):
    for bid in bids:
        src = MEDIA / f"{bid}.mp4"
        marker = MEDIA / f".{bid}.bugged"
        if marker.exists() and marker.stat().st_mtime >= src.stat().st_mtime:
            print(f"{bid}: already has the bug")
            continue
        w, h = map(int, subprocess.check_output(
            ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
             "-of", "csv=p=0", str(src)], text=True).strip().split(","))
        portrait = h > w
        scale = w / (1080 if portrait else 1920)
        mx, my, lh = (54, 96, 60) if portrait else (96, 54, 54)   # matches PBug / HaiBug
        make_logo(round(lh * scale))
        tmp = MEDIA / f".{bid}.tmp.mp4"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), "-i", str(LOGO), "-filter_complex",
                        f"[0:v][1:v]overlay=W-w-{round(mx * scale)}:H-h-{round(my * scale)}",
                        "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", "-c:a", "copy", str(tmp)], check=True)
        tmp.replace(src)
        marker.touch()
        print(f"{bid}: bug added ({w}x{h})")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[:1] == ["--dir"]:
        MEDIA = HERE / args[1] / "media"
        args = args[2:]
    main(args)
