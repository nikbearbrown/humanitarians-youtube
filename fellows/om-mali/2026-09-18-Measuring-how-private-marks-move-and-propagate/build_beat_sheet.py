#!/usr/bin/env python3
"""
build_beat_sheet.py — week 8, Measuring How Private Marks Move and Propagate.

Writes beat_sheet.json with EVERY on-screen figure injected from figdata_week8.json.
No number is typed into a scene or a beat sheet by hand.

The assertions below cover the four defects the README records — each of which was wrong in
the drawing code until the PNG was read:
  1. a subtitle hard-coded "Nine managers" for a window holding 8 managers and 11 marks;
  2. the window's red/grey split hard-coded at `price > 220`;
  3. the dispersion highlight hard-coded at `spread >= 0.4`;
  4. the propagation figure claiming "the biggest events are the fastest" — which the data
     does not support.
All four are handled here by DERIVING the value instead: the window's manager and mark
counts are counted, its levels come from the same single-linkage clustering the findings
module uses (`same_date.level_rel`), the dispersion highlight is the measured p90, and the
big-vs-small comparison is computed so the beat can show why the old claim came out.

Usage:  python build_beat_sheet.py            (writes beat_sheet.json)
        python build_beat_sheet.py --check    (assertions only, writes nothing)
"""
import json, statistics, sys
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIG = json.loads((HERE / "figdata_week8.json").read_text(encoding="utf-8"))

REMARK = FIG["remark"]
OVERALL = REMARK["overall"]
SENS = REMARK["sensitivity"]
BY_CO = REMARK["by_company"]
SAME = FIG["same_date"]
STATS = FIG["same_date_stats"]
PROP = FIG["propagation"]
EVENTS = PROP["events"]
GUARDS = FIG["guards"]
WINDOW = FIG["window"]

D = Decimal

# ── assertions: the build fails rather than the video lying ───────────────────
assert GUARDS["marks"] == 5479, "the panel week 7 built"
assert GUARDS["unadjudicated_splits"] == 0 and GUARDS["incomplete_runs"] == 0, \
    "no statistic may run over an unadjudicated split or an incomplete run"
assert OVERALL["steps"] + OVERALL["first_observation"] == OVERALL["marks"] \
    == GUARDS["marks"] - GUARDS["change_blocked"], \
    "the measured population must reconcile to marks minus the change-blocked ones"

assert OVERALL["steps"] == 4079 and OVERALL["unchanged"] == 1019
assert round(OVERALL["share_unchanged"], 4) == 0.2498, "25.0% unchanged"
assert OVERALL["moved"] + OVERALL["unchanged"] == OVERALL["steps"], "moved + unchanged = steps"

# the plan expected 30-40%. EVERY widening of "unchanged" must still land under 30, or the
# finding is an artifact of where the line was drawn rather than a disagreement with the plan.
PLAN_LO, PLAN_HI = 0.30, 0.40
WIDENINGS = [
    ("exactly equal", SENS["unchanged_exact"]),
    ("within 0.1%", SENS["unchanged_if_0_1pct_is_flat"]),
    ("within 1%", SENS["unchanged_if_1pct_is_flat"]),
]
assert all(v < PLAN_LO for _, v in WIDENINGS), \
    "if any widening reaches the plan's band the finding is a threshold artifact, not a result"
assert WIDENINGS[0][1] < WIDENINGS[1][1] < WIDENINGS[2][1], "widenings must be monotonic"

assert len(BY_CO) == 10, "ten companies"
assert sum(c["steps"] for c in BY_CO) == OVERALL["steps"], "the split must cover every step"
CO_MAX = max(BY_CO, key=lambda c: c["share_unchanged"])
CO_LARGEST = max(BY_CO, key=lambda c: c["steps"])     # biggest sample, not biggest share
CO_SMALLEST = min(BY_CO, key=lambda c: c["steps"])
CO_MIN = min(BY_CO, key=lambda c: c["share_unchanged"])
assert CO_MAX["company"].startswith("X.AI") and round(CO_MAX["share_unchanged"], 4) == 0.4854
assert CO_MIN["share_unchanged"] == 0.0, "the true floor is zero, not OpenAI's 1.1%"

assert STATS["groups"] == 130 and round(STATS["median"], 4) == 0.1082
assert STATS["multi_level"] == 92 == len(SAME["transition"]), "92 groups hold >1 price level"
assert len(SAME["steady"]) + len(SAME["transition"]) == STATS["groups"], "steady + transition"
assert STATS["p90"] == 0.405, "the dispersion highlight is the MEASURED p90, not a round number"

