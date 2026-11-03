"""Shortened on-screen strings for the 9:16 cut (vertical/beat_sheet.json), so portrait text meets
the phone type floor. Narration is identical in both cuts; each short form says the same thing."""
import json
from pathlib import Path

p = Path(__file__).resolve().parent / "vertical" / "beat_sheet.json"
b = json.loads(p.read_text(encoding="utf-8"))
SHORT = {
    "B01": {"title": "The Handbook, v1.0", "sparkLine": "One document, not asking around.",
            "stats": [{"value": "46", "label": "PAGES"}, {"value": "12", "label": "SECTIONS"}, {"value": "v1.0", "label": "WORD FILE"}]},
    "B02": {"title": "Access Steps", "docLabel": "SECTION 4", "docStatus": "WRITTEN · v1.0",
            "sparkLine": "Numbered steps now.", "phoneType": True,
            "tools": [{"name": "Discord", "purpose": "THE KEY", "hue": "#5865F2"},
                      {"name": "Suno", "purpose": "MUSIC", "hue": "#E5197F"},
                      {"name": "Midjourney", "purpose": "IMAGES", "hue": "#2F2A26"},
                      {"name": "Canva", "purpose": "DESIGN", "hue": "#00A3B4"},
                      {"name": "Adobe CC", "purpose": "EDITING", "hue": "#DA1F26"}]},
    "B03": {"title": "After Review", "leftHeader": "draft", "rightHeader": "after review", "phoneType": True,
            "sparkLine": "The draft was the start.",
            "rows": [{"was": "navy and cream", "now": "website look"},
                     {"was": "username to PM", "now": "step removed"},
                     {"was": "logs by hand", "now": "Claude keeps them"},
                     {"was": "no video on GitHub", "now": "inputs on GitHub"},
                     {"was": "videos to PM", "now": "one reviewer"}]},
    "B04": {"title": "Done, and Not Yet", "good": ["one place for all of it", "editable Word file", "shared privately"],
            "notYet": ["used by a new fellow"], "pending": "PAGE ONE, NO HELP", "sparkLine": "Written isn't tested.",
            "baseline": True},
    "B05": {"title": "Shipped, and Next", "phoneType": True, "sparkLine": "Next: video editing.",
            "shipped": [{"label": "Renewal approved", "sub": "Oct – Jan"}, {"label": "Handbook v1.0", "sub": "a month early"}],
            "next": [{"label": "Test 2 editors", "sub": "same footage", "due": "2–20 NOV"},
                     {"label": "LL edit pipeline", "sub": "best tool", "due": "BY 11 DEC"}]},
    "B06": {"title": "New? Start Here", "lede": "One place to start.", "phoneType": True,
            "steps": ["Ask your PM for it", "First-week checklist", "Wed, 12 pm ET", "Unclear? Tell me"],
            "sparkLine": "Checklist first."},
}
for x in b["beats"]:
    if x["beat_id"] in SHORT:
        x["shot"]["remotion"]["props"].update(SHORT[x["beat_id"]])
p.write_text(json.dumps(b, ensure_ascii=False, indent=1), encoding="utf-8")
print("vertical strings set")
