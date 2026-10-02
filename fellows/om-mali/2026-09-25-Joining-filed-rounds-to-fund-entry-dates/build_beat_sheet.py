#!/usr/bin/env python3
"""
build_beat_sheet.py — week 9, Joining Filed Rounds to Fund Entry Dates.

Writes beat_sheet.json with EVERY on-screen figure injected from figdata_week9.json.
No number is typed into a scene or a beat sheet by hand.

The assertions below cover the two defects the README records — each of which was wrong in
the drawing code until the PNG was read:
  1. `w9-entries` was titled as though every row predated the panel; four of seven were
     negative, because only the LATEST annual and semi-annual per registrant were fetched.
  2. `w9-exposure` truncated manager names into the next column, which the layout auditor
     cannot see because the two are separate text elements sharing a baseline.
(1) is handled here by DERIVING which companies genuinely reach back and asserting the
count; (2) is a layout matter and is handled in the scene file, where the manager column has
its own width and ellipsis.

THREE VALUES IN THIS REEL ARE NOT IN figdata_week9.json. They come from the narration script
and the underlying filings, are passed as named constants below, and every screen that uses
one says so:
  · XAI_COLLISION   — the 2014 filer whose name normalises to the same string as X.AI
  · LAYOUT_COUNT    — "four use tables, one uses none, a sixth needed no new code"
  · DBX_ROUND_USD   — the $400M Databricks reported selling in October 2019

Usage:  python build_beat_sheet.py            (writes beat_sheet.json)
        python build_beat_sheet.py --check    (assertions only, writes nothing)
"""
import json, sys
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIG = json.loads((HERE / "figdata_week9.json").read_text(encoding="utf-8"))

FORM_D = FIG["form_d"]
NCSR = FIG["ncsr"]
EXPOSURE = FIG["exposure"]
CORR = FIG["corroboration"]
BY_FILER = FIG["by_filer"]
ENTRY_VS_MARK = FIG["entry_vs_mark"]

D = Decimal

# NOT from figdata — see the module docstring.
XAI_COLLISION = {"year": "2014", "note": "normalises to the same string as X.AI, and is a "
                                         "completely different company"}
LAYOUT_COUNT = {"tables": 4, "no_table": 1, "free": 1}
DBX_ROUND_USD = 400_000_000

# ── assertions: the build fails rather than the video lying ───────────────────
assert FORM_D["quarters_scanned"] == 49 and FORM_D["rows"] == 706
assert sum(c["rows"] for c in FORM_D["by_class"]) == FORM_D["rows"], \
    "the vehicle classes must account for every scanned row"
POOLED = next(c for c in FORM_D["by_class"] if c["vehicle_class"] == "pooled_vehicle")
CANDIDATE = next(c for c in FORM_D["by_class"] if c["vehicle_class"] == "candidate_operating")
assert POOLED["rows"] == 595 and CANDIDATE["rows"] == 111
assert round(POOLED["rows"] / FORM_D["rows"], 4) == 0.8428, "≈84% are feeders, not the company"
assert POOLED["rows"] > CANDIDATE["rows"] * 5, \
    "the trap is that feeders DOMINATE a name scan — if they ever stop dominating, the " \
    "framing of B02 has to change with it"
assert FORM_D["archive_gap"], "the archive gap must be stated, not assumed away"

assert NCSR["filings"]["filings"] == 60 and NCSR["filings"]["with_lots"] == 31
assert len(BY_FILER) == 10, "ten filers carry lots in the data"
LOTS = sum(f["lots"] for f in BY_FILER)
POS_COST = sum(f["position_cost"] for f in BY_FILER)
FUND_COST = sum(f["fund_cost"] for f in BY_FILER)
assert LOTS == 249 and POS_COST == 227, "249 positions, 227 with a POSITION cost"
assert POS_COST + FUND_COST == LOTS, \
    "every lot carries one kind of cost or the other; 227 + 22 = 249"
ODD_FILER = [f for f in BY_FILER if f["fund_cost"] > 0 and f["position_cost"] == 0]
assert len(ODD_FILER) == 1, \
    "exactly one filer reports cost at fund level rather than per position — the beat says " \
    "'227 with a cost' and this is what the other 22 are"

# README defect 1: only the companies whose footnote GENUINELY reaches back may be shown.
REACH_BACK = [e for e in ENTRY_VS_MARK if e["first_entry"] < e["first_mark"]]
assert len(ENTRY_VS_MARK) == 7 and len(REACH_BACK) == 3, \
    "3 of 7 reach back; the figure used to title all seven as though they did"
EARLIEST = min(e["first_entry"] for e in ENTRY_VS_MARK)
assert EARLIEST == "2015-01-20", "the earliest acquisition date in the set"

