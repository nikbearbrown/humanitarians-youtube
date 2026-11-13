#!/usr/bin/env python3
"""READ-ALOUD-SHORT.md: the Short Gate P sheet, generated from short/beat_sheet.json (draft 2)."""
import json
import re
from pathlib import Path

HERE = Path(__file__).parent
sheet = json.loads((HERE / "beat_sheet.json").read_text())
WPS = 3.6   # the long film's measured Kokoro pace
out = ["# READ-ALOUD: Short Gate P sheet, draft 2", "",
       f"*{sheet['metadata']['title']}* (working title) · 9:16 · voice `am_onyx`", "",
       "Draft 2 of the Short, rewritten for context (what changed and why: the audit table at the top of",
       "`SCRIPT-SHORT.md`). Your draft 1 PASS doesn't carry over, because most lines are new. Read it aloud, top to",
       "bottom, in one sitting, as someone who has never seen the long film. Then reply **\"Short Gate P PASS\"**",
       "or list the beats that tripped you.", "",
       "Say-it-right: **Mycroft** = MY-croft (the audio uses the override). **Meta** = MEH-tuh.", "",
       "## Mechanical pass, already run", ""]
long_s = [(b["beat_id"], s) for b in sheet["beats"]
          for s in re.split(r"(?<=[.?!])\s+", b["narration_text"]) if len(s.split()) > 22]
out.append(f"- Sentences over 22 words: {len(long_s)}" + ("".join(f"\n  - {b}: {s}" for b, s in long_s)))
out.append("- Digits in narration: " + str(sum(bool(re.search(r"\d", b["narration_text"])) for b in sheet["beats"])))
out += ["- Stills: portrait zones 7/7, Gate V 0 BLOCKER / 0 MAJOR, and every frame looked at (S03 and S05 overlaps fixed)", "",
        "## The script", ""]
t = 0.0
for b in sheet["beats"]:
    p = b["shot"]["remotion"]["props"]
    screen = [p["heading"]] + [f"{c['label']}: {c['value']}" for c in p.get("compare", [])] + p.get("evidenceLines", [])
    if p.get("question", {}).get("text"):
        screen += [p["question"]["text"], p["question"]["good"], p["question"]["weak"]]
    out += [f"### [{int(t // 60)}:{int(t % 60):02d}] {b['beat_id']} · {b['act']}" + (f"  _(tone: {b['tone']})_" if b["tone"] else ""), "",
            b["narration_text"], ""]
    if b.get("hold_after_s"):
        out += [f"*({b['hold_after_s']:g} s silence)*", ""]
    out += [f"<sub>**On screen:** {' · '.join(s for s in screen if s)}</sub>", "",
            "> ☐ reads cleanly   ☐ note: ______________________", ""]
    t += len(b["narration_text"].split()) / WPS + b.get("hold_after_s", 0)
out += [f"**Total: about {int(t // 60)}:{int(t % 60):02d}.**", ""]
(HERE / "READ-ALOUD-SHORT.md").write_text("\n".join(out))
print("READ-ALOUD-SHORT.md", f"~{t:.0f} s", f"{len(long_s)} long sentences")
