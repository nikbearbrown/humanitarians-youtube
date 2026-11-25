"""Shortened on-screen strings for the 9:16 cut (vertical/beat_sheet.json), so portrait text fits on one
line at the phone type scale. Narration is identical in both cuts; each short form says the same thing.
Lone words with no tall letters ("a", "or", "same", "error") are avoided: they fall under the 4K phone floor.
Run after ./art vertical:  python vertical_strings.py"""
import json
from pathlib import Path

p = Path(__file__).resolve().parent / "vertical" / "beat_sheet.json"
b = json.loads(p.read_text(encoding="utf-8"))
SHORT = {
    "B08": {"title": "Help the Map", "lede": "People feed it data.", "phoneType": True,
            "steps": ["Big blue circle? Look up", "Report crashes", "Answer the crowd question"], "sparkScale": 1.25,
            "sparkLine": "Your phone is a sensor."},
}
for x in b["beats"]:
    if x["beat_id"] in SHORT:
        x["shot"]["remotion"]["props"].update(SHORT[x["beat_id"]])
p.write_text(json.dumps(b, ensure_ascii=False, indent=1), encoding="utf-8")
print("vertical strings set")
