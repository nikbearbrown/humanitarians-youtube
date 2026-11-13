"""Shortened on-screen strings for the 9:16 cut (vertical/beat_sheet.json), so portrait text fits on one
line at the phone type scale. Narration is identical in both cuts; each short form says the same thing.
Lone words with no tall letters ("a", "or", "same", "error") are avoided: they fall under the 4K phone floor.
Run after ./art vertical:  python vertical_strings.py"""
import json
from pathlib import Path

p = Path(__file__).resolve().parent / "vertical" / "beat_sheet.json"
b = json.loads(p.read_text(encoding="utf-8"))
SHORT = {
    "B01": {"title": "Seven Notes", "sparkLine": "Same notes, different home."},
    "B02": {"title": "Count the Notes", "sparkLine": "Twelve bars: the note profile."},
    "B03": {"title": "Match the Shape", "sparkLine": "The closest shape wins."},
    "B04": {"title": "Fifty of Sixty Right", "sparkLine": "Pop, rock, blues: all right."},
    "B05": {"title": "Wrong Home", "sparkLine": "A minor, C major: identical notes."},
    "B06": {"title": "When Keys Change", "sparkLine": "One label can't follow it."},
    "B07": {"title": "When the Key Looks Off", "lede": "Check the related keys.", "phoneType": True,
            "steps": ["Check the relative key", "A minor and C major match", "Check each section"], "sparkScale": 1.25,
            "sparkLine": "Same notes, then the home note."},
}
for x in b["beats"]:
    if x["beat_id"] in SHORT:
        x["shot"]["remotion"]["props"].update(SHORT[x["beat_id"]])
p.write_text(json.dumps(b, ensure_ascii=False, indent=1), encoding="utf-8")
print("vertical strings set")
