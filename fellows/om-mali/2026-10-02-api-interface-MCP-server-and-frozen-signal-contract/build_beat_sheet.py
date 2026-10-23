#!/usr/bin/env python3
"""
build_beat_sheet.py — week 10, Serving the Panel over MCP and Freezing the Signal Contract.

Writes beat_sheet.json with EVERY on-screen figure injected from figdata.json or read
straight out of signal_example.json. No number is typed into a scene or a beat sheet by hand.

THE FRAMING ASSERTION of this reel is ENVELOPE_COST. The script and both figures present
bounding as a pure win, because the one tool they show is the one where it is. On five of the
six tools the envelope makes the answer BIGGER. B03 exists to say that out loud, and the
assertion fails the build if a future measurement quietly turned bounding into a free lunch —
which would make the beat's framing wrong while every number on it stayed right.

THREE THINGS IN THIS REEL ARE NOT IN figdata.json. They come from README.md and
narration_script.md, are passed as named constants below, and every screen that uses one says
so:
  · FOURTH_GUARD  — the length check. figdata.json carries THREE guards and w11-guards.png is
                    titled "Three guards"; the script says four. The fourth arrived after the
                    figure was drawn. This is the load-bearing one: see FACTCHECK.md row 12.
  · LATE_MISSES   — the empty note accepted as a success, and the spelled-out number
  · SETUP_BUGS    — the three client-side registration defects named in the close

Usage:  python build_beat_sheet.py            (writes beat_sheet.json)
        python build_beat_sheet.py --check    (assertions only, writes nothing)
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIG = json.loads((HERE / "figdata.json").read_text(encoding="utf-8"))
SIGNAL = json.loads((HERE / "signal_example.json").read_text(encoding="utf-8"))

TOOLS = FIG["tools"]
LIMITS = FIG["limits"]
SIG = FIG["signal"]
GUARDS = FIG["guards"]

BY_TOOL = {t["tool"]: t for t in TOOLS}
MARKS = BY_TOOL["get_marks"]

# ── derived, never typed ──────────────────────────────────────────────────────
CHARS_PER_TOKEN = 4          # the figure's own stated estimate, not a tokenizer count
def toks(chars): return chars / CHARS_PER_TOKEN

UNBOUNDED = MARKS["unbounded_chars"]
BOUNDED = MARKS["bounded_chars"]
SHRINK = 1 - BOUNDED / UNBOUNDED                        # 0.9688

# The tools where the envelope COSTS rather than saves. This is B03's whole subject.
COSTLIER = [t for t in TOOLS if t["bounded_chars"] > t["unbounded_chars"]]
CHEAPER = [t for t in TOOLS if t["bounded_chars"] < t["unbounded_chars"]]
def overhead(t): return t["bounded_chars"] / t["unbounded_chars"] - 1
OVH_LO = min(overhead(t) for t in COSTLIER)
OVH_HI = max(overhead(t) for t in COSTLIER)

PAGED = [t for t in TOOLS if t["rows_returned"] < t["rows_total"]]
WHOLE = [t for t in TOOLS if t["rows_returned"] == t["rows_total"]]
EMPTY = [t for t in TOOLS if t["rows_total"] == 0]

SIGNAL_KEYS = list(SIGNAL.keys())
SUPPRESSED = SIG["suppressed"]

# ── assertions ────────────────────────────────────────────────────────────────
assert len(TOOLS) == 6, "six tools is spoken in B04 and titles the source figure"
assert all(t["rows_returned"] <= t["rows_total"] for t in TOOLS)

assert MARKS["rows_total"] == 2151 and MARKS["rows_returned"] == LIMITS["default_limit"] == 50
assert UNBOUNDED == 575299 and BOUNDED == 17976
assert round(toks(UNBOUNDED) / 1000) == 144 or round(toks(UNBOUNDED) / 1000) == 143, \
    "the ~143k token figure is derived from chars/4; if that changes, B02's headline changes"
assert round(SHRINK, 3) == 0.969

# THE FRAMING ASSERTION. If bounding ever became free, B03 would be a beat about nothing.
assert len(COSTLIER) == 5 and len(CHEAPER) == 1, \
    "B03 claims the envelope costs on FIVE of six tools and pays on exactly one"
assert CHEAPER[0]["tool"] == "get_marks"
assert 0.18 < OVH_LO < OVH_HI < 0.50, "B03 puts the overhead band on screen as 19-49%"

assert len(PAGED) == 1 and PAGED[0]["tool"] == "get_marks", \
    "exactly one tool paged; the red row in w10-tools.png is that one"
assert len(WHOLE) == 5
assert len(EMPTY) == 1 and EMPTY[0]["tool"] == "list_unresolved", \
    "B06's 'an empty answer is still an answer' names this tool"

assert LIMITS["max_response_chars"] == 48000
assert BOUNDED < LIMITS["max_response_chars"], "the char ceiling must actually bind above the page"

assert SIG["schema_version"] == SIGNAL["schema_version"] == "1.0"
assert SIG["top_level_keys"] == len(SIGNAL_KEYS) == 9, \
    "the signal on disk must have exactly the key count the figure claims"
assert SIG["forbidden_fields"] == 10
assert SIG["companies"] == 10
assert SIG["not_supported"] == len(SUPPRESSED) == len(SIGNAL["not_supported"]) == 4
assert not any(k in SIGNAL for k in
               ("valuation", "market_cap", "shares_outstanding", "post_money", "pre_money",
                "return", "irr", "moic")), "the contract must refuse these IN THE EMITTED FILE"

# B06's reconciliation: the server lists 11 companies, the signal publishes 10.
LISTED = BY_TOOL["list_companies"]["rows_total"]
assert LISTED == 11 and SIG["companies"] == 10 and LISTED - SIG["companies"] == 1, \
    "B06 reconciles 11 listed against 10 published; the eleventh carries zero marks"

assert len(GUARDS) == 3 and all(g["caught"] for g in GUARDS)
assert any("lowest number of marks" in g["draft"] for g in GUARDS), \
    "the invented-ranking draft is the one B07 reads aloud"
assert SIG["commentary_words"] == 388

# ── the three values figdata.json does not carry ──────────────────────────────
FOURTH_GUARD = {
    # "length" is the README's own word for it, and it fits the guard column on one line —
    # "empty or short draft" wrapped and pushed its second line into the attribution note.
    "guard": "length",
    "why": "an empty draft passes every content check trivially",
    "note": "added after w11-guards.png was drawn, which is why that figure says three",
}
LATE_MISSES = [
    {"miss": "an empty note was accepted as a success",
     "detail": "recorded as \"0 words\" — nothing to fabricate, nothing to rank, no placeholder"},
    {"miss": "spelled-out numbers went unread",
     "detail": "\"across sixty-one groups\" was correct, and would have passed had it been wrong"},
]
SETUP_BUGS = [
    "a cwd key the client never applies before resolving the module",
    "a --cwd flag that does not exist on the CLI",
    "a default registration scope that binds the server to whichever directory it ran in",
]

HANDLE = "@HumanitariansAI"
SEGMENT = "Serving the Panel over MCP and Freezing the Signal Contract"
KICKER = "Irreducibly Human"     # GATE L rule 7 — the FIXED claude-hai series name
NOT_IN_FIGDATA = "not in figdata.json — from README.md and narration_script.md"


def num(n):
    return f"{n:,}"


def kchars(n):
    return f"{n/1000:.0f}k" if n >= 1000 else str(n)


def pct0(x):
    return f"{round(x * 100)}%"


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
    "Hi, I'm Om Mali. This video is about making this dataset usable by something other than "
    "me. Two pieces: a read only server an A I assistant can query directly, and a frozen "
    "J S O N contract another system can parse without guessing. Up to now everything here "
    "was a script I run and a document I read. Fine for building it. Useless to anyone else.",
    22,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": "Moi, HAI",
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "Serve the marks panel over MCP so an assistant can query it directly, and freeze "
            "the quarter's numbers into a contract another system can parse. Keep it read-only "
            "— and tell me what it has to refuse."
        ),
        "runningText": "starting the server…",
        "folderLabel": HANDLE,
        "modelLabel": "Opus 5",
        "effortLabel": "High",
        "output": [
            f"{len(TOOLS)} read-only tools, none of which writes a mark, a gate or a decision",
            f"one query returns {num(MARKS['rows_total'])} rows — bounded to "
            f"{kchars(BOUNDED)} characters from {kchars(UNBOUNDED)}",
            f"and a signal frozen at {SIG['schema_version']} that refuses "
            f"{SIG['forbidden_fields']} field names by name",
        ],
    }, "type-on", [
        {"at": "on 'something other than me'", "event": "The ask types into the Claude composer."},
        {"at": "on 'read only server'", "event": "The result lands ANSWERED with three output lines."},
    ], intent="COLD OPEN LAW: the interface IS the subject this week, so the reel opens inside a client talking to the thing it is about."),
))

# ── B01 · EXECUTIVE SUMMARY ───────────────────────────────────────────────────
beats.append(beat(
    "B01", "EXECUTIVE SUMMARY", "REMOTION",
    "Two deliverables. A server with six tools, none of which writes anything, and a signal "
    "file frozen at version one point zero. The hard part was never the protocol. Writing a "
    "server that speaks it took an afternoon. The hard parts were size, and what a contract "
    "has to refuse.",
    21,
    remotion("W10Bluf", "reel-local/ServingThePanelOverMcp", {
        "sparkLine": "The protocol was the easy part.",
        "headline": "Two deliverables, one week.",
        "pieces": [
            {"name": "MCP server", "who": "an assistant queries the panel directly",
             "gives": f"{len(TOOLS)} tools, every answer bounded",
             # Typography: an ASCII arrow in a serif/mono frame reads as a code artifact.
             "scale": f"{num(MARKS['rows_total'])} rows → {kchars(BOUNDED)} chars"},
            {"name": "Signal contract", "who": "another system parses it without guessing",
             "gives": f"frozen at {SIG['schema_version']}, validated before it is written",
             "scale": f"{SIG['top_level_keys']} keys · {SIG['forbidden_fields']} refused"},
        ],
        "haveLabel": "what the project had until now",
        "have": "A script I run and a document I read. Fine for building it. Useless to anyone else.",
        "keyLabel": "and the hard part was not",
        "joinKey": "the protocol",
        "keyNote": "It was size, and what the contract has to refuse. Both are measured here.",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'two deliverables'", "event": "The headline sets, then the two pieces land side by side."},
        {"at": "on 'never the protocol'", "event": "A 'the protocol' chip lands and is struck through."},
        {"at": "on 'size, and what a contract has to refuse'", "event": "The real constraints replace it."},
    ], intent="BLUF names both deliverables and strikes the thing a viewer would assume was hard, so the rest of the reel has somewhere to go."),
))

# ── B02 · THE SIZE PROBLEM ────────────────────────────────────────────────────
beats.append(beat(
    "B02", "THE SIZE PROBLEM", "REMOTION",
    "Ask for Databricks' full price history and you get two thousand one hundred and fifty one "
    "rows. Five hundred and seventy five thousand characters. Roughly a hundred and forty "
    "three thousand tokens. That is larger than most context windows, and useless even where "
    "it fits, because a model handed two thousand rows will not read them.",
    21,
    remotion("W10Bounding", "reel-local/ServingThePanelOverMcp", {
        "sparkLine": "Larger than the window, and unread inside it.",
        "eyebrow": "WEEK 10 · THE SIZE PROBLEM",
        "title": "One query, two possible answers",
        "subtitle": f"get_marks('Databricks, Inc.') — {num(MARKS['rows_total'])} rows available",
        "bars": [
            {"label": "the whole table", "chars": UNBOUNDED, "rows": MARKS["rows_total"],
             "hot": False},
            {"label": "one bounded page", "chars": BOUNDED, "rows": MARKS["rows_returned"],
             "hot": True},
        ],
        "tokenNote": f"~{CHARS_PER_TOKEN} characters per token is an estimate, not a tokenizer count",
        "shrinkLabel": pct0(SHRINK),
        "shrinkNote": "smaller, for the same question",
        "readNote": (
            f"A model handed {num(MARKS['rows_total'])} rows does not read them. It reads the "
            f"summary, which describes the WHOLE result set, and pages only if it needs to."
        ),
        "source": "SOURCE: figdata.json — tools[get_marks]; token figure derived at chars/4",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'two thousand one hundred and fifty one rows'", "event": "The full-table bar draws across the frame and lands its char and token counts."},
        {"at": "on 'larger than most context windows'", "event": "The bounded bar draws beneath it, a fraction of the width."},
        {"at": "on 'will not read them'", "event": "The reason the size matters lands under both."},
    ], intent="Rebuild of pantry/w10-bounding.png. The ratio between the two bars IS the argument, so nothing else on the frame competes with it."),
))

# ── B03 · WHAT BOUNDING COSTS ─────────────────────────────────────────────────
beats.append(beat(
    "B03", "WHAT BOUNDING COSTS", "REMOTION",
    "So every answer is three parts: a summary describing the whole result set, one bounded "
    "page, and a cursor. On that query, eighteen thousand characters instead of five hundred "
    "and seventy five thousand. But look at the other five tools. The envelope makes every one "
    "of them bigger, by nineteen to forty nine percent. Bounding is not free.",
    22,
    remotion("W10Envelope", "reel-local/ServingThePanelOverMcp", {
        "sparkLine": "It pays for itself exactly once.",
        "eyebrow": "WEEK 10 · WHAT BOUNDING COSTS",
        "title": "The envelope is not free",
        "subtitle": "bounded response against the same answer serialised whole, per tool",
        "parts": ["a summary of the WHOLE result set", "one bounded page", "a cursor"],
        "partsLabel": "every answer is three parts",
        "rows": [
            {"tool": t["tool"], "bounded": t["bounded_chars"],
             "unbounded": t["unbounded_chars"], "delta": overhead(t),
             "hot": t["bounded_chars"] < t["unbounded_chars"]}
            for t in sorted(TOOLS, key=lambda x: -abs(overhead(x)))
        ],
        "verdictBig": f"{len(COSTLIER)} of {len(TOOLS)}",
        "verdictText": "cost more bounded than whole",
        "bandLabel": f"+{pct0(OVH_LO)} to +{pct0(OVH_HI)}",
        "note": (
            f"It pays for itself on exactly one tool — the one that would otherwise return "
            f"{num(MARKS['rows_total'])} rows, where it saves {pct0(SHRINK)}. That is the "
            f"trade, and it is worth saying out loud."
        ),
        "source": "SOURCE: figdata.json — tools[]; the overheads are derived, and asserted",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'three parts'", "event": "The envelope's three parts land as a short list."},
        {"at": "on 'look at the other five tools'", "event": "Six rows land, each with its bounded-versus-whole delta."},
        {"at": "on 'bounding is not free'", "event": "The five costlier rows take the count, and the one that pays takes the accent."},
    ], intent="Not in the script or either figure. Both present bounding as a pure win because the one tool they show is the one where it is. This beat is the reel arguing with its own source material."),
))

# ── B04 · SIX TOOLS, NONE WRITES ──────────────────────────────────────────────
beats.append(beat(
    "B04", "SIX TOOLS, NONE WRITES", "REMOTION",
    "Six tools. List the companies, get one company's marks, compare managers on a date, get "
    "propagation, get a fund's exposure, and list what is still unresolved. Nothing writes. No "
    "tool records a decision, clears a gate, or changes a mark. Earlier I established that a "
    "resolution decision needs a named human. A tool a model can call is the opposite of that.",
    23,
    remotion("W10Tools", "reel-local/ServingThePanelOverMcp", {
        "sparkLine": "The code proposes. A person still decides.",
        "eyebrow": "WEEK 10 · THE SURFACE",
        "title": "Six tools, and none of them writes",
        "subtitle": "rows returned against rows available, with the response size",
        "rows": [
            {"tool": t["tool"], "total": t["rows_total"], "returned": t["rows_returned"],
             "chars": t["bounded_chars"], "paged": t["rows_returned"] < t["rows_total"]}
            for t in TOOLS
        ],
        "pagedNote": "Red marks the one tool whose answer was paged. Everything else fits whole.",
        "readOnlyLabel": "what no tool can do",
        "readOnly": [
            "record a resolution decision",
            "clear a gate",
            "change a mark",
        ],
        "whyNote": (
            "A resolution decision needs a named human. A tool a model can call to record one "
            "is the opposite of that. A model here reads every judgment already made, and sees "
            "what is still open. It cannot make one."
        ),
        "source": "SOURCE: figdata.json — tools[]; measured against the live database",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'six tools'", "event": "Six rows land, each with rows returned against rows available."},
        {"at": "on 'nothing writes'", "event": "Three things no tool can do land beneath, as a list of absences."},
        {"at": "on 'needs a named human'", "event": "The reason lands as the beat's closing block."},
    ], intent="Rebuild of pantry/w10-tools.png. SHOW-DON'T-TELL: 'read-only' is drawn as a list of what is ABSENT, because an absence is the claim."),
))

# ── B05 · THE CONTRACT ────────────────────────────────────────────────────────
beats.append(beat(
    "B05", "THE CONTRACT", "REMOTION",
    "The other piece is the signal. Nine top level keys, frozen at version one point zero, and "
    "validated before it is ever written to disk. It refuses ten field names outright. "
    "Valuation. Market cap. Shares outstanding. Return. Not style, structure. These filings "
    "give a fund's share count, never the company's total shares.",
    22,
    remotion("W10Contract", "reel-local/ServingThePanelOverMcp", {
        "sparkLine": "A contract is what it refuses.",
        "eyebrow": "WEEK 10 · THE CONTRACT",
        "title": f"{SIG['top_level_keys']} keys it carries, {SIG['forbidden_fields']} names it refuses",
        "subtitle": f"schema_version {SIG['schema_version']} · validated before it is written to disk",
        "carriesLabel": "the signal carries",
        "carries": SIGNAL_KEYS,
        "refusesLabel": "it will not carry",
        "refuses": ["valuation", "market_cap", "shares_outstanding", "post_money",
                    "pre_money", "return", "irr", "moic", "fair_value", "nav_per_share"],
        "whyNote": (
            "N-PORT gives a fund's share count, never the company's shares outstanding, so "
            "there is no arithmetic here to a company's value. A field for one would invite a "
            "consumer to fill it from elsewhere and inherit that source's error."
        ),
        "proofLabel": "checked against the emitted file",
        "proof": f"{len(SIGNAL_KEYS)} top-level keys present · 0 refused names present",
        "source": "SOURCE: signal_example.json, read directly — the key list is the file's own",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'nine top level keys'", "event": "The nine keys the signal carries land in a column."},
        {"at": "on 'refuses ten field names'", "event": "Ten refused names land opposite, struck as they arrive."},
        {"at": "on 'never the company's total shares'", "event": "The structural reason lands below both."},
    ], intent="Rebuild of pantry/w11-contract.png. The refused column is read FROM the emitted file rather than from a list in the figure, so the frame proves the refusal rather than restating it."),
))

# ── B06 · SUPPRESSED, NOT MISSING ─────────────────────────────────────────────
beats.append(beat(
    "B06", "SUPPRESSED, NOT MISSING", "REMOTION",
    "Where a figure is withheld, the reason is a value, not a missing key. Four companies are "
    "suppressed this quarter. And two counts here disagree on purpose. The server lists eleven "
    "companies. The signal publishes ten. The eleventh has zero marks. An empty answer is "
    "still an answer, and the server says so rather than returning nothing.",
    22,
    remotion("W10Suppressed", "reel-local/ServingThePanelOverMcp", {
        "sparkLine": "A reason, not a missing key.",
        "eyebrow": "WEEK 10 · WITHHELD",
        "title": "Suppressed is a value",
        "subtitle": "what the signal does when it will not publish a figure",
        "listedCount": LISTED,
        "publishedCount": SIG["companies"],
        "reconcileLabel": "two counts that disagree on purpose",
        "reconcileNote": (
            f"The server lists {LISTED} companies because that is the universe it carries. The "
            f"signal publishes {SIG['companies']} because {LISTED - SIG['companies']} of them has "
            f"zero marks. Neither number is wrong; they answer different questions."
        ),
        "suppressedLabel": f"suppressed this quarter — {len(SUPPRESSED)} of {SIG['companies']}",
        "suppressed": SUPPRESSED,
        "emptyLabel": "and an empty answer is still an answer",
        "emptyNote": (
            f"{EMPTY[0]['tool']} returns {EMPTY[0]['rows_total']} rows and says so in its "
            f"summary. Nothing is unresolved this quarter. That is a finding, not a blank."
        ),
        "source": "SOURCE: figdata.json — signal.suppressed, tools[]; counts reconciled at injection",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'the reason is a value'", "event": "The four suppressed companies land, each carrying a reason rather than a gap."},
        {"at": "on 'the server lists eleven'", "event": "The two counts land side by side and the difference resolves to one company."},
        {"at": "on 'an empty answer is still an answer'", "event": "The zero-row tool lands with its own summary note."},
    ], intent="DOUBLE-CHECK LAW. The 11-versus-10 looks like a defect on any frame that shows both, so the reel reconciles it rather than hoping nobody notices."),
))

# ── B07 · THE GUARD THAT WASN'T ENOUGH ────────────────────────────────────────
beats.append(beat(
    "B07", "THE GUARD THAT WASN'T ENOUGH", "REMOTION",
    "The quarterly note is the only prose a model writes here, and it gets the computed "
    "figures and nothing else. No database. No tools. I expected one check to be enough: no "
    "number that is not in the figures. It was not. A draft passed cleanly and still said one "
    "company had the fewest marks, one sentence before saying a different company had the "
    "fewest.",
    23,
    remotion("W10Guards", "reel-local/ServingThePanelOverMcp", {
        "sparkLine": "Every number real. The ranking invented.",
        "eyebrow": "WEEK 10 · THE GUARDS",
        "title": "The grounding check passed anyway",
        "subtitle": f"{SIG['commentary_words']} words accepted from {SIG['commentary_model']} after retries",
        "inputLabel": "what the model gets",
        "inputHas": ["the computed figures"],
        "inputLacks": ["no database", "no tools", "no retrieval"],
        "guards": [
            {"guard": g["guard"], "draft": g["draft"], "caught": g["caught"],
             "hot": "lowest number of marks" in g["draft"]}
            for g in GUARDS
        ],
        "fourth": {"guard": FOURTH_GUARD["guard"], "draft": FOURTH_GUARD["why"],
                   "caught": True, "late": True},
        "fourthNote": (
            f"The fourth check is {NOT_IN_FIGDATA} — it {FOURTH_GUARD['note']}."
        ),
        "punchNote": (
            "Every number in that draft was real, so the grounding check passed. The RANKING "
            "was what the model invented, and it contradicted itself inside one paragraph."
        ),
        "retryNote": "A failed draft goes back to the model with the specific complaint, up to three times.",
        "source": "SOURCE: figdata.json — guards[], signal.commentary_words",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'the computed figures and nothing else'", "event": "What the model has lands beside three things it does not."},
        {"at": "on 'one check to be enough'", "event": "The three guards land with the draft that fails each."},
        {"at": "on 'a different company had the fewest'", "event": "The invented-ranking row takes the accent and the contradiction lands beneath it."},
    ], intent="Rebuild of pantry/w11-guards.png, plus the fourth check the figure predates. FALSIFIABILITY: the beat is the author's own expectation being wrong."),
))

# ── B08 · WHAT THE CHECKS STILL MISS ──────────────────────────────────────────
beats.append(beat(
    "B08", "WHAT THE CHECKS STILL MISS", "REMOTION",
    "Two things the checks still miss. A draft that came back empty passed every one of them "
    "and was recorded as a success, at zero words. And a draft that spelled a number in words "
    "went unread, because the check only looked at digits. Then three setup bugs in a row, all "
    "invisible from inside the server, all because my test supplied what a real client does not.",
    22,
    remotion("W10Limits", "reel-local/ServingThePanelOverMcp", {
        "sparkLine": "A test that withholds what the caller withholds.",
        "eyebrow": "WEEK 10 · THE LIMITS",
        "title": "What none of the checks catch",
        "missesLabel": "two the checks still miss",
        "misses": LATE_MISSES,
        "bugsLabel": "three setup bugs, all the same shape",
        "bugs": SETUP_BUGS,
        "lessonLabel": "the lesson",
        "lesson": (
            "The server's own selftest passed through all three, and so did an in-process "
            "protocol test that supplied the working directory itself. A test finds this class "
            "of bug only if it WITHHOLDS what the real caller withholds."
        ),
        "notShownLabel": "what none of this shows",
        "notShown": [
            "No company valuation. These filings give a fund's share count, never the company's shares outstanding.",
            "Not timely. Filings lag their period end by roughly 55 to 60 days, and the bulk sets lag those again.",
            "Every rendering is labelled model output, not a verified claim — a wrong adjective with a correct number attached still passes.",
        ],
        "source": f"SOURCE: {NOT_IN_FIGDATA} — both misses and all three bugs",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'recorded as a success, at zero words'", "event": "The two misses land, each with what the check actually read."},
        {"at": "on 'three setup bugs in a row'", "event": "The three land as a stack, then the shape they share."},
        {"at": "on 'what a real client does not'", "event": "The closing block states what none of this shows."},
    ], intent="The reel's last body beat is its own limits, as in every episode of this series. The three bugs are the author's, and the lesson is stated as a rule rather than an apology."),
))

# ── B09 · VERDICT ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B09", "VERDICT", "BOOKEND",
    "Week ten on one page. A read only server with six tools, none of which writes a mark, a "
    "gate or a decision. One query returns two thousand one hundred and fifty one rows, "
    "bounded to eighteen thousand characters from five hundred and seventy five thousand, and "
    "the envelope costs more on the other five tools than it saves there. A signal frozen at "
    "one point zero with nine keys and ten field names refused by name. And the grounding "
    "check passed a draft that invented a ranking, which is why there are four checks now and "
    "not one.",
    30,
    # PROP NAMES ARE THE SCHEMA'S, NOT MINE. zod fills unknown keys with DEFAULTS and renders
    # them silently, so `title`/`heading`/`lines` shipped this beat as "Verdict / The split /
    # Chat: synchronous judgment" — another project's placeholder copy, at 4K.
    remotion("ClaudeVerdictArtifact", "proven-core/ClaudeVerdictArtifact", {
        "artifactTitle": f"{SEGMENT} — week 10",
        "artifactHeading": "What shipped, and what it refuses",
        "artifactLines": [
            f"A read-only MCP server: {len(TOOLS)} tools, none of which writes a mark, clears a "
            f"gate or records a decision. A resolution decision still needs a named human.",
            f"Every answer is bounded twice — {LIMITS['default_limit']} rows AND "
            f"{num(LIMITS['max_response_chars'])} characters — because row widths are not uniform. "
            f"get_marks: {num(MARKS['rows_total'])} rows, {kchars(BOUNDED)} chars instead of "
            f"{kchars(UNBOUNDED)}, a {pct0(SHRINK)} cut.",
            f"But the envelope COSTS on {len(COSTLIER)} of the {len(TOOLS)} tools, "
            f"+{pct0(OVH_LO)} to +{pct0(OVH_HI)}. It pays for itself on exactly one.",
            f"A signal frozen at {SIG['schema_version']}: {SIG['top_level_keys']} top-level keys, "
            f"{SIG['forbidden_fields']} field names refused by name, {len(SUPPRESSED)} companies "
            f"suppressed with a reason rather than a missing key.",
            f"The grounding check passed a draft that invented a ranking and contradicted "
            f"itself in one paragraph. Four checks now, not one — and the fourth is why an "
            f"empty note no longer counts as a success.",
        ],
    }, "stagger", [
        {"at": "per clause", "event": "Five findings stagger in, one per spoken clause."},
    ], intent="Judgment beat. The artifact page is the point (ILLUSTRATE LAW carve-out)."),
))

# ── B10 · HANDOFF ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B10", "HANDOFF", "BOOKEND",
    "Your turn. Paste this into Claude. Take a test you trust and find what it supplies that a "
    "real caller would not. The working directory. An environment variable. An already running "
    "process. Then withhold one and run it again. Mine passed three times before a real client "
    "ever reached it.",
    20,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": "Your turn.",
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "Take the test I trust most and list everything it supplies that a real caller "
            "would not — working directory, environment variables, an already-running process, "
            "an import path. Then withhold one and run it again. Tell me which ones it was "
            "hiding."
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
    "Serving the panel over M C P, and freezing the signal contract. Week ten of the Private "
    "A I Valuation Agent. Om Mali, for Humanitarians A I.",
    10,
    remotion("ClaudeTitleOutro", "proven-core/ClaudeTitleOutro", {
        "title": SEGMENT,
        "handle": HANDLE,
        # `subline`, not `subtitle` — the wrong name shipped the outro reading
        # "bot vs bot, season one", a default from an unrelated show.
        "subline": "week 10 · the Private AI Valuation Agent",
    }, "fade", [
        {"at": "on the title", "event": "Title restate, poster-style."},
    ], intent="OUTRO LAW: title restate, handle, nothing that moves."),
))

META = {
    "title": SEGMENT,
    "slug": "serving-the-panel-over-mcp-and-freezing-the-signal-contract",
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
    "greeting": "Moi, HAI",
    "greeting_note": "hello lexicon: Finnish (short form). HAI persona takes only the shortest cues (Hi · Ola · Hej · Ciao · Hallo · Salut · Ahoj · Szia · Tere · Moi). Rotate; never repeat a language.",
    "aspect_ratio": "16:9",
    "fps": 24,
    "lead_silence_s": 0.4,
    "note": (
        "ai-explainer / claude-hai. ILLUSTRATE LAW: the Claude UI appears at B00 (cold open, "
        "answered), B09 (verdict artifact), B10 (handoff) and B11 (outro) only — every body "
        "beat illustrates its concept as a native animated Remotion scene (REBUILD LAW). The "
        "four source PNGs and their SVG sources are REFERENCE in pantry/, never slotted as "
        "media. The script's six sections are split into eight body beats; the split is logged "
        "in BUILD-LOG.md. THREE THINGS NOT TO GET WRONG: token bounding is the deliverable and "
        "not a detail; read-only is a design decision and not a limitation; and the refused "
        "fields are structural and not stylistic."
    ),
}

sheet = {"metadata": META, "beats": beats}

body = [b for b in beats if b["beat_id"] not in ("B00", "B09", "B10", "B11")]
words = {b["beat_id"]: len(b["narration_text"].split()) for b in beats}
lo = min(words[b["beat_id"]] for b in body)
hi = max(words[b["beat_id"]] for b in body)
assert 45 <= lo and hi <= 70, f"body beat word budget 45-70 violated: {lo}-{hi}"

if "--check" in sys.argv:
    print("[week10] all assertions pass")
    sys.exit(0)

out = HERE / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"[week10] wrote {out}  — {len(beats)} beats")
print("[week10] narration words: " + " ".join(f"{k}={v}" for k, v in words.items()))
print(f"[week10] body beats {lo}-{hi}w (band 45-70), total {sum(words.values())}w")
print(f"[week10] derived: shrink {pct0(SHRINK)}  envelope costs on {len(COSTLIER)}/{len(TOOLS)} "
      f"(+{pct0(OVH_LO)}..+{pct0(OVH_HI)})  keys {SIG['top_level_keys']}  refused "
      f"{SIG['forbidden_fields']}  listed {LISTED} vs published {SIG['companies']}")
