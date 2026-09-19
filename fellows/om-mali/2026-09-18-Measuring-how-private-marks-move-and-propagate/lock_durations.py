#!/usr/bin/env python3
"""
lock_durations.py — write the MEASURED Kokoro durations into each Remotion beat's
`durationInSeconds` prop, for this reel and for its 9:16 companion.

Audio-first: the narration MP3s are the master clock. Every week-5 composition derives
durationInFrames from `durationInSeconds` via calculateMetadata, so a scene RE-TIMES to
the real narration instead of being centre-cut or freeze-padded. Nothing here is timed
by hand; run this after every audio regeneration, before rendering.

Usage:  python lock_durations.py [beat_sheet.json ...]     (default: beat_sheet.json)
"""
import json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sheets = [Path(a) for a in sys.argv[1:]] or [HERE / "beat_sheet.json"]


def measure(mp3):
    """The MP3 on disk is the clock — not a number remembered in the sheet. Measuring
    here means build_beat_sheet.py can be re-run at any time without losing the timing."""
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(mp3)],
        capture_output=True, text=True, check=True).stdout.strip()
    return round(float(out), 2)


for sp in sheets:
    if not sp.is_absolute():
        sp = HERE / sp
    sheet = json.loads(sp.read_text(encoding="utf-8"))
    changed = []
    for b in sheet["beats"]:
        mp3 = sp.parent / b.get("audio_file", "")
        if not mp3.is_file():
            sys.exit(f"[lock] {b['beat_id']}: no {b.get('audio_file')} — generate audio first")
        d = measure(mp3)
        b["actual_duration_s"] = d
        rem = (b.get("shot") or {}).get("remotion")
        if not rem:
            continue
        if rem["props"].get("durationInSeconds") != d:
            rem["props"]["durationInSeconds"] = d
            changed.append(f"{b['beat_id']}={d:.2f}s")
    sp.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    total = sum(b.get("actual_duration_s", 0) for b in sheet["beats"])
    lead = sum(b.get("lead_silence_s", 0) for b in sheet["beats"])
    print(f"[lock] {sp.name}: {len(changed)} beat(s) retimed — {' '.join(changed)}")
    print(f"[lock] {sp.name}: narration {total:.2f}s + {lead:.2f}s lead "
          f"= {total + lead:.2f}s ({int((total + lead) // 60)}:{(total + lead) % 60:04.1f})")
