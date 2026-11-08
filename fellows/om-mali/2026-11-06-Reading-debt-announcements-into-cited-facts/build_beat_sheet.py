#!/usr/bin/env python3
"""
build_beat_sheet.py — AI Debt Tracker, WEEK 4: Reading debt announcements into cited facts.

Writes beat_sheet.json with EVERY on-screen figure injected from figdata.json. No number is
typed into a scene or into a beat sheet by hand.

THE FRAMING ASSERTION of this reel is B2_SHARE > READER_SHARE. The week's check, fixed in
the design in week 1, was that the event reader must beat B1's regex rules on field
accuracy. It did. But the baseline nobody planned to take seriously — one model call typing
every value itself — read MORE fields right than the reader did. The entire reel is built
on that gap: the reader cannot be sold on accuracy, only on provenance. If the reader ever
overtook B2, B03 and B04 would be arguing about something that no longer exists, and the
build fails rather than let the episode quietly become a victory lap.

THE SECOND ARGUMENT, asserted the same way: the fresh triage check FAILED. 8 of 9 is below
the 95% line that was written down before the run, while last week's set scores 24 of 24
because it is the set the fixes were made against. A reel that says "below my line" while
its arithmetic clears the line is lying in the other direction.

A THIRD assertion holds the reader's own cost. The reader reports more instruments that the
filing never announces than either baseline — 29 against 9 and 1. A frame that showed 94%
without that number beside it would be flattering the thing this episode is about.

A FOURTH ties the refusal tally together: the 8 currency rewrites and the 16 "null" strings
must be exactly the 24 refused, and the three copy outcomes must sum to every copy made.

THREE CLAIMS ARE NOT MEASURED in figdata.json. They come from narration_script.md,
FRICTIONAL.md and the project documents, are passed as named constants below, and every
screen that uses one says where it came from:
  · GATE_RECORD    — the week is recorded DELEGATED, not CLEARED; no person has reviewed it
  · LABELLER       — the labels and the truth are a model judgment, not a person's
  · CHECK_ORIGIN   — the check and the pass line were fixed in week 1, before any run

Usage:  python build_beat_sheet.py            (writes beat_sheet.json)
        python build_beat_sheet.py --check    (assertions only, writes nothing)
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIG = json.loads((HERE / "figdata.json").read_text(encoding="utf-8"))

RD = FIG["reader"]
GR = FIG["grounding"]
TR = FIG["triage"]
HC = FIG["handcheck"]
TC = FIG["truthcheck"]
RO = FIG["reader_defects_open"]

# ── derived, never typed ──────────────────────────────────────────────────────
METH = {m["key"]: m for m in RD["methods"]}
B1, READER, B2 = METH["b1"], METH["reader"], METH["b2"]
SHARE = {k: m["got"] / m["of"] for k, m in METH.items()}

COPIES = GR["copies"]
COPIES_TOTAL = sum(COPIES.values())
KINDS = GR["refused_kinds"]
CURRENCY = next(k for k in KINDS if k["hot"])

TROWS = {r["key"]: r for r in TR["rows"]}
T_FRESH, T_LAST = TROWS["fresh"], TROWS["last_week"]
T_FRESH_SHARE = T_FRESH["got"] / T_FRESH["of"]
T_LAST_SHARE = T_LAST["got"] / T_LAST["of"]

K_LAST, K_FRESH = HC["last_week"], HC["fresh"]
K_LAST_SHARE = K_LAST["got"] / K_LAST["of"]
K_FRESH_SHARE = K_FRESH["got"] / K_FRESH["of"]
DEFECTS = HC["defects"]

# ── assertions ────────────────────────────────────────────────────────────────
# THE FRAMING ASSERTION. The reel exists because of the order of these three numbers.
assert SHARE["b2"] > SHARE["reader"], (
    "B03/B04's whole claim: the reader passes the check it was set and STILL reads fewer "
    "fields right than one model call typing the values itself. If the reader ever "
    "overtook B2, this episode would be a different episode."
)
assert SHARE["reader"] > SHARE["b1"], (
    "and the check it was set — beat B1 — has to be a check it actually passes, or B03 is "
    "reporting a pass that did not happen"
)
assert SHARE["b2"] == 1.0 and B2["got"] == B2["of"], "B2 read every field right"

# THE THIRD. What the reader costs, asserted so it can never be dropped from the frame.
assert READER["extra"] > B2["extra"] > B1["extra"], (
    "94% only means something beside the 29 instruments the reader reports that the "
    "filings never announce — more than either baseline invents"
)
assert READER["of"] != B1["of"], (
    "the three bars do NOT share a denominator (135/160, 157/167, 160/160); every row "
    "prints its own fraction, and this assertion is what stops that becoming a footnote"
)
assert RD["composition"]["new_notes"] + RD["composition"]["other"] == RD["instruments"] == 66
assert RD["composition"]["new_notes"] > RD["composition"]["other"] * 10, (
    "B08's limit: these are mostly clean pricing documents, 62 of 66"
)
assert RD["docs"] == 24

# THE FOURTH. The refusal tally has to close, both ways.
assert COPIES_TOTAL == 254 and COPIES["in_cited"] > COPIES["refused"] > COPIES["in_other"]
assert sum(k["count"] for k in KINDS) == COPIES["refused"] == 24, (
    "B05 draws 24 cells and breaks them into 8 and 16; a breakdown that does not add up "
    "to the thing it breaks down is not a breakdown"
)
assert CURRENCY["count"] == 8 and CURRENCY["count"] < COPIES["refused"], (
    "eight OF the twenty-four — the currency bug is the real one, not all of them"
)
assert len([k for k in KINDS if k["hot"]]) == 1
assert GR["copied"] != GR["passage"][GR["passage"].find("€1,500,000,000"):][:14], (
    "B02 only works if the copy and the passage really do differ — the beat is one "
    "character wide"
)
assert "€" in GR["passage"] and "$" in GR["copied"], (
    "the € must be in the filing and the $ in the copy, or the frame has nothing to mark"
)

# THE SECOND ARGUMENT. This check FAILED, and the build holds it failed.
assert T_FRESH_SHARE < TR["pass_line"], (
    "B06 says 'below my line' on camera. If the fresh triage score ever cleared 95%, the "
    "beat would be announcing a failure that did not happen."
)
assert T_LAST_SHARE >= TR["pass_line"] and T_LAST_SHARE == 1.0, (
    "and last week's set clears it easily, which is exactly why it is drawn as a "
    "calibration rather than as evidence"
)
assert T_FRESH["of"] < 10, "nine positives is a small check, and B06 says so"
assert TR["labelled"] == 50 and TR["false_alarms"] == 4

# The answer key, same shape as week 3: a calibration above a measurement.
assert K_FRESH_SHARE < K_LAST_SHARE, (
    "3 of 3 is on the reports last week's fixes were made against; 1 of 5 is the one that "
    "was drawn before reading"
)
assert K_LAST["got"] == K_LAST["of"] == 3
assert K_FRESH["got"] == 1 and K_FRESH["of"] == 5
assert len(DEFECTS) == 4, "four new defects, and B07 names every one of them"
assert len({d["who"] for d in DEFECTS}) == len(DEFECTS), (
    "'each in a different company's tagging' — if two ever landed on one company the "
    "sentence would be wrong"
)
assert all(d["id"].startswith("P") for d in DEFECTS)

# The machine check on the labels. It is not a person, and it is not nothing.
assert TC["bonds"]["got"] == TC["bonds"]["of"] == 51
assert TC["principal"]["got"] == TC["principal"]["of"] == 19
assert TC["labeller"] == "Claude"

assert len(RO["items"]) == 3 and len(FIG["next"]) == 3

# ── the values figdata.json does not measure ──────────────────────────────────
NOT_IN_FIGDATA = "not in figdata.json — from narration_script.md, FRICTIONAL.md and the project documents"
GATE_RECORD = {
    "state": "DELEGATED",
    "not": "CLEARED",
    "where": "manifests/week4_gate.json",
    "note": "Handed to Claude end to end before it started. No person has reviewed the "
            "labels, the truth or the results, and the record also notes that the fresh "
            "triage check failed.",
}
LABELLER = {
    "who": TC["labeller"],
    "kind": "a model judgment, not a person's",
    "note": TC["labeller_note"],
}
CHECK_ORIGIN = {
    "what": "beat B1 on field accuracy",
    "when": RD["check_set_when"],
    "line": "the 95% triage line was fixed the same way",
}

HANDLE = "@HumanitariansAI"
SEGMENT = "Reading Debt Announcements into Cited Facts"
SLUG = "reading-debt-announcements-into-cited-facts"
KICKER = "Irreducibly Human"     # GATE L rule 7 — the FIXED claude-hai series name
GREETING = "Merhaba, HAI"        # Turkish. Never repeats a language; see metadata note.


def num(n):
    return f"{n:,}"


def pct0(x):
    return f"{x * 100:.0f}%"


def beat(bid, act, lane, text, est, shot, lead=None):
    b = {
        "beat_id": bid, "act": act, "lane": lane,
        "narration_text": text,
        "engine": "kokoro", "voice": "am_onyx",
        "estimated_duration_s": est,
    }
    if lead:
        b["lead_silence_s"] = lead
    b["shot"] = shot
    b["audio_file"] = f"mp3/beat-{bid}.mp3"
    return b


def remotion(pattern, provenance, props, motion, show, intent=None):
    shot = {"type": "GRAPHIC", "source": "remotion", "motion": motion}
    if intent:
        shot["visual_intent"] = intent
    shot["show"] = show
    shot["remotion"] = {"pattern": pattern, "provenance": provenance, "props": props}
    return shot


LOCAL = "reel-local/ReadingIntoCitedFacts"
beats = []

# ── B00 · COLD OPEN ───────────────────────────────────────────────────────────
beats.append(beat(
    "B00", "COLD OPEN", "BOOKEND",
    "Hi, I'm Om Mali. This video is about teaching my A I debt tracker to read a debt "
    "announcement into structured facts, where every number points back to the sentence it "
    "came from. This is week four of the A I Debt Tracker. It passed the check it was set. "
    "A simpler baseline still read more fields right.",
    19,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": GREETING,
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "Read every debt filing into structured bonds and loans. The model never types "
            "a number — it points at the words it read, and code parses them. Then show me "
            "what the pointing actually bought."
        ),
        "runningText": "reader_eval.py run — reader vs B1 vs B2…",
        "folderLabel": HANDLE,
        "modelLabel": "Opus 5",
        "effortLabel": "High",
        "output": [
            f"{READER['got']} of {READER['of']} fields right — {pct0(SHARE['reader'])} "
            f"against {pct0(SHARE['b1'])} for regex rules. The week's check passes.",
            f"but one model call typing the values itself read "
            f"{B2['got']} of {B2['of']} — the reader's gain is a cited sentence, not accuracy",
            f"{COPIES['refused']} copied values refused, {CURRENCY['count']} of them a "
            f"rewritten currency sign; and fresh triage found {T_FRESH['got']} of "
            f"{T_FRESH['of']}, below the {pct0(TR['pass_line'])} line",
        ],
    }, "type-on", [
        {"at": "on 'read a debt announcement into structured facts'", "event": "The ask types into the Claude composer."},
        {"at": "on 'a simpler baseline still read more fields right'", "event": "The result lands ANSWERED with three output lines."},
    ], intent="COLD OPEN LAW: the ask is the week itself. It lands ANSWERED, and the answer contains its own bad news — the pass and the baseline that beat it are on the same frame from the first beat."),
))

# ── B01 · THE READER ──────────────────────────────────────────────────────────
beats.append(beat(
    "B01", "THE READER", "REMOTION",
    "Last week the agent learned to find the debt news. This week it reads it. The rule "
    "from week one is that the model never types a number. So the reader works in three "
    "steps. Code picks the passages that state debt terms. The model lists each bond and "
    "copies the exact words for every value, naming the passage. Then code checks those "
    "words are really there, and parses the number.",
    22,
    remotion("W4Pipeline", LOCAL, {
        "sparkLine": "The model points. Code parses.",
        "eyebrow": "AI DEBT TRACKER · THE EVENT READER",
        "title": "Three steps, and the model is in the middle one",
        "subtitle": "Turning a debt filing into instruments: amount, currency, coupon, "
                    "due year, and what kind of event it is",
        "ruleLabel": "the rule, set in week 1",
        "rule": "The model never types a number.",
        "stages": [
            {"n": "1", "who": "CODE",
             "what": "picks out the passages that state debt terms", "hot": False},
            {"n": "2", "who": "THE MODEL",
             "what": "lists each bond and loan and, for every value, copies the exact "
                     "words and names the passage they came from", "hot": True},
            {"n": "3", "who": "CODE",
             "what": "checks those words really are in that passage, then parses the "
                     "number itself", "hot": False},
        ],
        "note": "The model is bracketed by code on both sides. It chooses what to point "
                "at; it never decides what a number is.",
        "source": "SOURCE: AI Debt Tracker docs/reader.md · DESIGN.md (the rule is from "
                  "week 1) · figdata.json",
    }, "stagger", [
        {"at": "on 'the model never types a number'", "event": "The rule lands above the three steps."},
        {"at": "per step", "event": "Code, then the model in the accent, then code again."},
    ], intent="A list of three steps STATES the rule. A code-model-code sandwich, with the model as the only accented card, shows it."),
))

# ── B02 · THE COPY CHECK, WORKED ──────────────────────────────────────────────
beats.append(beat(
    "B02", "THE COPY CHECK", "REMOTION",
    "And that check earned its place. For Alphabet's euro bonds, the model said it copied "
    "one and a half billion dollars. The filing says euros. It rewrote the currency sign "
    "while claiming to copy. Those words aren't in the passage, so the values were "
    "refused — missing, rather than wrong. That is the trade the design asked for.",
    19,
    remotion("W4Copy", LOCAL, {
        "sparkLine": "It rewrote the currency sign while claiming to copy.",
        "eyebrow": "AI DEBT TRACKER · THE COPY CHECK",
        "title": "Copy it, or it doesn't count",
        "subtitle": GR["rule"],
        "filingLabel": f"{GR['filing']} — passage {GR['passage_id']}",
        "passage": GR["passage"],
        "passageMark": "€1,500,000,000",
        "copiedLabel": "the model copies:",
        "copied": GR["copied"],
        "copiedMark": "$1,500,000,000",
        "verdict": f"{GR['verdict']}",
        "outcome": GR["outcome"],
        "note": GR["trade"],
        "source": "SOURCE: AI Debt Tracker docs/reader.md, week4/reader_reader.json · "
                  "figdata.json",
    }, "cite", [
        {"at": "on 'the filing says euros'", "event": "The euro amount lights in the passage."},
        {"at": "on 'rewrote the currency sign'", "event": "The dollar copy lights beneath it — one character apart."},
        {"at": "on 'refused'", "event": "REFUSED lands in the accent."},
    ], intent="One character is the whole beat, so one character is what the frame marks. The € in the filing and the $ in the copy are the only highlighted things on screen."),
))

# ── B03 · THE RESULT ──────────────────────────────────────────────────────────
beats.append(beat(
    "B03", "THE RESULT", "REMOTION",
    f"I tested it on twenty-four filings whose sixty-six bonds and loans were labelled "
    f"before anything ran. The week's check was simple: beat plain pattern matching. It "
    f"did — ninety-four percent of fields right against eighty-four. The denominators "
    f"differ, and the reader reported twenty-nine instruments the filings never announce. "
    f"But the third bar is the honest one. Asking the same model to type the numbers got "
    f"every field right.",
    23,
    remotion("W4Bakeoff", LOCAL, {
        "sparkLine": "It passed its check. The third bar is the honest one.",
        "eyebrow": "AI DEBT TRACKER · THE RESULT",
        "title": "Three ways to read a debt filing",
        "subtitle": f"Fields read right on {RD['docs']} filings, {RD['instruments']} "
                    f"instruments labelled before any run",
        "rows": [
            {"label": m["label"], "what": m["what"], "got": m["got"], "of": m["of"],
             "pct": pct0(SHARE[m["key"]]), "extra": m["extra"], "hot": m["hot"]}
            for m in RD["methods"]
        ],
        "extraLabel": "extra",
        "extraNote": f"Extra = {RD['extra_means']}. Counted in instruments, not fields — "
                     f"a second scale, which is why it is drawn past the divider.",
        "verdict": f"The week 4 check, fixed in the design in week 1, was to beat B1. The "
                   f"reader did: {READER['got']} of {READER['of']} fields against "
                   f"{B1['got']} of {B1['of']}. But B2 read {B2['got']} of {B2['of']}.",
        "note": f"Each bar has its own denominator. On clean pricing documents a small "
                f"model reads numbers well, so what the reader adds is not accuracy.",
        "source": "SOURCE: AI Debt Tracker docs/reader.md, manifests/reader_truth.json · "
                  "figdata.json",
    }, "grow", [
        {"at": "on 'beat plain pattern matching'", "event": "The B1 bar fills to 84%."},
        {"at": "on 'ninety-four percent'", "event": "The reader bar fills past it, in the accent."},
        {"at": "on 'the third bar is the honest one'", "event": "The B2 bar fills the whole track."},
    ], intent="Three bars, three different denominators, each printed. The extras sit past a divider on their OWN scale because they count instruments and the bars count fields."),
))

# ── B04 · WHAT POINTING BUYS ──────────────────────────────────────────────────
beats.append(beat(
    "B04", "WHAT POINTING BUYS", "REMOTION",
    "So what did pointing buy? Not accuracy. On clean pricing documents a small model reads "
    "numbers well. What the reader adds is a sentence behind every value — an id you can "
    "open and read. And it fails safe: when the model writes a number that isn't in the "
    "filing, the number is refused instead of used.",
    18,
    remotion("W4Cite", LOCAL, {
        "sparkLine": "The same number twice. Only one of them can be checked.",
        "eyebrow": "AI DEBT TRACKER · WHAT POINTING BUYS",
        "title": "Traceability, not accuracy",
        "subtitle": "The same value, read two ways — both of them right",
        "cards": [
            {"who": B2["label"], "method": B2["what"],
             "value": "€1,500,000,000", "chip": "",
             "evidence": "no sentence behind it — to check this number you have to go and "
                         "find the filing yourself",
             "hot": False},
            {"who": READER["label"], "method": READER["what"],
             "value": "€1,500,000,000", "chip": GR["passage_id"],
             "evidence": GR["passage"],
             "hot": True},
        ],
        "failSafeLabel": "and it fails safe",
        "failSafe": "When the model writes a number that is not in the filing, the value is "
                    "refused rather than used. Missing, not wrong.",
        "note": f"B2 read {B2['got']} of {B2['of']}, so this is a value it got right too. "
                f"It is the left-hand card that cannot be audited — not the one that was "
                f"wrong.",
        "source": "SOURCE: AI Debt Tracker docs/reader.md · narration_script.md notes · "
                  "figdata.json",
    }, "stagger", [
        {"at": "on 'not accuracy'", "event": "The bare value lands, correct and uncited."},
        {"at": "on 'a sentence behind every value'", "event": "The cited card lands beside it, with its passage id and the sentence."},
    ], intent="The honest comparison drawn as two cards. The left one is CORRECT; the point is that it cannot be audited. Nothing on this frame says the reader is more accurate, because it is not."),
))

# ── B05 · WHAT WAS REFUSED ────────────────────────────────────────────────────
beats.append(beat(
    "B05", "WHAT WAS REFUSED", "REMOTION",
    "Across the set, two hundred and twenty-seven copied values were found in the passage "
    "the model cited. Three turned up in a different passage. Twenty-four were refused. "
    "Eight of those were currency signs rewritten, like Alphabet's. The other sixteen were "
    "the model writing the word null — bookkeeping, with no effect on any score.",
    19,
    remotion("W4Refused", LOCAL, {
        "sparkLine": "Twenty-four refusals, and eight of them were real.",
        "eyebrow": "AI DEBT TRACKER · WHAT WAS REFUSED",
        "title": "Where every copied value landed",
        "subtitle": f"{num(COPIES_TOTAL)} copied values across {RD['docs']} filings",
        "tallyLabel": "every copy the model made",
        "tally": [
            {"label": "in the passage it cited", "count": COPIES["in_cited"], "hot": False},
            {"label": "in a different passage", "count": COPIES["in_other"], "hot": False},
            {"label": "refused", "count": COPIES["refused"], "hot": True},
        ],
        "cellsLabel": f"the {COPIES['refused']} refusals, one cell each",
        "kinds": [{"what": k["what"], "count": k["count"], "hot": k["hot"]} for k in KINDS],
        "trade": GR["trade"],
        "note": "",
        "source": "SOURCE: AI Debt Tracker docs/reader.md, week4/reader_reader.json · "
                  "figdata.json",
    }, "gather", [
        {"at": "on 'two hundred and twenty-seven'", "event": "The three counts land as plain figures."},
        {"at": "on 'twenty-four were refused'", "event": "24 cells fill in."},
        {"at": "on 'eight of those'", "event": "The 8 currency rewrites are the accented cells."},
    ], intent="24 of 254 is a 9% sliver on a proportional band and reads as a rendering fault. As 24 countable cells with 8 filled, both the tail and the real bug inside it are legible without scaling anything."),
))

# ── B06 · TRIAGE, FRESH ───────────────────────────────────────────────────────
beats.append(beat(
    "B06", "TRIAGE, FRESH", "REMOTION",
    "I also re-checked last week's triage on fifty new filings, labelled first. It found "
    "eight of nine — below my ninety-five percent line. That is a failed check and I am "
    "not dressing it up. The miss was an I B M prospectus whose cover leaves even the year "
    "blank. I logged it and didn't tune it away. Nine positives is a small check, and I "
    "say so.",
    21,
    remotion("W4Triage", LOCAL, {
        "sparkLine": "A check I set myself, and did not pass.",
        "eyebrow": "AI DEBT TRACKER · TRIAGE, CHECKED AGAIN",
        "title": "Triage, checked again on fresh filings",
        "subtitle": f"{TR['labelled']} new filings labelled before the run, after last "
                    f"week's two rule fixes",
        "rows": [
            {"label": T_FRESH["label"], "note": f"{pct0(T_FRESH_SHARE)} — below the line",
             "got": T_FRESH["got"], "of": T_FRESH["of"], "hot": True},
            {"label": T_LAST["label"], "note": "a calibration — the set the fixes were "
                                               "made against",
             "got": T_LAST["got"], "of": T_LAST["of"], "hot": False},
        ],
        "line": TR["pass_line"],
        "lineLabel": f"dashed = the {pct0(TR['pass_line'])} pass line, fixed in the design "
                     f"before the run — one rule, drawn through both tracks. Only "
                     f"{T_FRESH['of']} debt filings were in the draw.",
        "missLabel": "the one it missed",
        "missWho": f"{TR['miss']['who']}, {TR['miss']['doc']} — the cover reads",
        "missCover": TR["miss"]["cover"],
        "missWhy": f"{TR['miss']['why']}. Logged ({TR['miss']['defect']}), not tuned away. "
                   f"Of the {TR['false_alarms']} false alarms, one is probably a labelling "
                   f"error — {TR['false_alarm_note']['who']}: "
                   f"{TR['false_alarm_note']['what']}; {TR['false_alarm_note']['rule']}.",
        "note": "",
        "source": "SOURCE: AI Debt Tracker docs/triage.md, manifests/triage_labels_w4.json "
                  "· DESIGN.md P45–P46 · figdata.json",
    }, "narrow", [
        {"at": "on 'eight of nine'", "event": "The fresh bar fills and stops short of the dashed line."},
        {"at": "on 'below my ninety-five percent line'", "event": "Last week's bar fills past it — a calibration."},
        {"at": "on 'leaves even the year blank'", "event": "The blank cover lands, set as the cover reads."},
    ], intent="The pass line was written down before the run, so it is drawn through BOTH tracks rather than printed beside the number that misses it. The failure is the subject of the beat and takes the accent."),
))

# ── B07 · THE ANSWER KEY ──────────────────────────────────────────────────────
beats.append(beat(
    "B07", "THE ANSWER KEY", "REMOTION",
    "The answer key got the same treatment. Last week's three now agree, but those are the "
    "reports the fixes were made against. Five fresh reports, chosen before reading: one "
    "agreed. Four new defects, each in a different company's tagging — one Marvell bond "
    "tagged under two names, a range of years read as a single bond. All logged for next "
    "week.",
    19,
    remotion("W4Key", LOCAL, {
        "sparkLine": "One of five, and four defects with names on them.",
        "eyebrow": "AI DEBT TRACKER · THE ANSWER KEY",
        "title": "The answer key, on five more unread reports",
        "subtitle": "Printed debt tables against the key, graded once after last week's "
                    "two fixes",
        "calibrationLabel": f"{K_LAST['label']}: {K_LAST['got']} of {K_LAST['of']} "
                            f"{K_LAST['qualifier']}",
        "calibration": "— but that is the set the fixes were made against, so it is a "
                       "calibration, not a measurement.",
        "cellsLabel": f"{K_FRESH['of']} fresh reports, {HC['drawn_how']}",
        "agreed": K_FRESH["got"],
        "drawn": K_FRESH["of"],
        "agreedWho": f"{HC['agreed']['who']}: {HC['agreed']['what']}. {HC['left_open']}",
        "defectsLabel": f"{len(DEFECTS)} new defects, each in a different company's tagging",
        "defects": [{"who": d["who"], "what": d["what"], "id": d["id"]} for d in DEFECTS],
        "note": "One slip in the process, disclosed beside the result: the key's totals for "
                "these five reports were printed once before the transcriptions were "
                f"written. ({NOT_IN_FIGDATA})",
        "source": "SOURCE: AI Debt Tracker docs/handcheck.md, manifests/handcheck/ · "
                  "DESIGN.md P41–P44 · figdata.json",
    }, "stagger", [
        {"at": "on 'last week's three now agree'", "event": "The calibration line lands first, named as a calibration."},
        {"at": "on 'one agreed'", "event": "Five cells land; one of them is filled."},
        {"at": "per defect", "event": "Four companies, four defects, four ids."},
    ], intent="'One of five' as a bar is a rectangle at 20%. As five cells it is five reports, four of which get a name and a defect id someone can look up next week."),
))

# ── B08 · THE LIMITS ──────────────────────────────────────────────────────────
beats.append(beat(
    "B08", "THE LIMITS", "REMOTION",
    "The limits. Ninety-four percent is on twenty-four filings that are mostly clean "
    "pricing documents — sixty-two of the sixty-six instruments were new notes. The labels "
    "are Claude's reading, machine-checked but not read by a person. And the week's gate "
    "says delegated, not cleared: I handed the whole week to Claude and have not reviewed "
    "any of it. Next week connects the reader to a ledger.",
    22,
    remotion("W4Limits", LOCAL, {
        "sparkLine": "What the week does not show.",
        "eyebrow": "AI DEBT TRACKER · THE LIMITS",
        "title": "Every number above, and the limit that narrows it",
        "subtitle": "",
        "rows": [
            {"claim": f"{pct0(SHARE['reader'])} of fields",
             "limit": f"on {RD['docs']} filings where "
                      f"{RD['composition']['new_notes']} of {RD['instruments']} instruments "
                      f"were new notes in pricing documents. "
                      f"{RD['composition']['other']} were "
                      f"{RD['composition']['other_what']}. Whether it holds on harder "
                      f"documents is not known.",
             "hot": True},
            {"claim": "it beat B1",
             "limit": f"which is the check the design set in week 1 — and "
                      f"{B2['label']} read {B2['got']} of {B2['of']}. Passing the check a "
                      f"week was set is not the same as being the best option measured "
                      f"that week.",
             "hot": False},
            {"claim": f"{RD['instruments']} labelled instruments",
             "limit": f"{LABELLER['kind']} — {LABELLER['who']} read each filing. "
                      f"Machine-checked: all {TC['bonds']['got']} of "
                      f"{TC['bonds']['of']} labelled new bonds appear in the next quarterly "
                      f"report with the same coupon and year. No person has read them.",
             "hot": False},
            {"claim": f"{T_FRESH['got']} of {T_FRESH['of']} on fresh triage",
             "limit": f"a failed check on {T_FRESH['of']} positives — too few to tell a "
                      f"rule problem from a draw. Whether triage reaches "
                      f"{pct0(TR['pass_line'])} once {TR['miss']['defect']} is fixed needs "
                      f"a third fresh check.",
             "hot": False},
            {"claim": "the reader's own defects",
             "limit": f"{len(RO['items'])} are open and unfixed on purpose. "
                      f"{RO['why_open']}",
             "hot": False},
        ],
        "gateLabel": "the week's gate record",
        "gateState": f"{GATE_RECORD['state']}, not {GATE_RECORD['not']}",
        "gateNote": f"{GATE_RECORD['note']} ({NOT_IN_FIGDATA}; {GATE_RECORD['where']})",
        "nextLabel": "next",
        "next": FIG["next"],
        "source": "SOURCE: narration_script.md notes · FRICTIONAL.md · docs/reader.md · "
                  "DESIGN.md §17 · figdata.json",
    }, "stagger", [
        {"at": "per limit", "event": "Each claim lands with the limit that narrows it."},
        {"at": "on 'delegated, not cleared'", "event": "The gate record lands as the largest object on the frame."},
        {"at": "on 'next week'", "event": "Three next steps land at the foot."},
    ], intent="Every episode in this series ends on its own limits. This week the gate record is one of them and it is drawn largest, because 'nobody has checked any of this' outranks every number above it."),
))

# ── B09 · VERDICT ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B09", "VERDICT", "BOOKEND",
    "So: an event reader where code picks the passages, the model points at words, and code "
    "parses the numbers. Ninety-four percent of fields right against eighty-four for regex "
    "rules — it passes. One model call typing the values read all of them. Twenty-four "
    "copies refused, eight of them rewritten currency signs. Fresh triage failed at eight "
    "of nine, the answer key agreed on one of five, and nobody has reviewed any of it.",
    28,
    remotion("ClaudeVerdictArtifact", "proven-core/ClaudeVerdictArtifact", {
        "artifactTitle": SEGMENT,
        "artifactHeading": "What week 4 built, and what it is allowed to claim",
        "artifactLines": [
            f"An event reader in three steps: code picks the passages that state debt "
            f"terms, the model lists each instrument and copies the exact words for every "
            f"value, and code checks the words are really there before parsing the number. "
            f"The model never types a number.",
            f"On {RD['docs']} filings whose {RD['instruments']} instruments were labelled "
            f"before any run, it read {READER['got']} of {READER['of']} fields right "
            f"({pct0(SHARE['reader'])}) against {B1['got']} of {B1['of']} "
            f"({pct0(SHARE['b1'])}) for regex rules. That was the week's check, and it "
            f"passes.",
            f"{B2['label']} — the model typing every value itself — read {B2['got']} of "
            f"{B2['of']}. The reader's gain is a cited sentence behind every value, not "
            f"accuracy. It also reported {READER['extra']} instruments the filings do not "
            f"announce, against {B2['extra']} and {B1['extra']}.",
            f"The copy check refused {COPIES['refused']} of {num(COPIES_TOTAL)} copied "
            f"values: {CURRENCY['count']} were currency signs the model rewrote while "
            f"claiming to copy, {KINDS[1]['count']} were the word \"null\". A refused value "
            f"is missing, not wrong.",
            f"Fresh triage found {T_FRESH['got']} of {T_FRESH['of']} — below the "
            f"{pct0(TR['pass_line'])} line, logged as {TR['miss']['defect']} and not tuned "
            f"away. The answer key agreed on {K_FRESH['got']} of {K_FRESH['of']} fresh "
            f"reports with {len(DEFECTS)} new defects. The gate records the week "
            f"{GATE_RECORD['state']}, not {GATE_RECORD['not']}.",
        ],
    }, "stagger", [
        {"at": "per clause", "event": "Five findings stagger in, one per spoken clause."},
    ], intent="Judgment beat. The artifact page is the point (ILLUSTRATE LAW carve-out). Two of the five findings are failures, and they are not last."),
))

# ── B10 · HANDOFF ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B10", "HANDOFF", "BOOKEND",
    "Your turn. Paste this into Claude. Before you build the clever version, run the stupid "
    "one. Mine beat the baseline it was measured against and lost to the one it wasn't. If "
    "your system is more complicated, be able to say what the complication buys.",
    15,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": "Your turn.",
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "Before I build the structured, grounded version of this, write and run the "
            "dumbest baseline that could possibly work — one call, no scaffolding. Score "
            "both on the same labelled set and show me the denominators. Then tell me in "
            "one sentence what my complicated version buys that the simple one does not, "
            "and if the answer is \"nothing I measured\", say that instead."
        ),
        "runningText": "paste this into Claude…",
        "folderLabel": HANDLE,
        "modelLabel": "Opus 5",
        "effortLabel": "High",
        "output": [],
    }, "type-on", [
        {"at": "on 'paste this into Claude'", "event": "The prompt types into the composer."},
    ], intent="HANDOFF LAW: a real prompt, read ALOUD verbatim and then discussed. One of exactly two typing beats. It is the lesson of this week turned into something a viewer can run."),
))

# ── B11 · OUTRO ───────────────────────────────────────────────────────────────
beats.append(beat(
    "B11", "OUTRO", "BOOKEND",
    "Reading debt announcements into cited facts. Week four of the A I Debt Tracker. Om "
    "Mali, for Humanitarians A I.",
    9,
    remotion("ClaudeTitleOutro", "proven-core/ClaudeTitleOutro", {
        "title": SEGMENT,
        "handle": HANDLE,
        # `subline`, not `subtitle` — the wrong name ships the outro reading
        # "bot vs bot, season one", a default from an unrelated show.
        "subline": "week 4 · the AI Debt Tracker",
    }, "fade", [
        {"at": "on the title", "event": "Title restate, poster-style."},
    ], intent="OUTRO LAW: title restate, handle, nothing that moves."),
))

META = {
    "title": SEGMENT,
    "slug": SLUG,
    "topic": KICKER,
    "topic_note": "Slot-1 kicker is the FIXED claude-hai series name (runtime/qc/brand_labels.json, GATE L rule 7) — never a per-video guess.",
    "register": "Pragmatist",
    "audience": "Humanitarians AI",
    "brand": "claude-hai",
    "engine": "kokoro",
    "voice_kokoro": "am_onyx",
    "voice_policy": "persistent-fellow-selected",
    "voice_approval": "APPROVED",
    "palette": "claude",
    "style_preset": "claude",
    "ground": "#FAF9F5",
    "greeting": GREETING,
    "greeting_note": "hello lexicon: Turkish. HAI persona takes only the shortest cues (Hi · Ola · Hej · Ciao · Hallo · Salut · Ahoj · Szia · Tere · Moi · Hoi · Labas · Salve · Sveiki · Zdravo · Merhaba). Rotate; never repeat a language.",
    "aspect_ratio": "16:9",
    "fps": 24,
    "lead_silence_s": 0.4,
    "note": (
        "ai-explainer / claude-hai. AI Debt Tracker WEEK 4. ILLUSTRATE LAW: the Claude UI "
        "appears at B00 (cold open, answered), B09 (verdict artifact), B10 (handoff) and "
        "B11 (outro) only — every body beat illustrates its concept as a native animated "
        "Remotion scene (REBUILD LAW). The four source PNGs and their SVG sources are "
        "REFERENCE in pantry/, never slotted as media. The script's five body sections "
        "become eight body beats: 0:15 splits into the pipeline (B01) and the worked copy "
        "check (B02); 0:45 splits into the bake-off (B03) and what pointing actually buys "
        "(B04); 1:20's tally becomes B05; and the closing on-camera section becomes a "
        "limits beat. FIVE THINGS NOT TO GET WRONG: the reader is NOT more accurate — B2 "
        "read every field right and the reel says so on four separate frames; the three "
        "bars do not share a denominator; the reader invents more instruments than either "
        "baseline; the fresh triage check FAILED; and the week's gate records DELEGATED, "
        "not cleared — no person has reviewed any of it."
    ),
}

sheet = {"metadata": META, "beats": beats}

body = [b for b in beats if b["beat_id"] not in ("B00", "B09", "B10", "B11")]
words = {b["beat_id"]: len(b["narration_text"].split()) for b in beats}
lo = min(words[b["beat_id"]] for b in body)
hi = max(words[b["beat_id"]] for b in body)
# 45-72, the band weeks 2 and 3 settled on. This script spells its numbers aloud
# ("two hundred and twenty-seven", "eight of nine"), and one figure can cost six words;
# tightening the band would mean cutting evidence to pay for pronunciation.
assert 45 <= lo and hi <= 72, f"body beat word budget 45-72 violated: {lo}-{hi}"
assert len(body) == 8 and len(beats) == 12

if "--check" in sys.argv:
    print("[adt-w4] all assertions pass")
    sys.exit(0)

out = HERE / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"[adt-w4] wrote {out}  — {len(beats)} beats")
print("[adt-w4] narration words: " + " ".join(f"{k}={v}" for k, v in words.items()))
print(f"[adt-w4] body beats {lo}-{hi}w (band 45-72), total {sum(words.values())}w")
print(f"[adt-w4] derived: reader {READER['got']}/{READER['of']} ({pct0(SHARE['reader'])}) "
      f"beats B1 {B1['got']}/{B1['of']} ({pct0(SHARE['b1'])}) and LOSES to B2 "
      f"{B2['got']}/{B2['of']} ({pct0(SHARE['b2'])}) · extras "
      f"{B1['extra']}/{READER['extra']}/{B2['extra']} · copies {num(COPIES_TOTAL)} = "
      f"{COPIES['in_cited']}+{COPIES['in_other']}+{COPIES['refused']} "
      f"({CURRENCY['count']} currency + {KINDS[1]['count']} null) · triage fresh "
      f"{T_FRESH['got']}/{T_FRESH['of']} = {pct0(T_FRESH_SHARE)} BELOW "
      f"{pct0(TR['pass_line'])} · key {K_FRESH['got']}/{K_FRESH['of']} + "
      f"{len(DEFECTS)} defects · gate {GATE_RECORD['state']}")