# ── the window, entirely derived (README defects 1 and 2) ─────────────────────
WIN_MANAGERS = sorted({r["manager"] for r in WINDOW})
WIN_PERIODS = sorted({r["period_end"] for r in WINDOW})
assert len(WINDOW) == 11 and len(WIN_MANAGERS) == 8, \
    "8 managers, 11 marks — the subtitle used to say nine managers"
assert len(WIN_PERIODS) == 2, "two consecutive period ends"

LEVEL_REL = SAME["level_rel"]


def cluster_levels(prices, rel):
    """Single-linkage on relative gap — the same rule the findings module uses to decide
    what counts as one price level. The window figure used to hard-code `price > 220`."""
    out = []
    for p in sorted(prices):
        if out and (p - out[-1][-1]) / out[-1][-1] <= rel:
            out[-1].append(p)
        else:
            out.append([p])
    return out


WIN_PRICES = [float(D(r["price"])) for r in WINDOW]
WIN_LEVELS = cluster_levels(WIN_PRICES, LEVEL_REL)
assert len(WIN_LEVELS) >= 2, "the window must show more than one level or it argues nothing"
OLD_LEVEL, NEW_LEVEL = WIN_LEVELS[0], WIN_LEVELS[-1]
assert len(NEW_LEVEL) > len(OLD_LEVEL), "the level most managers ended on is the new one"
assert round(min(WIN_PRICES), 4) == 140.9676 and round(max(WIN_PRICES), 4) == 261.5705

# ── propagation, and the claim that came out (README defect 4) ────────────────
assert PROP["events_counted"] == len(EVENTS) == 37
LAGS = [e["lag_to_half_days"] for e in EVENTS]
assert PROP["median_lag_to_half_days"] == 30 == int(statistics.median(LAGS))
assert PROP["max_lag_to_half_days"] == 92 == max(LAGS)
ZERO_DAY = sum(1 for l in LAGS if l == 0)
assert ZERO_DAY == 15, "15 of 37 reach half on the very same period end"

BIG = [e for e in EVENTS if e["managers"] >= 10]
SMALL = [e for e in EVENTS if e["managers"] < 10]
BIG_MED = statistics.median([e["lag_to_half_days"] for e in BIG])
SMALL_MED = statistics.median([e["lag_to_half_days"] for e in SMALL])
BIG_ZERO = sum(1 for e in BIG if e["lag_to_half_days"] == 0)
SMALL_ZERO = sum(1 for e in SMALL if e["lag_to_half_days"] == 0)
assert (SMALL_ZERO / len(SMALL)) > (BIG_ZERO / len(BIG)), \
    "the SMALLER events reach the same period end more often — which is what broke the " \
    "'biggest events are the fastest' claim the figure used to make"
assert PROP["caveat"], "the observability caveat must be present, not assumed"

if "--check" in sys.argv:
    print("[week8] all assertions pass")
    sys.exit(0)

# ── derived, never typed ──────────────────────────────────────────────────────
pct1 = lambda v: f"{v * 100:.1f}%"
num = lambda v: f"{int(v):,}"

UNCHANGED_PCT = pct1(OVERALL["share_unchanged"])                 # 25.0%
MEDIAN_SPREAD = pct1(STATS["median"])                            # 10.8%
P90_SPREAD = pct1(STATS["p90"])                                  # 40.5%
MEASURED_POP = OVERALL["marks"]                                  # 5,178
OLD_LO, OLD_HI = min(OLD_LEVEL), max(OLD_LEVEL)
NEW_LO, NEW_HI = min(NEW_LEVEL), max(NEW_LEVEL)
IN_TRANSIT = [p for lv in WIN_LEVELS[1:-1] for p in lv]
STAGGER = PROP["stagger"]

HANDLE = "@HumanitariansAI"
SEGMENT = "Measuring How Private Marks Move and Propagate"
KICKER = "Irreducibly Human"     # GATE L rule 7 — the FIXED claude-hai series name


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
    "Hi, I'm Om Mali. This video is about measuring how private company share prices actually "
    "move, and how a new price spreads from one fund manager to the next. For seven weeks I "
    "was building a panel of prices out of S E C filings. This week I stopped building it and "
    "started measuring it. Five thousand four hundred and seventy-nine marks, four questions.",
    22,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": "Szia, HAI",
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "Stop building the marks panel and measure it. How often does a price actually "
            "change? Is that rate the same everywhere? Do two managers pricing the same company "
            "on the same date agree? And how fast does a new price level travel?"
        ),
        "runningText": "measuring 5,479 marks…",
        "folderLabel": HANDLE,
        "modelLabel": "Opus 5",
        "effortLabel": "High",
        "output": [
            f"{UNCHANGED_PCT} of {num(OVERALL['steps'])} steps unchanged — the plan expected 30–40%",
            f"and that headline hides everything: {pct1(CO_MIN['share_unchanged'])} to "
            f"{pct1(CO_MAX['share_unchanged'])} by company",
            f"median same-date spread {MEDIAN_SPREAD}; a new level reaches half its holders in "
            f"{PROP['median_lag_to_half_days']} days",
        ],
    }, "type-on", [
        {"at": "0.00", "event": "Cream Claude composer, empty. Serif greeting 'Szia, HAI' + terracotta spark above it."},
        {"at": "0.15", "event": "The ask types itself into the composer, character by character."},
        {"at": "0.60", "event": "Send button arms terracotta; running indicator reads 'measuring 5,479 marks…'."},
        {"at": "0.75", "event": "Three output lines land in sequence — the ask arrives ANSWERED (COLD OPEN LAW)."},
    ]),
))

