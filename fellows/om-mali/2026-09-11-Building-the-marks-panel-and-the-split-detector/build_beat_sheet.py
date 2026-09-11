#!/usr/bin/env python3
"""
build_beat_sheet.py — week 7, Building the Marks Panel and the Split Detector.

Writes beat_sheet.json with EVERY on-screen figure injected from figdata_week7.json.
No number is typed into a scene or a beat sheet by hand.

The assertions below cover the four corrections the README records — each of which was
wrong until the figure was built:
  1. the evidence figure quoted a different fund than the write-up (smallest, not largest);
  2. a value was rounded in a way that flattered "the same dollars";
  3. red was used as a warning colour, which DESIGN.md forbids;
  4. a check failed because a human answered it, and a title hardcoded "0 fail".
(3) is a palette rule and is handled in the scene file; (1), (2) and (4) are asserted here.

ONE NUMBER IN THIS REEL IS NOT IN figdata_week7.json: the OLD detector window, ±0.02.
figdata carries only the NEW tolerance (0.01). The old value comes from the narration
script and plan.md, is passed as OLD_WINDOW below, and every screen that uses it says so.

Usage:  python build_beat_sheet.py            (writes beat_sheet.json)
        python build_beat_sheet.py --check    (assertions only, writes nothing)
"""
import json, sys
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIG = json.loads((HERE / "figdata_week7.json").read_text(encoding="utf-8"))

COV = FIG["coverage"]
TOT = FIG["totals"]
BLOCKS = FIG["blocks"]
QUAR = FIG["quarantine"]
PERP = FIG["perplexity"]
ANTH = FIG["anthropic"]
SPX = FIG["spacex"]
CHECKS = FIG["checks"]
AGREE = FIG["agreement"]
NEW_TOL = FIG["tolerance"]          # 0.01 — relative, the rule that ships now

# NOT from figdata. The previous absolute window, per narration_script.md / plan.md.
OLD_WINDOW = Decimal("0.02")

D = Decimal

# ── assertions: the build fails rather than the video lying ───────────────────
assert COV["holdings"] == 5806, "5,806 filed holdings go in"
assert COV["holdings"] - COV["rejected_not_in_universe"] - COV["superseded_by_amendment"] \
    == COV["lines_in_marks"] == 5706, "the deductions must reconcile to the priced lines"
assert COV["reconciles"] is True, "figdata itself must claim reconciliation"

assert TOT["marks"] == 5479, "5,479 marks"
assert sum(b["marks"] for b in BLOCKS) == TOT["blocked"] == 301, "the block reasons must sum"
SPLIT_BLOCK = [b for b in BLOCKS if "split" in b["reason"]]
assert len(SPLIT_BLOCK) == 1 and SPLIT_BLOCK[0]["marks"] == 7, \
    "exactly one block reason is the confirmed split, and it holds 7 marks"
assert TOT["priced"] + sum(b["marks"] for b in BLOCKS if "split" not in b["reason"]) \
    == TOT["marks"], \
    "priced + unpriceable == marks; the 7 split marks ARE priced but held out of change series"
assert sum(r["blocked"] for r in QUAR) == 7, "and those 7 are the quarantined split marks"

assert NEW_TOL == 0.01, "the rule that ships is a RELATIVE 1% window"

assert len(QUAR) == 7 and all(r["adjudicated"] for r in QUAR), \
    "every quarantined series has been adjudicated by a person"
assert all("Om Mali" in r["note"] for r in QUAR), \
    "and every adjudication carries the reviewer's name in its written reason"
QUAR_COMPANIES = sorted({r["company"] for r in QUAR})
assert len(QUAR_COMPANIES) == 3, "THREE companies threw a suspected split"
assert {r["note"].split(" -- ")[0] for r in QUAR} == {"split", "not_a_split"}, \
    "both verdicts are represented — the detector did not just agree with itself"

# the 11.93 row: ARK's COMMON line. Its ratio and its decided factor DIFFER, which is the
# whole point of the factor beat.
ARK = next(r for r in QUAR if r["class"] == "COM:UNSPECIFIED"
           and r["company"].startswith("Perplexity"))
assert ARK["ratio_min"] == ARK["ratio_max"] == "11.9300", "the ratio is 11.93"
assert ARK["factor"] == "10.0000" and D(ARK["factor"]) != D(ARK["ratio_min"]), \
    "ratio is NOT factor — the panel records them separately"

# correction 1: the evidence series must be the LARGEST position, not the smallest.
# correction 2: the unchanged value must survive to the cent, un-rounded.
PERP_PRE, PERP_POST = PERP[-2], PERP[-1]
assert D(PERP_POST["shares"]) == D(PERP_PRE["shares"]) * 10, "ten times the shares"
assert PERP_PRE["value_usd"] == PERP_POST["value_usd"] == "13488132.50", \
    "the same dollars TO THE CENT — figdata must carry the unrounded value"
