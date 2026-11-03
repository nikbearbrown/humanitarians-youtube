"""Shortened on-screen strings for the 9:16 cut (vertical/beat_sheet.json), so portrait text fits on one
line at the phone type scale. Narration is identical in both cuts; each short form says the same thing.
Run after ./art vertical:  python vertical_strings.py"""
import json
from pathlib import Path

p = Path(__file__).resolve().parent / "vertical" / "beat_sheet.json"
b = json.loads(p.read_text(encoding="utf-8"))
SHORT = {
    "B01": {"title": "Loudest Points", "sparkLine": "Thousands of numbers, a few stars."},
    "B02": {"title": "Pairs Into Codes", "sparkLine": "Two frequencies, one gap: a hash."},
    "B03": {"title": "Timing Votes", "sparkLine": "Real matches line up."},
    "B04": {"title": "I Built One", "sparkLine": "Thirty-three votes against two."},
    "B05": {"title": "The Noise Test", "sparkLine": "Unsure? It says no match."},
    "B06": {"title": "Recording, Not Song", "sparkLine": "New key or speed, new codes."},
    "B07": {"title": "It Gets Matched", "lede": "Even under talking.", "phoneType": True,
            "steps": ["Talking won't hide it", "Uploads get checked", "Own the rights to it"],
            "sparkLine": "Check the rights first."},
}
for x in b["beats"]:
    if x["beat_id"] in SHORT:
        x["shot"]["remotion"]["props"].update(SHORT[x["beat_id"]])
p.write_text(json.dumps(b, ensure_ascii=False, indent=1), encoding="utf-8")
print("vertical strings set")
