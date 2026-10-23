#!/usr/bin/env python3
"""
build_beat_sheet.py — week 11, Documenting the System and Making the Demo Re-runnable.

Writes beat_sheet.json with EVERY on-screen figure injected from figdata.json. No number is
typed into a scene or a beat sheet by hand.

THE FRAMING ASSERTION of this reel is PUBLISHED_ZEROES. `w12-priorart.png` tabulates THREE
documents at "BEFORE 0", but one of them — proposal.md — did not exist, so its zero is a
property of an absent file rather than of a document that failed the requirement. The figure's
own caption is careful ("in either published document"); its table is not. The genuine finding
is TWO published documents at a real zero, and B03 draws that distinction on the frame. The
assertion fails the build if that split ever changes, because the beat's whole claim is which
zero is which.

THREE THINGS IN THIS REEL ARE NOT IN figdata.json. They come from narration_script.md and the
documents behind it, are passed as named constants below, and every screen that uses one says
so:
  · PRIOR_ART_NAMES  — Caplight, Gornall & Strebulaev, Agarwal, Chernenko, Kwon
  · LOAD_BEARING     — what the Gornall & Strebulaev citation actually changed
  · LM_SITES         — "exactly two places a language model sits, neither touching a number"

Usage:  python build_beat_sheet.py            (writes beat_sheet.json)
        python build_beat_sheet.py --check    (assertions only, writes nothing)
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIG = json.loads((HERE / "figdata.json").read_text(encoding="utf-8"))

DOCS = FIG["documents"]
PRIOR = FIG["prior_art"]
REMARK = FIG["remark"]
LAYERS = FIG["layers"]
DEMO = FIG["demo"]

# ── derived, never typed ──────────────────────────────────────────────────────
ABSENT = [d for d in DOCS if not d["existed"]]
PRESENT = [d for d in DOCS if d["existed"]]
NEW_LINES = sum(d["lines_now"] for d in ABSENT)
GROWN_LINES = sum(d["lines_now"] - d["lines_before"] for d in PRESENT)

# The split B03 exists for: a zero in a file that did not exist is not the same finding as a
# zero in a file that did.
PUBLISHED_ZEROES = [p for p in PRIOR if p["existed"]]
NEW_DOC_ZEROES = [p for p in PRIOR if not p["existed"]]
CITES_ADDED = sum(p["after"] for p in PRIOR)
CITES_PUBLISHED = sum(p["after"] for p in PUBLISHED_ZEROES)

BY_LAYER = {l["layer"]: l for l in LAYERS}
TABLES_TOTAL = sum(len(l["tables"]) for l in LAYERS)
ROWS_TOTAL = sum(l["rows"] for l in LAYERS)
RAW = BY_LAYER["raw / filed"]
JUDGMENT = BY_LAYER["judgment"]
RESOLVED = BY_LAYER["resolved"]


def table_rows(layer, name):
    return next(t["rows"] for t in layer["tables"] if t["table"] == name)


HOLDINGS = table_rows(RAW, "raw_holdings")
MATCHES = table_rows(JUDGMENT, "match_decisions")
MARKS = table_rows(RESOLVED, "marks")
REVIEWS = table_rows(JUDGMENT, "review_decisions")
RUNS = table_rows(RAW, "runs")
BLOCKED = HOLDINGS - MARKS

SHARE = REMARK["share_unchanged"]

# ── assertions ────────────────────────────────────────────────────────────────
assert len(DOCS) == 6, "the plan names six documents; B02's headline counts them"
assert len(ABSENT) == 3 and len(PRESENT) == 3
assert all(d["lines_before"] == 0 for d in ABSENT), "an absent file has no 'before'"
assert all(d["lines_now"] > d["lines_before"] for d in DOCS), "nothing shrank"
assert NEW_LINES == 444 and GROWN_LINES == 104

# THE FRAMING ASSERTION. B03's claim is about WHICH zero is which.
assert len(PRIOR) == 3 and len(PUBLISHED_ZEROES) == 2 and len(NEW_DOC_ZEROES) == 1, \
    "B03 splits a real zero in 2 published documents from 1 zero in a file that did not exist"
assert all(p["before"] == 0 for p in PRIOR), "every one was at zero before"
assert all(p["after"] > 0 for p in PRIOR)
assert CITES_ADDED == 22 and CITES_PUBLISHED == 13

assert REMARK["unchanged"] == 1019 and REMARK["steps"] == 4079
assert round(REMARK["unchanged"] / REMARK["steps"], 4) == SHARE == 0.2498
assert REMARK["marks"] == 5178

assert len(LAYERS) == 3 and TABLES_TOTAL == FIG["tables_total"] == 15, \
    "the layer tables must account for every table the figure counts"
assert all(l["rows"] == sum(t["rows"] for t in l["tables"]) for l in LAYERS), \
    "each layer's row total must be the sum of its own tables, not a separate number"
assert [l["mutability"] for l in LAYERS] == ["immutable", "append-only", "rebuildable"]

# The identity B05 is built around: every filed holding carries a match decision.
assert MATCHES == HOLDINGS == 5806, \
    "B05 shows one judgment row per filed row; if that ever breaks the beat is wrong"
assert MARKS < HOLDINGS and BLOCKED == 327

assert DEMO["acts"] == 5 and DEMO["write_statements"] == 0 and DEMO["files_scanned"] == 5

# ── the three values figdata.json does not carry ──────────────────────────────
PRIOR_ART_NAMES = ["Caplight", "Gornall & Strebulaev", "Agarwal", "Chernenko", "Kwon"]
LOAD_BEARING = {
    "finding": "funds write up every share class to the latest round price",
    "who": "Gornall & Strebulaev",
    "what_it_changed": "dispersion is measured per company with the share class recorded",
    "overturned": "an earlier draft's rule",
}
LM_SITES = {
    "count": 2,
    "note": "exactly two places a language model sits, and neither touches a number",
}

HANDLE = "@HumanitariansAI"
# PLAIN hyphen, deliberately. A non-breaking hyphen (U+2011) fixed a cosmetic wrap in the
# landscape outro ("Re-" above "runnable") and made the word unbreakable, which pushed the
# title past the title-safe right edge at 1080 wide — GATE V, 2 BLOCKERs on the 9:16 cut.
# A hyphen break is legitimate typesetting; an edge bleed is not.
SEGMENT = "Documenting the System and Making the Demo Re-runnable"
KICKER = "Irreducibly Human"     # GATE L rule 7 — the FIXED claude-hai series name
NOT_IN_FIGDATA = "not in figdata.json — from narration_script.md and the documents themselves"


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


beats = []

# ── B00 · COLD OPEN ───────────────────────────────────────────────────────────
beats.append(beat(
    "B00", "COLD OPEN", "BOOKEND",
    "Hi, I'm Om Mali. This video is about the last week of the build: writing the documents "
    "that explain the system, discovering a stated requirement I had met zero times, and "
    "turning the demo into something that re runs instead of something that was true once. "
    "The code was finished. What was missing was the part that lets someone else understand "
    "it without me sitting next to them.",
    23,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": "Hoi, HAI",
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "The code is done. Audit the documents the plan names against the last commit — "
            "do not trust my memory — and tell me which stated requirements I have actually "
            "met. Then make the demo re-runnable."
        ),
        "runningText": "git show HEAD:<path>…",
        "folderLabel": HANDLE,
        "modelLabel": "Opus 5",
        "effortLabel": "High",
        "output": [
            f"{len(DOCS)} documents named in the plan — {len(ABSENT)} of them did not exist",
            f"one stated requirement sat at zero in {len(PUBLISHED_ZEROES)} published documents",
            f"and the demo is {DEMO['acts']} acts with {DEMO['write_statements']} write "
            f"statements, every figure queried live",
        ],
    }, "type-on", [
        {"at": "on 'the last week of the build'", "event": "The ask types into the Claude composer."},
        {"at": "on 'a stated requirement I had met zero times'", "event": "The result lands ANSWERED with three output lines."},
    ], intent="COLD OPEN LAW: the ask is an AUDIT, which is what the week turned out to be about — the reel opens on the instruction not to trust memory."),
))

# ── B01 · EXECUTIVE SUMMARY ───────────────────────────────────────────────────
beats.append(beat(
    "B01", "EXECUTIVE SUMMARY", "REMOTION",
    "Three things this week, and none of them is code. The documents that explain the system. "
    "A literature requirement I had written down and never met. And a demo that re runs "
    "instead of one that was true on the day I recorded it. Every count here is measured "
    "against the last commit, not remembered.",
    21,
    remotion("W11Bluf", "reel-local/DocumentingTheSystem", {
        "sparkLine": "Measured against the commit, not remembered.",
        "headline": "The code was the easy part.",
        "pieces": [
            {"name": "The documents", "who": "what lets someone else understand the system",
             "gives": f"{len(ABSENT)} of {len(DOCS)} named documents did not exist",
             "scale": f"{num(NEW_LINES)} lines written · {num(GROWN_LINES)} added"},
            {"name": "The demo", "who": "something that re-runs, not something recorded",
             "gives": f"{DEMO['acts']} acts, every figure queried live",
             "scale": f"{DEMO['write_statements']} write statements across "
                      f"{DEMO['files_scanned']} files"},
        ],
        "haveLabel": "and one requirement I had written down",
        "have": "The plan says the published documents must cite the prior-art literature honestly.",
        "keyLabel": "times I had met it",
        "joinKey": "zero",
        "keyNote": (
            f"Not thin coverage. Zero mentions in {len(PUBLISHED_ZEROES)} published documents, "
            f"found by grep rather than by memory."
        ),
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'three things this week'", "event": "The headline sets, then the two deliverables land side by side."},
        {"at": "on 'a literature requirement'", "event": "The stated requirement lands beneath them."},
        {"at": "on 'never met'", "event": "A 'zero' chip lands and is struck through."},
    ], intent="The BLUF leads with the week's finding rather than its output, because the finding is what the author did not know at the start."),
))

# ── B02 · THE AUDIT ───────────────────────────────────────────────────────────
beats.append(beat(
    "B02", "THE AUDIT", "REMOTION",
    "The plan names six documents. Rather than assume, I checked each one against the last "
    "commit. Three of them did not exist at all. Not thin, not stale. Absent. The proposal, "
    "the system architecture and the data architecture. The audit found them. The plan had "
    "not predicted them.",
    20,
    remotion("W11Docs", "reel-local/DocumentingTheSystem", {
        "sparkLine": "Not thin. Not stale. Absent.",
        "eyebrow": "WEEK 11 · THE AUDIT",
        "title": f"{len(DOCS)} documents named, {len(ABSENT)} of them absent",
        "subtitle": "audited with git show HEAD against the working tree, at build time",
        "rows": [
            {"document": d["document"], "before": d["lines_before"],
             "now": d["lines_now"], "absent": not d["existed"]}
            for d in DOCS
        ],
        "absentLabel": "did not exist",
        "totalsLabel": (
            f"{num(NEW_LINES)} lines written from nothing · {num(GROWN_LINES)} added to what "
            f"was already there"
        ),
        "note": (
            "The audit found them; the plan did not predict them. All three were written from "
            "the project's own measured figures rather than from the plan's prose."
        ),
        "source": "SOURCE: figdata.json — documents[]; the before column IS the last commit",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'the plan names six documents'", "event": "Six rows land with their before and after line counts."},
        {"at": "on 'did not exist at all'", "event": "The three absent rows take the accent and their before column reads 'did not exist' rather than a number."},
        {"at": "on 'the plan had not predicted them'", "event": "The totals land beneath."},
    ], intent="Rebuild of pantry/w12-docs.png. An absent file has no 'before' NUMBER, so the frame prints words there rather than a zero that would sit in the same column as 231 and 956."),
))

# ── B03 · A REQUIREMENT AT ZERO ───────────────────────────────────────────────
beats.append(beat(
    "B03", "A REQUIREMENT AT ZERO", "REMOTION",
    "Then the one that stung. The plan says the published documents must cite the prior art "
    "literature honestly. I grepped for every name. Zero. And the honest version of that is "
    "narrower than it first looks: two published documents were genuinely at zero. The third "
    "was the proposal, which did not exist yet, so its zero is a missing file and not a "
    "failed requirement.",
    24,
    remotion("W11PriorArt", "reel-local/DocumentingTheSystem", {
        "sparkLine": "Which zero is which.",
        "eyebrow": "WEEK 11 · THE REQUIREMENT",
        "title": "One stated requirement, zero mentions",
        "subtitle": 'plan.md: "citing the prior-art literature honestly"',
        "quoteLabel": "the names I grepped for",
        "names": PRIOR_ART_NAMES,
        "realLabel": f"a real zero — {len(PUBLISHED_ZEROES)} published documents",
        "real": [
            {"document": p["document"], "before": p["before"], "after": p["after"]}
            for p in PUBLISHED_ZEROES
        ],
        "trivialLabel": f"and {len(NEW_DOC_ZEROES)} zero that is not a finding",
        "trivial": [
            {"document": p["document"], "before": p["before"], "after": p["after"]}
            for p in NEW_DOC_ZEROES
        ],
        "trivialNote": (
            "The proposal did not exist, so its zero is an absent file rather than a document "
            "that failed the requirement. The source figure tabulates all three in one column; "
            "the distinction is the finding."
        ),
        "totalLabel": f"{CITES_PUBLISHED} citations added where the requirement actually bit",
        "source": (
            f"SOURCE: figdata.json — prior_art[]; the split is derived and asserted. "
            f"The five names are {NOT_IN_FIGDATA}."
        ),
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'I grepped for every name'", "event": "The five names land as a row of chips."},
        {"at": "on 'two published documents were genuinely at zero'", "event": "Those two land with their real before-and-after."},
        {"at": "on 'a missing file and not a failed requirement'", "event": "The third lands separately, dimmed, with the reason."},
    ], intent="Not in the script's framing and not in the figure's table. The figure's own caption says 'either published document' while its table shows three rows at zero; this beat draws the distinction the caption implies."),
))

# ── B04 · ONE CITATION THAT IS LOAD-BEARING ───────────────────────────────────
beats.append(beat(
    "B04", "LOAD-BEARING", "REMOTION",
    "A citation count is not a literature review, and most of those twenty two are context. "
    "One is load bearing. Gornall and Strebulaev established that funds write up every share "
    "class to the latest round price. I reproduced that on this cohort, and it is the reason "
    "dispersion is measured per company with the share class recorded. It overturned an "
    "earlier draft's rule.",
    24,
    remotion("W11LoadBearing", "reel-local/DocumentingTheSystem", {
        "sparkLine": "A citation that changed the code.",
        "eyebrow": "WEEK 11 · LOAD-BEARING",
        "title": "One of them is not decoration",
        "subtitle": f"{CITES_ADDED} citations added · this is the one that changed a rule",
        "decorativeLabel": "context",
        "decorativeCount": CITES_ADDED - 1,
        "loadLabel": "load-bearing",
        "loadCount": 1,
        "who": LOAD_BEARING["who"],
        "finding": LOAD_BEARING["finding"],
        "steps": [
            {"step": "established in the literature", "text": LOAD_BEARING["finding"]},
            {"step": "reproduced on this cohort", "text": "not cited and assumed — checked against the panel"},
            {"step": "so the rule changed", "text": LOAD_BEARING["what_it_changed"]},
            {"step": "which overturned", "text": LOAD_BEARING["overturned"]},
        ],
        "note": (
            "A citation that only decorates a document can be added at the end. This one had "
            "to be read before the measurement was correct."
        ),
        "source": f"SOURCE: {NOT_IN_FIGDATA} — figdata.json carries the counts, not the argument",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'most of those twenty two are context'", "event": "The 22 split into 21 context and 1 load-bearing."},
        {"at": "on 'Gornall and Strebulaev'", "event": "The chain lands: established, reproduced, rule changed, draft overturned."},
        {"at": "on 'overturned an earlier draft's rule'", "event": "The last step takes the accent."},
    ], intent="SHOW-DON'T-TELL: 'load-bearing' is drawn as a four-step chain ending in a rule that CHANGED, because a citation that changes nothing is the thing this beat is distinguishing itself from."),
))

# ── B05 · THE LADDER ──────────────────────────────────────────────────────────
beats.append(beat(
    "B05", "THE LADDER", "REMOTION",
    "The architecture document's spine is one idea: fifteen tables in three layers, and each "
    "layer is allowed to change in a different way. What the S E C filed is immutable. What a "
    "human decided is append only. What the code derived is rebuildable. Every filed holding "
    "carries exactly one match decision, which is why the middle layer has the same row count "
    "as the first.",
    25,
    remotion("W11Layers", "reel-local/DocumentingTheSystem", {
        "sparkLine": "Three layers, three rules for changing.",
        "eyebrow": "WEEK 11 · THE LADDER",
        "title": f"{TABLES_TOTAL} tables, {len(LAYERS)} layers, three rules",
        "subtitle": "what each layer is allowed to do, not just what it holds",
        "layers": [
            {"layer": l["layer"], "mutability": l["mutability"],
             "tables": len(l["tables"]), "rows": l["rows"],
             "hot": l["mutability"] == "append-only"}
            for l in LAYERS
        ],
        "identityLabel": "one judgment row per filed row",
        "identity": (
            f"raw_holdings {num(HOLDINGS)}  =  match_decisions {num(MATCHES)}"
        ),
        "identityNote": (
            f"Every filed holding carries exactly one match decision. {num(REVIEWS)} of them "
            f"needed a named human. The resolved layer holds {num(MARKS)} marks — "
            f"{num(BLOCKED)} fewer than were filed, and the guards are the difference."
        ),
        "note": (
            "A layer that is allowed to be rebuilt can be deleted and recomputed. A layer that "
            "is append-only cannot, because a human decision is not derivable from anything."
        ),
        "source": "SOURCE: figdata.json — layers[]; each layer's total is asserted equal to the sum of its own tables",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'fifteen tables in three layers'", "event": "Three layer blocks land with their table and row counts."},
        {"at": "on 'append only'", "event": "The judgment layer takes the accent."},
        {"at": "on 'the same row count as the first'", "event": "The 5,806 = 5,806 identity lands beneath."},
    ], intent="The architecture document's core idea, which the script names but no figure draws. MUTABILITY is the subject, so the frame leads with it rather than with row counts."),
))

# ── B06 · EIGHT LINKS ─────────────────────────────────────────────────────────
beats.append(beat(
    "B06", "EIGHT LINKS", "REMOTION",
    "The data architecture document ends with a trace. One headline, twenty five percent of "
    "consecutive observations unchanged, followed down eight links: the published sentence, "
    "the generated figure, the function with its guards, the panel, the match decision, the "
    "named human behind it, the filed position, and the archive file the S E C published. "
    "Break any link and you have an output, not evidence.",
    25,
    remotion("W11Provenance", "reel-local/DocumentingTheSystem", {
        "sparkLine": "Break any link and you have an output.",
        "eyebrow": "WEEK 11 · THE TRACE",
        "title": f"One published number, {pct1(SHARE)}, down to the bytes",
        "subtitle": (
            f"{num(REMARK['unchanged'])} unchanged steps of {num(REMARK['steps'])}, "
            f"over {num(REMARK['marks'])} published marks"
        ),
        "links": [
            {"name": "docs/findings.md part 1", "what": "the published sentence", "end": True},
            {"name": "docs/_findings.json", "what": "the figure as computed", "end": False},
            {"name": "src/signal/findings.py", "what": "remark_frequency(), guards applied", "end": False},
            {"name": "marks", "what": "NOT change_blocked, price not null", "end": False},
            {"name": "match_decisions", "what": "which company, and by what method", "end": False},
            {"name": "review_decisions", "what": "a named human, where method = human", "end": False},
            {"name": "raw_holdings", "what": "the filed position: balance, value_usd", "end": False},
            # Typography: an ASCII arrow in a mono/serif frame reads as a code artifact (weeks 9-10).
            {"name": "filings → data/<qtr>_nport.zip", "what": "accession, period end, the SEC", "end": True},
        ],
        "verdict": "Break any link and you have an output, not evidence.",
        "source": "SOURCE: figdata.json — remark; the chain is data_architecture.md's own",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'twenty five percent'", "event": "The headline sets with its three counts."},
        {"at": "on 'eight links'", "event": "The chain draws downward, one link at a time, the two ends in accent."},
        {"at": "on 'an output, not evidence'", "event": "The verdict lands under the chain."},
    ], intent="Rebuild of pantry/w12-provenance.png. The chain is drawn as a connected descent rather than a list, because the claim is that the links JOIN."),
))

# ── B07 · A DEMO THAT RE-RUNS ─────────────────────────────────────────────────
beats.append(beat(
    "B07", "A DEMO THAT RE-RUNS", "REMOTION",
    "The plan said record a demo. I wrote a script instead. Five acts, every figure queried "
    "live, so a transcript that disagrees with the database is a bug rather than an old file. "
    "It writes nothing. Zero write statements across the demo and the server it calls. Act two "
    "shows a decision a named human already made, and deliberately does not make a new one.",
    24,
    remotion("W11Demo", "reel-local/DocumentingTheSystem", {
        "sparkLine": "A recording is true on the day it was made.",
        "eyebrow": "WEEK 11 · THE DEMO",
        "title": "A demo that re-runs, and writes nothing",
        "subtitle": f"{DEMO['acts']} acts · every figure queried live",
        "acts": [
            {"act": "Act I", "what": "ingest, and the reconciliation"},
            {"act": "Act II", "what": "a review-queue decision a human made", "hot": True},
            {"act": "Act III", "what": "a resolved series"},
            {"act": "Act IV", "what": "propagation"},
            {"act": "Act V", "what": "an MCP query, bounded"},
        ],
        "writesBig": str(DEMO["write_statements"]),
        "writesLabel": (
            f"write statements across {DEMO['files_scanned']} scanned files — the demo and "
            f"the server it calls"
        ),
        "actTwoNote": (
            "Act II shows a decision a named human already made, and does not make a new one. "
            "A demo that recorded a judgment would be a demo clearing a gate for a screenshot."
        ),
        "reRunNote": "A recording is true on the day it was made. This re-runs.",
        "source": "SOURCE: figdata.json — demo; the write-statement count is a static scan",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'five acts'", "event": "The five acts land in order."},
        {"at": "on 'zero write statements'", "event": "The zero lands large, with what was scanned to get it."},
        {"at": "on 'deliberately does not make a new one'", "event": "Act II takes the accent and the reason lands beneath."},
    ], intent="Rebuild of pantry/w12-demo.png, whose own last line runs off the right edge. The zero is the claim, so it is drawn at headline size with the scope of the scan beside it."),
))

# ── B08 · WHAT THE AUDIT DOES NOT COVER ───────────────────────────────────────
beats.append(beat(
    "B08", "WHAT THE AUDIT MISSES", "REMOTION",
    "Four things this week does not establish. The audit covers the six documents the plan "
    "names and no others. A citation count is not a literature review. The write statement "
    "count is a static scan of five files, not a proof. And the run log that makes the chain "
    "datable has two rows in it, which is a start and not a history.",
    24,
    remotion("W11Limits", "reel-local/DocumentingTheSystem", {
        "sparkLine": "A start, not a history.",
        "eyebrow": "WEEK 11 · THE LIMITS",
        "title": "What none of this establishes",
        "limits": [
            {"claim": f"the audit covers {len(DOCS)} documents",
             "limit": "the ones the plan names, and no others — an unnamed gap stays unnamed"},
            {"claim": f"{CITES_ADDED} citations added",
             "limit": "a citation count is not a literature review; only one of them changed a rule"},
            {"claim": f"{DEMO['write_statements']} write statements",
             "limit": f"a static scan of {DEMO['files_scanned']} files, not a proof that nothing writes"},
            {"claim": f"the chain is datable",
             "limit": f"the run log has {RUNS} rows in it — a start, not a history"},
        ],
        "lmLabel": "and where a language model sits in all of this",
        "lmNote": (
            f"Exactly {LM_SITES['count']} places, and neither of them touches a number. "
            f"That is stated in the architecture document rather than left to be inferred."
        ),
        "notShownLabel": "what none of this shows",
        "notShown": [
            "No company valuation. These filings give a fund's share count, never the company's shares outstanding.",
            "Eleven weeks of work, and the last one was mostly finding out what had been assumed.",
        ],
        "source": f"SOURCE: figdata.json — runs, demo, prior_art. The language-model count is {NOT_IN_FIGDATA}.",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'four things this week does not establish'", "event": "Each claim lands with the limit beside it."},
        {"at": "on 'two rows in it'", "event": "The run-log limit takes the accent."},
        {"at": "on 'a start and not a history'", "event": "The closing block lands."},
    ], intent="The reel's last body beat is its own limits, as in every episode of this series. Each limit is attached to the claim it narrows rather than listed separately."),
))

# ── B09 · VERDICT ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B09", "VERDICT", "BOOKEND",
    "Week eleven on one page. Six documents named in the plan, three of which did not exist, "
    "now four hundred and forty four lines written from nothing. A stated requirement that had "
    "been met zero times in two published documents, now cited thirteen times, one of them "
    "load bearing enough to overturn a rule. Fifteen tables in three layers, each with its own "
    "rule for changing. One published number traced down eight links to the archive file the "
    "S E C published. And a demo in five acts with zero write statements.",
    32,
    remotion("ClaudeVerdictArtifact", "proven-core/ClaudeVerdictArtifact", {
        "artifactTitle": f"{SEGMENT} — week 11",
        "artifactHeading": "What the audit found, and what it does not cover",
        "artifactLines": [
            f"The plan named {len(DOCS)} documents and {len(ABSENT)} of them did not exist — "
            f"not thin, absent. {num(NEW_LINES)} lines written from nothing, {num(GROWN_LINES)} "
            f"added to what was there. Audited with git, not from memory.",
            f"A stated requirement sat at zero in {len(PUBLISHED_ZEROES)} published documents. "
            f"The third zero was a file that did not exist yet, which is a different finding "
            f"and is drawn as one. {CITES_PUBLISHED} citations added where the requirement bit.",
            f"One citation is load-bearing: funds write up every share class to the latest "
            f"round price, reproduced on this cohort, which is why dispersion is measured per "
            f"company with the class recorded. It overturned an earlier draft's rule.",
            f"{TABLES_TOTAL} tables in {len(LAYERS)} layers — immutable, append-only, "
            f"rebuildable. Every one of the {num(HOLDINGS)} filed holdings carries exactly one "
            f"match decision, and the {num(BLOCKED)} that are not marks are the guards.",
            f"{pct1(SHARE)} traced down 8 links to the SEC archive file, and a demo of "
            f"{DEMO['acts']} acts with {DEMO['write_statements']} write statements. The run log "
            f"behind the trace has {RUNS} rows — a start, not a history.",
        ],
    }, "stagger", [
        {"at": "per clause", "event": "Five findings stagger in, one per spoken clause."},
    ], intent="Judgment beat. The artifact page is the point (ILLUSTRATE LAW carve-out)."),
))

# ── B10 · HANDOFF ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B10", "HANDOFF", "BOOKEND",
    "Your turn. Paste this into Claude. Take your own plan, list every requirement it states "
    "as a must, and grep for evidence of each one against your last commit rather than against "
    "what you remember. Count the ones at zero. Mine was one, and I had written it down myself.",
    20,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": "Your turn.",
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "Read my plan and list every requirement it states as a MUST. For each one, grep "
            "the repository at HEAD for evidence that it was actually met — not my memory of "
            "it. Tell me which ones are at zero, and which are thin rather than absent."
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
    "Documenting the system, and making the demo re runnable. Week eleven of the Private A I "
    "Valuation Agent. Om Mali, for Humanitarians A I.",
    10,
    remotion("ClaudeTitleOutro", "proven-core/ClaudeTitleOutro", {
        "title": SEGMENT,
        "handle": HANDLE,
        # `subline`, not `subtitle` — the wrong name ships the outro reading
        # "bot vs bot, season one", a default from an unrelated show (week 10, B11).
        "subline": "week 11 · the Private AI Valuation Agent",
    }, "fade", [
        {"at": "on the title", "event": "Title restate, poster-style."},
    ], intent="OUTRO LAW: title restate, handle, nothing that moves."),
))

META = {
    "title": SEGMENT,
    "slug": "documenting-the-system-and-making-the-demo-runnable",
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
    "greeting": "Hoi, HAI",
    "greeting_note": "hello lexicon: Dutch (short form). HAI persona takes only the shortest cues (Hi · Ola · Hej · Ciao · Hallo · Salut · Ahoj · Szia · Tere · Moi · Hoi). Rotate; never repeat a language.",
    "aspect_ratio": "16:9",
    "fps": 24,
    "lead_silence_s": 0.4,
    "note": (
        "ai-explainer / claude-hai. ILLUSTRATE LAW: the Claude UI appears at B00 (cold open, "
        "answered), B09 (verdict artifact), B10 (handoff) and B11 (outro) only — every body "
        "beat illustrates its concept as a native animated Remotion scene (REBUILD LAW). The "
        "four source PNGs and their SVG sources are REFERENCE in pantry/, never slotted as "
        "media. The script's six sections are split into eight body beats; the split is logged "
        "in BUILD-LOG.md. THREE THINGS NOT TO GET WRONG: an absent file's zero is not the same "
        "finding as a published document's zero; a citation count is not a literature review, "
        "and exactly one citation changed a rule; and the demo writing nothing is a static "
        "scan rather than a proof."
    ),
}

sheet = {"metadata": META, "beats": beats}

body = [b for b in beats if b["beat_id"] not in ("B00", "B09", "B10", "B11")]
words = {b["beat_id"]: len(b["narration_text"].split()) for b in beats}
lo = min(words[b["beat_id"]] for b in body)
hi = max(words[b["beat_id"]] for b in body)
assert 45 <= lo and hi <= 70, f"body beat word budget 45-70 violated: {lo}-{hi}"

if "--check" in sys.argv:
    print("[week11] all assertions pass")
    sys.exit(0)

out = HERE / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"[week11] wrote {out}  — {len(beats)} beats")
print("[week11] narration words: " + " ".join(f"{k}={v}" for k, v in words.items()))
print(f"[week11] body beats {lo}-{hi}w (band 45-70), total {sum(words.values())}w")
print(f"[week11] derived: {len(ABSENT)}/{len(DOCS)} absent · {num(NEW_LINES)} new + "
      f"{num(GROWN_LINES)} added lines · real zeroes {len(PUBLISHED_ZEROES)} of {len(PRIOR)} · "
      f"{CITES_PUBLISHED}/{CITES_ADDED} citations · {TABLES_TOTAL} tables/{len(LAYERS)} layers · "
      f"blocked {num(BLOCKED)} · runs {RUNS}")
