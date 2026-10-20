"""Shortened on-screen strings for the 9:16 cut (vertical/beat_sheet.json), so portrait text fits on one
line at the phone type scale. Narration is identical in both cuts; each short form says the same thing.
Run after ./art vertical:  python vertical_strings.py"""
import json
from pathlib import Path

p = Path(__file__).resolve().parent / "vertical" / "beat_sheet.json"
b = json.loads(p.read_text(encoding="utf-8"))
SHORT = {
    "B01": {"title": "Call and Response", "note": "Native review pending", "sparkLine": "English lands with its Hindi."},
    "B02": {"title": "Two Tiers", "sparkLine": "Move up, keep the song.",
            "tiers": [{"name": "TIER 1 · FOUNDATION", "english": 50, "line": "Half Hindi, half English"},
                      {"name": "TIER 2 · BRIDGE", "english": 80, "line": "Mostly English"}]},
    "B03": {"title": "New Sound", "phoneType": True, "leftHeader": "first", "rightHeader": "revision",
            "rows": [{"was": "Guitar and violin", "now": "Dhol, tabla, sitar"},
                     {"was": "Violin every chorus", "now": "Strings far back"},
                     {"was": "102 to 106 BPM", "now": "108 to 110 BPM"},
                     {"was": "Lead with group", "now": "Big group replies"}],
            "sparkLine": "Bigger, brighter, faster."},
    "B04": {"title": "Protecting the Girls", "good": ["Dreams and jobs", "Daily routines", "Values"],
            "notYet": ["Names, stories", "Any real likeness"],
            "pending": "Staff check home-life lines", "sparkLine": "Dreams, not identities."},
    "B05": {"title": "Done, and Next", "phoneType": True,
            "shipped": [{"label": "Four songs", "sub": "two tiers each"},
                        {"label": "Versions made", "sub": "the team picks"}],
            "next": [{"label": "Hindi review", "sub": "native speaker", "due": "NEXT"},
                     {"label": "Pitch video", "sub": "proof of concept", "due": "THEN"}],
            "sparkLine": "Pick, review, pitch."},
}
for x in b["beats"]:
    if x["beat_id"] in SHORT:
        x["shot"]["remotion"]["props"].update(SHORT[x["beat_id"]])
p.write_text(json.dumps(b, ensure_ascii=False, indent=1), encoding="utf-8")
print("vertical strings set")