assert "." in PERP_PRE["value_usd"], "values carry two decimals, not a flattering round number"

assert len({r["shares"] for r in ANTH}) == 1 and len(ANTH) == 13, \
    "Anthropic: one share count across all thirteen quarters"
ANTH_STEP = next(i for i, r in enumerate(ANTH) if r["suspected"])
assert D(ANTH[ANTH_STEP + 1]["price"]) < D(ANTH[ANTH_STEP]["price"]), \
    "and the step REVERSES the next quarter, which a split never does"

assert len({r["shares"] for r in SPX}) == 1, "SpaceX: constant share count"
SPX_STEP = next(i for i, r in enumerate(SPX) if r["suspected"])
assert D(SPX[SPX_STEP]["value_usd"]) == D(SPX[SPX_STEP - 1]["value_usd"]) * 2, \
    "value exactly doubled"

# correction 4: the check table is COUNTED, never hardcoded, and 'unreachable' is not 'fail'
assert len(CHECKS) == 7, "plan.md listed seven checks"
assert sum(1 for c in CHECKS if c["passed"] is True) == 6, "six pass"
assert sum(1 for c in CHECKS if c["passed"] is False) == 0, "none fail"
assert sum(1 for c in CHECKS if c["passed"] is None) == 1, "one is unreachable and says so"
assert next(c for c in CHECKS if c["passed"] is None)["note"], \
    "the unreachable check must carry its reason, or it is just a silent pass"

assert AGREE["families"] == sum(c["families"] for c in AGREE["clusters"]) == 10, \
    "ten manager families, and the clusters must account for all of them"

if "--check" in sys.argv:
    print("[week7] all assertions pass")
    sys.exit(0)

# ── derived, never typed ──────────────────────────────────────────────────────
def money(v):
    return "$" + f"{D(str(v)):,.2f}"


def num(v):
    return f"{int(D(str(v))):,}"


ARK_BEFORE, ARK_AFTER = D(ARK["price_before"]), D(ARK["price_after"])
ARK_RATIO = D(ARK["ratio_min"])
ARK_FACTOR = D(ARK["factor"])
COLLAPSE_PCT = round(float((1 - ARK_AFTER / ARK_BEFORE) * 100))            # 92
NEAREST_WHOLE = ARK_RATIO.to_integral_value(rounding="ROUND_HALF_UP")      # 12
GAP = abs(NEAREST_WHOLE - ARK_RATIO)                                       # 0.07
MISS_FACTOR = int(GAP / OLD_WINDOW)                                        # 3
NEW_WINDOW_AT = NEAREST_WHOLE * D(str(NEW_TOL))                            # 0.12
MARKDOWN_PCT = round(float((1 - ARK_AFTER / (ARK_BEFORE / ARK_FACTOR)) * 100))  # 16
UNPRICEABLE = sum(b["marks"] for b in BLOCKS if "split" not in b["reason"])      # 294
CLUSTER_GAP = abs(D(AGREE["clusters"][0]["price"]) - D(AGREE["clusters"][1]["price"]))
EXACT_TEN = next(r for r in QUAR if r["ratio_min"] == "10.0000")

HANDLE = "@HumanitariansAI"
SEGMENT = "Building the Marks Panel and the Split Detector"
KICKER = "Irreducibly Human"     # GATE L rule 7 — the FIXED claude-hai series name
OLD_WINDOW_SRC = ("the previous window (±0.02) is from narration_script.md / plan.md — "
                  "figdata_week7.json carries only the rule that ships")


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
    "Hi, I'm Om Mali. This video is about the price panel, turning S E C filings into an "
    "actual per share price history for private A I companies, and catching the one thing "
    "that would have silently ruined it. The arithmetic is one line. Everything hard is in "
    "deciding which rows deserve to be in it.",
    20,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": "Ahoj, HAI",
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "Build the per-share price panel: value divided by share count, once per security "
            "per fund per quarter. Then catch the stock splits before they enter the series as "
            "crashes — and do not let the detector decide what a step actually is."
        ),
        "runningText": "pricing 5,806 holdings…",
        "folderLabel": HANDLE,
        "modelLabel": "Opus 5",
        "effortLabel": "High",
        "output": [
            f"{num(TOT['marks'])} marks from {num(COV['holdings'])} filed holdings — "
            f"reconciles exactly",
            f"split detector: window was ±{OLD_WINDOW}, the test case is {ARK_RATIO} — missed",
            f"now a relative {NEW_TOL:.0%} rule; {len(QUAR_COMPANIES)} suspected splits, "
            f"all decided by a person",
        ],
    }, "type-on", [
        {"at": "0.00", "event": "Cream Claude composer, empty. Serif greeting 'Ahoj, HAI' + terracotta spark above it."},
        {"at": "0.15", "event": "The ask types itself into the composer, character by character."},
        {"at": "0.60", "event": "Send button arms terracotta; running indicator reads 'pricing 5,806 holdings…'."},
        {"at": "0.75", "event": "Three output lines land in sequence — the ask arrives ANSWERED (COLD OPEN LAW)."},
    ]),
))