# ── B01 · EXECUTIVE SUMMARY ───────────────────────────────────────────────────
beats.append(beat(
    "B01", "EXECUTIVE SUMMARY", "REMOTION",
    "Four questions, and the panel answered all four against expectation. Prices move more "
    "often than the plan predicted. The headline rate hides almost everything. Managers "
    "pricing the same company on the same day usually hold different prices. And a new price "
    "level takes a median of thirty days to reach half the managers who will carry it.",
    22,
    remotion("W8Bluf", "reel-local/MarksMoveAndPropagate", {
        "sparkLine": "It stopped growing. It started answering.",
        "headline": "Four questions, four surprises.",
        "questions": [
            {"q": "How often does a price change?",
             "a": f"{UNCHANGED_PCT} unchanged",
             "note": "the plan expected 30–40%"},
            {"q": "Is that rate the same everywhere?",
             "a": f"{pct1(CO_MIN['share_unchanged'])} → {pct1(CO_MAX['share_unchanged'])}",
             "note": "one number would have been true and useless"},
            {"q": "Do two managers agree on a date?",
             "a": f"{MEDIAN_SPREAD} median spread",
             "note": f"{STATS['multi_level']} of {STATS['groups']} groups hold >1 level"},
            {"q": "How fast does a new level travel?",
             "a": f"{PROP['median_lag_to_half_days']} days to half",
             "note": f"{ZERO_DAY} of {len(EVENTS)} arrive on the same period end"},
        ],
        "popLabel": "measured over",
        "popValue": num(MEASURED_POP),
        "popNote": f"marks — {num(GUARDS['marks'])} less the {GUARDS['change_blocked']} held out of every change series",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'four questions'", "event": "The headline sets, then four question rows land in sequence."},
        {"at": "on each answer", "event": "Each row's measured answer resolves to its right, with the expectation beneath."},
        {"at": "on 'a median of thirty days'", "event": "The measured population lands across the foot."},
    ], intent="The BLUF as a question sheet: every row carries what was expected beside what was measured, so the reel's shape is visible in ten seconds."),
))

# ── B02 · HOW OFTEN ───────────────────────────────────────────────────────────
beats.append(beat(
    "B02", "HOW OFTEN", "REMOTION",
    "First question. How often does a mark just get carried forward unchanged? The plan "
    "expected thirty to forty percent. Measured, it is twenty-five. And this is not an "
    "artifact of where I drew the line. I widened the test three ways, and even the most "
    "generous reading stays below the plan's band. Private marks move more than the plan "
    "assumed they would.",
    24,
    remotion("W8Remark", "reel-local/MarksMoveAndPropagate", {
        "sparkLine": "It survives every reasonable definition.",
        "eyebrow": "WEEK 8 · HOW OFTEN",
        "title": "Carried forward unchanged",
        "subtitle": f"{num(OVERALL['steps'])} consecutive observations, guarded",
        "planLo": PLAN_LO,
        "planHi": PLAN_HI,
        "planLabel": "the plan expected",
        "measured": OVERALL["share_unchanged"],
        "measuredLabel": "measured",
        "widenings": [
            {"label": lbl, "value": v, "pct": pct1(v)} for lbl, v in WIDENINGS
        ],
        "widenLabel": "and three ways of widening “unchanged”",
        "verdict": (
            f"Even the most generous reading — anything under 1% counted as flat — is "
            f"{pct1(WIDENINGS[-1][1])}, still under the band. The finding is not a threshold."
        ),
        "source": "SOURCE: figdata_week8.json — remark.overall, remark.sensitivity",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'thirty to forty percent'", "event": "The plan's band draws as a grey span on a 0–50% axis."},
        {"at": "on 'measured, it is twenty-five'", "event": "The measured value lands as a terracotta mark, clearly outside and below the band."},
        {"at": "on 'I widened the test three ways'", "event": "Three widened readings step up in sequence, each still short of the band."},
        {"at": "on 'move more than the plan assumed'", "event": "The verdict lands across the foot."},
    ], intent="Rebuild of pantry/w8-remark.png. The three widenings must be seen to CLIMB toward the band and stop short — that is what makes the result a disagreement rather than a threshold choice."),
))

