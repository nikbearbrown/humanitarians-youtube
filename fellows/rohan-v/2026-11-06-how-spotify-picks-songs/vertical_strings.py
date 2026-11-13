"""Shortened on-screen strings for the 9:16 cut (vertical/beat_sheet.json), so portrait text fits on one
line at the phone type scale. Narration is identical in both cuts; each short form says the same thing.
Lone words with no tall letters ("a", "or", "same", "error") are avoided: they fall under the 4K phone floor.
Run after ./art vertical:  python vertical_strings.py"""
import json
from pathlib import Path

p = Path(__file__).resolve().parent / "vertical" / "beat_sheet.json"
b = json.loads(p.read_text(encoding="utf-8"))
SHORT = {
    "B01": {"title": "What It Learns From", "sparkLine": "Plays, skips, saves."},
    "B02": {"title": "Mostly Empty", "sparkLine": "Taste lists, multiplied."},
    "B03": {"title": "It Found Genres", "sparkLine": "Shared listeners, close."},
    "B04": {"title": "Just Beats the Hits", "sparkLine": "Seventy-four to sixty-five."},
    "B05": {"title": "It Leans on Hits", "sparkLine": "No plays, no picks."},
    "B06": {"title": "Room to Explore", "sparkLine": "Two slots for the unknown."},
    "B07": {"title": "Steer Your Picks", "lede": "It follows what you play.", "phoneType": True,
            "steps": ["Play, skip, save on purpose", "Exclude sleep playlists", "Search for new music"], "sparkScale": 1.25,
            "sparkLine": "Your listening is the input."},
}
for x in b["beats"]:
    if x["beat_id"] in SHORT:
        x["shot"]["remotion"]["props"].update(SHORT[x["beat_id"]])
p.write_text(json.dumps(b, ensure_ascii=False, indent=1), encoding="utf-8")
print("vertical strings set")