assert CORR["dates_in_window"] == 18 and CORR["hits"]["0"] == 10
assert round(CORR["share"]["0"], 4) == 0.5556

# index of the first NON-zero gap in the sorted pair list — the near-miss the chart shows
# sitting on top of the zero stack. Derived, so it cannot drift away from the data.
NEAR_IDX = CORR["hits"]["0"]
assert sorted(p["gap_days"] for p in CORR["pairs"])[NEAR_IDX] == 1

assert len(CORR["pairs"]) == CORR["dates_in_window"], "one pair row per date in window"
assert sum(1 for p in CORR["pairs"] if p["gap_days"] == 0) == CORR["hits"]["0"], \
    "the pair rows and the summary must agree on how many land on the day"
DBX = next(p for p in CORR["pairs"]
           if p["company"].startswith("Databricks") and p["acquired"] == "2019-10-22")
assert DBX["gap_days"] == 0 and DBX["registrants"] == 5, "five managers, same day"

OUTSIDE = sum(c["dates_outside_window"] for c in CORR["by_company"])
assert OUTSIDE == 12, "12 acquisition dates fall outside any company's Form D window"
NAIVE_TOTAL = CORR["dates_in_window"] + OUTSIDE
assert round(CORR["hits"]["0"] / NAIVE_TOTAL, 4) == 0.3333, \
    "counting the out-of-window dates turns 56% into 33% — the denominator IS the finding"
assert CORR["caveat"], "the evidence-not-causation caveat must be present"

assert len(EXPOSURE) == 90
assert len({e["manager"] for e in EXPOSURE}) == 30 and len({e["company"] for e in EXPOSURE}) == 10

if "--check" in sys.argv:
    print("[week9] all assertions pass")
    sys.exit(0)

# ── derived, never typed ──────────────────────────────────────────────────────
pct1 = lambda v: f"{v * 100:.1f}%"
pct0 = lambda v: f"{round(v * 100)}%"
num = lambda v: f"{int(v):,}"
money_m = lambda v: f"${v / 1_000_000:,.0f}M"

FEEDER_SHARE = POOLED["rows"] / FORM_D["rows"]                     # 0.8428
NAIVE_SHARE = CORR["hits"]["0"] / NAIVE_TOTAL                      # 0.3333
YEARS_BACK = (D(REACH_BACK[0]["first_mark"][:4]) - D(EARLIEST[:4]))  # rough, refined below
SPX = next(e for e in ENTRY_VS_MARK if e["first_entry"] == EARLIEST)


def years_between(a, b):
    ay, am, ad = (int(x) for x in a.split("-"))
    by, bm, bd = (int(x) for x in b.split("-"))
    return ((by - ay) * 12 + (bm - am) + (bd - ad) / 30.0) / 12.0


SPX_GAP_YEARS = years_between(SPX["first_entry"], SPX["first_mark"])   # ~7.9

TOP_EXPOSURE = sorted(EXPOSURE, key=lambda e: -float(D(e["value_usd"])))[:8]
MAX_PCT = max(EXPOSURE, key=lambda e: float(D(e["max_pct_net_assets"])))

HANDLE = "@HumanitariansAI"
SEGMENT = "Joining Filed Rounds to Fund Entry Dates"
KICKER = "Irreducibly Human"     # GATE L rule 7 — the FIXED claude-hai series name
NOT_IN_FIGDATA = "not in figdata_week9.json — from narration_script.md and the filing itself"


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
    "Hi, I'm Om Mali. This video is about joining two different S E C filings together, so "
    "that a private company's funding round and the day a mutual fund actually bought into it "
    "can be lined up against each other. Until now this project worked from one form, which "
    "says what a position is worth but never when it was bought. This week I added two that do.",
    22,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": "Tere, HAI",
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "Bring in Form D for offering dates and the restricted-securities footnote for "
            "acquisition dates, and join them to the marks panel. Do not key the join on a "
            "company name — tell me what breaks if I do."
        ),
        "runningText": "scanning 49 quarters…",
        "folderLabel": HANDLE,
        "modelLabel": "Opus 5",
        "effortLabel": "High",
        "output": [
            f"a name scan returns {num(FORM_D['rows'])} rows — {pct0(FEEDER_SHARE)} of them "
            f"are feeder funds, not the company",
            f"footnote parser: {num(LOTS)} positions, {num(POS_COST)} with a position cost, "
            f"entry dates back to {EARLIEST}",
            f"and {CORR['hits']['0']} of {CORR['dates_in_window']} fund entry dates land on the "
            f"exact day an issuer reported a sale",
        ],
    }, "type-on", [
        {"at": "0.00", "event": "Cream Claude composer, empty. Serif greeting 'Tere, HAI' + terracotta spark above it."},
        {"at": "0.15", "event": "The ask types itself into the composer, character by character."},
        {"at": "0.60", "event": "Send button arms terracotta; running indicator reads 'scanning 49 quarters…'."},
        {"at": "0.75", "event": "Three output lines land in sequence — the ask arrives ANSWERED (COLD OPEN LAW)."},
    ]),
))

