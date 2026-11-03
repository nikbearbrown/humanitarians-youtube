#!/usr/bin/env python3
"""Writes READ-ALOUD.md from SCRIPT.md, the sheet Tanmay reads from for Gate P (generated, never hand-edited)."""
import re
from pathlib import Path

HERE = Path(__file__).parent
s = (HERE / "SCRIPT.md").read_text()
beats = re.findall(r"^### (B\d\d) · (.+?)\n> (.+?)\n\n\*On screen:\* (.+?)\n", s, re.M | re.S)
EAR = [("Mycroft", "MY-croft", "mˈɪkɹɔft ✗ (MICK-roft)", "mˈaɪkɹɔft", "B02"),
       ("Tanmay Kulkarni", "TAN-may kul-KAR-nee", "tˈænmeɪ kˈʌlkɑːɹni ✓", "—", "B02, B12"),
       ("Ironbridge Power", "EYE-urn-bridge POW-er", "ˈaɪɚnbɹɪdʒ pˈaʊɚ ✓", "—", "B03"),
       ("price-to-earnings", "price to earnings", "pɹˈaɪstʊˈɜːnɪŋz ✓", "—", "B03, B05"),
       ("minute-taker", "MIN-it taker", "mˈɪnɪttˈeɪkɚ ✓ (not my-NOOT)", "—", "B09"),
       ("Python, JavaScript", "PIE-thon, JAH-vuh-script", "pˈaɪθən ✓, dʒˈɑːvə skɹˈɪpt ✓", "—", "B09"),
       ("summarise", "SUM-uh-rize", "sˈʌmɚɹˌaɪz ✓", "—", "B11")]
RE_READ = {"B02", "B07", "B09", "B11"}   # changed after the PROOF review; draft 1 was signed
LISTEN = [("B01", "the cold open: the quoted line is read plainly, as a line of text, then the question lands: \"So who decided the verdict?\""),
          ("B02", "**changed:** the new line \"who had a vote, and how much?\" is the question the whole video answers; say it as a promise, lightly"),
          ("B03", "\"The meeting starts anyway\": dry, not alarmed. The chair and voices are a metaphor; say it lightly"),
          ("B05", "the four limits are quick and parallel; let \"Four out of four\" land before \"Enter a full position\""),
          ("B07", "**changed, and the reversal.** \"Now they disagree.\" then the numbers calmly; \"Nobody has made a mistake\" is warm, not defensive"),
          ("B08", "\"looks exactly like\": a plain observation about the briefing, not a complaint"),
          ("B09", "**the turn, and it is mine.** \"Here's where I got something wrong\" said lightly, then the fix, plain and quick; no flourish"),
          ("B10", "plain and honest; \"on purpose\" without a flourish"),
          ("B11", "**changed:** a real question, unhurried, three short questions each with its own breath; then a good answer and a weak one, the weak one with a small smile")]
out = ["# READ-ALOUD: Gate P sheet (work video)", "",
       "*Minutes of the Meeting* (working title) · structure: MINUTES OF ONE MEETING · voice `am_onyx`", "",
       "Generated from `SCRIPT.md` by `make_read_sheet.py`. Read each beat aloud at speaking pace, top to bottom, in one",
       "sitting; tick or note; skim the *on screen* line too. **Draft 2:** draft 1 was signed; only B02, B07, B09 and B11 changed (marked below).",
       "Re-read those four; the other eight are unchanged. Reply **\"Gate P PASS\"** or list the beats that tripped you.", "",
       "## Say-it-right checklist (Kokoro's phonemes, checked 2026-10-17)", "",
       "| Word | Should sound like | Kokoro alone | Override | Where |", "|---|---|---|---|---|"]
out += [f"| {a} | {b} | `{c}` | `{d}` | {e} |" for a, b, c, d, e in EAR]
out += ["", "## Where to listen hardest", ""] + [f"- **{b}**: {n}" for b, n in LISTEN] + ["", "## The script", ""]
t, total = 0.0, 0
for bid, title, text, screen in beats:
    w = len(text.split()); total += w
    mark = "  ← CHANGED, please re-read" if bid in RE_READ else ""
    out += [f"### [{int(t // 60)}:{int(t % 60):02d}] {bid} · {title}{mark}", "", text, "",
            f"<sub>**On screen:** {screen.strip()}</sub>", "", "> ☐ reads cleanly   ☐ note: ______________________", ""]
    t += w / 3.3
out += [f"_{len(beats)} beats · {total} words · about {int(t // 60)}:{int(t % 60):02d} at 3.3 words/s, before holds._", ""]
(HERE / "READ-ALOUD.md").write_text("\n".join(out))
print(f"READ-ALOUD.md · {len(beats)} beats · {total} words")
