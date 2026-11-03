"""make_captions.py — captions.srt from the aligned narration, placed on the compiled timeline.

The toolkit's make_srt.py no longer exists and stage_publish.py also stages publishing files, so
this builds the caption source directly:
  - word timings: <reel>/mp3/words.json (align.py output; frames at words.json "fps")
  - beat start times: the compiled timeline, <folder>/clips/_work/resolved-sheet.json
    (each beat starts at the sum of the previous beats' actual_duration_s)
  - cues: at most ~7 words / 42 characters, broken at sentence ends; narration text only
Then muxes captions as a soft mov_text track, in place (fellows CLAUDE.md §2: never burned in).

Usage: python make_captions.py <folder> <video.mp4> [--words <reel>/mp3/words.json]
"""
import argparse
import json
import os
import subprocess
from pathlib import Path


def ts(sec):
    ms = int(round(sec * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"


def build(folder: Path, words_path: Path) -> str:
    words = json.loads(words_path.read_text(encoding="utf-8"))
    fps = float(words["fps"])
    sheet = json.loads((folder / "clips" / "_work" / "resolved-sheet.json").read_text(encoding="utf-8"))
    cues, t0 = [], 0.0
    for b in sheet["beats"]:
        ws = words["beats"].get(b["beat_id"], [])
        cur = []
        for w in ws:
            cur.append(w)
            text = " ".join(x["text"] for x in cur)
            if len(cur) >= 7 or len(text) >= 42 or w["text"].rstrip().endswith((".", "?")):
                cues.append((t0 + cur[0]["startFrame"] / fps, t0 + cur[-1]["endFrame"] / fps, text))
                cur = []
        if cur:
            cues.append((t0 + cur[0]["startFrame"] / fps, t0 + cur[-1]["endFrame"] / fps, " ".join(x["text"] for x in cur)))
        t0 += float(b["actual_duration_s"])
    out, prev_end = [], 0.0
    for i, (a, e, text) in enumerate(cues, 1):
        a = max(a, prev_end)
        e = max(e, a + 0.5)
        out += [str(i), f"{ts(a)} --> {ts(e)}", text, ""]
        prev_end = e
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder", type=Path)
    ap.add_argument("video", type=Path)
    ap.add_argument("--words", type=Path)
    a = ap.parse_args()
    words = a.words or a.folder / "mp3" / "words.json"
    srt = a.folder / "captions.srt"
    srt.write_text(build(a.folder, words), encoding="utf-8")
    tmp = a.video.with_name("_tmp_captioned.mp4")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(a.video), "-i", str(srt), "-map", "0", "-map", "1",
                    "-c", "copy", "-c:s", "mov_text", "-metadata:s:s:0", "language=eng", str(tmp)], check=True)
    os.replace(tmp, a.video)
    print(f"[captions] {srt} muxed into {a.video}")


if __name__ == "__main__":
    main()
