#!/usr/bin/env python3
"""
build_beat_sheet.py — AI Debt Tracker, WEEK 1: Grounding an AI Debt Tracker in Real SEC Filings.

Writes beat_sheet.json with EVERY on-screen figure injected from figdata.json. No number is
typed into a scene or into a beat sheet by hand.

THE FRAMING ASSERTION of this reel is MEASURED_BY_BOND < ASSUMED, over a partition that must
still sum to the whole universe. B05's entire claim is "fifteen, not twenty-one": the count of
companies whose reports can be graded bond by bond FELL when it was measured by how much of
each company's debt is actually itemised, instead of counted by how many instruments carry a
tag. If a data change ever made those two numbers equal — or made the three grading levels stop
accounting for all 25 companies — the beat would be arguing about nothing, and this build must
fail rather than ship it.

THE SECOND ARGUMENT, asserted the same way, is the bake-off: the WINNER MUST BE THE SMALLEST
MODEL and must beat every larger one outright. "The smallest won" is the beat; a tie or a
reversal is a different video.

FOUR VALUES ARE NOT IN figdata.json. They come from narration_script.md and the project
documents behind it, are passed as named constants below, and every screen that uses one says
where it came from:
  · MYCROFT_RECIPES  — ~99 recipes in the Mycroft repo, none on debt or credit      (B01)
  · PIPELINE         — the four designed stages; DESIGN.md, not a measurement       (B02)
  · COARSE_EXAMPLES  — Microsoft's 13 batches, Oracle's partial 10-Qs               (B05)
  · PIT_SERVER       — what the point-in-time server refuses, and that it is built  (B03)

Usage:  python build_beat_sheet.py            (writes beat_sheet.json)
        python build_beat_sheet.py --check    (assertions only, writes nothing)
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIG = json.loads((HERE / "figdata.json").read_text(encoding="utf-8"))

ISS = FIG["issuance_bn"]
UNI = FIG["universe"]
LEVELS = FIG["levels"]
GATE = FIG["levels_gate"]
CASES = FIG["cases"]
MATCH = FIG["matching"]
SPIKE = FIG["spike"]
BAKE = FIG["bakeoff"]

# ── derived, never typed ──────────────────────────────────────────────────────
BY_LEVEL = {l["level"]: l for l in LEVELS}
MEASURED_BY_BOND = BY_LEVEL["bond by bond"]["companies"]
ASSUMED = FIG["levels_assumed"]
GRADED_COARSER = sum(l["companies"] for l in LEVELS if l["level"] != "bond by bond")

ANN = SPIKE["announced"]
HEAD = SPIKE["headroom"]

MODELS = sorted(BAKE["models"], key=lambda m: -m["got"])
WINNER = MODELS[0]
RUNNERS = MODELS[1:]
SHARE = {m["name"]: m["got"] / m["of"] for m in BAKE["models"]}

# ── assertions ────────────────────────────────────────────────────────────────
assert ISS["y2025"] == 121 and ISS["avg_2020_2024"] == 28, "B01's two bars"
assert round(ISS["y2025"] / ISS["avg_2020_2024"], 1) == ISS["multiple"] == 4.3, \
    "the multiple is derived from the two bars, never stated separately"
assert len(ISS["companies"]) == 5

# THE FRAMING ASSERTION. B05 exists because these two numbers disagree.
assert MEASURED_BY_BOND < ASSUMED, (
    "B05's whole claim is 'fifteen, not twenty-one'. If measuring by coverage ever stopped "
    "lowering the count, this beat would be arguing about nothing."
)
assert MEASURED_BY_BOND == 15 and ASSUMED == 21
assert sum(l["companies"] for l in LEVELS) == UNI["ai"] == 25, (
    "the three grading levels must account for every company in the universe — a partition "
    "that leaks is not a partition, and the bar in B05 is drawn as one row of 25"
)
assert len(LEVELS) == 3 and GRADED_COARSER == 10
# ... and the gate behind it must still add up to the 15 the beat says.
assert GATE["qualified_on_coverage"] + GATE["moved_up_on_tie"] == MEASURED_BY_BOND
assert GATE["coverage_line"] == 0.80

assert CASES["dev"] + CASES["test"] == CASES["total"] == 495, \
    "B06 splits 495 into a build set and a held-back set; they must be the whole set"
assert CASES["test"] > CASES["dev"], "most of the set is held back — that is the claim"

assert MATCH["got"] == 594 and MATCH["of"] == 636
assert round(MATCH["got"] / MATCH["of"], 3) == MATCH["share"] == 0.934
assert MATCH["share"] > MATCH["line"] == 0.90, "B06 says it clears the line set beforehand"
assert MATCH["all_quarters_share"] < MATCH["share"], (
    "B06's and B08's caveat only means something while the all-quarters figure is LOWER than "
    "the per-bond figure it qualifies"
)

assert SPIKE["quarters"] == 46 and SPIKE["companies"] < UNI["ai"], "23 of the 25, not all"
assert ANN["got"] == 56 and ANN["of"] == 64 and ANN["share"] == 0.875 > ANN["line"] == 0.80
assert HEAD["got"] == 21 and HEAD["of"] == 46 and HEAD["share"] > HEAD["line"]
assert HEAD["raw"] == 33 > HEAD["got"], \
    "the conservative count must stay BELOW the raw one, or B04's footnote is backwards"

# THE SECOND ARGUMENT. "The smallest won" has to keep being true.
assert len(BAKE["models"]) == 3
assert all(WINNER["params_b"] < r["params_b"] for r in RUNNERS), \
    "B07's claim is that the SMALLEST model won; a larger winner is a different beat"
assert all(WINNER["got"] > r["got"] for r in RUNNERS), "and won outright, not on a tie"
assert all(m["of"] == BAKE["fields_total"] == 143 for m in BAKE["models"]), \
    "one denominator for all three — a shared scale is only honest if the sets are the same"
assert all(SHARE[m["name"]] > BAKE["line"] for m in BAKE["models"]), \
    "all three clear the 85% line; B07 draws ONE rule through all three tracks because of it"
assert WINNER["runaway"] == 0 and sum(r["runaway"] for r in RUNNERS) == 5
assert BAKE["documents"] == 29 and BAKE["cost_usd"] == 0 and BAKE["gpu_gb"] == 8
assert BAKE["share_before_corrections"] < round(SHARE[WINNER["name"]], 2), \
    "B07's and B08's caveat: 99% is AFTER corrections, 95% before"
assert BAKE["valid_answers"]["got"] == BAKE["valid_answers"]["of"] == BAKE["documents"]

# ── the values figdata.json does not carry ────────────────────────────────────
NOT_IN_FIGDATA = "not in figdata.json — from narration_script.md and the project documents"
MYCROFT_RECIPES = {
    "count": "~99",
    "note": "Mycroft runs agents for news, patents and hiring. None of ~99 recipes tracks "
            "debt or credit.",
    "where": "the Mycroft repo's recipes/",
}
PIPELINE = [
    ("SEC filings", ["8-K notices", "prospectuses", "term sheets"], False),
    ("Readers", ["one per filing", "run in parallel", "local model, $0"], False),
    ("Ledger", ["each bond and loan:", "amount, rate, due date"], True),
    ("Signal", ["total debt", "new borrowing", "due in 1–2 years"], False),
]
COARSE_EXAMPLES = [
    'Microsoft’s 13 "bonds" are really 13 batches of bonds.',
    "Oracle’s quarterly reports list only the newest few.",
]
PIT_SERVER = {
    "what": "Ask it for a filing published after the report you are graded on, and it refuses.",
    "built": True,
    "where": "src/ai_debt_tracker/mcp_servers/edgar_pit_core.py, tests/test_edgar_pit.py",
}

HANDLE = "@HumanitariansAI"
SEGMENT = "Grounding an AI Debt Tracker in Real SEC Filings"
SLUG = "grounding-an-ai-debt-tracker-in-real-sec-filings"
KICKER = "Irreducibly Human"     # GATE L rule 7 — the FIXED claude-hai series name
GREETING = "Salve, HAI"          # Latin. Never repeats a language; see metadata note.


def num(n):
    return f"{n:,}"


def pct1(x):
    return f"{x * 100:.1f}%"


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


LOCAL = "reel-local/GroundingTheDebtTracker"
beats = []

# ── B00 · COLD OPEN ───────────────────────────────────────────────────────────
beats.append(beat(
    "B00", "COLD OPEN", "BOOKEND",
    "Hi, I'm Om Mali. This video is about the A I Debt Tracker, a new Mycroft project that "
    "follows the bonds and loans paying for the A I build out, and about how I grounded it in "
    "real S E C filings before building the agent. The answer key, the cut off that stops it "
    "peeking, the matcher and the model are measured. The agent itself is not written yet.",
    21,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": GREETING,
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "New project. Before I write the debt-tracking agent, ground it: build the answer "
            "key from real SEC filings, refuse it anything published after the report it is "
            "graded on, and tell me what it can actually be graded at."
        ),
        "runningText": "edgar_pit.get(cik, as_of=…)…",
        "folderLabel": HANDLE,
        "modelLabel": "Opus 5",
        "effortLabel": "High",
        "output": [
            f"{CASES['total']} dated test cases across {UNI['ai'] + UNI['non_ai']} companies, "
            f"read only up to each cut-off",
            f"{MEASURED_BY_BOND} of {UNI['ai']} AI companies can be graded bond by bond — "
            f"not the {ASSUMED} I assumed",
            f"and the smallest local model read {pct0(SHARE[WINNER['name']])} of the bond "
            f"details, at ${BAKE['cost_usd']}",
        ],
    }, "type-on", [
        {"at": "on 'a new Mycroft project'", "event": "The ask types into the Claude composer."},
        {"at": "on 'before building the agent'", "event": "The result lands ANSWERED with three output lines."},
    ], intent="COLD OPEN LAW: the ask is the week itself — ground the project before writing it. Lands ANSWERED."),
))

# ── B01 · WHY DEBT ────────────────────────────────────────────────────────────
beats.append(beat(
    "B01", "WHY DEBT", "REMOTION",
    "The A I build out is increasingly paid for with borrowed money. In twenty twenty five, "
    "the five biggest cloud companies sold a hundred and twenty one billion dollars of U S "
    "bonds. Their average over the previous five years was twenty eight billion. Mycroft has "
    "agents for news, patents and hiring. None of them watches debt.",
    19,
    remotion("GDTBorrowing", LOCAL, {
        "sparkLine": "Debt is paying for the build-out. Nothing was watching it.",
        "eyebrow": "AI DEBT TRACKER · WEEK 1",
        "title": "AI is increasingly built with borrowed money",
        "subtitle": "US corporate bonds sold by " + ", ".join(ISS["companies"][:-1])
                    + " and " + ISS["companies"][-1],
        "bars": [
            {"label": "2020–2024, average per year", "value": ISS["avg_2020_2024"], "hot": False},
            {"label": "2025", "value": ISS["y2025"], "hot": True},
        ],
        "unit": "bn",
        "multipleLabel": f"{ISS['multiple']}×",
        "multipleNote": "the five-year average",
        "gapLabel": "the gap this project is for",
        "gapNote": MYCROFT_RECIPES["note"] + f"  ({MYCROFT_RECIPES['where']}; {NOT_IN_FIGDATA})",
        "source": f"SOURCE: {ISS['source']} · figdata.json",
    }, "grow", [
        {"at": "on 'a hundred and twenty-one billion'", "event": "The 2025 bar grows past the five-year average."},
        {"at": "on 'None of them watches debt'", "event": "The gap line lands under both bars."},
    ], intent="One scale, two bars, so 4.3× is seen rather than asserted. The gap is the reason the project exists."),
))

# ── B02 · WHAT IT WILL DO ─────────────────────────────────────────────────────
beats.append(beat(
    "B02", "WHAT IT WILL DO", "REMOTION",
    "The agent will watch S E C filings from twenty five A I companies, read each debt "
    "announcement, and keep a ledger of every bond and loan: the amount, the interest rate, "
    "the due date. From that ledger it produces a signal. Total debt, new borrowing, and what "
    "falls due in the next two years. None of this is built yet.",
    20,
    remotion("GDTPipeline", LOCAL, {
        "sparkLine": "Four stages. None of them written yet.",
        "eyebrow": "AI DEBT TRACKER · THE DESIGN",
        "title": "What the agent will do",
        "subtitle": f"{UNI['ai']} AI-sector companies: cloud, chips, data centres, power, "
                    f"AI software",
        "stages": [{"name": n, "lines": ls, "hot": h} for n, ls, h in PIPELINE],
        "tenseNote": "Design, not status. Week 1 built the answer key, the cut-off server, "
                     "the matcher and the model test — not the agent.",
        "source": f"DESIGN: AI Debt Tracker DESIGN.md, Mycroft (2026) · universe_v1.json "
                  f"({NOT_IN_FIGDATA})",
    }, "stagger", [
        {"at": "per stage", "event": "Each box lands in turn, left to right."},
        {"at": "on 'None of this is built yet'", "event": "The tense note lands under the row."},
    ], intent="TENSE DISCIPLINE: a four-box pipeline reads as a description of something that exists, so the frame says in writing that it does not."),
))

# ── B03 · THE CUT-OFF ─────────────────────────────────────────────────────────
beats.append(beat(
    "B03", "THE CUT-OFF", "REMOTION",
    "Each quarter's ledger is graded against that company's next quarterly report, which is "
    "published afterwards. So the answer always arrives later than the evidence. A point in "
    "time server I did build enforces that: ask it for a filing dated after the report you "
    "are being graded on, and it refuses. Without that refusal, every number later in this "
    "video would be worthless.",
    22,
    remotion("GDTCutoff", LOCAL, {
        "sparkLine": "The answer always arrives after the evidence.",
        "eyebrow": "AI DEBT TRACKER · THE CUT-OFF",
        "title": "Graded against a report it cannot have read",
        "ledgerLabel": "what the agent files",
        "ledger": "a ledger for the quarter — every bond and loan, with amount, rate and due date",
        "gradedLabel": "graded against",
        "answer": "the company's NEXT quarterly report",
        "answerNote": "its debt, machine-readable (XBRL), published after the quarter closes",
        "cutoffLabel": "point-in-time server · built and tested",
        "cutoff": PIT_SERVER["what"],
        "whyNote": "Without the refusal, every later number in this video is a model that was "
                   "shown the answer.",
        "source": f"SOURCE: {PIT_SERVER['where']} ({NOT_IN_FIGDATA})",
    }, "descend", [
        {"at": "on 'graded against'", "event": "A dashed rule descends from the ledger to the later report."},
        {"at": "on 'it refuses'", "event": "The cut-off rule lands beneath both boxes."},
    ], intent="The grading relation is drawn, not implied — the beat is that the answer is published after the evidence."),
))

# ── B04 · COULD IT FAIL ───────────────────────────────────────────────────────
beats.append(beat(
    "B04", "COULD IT FAIL", "REMOTION",
    "Before building anything, I asked whether it could fail. On forty six real company "
    "quarters, eighty seven and a half percent of new bonds were announced in a filing before "
    "the report showed them. And copying last quarter forward is wrong in twenty one of those "
    "forty six. So there is something to beat.",
    18,
    remotion("GDTSpike", LOCAL, {
        "sparkLine": "Could it fail? Two ways, tested first.",
        "eyebrow": "AI DEBT TRACKER · COULD IT FAIL",
        "title": "Tested before anything was built",
        "subtitle": f"{SPIKE['quarters']} real company-quarters, {SPIKE['companies']} "
                    f"AI-sector companies",
        "rows": [
            {
                "claim": "Debt changes are announced",
                "detail": f"{ANN['got']} of {ANN['of']} new bonds, in a filing before the "
                          f"report showed them",
                "share": ANN["share"], "line": ANN["line"], "verdict": "PASS", "hot": True,
            },
            {
                "claim": "Copying last quarter is wrong",
                "detail": f"{HEAD['got']} of {HEAD['of']} quarters changed, confirmed by an "
                          f"announcement",
                "share": HEAD["share"], "line": HEAD["line"], "verdict": "PASS", "hot": False,
            },
        ],
        "legend": "dashed = the pass mark, written down before the test ran",
        "conservativeNote": f"{HEAD['got']} of {HEAD['of']} is the conservative count. Raw, "
                            f"carry-forward differed in {HEAD['raw']} of {HEAD['of']} — some "
                            f"of that is companies changing how they tag, not new debt.",
        "source": "SOURCE: AI Debt Tracker docs/feasibility.md · figdata.json",
    }, "grow", [
        {"at": "on 'eighty-seven and a half percent'", "event": "The first bar grows past its own mark."},
        {"at": "on 'something to beat'", "event": "The second bar lands and the conservative note follows."},
    ], intent="Each test carries its OWN pass mark, because the two marks are different numbers and were both set before the test."),
))

# ── B05 · THE ANSWER KEY ──────────────────────────────────────────────────────
beats.append(beat(
    "B05", "THE ANSWER KEY", "REMOTION",
    "Then I built the answer key: every quarterly report since mid twenty twenty four, for "
    "the twenty five A I companies and seventy five others. The first surprise was in the "
    "tagging. Microsoft's thirteen bonds are really thirteen batches of bonds. Counted by how "
    "much of the debt is actually itemised, fifteen companies can be graded bond by bond, not "
    "the twenty one I had assumed.",
    22,
    remotion("GDTLevels", LOCAL, {
        "sparkLine": "Fifteen, not twenty-one.",
        "eyebrow": "AI DEBT TRACKER · THE ANSWER KEY",
        "title": "Companies tag their debt more coarsely than they appear to",
        "subtitle": f"{UNI['ai']} AI companies · every quarterly report, "
                    f"{UNI['reports_from']} – {UNI['reports_to']} · "
                    f"{UNI['non_ai']} non-AI companies held alongside",
        "total": UNI["ai"],
        "segments": [
            {"level": l["level"][0].upper() + l["level"][1:], "companies": l["companies"],
             "note": l["note"], "hot": l["level"] == "bond by bond"}
            for l in LEVELS
        ],
        "assumed": ASSUMED,
        "assumedLabel": f"assumed {ASSUMED} — {FIG['levels_assumed_basis']}",
        "measuredLabel": f"The same {UNI['ai']} companies, split by how much of each one's "
                         f"debt its report itemises.",
        "examples": COARSE_EXAMPLES,
        "gateNote": f"The gate is coverage ≥ {pct0(GATE['coverage_line'])}. "
                    f"{GATE['qualified_on_coverage']} companies qualified outright; one more "
                    f"moved up on a {GATE['tie']} tie.",
        "source": "SOURCE: universe_v1.json, docs/universe_v1_review.md, "
                  "manifests/week1_gate.json · figdata.json",
    }, "partition", [
        {"at": "on 'the twenty-five AI companies'", "event": "The assumed 21 is bracketed first, in outline."},
        {"at": "on 'fifteen companies'", "event": "The same 25 fill in beneath it, partitioned three ways."},
    ], intent="ONE row of 25, partitioned — not three bars. The beat is that a fixed set splits differently once coverage is measured, so the assumption is drawn OVER the measurement."),
))

# ── B06 · WHAT IT GRADES ON ───────────────────────────────────────────────────
beats.append(beat(
    "B06", "WHAT IT GRADES ON", "REMOTION",
    "So each quarter is graded at the detail its own report gives. That leaves four hundred "
    "and ninety five dated test cases: ninety five to build on, and four hundred held back, "
    "never tuned on. And on the quarters graded bond by bond, bonds now match from one report "
    "to the next ninety three point four percent of the time, above the ninety percent line I "
    "set beforehand.",
    22,
    remotion("GDTSplit", LOCAL, {
        "sparkLine": f"{CASES['dev']} to learn on. {CASES['test']} never touched.",
        "eyebrow": "AI DEBT TRACKER · WHAT IT GRADES ON",
        "title": "Each quarter graded at the detail its own report gives",
        "subtitle": "",
        "totalBig": num(CASES["total"]),
        "totalLabel": "dated test cases",
        "parts": [
            {"big": num(CASES["dev"]), "label": "to build on", "badge": "", "hot": False},
            {"big": num(CASES["test"]), "label": "held back", "badge": "never tuned on",
             "hot": True},
        ],
        "gaugeLabel": "Bonds matched from one report to the next",
        "gaugeShare": MATCH["share"],
        "gaugeLine": MATCH["line"],
        "gaugePct": pct1(MATCH["share"]),
        "gaugeFraction": f"{MATCH['got']} of {MATCH['of']}",
        "lineLabel": f"dashed = {pct0(MATCH['line'])} pass line, set beforehand",
        "caveat": f"On the {MATCH['scope']}, on the {MATCH['split']} split. Across every "
                  f"quarter it is {pct0(MATCH['all_quarters_share'])} — "
                  f"{MATCH['all_quarters_gap']}.",
        "source": "SOURCE: manifests/dev.csv + test.csv, scripts/f1_matching.py (dev) · "
                  "figdata.json",
    }, "count-in", [
        {"at": "on 'four hundred held back'", "event": "The 495 splits into 95 and a held-back 400."},
        {"at": "on 'ninety-three point four percent'", "event": "The gauge fills past its pass line."},
    ], intent="A count broken into its two parts, then ONE gauge — a different object from B05's partition, because this beat is about a split and a score, not a taxonomy."),
))

# ── B07 · THE BAKE-OFF ────────────────────────────────────────────────────────
beats.append(beat(
    "B07", "THE BAKE-OFF", "REMOTION",
    "Last, the model, on my laptop's eight gigabyte G P U. I gave three local models twenty "
    "nine real announcements and no hints, with the rule for picking a winner fixed before "
    "the test. The smallest won. Chwen three at four billion parameters read ninety nine "
    "percent of the details, in about six seconds a filing, at zero cost. The eight billion "
    "version got eighty eight.",
    22,
    remotion("GDTBakeoff", LOCAL, {
        "sparkLine": "The smallest model won.",
        "eyebrow": "AI DEBT TRACKER · THE BAKE-OFF",
        "title": f"Three local models, {BAKE['documents']} real announcements, no hints",
        "subtitle": f"Bond details read correctly · {BAKE['gpu_gb']} GB laptop GPU",
        "models": [
            {
                "name": m["name"],
                "params": f"{m['params_b']}B parameters",
                "share": m["got"] / m["of"],
                "pct": pct0(m["got"] / m["of"]),
                "fraction": f"{m['got']} / {m['of']}",
                "loops": "never looped" if m["runaway"] == 0
                         else f"{m['runaway']} looped until cut off",
                "hot": m["name"] == WINNER["name"],
            }
            for m in MODELS
        ],
        "line": BAKE["line"],
        "lineLabel": f"one pass line, {pct0(BAKE['line'])}, fixed before the test — the same "
                     f"rule for all three",
        "stats": [
            {"big": f"{WINNER['median_s']} s", "small": f"median per filing, {WINNER['name']}"},
            {"big": f"{BAKE['valid_answers']['got']} / {BAKE['valid_answers']['of']}",
             "small": "valid answers"},
            {"big": f"${BAKE['cost_usd']}", "small": "laptop GPU, no paid API"},
        ],
        "caveat": f"One plain prompt, not the finished system. "
                  f"{pct0(SHARE[WINNER['name']])} is after correcting "
                  f"{BAKE['truth_corrections']} expected values the documents themselves "
                  f"contradicted — {pct0(BAKE['share_before_corrections'])} before, same winner.",
        "source": "SOURCE: AI Debt Tracker docs/bakeoff.md (scripts/bakeoff.py), Oct 2026 · "
                  "figdata.json",
    }, "grow", [
        {"at": "on 'the rule fixed before the test'", "event": "One dashed rule drops through all three tracks."},
        {"at": "on 'the smallest won'", "event": "The 4B bar overtakes both 8B bars."},
    ], intent="ONE shared pass line drawn as a single rule, because one rule was written down and all three models were held to it — unlike B04, where each test had its own mark."),
))

# ── B08 · THE LIMITS ──────────────────────────────────────────────────────────
beats.append(beat(
    "B08", "THE LIMITS", "REMOTION",
    "What this does not show. Twenty nine documents is a small set, and that ninety nine "
    "percent is after correcting six expected values the filings themselves contradicted. "
    "Ninety three point four percent is on the per bond quarters; across every quarter it is "
    "eighty five. And fifteen rather than twenty one came down to one company on a four four "
    "tie.",
    20,
    remotion("GDTLimits", LOCAL, {
        "sparkLine": "What the week does not show.",
        "eyebrow": "AI DEBT TRACKER · THE LIMITS",
        "title": "Every number above, and the limit that narrows it",
        "limits": [
            {"claim": f"{pct0(SHARE[WINNER['name']])} of details read",
             "limit": f"{BAKE['documents']} documents is a small set, and the figure is after "
                      f"correcting {BAKE['truth_corrections']} expected values the filings "
                      f"themselves contradicted — {pct0(BAKE['share_before_corrections'])} "
                      f"before, same winner.",
             "hot": True},
            {"claim": f"{pct1(MATCH['share'])} matched",
             "limit": f"on the {MATCH['scope']}, {MATCH['split']} split. Across every quarter "
                      f"it is {pct0(MATCH['all_quarters_share'])}.",
             "hot": False},
            {"claim": f"{MEASURED_BY_BOND} graded bond by bond",
             "limit": f"{GATE['qualified_on_coverage']} qualified on coverage; the "
                      f"{MEASURED_BY_BOND}th moved up on a {GATE['tie']} tie.",
             "hot": False},
            {"claim": f"{HEAD['got']} of {HEAD['of']} quarters changed",
             "limit": f"the conservative count. Raw it is {HEAD['raw']} of {HEAD['of']}, but "
                      f"some of that is re-tagging rather than new debt.",
             "hot": False},
            {"claim": f"${ISS['y2025']}bn sold in 2025",
             "limit": "five companies' bond sales, from Bank of America via Reuters — context "
                      "for the project, not a measurement by it.",
             "hot": False},
        ],
        "nextLabel": "next",
        "next": "The grader and the do-nothing baseline — so the score the agent has to beat "
                "exists before the agent does.",
        "source": "SOURCE: narration_script.md notes · docs/bakeoff.md · "
                  "manifests/week1_gate.json · figdata.json",
    }, "stagger", [
        {"at": "per limit", "event": "Each claim lands with the limit that narrows it."},
        {"at": "on 'a four-four tie'", "event": "The NEXT block lands at the foot of the frame."},
    ], intent="Every episode in this series ends on its own limits. Each limit is tied to the claim it narrows, never left as a free-floating caveat list."),
))

# ── B09 · VERDICT ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B09", "VERDICT", "BOOKEND",
    "So: the A I build out is being financed with debt, at four times the recent pace, and "
    "nothing in Mycroft tracks it. The agent will be graded against the report published "
    "after it files, and a server I built refuses it anything later. Four hundred and ninety "
    "five dated cases exist, four hundred of them held back. Fifteen companies can be graded "
    "bond by bond, not twenty one. And a four billion parameter model on a laptop reads the "
    "details better than two eight billion ones, for nothing.",
    28,
    remotion("ClaudeVerdictArtifact", "proven-core/ClaudeVerdictArtifact", {
        "artifactTitle": SEGMENT,
        "artifactHeading": "What week 1 grounded, and what it did not build",
        "artifactLines": [
            f"${ISS['y2025']}bn of bonds from {len(ISS['companies'])} cloud companies in "
            f"2025, {ISS['multiple']}× their ${ISS['avg_2020_2024']}bn five-year average — and "
            f"no Mycroft agent watches debt. That gap is the project.",
            f"Every quarter is graded against the company's NEXT report, and the "
            f"point-in-time server refuses any filing published after it. Built and tested; "
            f"the agent that keeps the ledger is not.",
            f"{MEASURED_BY_BOND} of {UNI['ai']} companies can be graded bond by bond, not the "
            f"{ASSUMED} assumed — measured by how much of each company's debt its report "
            f"itemises, not by counting tags.",
            f"{num(CASES['total'])} dated cases, {num(CASES['test'])} held back and never "
            f"tuned on. Bonds match report to report {pct1(MATCH['share'])} on the per-bond "
            f"quarters, against a {pct0(MATCH['line'])} line set beforehand.",
            f"{WINNER['name']} read {pct0(SHARE[WINNER['name']])} of the bond details in "
            f"{WINNER['median_s']}s a filing at ${BAKE['cost_usd']}, ahead of both 8B models "
            f"— on {BAKE['documents']} documents, after {BAKE['truth_corrections']} "
            f"corrections.",
        ],
    }, "stagger", [
        {"at": "per clause", "event": "Five findings stagger in, one per spoken clause."},
    ], intent="Judgment beat. The artifact page is the point (ILLUSTRATE LAW carve-out)."),
))

# ── B10 · HANDOFF ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B10", "HANDOFF", "BOOKEND",
    "Your turn. Paste this into Claude. Before you build an agent, go and find out what its "
    "answer key can actually say. Mine turned out to be coarser than I had assumed, and it "
    "changed what the agent is allowed to be graded on. Check before you build, not after.",
    17,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": "Your turn.",
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "Before I build this agent, inspect the ground truth I plan to grade it on. For "
            "each case, tell me the finest level of detail the source actually supports — and "
            "count how many cases support less than I assumed."
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
    "Grounding an A I debt tracker in real S E C filings. Week one of the A I Debt Tracker. "
    "Om Mali, for Humanitarians A I.",
    9,
    remotion("ClaudeTitleOutro", "proven-core/ClaudeTitleOutro", {
        "title": SEGMENT,
        "handle": HANDLE,
        # `subline`, not `subtitle` — the wrong name ships the outro reading
        # "bot vs bot, season one", a default from an unrelated show (week 10, B11).
        "subline": "week 1 · the AI Debt Tracker",
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
    "greeting_note": "hello lexicon: Latin. HAI persona takes only the shortest cues (Hi · Ola · Hej · Ciao · Hallo · Salut · Ahoj · Szia · Tere · Moi · Hoi · Labas · Salve). Rotate; never repeat a language.",
    "aspect_ratio": "16:9",
    "fps": 24,
    "lead_silence_s": 0.4,
    "note": (
        "ai-explainer / claude-hai. AI Debt Tracker WEEK 1 — a second reel of a new project, "
        "not week 13 of the Private AI Valuation Agent. ILLUSTRATE LAW: the Claude UI appears "
        "at B00 (cold open, answered), B09 (verdict artifact), B10 (handoff) and B11 (outro) "
        "only — every body beat illustrates its concept as a native animated Remotion scene "
        "(REBUILD LAW). The six source PNGs and their SVG sources are REFERENCE in pantry/, "
        "never slotted as media. The script's seven sections are split into eight body beats "
        "(0:32 splits into B02 design and B03 cut-off) and a limits beat is added; the split "
        "is logged in BUILD-LOG.md. FOUR THINGS NOT TO GET WRONG: the agent is NOT built, only "
        "the ground under it; 15 rather than 21 is a measurement by coverage, not a recount; "
        "93.4% is on the per-bond quarters and 85% across all of them; and 99% is after six "
        "truth corrections on a 29-document set."
    ),
}

sheet = {"metadata": META, "beats": beats}

body = [b for b in beats if b["beat_id"] not in ("B00", "B09", "B10", "B11")]
words = {b["beat_id"]: len(b["narration_text"].split()) for b in beats}
lo = min(words[b["beat_id"]] for b in body)
hi = max(words[b["beat_id"]] for b in body)
# 45-68, the band weeks 9-11 settled on. The script targets 3:00 for its own seven sections;
# the four bookends this channel requires are additive, and the measured runtime is recorded
# in PEDAGOGY.md rather than fudged by cutting a body beat below the band.
assert 45 <= lo and hi <= 68, f"body beat word budget 45-68 violated: {lo}-{hi}"
assert len(body) == 8 and len(beats) == 12

if "--check" in sys.argv:
    print("[adt-w1] all assertions pass")
    sys.exit(0)

out = HERE / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"[adt-w1] wrote {out}  — {len(beats)} beats")
print("[adt-w1] narration words: " + " ".join(f"{k}={v}" for k, v in words.items()))
print(f"[adt-w1] body beats {lo}-{hi}w (band 45-68), total {sum(words.values())}w")
print(f"[adt-w1] derived: {ISS['multiple']}x issuance · {MEASURED_BY_BOND}/{UNI['ai']} "
      f"bond-by-bond vs {ASSUMED} assumed · {CASES['dev']}+{CASES['test']}={CASES['total']} "
      f"cases · match {pct1(MATCH['share'])} vs line {pct0(MATCH['line'])} "
      f"(all quarters {pct0(MATCH['all_quarters_share'])}) · winner {WINNER['name']} "
      f"{pct0(SHARE[WINNER['name']])} at {WINNER['median_s']}s, ${BAKE['cost_usd']}")
