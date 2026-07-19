#!/usr/bin/env python3
"""make_audio_kokoro.py — regenerate Kokoro narration for this lecture.
Free, local; no API key needed.  Voice: am_onyx (brutalist default).

Run from any directory:
    python3 make_audio_kokoro.py          # regenerate all missing/stale
    python3 make_audio_kokoro.py --all    # force-regenerate every segment
    python3 make_audio_kokoro.py S03 S07  # regenerate specific segment IDs

Keep make_audio.py alongside this for ElevenLabs override if needed.
"""
import argparse
import json
import os
import shutil
import struct
import subprocess
import sys
import wave
from pathlib import Path

HERE = Path(__file__).resolve().parent
ART_HOME = Path(os.environ.get("ART_HOME",
                               HERE.parents[1] / "brutalist-art"))
KOKORO_MODEL = Path(os.environ.get("KOKORO_MODEL",
                                    ART_HOME / "runtime/models/kokoro/kokoro-v1.0.onnx"))
KOKORO_VOICES = Path(os.environ.get("KOKORO_VOICES",
                                     ART_HOME / "runtime/models/kokoro/voices-v1.0.bin"))
FFMPEG = shutil.which("ffmpeg") or "ffmpeg"
FFPROBE = shutil.which("ffprobe") or "ffprobe"


def load_kokoro():
    if not (KOKORO_MODEL.exists() and KOKORO_VOICES.exists()):
        sys.exit(f"[kokoro] model files missing. Expected: {KOKORO_MODEL}")
    try:
        from kokoro_onnx import Kokoro
    except ImportError:
        sys.exit("[kokoro] pip install kokoro-onnx")
    return Kokoro(str(KOKORO_MODEL), str(KOKORO_VOICES))


def write_mp3(samples, sr, out_path: Path):
    tmp = out_path.with_suffix(".tmp.wav")
    ints = [max(-32768, min(32767, int(s * 32767))) for s in samples]
    with wave.open(str(tmp), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes(struct.pack(f"<{len(ints)}h", *ints))
    subprocess.run([FFMPEG, "-y", "-v", "error", "-i", str(tmp),
                    "-c:a", "libmp3lame", "-q:a", "2", str(out_path)], check=True)
    tmp.unlink()


def measure(path: Path) -> float:
    r = subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", str(path)],
                       capture_output=True, text=True, check=True)
    return float(r.stdout.strip())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("segments", nargs="*", help="segment IDs to regenerate (e.g. S03 S07)")
    ap.add_argument("--all", action="store_true", help="regenerate all segments")
    args = ap.parse_args()

    sheet_path = HERE / "beat_sheet.json"
    if not sheet_path.exists():
        sys.exit(f"[err] beat_sheet.json not found in {HERE}")

    sheet = json.loads(sheet_path.read_text())
    voice = sheet.get("metadata", {}).get("voice_kokoro", "am_onyx")
    audio_dir = HERE / "audio"
    audio_dir.mkdir(exist_ok=True)

    segs = sheet["segments"]
    if args.segments:
        target_ids = set(args.segments)
        segs = [s for s in segs if s["id"] in target_ids]

    k = load_kokoro()
    total = 0.0
    for s in segs:
        out = audio_dir / f"{s['id']}.mp3"
        if out.exists() and not args.all and not args.segments:
            dur = measure(out)
            s["beats"][0]["actual_duration_s"] = dur
            total += dur
            print(f"  [{s['id']}] exists ({dur:.1f}s) — skip (use --all to force)")
            continue
        text = s["beats"][0]["text"].strip() or "."
        samples, sr = k.create(text, voice=voice, speed=1.0, lang="en-us")
        write_mp3(samples, sr, out)
        dur = measure(out)
        s["beats"][0]["audio_file"] = f"audio/{s['id']}.mp3"
        s["beats"][0]["actual_duration_s"] = round(dur, 2)
        total += dur
        print(f"  [{s['id']}] {out.name}  {dur:.1f}s")

    sheet_path.write_text(json.dumps(sheet, indent=2, ensure_ascii=False))
    print(f"\n[ok] {len(segs)} segment(s) · {total:.0f}s total · durations written back")
    print("[next] run:  python3 brutalist-art/runtime/scripts/build_deck.py <folder> && python3 brutalist-art/runtime/scripts/render.py <folder>")


if __name__ == "__main__":
    main()
