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
words = sum(len(b["text"].split()) for b in lines); est = words / 3.4   # measured Kokoro pace with whole-beat synthesis (about 3.4 words a second in narration)
out = ["# READ-ALOUD: Gate P sheet, the Short", "",
 "*Who Fills the Blank?* (working title) · 9:16 · voice `am_onyx` · trailer for *Minutes of the Meeting: What an AI Is Handed*", "",
 "Generated from `short/SHORT-SCRIPT.md` by `make_read_sheet_short.py`. Its own script, written fresh for a viewer who never sees the long film.",
 "Read it aloud, top to bottom, in one sitting, then reply **\"Short Gate P PASS\"** or list the lines that tripped you.", "",
 f"**Size:** {len(lines)} lines, {words} words, about {est:.0f} s at the measured whole-beat pace (about 3.4 words a second), plus the gaps between lines.", "",
 "**The shape: ONE BLANK THAT GETS FILLED.** One scene, never cut: the last line an AI is handed has a blank where the verdict goes; three voices disagree about one invented stock, a chair weighs them, and the answer is written into the blank; the meeting folds into the minutes the AI actually gets, with that line at its foot; four previews of the full film gather around that sheet; then they recede, the verdict dissolves back to a blank and the loop closes.", "",
 "## Does it carry its own context? (the thing to judge)", "",
 "| A first-time viewer needs | Where | How the Short gives it |", "|---|---|---|",
 "| The question | S01 | an AI is told its answer must match a blank; who fills it in? |",
 "| Who is speaking, and what this is | S02 | Tanmay Kulkarni, for Humanitarians AI; an open-source finance pipeline; three voices; one invented stock |",
 "| The surprise | S03 | the three voices disagree: strong sell, enter a full position, a fragile stability |",
 "| The answer | S04 | a chair weighs them, 45, 35, 20; two point one seven out of five; a sell; the blank fills |",
 "| Why it matters | S05 | the AI never hears the meeting; it gets about 470 words of minutes ending in that line |",
 "| What to expect from the full film | S06 | one stock through the whole meeting, every figure from a file you can open; what the AI is handed and what the minutes do not say; the one place my own copy disagreed with the original, and how I caught it |",
 "| A real ending and a pointer | S07 | the viewer's question; the exact title of the full film; the loop closes |", "",
 "## Mechanical pass (`make_read_sheet_short.py`), already run", ""]
out += [f"- {i} {k}: {m}" for i, k, m in flags] or ["- 0 flags: no digits, no symbols or markup, no sentence over 28 words."]
out += ["", "## Say-it-right (Kokoro phonemes: as in the long film's `PHONEMES-CHECK.md`)", "",
 "- \"Tanmay Kulkarni\", \"point oh five\", \"forty-five\", \"summarises\": as in the long film. \"Minutes of the Meeting: What an AI Is Handed\": the film's own title, read plainly.", "",
 "## Where to listen hardest", "",
 "- **S01:** the pause before \"and then a blank\" should leave room for the blank; \"Who fills in the blank?\" is a real question.",
 "- **S03:** three short claims, each a little more surprised; \"fragile\" lands softly.",
 "- **S04:** \"That's a sell, and the blank fills in.\" is the landing: plain, no flourish.",
 "- **S06:** friendly and concrete, no hype; \"my own copy ... disagreed with the original\" is said plainly, as a fact.",
 "- **S07:** three questions, each with its own breath, then the title read like a title.", "",
 "## The script", ""]
t = 0.0
for b in lines:
    out += [f"### [{int(t // 60)}:{int(t % 60):02d}] {b['id']} · {b['title']}  _(tone: {b['tone']})_ · **{'SIGNED (unchanged)' if b['signed'] else 'RE-READ NEEDED (new wording)'}**", "", b["text"], "",
            f"<sub>**On screen:** {b['vis']}  ·  **Source line:** {b['src']}</sub>", "", "> ☐ reads cleanly   ☐ note: ______________________", ""]
    t += len(b["text"].split()) / 3.4 + 0.35
so = HERE / "short" / "GATE-P-SIGNOFF-SHORT.md"
out += ["## Sign-off", ""] + (so.read_text().splitlines() if so.exists() else ["- [ ] Short Gate P PASS (date, notes)"]) + [""]
(HERE / "short" / "READ-ALOUD-SHORT.md").write_text("\n".join(out))
print(len(lines), "lines", words, "words ~%d s;" % est, len(flags), "flags")
for f in flags: print(f)
