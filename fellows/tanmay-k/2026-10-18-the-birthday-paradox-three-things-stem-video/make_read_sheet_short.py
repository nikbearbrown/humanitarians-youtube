#!/usr/bin/env python3
"""READ-ALOUD-SHORT.md (Gate P sheet for the Short) from short/SHORT-SCRIPT.md, plus a mechanical pass.
Not Gate P itself: a human reads every line aloud and signs."""
import json, os, re
from pathlib import Path
HERE = Path(__file__).parent
HEAD = re.compile(r"^### (S\d+) · ([^·]+?) · ~(\d+) s \(tone: ([^)]*)\)", re.M)
src = (HERE / "short" / "SHORT-SCRIPT.md").read_text(); ms = list(HEAD.finditer(src)); lines = []
for i, m in enumerate(ms):
    blk = src[m.end(): ms[i + 1].start() if i + 1 < len(ms) else len(src)]
    g = lambda tag: next((l[len(tag):].strip().rstrip("*") for l in blk.splitlines() if l.startswith(tag)), "")
    lines.append(dict(id=m.group(1), title=m.group(2).strip(), sec=int(m.group(3)), tone=m.group(4),
                      text=" ".join(l[2:].strip() for l in blk.splitlines() if l.startswith("> ")), vis=g("*On screen:*"), src=g("*Source:*")))
signed = json.loads((HERE / "short" / "SIGNED-NARRATION.json").read_text()) if (HERE / "short" / "SIGNED-NARRATION.json").exists() else {}
for b in lines: b["signed"] = signed.get(b["id"]) == b["text"]
flags = []
for b in lines:
    t = b["text"]
    if re.search(r"\d", t): flags.append((b["id"], "DIGIT", "digits in narration"))
    if re.search(r"[%&/=*_#<>\[\]()—–√×]", t): flags.append((b["id"], "SYMBOL", "symbol/markup"))
    for s in re.split(r"(?<=[.?!])\s+", t):
        if len(s.split()) > 28: flags.append((b["id"], "BREATH", f"{len(s.split())}-word sentence: {s[:50]}..."))
words = sum(len(b["text"].split()) for b in lines); est = words / 2.27   # measured Kokoro pace in the long film (about 2.3 words a second)
out = ["# READ-ALOUD: Gate P sheet, the Short", "",
 "*Take Away Days* (working title) · 9:16 · voice `am_onyx` · trailer for *The Birthday Paradox: Three Things You Could Change*", "",
 "Generated from `short/SHORT-SCRIPT.md` by `make_read_sheet_short.py`. Its own script, written fresh for a viewer who never sees the long film.",
 "Read it aloud, top to bottom, in one sitting, then reply **\"Short Gate P PASS\"** or list the lines that tripped you.", "",
 f"**Size:** {len(lines)} lines, {words} words, about {est:.0f} s at the long film's measured pace (about 2.3 words a second), plus a short end card.", "",
 "**The shape: ONE GRID THAT SQUEEZES.** One scene, never cut: a calendar holds 23 dots, the narration takes days away and the calendar narrows around the same dots while the odds climb, then widens again and the loop closes where it opened (a year, twenty three people). It is not long-film beats cut down.", "",
 "## Does it carry its own context? (the thing to judge)", "",
 "| A first-time viewer needs | Where | How the Short gives it |", "|---|---|---|",
 "| Who is speaking | S01, S07 | Tanmay Kulkarni, for Humanitarians AI at the start; the channel named again at the end |",
 "| The claim | S01–S02 | 23 people, a bet that two share a birthday, you'd lose about half the time |",
 "| The surprise | S03 | same group size, fewer days: ninety five percent at ninety days, almost certain at a month |",
 "| Why | S04 | not the people, not uneven birthdays (a tenth of a point), the number of days |",
 "| A rule they can keep | S05–S06 | square root of the days, times 1.2, plus a half: a year needs 23 people, a month needs 7 |",
 "| A real ending | S07 | the loop closes: \"That's why it's twenty three\", then the pointer to the full video |", "",
 "## Mechanical pass (`make_read_sheet_short.py`), already run", ""]
out += [f"- {i} {k}: {m}" for i, k, m in flags] or ["- 0 flags: no digits, no symbols or markup, no sentence over 28 words."]
out += ["", "## Say-it-right (Kokoro phonemes checked for the long film; same overrides, none needed)", "",
 "- \"Tanmay Kulkarni\", \"one point two\", \"a half\", the percent figures: as in `PHONEMES-CHECK.md` of the long film.", "",
 "## Where to listen hardest", "",
 "- **S03:** the climb from \"ninety five percent\" to \"almost certain\" should sound like a surprise, not a list.",
 "- **S04:** \"Not the people, we kept them. Not uneven birthdays…\" should sound like elimination, ending on \"It's how many days there are.\"",
 "- **S06:** \"A year needs twenty three people. One month needs seven.\" Two short statements, the second quieter.", "",
 "## The script", ""]
t = 0.0
for b in lines:
    out += [f"### [{int(t // 60)}:{int(t % 60):02d}] {b['id']} · {b['title']}  _(tone: {b['tone']})_ · **{'SIGNED (unchanged)' if b['signed'] else 'RE-READ NEEDED (new wording)'}**", "", b["text"], "",
            f"<sub>**On screen:** {b['vis']}  ·  **Source line:** {b['src']}</sub>", "", "> ☐ reads cleanly   ☐ note: ______________________", ""]
    t += len(b["text"].split()) / 2.27 + 0.4
so = HERE / "short" / "GATE-P-SIGNOFF-SHORT.md"
out += ["## Sign-off", ""] + (so.read_text().splitlines() if so.exists() else ["- [ ] Short Gate P PASS (date, notes)"]) + [""]
(HERE / "short" / "READ-ALOUD-SHORT.md").write_text("\n".join(out))
print(len(lines), "lines", words, "words ~%d s;" % est, len(flags), "flags")
for f in flags: print(f)