# ── B01 · EXECUTIVE SUMMARY ───────────────────────────────────────────────────
beats.append(beat(
    "B01", "EXECUTIVE SUMMARY", "REMOTION",
    "Two new filings, beside the panel. Form D, which a company files when it sells shares, "
    "gives offering dates and amounts. The restricted securities footnote in a fund's annual "
    "report gives acquisition dates and cost. Joining them is the week. And the join does not "
    "run on a company name. It runs on an identifier a person confirmed.",
    22,
    remotion("W9Bluf", "reel-local/JoiningFiledRounds", {
        "sparkLine": "The code proposes. A person decides.",
        "headline": "Two filings, one join.",
        "sources": [
            {"name": "Form D", "who": "filed by the COMPANY when it sells shares",
             "gives": "offering dates and amounts",
             "scale": f"{num(FORM_D['rows'])} rows across {FORM_D['quarters_scanned']} quarters"},
            {"name": "Reg S-X 12-12 footnote", "who": "filed by the FUND in its annual report",
             "gives": "acquisition dates and cost",
             "scale": f"{num(LOTS)} positions from {NCSR['filings']['with_lots']} filings"},
        ],
        "haveLabel": "what the panel already had",
        "have": "N-PORT — what a position is WORTH at a month end. Never when it was bought.",
        "keyLabel": "and the join key is not",
        "joinKey": "a name",
        "keyNote": "It is an EDGAR identifier a person has confirmed. Next: why a name cannot work.",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'two new filings'", "event": "The headline sets, then the two source cards land side by side."},
        {"at": "on 'offering dates and amounts'", "event": "Each card fills in who files it, what it gives, and how much of it there is."},
        {"at": "on 'does not run on a company name'", "event": "A 'a name' chip lands as the join key and is struck through."},
        {"at": "on 'an identifier a person confirmed'", "event": "The real key replaces it beneath."},
    ], intent="The BLUF names both sources by WHO files them, because that asymmetry is what makes B07's agreement evidence rather than arithmetic."),
))

# ── B02 · THE NAME TRAP ───────────────────────────────────────────────────────
beats.append(beat(
    "B02", "THE NAME TRAP", "REMOTION",
    "Here is why. The obvious way to find a company's Form D filings is to search for its "
    "name. I did that across forty-nine quarters and got seven hundred and six rows. Five "
    "hundred and ninety-five of them, about eighty-four percent, are not the company. They are "
    "feeder funds named after it, raising money to buy its shares on the secondary market.",
    24,
    remotion("W9NameTrap", "reel-local/JoiningFiledRounds", {
        "sparkLine": "Eighty-four percent are not the company.",
        "eyebrow": "WEEK 9 · THE NAME TRAP",
        "title": "What a name scan actually returns",
        "subtitle": f"{FORM_D['quarters_scanned']} quarters, {FORM_D['first_quarter']} → {FORM_D['last_quarter']}",
        "total": FORM_D["rows"],
        "totalLabel": "rows matched by name",
        "split": [
            {"label": "feeder vehicles — not the company", "value": POOLED["rows"],
             "ciks": POOLED["ciks"], "hot": True},
            {"label": "candidate operating companies", "value": CANDIDATE["rows"],
             "ciks": CANDIDATE["ciks"], "hot": False},
        ],
        "shareLabel": pct1(FEEDER_SHARE),
        "example": "Anthropic Jan 2026 a Series of CGF2021 LLC",
        "exampleNote": (
            "A fund raising money to buy Anthropic shares on the secondary market. The amount "
            "it sold is its own raise, not Anthropic's."
        ),
        "archiveNote": FORM_D["archive_gap"],
        "source": "SOURCE: figdata_week9.json — form_d.by_class, form_d.archive_gap",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'seven hundred and six rows'", "event": "One full-width bar draws and the total counts up to 706."},
        {"at": "on 'five hundred and ninety-five'", "event": "The bar splits — the feeder share takes the accent and dominates the frame."},
        {"at": "on 'feeder funds named after it'", "event": "A REAL feeder name lands beneath, with what it actually is."},
    ], intent="Rebuild of pantry/w9-nametrap.png. The feeder share has to LOOK like the majority, because the whole join design follows from it being one."),
))

