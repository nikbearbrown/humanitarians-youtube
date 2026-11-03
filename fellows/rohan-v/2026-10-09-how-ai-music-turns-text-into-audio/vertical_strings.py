"""Shortened on-screen strings for the 9:16 cut (vertical/beat_sheet.json), so portrait text fits on one
line at the phone type scale. Narration is identical in both cuts; each short form says the same thing.
Run after ./art vertical:  python vertical_strings.py"""
import json
from pathlib import Path

p = Path(__file__).resolve().parent / "vertical" / "beat_sheet.json"
b = json.loads(p.read_text(encoding="utf-8"))
SHORT = {
    "B01": {"title": "Audio Is Numbers", "sparkLine": "Sixteen million: too much to predict."},
    "B02": {"title": "Frame to Token", "sparkLine": "Find the closest shape."},
    "B03": {"title": "Codebooks Stack", "sparkLine": "Add the pieces. Get closer."},
    "B04": {"title": "I Built a Codec", "sparkLine": "The treble goes first."},
    "B05": {"title": "The Next Token", "sparkLine": "Learn what follows."},
    "B06": {"title": "Words Tilt Odds", "sparkLine": "Words steer the guesses."},
    "B07": {"title": "Steer, Then Pick", "lede": "Words steer the odds.", "phoneType": True,
            "steps": ["Generate several", "Name the instruments", "Check the treble"],
            "sparkLine": "Steer, then listen."},
}
for x in b["beats"]:
    if x["beat_id"] in SHORT:
        x["shot"]["remotion"]["props"].update(SHORT[x["beat_id"]])
p.write_text(json.dumps(b, ensure_ascii=False, indent=1), encoding="utf-8")
print("vertical strings set")
