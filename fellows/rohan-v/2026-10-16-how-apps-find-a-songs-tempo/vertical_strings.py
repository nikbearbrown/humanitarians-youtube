"""Shortened on-screen strings for the 9:16 cut (vertical/beat_sheet.json), so portrait text fits on one
line at the phone type scale. Narration is identical in both cuts; each short form says the same thing.
Run after ./art vertical:  python vertical_strings.py"""
import json
from pathlib import Path

p = Path(__file__).resolve().parent / "vertical" / "beat_sheet.json"
b = json.loads(p.read_text(encoding="utf-8"))
SHORT = {
    "B01": {"title": "Beats Per Minute", "sparkLine": "Only the sound."},
    "B02": {"title": "Step One: Onsets", "sparkLine": "Every drum hit spikes."},
    "B03": {"title": "Step Two: Repeats", "sparkLine": "Two real repeats. One beat."},
    "B04": {"title": "Step Three: Choose", "sparkLine": "A preference picks the beat."},
    "B05": {"title": "Double or Half", "sparkLine": "Exactly double. Exactly half."},
    "B06": {"title": "Drummers Drift", "sparkLine": "Follow the hits, not the grid."},
    "B07": {"title": "When the BPM Is Off", "lede": "Double and half: typical.", "phoneType": True,
            "steps": ["Tap along to check it", "Halve it, double it", "Check the beat grid"],
            "sparkLine": "Trust your foot first."},
}
for x in b["beats"]:
    if x["beat_id"] in SHORT:
        x["shot"]["remotion"]["props"].update(SHORT[x["beat_id"]])
p.write_text(json.dumps(b, ensure_ascii=False, indent=1), encoding="utf-8")
print("vertical strings set")