# ── B03 · THE JOIN KEY ────────────────────────────────────────────────────────
beats.append(beat(
    "B03", "THE JOIN KEY", "REMOTION",
    "The amount a feeder sold is its own raise. Add those up, call it a funding round, and you "
    "have published numbers no company ever filed. So the join runs on an EDGAR identifier a "
    "person has confirmed. The code proposes, a human decides. That mattered. One filer from "
    "twenty fourteen normalises to exactly the same string as X dot A I, and is a completely "
    "different company.",
    25,
    remotion("W9JoinKey", "reel-local/JoiningFiledRounds", {
        "sparkLine": "Same string. Different company.",
        "eyebrow": "WEEK 9 · THE JOIN KEY",
        "title": "Why the key is an identifier, not a name",
        "wrongLabel": "join on the name",
        "wrongNote": "sums feeder raises into a round the company never filed",
        "rightLabel": "join on a confirmed EDGAR identifier",
        "rightNote": "the code proposes a match; a person accepts or rejects it",
        "collisionLabel": "and names collide",
        "collision": [
            {"side": "X.AI Corp", "detail": "the company this project tracks"},
            {"side": f"a filer from {XAI_COLLISION['year']}", "detail": XAI_COLLISION["note"]},
        ],
        "collisionNote": (
            "Both normalise to the same string. No amount of string cleaning separates them; "
            "only an identifier does."
        ),
        "falsePositiveNote": (
            "The scan's own output carries a row labelled FALSE POSITIVE — a company that "
            "matched by name and is not in the universe at all. It is left visible in the data "
            "rather than quietly dropped."
        ),
        "source": (
            f"SOURCE: figdata_week9.json — form_d.by_company. The {XAI_COLLISION['year']} "
            f"collision is {NOT_IN_FIGDATA}."
        ),
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'numbers no company ever filed'", "event": "The name-join path lands and is struck through."},
        {"at": "on 'an EDGAR identifier a person has confirmed'", "event": "The identifier path lands beneath it and takes the accent."},
        {"at": "on 'the same string as X.AI'", "event": "Two filer cards land showing the identical normalised string and two different companies."},
    ], intent="The collision is the argument's teeth: it shows that no better string normalisation would have helped, which is what justifies a human in the loop."),
))

# ── B04 · FIVE LAYOUTS ────────────────────────────────────────────────────────
beats.append(beat(
    "B04", "FIVE LAYOUTS", "REMOTION",
    "The second source has no bulk dataset and no required format. The regulation says what "
    "must be disclosed, not what the columns are called, so every fund family writes it "
    "differently. Four use tables with different headings. One uses no table at all. That got "
    "me two hundred and forty-nine positions, two hundred and twenty-seven with a cost.",
    23,
    remotion("W9Layouts", "reel-local/JoiningFiledRounds", {
        "sparkLine": "No bulk dataset. No required format.",
        "eyebrow": "WEEK 9 · FIVE LAYOUTS",
        "title": "The same footnote, written five ways",
        "subtitle": "the rule says what must be disclosed, not what the columns are called",
        "layouts": [
            {"kind": "tables, each with different headings", "count": str(LAYOUT_COUNT["tables"])},
            {"kind": "no table at all — date and cost inside a portfolio line", "count": str(LAYOUT_COUNT["no_table"])},
            # "+" so the row is not read as part of the five. It is a sixth family whose footnote
            # one of the four table parsers already handled.
            {"kind": "needed no new code", "count": f"+{LAYOUT_COUNT['free']}"},
        ],
        "filers": [
            {"filer": f["filer"], "lots": f["lots"], "positionCost": f["position_cost"],
             "fundCost": f["fund_cost"], "ranges": f["ranges"],
             "hot": f["fund_cost"] > 0 and f["position_cost"] == 0}
            for f in BY_FILER
        ],
        "totals": {"lots": LOTS, "positionCost": POS_COST, "fundCost": FUND_COST},
        "totalsLabel": f"{num(LOTS)} positions · {num(POS_COST)} with a position cost",
        "oddNote": (
            f"The other {FUND_COST} are {ODD_FILER[0]['filer'].title()}'s, which reports cost at "
            f"fund level rather than per position. Counted, not discarded. Two rows read "
            f"BlackRock: these groups are keyed on a case-sensitive name prefix, so the data "
            f"keeps them apart. Left exactly as filed."
        ),
        "source": (
            f"SOURCE: figdata_week9.json — by_filer[] (10 filers carry lots). The layout count "
            f"— {LAYOUT_COUNT['tables']} tables, {LAYOUT_COUNT['no_table']} without one, "
            f"{LAYOUT_COUNT['free']} free — is {NOT_IN_FIGDATA}."
        ),
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'no required format'", "event": "Three layout kinds land as a short list with their counts."},
        {"at": "on 'every fund family writes it differently'", "event": "The ten filers that carry lots land as rows with their counts."},
        {"at": "on 'two hundred and forty-nine positions'", "event": "The totals resolve; the fund-level-cost filer takes the accent."},
    ], intent="Rebuild of pantry/w9-layouts.png. The point is heterogeneity, so the filer rows are shown individually rather than summed into one number."),
))

