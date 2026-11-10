"""Shortened on-screen strings for the 9:16 cut's Remotion apply card (vertical/beat_sheet.json, B07), so phone
text fits on one line at the phone type scale. Narration is identical in both cuts; each short form says the same
thing. Run after ./art vertical:   python vertical_strings.py <reel-dir>"""
import json
import sys
from pathlib import Path

reel = Path(sys.argv[1]).resolve()
SHORT = {
    "netflix-streaming-explainer": {"B07": {
        "title": "Get the Best Picture", "lede": "It can't beat your connection.", "phoneType": True,
        "steps": ["Full HD: 5 Mbit/s", "4K: 15 Mbit/s", "Keep it steady"], "sparkScale": 1.25,
        "sparkLine": "Chosen chunk by chunk."}},
    "spatial-audio-explainer": {"B07": {
        "title": "Try Spatial Audio", "lede": "Rebuilt in your headphones.", "phoneType": True,
        "steps": ["Headphones with head tracking", "Set up your ear profile", "Pick Dolby Atmos music"], "sparkScale": 1.25,
        "sparkLine": "Two ears, a little maths."}},
}
p = reel / "vertical" / "beat_sheet.json"
b = json.loads(p.read_text(encoding="utf-8"))
slug = b["metadata"]["slug"].replace("-vertical", "")
for x in b["beats"]:
    if x["beat_id"] in SHORT.get(slug, {}):
        x["shot"]["remotion"]["props"].update(SHORT[slug][x["beat_id"]])
p.write_text(json.dumps(b, ensure_ascii=False, indent=1), encoding="utf-8")
print("vertical strings set for", slug)
