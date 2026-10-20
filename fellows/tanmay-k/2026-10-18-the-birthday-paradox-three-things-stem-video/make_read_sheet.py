#!/usr/bin/env python3
"""Build READ-ALOUD.md (Gate P sheet) from BEATS-DRAFT.md, plus a mechanical pass.
Marks each beat SIGNED (narration identical to the Gate-P-signed draft 1) or RE-READ NEEDED.
Not Gate P itself: a human reads every line aloud and signs."""
import re, os
HEAD = re.compile(r"^\*\*(B\d+\w*) · ([^·]+?) · ~(\d+) s( \+ (\d+) s hold)?\*\* \(tone: ([^)]*)\)", re.M)

def parse(path):
    src = open(path).read(); ms = list(HEAD.finditer(src)); out = []
    for i, m in enumerate(ms):
        blk = src[m.end(): ms[i + 1].start() if i + 1 < len(ms) else len(src)]
        narr = " ".join(l[2:].strip() for l in blk.splitlines() if l.startswith("> "))
        g = lambda tag: next((l[len(tag):].strip().rstrip("*") for l in blk.splitlines() if l.startswith(tag)), "")
        out.append(dict(id=m.group(1), title=m.group(2).strip(), sec=int(m.group(3)), hold=int(m.group(5) or 0),
                        tone=m.group(6), text=narr, vis=g("*Visual:*"), src=g("*Source:*")))
    return out

beats = parse("BEATS-DRAFT.md")
signed_txt = set()
if os.path.exists("BEATS-DRAFT-v1-gateP-signed.md"):
    signed_txt = {b["text"] for b in parse("BEATS-DRAFT-v1-gateP-signed.md") if "first test changed" not in b["text"]}
for b in beats: b["signed"] = b["text"] in signed_txt

NUM = set("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred point".split())
flags = []
for b in beats:
    t = b["text"]
    if re.search(r"\d", t): flags.append((b["id"], "DIGIT", "digits in narration"))
    if re.search(r"[%&/=*_#<>\[\]()—–√×]", t): flags.append((b["id"], "SYMBOL", "symbol/markup in narration"))
    for s in re.split(r"(?<=[.?!])\s+", t):
        if len(s.split()) > 28: flags.append((b["id"], "BREATH", f"{len(s.split())}-word sentence: {s[:60]}..."))
    run = best = 0
    for w in re.findall(r"[a-z]+", t.lower()):
        run = run + 1 if w in NUM else 0; best = max(best, run)
    if best >= 6: flags.append((b["id"], "DIGIT-CHAIN", f"{best} number-words in a row"))
words = sum(len(b["text"].split()) for b in beats)
secs = words / 3.3 + sum(b["hold"] for b in beats)
n_signed = sum(b["signed"] for b in beats)
out = ["# READ-ALOUD: Gate P sheet", "",
 "*The Birthday Paradox: Three Things You Could Change* (working title) · form: THREE CHANGES, ONE RULE · voice `am_onyx`", "",
 "Generated from `BEATS-DRAFT.md` (draft 2) by `make_read_sheet.py`. If the narration changes, this sheet is regenerated and the changed beats need a fresh read.", "",
 "**How to run Gate P:** read each beat out loud at speaking pace, top to bottom, in one sitting. Listen for rhythm, emphasis, and whether each turn lands. Tick the box or write a note. Also skim the *on screen* and *source* lines under each beat. Then reply **\"Gate P PASS\"** (with any notes) or list the beats that tripped you.", "",
 "**What a page can't show:** the three chapter cards (PEOPLE, EVENNESS, DAYS) stay on screen as an index. Peaks are **B07** (quietly surprised) and **B09** (struck); B08 and B14 pull back after them. **B16 has an 8 second silent hold**: when you reach it, *do the task* (work out the answer with the rule) before reading B17. That is the only honest way to judge it.", "",
 "**No slates yet.** The calendar grid, dots, counter and cards are not built, so this is a read-aloud Gate P. Visuals are reviewed as rendered stills at the next stage, before any audio.", "",
 f"**Size:** {len(beats)} beats, {words} narration words, about {secs/60:.1f} min at 3.3 w/s including the 8 s hold.", "",
 f"**Sign-off status vs draft 1:** {n_signed} of {len(beats)} beats are word-for-word identical to the text read for the first Gate P; the other {len(beats)-n_signed} are new or reworded and need a read. Each beat below is marked.", "",
 "## Mechanical pass (`make_read_sheet.py`), already run", ""]
out += [f"- {i} {k}: {m}" for i, k, m in flags] or ["- 0 flags: no digits, no symbols or markup, no sentence over 28 words, no long number-word chains."]
out += ["", "## Say-it-right checklist (to confirm by ear before audio)", "",
 "Kokoro's phonemes are not yet checked for this film. Read these the way you would say them and flag any that need an override:", "",
 "| Where | Word | Say it as |", "|---|---|---|",
 "| B02, B18 | Tanmay Kulkarni | your own pronunciation |",
 "| B06 | National Center for Health Statistics, Social Security Administration | spelled out, no acronyms |",
 "| B06 | February twenty ninth | \"February twenty-ninth\" |",
 "| B11 | fortnight | \"FORT-night\" |",
 "| B13, B15, B17 | \"times one point two, plus a half\" | check \"one point two\" and \"a half\" are clear in the ear |",
 "| All | percent figures | \"fifty point seven percent\": check the unit is audible each time (unit-drop hazard) |", "",
 "## Beats", ""]
for b in beats:
    status = "SIGNED (unchanged since first Gate P)" if b["signed"] else "RE-READ NEEDED (new or reworded)"
    hold = f" + {b['hold']} s hold" if b["hold"] else ""
    out += [f"### {b['id']} · {b['title']} · ~{b['sec']} s{hold}", f"*tone: {b['tone']}* · **{status}**", "", f"> {b['text']}", ""]
    if b["vis"]: out += [f"*on screen:* {b['vis']}", ""]
    if b["src"]: out += [f"*source line:* {b['src']}", ""]
    out += ["- [ ] reads clean  - [ ] turn lands  - notes:", ""]
out += ["## Sign-off", ""] + (open("GATE-P-SIGNOFF.md").read().splitlines() if os.path.exists("GATE-P-SIGNOFF.md") else ["- [ ] Gate P PASS (date, notes)"]) + [""]
open("READ-ALOUD.md", "w").write("\n".join(out))
print(len(beats), "beats", words, "words", f"{secs/60:.1f} min;", len(flags), "flags;", n_signed, "signed")
for f in flags: print(f)