# ── B05 · ENTRY DATES ─────────────────────────────────────────────────────────
beats.append(beat(
    "B05", "ENTRY DATES", "REMOTION",
    "Two things the marks panel could not say before. The first is when a fund actually "
    "bought. Entry dates reach back to January twenty fifteen, nearly eight years before the "
    "panel's first observation of that company. But only three of the seven companies "
    "genuinely reach back. For the rest I have only the latest reports, so this is a floor, "
    "not a history.",
    25,
    remotion("W9Entries", "reel-local/JoiningFiledRounds", {
        "sparkLine": "A floor, not a history.",
        "eyebrow": "WEEK 9 · ENTRY DATES",
        "title": "How far back the footnote reaches",
        "subtitle": "acquisition date against the panel's first mark for the same company",
        "rows": [
            {"company": e["company"].split(",")[0], "entry": e["first_entry"],
             "mark": e["first_mark"], "lots": e["lots"],
             "reachesBack": e["first_entry"] < e["first_mark"]}
            for e in sorted(ENTRY_VS_MARK, key=lambda e: e["first_entry"])
        ],
        "entryLabel": "first acquisition date",
        "markLabel": "panel's first mark",
        "earliest": EARLIEST,
        "earliestLabel": f"{SPX_GAP_YEARS:.1f} years before {SPX['company'].split(',')[0]}'s first mark",
        "reachBackCount": len(REACH_BACK),
        "totalCount": len(ENTRY_VS_MARK),
        "floorNote": (
            f"Only {len(REACH_BACK)} of {len(ENTRY_VS_MARK)} genuinely predate the panel. Only "
            f"the LATEST annual and semi-annual per registrant were fetched, so older purchases "
            f"disclosed in older reports are simply not in view. This is a floor on how far "
            f"back the record goes, not the record."
        ),
        "source": "SOURCE: figdata_week9.json — entry_vs_mark[]; which rows reach back is derived from the dates, and asserted",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'when a fund actually bought'", "event": "Seven company rows land on a shared time axis."},
        {"at": "on 'January twenty fifteen'", "event": "The earliest entry marks at the far left, with its distance to that company's first mark."},
        {"at": "on 'only three of the seven'", "event": "The three that reach back take the accent; the four that do not dim."},
        {"at": "on 'a floor, not a history'", "event": "The reason lands across the foot."},
    ], intent="Rebuild of pantry/w9-entries.png, corrected. The figure used to title all seven as reaching back when four do not — so the split is drawn, and the reason is on the frame."),
))

# ── B06 · EXPOSURE ────────────────────────────────────────────────────────────
beats.append(beat(
    "B06", "EXPOSURE", "REMOTION",
    "The second is an exposure map. Who holds what, and how much of their fund it is, using "
    "each filer's own percentage of net assets. Ninety manager and company pairs, across "
    "thirty managers and ten companies. This is concentration, not conviction. A large "
    "percentage is a fact about the fund's size as much as about the position.",
    24,
    remotion("W9Exposure", "reel-local/JoiningFiledRounds", {
        "sparkLine": "Concentration, not conviction.",
        "eyebrow": "WEEK 9 · EXPOSURE",
        "title": "Who holds what, and how much of their fund it is",
        "subtitle": f"{len(EXPOSURE)} manager–company pairs · {len({e['manager'] for e in EXPOSURE})} managers · {len({e['company'] for e in EXPOSURE})} companies",
        "rows": [
            {"manager": e["manager"], "company": e["company"].split(",")[0],
             "value": float(D(e["value_usd"])), "pct": float(D(e["max_pct_net_assets"])),
             "funds": e["funds"], "asOf": e["as_of"]}
            for e in TOP_EXPOSURE
        ],
        "valueLabel": "position value",
        "pctLabel": "max % of a fund's net assets",
        "shownNote": f"the {len(TOP_EXPOSURE)} largest by value, of {len(EXPOSURE)}",
        "maxPctRow": {
            "manager": MAX_PCT["manager"], "company": MAX_PCT["company"].split(",")[0],
            "pct": float(D(MAX_PCT["max_pct_net_assets"])),
        },
        "verdict": (
            "Concentration, not conviction. A large percentage is a fact about the fund's size "
            "as much as about the position."
        ),
        "source": "SOURCE: figdata_week9.json — exposure[], each filer's own reported percentage of net assets",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'who holds what'", "event": "Manager–company rows land, largest first, each with its own value."},
        {"at": "on 'each filer's own percentage'", "event": "A percentage-of-net-assets bar grows beside each row."},
        {"at": "on 'concentration, not conviction'", "event": "The caution lands across the foot."},
    ], intent="Rebuild of pantry/w9-exposure.png. The manager column has its own width and ellipsis — the source figure ran 'Robinhood Ventures Fund' into the next column, which the layout auditor cannot see."),
))

