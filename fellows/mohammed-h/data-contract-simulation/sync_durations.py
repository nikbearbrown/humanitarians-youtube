#!/usr/bin/env python3
"""sync_durations.py — push the measured mp3 length into each Sim* beat's props.

WHY THIS EXISTS (audio-first, enforced at the composition boundary)

remotion_scenes.py renders a beat at the composition's OWN durationInFrames and
then reconciles it against the beat: a short render is freeze-held up to the
beat length, a long one is hard-trimmed with `-t`. Both are lossy in their own
way — a fixed-length composition either sits frozen for ten seconds or gets its
payoff amputated.

The Sim* compositions dodge that by deriving durationInFrames from a
`durationSeconds` prop (see calculateMetadata in Root.tsx). This script is what
puts the real number there: it copies `actual_duration_s` — the ground truth
Kokoro measured — into `shot.remotion.props.durationSeconds` for every beat
whose pattern starts with `Sim`. After this runs, `useP()` inside each scene
spans exactly the narration it plays under.

The house Claude scenes (ClaudeComposerAsk / ClaudeVerdictArtifact /
ClaudeTitleOutro) are deliberately skipped: they are absolute-frame paced —
everything happens in the first ~4s and then the frame holds — so the house
freeze-hold behaviour is already correct for them, and adding a prop their zod
schemas don't declare would be noise.

Run it after generate_audio_kokoro.py and before remotion_scenes.py, on the
16:9 folder and again on the 9:16 folder. It is idempotent.

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
        rem = (beat.get("shot") or {}).get("remotion") or {}
        pattern = rem.get("pattern") or ""
        if not pattern.startswith("Sim"):
            continue
        dur = beat.get("actual_duration_s")
        if not dur:
            missing.append(beat["beat_id"])
            continue
        props = rem.setdefault("props", {})
        if props.get("durationSeconds") != dur:
            props["durationSeconds"] = dur
            touched.append(f"{beat['beat_id']}={dur}s")

    if missing:
        print(f"[sync] WARNING no measured audio yet for: {', '.join(missing)} "
              f"— run generate_audio_kokoro.py first")

    # UTF-8 + atomic replace: this sheet carries em dashes, arrows and middle
    # dots, and write_text()'s locale default (cp1252 on Windows) would raise
    # mid-write and truncate it. Same guard as compile.py's stamp_sheet().
    tmp = sheet_path.with_suffix(sheet_path.suffix + ".tmp")
    tmp.write_text(json.dumps(sheet, indent=1, ensure_ascii=False), encoding="utf-8")
    tmp.replace(sheet_path)

    print(f"[sync] {len(touched)} Sim beat(s) pinned to their audio"
          + (f": {', '.join(touched)}" if touched else " (already in sync)"))
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
