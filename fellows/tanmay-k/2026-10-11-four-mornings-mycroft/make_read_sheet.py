#!/usr/bin/env python3
"""Writes READ-ALOUD.md from SCRIPT.md, the sheet Tanmay reads from for Gate P (generated, never hand-edited)."""
import re
from pathlib import Path

HERE = Path(__file__).parent
s = (HERE / "SCRIPT.md").read_text()
beats = re.findall(r"^### (B\d\d) · (.+?)\n> (.+?)\n\n\*On screen:\* (.+?)\n", s, re.M | re.S)
EAR = [("Mycroft", "MY-croft", "mˈɪkɹɔft ✗ (MICK-roft)", "mˈaɪkɹɔft", "B02"),
       ("Tanmay Kulkarni", "TAN-may kul-KAR-nee", "tˈænmeɪ kˈʌlkɑːɹni ✓", "—", "B02, B10"),
       ('a JavaScript "or"', "jah-vuh-script OR", 'dʒˈɑːvə skɹˈɪpt "ɔːɹ" ✓', "—", "B03")]
LISTEN = [("B01", "the cold open has to sound like a normal morning, then turn on \"But every number…\""),
          ("B03", "\"The math is right. The reader just doesn't know\": calm, not alarmed; it is the workflow's choice"),
          ("B05", "**\"this one surprised me\"**: a genuine turn, said lightly"),
          ("B07", "**the turn.** \"It passed. All green.\" then the drop: \"But the broken version had never run at all.\""),
          ("B08", "the cool-down: plain and honest; \"and they say so\" without a flourish"),
          ("B09", "a real question to the viewer, unhurried")]
out = ["# READ-ALOUD: Gate P sheet (work video)", "",
       "*Four Mornings* (working title) · structure: FOUR MORNINGS · voice `am_onyx`", "",
       "Generated from `SCRIPT.md` by `make_read_sheet.py`. Read each beat aloud at speaking pace, top to bottom, in one",
       "sitting; tick or note; skim the *on screen* line too. Reply **\"Gate P PASS\"** or list the beats that tripped you.", "",
       "## Say-it-right checklist (Kokoro's phonemes, checked 2026-10-10)", "",
       "| Word | Should sound like | Kokoro alone | Override | Where |", "|---|---|---|---|---|"]
out += [f"| {a} | {b} | `{c}` | `{d}` | {e} |" for a, b, c, d, e in EAR]
out += ["", "## Where to listen hardest", ""] + [f"- **{b}**: {n}" for b, n in LISTEN] + ["", "## The script", ""]
t, total = 0.0, 0
for bid, title, text, screen in beats:
    w = len(text.split()); total += w
    out += [f"### [{int(t // 60)}:{int(t % 60):02d}] {bid} · {title}", "", text, "",
            f"<sub>**On screen:** {screen.strip()}</sub>", "", "> ☐ reads cleanly   ☐ note: ______________________", ""]
    t += w / 3.3
out += [f"_{len(beats)} beats · {total} words · about {int(t // 60)}:{int(t % 60):02d} at 3.3 words/s, before holds._", ""]
(HERE / "READ-ALOUD.md").write_text("\n".join(out))
print(f"READ-ALOUD.md · {len(beats)} beats · {total} words")