# ── B01 · EXECUTIVE SUMMARY ───────────────────────────────────────────────────
beats.append(beat(
    "B01", "EXECUTIVE SUMMARY", "REMOTION",
    "Here is the whole week. Value divided by share count, once per security per fund per "
    "quarter, gives five thousand four hundred and seventy-nine marks. That part is one line "
    "of arithmetic. The part that took the week is a detector for stock splits, because a "
    "split makes a price look like a crash. It found three. It could not tell me what any of "
    "them were.",
    23,
    remotion("W7Bluf", "reel-local/MarksPanelAndSplitDetector", {
        "sparkLine": "One line of arithmetic. A week of judgment.",
        "headline": "Value ÷ shares.",
        "formulaNote": f"once per security, per fund, per quarter — {num(TOT['marks'])} marks",
        "halves": [
            # NOT a product: 232 x 55 x 10 is not 5,479. Marks exist only where a fund
            # actually filed that security in that period, so the dimensions are listed,
            # never multiplied.
            {"kicker": "THE ARITHMETIC", "value": "1 line",
             "sub": f"across {num(TOT['securities'])} securities, {num(TOT['periods'])} period ends, {num(TOT['companies'])} companies"},
            {"kicker": "THE WEEK", "value": "the detector",
             "sub": f"{len(QUAR_COMPANIES)} companies threw a suspected split — the ratio classifies none of them"},
        ],
        "verdictLabel": "what the detector cannot do",
        "verdict": "decide",
        "rule": (
            f"A split makes a price look like a crash. Catching the step is arithmetic; "
            f"deciding what it is took a person and a written reason on all "
            f"{len(QUAR)} quarantined series."
        ),
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'value divided by share count'", "event": "The formula sets in serif at display size."},
        {"at": "on 'five thousand four hundred and seventy-nine marks'", "event": "The mark count resolves beneath it."},
        {"at": "on 'one line of arithmetic'", "event": "Two halves land — the arithmetic, and the week."},
        {"at": "on 'could not tell me what any of them were'", "event": "A 'decide' chip lands and is struck through."},
    ], intent="The BLUF and the division of labour: the panel is one line, the detector is the week, and the detector does not decide."),
))

# ── B02 · THE PANEL ───────────────────────────────────────────────────────────
beats.append(beat(
    "B02", "THE PANEL", "REMOTION",
    "Five thousand eight hundred and six filed holdings go in. Twenty-eight were rejected last "
    "month as belonging to nothing. Seventy-two sit on filings a later amendment replaced. The "
    "remaining five thousand seven hundred and six aggregate into marks. It reconciles exactly, "
    "and nothing gets dropped for being awkward.",
    21,
    remotion("W7Panel", "reel-local/MarksPanelAndSplitDetector", {
        "sparkLine": "Every filed row accounts for itself.",
        "eyebrow": "WEEK 7 · THE PANEL",
        "title": "Where every filed row went",
        "subtitle": "one mark = one fund's recorded price for one security at one period end",
        "start": COV["holdings"],
        "startLabel": "filed holdings",
        "deductions": [
            {"label": "rejected last month — belonged to nothing", "value": COV["rejected_not_in_universe"]},
            {"label": "superseded by a later amendment", "value": COV["superseded_by_amendment"]},
        ],
        "remain": COV["lines_in_marks"],
        "remainLabel": "priced lines, aggregated into marks",
        "marks": TOT["marks"],
        "marksLabel": "marks",
        "splits": [
            {"label": "priced", "value": TOT["priced"], "hot": False},
            {"label": "not a share price", "value": UNPRICEABLE, "hot": True},
        ],
        "blocks": [{"label": b["reason"], "value": b["marks"]} for b in BLOCKS],
        "blocksLabel": "held out of the change series",
        "reconcileNote": (
            f"{num(COV['holdings'])} − {COV['rejected_not_in_universe']} − "
            f"{COV['superseded_by_amendment']} = {num(COV['lines_in_marks'])}. Reconciles exactly. "
            f"Nothing dropped for being awkward."
        ),
        "source": "SOURCE: figdata_week7.json — coverage, totals, blocks; queried from the panel at build time",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'five thousand eight hundred and six'", "event": "The starting count resolves at display size."},
        {"at": "on each deduction", "event": "28 and 72 are subtracted in sequence, each with its reason."},
        {"at": "on 'aggregate into marks'", "event": "5,706 lines collapse into 5,479 marks."},
        {"at": "on 'reconciles exactly'", "event": "The arithmetic lands across the foot as a single line."},
    ], intent="Rebuild of pantry/w7-panel.png. The subtraction happens on screen, so 'reconciles' is shown rather than asserted."),
))

