#!/usr/bin/env python3
"""
build_beat_sheet.py — AI Debt Tracker, WEEK 3: Building the Filing Timeline, Triage and
Document Server.

Writes beat_sheet.json with EVERY on-screen figure injected from figdata.json. No number is
typed into a scene or into a beat sheet by hand.

THE FRAMING ASSERTION of this reel is FRESH_SHARE < LAST_WEEK_SHARE. B01's claim is that
"3 of 3" is a score on reports that had already been read while last week's defects were being
fixed, and that the honest number is "1 of 3" on reports drawn fresh and graded once. If the
fresh score ever caught up, the beat would be drawing a distinction that no longer exists. The
build fails rather than advertise a recovered answer key.

THE SECOND ARGUMENT, asserted the same way: triage's perfect recall must keep sitting beside
two weaker numbers. 24 of 24 is flattering on its own; precision is 24 of 26 and the event type
is right on 20 of 24. If recall stopped being perfect, or the other two caught up with it, B05
is a different beat.

A THIRD assertion ties the named false alarms to the precision denominator: the two things
B05 names on screen must be exactly the gap between 24 found and 26 kept. A beat that names
two mistakes while its arithmetic implies a different number is lying quietly.

THREE CLAIMS ARE NOT MEASURED in figdata.json. They come from narration_script.md and the
project documents, are passed as named constants below, and every screen that uses one says
where it came from:
  · AGENT_STATE    — the agent still cannot read a filing into structured facts  (B00/B04/B08)
  · LABELLER       — the 50 labels are Claude's judgment, not a person's         (B05/B08)
  · OWN_MISTAKE    — one transcription error in the author's own hand-check      (B02)

Usage:  python build_beat_sheet.py            (writes beat_sheet.json)
        python build_beat_sheet.py --check    (assertions only, writes nothing)
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIG = json.loads((HERE / "figdata.json").read_text(encoding="utf-8"))

HC = FIG["handcheck"]
TL = FIG["timeline"]
FU = FIG["funnel"]
CK = FIG["check"]
WR = FIG["wrong"]
QU = FIG["quotes"]
DC = FIG["docs"]

# ── derived, never typed ──────────────────────────────────────────────────────
LAST, FRESH = HC["last_week"], HC["fresh"]
LAST_SHARE = LAST["got"] / LAST["of"]
FRESH_SHARE = FRESH["got"] / FRESH["gradable"]
REPORTS = HC["reports"]
AGREED = [r for r in REPORTS if r["agreed"]]
DEFECTS = [r for r in REPORTS if r["defect"]]

TYPES = TL["types"]
ROWS = {r["kind"]: r for r in CK["rows"]}
RECALL, PRECISION = ROWS["recall"], ROWS["precision"]
EVENT, CARRY = ROWS["event type"], ROWS["carry-over"]
RECALL_SHARE = RECALL["got"] / RECALL["of"]
PRECISION_SHARE = PRECISION["got"] / PRECISION["of"]
EVENT_SHARE = EVENT["got"] / EVENT["of"]

RULES_SHARE = FU["rules_decided"] / FU["total"]

# ── assertions ────────────────────────────────────────────────────────────────
# THE FRAMING ASSERTION. B01 exists because these two scores mean different things.
assert FRESH_SHARE < LAST_SHARE, (
    "B01's whole claim: 3 of 3 is on reports already read while last week's defects were "
    "being fixed, and 1 of 3 is on reports drawn fresh and graded once. If the fresh score "
    "ever caught up, the beat would be arguing about nothing."
)
assert LAST["got"] == LAST["of"] == 3 and HC["fixes_last_week"] == 3
assert FRESH["gradable"] + FRESH["not_gradable"] == FRESH["drawn"] == 5, (
    "the 2 reports with nothing to grade are DRAWN on B01 as an excluded tail, so the "
    "denominator change has to add back up to the set that was drawn"
)
assert len(FRESH["not_gradable_who"]) == FRESH["not_gradable"]
assert len(REPORTS) == FRESH["gradable"] == 3
assert len(AGREED) == FRESH["got"] == 1 and len(DEFECTS) == 2, (
    "B02 names one agreement and two defects; the counts and the rows must not drift apart"
)

assert sum(ty["count"] for ty in TYPES) == TL["filings"] == 593, (
    "B03 draws the filing types as the composition of the window's 593; a partition that "
    "does not sum to the thing it partitions is not a partition"
)
assert len(TYPES) == 3 and TL["companies"] == 25

assert FU["rules_decided"] + FU["model_asked"] == FU["total"] == TL["filings"], (
    "every filing is either decided by a rule or sent to the model — there is no third place"
)
assert FU["rules_kept"] + FU["model_kept"] == FU["kept"] == 184, (
    "what is kept has to be what the rules kept plus what the model kept"
)
assert FU["model_kept"] < FU["model_asked"] and FU["kept"] < FU["total"]
assert 0.64 <= RULES_SHARE <= 0.69, "the narration says the rules decide 'two thirds'"
assert FU["median_s"] > 0

# THE SECOND ARGUMENT. Perfect recall, with its qualifiers beside it.
assert RECALL_SHARE == 1.0, "B05's hero bar is full; a partial recall is a different beat"
assert RECALL_SHARE >= CK["pass_line"] == 0.95, "and it has to clear the mark set beforehand"
assert PRECISION_SHARE < RECALL_SHARE, (
    "24 of 24 only means something while the reel also shows what it kept that it should not"
)
assert EVENT_SHARE < PRECISION_SHARE, (
    "and the event type is the weakest of the three — B05 orders them that way deliberately"
)
# THE THIRD. The two alarms NAMED on the frame are the whole gap between found and kept.
assert PRECISION["of"] - RECALL["got"] == len(CK["false_alarms"]) == 2, (
    "B05 names two false alarms; if precision's denominator ever implied a different number, "
    "the frame would be naming a subset while the bar claims a total"
)
assert CARRY["got"] == CARRY["of"] == 22, "every one of last week's announcements survives"
assert CK["labelled"] == CK["labelled_random"] + CK["labelled_debt_word"] == 50
assert RECALL["of"] < CK["labelled"], "24 positives inside a 50-filing sample — a small set"

assert len(WR) == 3, "B06 pairs three failures with what each one changed"
assert all(w["now"] for w in WR), "a failure with no consequence is a confession, not a record"
assert QU["not_verbatim"] < QU["checked"], "8 of 21, not all of them"

# ── the values figdata.json does not measure ──────────────────────────────────
NOT_IN_FIGDATA = "not in figdata.json — from narration_script.md and the project documents"
AGENT_STATE = {
    "built": False,
    "note": "The agent still cannot read a filing into structured debt events. This week "
            "built what finds the filings worth reading, and what lets a reader point into "
            "them.",
}
LABELLER = {
    "who": CK["labeller"],
    "note": CK["labeller_note"],
    "kind": "a model judgment, not a person's",
}
# .capitalize() would lower-case the rest of the string and eat a company name.
def SENT(s: str) -> str:
    return s[:1].upper() + s[1:]

OWN_MISTAKE = {
    "what": "one reading mistake in the hand-check was mine — a Super Micro coupon taken from "
            "the notes' original terms, which were amended in 2025",
    "effect": "it does not change the verdict; the double-counted allotment alone makes that "
              "report disagree",
}

HANDLE = "@HumanitariansAI"
SEGMENT = "Building the Filing Timeline, Triage and Document Server"
SLUG = "building-the-filing-timeline-triage-and-document-server"
KICKER = "Irreducibly Human"     # GATE L rule 7 — the FIXED claude-hai series name
GREETING = "Zdravo, HAI"         # Croatian. Never repeats a language; see metadata note.


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


LOCAL = "reel-local/BuildingTheTriage"
beats = []

# ── B00 · COLD OPEN ───────────────────────────────────────────────────────────
beats.append(beat(
    "B00", "COLD OPEN", "BOOKEND",
    "Hi, I'm Om Mali. This video is about teaching my A I debt tracker to find the debt news "
    "in S E C filings, with a filing timeline, a triage step and a document server. This is "
    "week three of the A I Debt Tracker. The agent still cannot read a filing into structured "
    "facts. This week built what finds the filings worth reading.",
    20,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": GREETING,
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "Gather every filing in each quarter's window, throw away the ones that are not "
            "about debt, and prove to me that nothing was thrown away that should have been "
            "kept. Then make the survivors citable."
        ),
        "runningText": "triage_eval.py run qwen3:4b…",
        "folderLabel": HANDLE,
        "modelLabel": "Opus 5",
        "effortLabel": "High",
        "output": [
            f"{num(TL['filings'])} filings in the windows — {num(FU['rules_decided'])} "
            f"decided by rules, {FU['model_asked']} asked the model, {FU['kept']} kept",
            f"on {CK['labelled']} filings labelled beforehand, triage found "
            f"{RECALL['got']} of {RECALL['of']} — and kept {PRECISION['of'] - PRECISION['got']} "
            f"it should not have",
            f"and on {FRESH['drawn']} fresh answer-key reports, {FRESH['got']} of "
            f"{FRESH['gradable']} gradable ones agreed",
        ],
    }, "type-on", [
        {"at": "on 'find the debt news'", "event": "The ask types into the Claude composer."},
        {"at": "on 'what finds the filings worth reading'", "event": "The result lands ANSWERED with three output lines."},
    ], intent="COLD OPEN LAW: the ask is the week itself — find the news, and prove nothing was lost. Lands ANSWERED."),
))

# ── B01 · LAST WEEK'S LEFTOVERS ───────────────────────────────────────────────
beats.append(beat(
    "B01", "LAST WEEK'S LEFTOVERS", "REMOTION",
    "First, last week's leftovers. Three data problems are fixed, and last week's three test "
    "reports now all agree. But I'd read those reports by now, so I graded five fresh ones, "
    "once. Two of them had no debt on either side, so there was nothing to grade. Of the "
    "three that did, only one agreed.",
    20,
    remotion("W3Recheck", LOCAL, {
        "sparkLine": "Three of three on reports I had read. One of three on reports I had not.",
        "eyebrow": "AI DEBT TRACKER · WEEK 3",
        "title": "The answer key, checked on reports nobody had read",
        "subtitle": "Printed debt tables against the answer key, graded once after last "
                    "week's fixes",
        "rows": [
            {"label": LAST["label"], "got": LAST["got"], "of": LAST["of"],
             "excluded": 0, "hot": False},
            {"label": FRESH["label"], "got": FRESH["got"], "of": FRESH["gradable"],
             "excluded": FRESH["not_gradable"], "hot": True},
        ],
        "excludedNote": f"The dashed cells are the {FRESH['not_gradable']} of "
                        f"{FRESH['drawn']} drawn reports that {FRESH['not_gradable_note']} "
                        f"({', '.join(FRESH['not_gradable_who'])}). They are excluded, not "
                        f"counted as agreements.",
        "fixedLabel": f"{HC['fixes_last_week']} defects fixed from last week",
        "fixed": "Last week's three reports now agree — but they are the reports the fixes "
                 "were made against, so that score is a calibration, not a measurement.",
        "source": "SOURCE: AI Debt Tracker docs/handcheck.md, manifests/handcheck/, "
                  "DESIGN.md P35–P39 · figdata.json",
    }, "grow", [
        {"at": "on 'now all agree'", "event": "The first bar fills to 3 of 3."},
        {"at": "on 'nothing to grade'", "event": "The fresh bar fills to 1 of 3, with 2 dashed cells beyond its end."},
    ], intent="The 2 reports with nothing to grade are DRAWN as an excluded tail. Scoring 1 of 5 would punish the key for empty reports; dropping them silently would hide a denominator change."),
))

# ── B02 · WHAT THE FRESH REPORTS SHOWED ───────────────────────────────────────
beats.append(beat(
    "B02", "WHAT THE FRESH REPORTS SHOWED", "REMOTION",
    "Dell's totals agree exactly. The answer key counted the banks' extra allotment on a "
    "Super Micro convertible as a second bond. And Core Scientific's small notes have no due "
    "date anywhere in the data. Two new defects, written down for next week, not tuned away "
    "against the reports that found them. And one reading mistake was mine.",
    21,
    remotion("W3Fresh", LOCAL, {
        "sparkLine": "Two new defects, left open on purpose.",
        "eyebrow": "AI DEBT TRACKER · WHAT THE FRESH REPORTS SHOWED",
        "title": "Three reports, one agreement",
        "subtitle": "Drawn before reading, graded once",
        "reports": [
            {"who": r["who"], "what": r["what"], "defect": r["defect"], "agreed": r["agreed"]}
            for r in REPORTS
        ],
        "openLabel": f"{len(DEFECTS)} defects, left open",
        "open": f"Fixing them against the reports that found them would turn next week's "
                f"check into another calibration. {SENT(OWN_MISTAKE['what'])} — "
                f"{OWN_MISTAKE['effect']}. ({NOT_IN_FIGDATA})",
        "source": "SOURCE: AI Debt Tracker docs/handcheck.md, DESIGN.md P38–P39 · figdata.json",
    }, "stagger", [
        {"at": "per report", "event": "Three named reports land, the two disagreements in the accent."},
        {"at": "on 'written down for next week'", "event": "The open-defect block lands beneath them."},
    ], intent="Named reports with named defects, not a score. The defect ids are on the frame because 'left open' is only checkable if the thing left open has a name."),
))

# ── B03 · THE TIMELINE ────────────────────────────────────────────────────────
beats.append(beat(
    "B03", "THE TIMELINE", "REMOTION",
    "Now the agent's first job: finding the news. For every quarter, the timeline gathers "
    "each eight K, prospectus and term sheet filed in the window, including the subsidiaries "
    "that borrow on a company's behalf. Across the development quarters, that's five hundred "
    "and ninety three filings. The window ends at the report the quarter is graded on, so "
    "nothing later can get in.",
    23,
    remotion("W3Timeline", LOCAL, {
        "sparkLine": "A window that closes before the answer is published.",
        "eyebrow": "AI DEBT TRACKER · THE TIMELINE",
        "title": "Every filing in the quarter's window",
        "subtitle": f"{TL['companies']} AI companies and their borrowing subsidiaries, "
                    f"across the development quarters",
        "windowLabel": "one quarter's window",
        "cutoffLabel": "cut-off: the report it is graded on",
        "tickCount": 44,
        "totalBig": num(TL["filings"]),
        "totalSmall": "filings gathered",
        "types": [{"type": ty["type"], "what": ty["what"], "count": ty["count"]}
                  for ty in TYPES],
        "subsNote": f"A company's debt is often issued by a financing subsidiary, so "
                    f"{TL['subsidiaries']} — a filing missed there is a bond missed.",
        "source": "SOURCE: AI Debt Tracker week3/pool.json ← triage_eval.py pool · figdata.json",
    }, "gather", [
        {"at": "on 'gathers each 8-K, prospectus and term sheet'", "event": "Filings land as ticks inside the window."},
        {"at": "on 'nothing later can get in'", "event": "The window's right edge is the solid accent rule."},
    ], intent="The beat is called the filing TIMELINE, so it is drawn as one. A bar chart of filing types would count the same things and show nothing of what the window is."),
))

# ── B04 · TRIAGE ──────────────────────────────────────────────────────────────
beats.append(beat(
    "B04", "TRIAGE", "REMOTION",
    "Most of them aren't about debt at all. Triage sorts them. Five plain rules decide two "
    "thirds: a new borrowing item on an eight K, a prospectus selling notes rather than "
    "shares, a filing with no debt words at all. Only the doubtful third, a hundred and "
    "ninety nine, goes to the small local model, at about three seconds each. A hundred and "
    "eighty four are kept.",
    23,
    remotion("W3Funnel", LOCAL, {
        "sparkLine": "Rules first. The model only sees what the rules could not settle.",
        "eyebrow": "AI DEBT TRACKER · TRIAGE",
        "title": "From every filing to the ones about debt",
        "subtitle": "Each bar is the same 593 filings, narrowed",
        "total": FU["total"],
        "stages": [
            {"label": "Filings in the windows", "value": FU["total"], "note": "", "hot": False},
            {"label": "Decided by five rules", "value": FU["rules_decided"],
             "note": f"{pct0(RULES_SHARE)} of them, before any model runs", "hot": False},
            {"label": "Asked the local model", "value": FU["model_asked"],
             "note": f"{FU['model']}, median {FU['median_s']}s each", "hot": True},
            {"label": "Kept as debt news", "value": FU["kept"],
             "note": f"{FU['rules_kept']} by rule + {FU['model_kept']} by model", "hot": True},
        ],
        "rulesLabel": "the five rules",
        "rules": FU["rules"],
        "modelNote": f"The model is asked only about the doubtful {FU['model_asked']}, and "
                     f"keeps {FU['model_kept']} of them. It does not read the filing into "
                     f"facts — that is next week's job. ({NOT_IN_FIGDATA})",
        "source": "SOURCE: AI Debt Tracker week3/triage_qwen3_4b.json ← triage_eval.py, "
                  "docs/triage.md · figdata.json",
    }, "narrow", [
        {"at": "per stage", "event": "Each stage fills inside the same full-width outline."},
        {"at": "on 'a hundred and eighty-four are kept'", "event": "The five rules land as chips beneath."},
    ], intent="Four free-standing bars would read as four populations. This is ONE population being narrowed, so every row keeps the full 593 outline and the part that fell away stays visible as the gap."),
))

# ── B05 · THE CHECK ───────────────────────────────────────────────────────────
beats.append(beat(
    "B05", "THE CHECK", "REMOTION",
    "Does it miss anything? Fifty filings, drawn by a fixed random rule, were labelled "
    "against a written definition before triage ran, by Claude, a different model from the "
    "one being tested. Triage found all twenty four debt filings; the pass line was ninety "
    "five percent. It raised two false alarms. And it kept all twenty two filings that last "
    "week's search found announcing a bond change.",
    24,
    remotion("W3Check", LOCAL, {
        "sparkLine": "It found everything. Look at the three numbers under that one.",
        "eyebrow": "AI DEBT TRACKER · THE CHECK",
        "title": f"Triage against {CK['labelled']} filings labelled beforehand",
        "subtitle": f"{CK['labelled_random']} drawn at random, "
                    f"{CK['labelled_debt_word']} from filings containing debt words",
        "rows": [
            {"metric": r["metric"], "got": r["got"], "of": r["of"],
             "kind": r["kind"], "hot": r["hot"]}
            for r in CK["rows"]
        ],
        "line": CK["pass_line"],
        "lineLabel": f"dashed = the {pct0(CK['pass_line'])} pass line, set before the check "
                     f"ran — one rule, drawn through all four tracks",
        "alarmsLabel": f"the {len(CK['false_alarms'])} it kept that were not debt",
        "alarms": CK["false_alarms"],
        "labelNote": f"The labels are {LABELLER['kind']} — {LABELLER['who']}, "
                     f"{LABELLER['note']}. ({NOT_IN_FIGDATA})",
        "source": "SOURCE: AI Debt Tracker docs/triage.md, docs/triage_labels.md, "
                  "manifests/triage_labels.json · figdata.json",
    }, "grow", [
        {"at": "on 'found all twenty-four'", "event": "The recall bar fills past the dashed pass line inside it."},
        {"at": "on 'two false alarms'", "event": "The weaker bars land beneath it and the two alarms are named."},
    ], intent="Perfect recall is the flattering number, so the two that qualify it sit directly beneath it on the same scale, and the two false alarms are NAMED rather than left as a denominator."),
))

# ── B06 · WHAT WENT WRONG ─────────────────────────────────────────────────────
beats.append(beat(
    "B06", "WHAT WENT WRONG", "REMOTION",
    "Not everything went smoothly. The first run crashed when a model answer got cut off mid "
    "sentence, so now an unreadable answer keeps the filing. The check also exposed a bug in "
    "last week's search: zero percent was matching inside twenty percent. And eight of the "
    "model's twenty one yes answers gave a quote that isn't word for word in what it read.",
    22,
    remotion("W3Wrong", LOCAL, {
        "sparkLine": "Three failures, and what each one changed.",
        "eyebrow": "AI DEBT TRACKER · WHAT WENT WRONG",
        "title": "What broke, and what it changed",
        "subtitle": "",
        "items": [{"what": w["what"], "detail": w["detail"], "now": w["now"]} for w in WR],
        "quoteNote": f"The quote check compares the first {QU['window_chars']} characters of "
                     f"the model's quote with the text it was given. "
                     f"{QU['not_verbatim']} of {QU['checked']} did not match — which can be a "
                     f"paraphrase rather than an invention, so the filing is still kept and "
                     f"the event reader must re-check every fact.",
        "source": "SOURCE: AI Debt Tracker docs/triage.md, logs/RUN_LOG.md 2026-10-31, "
                  "DESIGN.md P40 · figdata.json",
    }, "stagger", [
        {"at": "per failure", "event": "Each failure lands with the change it forced beneath it."},
        {"at": "on 'word for word'", "event": "The quote-check footnote lands."},
    ], intent="Three things that went wrong is a confession. Three things that went wrong, each with the change it forced, is a record — so the consequence takes the accent, not the failure."),
))

# ── B07 · THE DOCUMENT SERVER ─────────────────────────────────────────────────
beats.append(beat(
    "B07", "THE DOCUMENT SERVER", "REMOTION",
    "That's why the document server matters. It turns a filing into numbered sentences and "
    "table cells, so the agent cites sentence five instead of retyping one and a half billion "
    "dollars. And it refuses to open the report the agent will be graded on. Every document "
    "goes through the same point in time rule.",
    20,
    remotion("W3Docs", LOCAL, {
        "sparkLine": "Cite the sentence. Never retype the number.",
        "eyebrow": "AI DEBT TRACKER · THE DOCUMENT SERVER",
        "title": "A filing the agent can point into",
        "subtitle": "The docs server turns a filing into numbered sentences, tables, rows "
                    "and cells",
        "filing": DC["filing"],
        "filingMeta": f"{DC['sentences']} sentences · {DC['tables']} tables",
        "query": DC["query"],
        "hitId": f"→ {DC['hit']}",
        "hitText": DC["hit_text"],
        "citeNote": f"The agent cites {DC['cites']} — it never retypes a number.",
        "refusalQuery": "open(the report it will be graded on)",
        "refusal": DC["refusal"],
        "pitNote": "Every document is opened through the point-in-time server, so week 1's "
                   "rule holds here too: the agent cannot read the answer it is graded on.",
        "source": "SOURCE: AI Debt Tracker src/ai_debt_tracker/documents/, "
                  "mcp_servers/docs.py · figdata.json",
    }, "cite", [
        {"at": "on 'numbered sentences and table cells'", "event": "The query lands and resolves to s5."},
        {"at": "on 'refuses to open the report'", "event": "The refusal lands beneath it, in the accent."},
    ], intent="The citation is shown resolving — query, id, the actual sentence — so 'cites instead of retyping' is seen rather than claimed."),
))

# ── B08 · THE LIMITS ──────────────────────────────────────────────────────────
beats.append(beat(
    "B08", "THE LIMITS", "REMOTION",
    "What this does not show. Twenty four of twenty four is recall on a small set; precision "
    "is twenty four of twenty six, and the event type is right on only twenty of twenty four. "
    "The labels are a model's judgment, not a person's. And a quote that isn't verbatim may "
    "be a paraphrase, not an invention. Next: fix the two new defects, check fresh reports, "
    "build the event reader.",
    23,
    remotion("W3Next", LOCAL, {
        "sparkLine": "What the week does not show.",
        "eyebrow": "AI DEBT TRACKER · THE LIMITS",
        "title": "Every number above, and the limit that narrows it",
        "limits": [
            {"claim": f"{RECALL['got']} of {RECALL['of']} found",
             "limit": f"recall on {RECALL['of']} positives inside a {CK['labelled']}-filing "
                      f"sample. Precision is {PRECISION['got']} of {PRECISION['of']} and the "
                      f"event type is right on {EVENT['got']} of {EVENT['of']}.",
             "hot": True},
            {"claim": f"{CK['labelled']} labelled filings",
             "limit": f"{LABELLER['kind']} — {LABELLER['who']} labelled them against a "
                      f"written definition before triage ran. A different model, but not a "
                      f"person.",
             "hot": False},
            {"claim": f"{QU['not_verbatim']} of {QU['checked']} not verbatim",
             "limit": "a quote that is not verbatim can be a paraphrase rather than an "
                      "invention. The filing is still kept and every fact is re-checked later.",
             "hot": False},
            {"claim": f"{LAST['got']} of {LAST['of']} after fixes",
             "limit": f"on the reports the fixes were made against. The measured number is "
                      f"{FRESH['got']} of {FRESH['gradable']}, and {FRESH['not_gradable']} "
                      f"drawn reports had nothing to grade.",
             "hot": False},
            {"claim": "the agent",
             "limit": "still cannot read a filing into structured debt events. This week "
                      "built what finds the filings and what lets a reader cite them.",
             "hot": False},
        ],
        "nextLabel": "next",
        "next": FIG["next"],
        "source": "SOURCE: narration_script.md notes · docs/triage.md · docs/handcheck.md · "
                  "DESIGN.md §17 · figdata.json",
    }, "stagger", [
        {"at": "per limit", "event": "Each claim lands with the limit that narrows it."},
        {"at": "on 'next'", "event": "Three next steps land at the foot of the frame."},
    ], intent="Every episode in this series ends on its own limits. Each limit is tied to the claim it narrows, never left as a free-floating caveat list."),
))

# ── B09 · VERDICT ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B09", "VERDICT", "BOOKEND",
    "So: five hundred and ninety three filings gathered per quarter window, two thirds "
    "settled by five plain rules, and a small local model asked only about the doubtful "
    "third. A hundred and eighty four kept. Checked against fifty filings labelled "
    "beforehand, it found every one of the twenty four, kept two it shouldn't have, and got "
    "the event type right on twenty. The answer key still has two open defects, and the "
    "agent still cannot read a filing.",
    28,
    remotion("ClaudeVerdictArtifact", "proven-core/ClaudeVerdictArtifact", {
        "artifactTitle": SEGMENT,
        "artifactHeading": "What week 3 built, and what it is allowed to claim",
        "artifactLines": [
            f"The answer key re-checked: last week's {LAST['of']} now agree, but on "
            f"{FRESH['drawn']} reports drawn fresh and graded once, {FRESH['got']} of the "
            f"{FRESH['gradable']} with any debt agreed. "
            f"{FRESH['not_gradable']} had nothing to grade. Two new defects, left open.",
            f"A timeline that gathers every 8-K, prospectus and term sheet in each quarter's "
            f"window — {num(TL['filings'])} filings across the dev quarters, including the "
            f"subsidiaries that borrow for a company. The window ends at the graded report.",
            f"Triage: {num(FU['rules_decided'])} filings settled by five plain rules, "
            f"{FU['model_asked']} sent to {FU['model']} at a median {FU['median_s']}s each, "
            f"{FU['kept']} kept — {FU['rules_kept']} by rule and {FU['model_kept']} by model.",
            f"Checked on {CK['labelled']} filings labelled by {LABELLER['who']} before triage "
            f"ran: {RECALL['got']} of {RECALL['of']} found against a "
            f"{pct0(CK['pass_line'])} line, {PRECISION['got']} of {PRECISION['of']} kept are "
            f"debt, event type right on {EVENT['got']} of {EVENT['of']}, and all "
            f"{CARRY['of']} of last week's announcements survive.",
            f"A document server that turns a filing into numbered sentences and cells so the "
            f"agent cites {DC['hit']} instead of retyping a number — and refuses the report "
            f"it will be graded on. Three things broke on the way, and each changed something.",
        ],
    }, "stagger", [
        {"at": "per clause", "event": "Five findings stagger in, one per spoken clause."},
    ], intent="Judgment beat. The artifact page is the point (ILLUSTRATE LAW carve-out)."),
))

# ── B10 · HANDOFF ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B10", "HANDOFF", "BOOKEND",
    "Your turn. Paste this into Claude. If you have a filter in front of a model, label a "
    "sample by hand before you run it, and write the definition down first. Mine found "
    "everything it was supposed to, and still kept two things it shouldn't have.",
    16,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": "Your turn.",
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "Write down, in one paragraph, what counts as a positive for my filter — before "
            "looking at any of its output. Then label a random sample against that "
            "definition, and report recall AND precision separately. Do not let the filter's "
            "own answers influence a single label."
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
    "Building the filing timeline, triage and document server. Week three of the A I Debt "
    "Tracker. Om Mali, for Humanitarians A I.",
    9,
    remotion("ClaudeTitleOutro", "proven-core/ClaudeTitleOutro", {
        "title": SEGMENT,
        "handle": HANDLE,
        # `subline`, not `subtitle` — the wrong name ships the outro reading
        # "bot vs bot, season one", a default from an unrelated show.
        "subline": "week 3 · the AI Debt Tracker",
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
    "greeting_note": "hello lexicon: Croatian. HAI persona takes only the shortest cues (Hi · Ola · Hej · Ciao · Hallo · Salut · Ahoj · Szia · Tere · Moi · Hoi · Labas · Salve · Sveiki · Zdravo). Rotate; never repeat a language.",
    "aspect_ratio": "16:9",
    "fps": 24,
    "lead_silence_s": 0.4,
    "note": (
        "ai-explainer / claude-hai. AI Debt Tracker WEEK 3. ILLUSTRATE LAW: the Claude UI "
        "appears at B00 (cold open, answered), B09 (verdict artifact), B10 (handoff) and B11 "
        "(outro) only — every body beat illustrates its concept as a native animated Remotion "
        "scene (REBUILD LAW). The four source PNGs and their SVG sources are REFERENCE in "
        "pantry/, never slotted as media. The script's eight sections become eight body beats: "
        "0:15 splits into B01 (the two scores) and B02 (the three named reports), and the "
        "closing on-camera section becomes a limits beat. FOUR THINGS NOT TO GET WRONG: the "
        "agent still cannot read a filing into facts; 3 of 3 is a calibration and 1 of 3 is "
        "the measurement, with 2 drawn reports excluded rather than counted; 24 of 24 recall "
        "sits beside 24 of 26 precision and 20 of 24 event types; and the 50 labels are "
        "Claude's judgment, not a person's."
    ),
}

sheet = {"metadata": META, "beats": beats}

body = [b for b in beats if b["beat_id"] not in ("B00", "B09", "B10", "B11")]
words = {b["beat_id"]: len(b["narration_text"].split()) for b in beats}
lo = min(words[b["beat_id"]] for b in body)
hi = max(words[b["beat_id"]] for b in body)
# 45-72, the band week 2 settled on. This script speaks its large numbers aloud ("five
# hundred and ninety three", "twenty four of twenty four"), and one figure can cost six
# words; tightening the band would mean cutting evidence to pay for pronunciation.
assert 45 <= lo and hi <= 72, f"body beat word budget 45-72 violated: {lo}-{hi}"
assert len(body) == 8 and len(beats) == 12

if "--check" in sys.argv:
    print("[adt-w3] all assertions pass")
    sys.exit(0)

out = HERE / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"[adt-w3] wrote {out}  — {len(beats)} beats")
print("[adt-w3] narration words: " + " ".join(f"{k}={v}" for k, v in words.items()))
print(f"[adt-w3] body beats {lo}-{hi}w (band 45-72), total {sum(words.values())}w")
print(f"[adt-w3] derived: handcheck {LAST['got']}/{LAST['of']} (calibration) vs fresh "
      f"{FRESH['got']}/{FRESH['gradable']} + {FRESH['not_gradable']} excluded · "
      f"timeline {num(TL['filings'])} = "
      f"{'+'.join(str(ty['count']) for ty in TYPES)} · funnel "
      f"{FU['total']}->{FU['rules_decided']}+{FU['model_asked']}->{FU['kept']} "
      f"({FU['rules_kept']}+{FU['model_kept']}) · check recall {RECALL['got']}/{RECALL['of']} "
      f"vs precision {PRECISION['got']}/{PRECISION['of']} vs event {EVENT['got']}/{EVENT['of']}"
      f" · quotes {QU['not_verbatim']}/{QU['checked']} not verbatim")
