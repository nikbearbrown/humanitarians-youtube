#!/usr/bin/env python3
"""
build_beat_sheet.py — AI Debt Tracker, WEEK 6: Reading the opening ledger instead of
borrowing it.

Writes beat_sheet.json with EVERY on-screen figure injected from figdata.json. No number is
typed into a scene or into a beat sheet by hand.

THE FRAMING ASSERTION of this reel is that REMOVING THE CRUTCH REMOVES THE CLAIM. Week 5
reported +7.0 points of recall over doing nothing. That number depended on every quarter
being handed an opening ledger taken from the answer key. This week the tracker reads that
ledger itself, and recall falls 7.9 points — to 90.1%, against the do-nothing baseline's
90.9%. The advantage over doing nothing was the borrowed ledger. The build asserts both
halves: oracle start must beat B0 on recall AND agent start must not. If agent start ever
pulled ahead of B0 on recall, this would be a different episode and B05 would be announcing
a loss that did not happen.

THE SECOND ARGUMENT, asserted the same way: precision moves the OTHER way. Agent start is
ahead of both oracle start and B0 on precision, because fewer bonds held means fewer held
wrongly. A reel that showed only the recall fall would be describing a failure; a reel that
showed only the precision rise would be describing a win. It is a trade, and both halves are
on the frame.

A THIRD holds the merge result honest. The wrong additions fell 26 -> 3 and precision rose
90.2% -> 93.3%, which is 0.5 points above B0 with a paired interval of -0.2 to +1.4. The
build asserts that the gain over B0 is SMALL, so the frame has to say "level" and can never
drift into "better".

A FOURTH holds the opening reader's own claim: the model buys RECALL, not precision. Its
recall gain over rules-only must exceed its precision gain, or B03's verdict line is wrong.
And the denominators must stay honest — 94 reports were read, 43 are what the percentages
are graded on, and the frame prints both.

A FIFTH holds the variance beat: the same report, asked twice, must give two DIFFERENT
counts, or B04 has nothing to show.

THREE CLAIMS ARE NOT MEASURED in figdata.json. They come from narration_script.md,
FRICTIONAL.md and the project documents, are passed as named constants below, and every
screen that uses one says where it came from:
  · GATE_RECORD    — the week is recorded DELEGATED, not CLEARED; no person has reviewed it
  · JUDGMENTS      — which rows are instruments is qwen3:4b's judgment, not a person's
  · ORACLE_WAS     — the borrowed start was a deliberate ablation (A4), not an oversight

Usage:  python build_beat_sheet.py            (writes beat_sheet.json)
        python build_beat_sheet.py --check    (assertions only, writes nothing)
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIG = json.loads((HERE / "figdata.json").read_text(encoding="utf-8"))

MG = FIG["merge"]
OP = FIG["opening"]
SC = FIG["score"]
VR = FIG["variance"]
GP = FIG["gap"]
WH = FIG["where"]
CA = FIG["catch"]
LM = FIG["limits"]
TC = FIG["truthcheck"]

# ── derived, never typed ──────────────────────────────────────────────────────
PREC = MG["precision"]
START = {s["key"]: s for s in GP["starts"]}
ORACLE, AGENT, B0 = START["oracle"], START["agent"], START["b0"]
SMET = {m["key"]: m for m in SC["metrics"]}
S_REC, S_PRE = SMET["recall"], SMET["precision"]
RUNS = VR["runs"]
R1, R2 = RUNS[0], RUNS[1]
WRONG, RIGHT = CA["wrong"], CA["right"]
Q = CA["questions"]
TD = LM["total_debt"]

WRONG_SHARE = WRONG["got"] / WRONG["of"]
RIGHT_SHARE = RIGHT["got"] / RIGHT["of"]

# ── assertions ────────────────────────────────────────────────────────────────
# THE FRAMING ASSERTION, in two halves. The reel exists because of the gap between them.
assert ORACLE["recall"] > B0["recall"], (
    "week 5's headline: borrowing the opening ledger put recall 7 points above doing "
    "nothing. If that were not true there would be no crutch to remove."
)
assert AGENT["recall"] <= B0["recall"], (
    "and the whole point of week 6: reading its own start, the agent is NOT ahead of the "
    "do-nothing baseline on recall. If it ever pulled ahead, B00 and B05 would be "
    "announcing a cost that did not land and this would be a different episode."
)
assert ORACLE["recall"] > AGENT["recall"], "the cost is a fall, not a rise"

# THE SECOND ARGUMENT. Precision goes the other way, and both halves are on the frame.
assert AGENT["precision"] > B0["precision"] and AGENT["precision"] > ORACLE["precision"], (
    "fewer bonds held means fewer held wrongly — the trade is real in both directions, and "
    "a frame showing only the recall fall would be describing a failure rather than a trade"
)

# THE THIRD. The merge result is LEVEL with doing nothing, and must never read as better.
assert MG["after"]["count"] < MG["before"]["count"] == 26 and MG["after"]["count"] == 3
assert PREC["after"] > PREC["before"], "the fixes moved precision"
assert 0 < PREC["after"] - PREC["b0"] <= 0.01, (
    "93.3% against B0's 92.8% is half a point with an interval straddling zero. The build "
    "holds the gap SMALL so B01 has to say 'level' and can never drift into 'better'."
)
assert sum(a["n"] for a in MG["actions"]) != MG["before"]["count"], (
    "21 + 25 + 4 is what the merge step DID, not a breakdown of the 26 — week 5's 26 broke "
    "down 10/10/4/2. This assertion exists so nobody can relabel one as the other."
)
assert len({a["id"] for a in MG["actions"]}) == 3
assert MG["new_bonds"]["caught"] < MG["new_bonds"]["of"] and MG["new_bonds"]["b0"] == 0

# THE FOURTH. The model buys recall, not precision — and the denominators stay honest.
assert S_REC["model"] > S_REC["rules"] and S_PRE["model"] > S_PRE["rules"]
assert (S_REC["model"] - S_REC["rules"]) > (S_PRE["model"] - S_PRE["rules"]), (
    "B03's verdict is 'the model adds recall, not precision'. If the precision gain ever "
    "exceeded the recall gain that sentence would be false."
)
assert SC["graded_on"] < SC["reports_read"], (
    "94 reports were READ; 43 is the denominator the percentages are GRADED on. Both go on "
    "the frame — quoting 89.7% against 94 would be quoting it against the wrong set."
)
assert SC["reports_read"] == 94 and SC["graded_on"] == 43

# THE FIFTH. Two asks, two different answers, or B04 has nothing to show.
assert R1["count"] != R2["count"], (
    "B04 is one report asked twice. If the two counts ever matched, the beat would be "
    "claiming a variance that is not there."
)
assert R1["count"] > R2["count"] and VR["who"] and VR["doc"]

# The self-checks catch a minority, and the investigators changed nothing.
assert WRONG["got"] < WRONG["of"] - WRONG["got"], (
    "17 of 50 — the checks miss MORE wrong episodes than they catch, and B07 says a third"
)
assert WRONG_SHARE < 0.5 and RIGHT_SHARE > 0
assert Q["settled"] < Q["of"], "21 of 67"
assert CA["no_change"].startswith("No graded bond changed")
assert "_settled_conflict" in CA, (
    "FRICTIONAL.md and description.txt disagree on how the 21 break down. No breakdown is "
    "drawn; the note records why."
)

# Limits that have to stay limits.
assert TD["agent"] < TD["oracle"] < TD["of"], (
    "total debt within 2%: 26 of 79 at agent start against 44 at oracle start — the weak "
    "spot, and it got weaker"
)
assert LM["handcheck"]["got"] < LM["handcheck"]["of"]
assert len(FIG["next"]) == 3
assert len(WH["cases"]) == 4 and len({c["who"] for c in WH["cases"]}) == 4

# ── the values figdata.json does not measure ──────────────────────────────────
NOT_IN_FIGDATA = "Not measured in figdata.json"


def sentence_case(text: str) -> str:
    """Uppercase the first letter ONLY.

    str.capitalize() also lowercases everything after it, which turns proper nouns
    like B0 into b0 on the frame. GATE V passes a case-folded proper noun.
    """
    return text[:1].upper() + text[1:]
GATE_RECORD = {
    "state": "DELEGATED",
    "not": "CLEARED",
    "where": "manifests/week6_gate.json",
    "note": "Handed to Claude end to end before the week started. The one decision taken "
            "during it was to resume the runs after the laptop ran low on memory. No "
            "person has reviewed the transcriptions or the results — for weeks 3 to 6.",
}
JUDGMENTS = {
    "model": OP["model"],
    "what": TC["model_judgments"],
    "handcheck": TC["handcheck_by"],
}
ORACLE_WAS = {
    "name": OP["was_called"],
    "light": OP["was_light"],
}

HANDLE = "@HumanitariansAI"
SEGMENT = "Reading the Opening Ledger Instead of Borrowing It"
SLUG = "reading-the-opening-ledger-instead-of-borrowing-it"
KICKER = "Irreducibly Human"     # GATE L rule 7 — the FIXED claude-hai series name
GREETING = "Bula, HAI"           # Fijian. Never repeats a language; see metadata note.


def num(n):
    return f"{n:,}"


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


LOCAL = "reel-local/ReadingTheOpeningLedger"
beats = []

# ── B00 · COLD OPEN ───────────────────────────────────────────────────────────
beats.append(beat(
    "B00", "COLD OPEN", "BOOKEND",
    "Hi, I'm Om Mali. This video is about my A I debt tracker reading its own starting "
    "ledger from a company's last report, instead of borrowing it from the answer key, and "
    "measuring what that costs. This is week six of the A I Debt Tracker. It costs about "
    "eight points of recall — and that is the whole advantage I reported last week.",
    21,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": GREETING,
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "Stop handing the agent an opening ledger from the answer key. Make it read "
            "that ledger out of the company's own last report, run the same quarters "
            "again, and tell me exactly what the convenience was worth."
        ),
        "runningText": "agent_start.py — A4, 45 quarters…",
        "folderLabel": HANDLE,
        "modelLabel": "Opus 5",
        "effortLabel": "High",
        "output": [
            f"last week's merge fixes landed: wrong additions {MG['before']['count']} → "
            f"{MG['after']['count']}, precision {PREC['before_s']} → {PREC['after_s']} — "
            f"level with doing nothing ({PREC['b0_s']}), not better",
            f"the new opening-ledger reader finds {S_REC['model_s']} of the bonds and "
            f"{S_PRE['model_s']} of what it finds is right, against {S_REC['rules_s']} for "
            f"rules with no model",
            f"and reading its own start costs {GP['cost_s']} of recall — "
            f"{ORACLE['recall_s']} → {AGENT['recall_s']}, which puts it LEVEL with "
            f"carrying last quarter forward ({B0['recall_s']}). Precision went the other "
            f"way, up to {AGENT['precision_s']}.",
        ],
    }, "type-on", [
        {"at": "on 'reading its own starting ledger'", "event": "The ask types into the Claude composer."},
        {"at": "on 'that is the whole advantage I reported last week'", "event": "The result lands ANSWERED with three output lines — the third is the cost."},
    ], intent="COLD OPEN LAW: the ask is the week itself. It lands ANSWERED, and the answer says in its third line that this week undoes last week's headline. Nothing is held back for a reveal."),
))

# ── B01 · THE MERGE FIXES ─────────────────────────────────────────────────────
beats.append(beat(
    "B01", "THE MERGE FIXES", "REMOTION",
    "First, last week's leftovers. The tracker had added twenty-six bonds that weren't in "
    "the report. I fixed all three causes in the merge step, which is code, not a model. On "
    "the same readings, the wrong additions fell from twenty-six to three. Precision went "
    "from ninety to ninety-three percent — which is level with doing nothing, not better "
    "than it.",
    22,
    remotion("W6Merge", LOCAL, {
        "sparkLine": "Twenty-six down to three.",
        "eyebrow": "AI DEBT TRACKER · THE MERGE FIXES",
        "title": "Fewer bonds that are not there",
        "subtitle": sentence_case(MG["same"]),
        "unitLabel": MG["what"],
        "bars": [
            {"label": MG["before"]["label"], "count": MG["before"]["count"],
             "hot": MG["before"]["hot"]},
            {"label": MG["after"]["label"], "count": MG["after"]["count"],
             "hot": MG["after"]["hot"]},
        ],
        "actionsLabel": "what the merge step does now — all of it code",
        "actions": [{"n": a["n"], "what": a["what"], "id": a["id"]} for a in MG["actions"]],
        "actionsNote": "These are what the merge step DID across the run, not a breakdown "
                       "of the 26.",
        "verdict": f"Precision {PREC['before_s']} → {PREC['after_s']}. B0 is "
                   f"{PREC['b0_s']}, so that is {MG['precision_verdict']} "
                   f"({MG['precision_paired']}). Recall held at {MG['recall_s']}, still "
                   f"{MG['recall_over_b0']} over B0.",
        "note": f"{MG['undiagnosed']} {MG['loans']}",
        "source": "SOURCE: AI Debt Tracker docs/agent_start.md · DESIGN.md P56–P58 · "
                  "figdata.json",
    }, "shrink", [
        {"at": "on 'twenty-six bonds that weren't in the report'", "event": "The week 5 bar draws to full length."},
        {"at": "on 'fell from twenty-six to three'", "event": "The week 6 bar draws beneath it on the SAME scale — a stub."},
        {"at": "per fix", "event": "Three actions land, each with its defect id."},
    ], intent="Two bars on one shared unit — 6px per bond — so 3 against 26 is read as a length, not as two numbers. The three lines beneath are labelled as ACTIONS because 21+25+4 is what the merge step did, not the 26 broken down, and conflating them would be a real error."),
))

# ── B02 · THE OPENING READER ──────────────────────────────────────────────────
beats.append(beat(
    "B02", "THE OPENING READER", "REMOTION",
    "Now the crutch. Until this week, every quarter started from an opening ledger taken "
    "from the answer key — cheating a little, deliberately. So I built a reader for it. "
    "Code finds the tables that look like a debt note. The model points at the rows that "
    "are one bond. Code reads every number out of the cell.",
    21,
    remotion("W6Opening", LOCAL, {
        "sparkLine": "Same rule as week one, a new job.",
        "eyebrow": "AI DEBT TRACKER · THE OPENING-LEDGER READER",
        "title": "Reading the start instead of being handed it",
        "subtitle": f"{OP['was']} The design calls it {ORACLE_WAS['name']}.",
        "ruleLabel": OP["rule_from"],
        "rule": OP["rule"],
        "steps": [{"who": s["who"], "what": s["what"], "hot": s["hot"]}
                  for s in OP["steps"]],
        "modelChip": OP["model"],
        "note": f"{ORACLE_WAS['light']} A design decision, not a measurement — "
                f"narration_script.md notes and DESIGN.md ablation A4.",
        "source": "SOURCE: AI Debt Tracker docs/opening_reader.md · DESIGN.md A4 · "
                  "figdata.json",
    }, "stagger", [
        {"at": "on 'taken from the answer key'", "event": "The old arrangement is named — oracle start."},
        {"at": "on 'the model points at the rows'", "event": "The middle step lands in the accent, the only one that is not CODE."},
        {"at": "on 'reads every number out of the cell'", "event": "The third step closes the sandwich."},
    ], intent="Same shape as the event reader from week 4, deliberately: code, then the model, then code. The model is the only accented card and the only one not labelled CODE, because the rule this whole project is built on is that it never types a number."),
))

# ── B03 · WHAT IT SCORED ──────────────────────────────────────────────────────
beats.append(beat(
    "B03", "WHAT IT SCORED", "REMOTION",
    "It read ninety-four opening reports. Graded on the forty-three the answer key covers, "
    "it found ninety percent of the bonds, and ninety-nine percent of what it found was "
    "right. Rules alone, with no model at all, found eighty-four percent. So the model buys "
    "recall, not precision — it finds rows the rules miss, and it isn't more accurate on "
    "them.",
    22,
    remotion("W6Score", LOCAL, {
        "sparkLine": "The model buys recall, not precision.",
        "eyebrow": "AI DEBT TRACKER · THE OPENING READER, SCORED",
        "title": "What the reader found, and what it got right",
        "subtitle": f"{SC['reports_read']} {SC['reports_read_what']} read · graded on the "
                    f"{SC['graded_on']} the answer key covers",
        "metrics": [
            {"name": m["name"], "qualifier": m["qualifier"],
             "model": m["model"], "rules": m["rules"],
             "modelS": m["model_s"], "rulesS": m["rules_s"],
             # derived, never typed — the beat's claim is about the SIZE of these two
             "gapS": f"+{(m['model'] - m['rules']) * 100:.1f} points from the model"}
            for m in SC["metrics"]
        ],
        "modelLabel": SC["model_label"],
        "rulesLabel": SC["rules_label"],
        "verdict": SC["verdict"],
        "note": f"{SC['defects']['what']} Fixed on {SC['defects']['fixed_on']} "
                f"({SC['defects']['id']}).",
        "source": "SOURCE: AI Debt Tracker docs/opening_reader.md (graded at L1, "
                  f"{SC['graded_on']} reports) · figdata.json",
    }, "grow", [
        {"at": "on 'found ninety percent of the bonds'", "event": "The recall pair fills; the model bar runs past the rules bar."},
        {"at": "on 'ninety-nine percent of what it found was right'", "event": "The precision pair fills — the two bars are almost the same length."},
        {"at": "on 'the model buys recall, not precision'", "event": "The gap on the first pair is marked; the second pair has almost none."},
    ], intent="Two metric pairs on one scale. The claim is about the SIZE of two gaps, so both gaps are drawn and the recall one is marked. The denominator split — 94 read, 43 graded — sits in the subtitle, because quoting 89.7% against 94 would be quoting it against the wrong set."),
))

# ── B04 · ASKED TWICE ─────────────────────────────────────────────────────────
beats.append(beat(
    "B04", "ASKED TWICE", "REMOTION",
    "One more thing about that reader. Nine reports had to be asked again, because the "
    "first pass truncated the model's answers. Broadcom's January report gave thirty-six "
    "matching bonds the first time and twenty-two the second. Same report, same prompt, "
    "different answer. That variance is part of what this reader is, and I'm reporting it "
    "rather than averaging it away.",
    22,
    remotion("W6Variance", LOCAL, {
        "sparkLine": "Same report. Two different answers.",
        "eyebrow": "AI DEBT TRACKER · THE READER, ASKED TWICE",
        "title": "The model does not answer the same way twice",
        "subtitle": "One of the nine reports that had to be asked again",
        "bracketLabel": f"{VR['who']}, {VR['doc']} — one report, two asks",
        "runs": [{"label": r["label"], "count": r["count"], "hot": r["hot"]}
                 for r in VR["runs"]],
        "unit": "matching bonds",
        "whyLabel": "why it was asked twice",
        "why": VR["why"],
        "meaning": VR["what_it_means"],
        "note": VR["unknown"],
        "source": "SOURCE: AI Debt Tracker FRICTIONAL.md · docs/opening_reader.md · "
                  "figdata.json",
    }, "diverge", [
        {"at": "on 'thirty-six matching bonds the first time'", "event": "The first count lands."},
        {"at": "on 'and twenty-two the second'", "event": "The second lands beside it, visibly shorter, in the accent."},
        {"at": "on 'rather than averaging it away'", "event": "The two are bracketed as ONE report, not two."},
    ], intent="Every other beat in this reel is a measurement. This one is the reason to distrust measurements of this kind: one input, two outputs, fourteen bonds apart. Drawn as two counts under a single bracket so the frame cannot be read as two different reports."),
))

# ── B05 · THE WEEK'S CHECK ────────────────────────────────────────────────────
beats.append(beat(
    "B05", "THE WEEK'S CHECK", "REMOTION",
    "Then the real test. The same forty-five quarters, run three ways. Borrowing the start: "
    "ninety-eight percent recall. Reading its own start: ninety. That's a cost of about "
    "eight points. Precision went the other way, up to ninety-five and a half — fewer bonds "
    "held means fewer held wrongly. And here is the part that matters: against doing "
    "nothing, the agent is now level on recall.",
    25,
    remotion("W6Gap", LOCAL, {
        "sparkLine": "The advantage was the borrowed ledger.",
        "eyebrow": "AI DEBT TRACKER · THE WEEK 6 CHECK",
        "title": "A borrowed start against a read one",
        "subtitle": f"{GP['graded']} {GP['graded_what']} — {GP['check']}",
        "metrics": [
            {"name": "Recall", "key": "recall",
             "rows": [{"label": s["label"], "note": s["note"], "value": s["recall"],
                       "valueS": s["recall_s"], "hot": s["hot"]} for s in GP["starts"]]},
            {"name": "Precision", "key": "precision",
             "rows": [{"label": s["label"], "note": s["note"], "value": s["precision"],
                       "valueS": s["precision_s"], "hot": s["hot"]} for s in GP["starts"]]},
        ],
        "costLabel": "the cost of reading its own start",
        "cost": GP["cost"],
        "verdict": GP["the_point"],
        "note": f"{GP['why_precision_rose']} {GP['vs_b0']}",
        "source": "SOURCE: AI Debt Tracker docs/agent_start.md (paired, same quarters) · "
                  "figdata.json",
    }, "fall", [
        {"at": "on 'borrowing the start: ninety-eight percent'", "event": "The oracle recall bar fills to its length."},
        {"at": "on 'reading its own start: ninety'", "event": "The agent bar fills SHORT of it, in the accent."},
        {"at": "on 'against doing nothing, the agent is now level'", "event": "The B0 bar lands level with the accent bar — the two are the same length."},
    ], intent="Six bars, one scale, three starts. The beat turns on the agent bar and the B0 bar ending at the same place on the recall rows while the accent bar runs PAST B0 on the precision rows. That is the week in one picture and it is drawn, not captioned."),
))

# ── B06 · WHERE THE GAP IS ────────────────────────────────────────────────────
beats.append(beat(
    "B06", "WHERE THE GAP IS", "REMOTION",
    "The good news is that the gap is concentrated. Broadcom alone: twenty-three "
    "instruments found where the reports hold thirty-nine and forty. Snowflake and Super "
    "Micro, convertible tables the reader never found. And Core Scientific, whose opening "
    "reports were filed the same day as the report being predicted — so the point-in-time "
    "rule refuses them. That last one is the rule working.",
    23,
    remotion("W6Where", LOCAL, {
        "sparkLine": "A few companies, not a general weakness.",
        "eyebrow": "AI DEBT TRACKER · WHERE THE GAP IS",
        "title": "The cost is concentrated, which is why it can be worked on",
        "subtitle": "Most of the 7.9-point fall sits in four names",
        "cases": [{"who": c["who"], "what": c["what"], "id": c["id"]}
                  for c in WH["cases"]],
        "ruleLabel": "the refusal is the rule working",
        "rule": f"{WH['refused_count']} {WH['refused_what']}. "
                f"{WH['rule_doing_its_job']}",
        "note": "",
        "source": "SOURCE: AI Debt Tracker docs/agent_start.md · FRICTIONAL.md · "
                  "DESIGN.md P60 · figdata.json",
    }, "stagger", [
        {"at": "per company", "event": "Four names land, each with what the reader missed."},
        {"at": "on 'that last one is the rule working'", "event": "The point-in-time refusal is set apart, in the accent, as a design decision rather than a defect."},
    ], intent="'Most of it is a few companies' is a claim. Four named companies with the specific table each one hid is the same claim as evidence — and it separates the three misses from the one refusal, which is not a miss at all."),
))

# ── B07 · DOES IT KNOW? ───────────────────────────────────────────────────────
beats.append(beat(
    "B07", "DOES IT KNOW?", "REMOTION",
    "Last measurement: when an episode ends wrong, do the checks notice? Seventeen times "
    "out of fifty. They also flagged eleven of the thirty-six that ended right. So a third, "
    "with false alarms. And the investigators I added settled twenty-one of sixty-seven "
    "open questions — but changed no graded bond. Mostly they confirmed what the ledger "
    "already held.",
    22,
    remotion("W6Catch", LOCAL, {
        "sparkLine": "It notices about a third of the time.",
        "eyebrow": "AI DEBT TRACKER · DOES IT KNOW WHEN IT IS WRONG?",
        "title": "When an episode ends wrong, do the checks notice?",
        "subtitle": "Agent start, development quarters",
        "rows": [
            {"label": WRONG["label"], "got": WRONG["got"], "of": WRONG["of"],
             "hot": WRONG["hot"]},
            {"label": RIGHT["label"], "got": RIGHT["got"], "of": RIGHT["of"],
             "hot": RIGHT["hot"]},
        ],
        "rateLabel": "self-catch rate",
        "rate": f"{CA['rate_s']} at agent start, {CA['oracle_rate']['s']} "
                f"({CA['oracle_rate']['got']} of {CA['oracle_rate']['of']}) at oracle "
                f"start",
        "questionsLabel": "the investigators",
        "questionsGot": Q["settled"],
        "questionsOf": Q["of"],
        "questionsWhat": f"{CA['investigators']} {CA['settled_what']} "
                         f"{CA['no_change'].upper()}",
        "note": CA["still_open"],
        "source": "SOURCE: AI Debt Tracker docs/agent_start.md · figdata.json",
    }, "fill", [
        {"at": "on 'seventeen times out of fifty'", "event": "50 cells land; 17 fill in the accent."},
        {"at": "on 'eleven of the thirty-six that ended right'", "event": "36 cells land beneath; 11 fill — the false alarms."},
        {"at": "on 'changed no graded bond'", "event": "21 of 67 lands, and the verdict beneath it is that nothing moved."},
    ], intent="A rate drawn as a bar is a rectangle. Drawn as 50 countable cells with 17 filled, the thing you see is the 33 it missed — which is the honest subject of the beat. The investigators get a plain figure because their result is that nothing changed."),
))

# ── B08 · THE LIMITS ──────────────────────────────────────────────────────────
beats.append(beat(
    "B08", "THE LIMITS", "REMOTION",
    "The limits. All of this is development quarters; the test split is still untouched. "
    "The opening reader was graded against the same answer key that supplies the borrowed "
    "start. Total debt lands within two percent on twenty-six of seventy-nine quarters — "
    "the weakest number here. And the gate says delegated, not cleared: nobody has reviewed "
    "any of it.",
    23,
    remotion("W6Limits", LOCAL, {
        "sparkLine": "What the week does not show.",
        "eyebrow": "AI DEBT TRACKER · THE LIMITS",
        "title": "Every number above, and the limit that narrows it",
        "subtitle": "",
        "rows": [
            {"claim": f"recall {ORACLE['recall_s']} → {AGENT['recall_s']}",
             "limit": f"{LM['test_split']} Every figure in this video is a development "
                      f"number.",
             "hot": False},
            {"claim": f"the reader, {S_REC['model_s']} / {S_PRE['model_s']}",
             "limit": f"{LM['same_key']} It is being marked by the thing it is trying to "
                      f"replace. And it was graded on {SC['graded_on']} of the "
                      f"{SC['reports_read']} reports it read.",
             "hot": False},
            {"claim": "total debt",
             "limit": f"within 2% on {TD['agent']} of {TD['of']} quarters at agent start, "
                      f"against {TD['oracle']} at oracle start. The bonds can be right "
                      f"while the total is not, and this is the weakest number in the "
                      f"video.",
             "hot": True},
            {"claim": f"{Q['settled']} of {Q['of']} questions settled",
             "limit": f"and no graded bond changed. {CA['still_open']} The investigators do "
                      f"not search older filings yet, which is where those answers are.",
             "hot": False},
            {"claim": "the judgments",
             "limit": f"{JUDGMENTS['what']} {JUDGMENTS['handcheck']} The fresh hand-check "
                      f"agreed on {LM['handcheck']['got']} of {LM['handcheck']['of']} "
                      f"({LM['handcheck']['defect']}). {LM['no_fresh_triage']}",
             "hot": False},
        ],
        "gateLabel": "the week's gate record",
        "gateState": f"{GATE_RECORD['state']}, not {GATE_RECORD['not']}",
        "gateNote": f"{GATE_RECORD['note']} ({NOT_IN_FIGDATA} — recorded in "
                    f"{GATE_RECORD['where']}.)",
        "nextLabel": "next",
        "next": FIG["next"],
        "source": "SOURCE: narration_script.md notes · FRICTIONAL.md · docs/agent_start.md "
                  "· docs/opening_reader.md · figdata.json",
    }, "stagger", [
        {"at": "per limit", "event": "Each claim lands with the limit that narrows it."},
        {"at": "on 'delegated, not cleared'", "event": "The gate record lands as the largest object on the frame."},
        {"at": "on 'next week'", "event": "Three next steps land at the foot."},
    ], intent="Every episode in this series ends on its own limits. Total debt is accented because it is the number the week made WORSE and the one no other frame shows; the gate record is still drawn largest, because 'nobody has checked any of this' outranks all of them."),
))

# ── B09 · VERDICT ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B09", "VERDICT", "BOOKEND",
    "So: the merge fixes cut the wrong additions from twenty-six to three, and a new reader "
    "builds the opening ledger out of the company's last report — ninety percent of the "
    "bonds, ninety-nine percent of those right. Standing on its own reading, the tracker "
    "loses about eight points of recall and is level with doing nothing. It gains on "
    "precision. The checks notice a third of its mistakes, and nobody has reviewed any of "
    "it.",
    30,
    remotion("ClaudeVerdictArtifact", "proven-core/ClaudeVerdictArtifact", {
        "artifactTitle": SEGMENT,
        "artifactHeading": "What week 6 built, and what it is allowed to claim",
        "artifactLines": [
            f"Three merge fixes, all code: launch notices fold into the priced bond "
            f"({MG['actions'][0]['id']}), a bond named with no amount becomes a question "
            f"({MG['actions'][1]['id']}), the banks' option is recorded but not added "
            f"({MG['actions'][2]['id']}). On the same readings the wrong additions fell "
            f"{MG['before']['count']} → {MG['after']['count']} and precision rose "
            f"{PREC['before_s']} → {PREC['after_s']} — level with B0's {PREC['b0_s']}, not "
            f"better.",
            f"An opening-ledger reader on the same rule as the event reader: code finds the "
            f"debt tables, {OP['model']} points at the rows that are one instrument, code "
            f"reads every value from the cited cell. {SC['reports_read']} reports read; "
            f"graded on {SC['graded_on']}, recall {S_REC['model_s']} and precision "
            f"{S_PRE['model_s']}, against {S_REC['rules_s']} / {S_PRE['rules_s']} for rules "
            f"with no model. The model adds recall, not precision.",
            f"THE WEEK'S CHECK (A4). Same {GP['graded']} quarters, borrowed start against "
            f"read start: recall {ORACLE['recall_s']} → {AGENT['recall_s']}, a cost "
            f"of {GP['cost']}. Precision moved the other way, {ORACLE['precision_s']} → "
            f"{AGENT['precision_s']}. Against B0 the agent is now LEVEL on recall "
            f"({B0['recall_s']}) and ahead on precision ({B0['precision_s']}). Last week's "
            f"{MG['recall_over_b0']} over doing nothing was the borrowed ledger.",
            f"The gap is concentrated: {WH['cases'][0]['who']} alone accounts for much of "
            f"it, {WH['cases'][1]['who']} and {WH['cases'][2]['who']} hid their convertible "
            f"tables, and {WH['cases'][3]['who']}'s opening reports are refused by the "
            f"point-in-time rule ({WH['cases'][3]['id']}) — the rule working, counted in "
            f"the gap rather than worked around. The reader is also not deterministic: "
            f"{VR['who']}'s {VR['doc']} gave {R1['count']} bonds on one ask and "
            f"{R2['count']} on the next.",
            f"Of the {WRONG['of']} quarters that ended wrong, the checks flagged "
            f"{WRONG['got']}; they flagged {RIGHT['got']} of {RIGHT['of']} that ended "
            f"right. Investigators settled {Q['settled']} of {Q['of']} questions and "
            f"changed no graded bond. Total debt is within 2% on {TD['agent']} of "
            f"{TD['of']} quarters, down from {TD['oracle']}. The gate records the week "
            f"{GATE_RECORD['state']}, not {GATE_RECORD['not']}.",
        ],
    }, "stagger", [
        {"at": "per clause", "event": "Five findings stagger in, one per spoken clause."},
    ], intent="Judgment beat. The artifact page is the point (ILLUSTRATE LAW carve-out). The third finding is the one that undoes last week's headline, and it is in the middle rather than buried at the end."),
))

# ── B10 · HANDOFF ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B10", "HANDOFF", "BOOKEND",
    "Your turn. Paste this into Claude. Find the place where your evaluation hands your "
    "system something it would have to work out for itself in the real thing — a label, a "
    "starting state, a cleaned-up input. Take it away and re-run. Whatever you lose is a "
    "number you were never really measuring.",
    18,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": "Your turn.",
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "Find every place my evaluation hands the system something it would have to "
            "produce for itself in production — a gold label, a starting state, a cleaned "
            "input, a retrieved document. List them, pick the one doing the most work, "
            "make the system generate it instead, and re-run the same evaluation "
            "unchanged. Report both numbers side by side and tell me what that convenience "
            "was worth."
        ),
        "runningText": "paste this into Claude…",
        "folderLabel": HANDLE,
        "modelLabel": "Opus 5",
        "effortLabel": "High",
        "output": [],
    }, "type-on", [
        {"at": "on 'paste this into Claude'", "event": "The prompt types into the composer."},
    ], intent="HANDOFF LAW: a real prompt, read ALOUD and then discussed. One of exactly two typing beats. It is this week's finding — that a convenience inside an evaluation is an unmeasured claim — turned into something a viewer can run on their own work."),
))

# ── B11 · OUTRO ───────────────────────────────────────────────────────────────
beats.append(beat(
    "B11", "OUTRO", "BOOKEND",
    "Reading the opening ledger instead of borrowing it. Week six of the A I Debt Tracker. "
    "Om Mali, for Humanitarians A I.",
    9,
    remotion("ClaudeTitleOutro", "proven-core/ClaudeTitleOutro", {
        "title": SEGMENT,
        "handle": HANDLE,
        # `subline`, not `subtitle` — the wrong name ships the outro reading
        # "bot vs bot, season one", a default from an unrelated show.
        "subline": "week 6 · the AI Debt Tracker",
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
    "greeting_note": "hello lexicon: Fijian. HAI persona takes only the shortest cues (Hi · Ola · Hej · Ciao · Hallo · Salut · Ahoj · Szia · Tere · Moi · Hoi · Labas · Salve · Sveiki · Zdravo · Merhaba · Jambo · Bula). Rotate; never repeat a language.",
    "aspect_ratio": "16:9",
    "fps": 24,
    "lead_silence_s": 0.4,
    "note": (
        "ai-explainer / claude-hai. AI Debt Tracker WEEK 6. ILLUSTRATE LAW: the Claude UI "
        "appears at B00 (cold open, answered), B09 (verdict artifact), B10 (handoff) and "
        "B11 (outro) only — every body beat illustrates its concept as a native animated "
        "Remotion scene (REBUILD LAW). The four source PNGs and their SVG sources are "
        "REFERENCE in pantry/, never slotted as media. The script's five body sections "
        "become eight body beats: 0:45 splits into the reader's mechanism (B02) and its "
        "score (B03), with the non-determinism the script mentions in one clause given its "
        "own beat (B04); 1:20 splits into the three-way check (B05) and where the gap "
        "actually sits (B06); 1:55 becomes B07; and the closing on-camera section becomes "
        "a limits beat. FIVE THINGS NOT TO GET WRONG: removing the borrowed ledger removes "
        "last week's recall advantage — agent start is LEVEL with B0, not ahead; precision "
        "moves the OTHER way and both halves belong on the frame; 93.3% against B0's 92.8% "
        "is LEVEL, never 'better'; the reader's 89.7%/98.8% are graded on 43 reports, not "
        "the 94 it read; and the week's gate records DELEGATED, not cleared."
    ),
}

sheet = {"metadata": META, "beats": beats}

body = [b for b in beats if b["beat_id"] not in ("B00", "B09", "B10", "B11")]
words = {b["beat_id"]: len(b["narration_text"].split()) for b in beats}
lo = min(words[b["beat_id"]] for b in body)
hi = max(words[b["beat_id"]] for b in body)
# 45-72, the band weeks 2-5 settled on. This script spells its numbers aloud
# ("ninety-five and a half", "twenty-one of sixty-seven"), and one figure can cost six
# words; tightening the band would mean cutting evidence to pay for pronunciation.
assert 45 <= lo and hi <= 72, f"body beat word budget 45-72 violated: {lo}-{hi}"
assert len(body) == 8 and len(beats) == 12

if "--check" in sys.argv:
    print("[adt-w6] all assertions pass")
    sys.exit(0)

out = HERE / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"[adt-w6] wrote {out}  — {len(beats)} beats")
print("[adt-w6] narration words: " + " ".join(f"{k}={v}" for k, v in words.items()))
print(f"[adt-w6] body beats {lo}-{hi}w (band 45-72), total {sum(words.values())}w")
print(f"[adt-w6] derived: merge {MG['before']['count']}->{MG['after']['count']} wrong, "
      f"precision {PREC['before_s']}->{PREC['after_s']} LEVEL with B0 {PREC['b0_s']} · "
      f"reader {S_REC['model_s']}/{S_PRE['model_s']} vs rules {S_REC['rules_s']}/"
      f"{S_PRE['rules_s']} on {SC['graded_on']} of {SC['reports_read']} · variance "
      f"{R1['count']} vs {R2['count']} · A4 recall {ORACLE['recall_s']}->"
      f"{AGENT['recall_s']} (cost {GP['cost_s']}) vs B0 {B0['recall_s']} = LEVEL · "
      f"precision {ORACLE['precision_s']}->{AGENT['precision_s']} vs B0 "
      f"{B0['precision_s']} = AHEAD · self-catch {WRONG['got']}/{WRONG['of']} · questions "
      f"{Q['settled']}/{Q['of']} no change · total debt {TD['agent']}/{TD['of']} (was "
      f"{TD['oracle']}) · gate {GATE_RECORD['state']}")
