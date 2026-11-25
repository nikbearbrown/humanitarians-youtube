"""Shortened on-screen strings for the 9:16 cut's Remotion apply card (vertical/beat_sheet.json, B07), so phone
text fits on one line at the phone type scale. Narration is identical in both cuts; each short form says the same
thing. Run after ./art vertical:   python vertical_strings.py <reel-dir>"""
import json
import sys
from pathlib import Path

reel = Path(sys.argv[1]).resolve()
SHORT = {
    "auto-tune-explainer": {"B07": {
        "title": "Try Pitch Correction", "lede": "Find the repeat, pick the note.", "phoneType": True,
        "steps": ["Set the key first", "Slow retune: natural", "Zero: the robot effect"], "sparkScale": 1.25,
        "sparkLine": "A little maths per note."}},
    "bluetooth-audio-explainer": {"B07": {
        "title": "Better Bluetooth Sound", "lede": "Squeezed, hopped, buffered.", "phoneType": True,
        "steps": ["Phone close by", "Pick a better codec", "Use game mode"], "sparkScale": 1.25,
        "sparkLine": "A quarter of the data."}},
}
p = reel / "vertical" / "beat_sheet.json"
b = json.loads(p.read_text(encoding="utf-8"))
slug = b["metadata"]["slug"].replace("-vertical", "")
for x in b["beats"]:
    if x["beat_id"] in SHORT.get(slug, {}):
        x["shot"]["remotion"]["props"].update(SHORT[slug][x["beat_id"]])
p.write_text(json.dumps(b, ensure_ascii=False, indent=1), encoding="utf-8")
print("vertical strings set for", slug)