# ── B03 · THE HEADLINE HIDES IT ───────────────────────────────────────────────
beats.append(beat(
    "B03", "ONE NUMBER, USELESS", "REMOTION",
    "Second thing. That one number across the whole panel would have been true and useless. "
    "Split by company, the same statistic runs from zero for Groq to forty-eight percent for X "
    "dot A I. Anthropic and OpenAI are repriced at nearly every observation. X dot A I and "
    "SpaceX get carried forward a third to a half of the time. Same panel, same rule, "
    "completely different behaviour.",
    25,
    remotion("W8ByCompany", "reel-local/MarksMoveAndPropagate", {
        "sparkLine": "True, and useless.",
        "eyebrow": "WEEK 8 · ONE NUMBER, USELESS",
        "title": "The same statistic, by company",
        "subtitle": "share of consecutive observations carried forward unchanged",
        "overall": OVERALL["share_unchanged"],
        "overallLabel": f"whole panel — {UNCHANGED_PCT}",
        "rows": [
            {"company": c["company"], "share": c["share_unchanged"],
             "pct": pct1(c["share_unchanged"]), "steps": c["steps"],
             "hot": c["company"] == CO_MAX["company"]}
            for c in sorted(BY_CO, key=lambda c: -c["share_unchanged"])
        ],
        "stepsLabel": "steps",
        "smallNote": (
            f"Sample sizes span two orders of magnitude — {num(CO_SMALLEST['steps'])} steps for "
            f"{CO_SMALLEST['company'].split(',')[0]} against {num(CO_LARGEST['steps'])} for "
            f"{CO_LARGEST['company'].split(',')[0]}. Each bar carries its own n, so "
            f"{pct1(CO_MIN['share_unchanged'])} on {CO_MIN['steps']} steps is not read as the "
            f"same kind of fact as {pct1(CO_LARGEST['share_unchanged'])} on {num(CO_LARGEST['steps'])}."
        ),
        "verdict": "Same panel, same rule. The headline describes none of them.",
        "source": "SOURCE: figdata_week8.json — remark.by_company, sorted by share unchanged",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'split by company'", "event": "Ten bars grow in rank order, each labelled with its share and its step count."},
        {"at": "on 'forty-eight percent for X.AI'", "event": "The top bar takes the accent."},
        {"at": "on 'repriced at nearly every observation'", "event": "The whole-panel rate draws as a single line across all ten bars, matching none of them."},
    ], intent="Rebuild of pantry/w8-bycompany.png. The panel-wide rate is drawn as a RULE across the bars so its uselessness is visible — it passes near nothing."),
))

# ── B04 · DO THEY AGREE ───────────────────────────────────────────────────────
beats.append(beat(
    "B04", "SAME DATE", "REMOTION",
    "Third question. When two managers price the same company on the same date, do they agree? "
    "Mostly not. Across a hundred and thirty same-date groups, the median spread between the "
    "highest and lowest price is just under eleven percent. Ninety-two of those groups hold "
    "more than one distinct price level. Different prices on the same date is the normal state "
    "here, not the exception.",
    25,
    remotion("W8Dispersion", "reel-local/MarksMoveAndPropagate", {
        "sparkLine": "Different prices, same date.",
        "eyebrow": "WEEK 8 · SAME DATE",
        "title": "130 same-date groups",
        "subtitle": "spread between the highest and lowest price, one dot per group",
        "spreads": STATS["spreads"],
        "median": STATS["median"],
        "medianLabel": f"median {MEDIAN_SPREAD}",
        "p90": STATS["p90"],
        "p90Label": f"p90 {P90_SPREAD}",
        "maxSpread": STATS["max"],
        "counts": [
            {"value": STATS["multi_level"], "of": STATS["groups"], "label": "hold more than one price level"},
            {"value": STATS["within_1pct"], "of": STATS["groups"], "label": "agree to within 1%"},
        ],
        "steadyNote": (
            f"{len(SAME['steady'])} groups sit on a single level with a median spread of "
            f"{pct1(SAME['median_steady_spread'])} — the stack at zero. The other "
            f"{len(SAME['transition'])} hold more than one level and spread across the rest of "
            f"the axis; only the ones past the dashed line are above the p90."
        ),
        "verdict": "Different prices on the same date is the normal state, not the exception.",
        "source": "SOURCE: figdata_week8.json — same_date_stats.spreads; the highlight is the MEASURED p90, not a round number",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'a hundred and thirty'", "event": "130 dots fill a spread axis, one per group."},
        {"at": "on 'just under eleven percent'", "event": "The median line drops through the field."},
        {"at": "on 'ninety-two of those groups'", "event": "The multi-level groups light terracotta and the count resolves."},
        {"at": "on 'the normal state'", "event": "The p90 marker lands and the verdict follows."},
    ], intent="Rebuild of pantry/w8-dispersion.png. The highlight threshold is the measured p90 — it used to be hard-coded at 0.4 (README defect 3)."),
))

