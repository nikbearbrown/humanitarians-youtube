"""Shortened on-screen strings for the 9:16 cut (vertical/beat_sheet.json), so portrait text fits on one
line at the phone type scale. Narration is identical in both cuts; each short form says the same thing.
Lone words with no tall letters ("a", "or", "same", "error") are avoided: they fall under the 4K phone floor.
Run after ./art vertical:  python vertical_strings.py"""
import json
from pathlib import Path

p = Path(__file__).resolve().parent / "vertical" / "beat_sheet.json"
b = json.loads(p.read_text(encoding="utf-8"))
SHORT = {
    "B01": {"title": "Flip the Wave", "sparkLine": "Noise plus anti-noise: silence."},
    "B02": {"title": "Listen, Flip, Adjust", "sparkLine": "Stay ahead of the noise."},
    "B03": {"title": "Late Hurts Highs", "sparkLine": "Same delay: high pitch fails."},
    "B04": {"title": "What It Cancels", "sparkLine": "Steady: gone. Sudden: still there."},
    "B05": {"title": "Quiet Lows Only", "sparkLine": "Cups block highs; chip cancels lows."},
    "B06": {"title": "Make It Work", "lede": "Steady noise, tight seal.", "phoneType": True,
            "steps": ["Use it for steady noise", "Seal the cups well", "Turn the music down"], "sparkScale": 1.25,
            "sparkLine": "Cancel hum, lower volume."},
}
for x in b["beats"]:
    if x["beat_id"] in SHORT:
        x["shot"]["remotion"]["props"].update(SHORT[x["beat_id"]])
p.write_text(json.dumps(b, ensure_ascii=False, indent=1), encoding="utf-8")
print("vertical strings set")
