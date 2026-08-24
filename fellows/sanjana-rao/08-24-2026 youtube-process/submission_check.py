"""submission_check.py — the artifact this reel builds.

Validates one Humanitarians AI YouTube submission folder against the
six-criteria acceptance gate (see youtube_video_production_spec.md § 3.1).

Usage:
    python submission_check.py ./ProjectA_Alice/

Exit code 0 = every gate green, 1 = one or more gates failed.
"""
import re
import subprocess
import sys
import urllib.parse
from pathlib import Path

EXPECT = {"16x9": (3840, 2160), "9x16": (2160, 3840)}
NAME = re.compile(r"^([A-Za-z0-9]+)_([A-Za-z0-9]+)_(16x9|9x16)\.mp4$")
FORBID = re.compile(r"_(final|FINAL|v\d+|FINAL2)")


def probe(mp4: Path) -> tuple[int, int]:
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height", "-of", "csv=p=0", str(mp4)],
        text=True,
    ).strip()
    return tuple(int(x) for x in out.split(","))


def check(folder: str) -> bool:
    folder = Path(folder)
    ok = True

    for mp4 in sorted(folder.glob("*.mp4")):
        if FORBID.search(mp4.stem):
            ok = False
            print(f"FAIL name   {mp4.name}  (version suffix — belongs in git)")
            continue
        m = NAME.match(mp4.name)
        if not m:
            ok = False
            print(f"FAIL name   {mp4.name}  (want {{Project}}_{{Volunteer}}_{{16x9|9x16}}.mp4)")
            continue
        print(f"PASS name   {mp4.name}")
        w, h = probe(mp4)
        want = EXPECT[m.group(3)]
        if (w, h) == want:
            print(f"PASS 4K     {mp4.name}  ({w}x{h})")
        else:
            ok = False
            print(f"FAIL 4K     {mp4.name}  ({w}x{h}, want {want[0]}x{want[1]})")

    url_path = folder / "github_url.txt"
    if not url_path.exists():
        ok = False
        print("FAIL github  (github_url.txt missing)")
    else:
        url = url_path.read_text().strip()
        good = urllib.parse.urlparse(url).scheme in ("http", "https")
        print(f"{'PASS' if good else 'FAIL'} github {url}")
        ok &= good

    print(f"{'PASS' if ok else 'FAIL'} submission  ({folder.name})")
    return ok


if __name__ == "__main__":
    sys.exit(0 if check(sys.argv[1]) else 1)