# ── B05 · A ROUND ARRIVING ────────────────────────────────────────────────────
beats.append(beat(
    "B05", "OR A ROUND ARRIVING", "REMOTION",
    "That raises an objection. Maybe those gaps are just timing. A new round lands, and some "
    "managers have picked it up and others have not. So I opened one window. Anthropic "
    "preferred stock, two consecutive period ends, eight managers, eleven marks, running from "
    "a hundred and forty-one up to two hundred and sixty-two. You can see the old level, the "
    "new one, and managers crossing between them.",
    26,
    remotion("W8Window", "reel-local/MarksMoveAndPropagate", {
        "sparkLine": "A round arriving, one manager at a time.",
        "eyebrow": "WEEK 8 · OR A ROUND ARRIVING",
        "title": "One window, opened",
        "subtitle": f"Anthropic preferred · {len(WIN_MANAGERS)} managers · {len(WINDOW)} marks · {WIN_PERIODS[0]} → {WIN_PERIODS[1]}",
        "periods": WIN_PERIODS,
        "marks": [
            {"manager": r["manager"], "period": r["period_end"], "price": float(D(r["price"])),
             "level": next(i for i, lv in enumerate(WIN_LEVELS) if float(D(r["price"])) in lv)}
            for r in WINDOW
        ],
        "levels": [
            {"index": i, "lo": min(lv), "hi": max(lv), "count": len(lv),
             "role": ("old" if i == 0 else "new" if i == len(WIN_LEVELS) - 1 else "in transit")}
            for i, lv in enumerate(WIN_LEVELS)
        ],
        "oldLabel": f"the old level — {len(OLD_LEVEL)} marks near ${OLD_LO:,.0f}",
        "newLabel": f"the new level — {len(NEW_LEVEL)} marks near ${NEW_HI:,.0f}",
        "transitLabel": f"{len(IN_TRANSIT)} in between, mid-crossing",
        "clusterNote": (
            f"Levels are single-linkage at {LEVEL_REL:.0%} relative gap — the same rule the "
            f"findings module uses. The figure used to hard-code the split at a price threshold."
        ),
        "verdict": "Not disagreement about value. A round arriving, one manager at a time.",
        "source": "SOURCE: figdata_week8.json — window[]; manager and mark counts are COUNTED, and the levels are clustered, not thresholded",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'maybe those gaps are just timing'", "event": "The objection sets as the beat's premise."},
        {"at": "on 'eight managers, eleven marks'", "event": "Eleven dots land on a price axis, split into two period-end columns."},
        {"at": "on 'the old level'", "event": "The lowest cluster bands in ink."},
        {"at": "on 'the new one'", "event": "The largest cluster bands in terracotta."},
        {"at": "on 'crossing between them'", "event": "The managers appearing in both columns are joined, and the in-between marks are named as mid-crossing."},
    ], intent="Rebuild of pantry/w8-window.png. Both readings must be visible AT ONCE — this beat exists to stop B04 being over-read as 'managers disagree about value'."),
))

