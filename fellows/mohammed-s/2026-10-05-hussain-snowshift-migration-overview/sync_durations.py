#!/usr/bin/env python3
"""sync_durations.py — pin every beat's composition length to its measured audio.

remotion_scenes.py renders a beat at the composition's own durationInFrames and
then trims a long render to the beat (or freeze-holds a short one). Every
composition this reel uses derives durationInFrames from a `durationSeconds`
prop (calculateMetadata in Root.tsx), so this script copies the ground truth
Kokoro measured into that prop: `actual_duration_s` plus the beat's
`lead_silence_s`, which the compiled beat also spans.

Skipping it is how motion keyed late in a beat gets silently cut (the Cortex
reel lost its B02 payoff that way). Run after generate_audio_kokoro.py and
before remotion_scenes.py — on this folder and again on vertical/. Idempotent.

    python3 sync_durations.py <reel_dir>
"""
import json
import sys
from pathlib import Path


def main() -> int:
    folder = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    sheet_path = folder / "beat_sheet.json"
    sheet = json.loads(sheet_path.read_text(encoding="utf-8"))

    touched, missing = [], []
    for beat in sheet["beats"]:
        rem = (beat.get("shot") or {}).get("remotion")
        if not rem:
            continue
        dur = beat.get("actual_duration_s")
        if not dur:
            missing.append(beat["beat_id"])
            continue
        want = round(dur + float(beat.get("lead_silence_s") or 0), 2)
        props = rem.setdefault("props", {})
        if props.get("durationSeconds") != want:
            props["durationSeconds"] = want
            touched.append(f"{beat['beat_id']}={want}s")

    if missing:
        print(f"[sync] WARNING no measured audio yet for: {', '.join(missing)}")

    # UTF-8 + atomic replace: the sheet carries em dashes and arrows, and the
    # Windows locale default (cp1252) would raise mid-write and truncate it.
    tmp = sheet_path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(sheet, indent=2, ensure_ascii=False), encoding="utf-8")
    tmp.replace(sheet_path)

    print(f"[sync] {len(touched)} beat(s) pinned to their audio"
          + (f": {', '.join(touched)}" if touched else " (already in sync)"))
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
