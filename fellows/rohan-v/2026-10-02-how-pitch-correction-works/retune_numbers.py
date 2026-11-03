"""One-off edit (2026-10-05): the last note moved from 62 to 75 cents flat so the chromatic result
stays on F#4 through the vibrato (at 62 the vibrato peaks crossed the halfway point and the
re-measured curve flickered to G4). The run's new figures are written into the narration here."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
EDITS = {
    "B04": [("On average, thirty-seven cents out.", "On average, forty cents out.")],
    "B05": [("It's eighteen cents from perfect", "It's nineteen cents from perfect")],
    "B06": [("My last note is sixty-two cents below G", "My last note is seventy-five cents below G")],
}
PROPS = {"B04": {"sparkLine": "Forty cents out, then under three."}}
CUES = {"B05": ("eighteen", "nineteen", "nineteen cents from perfect"),
        "B06": ("sixtytwo", "seventyfive", "seventy-five cents below G")}

for name in ("beat_sheet.json", "author_sheet.py"):
    p = HERE / name
    s = p.read_text(encoding="utf-8")
    for bid, pairs in EDITS.items():
        for old, new in pairs:
            assert old in s or name == "author_sheet.py", (name, old)
            s = s.replace(old, new)
    s = s.replace("Thirty-seven cents out, then under three.", "Forty cents out, then under three.")
    p.write_text(s, encoding="utf-8")

cues_p = HERE / "cues.json"
cues = json.loads(cues_p.read_text(encoding="utf-8"))
for bid, (old, new, phrase) in CUES.items():
    cues[bid].pop(old, None)
    cues[bid][new] = phrase
cues_p.write_text(json.dumps(cues, ensure_ascii=False, indent=1), encoding="utf-8")
print("narration and cues updated")