# ── B03 · A SPLIT LOOKS LIKE A CRASH ──────────────────────────────────────────
beats.append(beat(
    "B03", "WHY IT MATTERS", "REMOTION",
    "Here is why the detector matters. Perplexity went from six hundred and ninety-five dollars "
    "a share to fifty-eight. Read naively that is a ninety-two percent collapse, and it would "
    "have entered the price history as one. It is not a collapse. It is a stock split, and a "
    "price series has to know the difference.",
    21,
    remotion("W7Crash", "reel-local/MarksPanelAndSplitDetector", {
        "sparkLine": "Not a collapse. A split.",
        "eyebrow": "WEEK 7 · WHY IT MATTERS",
        "title": "A split looks exactly like a crash",
        "company": ARK["company"],
        "security": f"{ARK['class']} — ARK's common line",
        "fromPeriod": ARK["from_period"],
        "toPeriod": ARK["to_period"],
        "priceBefore": float(ARK_BEFORE),
        "priceAfter": float(ARK_AFTER),
        "naiveLabel": "read as a price move",
        "naive": f"−{COLLAPSE_PCT}%",
        "truthLabel": "what it actually is",
        "truth": "a stock split",
        "note": (
            f"The same shape, either way. A change series that cannot tell them apart publishes "
            f"a {COLLAPSE_PCT}% crash that never happened."
        ),
        "source": f"SOURCE: figdata_week7.json — quarantine, {ARK['class']}; the −{COLLAPSE_PCT}% is derived from the two prices",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'six hundred and ninety-five'", "event": "The before price sets at display size."},
        {"at": "on 'to fifty-eight'", "event": "A line falls off a cliff to the after price."},
        {"at": "on 'ninety-two percent collapse'", "event": "The naive reading lands in terracotta beneath the drop."},
        {"at": "on 'it is a stock split'", "event": "The naive reading is struck and the real cause replaces it."},
    ], intent="The drop must be FELT before it is explained — the beat exists so the viewer understands why a detector is worth a week."),
))

# ── B04 · TOO NARROW ──────────────────────────────────────────────────────────
beats.append(beat(
    "B04", "TOO NARROW", "REMOTION",
    "My detector used a window of plus or minus nought point nought two around whole numbers. "
    "Perplexity's ratio is eleven point nine three, nought point nought seven away from twelve. "
    "The window misses it by a factor of three. It looked correct only because the other "
    "Perplexity step landed on exactly ten. The rule is now a relative one percent window, "
    "imported by the detector and the review queue.",
    26,
    remotion("W7Tolerance", "reel-local/MarksPanelAndSplitDetector", {
        "sparkLine": "Too narrow to catch its own test case.",
        "eyebrow": "WEEK 7 · TOO NARROW",
        "title": "The window that missed its own test case",
        "nearest": float(NEAREST_WHOLE),
        "ratio": float(ARK_RATIO),
        "oldWindow": float(OLD_WINDOW),
        "oldWindowLabel": f"old window ±{OLD_WINDOW}",
        "newWindow": float(NEW_WINDOW_AT),
        "newWindowLabel": f"new window ±{NEW_TOL:.0%} = ±{NEW_WINDOW_AT}",
        "gap": float(GAP),
        "gapLabel": f"{GAP:.2f} away from {NEAREST_WHOLE:.2f}",
        "missLabel": f"missed by a factor of {MISS_FACTOR}",
        "decoyRatio": float(D(EXACT_TEN["ratio_min"])),
        "decoyLabel": (
            "the other Perplexity step — it lands on a whole number, inside any window, "
            "which is why an absolute rule passed its own smoke test"
        ),
        "fix": f"Now a RELATIVE {NEW_TOL:.0%} window. One rule, imported by the detector and the review queue.",
        "notBroken": "Not broken. Too narrow.",
        "source": f"SOURCE: figdata_week7.json — tolerance = {NEW_TOL}, quarantine ratios. {OLD_WINDOW_SRC}.",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'plus or minus nought point nought two'", "event": "A number line draws with a narrow grey box around 12."},
        {"at": "on 'eleven point nine three'", "event": "A terracotta mark lands OUTSIDE the box, and the gap is measured."},
        {"at": "on 'by a factor of three'", "event": "The gap and the window are shown against each other."},
        {"at": "on 'landed on exactly ten'", "event": "The decoy ratio appears at exactly 10, inside its own window."},
        {"at": "on 'a relative one percent window'", "event": "The wider new window draws and contains the 11.93 mark."},
    ], intent="Rebuild of pantry/w7-tolerance.png. The mark must sit visibly OUTSIDE the old box — the miss is a distance, so it is measured on screen."),
))