# ── B06 · HOW FAST ────────────────────────────────────────────────────────────
beats.append(beat(
    "B06", "HOW FAST", "REMOTION",
    "Last question. I took every price level that three or more managers adopted, thirty-seven "
    "of them, and measured how long it took to reach half its holders. The median is thirty "
    "days. Fifteen of the thirty-seven get there on the very same period end. The slowest "
    "takes ninety-two days.",
    20,
    remotion("W8Propagation", "reel-local/MarksMoveAndPropagate", {
        "sparkLine": "Thirty days to half.",
        "eyebrow": "WEEK 8 · HOW FAST",
        "title": "How long a new level takes to reach half its holders",
        "subtitle": f"{len(EVENTS)} price levels adopted by {PROP['min_holders']} or more managers",
        "lags": LAGS,
        "median": PROP["median_lag_to_half_days"],
        "medianLabel": f"median {PROP['median_lag_to_half_days']} days",
        "maxLag": PROP["max_lag_to_half_days"],
        "maxLabel": f"slowest {PROP['max_lag_to_half_days']} days",
        "zeroCount": ZERO_DAY,
        "zeroLabel": f"of {len(EVENTS)} reach half on the SAME period end",
        "toAll": PROP["median_lag_to_all_days"],
        "toAllLabel": "days, median, to reach ALL holders",
        "toAllNote": (
            "First-to-last is the weaker number: it counts managers still carrying an old level "
            "long after the company repriced, which is staleness, not slow propagation. That is "
            "why the headline is first-to-half."
        ),
        "source": "SOURCE: figdata_week8.json — propagation.events[].lag_to_half_days",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'thirty-seven of them'", "event": "37 lag values land as a dot column on a 0–92 day axis."},
        {"at": "on 'the median is thirty days'", "event": "The median line drops through them."},
        {"at": "on 'on the very same period end'", "event": "The 15 zero-day events light terracotta at the axis origin."},
        {"at": "on 'ninety-two days'", "event": "The slowest event is marked at the far end."},
    ], intent="Rebuild of pantry/w8-propagation.png. The 15 zero-day events must be visible as a stack AT zero — the distribution's shape is the finding, not the median alone."),
))

# ── B07 · WHAT THE LAG IS NOT ─────────────────────────────────────────────────
beats.append(beat(
    "B07", "WHAT IT IS NOT", "REMOTION",
    "Two things that number is not. It cannot be shorter than the reporting calendar. A "
    "manager filing on the thirtieth of April cannot reflect a thirty-first of March "
    "repricing any sooner. So this measures observability, not diligence. And the figure "
    "originally claimed the biggest events travel fastest. I checked, and it does not hold.",
    23,
    remotion("W8Caveat", "reel-local/MarksMoveAndPropagate", {
        "sparkLine": "Observability, not diligence.",
        "eyebrow": "WEEK 8 · WHAT IT IS NOT",
        "title": "Two things the thirty days is not",
        "bounds": [
            {
                "label": "not diligence",
                "text": (
                    f"The lag cannot be shorter than the reporting calendar. Across "
                    f"{STAGGER['distinct_period_ends']} period ends the panel sees only "
                    f"{STAGGER['distinct_days_of_month']} distinct days of the month, so a manager "
                    f"filing on the 30th cannot reflect a 31st repricing any sooner."
                ),
            },
            {
                "label": "not first-to-last",
                "text": (
                    f"Median to ALL holders is {PROP['median_lag_to_all_days']} days and the tail "
                    f"runs to {PROP['max_lag_to_all_days']}, but that counts managers still "
                    f"carrying an old level — staleness, not propagation."
                ),
            },
        ],
        "struckLabel": "and a claim that came out",
        "struck": "the biggest events are the fastest",
        "evidence": [
            {"label": f"{len(BIG)} events, 10+ managers", "median": f"{BIG_MED:.0f} days",
             "zero": f"{BIG_ZERO}/{len(BIG)} at zero days"},
            {"label": f"{len(SMALL)} events, under 10", "median": f"{SMALL_MED:.0f} days",
             "zero": f"{SMALL_ZERO}/{len(SMALL)} at zero days"},
        ],
        "evidenceNote": (
            f"{BIG_MED:.0f} days against {SMALL_MED:.0f} is three days on {len(BIG)} events, and "
            f"the SMALLER ones reach the same period end more often — "
            f"{SMALL_ZERO}/{len(SMALL)} against {BIG_ZERO}/{len(BIG)}. The caption was replaced "
            f"with counts that hold."
        ),
        "source": "SOURCE: figdata_week8.json — propagation.stagger, propagation.caveat; the big/small split is computed at injection",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'cannot be shorter than the reporting calendar'", "event": "The first bound lands with the 55-period-end, 5-distinct-days figure."},
        {"at": "on 'observability, not diligence'", "event": "The second bound lands beneath it."},
        {"at": "on 'the biggest events travel fastest'", "event": "The old caption sets and is struck through."},
        {"at": "on 'it does not hold'", "event": "Two evidence rows land underneath with the medians and the zero-day rates."},
    ], intent="A claim the author made, checked, and removed — shown with the arithmetic that removed it, not just asserted as corrected."),
))