# ── B07 · THE AGREEMENT ───────────────────────────────────────────────────────
beats.append(beat(
    "B07", "THE AGREEMENT", "REMOTION",
    "Then the part I did not expect. With both sources joined, ten of eighteen fund "
    "acquisition dates fall on the exact day a company reported selling shares. The clearest "
    "case is Databricks, October twenty nineteen. Five separate fund managers independently "
    "name that same day. The company files because it sold. The funds file because they own. "
    "Neither cites the other.",
    25,
    remotion("W9Corroborate", "reel-local/JoiningFiledRounds", {
        "sparkLine": "Neither filing cites the other.",
        "eyebrow": "WEEK 9 · THE AGREEMENT",
        "title": f"{CORR['hits']['0']} of {CORR['dates_in_window']} land on the exact day",
        "subtitle": "distance from a fund's acquisition date to the nearest filed round",
        "pairs": [
            {"company": p["company"].split(",")[0], "acquired": p["acquired"],
             "gap": p["gap_days"], "registrants": p["registrants"]}
            for p in CORR["pairs"]
        ],
        "zeroCount": CORR["hits"]["0"],
        "total": CORR["dates_in_window"],
        "shareLabel": pct0(CORR["share"]["0"]),
        # The dot sitting on top of the zero stack is a 1-day gap. Naming it stops the frame
        # reading as an eleventh zero drawn in the wrong colour.
        "chartNote": (
            f"the dark dot above the stack is {sorted(p['gap_days'] for p in CORR['pairs'])[NEAR_IDX]}"
            f" day away, not zero"
        ),
        "caseLabel": "the clearest case",
        "case": {
            "company": DBX["company"].split(",")[0],
            "date": DBX["acquired"],
            "registrants": DBX["registrants"],
            "amount": money_m(DBX_ROUND_USD),
        },
        "caseNote": (
            f"The company filed saying it sold {money_m(DBX_ROUND_USD)} of stock. "
            f"{DBX['registrants']} separate fund managers independently name that same day."
        ),
        "whyLabel": "why this is evidence and not arithmetic",
        "why": [
            "The company files because it SOLD.",
            "The funds file because they OWN.",
            "Neither filing cites the other.",
        ],
        # figdata stores the caveat with an ASCII double hyphen. Typography only — the
        # wording is the recorded caveat, unchanged.
        "caveat": CORR["caveat"].replace(" -- ", " — "),
        "source": (
            f"SOURCE: figdata_week9.json — corroboration.pairs[], corroboration.caveat. The "
            f"{money_m(DBX_ROUND_USD)} offering amount is {NOT_IN_FIGDATA}."
        ),
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'ten of eighteen'", "event": "Eighteen dates land on a gap-days axis; the ten at zero stack at the origin."},
        {"at": "on 'Databricks, October twenty nineteen'", "event": "That row lifts out with its five registrants."},
        {"at": "on 'neither cites the other'", "event": "Three lines land explaining why the agreement is independent."},
    ], intent="Rebuild of pantry/w9-corroborate.png. The independence of the two filings is the claim, so it is spelled out rather than implied by the count."),
))

