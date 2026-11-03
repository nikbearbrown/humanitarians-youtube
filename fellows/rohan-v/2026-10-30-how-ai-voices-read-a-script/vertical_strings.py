"""Shortened on-screen strings for the 9:16 cut (vertical/beat_sheet.json), so portrait text fits on one
line at the phone type scale. Narration is identical in both cuts; each short form says the same thing.
Lone words with no tall letters ("a", "or", "same", "error") are avoided: they fall under the 4K phone floor.
Run after ./art vertical:  python vertical_strings.py"""
import json
from pathlib import Path

p = Path(__file__).resolve().parent / "vertical" / "beat_sheet.json"
b = json.loads(p.read_text(encoding="utf-8"))
SHORT = {
    "B01": {"title": "Text to Voice", "sparkLine": "It speaks phonemes, not text."},
    "B02": {"title": "Letters to Sounds", "sparkLine": "Dictionary first, then rules."},
    "B03": {"title": "Two Readings", "sparkLine": "Ten of sixteen right."},
    "B04": {"title": "Numbers to Words", "sparkLine": "Six of seven right. Not prices."},
    "B05": {"title": "Respell It", "sparkLine": "Respell, then listen."},
    "B06": {"title": "Writing for AI Voices", "lede": "It reads the letters, not the intent.", "phoneType": True,
            "steps": ["Write prices out in words", "Respell names", "Reword two-meaning words"], "sparkScale": 1.25,
            "sparkLine": "Write it the way it sounds."},
}
for x in b["beats"]:
    if x["beat_id"] in SHORT:
        x["shot"]["remotion"]["props"].update(SHORT[x["beat_id"]])
p.write_text(json.dumps(b, ensure_ascii=False, indent=1), encoding="utf-8")
print("vertical strings set")
