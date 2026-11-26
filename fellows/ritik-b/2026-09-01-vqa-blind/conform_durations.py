#!/usr/bin/env python3
"""conform_durations.py — push the MEASURED audio length into each scene's durationS.

Audio-first: the mp3 durations generate_audio_kokoro.py wrote into `actual_duration_s`
are the clock. The seven body compositions take `durationS` as a prop and Root.tsx's
calculateMetadata turns it into durationInFrames, so a beat animates across exactly its
narration instead of finishing early and freeze-holding the tail. The four Claude UI
bookends have fixed-length compositions and are freeze-extended by remotion_scenes.py.

Run AFTER generate_audio_kokoro.py and BEFORE remotion_scenes.py, in both folders.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
FOLDERS = [HERE, HERE.parent / "blip-bootstrap-916"]

# only these schemas carry durationS; passing it to a bookend would fail zod validation
RESPONSIVE = {
    "ReelExecSummary", "ReelFramework", "BlipMed", "BlipCapFilt",
    "BlipIndependence", "BlipDiversity", "BlipLadder",
}


def conform(folder: Path) -> None:
    sheet_path = folder / "beat_sheet.json"
    sheet = json.loads(sheet_path.read_text())
    touched = []
    for b in sheet["beats"]:
        rem = b.get("shot", {}).get("remotion") or {}
        pattern = (rem.get("pattern") or "").removesuffix("916")
        if pattern not in RESPONSIVE:
            continue
        d = b.get("actual_duration_s") or b.get("estimated_duration_s")
        if not d:
            continue
        rem.setdefault("props", {})["durationS"] = round(float(d), 3)
        touched.append(f"{b['beat_id']}={d:.2f}s")
    # keep the human-readable estimate honest too
    for b in sheet["beats"]:
        if b.get("actual_duration_s"):
            b["estimated_duration_s"] = round(float(b["actual_duration_s"]), 2)
    sheet_path.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + "\n")
    total = sum(float(b.get("actual_duration_s") or 0) for b in sheet["beats"])
    print(f"{folder.name}: durationS -> {', '.join(touched)}")
    print(f"{folder.name}: total {total:.2f}s ({total/60:.2f} min)")


if __name__ == "__main__":
    for f in FOLDERS:
        conform(f)