# ── B08 · THE DENOMINATOR ─────────────────────────────────────────────────────
beats.append(beat(
    "B08", "THE DENOMINATOR", "REMOTION",
    "One caution, and it is the whole number. That fifty-six percent counts only purchases "
    "made while a company was still filing. One company stopped in mid twenty twenty-two, and "
    "most of its later buys have no round to match. Count those and fifty-six percent reads as "
    "thirty-three. The denominator is doing the work.",
    22,
    remotion("W9Denominator", "reel-local/JoiningFiledRounds", {
        "sparkLine": "The denominator is doing the work.",
        "eyebrow": "WEEK 9 · THE DENOMINATOR",
        "title": "The same ten hits, two denominators",
        "readings": [
            {"label": "inside the filing window", "num": CORR["hits"]["0"],
             "den": CORR["dates_in_window"], "pct": pct0(CORR["share"]["0"]), "honest": True},
            {"label": "every acquisition date", "num": CORR["hits"]["0"],
             "den": NAIVE_TOTAL, "pct": pct0(NAIVE_SHARE), "honest": False},
        ],
        "outside": OUTSIDE,
        "outsideLabel": "dates with no round to match",
        "whyNote": (
            "One company stopped filing Form D in mid-2022. Its later purchases have no round "
            "to be near, so the distance to the nearest one measures the end of the archive, "
            "not the behaviour of a fund."
        ),
        "notShownLabel": "what none of this shows",
        "notShown": [
            "No valuation. Neither source carries shares outstanding, so nothing divides to a company value.",
            "No return. A footnote cost over a later mark is not one — the share count may have changed between them.",
            "Agreement is evidence, not causation. A same-day buy is equally consistent with a secondary purchase that settled that day.",
        ],
        "source": "SOURCE: figdata_week9.json — corroboration.share, corroboration.by_company.dates_outside_window",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'that fifty-six percent'", "event": "The honest reading sets at display size with its denominator beneath it."},
        {"at": "on 'count those'", "event": "The 12 out-of-window dates slide into the denominator and the percentage falls to 33."},
        {"at": "on 'the denominator is doing the work'", "event": "Both readings sit side by side, same numerator."},
        {"at": "on the close", "event": "Three limits land beneath a rule."},
    ], intent="The same numerator under two denominators, side by side — the reel ends by showing how easily its own headline could be restated."),
))

# ── B09 · VERDICT ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B09", "VERDICT", "BOOKEND",
    "Week nine on one page. Two new filings joined to the panel. A name scan returns seven "
    "hundred and six rows of which eighty-four percent are feeder funds, so the join runs on a "
    "confirmed identifier instead. Five layouts of the same footnote gave two hundred and "
    "forty-nine positions and entry dates back to twenty fifteen. Ten of eighteen entry dates "
    "land on the exact day a company reported a sale, and that is evidence rather than "
    "causation. Counted against every date instead, fifty-six percent reads as thirty-three.",
    32,
    remotion("ClaudeVerdictArtifact", "proven-core/ClaudeVerdictArtifact", {
        "sparkLine": "",
        "artifactTitle": f"{SEGMENT} — week 9",
        "artifactHeading": "What the join found",
        "artifactLines": [
            f"Two sources added beside N-PORT: Form D ({num(FORM_D['rows'])} rows over "
            f"{FORM_D['quarters_scanned']} quarters) for offering dates, and the Reg S-X 12-12 "
            f"footnote ({num(LOTS)} positions from {NCSR['filings']['with_lots']} filings) for "
            f"acquisition dates and cost.",
            f"A name scan is {pct0(FEEDER_SHARE)} wrong: {num(POOLED['rows'])} of "
            f"{num(FORM_D['rows'])} matches are feeder vehicles raising money to buy the "
            f"company's shares, not the company. The join runs on a confirmed EDGAR identifier "
            f"— and one 2014 filer normalises to the same string as X.AI.",
            f"Five layouts for one footnote, because the rule names what must be disclosed and "
            f"not what the columns are called. {num(POS_COST)} of {num(LOTS)} positions carry a "
            f"position cost; the other {FUND_COST} report cost at fund level.",
            f"Entry dates reach to {EARLIEST}, {SPX_GAP_YEARS:.1f} years before that company's "
            f"first mark — but only {len(REACH_BACK)} of {len(ENTRY_VS_MARK)} companies "
            f"genuinely predate the panel, so this is a floor and not a history.",
            f"{CORR['hits']['0']} of {CORR['dates_in_window']} acquisition dates fall on the "
            f"exact day an issuer reported a sale ({pct0(CORR['share']['0'])}) — evidence, not "
            f"causation, and neither filing cites the other. Against all {NAIVE_TOTAL} dates it "
            f"is {pct0(NAIVE_SHARE)}.",
        ],
    }, "stagger", [
        {"at": "0.05", "event": f"The Claude artifact page opens — {SEGMENT}, week 9."},
        {"at": "each line", "event": "Five findings stagger in, one per spoken clause."},
    ]),
    lead=0.4,
))