# ── B05 · THE SHARE COUNT ─────────────────────────────────────────────────────
beats.append(beat(
    "B05", "THE EVIDENCE", "REMOTION",
    "But catching a step is not deciding what it is. Three companies threw one, and the ratio "
    "cannot tell you which is which. The share count can. Perplexity's preferred line went from "
    "nineteen thousand shares to a hundred and ninety-three thousand, while the dollar value "
    "did not move by a cent. Ten times the shares, exactly the same money.",
    23,
    remotion("W7Evidence", "reel-local/MarksPanelAndSplitDetector", {
        "sparkLine": "Splits move the share count.",
        "eyebrow": "WEEK 7 · THE EVIDENCE",
        "title": "The ratio cannot tell you. The share count can.",
        "company": EXACT_TEN["company"],
        "security": EXACT_TEN["title"],
        "rows": [
            {
                "period": r["period_end"],
                "shares": int(D(r["shares"])),
                "value": float(D(r["value_usd"])),
                "price": float(D(r["price"])),
                "hot": r["suspected"],
            } for r in PERP
        ],
        "sharesLabel": "shares",
        "valueLabel": "filed value",
        "priceLabel": "implied price",
        "unchanged": money(PERP_POST["value_usd"]),
        "unchangedLabel": "unchanged, to the cent",
        "ratio": f"×{int(D(PERP_POST['shares']) / D(PERP_PRE['shares']))}",
        "ratioLabel": "shares",
        "verdict": "Ten times the shares. Exactly the same money. That is a split.",
        "source": (
            f"SOURCE: figdata_week7.json — perplexity, the LARGEST position (the figure used to "
            f"pick the smallest; the run log cites the largest). Values to the cent, un-rounded."
        ),
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'three companies threw one'", "event": "The security and class are named so this row cannot be confused with the 11.93 one."},
        {"at": "on 'nineteen thousand shares'", "event": "Three filed rows land: shares, value, implied price."},
        {"at": "on 'a hundred and ninety-three thousand'", "event": "The share count column lights terracotta on the ×10 step."},
        {"at": "on 'did not move by a cent'", "event": "The two identical filed values are bracketed, shown to the cent."},
    ], intent="Rebuild of pantry/w7-evidence.png, first row. This is the T. Rowe PREFERRED line at ratio 10.0000 — a different security from the 11.93 common line, and labelled as such."),
))

