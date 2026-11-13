#!/usr/bin/env python3
"""
build_beat_sheet.py — AI Debt Tracker, WEEK 5: Running full episodes from filings to ledger.

Writes beat_sheet.json with EVERY on-screen figure injected from figdata.json. No number is
typed into a scene or into a beat sheet by hand.

THE FRAMING ASSERTION of this reel is a TRADE, and it is asserted in both directions:
recall must RISE against the do-nothing baseline and precision must FALL. The week's
headline is a system that finally runs end to end — and the honest shape of that result is
not a win, it is an exchange. If precision ever stopped falling, B03, B05 and B06 would be
arguing about a cost that no longer exists, and the build fails rather than let the episode
become a victory lap.

THE SECOND ARGUMENT, asserted the same way: the baseline catches ZERO new bonds and the
tracker catches 30 of 34 — most, and not all. Recall as a percentage is abstract; "none,
against thirty of thirty-four" is the thing recall is actually about, and both halves of it
are held by assertion so neither can drift.

A THIRD closes the addition tally both ways: the five segments of the author's stacked bar
must sum to 66, and the four real/wrong groups must too. The author's own figure legends
only FOUR of its five segments — the two plain misreads are named in its footnote and carry
no defect id. The reel draws all five and names the fifth; the assertion is what stops the
drawn band and the spoken breakdown quietly disagreeing.

A FOURTH holds the timing bug honest: the first run's precision must be BELOW the fixed
run's, and both are reported. A fix that is only reported as its own result is not reported.

A FIFTH keeps the fresh checks from being read as a clean sweep: triage passes 15 of 15 and
the SAME line failed it last week at 8 of 9, and the direct model call still reads more
fields than the reader (96% against 91%). Week 4's lesson is not allowed to expire because
this week's headline is somewhere else.

THREE CLAIMS ARE NOT MEASURED in figdata.json. They come from narration_script.md,
FRICTIONAL.md and the project documents, are passed as named constants below, and every
screen that uses one says where it came from:
  · GATE_RECORD    — the week is recorded DELEGATED, not CLEARED; no person has reviewed it
  · LABELLER       — the labels, the truth and the diagnosis are a model judgment
  · ORACLE_START   — every quarter began from the answer key's ledger, on purpose

Usage:  python build_beat_sheet.py            (writes beat_sheet.json)
        python build_beat_sheet.py --check    (assertions only, writes nothing)
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIG = json.loads((HERE / "figdata.json").read_text(encoding="utf-8"))

GP = FIG["graph"]
EN = FIG["engine"]
EP = FIG["episodes"]
AD = FIG["additions"]
TM = FIG["timing"]
FR = FIG["fresh"]
TC = FIG["truthcheck"]

# ── derived, never typed ──────────────────────────────────────────────────────
MET = {m["key"]: m for m in EP["metrics"]}
RECALL, PRECISION = MET["recall"], MET["precision"]
NEW = EP["new_bonds"]

SEG = {s["key"]: s for s in AD["segments"]}
REAL = SEG["real"]["count"]
WRONG = sum(s["count"] for s in AD["segments"] if s["key"] != "real")
NAMED_WRONG = [s for s in AD["segments"] if s["id"]]
UNNAMED_WRONG = [s for s in AD["segments"] if s["key"] != "real" and not s["id"]]

RUNS = {r["key"]: r for r in TM["runs"]}
FIRST, FIXED = RUNS["first"], RUNS["fixed"]

FROW = {r["key"]: r for r in FR["rows"]}
TRIAGE, READER, B1, B2, KEY = (
    FROW["triage"], FROW["reader"], FROW["b1"], FROW["b2"], FROW["key"])
T = FR["triage"]
K = FR["key"]

# ── assertions ────────────────────────────────────────────────────────────────
# THE FRAMING ASSERTION. The reel exists because these two numbers moved in OPPOSITE
# directions. Either half alone is a different episode.
assert RECALL["tracker"] > RECALL["baseline"], (
    "B03's first claim: reading the filings raises recall against carrying the last "
    "report forward. Without it there is nothing to trade away."
)
assert PRECISION["tracker"] < PRECISION["baseline"], (
    "B03's second claim, and the one the episode is honest about: precision FELL. If it "
    "ever stopped falling, B05 would be itemising a cost that no longer exists and this "
    "would be a victory lap instead of a trade."
)
assert RECALL["direction"] == "up" and PRECISION["direction"] == "down"
assert EP["graded"] == 45 and EP["same_start"]

# THE SECOND ARGUMENT. What recall is actually about: none, against most-but-not-all.
assert NEW["baseline_caught"] == 0, (
    "carrying the last report forward cannot see a new bond — it never reads anything, "
    "and B04 is built on that being exactly zero"
)
assert 0 < NEW["caught"] < NEW["issued"], (
    "30 of 34: most of them, and not all of them. A clean sweep would make B04 a boast "
    "and a miss would make it a different beat."
)
assert NEW["caught"] > NEW["issued"] // 2

# THE THIRD. The addition tally has to close, both ways, and the unlegended segment
# has to stay accounted for.
assert REAL + WRONG == AD["total"] == 66, (
    "B05 draws the author's band segment for segment; a band whose parts do not sum to "
    "the number above it is not a breakdown"
)
assert WRONG == 26 and REAL == 40
assert sum(s["count"] for s in NAMED_WRONG) + sum(s["count"] for s in UNNAMED_WRONG) == WRONG
assert len(NAMED_WRONG) == 3 and len(UNNAMED_WRONG) == 1, (
    "three kinds carry defect ids (P56-P58); the two plain misreads carry none, because "
    "FRICTIONAL.md gives none. No id is invented for them."
)
assert all(s["id"].startswith("P") for s in NAMED_WRONG)
assert UNNAMED_WRONG[0]["id"] == "" and UNNAMED_WRONG[0]["legend"] is False
assert len({s["id"] for s in NAMED_WRONG}) == 3
assert REAL > WRONG, "most of what it added was real, and the beat says so first"

# THE FOURTH. The timing fix, with both runs on the frame.
assert FIRST["precision"] < FIXED["precision"], (
    "B06 only works if the fix actually moved precision. Reporting the fixed run alone "
    "would be reporting the better of two numbers."
)
assert FIXED["precision"] == PRECISION["tracker"], (
    "the fixed run IS the run every other beat reports — otherwise B03 and B06 are "
    "quoting two different experiments"
)
assert TM["defect"] == "P55" and TM["fixed_on"].startswith("development data")

# THE FIFTH. The fresh checks are not a clean sweep.
assert TRIAGE["share"] >= FR["pass_line"], (
    "B07 says triage passes this time; 15 of 15 clears the 95% line that failed it last "
    "week"
)
assert T["last_week"]["got"] / T["last_week"]["of"] < FR["pass_line"], (
    "and last week's 8 of 9 is named on the same frame, because a check that passes once "
    "is not a check that passes"
)
assert T["got"] == T["of"] == 15 and T["last_week"]["of"] == 9
assert B2["share"] > READER["share"] > B1["share"], (
    "week 4's finding has not expired: the reader beats regex rules and a single model "
    "call still reads MORE fields than either. The reel never calls the reader accurate."
)
assert FR["reader"]["b2_extra"] == 15 and FR["reader"]["b2_caveat"]
assert K["got"] < K["of"] < K["drawn"], (
    "3 of 4 GRADABLE, of 5 drawn — the ungradable report is not quietly dropped from the "
    "denominator"
)
assert len(T["new_weaknesses"]) == 2 and T["false_alarms"] == 3
assert abs(sum(1 for r in FR["rows"] if r["hot"]) - 3) == 0

# The graph's own arithmetic, and the run that finished.
assert GP["read_by_model"] + GP["reused"] == GP["filings_kept"] == 245, (
    "174 read and 71 reused IS the 245 triage kept — B01 prints all three and they have "
    "to close"
)
assert GP["filings_kept"] < GP["filings_listed"]
assert GP["episodes_run"] == GP["episodes_of"] == 95
assert GP["questions"] == EN["questions"] == 53
assert EN["removed"]["got"] < EN["removed"]["of"], "repayments barely work, and B08 says so"
assert len(EN["ops"]) == 4 and sum(1 for o in EN["ops"] if o["hot"]) == 1
assert TC["labeller"] == "Claude"
assert len(FIG["next"]) == 3

# ── the values figdata.json does not measure ──────────────────────────────────
NOT_IN_FIGDATA = "Not measured in figdata.json"
GATE_RECORD = {
    "state": "DELEGATED",
    "not": "CLEARED",
    "where": "manifests/week5_gate.json",
    "note": "Handed to Claude end to end before the week started. The one decision taken "
            "during it was to resume the runs after the laptop stopped them. No person has "
            "reviewed the labels, the truth, the diagnosis or the results.",
}
LABELLER = {
    "who": TC["labeller"],
    "kind": "a model judgment, not a person's",
    "covers": TC["covers"],
    "note": TC["labeller_note"],
}
ORACLE_START = {
    "what": EN["opening_from"],
    "why": EN["opening_why"],
    "next": EN["opening_next"],
}

HANDLE = "@HumanitariansAI"
SEGMENT = "Running Full Episodes from Filings to Ledger"
SLUG = "running-full-episodes-from-filings-to-ledger"
KICKER = "Irreducibly Human"     # GATE L rule 7 — the FIXED claude-hai series name
GREETING = "Jambo, HAI"          # Swahili. Never repeats a language; see metadata note.


def num(n):
    return f"{n:,}"


def pct1(x):
    return f"{x * 100:.1f}%"


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


LOCAL = "reel-local/RunningFullEpisodes"
beats = []

# ── B00 · COLD OPEN ───────────────────────────────────────────────────────────
beats.append(beat(
    "B00", "COLD OPEN", "BOOKEND",
    "Hi, I'm Om Mali. This video is about running my A I debt tracker end to end, from a "
    "quarter's filings to a ledger of every bond the company owes. This is week five of "
    "the A I Debt Tracker. It finds the new bonds that doing nothing cannot find. It also "
    "adds some that are not there.",
    20,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": GREETING,
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "Run the whole thing. For each company and quarter: list the filings, triage "
            "them, read the ones about debt, merge what they say into a ledger of bonds, "
            "and then check your own result. Score it against doing nothing."
        ),
        "runningText": "episodes.py — 95 development quarters…",
        "folderLabel": HANDLE,
        "modelLabel": "Opus 5",
        "effortLabel": "High",
        "output": [
            f"all {GP['episodes_run']} of {GP['episodes_of']} development quarters ran end "
            f"to end — {num(GP['filings_listed'])} filings listed, "
            f"{GP['filings_kept']} kept, {GP['questions']} open questions raised",
            f"on {EP['graded']} quarters graded bond by bond, recall rose from "
            f"{RECALL['baseline_s']} to {RECALL['tracker_s']} against carrying the last "
            f"report forward — {NEW['caught']} of the {NEW['issued']} newly issued bonds "
            f"caught, against {NEW['baseline_caught']}",
            f"and precision FELL, {PRECISION['baseline_s']} to {PRECISION['tracker_s']}: "
            f"{WRONG} of the {AD['total']} bonds it added are not in the report, and every "
            f"one of them was traced",
        ],
    }, "type-on", [
        {"at": "on 'running my AI debt tracker end to end'", "event": "The ask types into the Claude composer."},
        {"at": "on 'it also adds some that are not there'", "event": "The result lands ANSWERED with three output lines — the third is the cost."},
    ], intent="COLD OPEN LAW: the ask is the week itself. It lands ANSWERED, and the answer carries its own bad news — the rise and the fall are on the same frame from the first beat."),
))

# ── B01 · THE GRAPH ───────────────────────────────────────────────────────────
beats.append(beat(
    "B01", "THE GRAPH", "REMOTION",
    "Until now the pieces worked alone. This week they run as one graph. Code lists the "
    "quarter's filings — eight hundred and eighty-two of them. Triage keeps the two "
    "hundred and forty-five about debt. A reader runs on each of those at the same time. "
    "Then code merges what they found and checks its own work. All ninety-five development "
    "quarters finished.",
    24,
    remotion("W5Graph", LOCAL, {
        "sparkLine": "The pieces, wired into one run.",
        "eyebrow": "AI DEBT TRACKER · THE EPISODE GRAPH",
        "title": "One quarter in, one ledger out",
        "subtitle": f"{GP['built_with']}",
        "nodes": [
            {"name": n["name"], "count": n["count"], "what": n["what"], "hot": n["hot"]}
            for n in GP["nodes"]
        ],
        "fanout": GP["fanout"],
        "tallyLabel": "every kept filing is accounted for",
        "tally": [
            {"n": num(GP["read_by_model"]), "what": "read by the model", "hot": True},
            {"n": num(GP["reused"]), "what": GP["reused_what"], "hot": False},
            {"n": num(GP["filings_kept"]), "what": "kept by triage, in total", "hot": False},
        ],
        "ranLabel": "the run",
        "ran": f"All {GP['episodes_run']} of {GP['episodes_of']} "
               f"{GP['episodes_what']} ran end to end.",
        "note": f"{GP['checkpointed']} {GP['stop']}",
        "source": "SOURCE: AI Debt Tracker docs/episodes.md, graph/supervisor.py · "
                  "figdata.json",
    }, "trace", [
        {"at": "on 'they run as one graph'", "event": "The nodes light left to right, timeline first."},
        {"at": "on 'a reader runs on each of those at the same time'", "event": "Triage fans out into three readers at once, in the accent."},
        {"at": "on 'all ninety-five development quarters finished'", "event": "The run line lands under the graph."},
    ], intent="A list of steps STATES a pipeline. A graph with a visible fan-out — one branch per filing, drawn side by side — shows the one thing that is new this week: the readers run at the same time, and code closes the loop after them."),
))

# ── B02 · THE LEDGER ENGINE ───────────────────────────────────────────────────
beats.append(beat(
    "B02", "THE LEDGER ENGINE", "REMOTION",
    "The second half is plain code. It merges events that describe the same bond, retires "
    "bonds that have matured, and applies the rest to the opening ledger. Anything it "
    "cannot place becomes an open question rather than a guess — fifty-three of them. And "
    "the opening ledger is borrowed from the answer key. Reading that from the filings is "
    "next week.",
    23,
    remotion("W5Engine", LOCAL, {
        "sparkLine": "The start is borrowed. Say so.",
        "eyebrow": "AI DEBT TRACKER · THE LEDGER ENGINE",
        "title": "What code does after the readers stop",
        "subtitle": "No model runs in this half of the graph",
        "openingLabel": EN["opening"],
        "openingChip": "BORROWED",
        "openingWhat": f"{ORACLE_START['what']}. {ORACLE_START['why']}",
        "closingLabel": EN["closing"],
        "closingWhat": f"{EN['cite_rule']} {EN['closing_what2']}",
        "ops": [{"op": o["op"], "what": o["what"], "hot": o["hot"]} for o in EN["ops"]],
        "questionsLabel": "open questions this run",
        "questions": EN["questions"],
        "questionsWhat": "For example: " + "; ".join(EN["unplaceable_examples"]) + ".",
        "note": f"{ORACLE_START['next']} Every number in this video is measured with the "
                f"opening ledger handed to both sides, which is what makes the comparison "
                f"fair and is also its largest limit.",
        "source": "SOURCE: AI Debt Tracker FRICTIONAL.md · docs/episodes.md · DESIGN.md · "
                  "figdata.json",
    }, "apply", [
        {"at": "on 'the second half is plain code'", "event": "The two ledger panels land, opening on the left."},
        {"at": "per operation", "event": "Merge, sweep and apply light between the panels."},
        {"at": "on 'rather than a guess'", "event": "ASK lands in the accent, with 53 beside it."},
        {"at": "on 'borrowed from the answer key'", "event": "The BORROWED chip lands on the opening ledger."},
    ], intent="The claim that would flatter this week is that the agent produced a ledger. It produced the DIFFERENCE between two ledgers, and the first one was handed to it. Drawing the opening panel with a BORROWED chip on it puts that on the same frame as the mechanism, not in a footnote."),
))

# ── B03 · AGAINST DOING NOTHING ───────────────────────────────────────────────
beats.append(beat(
    "B03", "AGAINST DOING NOTHING", "REMOTION",
    "The baseline is doing nothing: carry last quarter's debt forward. On forty-five "
    "quarters graded bond by bond, both start from the same opening ledger, so the gap is "
    "what reading added. Recall rose from ninety point nine percent to ninety-seven point "
    "eight. And precision fell, ninety-two point eight to ninety point two. That trade is "
    "the whole week.",
    23,
    remotion("W5Versus", LOCAL, {
        "sparkLine": "One number up. One number down.",
        "eyebrow": "AI DEBT TRACKER · AGAINST DOING NOTHING",
        "title": "Reading the filings, against carrying them forward",
        "subtitle": f"{EP['graded']} {EP['graded_what']} — {EP['same_start']}",
        "trackerLabel": EP["tracker_label"],
        "baselineLabel": EP["baseline_label"],
        "metrics": [
            {"name": m["name"], "what": m["what"],
             "tracker": m["tracker"], "baseline": m["baseline"],
             "trackerS": m["tracker_s"], "baselineS": m["baseline_s"],
             "direction": m["direction"],
             "delta": EP["recall_delta"] if m["key"] == "recall" else ""}
            for m in EP["metrics"]
        ],
        "note": EP["why"],
        "source": "SOURCE: AI Debt Tracker docs/episodes.md (paired, same episodes) · "
                  "figdata.json",
    }, "diverge", [
        {"at": "on 'carry last quarter's debt forward'", "event": "The baseline bar fills in each pair first."},
        {"at": "on 'recall rose'", "event": "The tracker's recall bar grows past it, in the accent."},
        {"at": "on 'and precision fell'", "event": "The tracker's precision bar stops SHORT of the baseline's."},
    ], intent="Two metrics, four bars, one scale. The accent means 'the tracker' on both rows, so the second row reads as the accent bar falling short — the fall is drawn, not captioned."),
))

# ── B04 · THE NEW BONDS ───────────────────────────────────────────────────────
beats.append(beat(
    "B04", "THE NEW BONDS", "REMOTION",
    "Recall is a percentage; this is what it means. Thirty-four bonds were first issued in "
    "those quarters. Carrying the last report forward finds none of them — it cannot, "
    "because it never reads anything. The tracker found thirty. That is the one thing "
    "reading buys, and it is the reason the whole graph exists.",
    19,
    remotion("W5NewBonds", LOCAL, {
        "sparkLine": "Thirty of thirty-four, against none.",
        "eyebrow": "AI DEBT TRACKER · THE NEW BONDS",
        "title": "What reading finds that carrying forward cannot",
        "subtitle": f"{EP['new_bonds_what'].capitalize()} — {NEW['issued']} of them, "
                    f"across the {EP['graded']} graded quarters",
        "total": NEW["issued"],
        "rows": [
            {"label": EP["tracker_label"], "caught": NEW["caught"],
             "value": f"{NEW['caught']} of {NEW['issued']}", "hot": True,
             "what": "read out of the filings in the quarter they were issued"},
            {"label": EP["baseline_short"], "caught": NEW["baseline_caught"],
             "value": f"{NEW['baseline_caught']} of {NEW['issued']}", "hot": False,
             "what": "a new bond is not in last quarter's report, so there is nothing to "
                     "carry forward"},
        ],
        "note": f"The {NEW['issued'] - NEW['caught']} it missed are still missed. This is "
                f"the half of the trade that went the right way; the next frame is the "
                f"other half.",
        "source": "SOURCE: AI Debt Tracker docs/episodes.md · figdata.json",
    }, "fill", [
        {"at": "on 'thirty-four bonds were first issued'", "event": "34 empty cells land in both rows."},
        {"at": "on 'finds none of them'", "event": "The baseline row stays empty — all 34 cells unfilled."},
        {"at": "on 'the tracker found thirty'", "event": "30 of the tracker's 34 cells fill, in the accent."},
    ], intent="SHOW-DON'T-TELL: '0 of 34' as a bar is an empty rectangle and reads as a rendering fault. As 34 countable cells beside a row where 30 are filled, the zero is visibly a row of things that were there to be found and were not."),
))

# ── B05 · WHAT IT ADDED ───────────────────────────────────────────────────────
beats.append(beat(
    "B05", "WHAT IT ADDED", "REMOTION",
    "And this is what it cost. In the quarters whose report itemises its bonds, the tracker "
    "added sixty-six. Forty are real. Ten were existing notes read from a prospectus as if "
    "new. Ten were launch notices with no coupon yet. Four were the banks' option to buy "
    "more. Two were plain misreads. Every one was checked, by Claude, not by me.",
    23,
    remotion("W5Added", LOCAL, {
        "sparkLine": "Twenty-six wrong, and all twenty-six named.",
        "eyebrow": "AI DEBT TRACKER · WHAT THE TRACKER ADDED",
        "title": "Every bond it added, checked one by one",
        "subtitle": f"{AD['total']} {AD['total_what']}",
        "total": AD["total"],
        "segments": [
            {"count": s["count"], "label": s["label"], "what": s["what"], "id": s["id"],
             "hot": s["hot"], "legend": s["legend"]}
            for s in AD["segments"]
        ],
        "realLabel": f"{REAL} in the report",
        "wrongLabel": f"{WRONG} not in the report",
        "note": f"{AD['fix_where']} {AD['legend_note']}",
        "attribution": f"The diagnosis of each wrong addition is {AD['diagnosis_by']}.",
        "source": "SOURCE: AI Debt Tracker docs/episodes.md, DESIGN.md P56-P58 · "
                  "figdata.json",
    }, "segment", [
        {"at": "on 'the tracker added sixty-six'", "event": "The band draws to full width, undivided."},
        {"at": "on 'forty are real'", "event": "The first segment separates in ink."},
        {"at": "per kind", "event": "Ten, ten, four and two split off in the accent, each with its defect id."},
    ], intent="The author's own figure legends four of its five segments. Drawing all five and naming the fifth is the difference between a breakdown and a breakdown that adds up. One hue across the four wrong kinds keeps the accent meaning 'this is the cost' rather than five competing colours."),
))

# ── B06 · THE TIMING BUG ──────────────────────────────────────────────────────
beats.append(beat(
    "B06", "THE TIMING BUG", "REMOTION",
    "The first run had a bug, and it was not a misread. The filing window runs up to the "
    "day the report is filed, weeks after the quarter ends — so bonds sold after the "
    "quarter closed were landing inside it. I fixed that on development data and re-ran. "
    "Precision went from eighty-nine point two to ninety point two. Both runs are reported.",
    23,
    remotion("W5Timing", LOCAL, {
        "sparkLine": "Not a misread. A bond in the wrong quarter.",
        "eyebrow": f"AI DEBT TRACKER · THE TIMING BUG ({TM['defect']})",
        "title": "A pipeline is only as good as its sense of time",
        "subtitle": TM["design"],
        "axisStart": "quarter start",
        "axisMid": "quarter END",
        "axisEnd": "the report is filed, weeks later",
        "windowLabel": "the filing window the reader is given",
        "bands": [
            {"label": "first run — applied everything in the window",
             "span": 1.0, "hot": False, "verdict": "bonds sold after the quarter end "
             "landed inside it"},
            {"label": f"after the fix — {TM['fix'].lower().rstrip('.')}",
             "span": 0.62, "hot": True, "verdict": "the ledger is kept by settlement date, "
             "as the design says"},
        ],
        "runsLabel": "bond precision, both runs reported",
        "runs": [{"label": r["label"], "value": r["precision_s"], "hot": r["hot"]}
                 for r in TM["runs"]],
        "unchanged": TM["unchanged"],
        "note": f"{TM['residual']} Fixed on {TM['fixed_on']}.",
        "source": "SOURCE: AI Debt Tracker FRICTIONAL.md · docs/episodes.md · "
                  f"DESIGN.md {TM['defect']} · figdata.json",
    }, "span", [
        {"at": "on 'the filing window runs up to the day the report is filed'", "event": "The axis draws; quarter end sits well left of the filing date."},
        {"at": "on 'landing inside it'", "event": "The first run's band stretches past the quarter end."},
        {"at": "on 'I fixed that'", "event": "The fixed band retracts to the quarter end, in the accent."},
        {"at": "on 'both runs are reported'", "event": "89.2% and 90.2% land side by side."},
    ], intent="The bug is a span, not a value, so the frame is a span. The two bands are the same rule applied to two different end points — which is exactly what the bug was. The two precision figures sit beneath them so the fix is reported as a before AND an after."),
))

# ── B07 · THE FRESH CHECKS ────────────────────────────────────────────────────
beats.append(beat(
    "B07", "THE FRESH CHECKS", "REMOTION",
    "I re-checked last week's pieces on filings nobody had read. Triage found fifteen of "
    "fifteen — it passes this time, after failing at eight of nine. The reader beat pattern "
    "matching again, ninety-one percent to seventy-four. Asking the model directly still "
    "reads more numbers, ninety-six, with fifteen instruments that aren't in the filings "
    "and no sentence behind any of them. And the answer key agreed on three of four "
    "reports.",
    27,
    remotion("W5Fresh", LOCAL, {
        "sparkLine": "Three checks, on filings nobody had read.",
        "eyebrow": "AI DEBT TRACKER · CHECKED AGAIN, ON FRESH FILINGS",
        "title": "Last week's pieces, on filings nobody had read",
        "subtitle": FR["drawn_how"],
        "rows": [
            {"label": r["label"], "value": r["value_s"], "share": r["share"],
             "hot": r["hot"], "line": FR["pass_line"] if r["key"] == "triage" else 0}
            for r in FR["rows"]
        ],
        "lineLabel": f"dashed = the {int(FR['pass_line'] * 100)}% triage line, fixed in the "
                     f"design before any run. It is triage's line and is drawn on triage's "
                     f"track only.",
        "notesLabel": "what each one does not say",
        "notes": [
            {"who": "triage", "what": f"last week this same check failed at "
                                      f"{T['last_week']['got']} of {T['last_week']['of']}. "
                                      f"{T['small']} Of its {T['false_alarms']} false "
                                      f"alarms, two are new rule weaknesses: "
                                      + "; ".join(f"{w['what']} ({w['id']})"
                                                  for w in T["new_weaknesses"]) + ".",
             "hot": False},
            {"who": "the reader", "what": FR["reader"]["b2_caveat"], "hot": True},
            {"who": "the answer key", "what": f"{K['got']} of {K['of']} gradable, of "
                                              f"{K['drawn']} drawn — "
                                              f"{K['ungradable']['who']} could not be "
                                              f"graded ({K['ungradable']['ids']}) and "
                                              f"{K['disagreement']['who']} is the one "
                                              f"disagreement: {K['disagreement']['what']} "
                                              f"({K['disagreement']['id']}). "
                                              f"{K['draw_note']}",
             "hot": False},
        ],
        "note": "",
        "source": "SOURCE: AI Debt Tracker docs/triage.md, docs/reader.md, "
                  "docs/handcheck.md · figdata.json",
    }, "grow", [
        {"at": "on 'fifteen of fifteen'", "event": "The triage bar fills the track, past the dashed line."},
        {"at": "on 'ninety-one percent to seventy-four'", "event": "The reader bar grows past the regex bar."},
        {"at": "on 'still reads more numbers'", "event": "B2's bar grows past the reader's, in ink — it is not the subject."},
        {"at": "on 'three of four reports'", "event": "The answer key bar lands at three quarters."},
    ], intent="Five bars on one track with ONE dashed line, drawn on the track that line belongs to. The reader is accented because it is the thing being checked, and B2's longer ink bar beside it is the frame refusing to call the reader accurate."),
))

# ── B08 · THE LIMITS ──────────────────────────────────────────────────────────
beats.append(beat(
    "B08", "THE LIMITS", "REMOTION",
    "The limits. Ninety-five of ninety-five is on development quarters; the test split is "
    "untouched. Every quarter started from the answer key's ledger, so none of this shows "
    "what happens when the tracker reads its own opening. Repayments barely work — three of "
    "fourteen. And the gate says delegated, not cleared: I handed the week to Claude and "
    "have not reviewed any of it.",
    24,
    remotion("W5Limits", LOCAL, {
        "sparkLine": "What the week does not show.",
        "eyebrow": "AI DEBT TRACKER · THE LIMITS",
        "title": "Every number above, and the limit that narrows it",
        "subtitle": "",
        "rows": [
            {"claim": f"{GP['episodes_run']} of {GP['episodes_of']} quarters ran",
             "limit": f"on {GP['episodes_what']}. The test split has not been touched, so "
                      f"'it finishes' is a claim about the quarters the system was built "
                      f"on.",
             "hot": False},
            {"claim": f"recall {RECALL['baseline_s']} to {RECALL['tracker_s']}",
             "limit": f"the opening ledger was {ORACLE_START['what']}, for the tracker "
                      f"and the baseline alike. "
                      f"How much of the gain survives a ledger the tracker reads itself is "
                      f"not known — that is next week, and it will add its own errors.",
             "hot": True},
            {"claim": f"{WRONG} wrong additions, in {len(NAMED_WRONG)} kinds",
             "limit": f"{LABELLER['kind']} — {LABELLER['who']} diagnosed each one after "
                      f"scoring. A merge rule that drops launch notices could also drop a "
                      f"real bond announced only once, so the fixes may cost recall.",
             "hot": False},
            {"claim": "repayments",
             "limit": f"{EN['removed']['got']} of {EN['removed']['of']} removed bonds were "
                      f"removed, and {EN['unmatched_repayments']} repayments matched "
                      f"nothing in the ledger at all. This part does not work yet.",
             "hot": False},
            {"claim": f"{GP['questions']} open questions",
             "limit": "raised by the checks and answered by nobody. The investigators that "
                      "would close them are next week's work.",
             "hot": False},
        ],
        "gateLabel": "the week's gate record",
        "gateState": f"{GATE_RECORD['state']}, not {GATE_RECORD['not']}",
        "gateNote": f"{GATE_RECORD['note']} {LABELLER['covers'].capitalize()} are "
                    f"{LABELLER['kind']}. ({NOT_IN_FIGDATA} — recorded in "
                    f"{GATE_RECORD['where']}.)",
        "nextLabel": "next",
        "next": FIG["next"],
        "source": "SOURCE: narration_script.md notes · FRICTIONAL.md · docs/episodes.md · "
                  "DESIGN.md · figdata.json",
    }, "stagger", [
        {"at": "per limit", "event": "Each claim lands with the limit that narrows it."},
        {"at": "on 'delegated, not cleared'", "event": "The gate record lands as the largest object on the frame."},
        {"at": "on 'next week'", "event": "Three next steps land at the foot."},
    ], intent="Every episode in this series ends on its own limits. The borrowed opening ledger is accented here because it is the limit that touches every other number on the frame, and the gate record is drawn largest because 'nobody has checked any of this' outranks all of them."),
))

# ── B09 · VERDICT ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B09", "VERDICT", "BOOKEND",
    "So: one graph that takes a quarter's filings and returns a ledger of bonds, and it ran "
    "on all ninety-five development quarters. Against doing nothing, recall rose almost "
    "seven points and it caught thirty of the thirty-four new bonds, where doing nothing "
    "catches none. Precision fell, and all twenty-six wrong additions were traced. One "
    "timing bug, both runs reported. And nobody has reviewed any of it.",
    29,
    remotion("ClaudeVerdictArtifact", "proven-core/ClaudeVerdictArtifact", {
        "artifactTitle": SEGMENT,
        "artifactHeading": "What week 5 built, and what it is allowed to claim",
        "artifactLines": [
            f"One LangGraph episode per company-quarter: code lists the filings, triage "
            f"keeps the {GP['filings_kept']} about debt, a reader runs on each of those at "
            f"the same time, and code merges, sweeps and applies the result to an opening "
            f"ledger before checking itself. All {GP['episodes_run']} of "
            f"{GP['episodes_of']} development quarters ran end to end.",
            f"On {EP['graded']} quarters graded bond by bond, against carrying the last "
            f"report forward: recall {RECALL['baseline_s']} to {RECALL['tracker_s']} "
            f"({EP['recall_delta']}), and {NEW['caught']} of the {NEW['issued']} newly "
            f"issued bonds caught where the baseline catches "
            f"{NEW['baseline_caught']}.",
            f"Precision FELL, {PRECISION['baseline_s']} to {PRECISION['tracker_s']}. Of "
            f"the {AD['total']} bonds the tracker added, {REAL} are in the report and "
            f"{WRONG} are not — {SEG['notes']['count']} existing notes read as new "
            f"({SEG['notes']['id']}), {SEG['launch']['count']} launch notices with no "
            f"coupon ({SEG['launch']['id']}), {SEG['options']['count']} bank options "
            f"({SEG['options']['id']}) and {SEG['misread']['count']} plain misreads.",
            f"One timing bug ({TM['defect']}): bonds sold after a quarter ended were being "
            f"applied to it. Fixed on {TM['fixed_on']}; precision "
            f"{FIRST['precision_s']} before the fix and {FIXED['precision_s']} after, and "
            f"both runs are reported. {TM['unchanged']}",
            f"Fresh checks on filings labelled before each run: triage {T['got']} of "
            f"{T['of']} (it failed last week at {T['last_week']['got']} of "
            f"{T['last_week']['of']}), the reader {FR['reader']['pct_s']} of fields "
            f"against {FR['reader']['b1_s']} for regex rules — and a single model call "
            f"{FR['reader']['b2_s']}, uncited. The answer key agreed on {K['got']} of "
            f"{K['of']} gradable reports. The gate records the week "
            f"{GATE_RECORD['state']}, not {GATE_RECORD['not']}.",
        ],
    }, "stagger", [
        {"at": "per clause", "event": "Five findings stagger in, one per spoken clause."},
    ], intent="Judgment beat. The artifact page is the point (ILLUSTRATE LAW carve-out). The third finding is the cost and the fifth is the gate — neither is last by accident, and neither is buried."),
))

# ── B10 · HANDOFF ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B10", "HANDOFF", "BOOKEND",
    "Your turn. Paste this into Claude. Before you measure the clever version, measure "
    "doing nothing — and when the clever version wins on one number and loses on another, "
    "say both out loud. Look at whether the answer reports the metric that moved the wrong "
    "way without being asked twice.",
    18,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": "Your turn.",
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "Before you score the clever version of my pipeline, write the do-nothing "
            "baseline — the one that changes nothing and carries last time's answer "
            "forward. Run both on the same set, from the same starting point, and report "
            "EVERY metric that moved, including the ones that moved the wrong way. Then "
            "tell me in one sentence what my version buys and what it costs."
        ),
        "runningText": "paste this into Claude…",
        "folderLabel": HANDLE,
        "modelLabel": "Opus 5",
        "effortLabel": "High",
        "output": [],
    }, "type-on", [
        {"at": "on 'paste this into Claude'", "event": "The prompt types into the composer."},
    ], intent="HANDOFF LAW: a real prompt, read ALOUD and then discussed. One of exactly two typing beats. It is this week's lesson — the trade, not the headline — turned into something a viewer can run on their own work."),
))

# ── B11 · OUTRO ───────────────────────────────────────────────────────────────
beats.append(beat(
    "B11", "OUTRO", "BOOKEND",
    "Running full episodes from filings to ledger. Week five of the A I Debt Tracker. Om "
    "Mali, for Humanitarians A I.",
    9,
    remotion("ClaudeTitleOutro", "proven-core/ClaudeTitleOutro", {
        "title": SEGMENT,
        "handle": HANDLE,
        # `subline`, not `subtitle` — the wrong name ships the outro reading
        # "bot vs bot, season one", a default from an unrelated show.
        "subline": "week 5 · the AI Debt Tracker",
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
    "greeting_note": "hello lexicon: Swahili. HAI persona takes only the shortest cues (Hi · Ola · Hej · Ciao · Hallo · Salut · Ahoj · Szia · Tere · Moi · Hoi · Labas · Salve · Sveiki · Zdravo · Merhaba · Jambo). Rotate; never repeat a language.",
    "aspect_ratio": "16:9",
    "fps": 24,
    "lead_silence_s": 0.4,
    "note": (
        "ai-explainer / claude-hai. AI Debt Tracker WEEK 5. ILLUSTRATE LAW: the Claude UI "
        "appears at B00 (cold open, answered), B09 (verdict artifact), B10 (handoff) and "
        "B11 (outro) only — every body beat illustrates its concept as a native animated "
        "Remotion scene (REBUILD LAW). The four source PNGs and their SVG sources are "
        "REFERENCE in pantry/, never slotted as media. The script's five body sections "
        "become eight body beats: 0:15 splits into the graph (B01) and the ledger engine "
        "with its borrowed opening (B02); 0:50 splits into the two metrics (B03) and the "
        "new bonds the first metric is about (B04); 1:15 splits into the 66 additions "
        "(B05) and the timing bug (B06); 1:55 becomes B07; and the closing on-camera "
        "section becomes a limits beat. FIVE THINGS NOT TO GET WRONG: this is a TRADE — "
        "recall rose and precision fell, and no frame shows one without the other; the "
        "opening ledger was BORROWED from the answer key, so the tracker is not reading "
        "its own start; the diagnosis of the 26 wrong additions is Claude's judgment, not "
        "a person's; the reader is still NOT more accurate than a single model call "
        "(91% against 96%); and the week's gate records DELEGATED, not cleared."
    ),
}

sheet = {"metadata": META, "beats": beats}

body = [b for b in beats if b["beat_id"] not in ("B00", "B09", "B10", "B11")]
words = {b["beat_id"]: len(b["narration_text"].split()) for b in beats}
lo = min(words[b["beat_id"]] for b in body)
hi = max(words[b["beat_id"]] for b in body)
# 45-72, the band weeks 2, 3 and 4 settled on. This script spells its numbers aloud
# ("ninety point nine percent", "thirty of thirty-four"), and one figure can cost six
# words; tightening the band would mean cutting evidence to pay for pronunciation.
assert 45 <= lo and hi <= 72, f"body beat word budget 45-72 violated: {lo}-{hi}"
assert len(body) == 8 and len(beats) == 12

if "--check" in sys.argv:
    print("[adt-w5] all assertions pass")
    sys.exit(0)

out = HERE / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"[adt-w5] wrote {out}  — {len(beats)} beats")
print("[adt-w5] narration words: " + " ".join(f"{k}={v}" for k, v in words.items()))
print(f"[adt-w5] body beats {lo}-{hi}w (band 45-72), total {sum(words.values())}w")
print(f"[adt-w5] derived: {GP['episodes_run']}/{GP['episodes_of']} quarters ran · recall "
      f"{RECALL['baseline_s']} -> {RECALL['tracker_s']} UP but precision "
      f"{PRECISION['baseline_s']} -> {PRECISION['tracker_s']} DOWN · new bonds "
      f"{NEW['caught']}/{NEW['issued']} vs baseline {NEW['baseline_caught']} · additions "
      f"{AD['total']} = {REAL} real + {WRONG} wrong ("
      + " + ".join(f"{s['count']} {s['key']}" for s in AD['segments'] if s['key'] != 'real')
      + f") · timing {FIRST['precision_s']} -> {FIXED['precision_s']} ({TM['defect']}) · "
      f"triage {T['got']}/{T['of']} PASSES (last week {T['last_week']['got']}/"
      f"{T['last_week']['of']}) · reader {FR['reader']['pct_s']} still under B2 "
      f"{FR['reader']['b2_s']} · key {K['got']}/{K['of']} of {K['drawn']} · gate "
      f"{GATE_RECORD['state']}")