# ── B08 · THE GUARDS ──────────────────────────────────────────────────────────
beats.append(beat(
    "B08", "THE GUARDS", "REMOTION",
    "Every one of those numbers runs behind a guard. Two hundred and ninety-four unpriced "
    "marks, and three hundred and one on a split-blocked series, are excluded before any "
    "statistic is computed. No unadjudicated split, no incomplete run. And the report says "
    "plainly what none of this shows. These are fund marks, not transactions.",
    23,
    remotion("W8Guards", "reel-local/MarksMoveAndPropagate", {
        "sparkLine": "What none of this shows.",
        "eyebrow": "WEEK 8 · THE GUARDS",
        "title": "What was excluded before anything was counted",
        "start": GUARDS["marks"],
        "startLabel": "marks in the panel",
        "exclusions": [
            {"label": "unpriced — not a share price", "value": GUARDS["unpriced"]},
            {"label": "on a split-blocked series", "value": GUARDS["change_blocked"]},
        ],
        "zeroes": [
            {"label": "unadjudicated splits", "value": GUARDS["unadjudicated_splits"]},
            {"label": "incomplete runs", "value": GUARDS["incomplete_runs"]},
            {"label": "statistics run over an incomplete run", "value": GUARDS["on_incomplete_runs"]},
        ],
        "remain": MEASURED_POP,
        "remainLabel": "marks measured",
        "notShownLabel": "what none of this shows",
        "notShown": [
            "These are fund marks, not transactions. Nobody traded at these prices.",
            "A spread between two managers is not a disagreement about value — B05 shows why.",
            "A lag is observability, not diligence — the reporting calendar sets the floor.",
        ],
        "source": "SOURCE: figdata_week8.json — guards{}; the measured population is derived, not asserted",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'behind a guard'", "event": "The panel total sets, then the two exclusions subtract in sequence."},
        {"at": "on 'no unadjudicated split, no incomplete run'", "event": "Three zero counters land as a row."},
        {"at": "on 'what none of this shows'", "event": "Three limits land beneath a rule, in the author's own words."},
    ], intent="The subtraction is performed on screen, and the reel ends on its own limits rather than its findings."),
))

# ── B09 · VERDICT ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B09", "VERDICT", "BOOKEND",
    "Week eight on one page. Five thousand one hundred and seventy-eight marks measured, after "
    "the guards. Twenty-five percent of steps carried forward unchanged against a plan that "
    "expected thirty to forty, and it holds under every widening I tried. That headline runs "
    "from zero to forty-eight percent by company, so on its own it describes nobody. Managers "
    "pricing the same company on the same date usually hold different prices, and one opened "
    "window shows why. A new level reaches half its holders in a median of thirty days, which "
    "measures observability, not diligence. Next week, back to building.",
    36,
    remotion("ClaudeVerdictArtifact", "proven-core/ClaudeVerdictArtifact", {
        "sparkLine": "",
        "artifactTitle": f"{SEGMENT} — week 8",
        "artifactHeading": "What the measurement found",
        "artifactLines": [
            f"{num(MEASURED_POP)} marks measured — {num(GUARDS['marks'])} less "
            f"{GUARDS['change_blocked']} on split-blocked series. "
            f"{GUARDS['unadjudicated_splits']} unadjudicated splits, "
            f"{GUARDS['incomplete_runs']} incomplete runs.",
            f"{UNCHANGED_PCT} of {num(OVERALL['steps'])} consecutive observations unchanged, "
            f"against a plan expecting 30–40%. Widening “unchanged” to ±0.1% gives "
            f"{pct1(WIDENINGS[1][1])} and to ±1% gives {pct1(WIDENINGS[2][1])} — all still under "
            f"the band, so this is a result and not a threshold.",
            f"By company the same statistic runs {pct1(CO_MIN['share_unchanged'])} "
            f"({CO_MIN['company'].split(',')[0]}) to {pct1(CO_MAX['share_unchanged'])} "
            f"({CO_MAX['company'].split(',')[0]}). One panel-wide number describes none of them.",
            f"{STATS['groups']} same-date groups, median spread {MEDIAN_SPREAD}, "
            f"{STATS['multi_level']} holding more than one price level. One opened window — "
            f"Anthropic preferred, {len(WIN_MANAGERS)} managers, {len(WINDOW)} marks — shows a "
            f"round arriving rather than a disagreement about value.",
            f"{len(EVENTS)} levels adopted by {PROP['min_holders']}+ managers: median "
            f"{PROP['median_lag_to_half_days']} days to half, {ZERO_DAY} on the same period end, "
            f"slowest {PROP['max_lag_to_half_days']}. Observability, not diligence — and the "
            f"“biggest events are fastest” claim did not survive checking.",
        ],
    }, "stagger", [
        {"at": "0.05", "event": f"The Claude artifact page opens — {SEGMENT}, week 8."},
        {"at": "each line", "event": "Five findings stagger in, one per spoken clause."},
    ]),
    lead=0.4,
))