# ── B06 · WHO DECIDED ─────────────────────────────────────────────────────────
beats.append(beat(
    "B06", "WHO DECIDED", "REMOTION",
    "Anthropic held the same eighty-nine thousand shares in all thirteen quarters. Only the "
    "value moved, and the step reverses the next quarter, which a split never does. SpaceX the "
    "same: share count constant, value exactly doubled. Splits move the share count. Repricings "
    "move the value. A person made all three calls, and wrote the reason down.",
    23,
    remotion("W7Verdicts", "reel-local/MarksPanelAndSplitDetector", {
        "sparkLine": "A person made every call.",
        "eyebrow": "WEEK 7 · WHO DECIDED",
        "rule": ["Splits move the share count.", "Repricings move the value."],
        "cases": [
            {
                "company": "Anthropic PBC",
                "ratio": f"×{D(ANTH[ANTH_STEP]['ratio']):.2f}",
                "shares": f"{int(D(ANTH[0]['shares'])):,} shares, all {len(ANTH)} quarters",
                "evidence": (
                    f"${D(ANTH[ANTH_STEP - 1]['price']):,.2f} → "
                    f"${D(ANTH[ANTH_STEP]['price']):,.2f} → "
                    f"${D(ANTH[ANTH_STEP + 1]['price']):,.2f} — it reverses. A split never does."
                ),
                "verdict": "not a split",
                "isSplit": False,
            },
            {
                "company": "Space Exploration Technologies Corp.",
                "ratio": f"×{D(SPX[SPX_STEP]['ratio']):.2f}",
                "shares": f"{int(D(SPX[0]['shares'])):,} shares, constant",
                "evidence": (
                    f"{money(SPX[SPX_STEP - 1]['value_usd'])} → {money(SPX[SPX_STEP]['value_usd'])}, "
                    f"exactly doubled; continues to ${D(SPX[SPX_STEP + 1]['price']):,.2f}"
                ),
                "verdict": "not a split",
                "isSplit": False,
            },
            {
                "company": EXACT_TEN["company"],
                "ratio": f"×{D(EXACT_TEN['ratio_min']):.2f}",
                "shares": f"{int(D(PERP_PRE['shares'])):,} → {int(D(PERP_POST['shares'])):,} shares",
                "evidence": f"value unchanged at {money(PERP_POST['value_usd'])} — the shares moved, not the money",
                "verdict": "split",
                "isSplit": True,
            },
        ],
        "reviewer": QUAR[0]["note"].split(" -- ")[1].split(":")[0].strip(),
        "reviewerLabel": "adjudicated by",
        "countNote": (
            f"All {len(QUAR)} quarantined series carry a written reason and a human name. "
            f"{sum(1 for r in QUAR if r['note'].startswith('split'))} were splits, "
            f"{sum(1 for r in QUAR if r['note'].startswith('not_a_split'))} were not."
        ),
        "source": "SOURCE: figdata_week7.json — quarantine notes, anthropic and spacex series",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "0.05", "event": "The two-line rule sets at display size: splits move the share count, repricings move the value."},
        {"at": "on 'Anthropic held the same eighty-nine thousand'", "event": "The Anthropic case lands with its constant share count and its reversal."},
        {"at": "on 'SpaceX the same'", "event": "The SpaceX case lands — constant shares, value exactly doubled."},
        {"at": "on 'a person made all three calls'", "event": "The reviewer's name lands against all three verdicts."},
    ], intent="The rule first, then each case tested against it. The two NOT-a-split verdicts come first so the beat is not a victory lap for the detector."),
))

# ── B07 · RATIO IS NOT FACTOR ─────────────────────────────────────────────────
beats.append(beat(
    "B07", "RATIO IS NOT FACTOR", "REMOTION",
    "One of those is subtler. Eleven point nine three is not a split factor. It is a ten for "
    "one split and a sixteen percent markdown that landed in the same quarter. Divide by eleven "
    "point nine three and you erase a real price move. Divide by ten and it survives. So the "
    "panel records what a person decided to divide by, separately from what the machine "
    "measured.",
    25,
    remotion("W7Factor", "reel-local/MarksPanelAndSplitDetector", {
        "sparkLine": "Measured is not decided.",
        "eyebrow": "WEEK 7 · RATIO IS NOT FACTOR",
        "title": f"{ARK_RATIO:.2f} is not a split factor",
        "observed": {"label": "measured ratio", "value": f"{ARK_RATIO:.2f}"},
        "parts": [
            {"label": "a real split", "value": f"{ARK_FACTOR:.0f}-for-1", "hot": True},
            {"label": f"and a markdown in the same quarter", "value": f"−{MARKDOWN_PCT}%", "hot": False},
        ],
        "outcomes": [
            {
                "label": f"divide by {ARK_RATIO:.2f}",
                "result": "the markdown disappears",
                "detail": f"a real {MARKDOWN_PCT}% price move erased as if it were an artifact",
                "right": False,
            },
            {
                "label": f"divide by {ARK_FACTOR:.0f}",
                "result": "the markdown survives",
                "detail": f"${ARK_BEFORE / ARK_FACTOR:,.2f} → ${ARK_AFTER:,.2f} stays in the series",
                "right": True,
            },
        ],
        "rule": (
            f"So the panel stores both: ratio {ARK_RATIO} as measured, factor "
            f"{ARK_FACTOR:.4f} as decided. Week 8 divides by the decided one."
        ),
        "source": f"SOURCE: figdata_week7.json — quarantine {ARK['class']}: ratio_min/max and factor are separate fields",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'eleven point nine three is not a split factor'", "event": "The measured ratio sets alone."},
        {"at": "on 'a ten for one split and a sixteen percent markdown'", "event": "It decomposes into two parts; only the split half takes the accent."},
        {"at": "on 'divide by eleven point nine three'", "event": "The wrong outcome lands — the markdown erased."},
        {"at": "on 'divide by ten and it survives'", "event": "The right outcome lands beside it and keeps the accent."},
    ], intent="Rebuild of pantry/w7-factor.png. Red marks the CORRECT answer, never the wrong one — DESIGN.md forbids red as a warning colour (README correction 3)."),
))

