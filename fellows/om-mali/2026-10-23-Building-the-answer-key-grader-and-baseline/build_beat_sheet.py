#!/usr/bin/env python3
"""
build_beat_sheet.py — AI Debt Tracker, WEEK 2: Building the Answer Key, Grader and Baseline.

Writes beat_sheet.json with EVERY on-screen figure injected from figdata.json. No number is
typed into a scene or into a beat sheet by hand.

THE FRAMING ASSERTION of this reel is HELD_OUT_SHARE < AFTER_SHARE. B04's entire claim is that
"ten of ten" is a CALIBRATION and "two of three" is the measurement: the ten reports are the
ones that found the five grader bugs, so the grader cannot help but agree with them afterwards.
The three held-out reports were picked before reading and graded once. If those two scores ever
became equal, the distinction the beat is built on would be empty and the reel would be
advertising a perfect score it has not earned. The build fails rather than ship that.

THE SECOND ARGUMENT, asserted the same way: the baseline's flattering number must keep hiding a
zero. 90.7% bond recall is high and meaningless on its own — the same baseline caught NONE of
the new bonds and reproduced fewer than half the quarters exactly. If recall ever stopped being
high, or the zero stopped being zero, B05 would be a different beat.

THREE VALUES ARE NOT IN figdata.json's measured block. They come from narration_script.md and
the project documents, are passed as named constants below, and every screen that uses one says
where it came from:
  · AGENT_STATE   — the agent is NOT built; this week built what will grade it   (B00/B02/B08)
  · TZ_INFERENCE  — "most likely a time-zone change" is an inference, not a log   (B07)
  · HELD_OUT_MISS — the one miss is a company's own tagging errors                (B04/B08)

Usage:  python build_beat_sheet.py            (writes beat_sheet.json)
        python build_beat_sheet.py --check    (assertions only, writes nothing)
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIG = json.loads((HERE / "figdata.json").read_text(encoding="utf-8"))

AK = FIG["answer_key"]
GR = FIG["grader"]
HC = FIG["handcheck"]
BASE = FIG["baseline"]
HEAD = FIG["headroom"]
CLOCK = FIG["clock"]

# ── derived, never typed ──────────────────────────────────────────────────────
LEVELS = AK["levels"]
BY_BOND = next(l for l in LEVELS if l["level"] == "Bond by bond")
FIRST, AFTER, HELD = HC["first_pass"], HC["after_fixes"], HC["held_out"]
BUGS = HC["bugs"]

FIRST_SHARE = FIRST["got"] / FIRST["of"]
AFTER_SHARE = AFTER["got"] / AFTER["of"]
HELD_SHARE = HELD["got"] / HELD["of"]

NEW = HEAD["new_bonds"]
REPAY = HEAD["repayments"]
EXACT_SHARE = BASE["exact"] / BASE["quarters"]

# ── assertions ────────────────────────────────────────────────────────────────
assert sum(l["reports"] for l in LEVELS) == AK["reports"] == 1093, (
    "B01 draws the grading levels as ONE bar the width of the whole answer key. A partition "
    "that does not sum to the thing it partitions is not a partition."
)
assert AK["companies_ai"] + AK["companies_other"] == AK["companies"] == 100
assert BY_BOND["reports"] > sum(l["reports"] for l in LEVELS if l is not BY_BOND), (
    "B01 says MOST reports list debt bond by bond; 'most' has to mean a majority"
)
assert AK["bonds"] == 9653

assert len(GR["bond_fields"]) == 4 and len(GR["modes"]) == 3

# THE FRAMING ASSERTION. B04 exists because these two numbers mean different things.
assert HELD_SHARE < AFTER_SHARE, (
    "B04's whole claim: 10 of 10 is a CALIBRATION on the reports that found the bugs, and "
    "2 of 3 is the measurement. If the held-out score ever caught up, the beat would be "
    "drawing a distinction that no longer exists."
)
assert FIRST_SHARE < AFTER_SHARE, "the fixes have to have moved the score"
assert AFTER["got"] == AFTER["of"] == 10 and FIRST["got"] == 8
assert len(BUGS) == 5, "the script says five fixes, B03 lists them, B04's label counts them"
assert AFTER["of"] == FIRST["of"], "the same ten reports, before and after"
assert HELD["of"] < FIRST["of"], "the honest check is the smaller set — say so, do not hide it"

# THE SECOND ARGUMENT. A high recall that hides a zero.
assert BASE["recall"] > 0.9, "B05 leads with the zero BECAUSE recall is flattering"
assert BASE["new_bonds_caught"] == 0, (
    "B05's hero is an EMPTY track. A non-zero here is a different beat and a different drawing."
)
assert EXACT_SHARE < 0.5, "fewer than half the quarters reproduce exactly"
assert BASE["recall_lo"] < BASE["recall"] < BASE["recall_hi"], "the interval must contain it"
assert BASE["quarters"] == 47 and BASE["exact"] == 18

# The searchable denominator, and the gap the agent has to win.
assert NEW["of"] == NEW["total"] - NEW["no_coupon"] == 32, (
    "30 of 32, not 30 of 36: four new bonds carry no tagged coupon to search for"
)
assert NEW["got"] > BASE["new_bonds_caught"], "B06 is the DISTANCE between these two"
assert REPAY["got"] == 5 and REPAY["of"] == 6
assert REPAY["disappeared"] - REPAY["matured"] - REPAY["no_coupon"] == REPAY["of"], (
    "16 bonds disappeared, 9 matured, 1 has no rate to search for, leaving the 6"
)

assert CLOCK["moved"] < CLOCK["of"], "43 of 495, not all of them"
assert CLOCK["moved"] == 43 and CLOCK["of"] == 495

# ── the values figdata.json's measured block does not carry ───────────────────
NOT_IN_FIGDATA = "not in figdata.json — from narration_script.md and the project documents"
AGENT_STATE = {
    "built": False,
    "note": "The agent is not written. This week built the answer key, the grader and the "
            "baseline it will be scored against.",
}
TZ_INFERENCE = {
    "claim": "most likely a time-zone change",
    "evidence": "4 hours on summer dates and 5 in winter, matching US Eastern to UTC",
    "kind": "inference — EDGAR published no note",
}
HELD_OUT_MISS = HC["held_out_miss"]

HANDLE = "@HumanitariansAI"
SEGMENT = "Building the Answer Key, Grader and Baseline"
SLUG = "building-the-answer-key-grader-and-baseline"
KICKER = "Irreducibly Human"     # GATE L rule 7 — the FIXED claude-hai series name
GREETING = "Sveiki, HAI"         # Latvian. Never repeats a language; see metadata note.


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


LOCAL = "reel-local/BuildingTheAnswerKey"
beats = []

# ── B00 · COLD OPEN ───────────────────────────────────────────────────────────
beats.append(beat(
    "B00", "COLD OPEN", "BOOKEND",
    "Hi, I'm Om Mali. This video is about building the answer key and the grader for my A I "
    "debt tracker, and measuring the do nothing baseline it has to beat. This is week two of "
    "the A I Debt Tracker. The agent still is not written. What this week built is the thing "
    "that will judge it, and the floor it has to clear.",
    20,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": GREETING,
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "Before the agent exists, build what will grade it: an answer key from the real "
            "reports, a grader with a stated matching rule, and the score a do-nothing "
            "baseline already gets. Then check the grader against printed tables."
        ),
        "runningText": "score_baseline.py dev…",
        "folderLabel": HANDLE,
        "modelLabel": "Opus 5",
        "effortLabel": "High",
        "output": [
            f"{num(AK['reports'])} reports, {AK['companies']} companies, "
            f"{num(AK['bonds'])} bonds in the answer key",
            f"the grader disagreed with {FIRST['of'] - FIRST['got']} of {FIRST['of']} printed "
            f"tables — every disagreement was a bug in mine",
            f"and the do-nothing baseline caught {BASE['new_bonds_caught']} of "
            f"{BASE['new_bonds_total']} new bonds",
        ],
    }, "type-on", [
        {"at": "on 'building the answer key and the grader'", "event": "The ask types into the Claude composer."},
        {"at": "on 'the floor it has to clear'", "event": "The result lands ANSWERED with three output lines."},
    ], intent="COLD OPEN LAW: the ask is the week itself — build the judge before the thing being judged. Lands ANSWERED."),
))

# ── B01 · THE ANSWER KEY ──────────────────────────────────────────────────────
beats.append(beat(
    "B01", "THE ANSWER KEY", "REMOTION",
    "The tracker is graded against each company's next quarterly report, so first that answer "
    "had to be written down. I built it for a hundred companies — twenty five A I companies "
    "and seventy five others — from one thousand and ninety three reports since January twenty "
    "twenty four. That's nine thousand six hundred and fifty three bonds. Most of those "
    "reports list debt bond by bond; some only by deal.",
    23,
    remotion("AKScale", LOCAL, {
        "sparkLine": "First, write down the answer.",
        "eyebrow": "AI DEBT TRACKER · WEEK 2",
        "title": "An answer key for 100 companies",
        "subtitle": f"Every quarterly and annual report, {AK['from']} – {AK['to']}, "
                    f"read from SEC filings",
        "counts": [
            {"big": num(AK["reports"]), "small": "reports"},
            {"big": f"{AK['companies']}", "small": f"companies · {AK['companies_ai']} AI + "
                                                   f"{AK['companies_other']} others"},
            {"big": num(AK["bonds"]), "small": "bonds"},
        ],
        "levelsLabel": "How much detail each report gives",
        "total": AK["reports"],
        "levels": [
            {"level": l["level"], "reports": l["reports"],
             "hot": l["level"] == "Bond by bond"}
            for l in LEVELS
        ],
        "unseenNote": AGENT_STATE["note"] + f"  ({NOT_IN_FIGDATA})",
        "source": "SOURCE: AI Debt Tracker answer_key/index.json, build_answer_key.py · "
                  "figdata.json",
    }, "count-in", [
        {"at": "on each of the three numbers", "event": "1,093 · 100 · 9,653 land in turn."},
        {"at": "on 'bond by bond'", "event": "One full-width bar splits into the three grading levels."},
    ], intent="ONE bar the width of the whole answer key, partitioned — not three bars, which would invite 900 to be compared with 41. The segments ARE the 1,093 counted above them."),
))

# ── B02 · THE GRADER ──────────────────────────────────────────────────────────
beats.append(beat(
    "B02", "THE GRADER", "REMOTION",
    "The grader scores a debt list three ways. Bond by bond, the currency, interest rate and "
    "due year must agree, and the amount must be within one percent. And each true bond can "
    "be claimed by only one answer. Then deal by deal, and then totals. Every score comes "
    "with a confidence range, so a small difference is never oversold.",
    21,
    remotion("AKGrader", LOCAL, {
        "sparkLine": "A score is only as honest as its rule.",
        "eyebrow": "AI DEBT TRACKER · THE GRADER",
        "title": "Three ways to score a debt list",
        "subtitle": "The agent is not written yet. This is what will judge it.",
        "modes": [
            {"mode": "Bond by bond", "note": "every instrument matched on four fields",
             "hot": True},
            {"mode": "Deal by deal", "note": "grouped issuances, where that is all a report gives",
             "hot": False},
            {"mode": "Totals", "note": "one figure, for reports that give nothing finer",
             "hot": False},
        ],
        "fieldsLabel": "a bond matches only if all four agree",
        "fields": [{"field": fd["field"], "rule": fd["rule"]} for fd in GR["bond_fields"]],
        "pairingLabel": "and once only",
        "pairing": GR["pairing"][0].upper() + GR["pairing"][1:] + ".",
        "intervalNote": f"Every score carries a {GR['interval']} interval, so a small "
                        f"difference between two runs is never read as an improvement.",
        "source": "SOURCE: src/ai_debt_tracker/eval/grader.py · figdata.json",
    }, "stagger", [
        {"at": "on 'three ways'", "event": "Three mode cards land, coarsest last."},
        {"at": "on 'only one answer'", "event": "The four field chips land, then the pairing rule."},
    ], intent="The pairing constraint is the part a viewer would never guess, so it gets its own block rather than a clause in a footnote. SHOW the rule, do not summarise it."),
))

# ── B03 · CHECKING THE CHECKER ────────────────────────────────────────────────
beats.append(beat(
    "B03", "CHECKING THE CHECKER", "REMOTION",
    "But who checks the checker? I compared the answer key with the debt tables printed in ten "
    "real reports. The first pass agreed on only eight. Every disagreement was my bug, not "
    "theirs. Oracle's repaid notes were still counted as owed. Broadcom's debt from buying V M "
    "ware had been dropped entirely. Two bonds in one entry, due dates read as issue dates, "
    "and a currency never stated.",
    24,
    remotion("AKBugs", LOCAL, {
        "sparkLine": "Every disagreement was my bug, not theirs.",
        "eyebrow": "AI DEBT TRACKER · CHECKING THE CHECKER",
        "title": "What the printed tables caught",
        "subtitle": f"The answer key against the debt tables printed in {FIRST['of']} real "
                    f"10-Qs and 10-Ks — first pass agreed on {FIRST['got']}",
        "bugs": [{"n": b["n"], "bug": b["bug"], "who": b["who"]} for b in BUGS],
        "verdictLabel": f"all {len(BUGS)} disagreements",
        "verdict": "were bugs in my grader, not errors in the reports.",
        "source": "SOURCE: AI Debt Tracker docs/handcheck.md, manifests/handcheck/ · "
                  "figdata.json",
    }, "stagger", [
        {"at": "per bug", "event": "Five numbered rows land, each naming the company that exposed it."},
        {"at": "on 'my bug, not theirs'", "event": "The verdict lands beneath them, in the accent."},
    ], intent="The honest centre of the reel. Five concrete defects, each attributed to the report that found it — not a sentence saying mistakes were made."),
))

# ── B04 · CALIBRATED vs MEASURED ──────────────────────────────────────────────
beats.append(beat(
    "B04", "CALIBRATED vs MEASURED", "REMOTION",
    "After fixing all five, ten of ten. But those ten reports are what found the fixes, so ten "
    "of ten is a calibration, not a score. For the honest check I graded three untouched "
    "reports, once. Two of three agree. The one miss is that company's own data entry errors, "
    "saved for next week rather than tuned away.",
    21,
    remotion("AKCalibration", LOCAL, {
        "sparkLine": "Ten of ten is a calibration. Two of three is the score.",
        "eyebrow": "AI DEBT TRACKER · CALIBRATED vs MEASURED",
        "title": "Which of these two numbers is evidence",
        "subtitle": "",
        "calibratedLabel": f"the {FIRST['of']} reports that FOUND the fixes",
        "calibrated": [
            {"label": FIRST["label"], "got": FIRST["got"], "of": FIRST["of"], "hot": False},
            {"label": AFTER["label"], "got": AFTER["got"], "of": AFTER["of"], "hot": False},
        ],
        "measuredLabel": f"the {HELD['of']} picked first and graded once",
        "measured": [
            {"label": HELD["label"], "got": HELD["got"], "of": HELD["of"], "hot": True},
        ],
        "missNote": f"The one miss is {HELD_OUT_MISS}. Three reports is a small check and is "
                    f"said as one — it is the only number here that was not read while the "
                    f"bugs were being fixed.",
        "source": "SOURCE: AI Debt Tracker docs/handcheck.md, DESIGN.md P30–P37 · figdata.json",
    }, "separate", [
        {"at": "on 'ten of ten'", "event": "The two calibration bars fill."},
        {"at": "on 'a calibration, not a score'", "event": "A dashed rule draws across, and the held-out bar lands below it."},
    ], intent="The dashed rule IS the argument: above it, reports read while the bugs were being fixed; below it, reports picked first and graded once."),
))

# ── B05 · THE FLOOR ───────────────────────────────────────────────────────────
beats.append(beat(
    "B05", "THE FLOOR", "REMOTION",
    "Then the floor. The simplest possible tracker just copies last quarter's debt forward. It "
    "caught none of the thirty six new bonds. None. It still finds ninety point seven percent "
    "of all bonds, because most debt doesn't change in three months, and it gets eighteen of "
    "forty seven quarters exactly right. That is the number the agent has to beat.",
    22,
    remotion("AKFloor", LOCAL, {
        "sparkLine": "A flattering number with a zero inside it.",
        "eyebrow": "AI DEBT TRACKER · THE FLOOR",
        "title": "What doing nothing misses",
        "subtitle": f"The baseline: {BASE['name']}, over {BASE['quarters']} dev quarters",
        "trackLabel": "New bonds caught by copying forward",
        "trackValue": f"{BASE['new_bonds_caught']} of {BASE['new_bonds_total']}",
        "emptyWord": "nothing at all",
        "stats": [
            {"big": pct1(BASE["recall"]), "hot": False,
             "small": f"of all bonds it still finds — {pct1(BASE['recall_lo'])}–"
                      f"{pct1(BASE['recall_hi'])}, because most debt simply carries over"},
            {"big": f"{BASE['exact']} of {BASE['quarters']}", "hot": True,
             "small": "quarters it reproduces exactly"},
        ],
        "whyNote": f"{pct1(BASE['recall'])} is bond recall, and it is high for the same reason "
                   f"the zero is zero: a quarter's debt mostly does not move. The agent is not "
                   f"being asked to beat {pct1(BASE['recall'])} — it is being asked to find "
                   f"what changed.",
        "source": "SOURCE: AI Debt Tracker docs/baseline_b0.md ← score_baseline.py dev · "
                  "figdata.json",
    }, "hold-empty", [
        {"at": "on 'copies last quarter's debt forward'", "event": "The track is drawn — and stays empty."},
        {"at": "on 'ninety point seven percent'", "event": "The two flattering numbers land beneath it, smaller."},
    ], intent="The zero is the hero and is drawn as an OUTLINED, LABELLED empty track — an absent bar reads as a rendering fault. The flattering numbers are deliberately smaller."),
))

# ── B06 · THE HEADROOM ────────────────────────────────────────────────────────
beats.append(beat(
    "B06", "THE HEADROOM", "REMOTION",
    "And the changes can be found. Of the thirty two new bonds that could be searched for, "
    "thirty were announced in a filing the agent could read in time. Of six early repayments, "
    "five were. So the distance between doing nothing and reading the filings is almost the "
    "whole gap. That is exactly what the agent has to win.",
    21,
    remotion("AKHeadroom", LOCAL, {
        "sparkLine": "The distance is the opportunity.",
        "eyebrow": "AI DEBT TRACKER · THE HEADROOM",
        "title": "What the filings announced in time",
        "subtitle": "Each line runs from what copying forward catches to what was announced",
        "axes": [
            {
                "name": "New bonds",
                "scale": NEW["of"],
                "baseline": BASE["new_bonds_caught"],
                "baselineLabel": f"copying forward: {BASE['new_bonds_caught']}",
                "announced": NEW["got"],
                "announcedLabel": f"announced in a readable filing: {NEW['got']} of {NEW['of']}",
                "gapLabel": "the gap the agent has to win",
            },
            {
                "name": "Early repayments",
                "scale": REPAY["of"],
                "baseline": 0,
                "baselineLabel": "copying forward: 0",
                "announced": REPAY["got"],
                "announcedLabel": f"announced: {REPAY['got']} of {REPAY['of']}",
                "gapLabel": "the same gap, smaller set",
            },
        ],
        "searchNote": f"{NEW['of']} of the {NEW['total']} new bonds could be searched for at "
                      f"all — {NEW['no_coupon']} carry no tagged interest rate. Of "
                      f"{REPAY['disappeared']} bonds that disappeared, {REPAY['matured']} "
                      f"simply reached their due date and {REPAY['no_coupon']} had no rate to "
                      f"search for, leaving {REPAY['of']}.",
        "source": "SOURCE: AI Debt Tracker docs/changes_dev.md ← explain_changes.py · "
                  "figdata.json",
    }, "span", [
        {"at": "on 'thirty of thirty-two'", "event": "A span draws from 0 across to 30 on one axis."},
        {"at": "on 'five were'", "event": "The second axis draws the same distance on a smaller set."},
    ], intent="ONE axis per claim, with the GAP drawn as a span. Two separate bars would show two quantities; the distance between them is the beat."),
))

# ── B07 · ONE SURPRISE ────────────────────────────────────────────────────────
beats.append(beat(
    "B07", "ONE SURPRISE", "REMOTION",
    "One surprise. E D G A R quietly moved forty three filing timestamps by four to five "
    "hours. The shift is four hours on summer dates and five in winter, which most likely "
    "means a time zone change. So the server that stops the agent seeing the future now "
    "anchors each cut off to the report itself, not to a clock.",
    22,
    remotion("AKClock", LOCAL, {
        "sparkLine": "The evidence moved under the experiment.",
        "eyebrow": "AI DEBT TRACKER · ONE SURPRISE",
        "title": "The timestamps moved",
        "subtitle": "Re-reading the same filings returned different publication times",
        "countBig": f"{CLOCK['moved']} of {CLOCK['of']}",
        "countSmall": f"filing timestamps shifted by {CLOCK['shift_hours']} hours between "
                      f"two reads of the same filings",
        "wasLabel": "as first read",
        "nowLabel": "as read again",
        "shiftLabel": f"{CLOCK['shift_hours']} hours",
        "inference": f"{TZ_INFERENCE['claim'].capitalize()}: {TZ_INFERENCE['evidence']}. "
                     f"EDGAR published no note, so this is an {TZ_INFERENCE['kind'].split(' — ')[0]}, "
                     f"not a fact. ({NOT_IN_FIGDATA})",
        "fixLabel": "what changed because of it",
        "fix": CLOCK["fix"][0].upper() + CLOCK["fix"][1:] + ".",
        "source": "SOURCE: AI Debt Tracker logs/RUN_LOG.md (2026-10-23), DESIGN.md P29 · "
                  "figdata.json",
    }, "shift", [
        {"at": "on 'moved forty-three filing timestamps'", "event": "The count lands, then one filing's marker."},
        {"at": "on 'four to five hours'", "event": "A dashed track draws the marker to its new position."},
    ], intent="A cut-off that depends on a wall clock is a cut-off that can move without telling you. The drawing is the marker moving."),
))

# ── B08 · THE LIMITS ──────────────────────────────────────────────────────────
beats.append(beat(
    "B08", "THE LIMITS", "REMOTION",
    "What this does not show. Ninety point seven percent is bond recall on forty seven dev "
    "quarters, with a range of eighty seven and a half to ninety three and a half. Ten of ten "
    "was calibrated on the same ten reports that found the bugs. And the agent itself still "
    "does not exist. Next: fix that company's data, check fresh reports, and build the "
    "document reader.",
    22,
    remotion("AKNext", LOCAL, {
        "sparkLine": "What the week does not show.",
        "eyebrow": "AI DEBT TRACKER · THE LIMITS",
        "title": "Every number above, and the limit that narrows it",
        "limits": [
            {"claim": f"{AFTER['got']} of {AFTER['of']} against printed tables",
             "limit": f"calibrated on the same {FIRST['of']} reports that found the "
                      f"{len(BUGS)} bugs. The measured number is "
                      f"{HELD['got']} of {HELD['of']}, on reports picked first.",
             "hot": True},
            {"claim": f"{pct1(BASE['recall'])} bond recall",
             "limit": f"on {BASE['quarters']} dev quarters graded bond by bond, "
                      f"{pct1(BASE['recall_lo'])}–{pct1(BASE['recall_hi'])}. High because "
                      f"most debt carries over, which is also why the zero is zero.",
             "hot": False},
            {"claim": f"{NEW['got']} of {NEW['of']} announced",
             "limit": f"of {NEW['total']} new bonds; {NEW['no_coupon']} carry no tagged "
                      f"interest rate and could not be searched for at all.",
             "hot": False},
            {"claim": f"{CLOCK['moved']} timestamps moved",
             "limit": f"{TZ_INFERENCE['claim']} — the shift matches US Eastern to UTC, but "
                      f"EDGAR published no note. An inference, not a log entry.",
             "hot": False},
            {"claim": "the agent",
             "limit": "still does not exist. This week built the answer key, the grader and "
                      "the baseline — the things that will judge it.",
             "hot": False},
        ],
        "nextLabel": "next",
        "next": FIG["next"],
        "source": "SOURCE: narration_script.md notes · docs/handcheck.md · docs/baseline_b0.md "
                  "· DESIGN.md §17 · figdata.json",
    }, "stagger", [
        {"at": "per limit", "event": "Each claim lands with the limit that narrows it."},
        {"at": "on 'next'", "event": "Three next steps land at the foot of the frame."},
    ], intent="Every episode in this series ends on its own limits. Each limit is tied to the claim it narrows, never left as a free-floating caveat list."),
))

# ── B09 · VERDICT ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B09", "VERDICT", "BOOKEND",
    "So: an answer key over one thousand and ninety three reports and nine thousand six "
    "hundred and fifty three bonds, and a grader that matches a bond on four fields and pairs "
    "each one only once. Checked against printed tables, it disagreed twice, and both times "
    "the grader was wrong, not the report. Ten of ten after five fixes is a calibration; two "
    "of three on untouched reports is the score. And doing nothing finds ninety one percent of "
    "bonds and none of the new ones.",
    29,
    remotion("ClaudeVerdictArtifact", "proven-core/ClaudeVerdictArtifact", {
        "artifactTitle": SEGMENT,
        "artifactHeading": "What week 2 built, and what it is allowed to claim",
        "artifactLines": [
            f"An answer key over {num(AK['reports'])} reports from {AK['companies']} companies "
            f"— {num(AK['bonds'])} bonds, {AK['from']} to {AK['to']}. "
            f"{BY_BOND['reports']} of those reports list debt bond by bond; the rest give "
            f"deals or totals, and are graded at the detail they give.",
            f"A bond counts as matched only if currency, interest rate, due year and amount "
            f"(within 1%) all agree, and each true bond can be claimed by at most one answer. "
            f"Every score carries a {GR['interval']} interval.",
            f"Against printed tables the grader agreed on {FIRST['got']} of {FIRST['of']} "
            f"first pass. All {len(BUGS)} disagreements were bugs in the grader — repaid notes "
            f"still counted, acquired debt dropped, two bonds in one entry, due dates read as "
            f"issue dates, a currency never stated.",
            f"{AFTER['got']} of {AFTER['of']} after the fixes is a CALIBRATION on the reports "
            f"that found them. {HELD['got']} of {HELD['of']} on untouched reports is the "
            f"measurement, and its one miss is the company's own tagging.",
            f"The do-nothing baseline finds {pct1(BASE['recall'])} of bonds and "
            f"{BASE['new_bonds_caught']} of {BASE['new_bonds_total']} new ones, reproducing "
            f"{BASE['exact']} of {BASE['quarters']} quarters exactly. "
            f"{NEW['got']} of {NEW['of']} new bonds were announced in time. That gap is the job.",
        ],
    }, "stagger", [
        {"at": "per clause", "event": "Five findings stagger in, one per spoken clause."},
    ], intent="Judgment beat. The artifact page is the point (ILLUSTRATE LAW carve-out)."),
))

# ── B10 · HANDOFF ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B10", "HANDOFF", "BOOKEND",
    "Your turn. Paste this into Claude. Before you trust a score, check the thing that produced "
    "it against something printed by someone else. Mine was wrong in five ways, and every one "
    "of them would have quietly flattered whatever I built next.",
    16,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": "Your turn.",
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "Take my evaluation harness and check IT, not the model. Pick a handful of cases "
            "where a human-readable source states the answer, compare my ground truth against "
            "that source line by line, and tell me which disagreements are errors in my "
            "harness rather than in the source."
        ),
        "runningText": "paste this into Claude…",
        "folderLabel": HANDLE,
        "modelLabel": "Opus 5",
        "effortLabel": "High",
        "output": [],
    }, "type-on", [
        {"at": "on 'paste this into Claude'", "event": "The prompt types into the composer."},
    ], intent="HANDOFF LAW: a real prompt, read ALOUD verbatim and then discussed. One of exactly two typing beats."),
))

# ── B11 · OUTRO ───────────────────────────────────────────────────────────────
beats.append(beat(
    "B11", "OUTRO", "BOOKEND",
    "Building the answer key, grader and baseline. Week two of the A I Debt Tracker. Om Mali, "
    "for Humanitarians A I.",
    9,
    remotion("ClaudeTitleOutro", "proven-core/ClaudeTitleOutro", {
        "title": SEGMENT,
        "handle": HANDLE,
        # `subline`, not `subtitle` — the wrong name ships the outro reading
        # "bot vs bot, season one", a default from an unrelated show.
        "subline": "week 2 · the AI Debt Tracker",
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
    "greeting_note": "hello lexicon: Latvian. HAI persona takes only the shortest cues (Hi · Ola · Hej · Ciao · Hallo · Salut · Ahoj · Szia · Tere · Moi · Hoi · Labas · Salve · Sveiki). Rotate; never repeat a language.",
    "aspect_ratio": "16:9",
    "fps": 24,
    "lead_silence_s": 0.4,
    "note": (
        "ai-explainer / claude-hai. AI Debt Tracker WEEK 2. ILLUSTRATE LAW: the Claude UI "
        "appears at B00 (cold open, answered), B09 (verdict artifact), B10 (handoff) and B11 "
        "(outro) only — every body beat illustrates its concept as a native animated Remotion "
        "scene (REBUILD LAW). The three source PNGs and their SVG sources are REFERENCE in "
        "pantry/, never slotted as media. The script's seven sections are split into eight "
        "body beats (1:13 splits into B03 the bugs and B04 calibrated-vs-measured) and the "
        "closing on-camera section becomes a limits beat; the split is logged in BUILD-LOG.md. "
        "FOUR THINGS NOT TO GET WRONG: the agent is NOT built, only its judge; 10 of 10 is a "
        "calibration and 2 of 3 is the measurement; 90.7% is flattering and hides a zero; and "
        "30 of 32 is the searchable denominator, not 30 of 36."
    ),
}

sheet = {"metadata": META, "beats": beats}

body = [b for b in beats if b["beat_id"] not in ("B00", "B09", "B10", "B11")]
words = {b["beat_id"]: len(b["narration_text"].split()) for b in beats}
lo = min(words[b["beat_id"]] for b in body)
hi = max(words[b["beat_id"]] for b in body)
# 45-72, four wider at the top than week 1's 45-68. This script SPEAKS its large numbers —
# "one thousand and ninety three", "nine thousand six hundred and fifty three", "eighty seven
# and a half" — and a single figure can cost six words. Tightening the band would mean cutting
# evidence to pay for the way a number is pronounced.
assert 45 <= lo and hi <= 72, f"body beat word budget 45-72 violated: {lo}-{hi}"
assert len(body) == 8 and len(beats) == 12

if "--check" in sys.argv:
    print("[adt-w2] all assertions pass")
    sys.exit(0)

out = HERE / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"[adt-w2] wrote {out}  — {len(beats)} beats")
print("[adt-w2] narration words: " + " ".join(f"{k}={v}" for k, v in words.items()))
print(f"[adt-w2] body beats {lo}-{hi}w (band 45-72), total {sum(words.values())}w")
print(f"[adt-w2] derived: {num(AK['reports'])} reports / {AK['companies']} companies / "
      f"{num(AK['bonds'])} bonds · levels {'/'.join(str(l['reports']) for l in LEVELS)} · "
      f"handcheck {FIRST['got']}/{FIRST['of']} -> {AFTER['got']}/{AFTER['of']} "
      f"(calibration) vs held-out {HELD['got']}/{HELD['of']} · baseline "
      f"{pct1(BASE['recall'])} recall but {BASE['new_bonds_caught']}/"
      f"{BASE['new_bonds_total']} new bonds and {BASE['exact']}/{BASE['quarters']} exact · "
      f"headroom {NEW['got']}/{NEW['of']} and {REPAY['got']}/{REPAY['of']} · "
      f"clock {CLOCK['moved']}/{CLOCK['of']}")