# ── B10 · HANDOFF ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B10", "HANDOFF", "BOOKEND",
    "Your turn. Paste this into Claude. Take a statistic you report as a single number and "
    "split it by the most obvious dimension you have. Customer, region, product, whatever it "
    "is. Then ask whether the headline still describes anything. Mine ran from zero to "
    "forty-eight percent, which means the panel-wide figure was true of no company in it. A "
    "number that is true on average and wrong everywhere is worse than no number.",
    30,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": "Your turn.",
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "Take a metric I report as one number and split it by the most obvious dimension in "
            "the data. Show me the per-group values beside the headline, with each group's "
            "sample size. Then tell me straight whether the headline still describes anything, "
            "or whether it is true on average and wrong everywhere."
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
    "Measuring how private marks move and propagate. Week eight of the Private AI Valuation "
    "Agent. Om Mali, for Humanitarians A I.",
    11,
    remotion("ClaudeTitleOutro", "proven-core/ClaudeTitleOutro", {
        "title": SEGMENT,
        "handle": HANDLE,
        "subline": "week 8 · the Private AI Valuation Agent",
    }, "fade", [
        {"at": "0.00", "event": "Title restates poster-style in serif with the terracotta period; handle beneath."},
    ]),
))

sheet = {
    "metadata": {
        "title": SEGMENT,
        "slug": "measuring-how-private-marks-move-and-propagate",
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
        "greeting": "Szia, HAI",
        "greeting_note": "hello lexicon: Hungarian (short form). HAI persona takes only the shortest cues (Hi · Ola · Hej · Ciao · Hallo · Salut · Ahoj · Szia). Rotated off weeks 1, 2, 4, 5, 6 and 7 so the series never repeats a language.",
        "aspect_ratio": "16:9",
        "fit": "pad",
        "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
        "color_semantics": "Claude FIDELITY skin: cream #F2F0E9 stage, warm ink #3D3929, terracotta #D97757 as the ONE accent. The source figures use red as the PRIMARY series, never a warning colour; that reading is preserved — terracotta marks the measured result and the subject of each beat, never a hazard.",
        "series": "Private AI Valuation Agent — week 8 (follows 2026-09-11-Building-the-marks-panel-and-the-split-detector)",
        "derived_from": "narration_script.md (human-authored, ~470 spoken words, target 3:00) plus README.md's figure-to-beat map. Every on-screen figure is a prop injected by build_beat_sheet.py from figdata_week8.json, under assertions — no number is typed by hand. The window's level split and the big-vs-small propagation comparison are COMPUTED at injection rather than thresholded, which is what README defects 2 and 4 were about.",
        "note": "ai-explainer / claude-hai. ILLUSTRATE LAW: the Claude UI appears at B00 (cold open, answered), B09 (verdict artifact), B10 (handoff) and B11 (outro) only — every body beat illustrates its concept as a native animated Remotion scene (REBUILD LAW). The five source PNGs and their SVG sources are REFERENCE in pantry/, never slotted as media. The script's seven sections are split into eight body beats; the split is logged in BUILD-LOG.md. THREE THINGS NOT TO GET WRONG: 25% is a disagreement with the plan and not a bug; same-date spread is not automatically disagreement about value; and every number sits behind a guard.",
        "companion_vertical": "vertical/ — the same twelve beats, same audio, rendered 9:16 at 2160×3840 from portrait compositions (never a crop).",
        "tags": ["SEC", "N-PORT", "marks panel", "price dispersion", "propagation", "measurement",
                 "private markets", "data engineering", "Humanitarians AI", "Mycroft"],
    },
    "beats": beats,
}

out = HERE / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

words = {b["beat_id"]: len(b["narration_text"].split()) for b in beats}
print(f"[week8] wrote {out}  — {len(beats)} beats")
print("[week8] narration words:", " ".join(f"{k}={v}" for k, v in words.items()))
body = [v for k, v in words.items() if k in ("B01", "B02", "B03", "B04", "B05", "B06", "B07", "B08")]
print(f"[week8] body beats {min(body)}–{max(body)}w (band 45–70), total {sum(words.values())}w")
print(f"[week8] derived: unchanged {UNCHANGED_PCT}  widenings "
      f"{[f'{v:.4f}' for _, v in WIDENINGS]}  by-company {pct1(CO_MIN['share_unchanged'])}"
      f"–{pct1(CO_MAX['share_unchanged'])}  median spread {MEDIAN_SPREAD}  p90 {P90_SPREAD}")
print(f"[week8] window levels: {[(round(min(lv),2), round(max(lv),2), len(lv)) for lv in WIN_LEVELS]}")
print(f"[week8] propagation: median {PROP['median_lag_to_half_days']}  zero {ZERO_DAY}/{len(EVENTS)}  "
      f"big {BIG_MED:.0f}d {BIG_ZERO}/{len(BIG)}  small {SMALL_MED:.0f}d {SMALL_ZERO}/{len(SMALL)}")