# ── B08 · THE CHECKS ──────────────────────────────────────────────────────────
beats.append(beat(
    "B08", "THE CHECKS", "REMOTION",
    "The plan listed seven checks for this panel. Six pass. The seventh needs filings the S E C "
    "has not published yet, and it reports that rather than quietly passing. And one of the six "
    "expected four managers to agree on Anthropic's price. Ten do, in two clusters four "
    "thousandths of a dollar apart.",
    22,
    remotion("W7Checks", "reel-local/MarksPanelAndSplitDetector", {
        "sparkLine": "Six pass. One says why it cannot.",
        "eyebrow": "WEEK 7 · THE CHECKS",
        "title": f"{len(CHECKS)} checks: {sum(1 for c in CHECKS if c['passed'] is True)} pass, "
                 f"{sum(1 for c in CHECKS if c['passed'] is None)} unreachable, "
                 f"{sum(1 for c in CHECKS if c['passed'] is False)} fail",
        "subtitle": "counted from the table, never hardcoded",
        "checks": [
            {"label": c["check"],
             "state": ("pass" if c["passed"] is True else "fail" if c["passed"] is False else "unreachable"),
             "note": c["note"]}
            for c in CHECKS
        ],
        "agreementLabel": "one check expected 4 managers to agree",
        "agreementValue": AGREE["families"],
        "agreementValueLabel": "manager families agree",
        "clusters": [
            {"price": c["price"], "families": c["families"], "managers": c["managers"]}
            for c in AGREE["clusters"]
        ],
        "clusterNote": (
            f"Two clusters, {CLUSTER_GAP} apart — the same price to the cent, "
            f"rounded differently by different filers."
        ),
        "honestNote": (
            "An unreachable check is not a pass. It carries its reason on screen: the bulk "
            "archive ends before the filings that would settle it."
        ),
        "source": "SOURCE: figdata_week7.json — checks[], agreement[]; pass/fail/unreachable counted at injection",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'seven checks'", "event": "Seven rows land, six ticking in sequence."},
        {"at": "on 'the seventh needs filings'", "event": "The seventh lands hollow, with its reason beside it."},
        {"at": "on 'four managers'", "event": "The expected 4 is replaced by the measured 10."},
        {"at": "on 'two clusters'", "event": "The two price clusters and their manager lists land beneath."},
    ], intent="Rebuild of pantry/w7-checks.png. The counts are computed from the table (README correction 4 — the title used to hardcode '0 fail' and disagreed with its own rows)."),
))

# ── B09 · VERDICT ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B09", "VERDICT", "BOOKEND",
    "Week seven on one page. Five thousand four hundred and seventy-nine marks, value divided "
    "by share count, every filed holding accounted for. A detector whose window was too narrow "
    "to catch its own test case, now a relative one percent rule. Three companies threw a "
    "suspected split and the ratio could not tell them apart. Share counts could, and a person "
    "made every call with the reason written down. Six of seven checks pass, and the seventh "
    "says why it cannot. Next week: how often these marks actually move.",
    34,
    remotion("ClaudeVerdictArtifact", "proven-core/ClaudeVerdictArtifact", {
        "sparkLine": "",
        "artifactTitle": f"{SEGMENT} — week 7",
        "artifactHeading": "What the panel does",
        "artifactLines": [
            f"{num(TOT['marks'])} marks — value ÷ share count, per security per fund per period. "
            f"{num(COV['holdings'])} − {COV['rejected_not_in_universe']} rejected − "
            f"{COV['superseded_by_amendment']} superseded = {num(COV['lines_in_marks'])}. Reconciles exactly.",
            f"The split detector's window was ±{OLD_WINDOW} absolute and missed its own test case "
            f"at {ARK_RATIO} by a factor of {MISS_FACTOR}. It is now a relative {NEW_TOL:.0%} rule, "
            f"imported by both the detector and the review queue.",
            f"{len(QUAR_COMPANIES)} companies threw a suspected split; the ratio cannot classify "
            f"them. Share counts can: ×10 shares at an unchanged "
            f"{money(PERP_POST['value_usd'])} is a split, constant shares with a reversing step "
            f"is not.",
            f"Ratio is not factor. {ARK_RATIO} = a {ARK_FACTOR:.0f}-for-1 split AND a "
            f"{MARKDOWN_PCT}% markdown in one quarter. The panel stores measured and decided "
            f"separately; {SPLIT_BLOCK[0]['marks']} marks stay blocked until Week 8 divides.",
            f"{sum(1 for c in CHECKS if c['passed'] is True)} of {len(CHECKS)} checks pass, "
            f"{sum(1 for c in CHECKS if c['passed'] is False)} fail, "
            f"{sum(1 for c in CHECKS if c['passed'] is None)} unreachable and says so. One expected "
            f"4 managers to agree on Anthropic's price; {AGREE['families']} do.",
        ],
    }, "stagger", [
        {"at": "0.05", "event": f"The Claude artifact page opens — {SEGMENT}, week 7."},
        {"at": "each line", "event": "Five findings stagger in, one per spoken clause."},
    ]),
    lead=0.4,
))