# ── B10 · HANDOFF ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B10", "HANDOFF", "BOOKEND",
    "Your turn. Paste this into Claude. Find a join in your own data that runs on a name or a "
    "label rather than an identifier. Then count how many of its matches are actually the "
    "thing you meant. Not a sample, a count. Mine was sixteen percent, and I only found out "
    "because I looked at what the other eighty-four were.",
    24,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": "Your turn.",
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "Find every join in my pipeline that keys on a name or a label rather than a stable "
            "identifier. For each one, count what share of the matches are actually the entity I "
            "meant — a count, not a sample — and show me the ones that are not. Then tell me "
            "which of them no amount of string normalisation would fix."
        ),
        "runningText": "paste this into Claude…",
        "folderLabel": HANDLE,
        "modelLabel": "Opus 5",
        "effortLabel": "High",
    }, "type-on", [
        {"at": "0.00", "event": "Composer returns, greeting reads 'Your turn.'"},
        {"at": "0.10", "event": "The suggested prompt types itself in as the narration reads it aloud, verbatim."},
        {"at": "0.70", "event": "Running text reads 'paste this into Claude…' while the narration discusses what to look for."},
    ]),
))

# ── B11 · OUTRO ───────────────────────────────────────────────────────────────
beats.append(beat(
    "B11", "OUTRO", "BOOKEND",
    "Joining filed rounds to fund entry dates. Week nine of the Private AI Valuation Agent. "
    "Om Mali, for Humanitarians A I.",
    11,
    remotion("ClaudeTitleOutro", "proven-core/ClaudeTitleOutro", {
        "title": SEGMENT,
        "handle": HANDLE,
        "subline": "week 9 · the Private AI Valuation Agent",
    }, "fade", [
        {"at": "0.00", "event": "Title restates poster-style in serif with the terracotta period; handle beneath."},
    ]),
))

sheet = {
    "metadata": {
        "title": SEGMENT,
        "slug": "joining-filed-rounds-to-fund-entry-dates",
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
        "greeting": "Tere, HAI",
        "greeting_note": "hello lexicon: Estonian (short form). HAI persona takes only the shortest cues (Hi · Ola · Hej · Ciao · Hallo · Salut · Ahoj · Szia · Tere). Rotated off weeks 1, 2, 4, 5, 6, 7 and 8 so the series never repeats a language.",
        "aspect_ratio": "16:9",
        "fit": "pad",
        "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
        "color_semantics": "Claude FIDELITY skin: cream #F2F0E9 stage, warm ink #3D3929, terracotta #D97757 as the ONE accent. The source figures use red as the primary series, never a warning colour; that reading is preserved — terracotta marks the subject of each beat, never a hazard.",
        "series": "Private AI Valuation Agent — week 9 (follows 2026-09-18-Measuring-how-private-marks-move-and-propagate)",
        "derived_from": "narration_script.md (human-authored, ~475 spoken words, target 3:00) plus README.md's figure-to-beat map. Every on-screen figure is a prop injected by build_beat_sheet.py from figdata_week9.json, under assertions. THREE values are not in figdata and are passed as named constants with on-screen attribution: the 2014 X.AI name collision, the five-layout count, and the $400M Databricks offering amount.",
        "note": "ai-explainer / claude-hai. ILLUSTRATE LAW: the Claude UI appears at B00 (cold open, answered), B09 (verdict artifact), B10 (handoff) and B11 (outro) only — every body beat illustrates its concept as a native animated Remotion scene (REBUILD LAW). The five source PNGs and their SVG sources are REFERENCE in pantry/, never slotted as media. The script's six sections are split into eight body beats; the split is logged in BUILD-LOG.md. THREE THINGS NOT TO GET WRONG: the 84% is the reason for the design and not a side note; the corroboration is evidence and not causation; and the denominator does the work.",
        "companion_vertical": "vertical/ — the same twelve beats, same audio, rendered 9:16 at 2160×3840 from portrait compositions (never a crop).",
        "tags": ["SEC", "Form D", "N-CSR", "restricted securities", "entity resolution",
                 "record linkage", "private markets", "data engineering", "Humanitarians AI", "Mycroft"],
    },
    "beats": beats,
}

out = HERE / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

words = {b["beat_id"]: len(b["narration_text"].split()) for b in beats}
print(f"[week9] wrote {out}  — {len(beats)} beats")
print("[week9] narration words:", " ".join(f"{k}={v}" for k, v in words.items()))
body = [v for k, v in words.items() if k in ("B01", "B02", "B03", "B04", "B05", "B06", "B07", "B08")]
print(f"[week9] body beats {min(body)}–{max(body)}w (band 45–70), total {sum(words.values())}w")
print(f"[week9] derived: feeders {pct1(FEEDER_SHARE)}  lots {LOTS}/{POS_COST}  "
      f"reach-back {len(REACH_BACK)}/{len(ENTRY_VS_MARK)}  earliest {EARLIEST} "
      f"({SPX_GAP_YEARS:.1f}y)  corroboration {pct0(CORR['share']['0'])} -> {pct0(NAIVE_SHARE)}")