# ── B10 · HANDOFF ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B10", "HANDOFF", "BOOKEND",
    "Your turn. Paste this into Claude. Take a threshold in your own code. An absolute "
    "tolerance, a cut off, a magic number. Find the case it was written for, then check whether "
    "it would still catch that case today. Mine would not, and it looked fine because a second "
    "case happened to land inside it. A threshold that has never been tested against the thing "
    "it exists to catch is just a guess with a number on it.",
    28,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": "Your turn.",
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "Find every absolute threshold in my code — tolerances, cut-offs, magic numbers. For "
            "each one, tell me which case it was written to catch, then test it against that case "
            "as the data looks today. Where an absolute window should be a relative one, say so, "
            "and tell me which other module would have to import the same rule."
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
    "Building the marks panel and the split detector. Week seven of the Private AI Valuation "
    "Agent. Next week, how often these marks move. Om Mali, for Humanitarians A I.",
    13,
    remotion("ClaudeTitleOutro", "proven-core/ClaudeTitleOutro", {
        "title": SEGMENT,
        "handle": HANDLE,
        "subline": "week 7 · the Private AI Valuation Agent",
    }, "fade", [
        {"at": "0.00", "event": "Title restates poster-style in serif with the terracotta period; handle beneath."},
    ]),
))

sheet = {
    "metadata": {
        "title": SEGMENT,
        "slug": "building-the-marks-panel-and-the-split-detector",
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
        "greeting": "Ahoj, HAI",
        "greeting_note": "hello lexicon: Czech (short form). HAI persona takes only the shortest cues (Hi · Ola · Hej · Ciao · Hallo · Salut · Ahoj). Rotated off weeks 1, 2, 4, 5 and 6 so the series never repeats a language.",
        "aspect_ratio": "16:9",
        "fit": "pad",
        "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
        "color_semantics": "Claude FIDELITY skin: cream #F2F0E9 stage, warm ink #3D3929, terracotta #D97757 as the ONE accent. The source figures use red as the PRIMARY series, never 'danger' — README correction 3 records red being misused as a warning and fixed so it marks the CORRECT answer. That reading is preserved: terracotta marks the right answer and the subject of each beat, never a hazard.",
        "series": "Private AI Valuation Agent — week 7 (follows 2026-09-04-Building-the-human-review-queue)",
        "derived_from": "narration_script.md (human-authored, 458 spoken words, target 3:00) plus README.md's figure-to-beat map. Every on-screen figure is a prop injected by build_beat_sheet.py from figdata_week7.json, under assertions — no number is typed by hand. The ONE exception is the OLD detector window (±0.02), which figdata does not carry; it comes from the script and plan.md and every screen using it says so.",
        "note": "ai-explainer / claude-hai. ILLUSTRATE LAW: the Claude UI appears at B00 (cold open, answered), B09 (verdict artifact), B10 (handoff) and B11 (outro) only — every body beat illustrates its concept as a native animated Remotion scene (REBUILD LAW). The five source PNGs and their SVG sources are REFERENCE in pantry/, never slotted as media. The script's six sections are split into eight body beats; the split is logged in BUILD-LOG.md. TWO THINGS NOT TO GET WRONG: the detector was not broken, it was too narrow; and the splits are detected and decided, NOT adjusted — that is Week 8.",
        "companion_vertical": "vertical/ — the same twelve beats, same audio, rendered 9:16 at 2160×3840 from portrait compositions (never a crop).",
        "tags": ["SEC", "N-PORT", "marks panel", "price history", "stock split", "split detector",
                 "tolerance", "human in the loop", "data engineering", "Humanitarians AI", "Mycroft"],
    },
    "beats": beats,
}

out = HERE / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

words = {b["beat_id"]: len(b["narration_text"].split()) for b in beats}
print(f"[week7] wrote {out}  — {len(beats)} beats")
print("[week7] narration words:", " ".join(f"{k}={v}" for k, v in words.items()))
body = [v for k, v in words.items() if k in ("B01", "B02", "B03", "B04", "B05", "B06", "B07", "B08")]
print(f"[week7] body beats {min(body)}–{max(body)}w (band 45–70), total {sum(words.values())}w")
print(f"[week7] derived: collapse -{COLLAPSE_PCT}%  gap {GAP}  miss x{MISS_FACTOR}  "
      f"new window ±{NEW_WINDOW_AT}  markdown -{MARKDOWN_PCT}%  unpriceable {UNPRICEABLE}  "
      f"cluster gap {CLUSTER_GAP}")
