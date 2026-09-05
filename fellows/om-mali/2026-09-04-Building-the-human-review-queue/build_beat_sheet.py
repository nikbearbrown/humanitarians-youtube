#!/usr/bin/env python3
"""
build_beat_sheet.py — week 6, Building the Human Review Queue.

Writes beat_sheet.json with EVERY on-screen figure injected from figdata_week6.json.
No number is typed into a scene or a beat sheet by hand.

The assertions below exist for the same reason weeks 4 and 5 had them, and this week the
README names three numbers the PROSE got wrong before the figures were generated: four
split questions instead of three (so "wrong three times out of four" instead of two out of
three), Perplexity's unchanged value rounded to the dollar, and the X.AI list missing the
security titles that distinguish three otherwise-identical rows. All three are asserted
here, so the build fails rather than the video quietly repeating a corrected error.

Usage:  python build_beat_sheet.py            (writes beat_sheet.json)
        python build_beat_sheet.py --check    (assertions only, writes nothing)
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIG = json.loads((HERE / "figdata_week6.json").read_text(encoding="utf-8"))

# ── the source of truth ───────────────────────────────────────────────────────
HOLDINGS = FIG["holdings"]
DECIDED = FIG["decided"]
AUTO = FIG["auto_holdings"]
HUMAN = FIG["human_holdings"]
BY_METHOD = FIG["by_method"]
BY_TRIGGER = FIG["by_trigger"]
GROUPS = FIG["review_groups"]
XAI = FIG["xai_spellings"]
PERP = FIG["perplexity"]
SPACEX = FIG["spacex_same_day"]
ANTH_STEP = FIG["anthropic_step"]
ANTH_SERIES = FIG["anthropic_series"]
REJECTED = FIG["rejected"]

# ── assertions: the build fails rather than the video lying ───────────────────
assert DECIDED == HOLDINGS == 5806, "every holding has a decision"
assert AUTO + HUMAN == HOLDINGS, "auto + human must account for every holding"
assert AUTO == 4537 and HUMAN == 1269, "78/22 split"
assert sum(t["holdings"] for t in BY_TRIGGER if t["trigger"] != "auto") == HUMAN, \
    "the non-auto triggers must sum to the human share"

assert len(GROUPS) == 8, "eight questions — this is the beat"
assert sum(g["cards"] for g in GROUPS) == FIG["review_cards"] == 42, "42 cards"
assert sum(g["holdings"] for g in GROUPS) == HUMAN, "the groups cover every human holding"
assert FIG["review_rows"] == 45, "45 recorded decisions, each with a name and a reason"

SPLITS = [g for g in GROUPS if g["trigger"] == "split"]
assert len(SPLITS) == 3, \
    "THREE suspected-split questions, not four — the README records the prose saying four"
assert sum(g["cards"] for g in SPLITS) == 9 and sum(g["holdings"] for g in SPLITS) == 925, \
    "9 cards, 925 holdings across the three split questions"

assert len(XAI) == 24, "X.AI arrives under 24 spellings"
assert sum(x["holdings"] for x in XAI) == 278, "and 278 holdings between them"
assert len({x["name"] for x in XAI}) < len(XAI), \
    "some spellings share an issuer name and differ only by security title — the titles " \
    "must be carried or three rows render identically and read as a data error"

assert len(PERP) == 2, "one split, two period ends"
_a, _b = PERP
assert _b["balance"] == _a["balance"] * 10, "ten times the shares"
assert _a["value_usd"] == _b["value_usd"] == 4228993.75, \
    "the same dollars TO THE CENT — an earlier query rounded this and lost the point"

assert len(SPACEX) == 2 and {r["asset_category"] for r in SPACEX} == {"EC", "EP"}, \
    "SpaceX's ten-times step is common vs preferred on the SAME DAY, not a split"
assert SPACEX[0]["period_end"] == SPACEX[1]["period_end"], "same day"
assert sum(r["holdings"] for r in REJECTED) == 28, "the canary: 28 holdings, not in the universe"

if "--check" in sys.argv:
    print("[week6] all assertions pass")
    sys.exit(0)

# ── derived, never typed ──────────────────────────────────────────────────────
AUTO_PCT = round(AUTO / HOLDINGS * 100, 1)          # 78.1
HUMAN_PCT = round(HUMAN / HOLDINGS * 100, 1)        # 21.9
XAI_GROUP = next(g for g in GROUPS if g["company"] == "X.AI Corp")
SPACEX_EC = next(r for r in SPACEX if r["asset_category"] == "EC")
SPACEX_EP = next(r for r in SPACEX if r["asset_category"] == "EP")
SPACEX_RATIO = round(SPACEX_EP["price"] / SPACEX_EC["price"])
ANTH_FROM, ANTH_TO = ANTH_STEP
WRONG_OF = f"{len(SPLITS) - 1} times out of {len(SPLITS)}"   # "2 times out of 3"

HANDLE = "@HumanitariansAI"
SEGMENT = "Building the Human Review Queue"
KICKER = "Irreducibly Human"     # GATE L rule 7 — the FIXED claude-hai series name

money = lambda v: "$" + f"{v:,.2f}"
num = lambda v: f"{v:,}"


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
    "Hi, I'm Om Mali. This video is about the human review queue I built this week, the part "
    "of the pipeline that knows when to stop and ask a person. The project turns S E C filings "
    "into share prices for private companies. The hard part was never the arithmetic. It is "
    "working out which company a filing is actually talking about.",
    22,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": "Salut, HAI",
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "Build me a review queue for the matcher: resolve what it can, stop at what it "
            "cannot, group the questions so I answer each one once, and hold a paused question "
            "in Postgres so it survives the process exiting."
        ),
        "runningText": "draining the queue…",
        "folderLabel": HANDLE,
        "modelLabel": "Opus 5",
        "effortLabel": "High",
        "output": [
            f"{num(HOLDINGS)} holdings — {num(AUTO)} resolved unaided ({AUTO_PCT}%)",
            f"{num(HUMAN)} stopped and waited: {FIG['review_cards']} cards, "
            f"{len(GROUPS)} actual questions",
            f"{FIG['review_rows']} decisions recorded, every one with a name and a reason",
        ],
    }, "type-on", [
        {"at": "0.00", "event": "Cream Claude composer, empty. Serif greeting 'Salut, HAI' + terracotta spark above it."},
        {"at": "0.15", "event": "The ask types itself into the composer, character by character."},
        {"at": "0.60", "event": "Send button arms terracotta; running indicator reads 'draining the queue…'."},
        {"at": "0.75", "event": "Three output lines land in sequence — the ask arrives ANSWERED (COLD OPEN LAW)."},
    ]),
))

# ── B01 · EXECUTIVE SUMMARY ───────────────────────────────────────────────────
beats.append(beat(
    "B01", "EXECUTIVE SUMMARY", "REMOTION",
    "Here is the whole week in one line. The matcher resolved seventy-eight percent of the "
    "holdings on its own, and on the rest it refused to guess. Those stopped and waited for a "
    "person. Nothing was dropped for being difficult. And nothing here was decided by a model. "
    "It routed, it grouped, it presented. Every decision carries my name and a written reason.",
    24,
    remotion("W6Bluf", "reel-local/BuildingTheHumanReviewQueue", {
        "sparkLine": "It stops, and it asks.",
        "headline": "It refuses to guess.",
        "halves": [
            {"kicker": "RESOLVED UNAIDED", "value": f"{AUTO_PCT}%", "sub": f"{num(AUTO)} holdings — registered identifier or a name already known"},
            {"kicker": "STOPPED AND WAITED", "value": f"{HUMAN_PCT}%", "sub": f"{num(HUMAN)} holdings — routed to a person, none dropped"},
        ],
        "chain": ["route", "group", "present"],
        "chainNote": "What the software did.",
        "verdictLabel": "What it did NOT do",
        "verdict": "decide",
        "rule": (
            f"All {FIG['review_rows']} recorded decisions carry a human name and a written "
            f"reason. The code rejects a decision missing either."
        ),
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'refused to guess'", "event": "Headline sets in serif at display size."},
        {"at": "on 'seventy-eight percent'", "event": "Two halves land: 78.1% resolved, 21.9% stopped, the human share in terracotta."},
        {"at": "on 'it routed, it grouped, it presented'", "event": "Three verb chips land in sequence."},
        {"at": "on 'nothing here was decided'", "event": "A fourth chip, 'decide', lands and is struck through."},
        {"at": "on 'my name and a written reason'", "event": "The rule lands across the foot."},
    ], intent="The BLUF and the week's one claim: the split of the work, and the verb the software never performed."),
))

# ── B02 · THE FUNNEL ──────────────────────────────────────────────────────────
beats.append(beat(
    "B02", "WHAT STOPPED", "REMOTION",
    "Five thousand eight hundred and six holdings. The matcher resolved four thousand five "
    "hundred and thirty-seven of them on its own, off a registered identifier or a name it "
    "already knew. Twelve hundred and sixty-nine stopped. Most of those were suspected stock "
    "splits. Three hundred were companies not yet admitted to the published universe. "
    "Twenty-eight belonged to nothing at all.",
    26,
    remotion("W6Funnel", "reel-local/BuildingTheHumanReviewQueue", {
        "sparkLine": "Nothing was dropped for being difficult.",
        "eyebrow": "WEEK 6 · WHAT STOPPED",
        "title": "Where each one went",
        "subtitle": "one bar, split by what decided it",
        "total": HOLDINGS,
        "totalLabel": "holdings",
        "segments": [
            {"label": "resolved unaided", "value": AUTO, "hot": False},
            {"label": "stopped for a person", "value": HUMAN, "hot": True},
        ],
        "pctLabel": f"{AUTO_PCT}% / {HUMAN_PCT}%",
        "triggers": [
            {"label": t["trigger"].replace("_", " "), "value": t["holdings"]}
            for t in BY_TRIGGER if t["trigger"] != "auto"
        ],
        "triggerLabel": "why it stopped",
        "methods": [
            {"label": m["method"], "holdings": m["holdings"], "questions": m["questions"]}
            for m in BY_METHOD
        ],
        "methodLabel": "how it was finally decided",
        "decidedNote": f"{num(DECIDED)} of {num(HOLDINGS)} decided. Nothing dropped, nothing pending.",
        "source": "SOURCE: figdata_week6.json — queried from the project Postgres at build time",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'five thousand eight hundred and six'", "event": "One full-width bar draws and the total counts up to 5,806."},
        {"at": "on 'resolved four and a half thousand'", "event": "The bar splits: 4,537 in ink, 1,269 in terracotta."},
        {"at": "on 'most of those were suspected splits'", "event": "The terracotta segment fans out into its four triggers."},
        {"at": "on 'nothing at all'", "event": "The 28-holding sliver lights last."},
    ], intent="Rebuild of pantry/w6-funnel.png. The terracotta segment is the subject of the week, so the bar splits before it fans."),
))

# ── B03 · FORTY-TWO CARDS, EIGHT QUESTIONS ────────────────────────────────────
beats.append(beat(
    "B03", "THE REPETITION", "REMOTION",
    "Now look at what stopped. Forty-two cards, but only eight actual questions. X dot A-I "
    "alone arrives under twenty-four different spellings. Some of them share an issuer name "
    "and differ only in the security title. Asking twenty-four times whether X dot A-I belongs "
    "in the dataset would be absurd.",
    22,
    remotion("W6Collapse", "reel-local/BuildingTheHumanReviewQueue", {
        "sparkLine": "Twenty-four spellings, one company.",
        "eyebrow": "WEEK 6 · THE REPETITION",
        "title": "42 cards, 8 questions",
        "subtitle": "every spelling X.AI Corp arrives under, as filed",
        "cards": FIG["review_cards"],
        "cardsLabel": "cards that stopped",
        "questions": len(GROUPS),
        "questionsLabel": "actual questions",
        "spellings": [
            {"name": x["name"], "title": x["title"], "holdings": x["holdings"]}
            for x in XAI
        ],
        "spellingCount": len(XAI),
        "spellingHoldings": XAI_GROUP["holdings"],
        "spellingNote": (
            f"{len(XAI)} spellings, {XAI_GROUP['holdings']} holdings, one company. Rows sharing "
            f"an issuer name differ only in the security title."
        ),
        "source": "SOURCE: figdata_week6.json — xai_spellings, name AND title as filed",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'forty-two cards'", "event": "Two counters resolve side by side: 42 cards, 8 questions."},
        {"at": "on 'twenty-four different spellings'", "event": "The real filed strings scroll — the repetition is the point."},
        {"at": "on 'differ only in the security title'", "event": "The rows sharing an issuer name light, with their titles beside them."},
    ], intent="Rebuild of pantry/w6-collapse.png, upper half. Titles are carried because three rows share an issuer name and would otherwise read as a data error."),
))

# ── B04 · THE ANSWER IS RECORDED AGAINST THE COMPANY ──────────────────────────
beats.append(beat(
    "B04", "THE KEY", "REMOTION",
    "So the answer is not recorded against the spelling. It is recorded against the company. "
    "One answer clears all twenty-four at once, and spelling number twenty-five never asks "
    "anyone. That is the difference between a queue that shrinks as you work and one that "
    "grows with every new filing.",
    20,
    remotion("W6Key", "reel-local/BuildingTheHumanReviewQueue", {
        "sparkLine": "Answer the company, not the string.",
        "eyebrow": "WEEK 6 · THE KEY",
        "title": "One answer, twenty-four cards",
        "wrongLabel": "keyed on the spelling",
        "wrongNote": f"{len(XAI)} questions, and a new one with every new filing",
        "rightLabel": "keyed on the company",
        "rightNote": "1 question, and it stays answered",
        "company": XAI_GROUP["company"],
        "verdict": XAI_GROUP["verdict"].replace("_", " "),
        "clears": len(XAI),
        "clearsLabel": "cards cleared by one answer",
        "nextLabel": f"spelling {len(XAI) + 1}",
        "nextNote": "arrives already answered — it never reaches a person",
        "keysNote": (
            f"{FIG['company_level_keys']} of the {len(GROUPS)} questions are keyed at company "
            f"level; the rest are single cards."
        ),
        "source": "SOURCE: figdata_week6.json — review_groups, company_level_keys",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'not recorded against the spelling'", "event": "Twenty-four separate question marks fan out, then dim."},
        {"at": "on 'recorded against the company'", "event": "They collapse into ONE card carrying the company and its verdict."},
        {"at": "on 'clears all twenty-four'", "event": "Twenty-four ticks fill from the single answer."},
        {"at": "on 'spelling number twenty-five'", "event": "A 25th card arrives already ticked and never enters the queue."},
    ], intent="The mechanism, not the tally: the same 24 strings resolve to one key, and the next one arrives pre-answered."),
))

# ── B05 · DURABILITY ──────────────────────────────────────────────────────────
beats.append(beat(
    "B05", "DURABILITY", "REMOTION",
    "The other half of this is durability. When the graph stops, it writes its entire state "
    "into Postgres. The process can exit. I tested that by pausing the graph in one process "
    "and answering the question in a completely separate one. The queue did not notice the "
    "difference.",
    20,
    remotion("W6Durability", "reel-local/BuildingTheHumanReviewQueue", {
        "sparkLine": "The process can exit.",
        "eyebrow": "WEEK 6 · DURABILITY",
        "title": "Where a paused question lives",
        "nodes": ["ingest", "match", "interrupt()", "resume", "commit"],
        "haltAt": 2,
        "haltLabel": "the graph stops here",
        "storeLabel": "Postgres",
        "storeNote": "the entire graph state, written on halt",
        "procA": {"label": "process A", "note": "paused the graph, then exited"},
        "procB": {"label": "process B", "note": "answered the question, resumed the graph"},
        "proof": "Two processes, one queue. Nothing was held in memory between them.",
        "source": ("SOURCE: the author's own run log. This beat is the one part of the reel "
                   "NOT evidenced by figdata_week6.json — see FACTCHECK rows 10 and 11."),
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'when the graph stops'", "event": "Five nodes draw left to right; the third halts and takes the accent."},
        {"at": "on 'writes its entire state into Postgres'", "event": "An arrow drops from the halted node into a Postgres cylinder."},
        {"at": "on 'in one process'", "event": "Process A appears above the store, then greys out and exits."},
        {"at": "on 'a completely separate one'", "event": "Process B appears below, reads the same store and resumes the graph."},
    ], intent="Rebuild of pantry/w6-durability.png. The two processes must be visibly separate, with only the store between them."),
))

# ── B06 · THE CRASH ───────────────────────────────────────────────────────────
beats.append(beat(
    "B06", "THE UNPLANNED TEST", "REMOTION",
    "Then I got a second test I did not ask for. The database server crashed. When it came "
    "back, all forty-two questions were still sitting there, exactly as they were. That is the "
    "part I would not have thought to test, and it is the part that actually matters.",
    19,
    remotion("W6Crash", "reel-local/BuildingTheHumanReviewQueue", {
        "sparkLine": "It came back whole.",
        "eyebrow": "WEEK 6 · THE UNPLANNED TEST",
        "before": {"label": "before", "value": FIG["review_cards"], "note": "questions waiting"},
        "event": "the database server crashed",
        "eventNote": "not a drill, and not part of the plan",
        "after": {"label": "after", "value": FIG["review_cards"], "note": "questions waiting, unchanged"},
        "verdict": "Nothing was in memory to lose.",
        "caveat": (
            "One unplanned outage is not a durability guarantee. It is the only test of this "
            "kind that has been run, and it was run by accident."
        ),
        "source": ("SOURCE: figdata_week6.json — review_cards = 42. The before/after identity is "
                   "the author's observation of one outage, not two recorded snapshots "
                   "(FACTCHECK row 12)."),
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'a second test I did not ask for'", "event": "42 question marks sit in a settled block."},
        {"at": "on 'the database server crashed'", "event": "The frame cuts to a hard rule; the block goes dark."},
        {"at": "on 'when it came back'", "event": "The identical block returns, counted again to 42."},
        {"at": "on 'exactly as they were'", "event": "The caveat lands beneath — one accident is not a guarantee."},
    ], intent="The script calls this the strongest beat. The count must be shown to be the SAME number, not asserted to be."),
))

# ── B07 · THE SPLIT ───────────────────────────────────────────────────────────
beats.append(beat(
    "B07", "WHAT IT CAUGHT", "REMOTION",
    "And here is what that bought. Perplexity's share count went from six thousand and "
    "eighty-one to sixty thousand eight hundred and ten, while the dollar value stayed the "
    "same, to the cent. That is a ten for one stock split. Priced naively it would have "
    "entered my price history as a ninety percent crash.",
    22,
    remotion("W6Split", "reel-local/BuildingTheHumanReviewQueue", {
        "sparkLine": "Ten times the shares. The same dollars.",
        "eyebrow": "WEEK 6 · WHAT IT CAUGHT",
        "title": "A split, not a crash",
        "company": PERP[0].get("company", "Perplexity AI, Inc."),
        "rows": [
            {
                "period": r["period_end"],
                "balance": r["balance"],
                "value": r["value_usd"],
                "price": r["price"],
            } for r in PERP
        ],
        "balanceLabel": "shares",
        "valueLabel": "filed value",
        "priceLabel": "implied price",
        "unchanged": money(PERP[0]["value_usd"]),
        "unchangedLabel": "unchanged, to the cent",
        "ratio": f"{int(PERP[1]['balance'] // PERP[0]['balance'])} for 1",
        "ratioLabel": "stock split",
        "naive": f"−{round((1 - PERP[1]['price'] / PERP[0]['price']) * 100)}%",
        "naiveLabel": "what a naive price series would have recorded",
        "source": "SOURCE: figdata_week6.json — perplexity, both period ends as filed",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'six thousand and eighty-one'", "event": "The first row lands: shares, filed value, implied price."},
        {"at": "on 'sixty thousand eight hundred and ten'", "event": "The second row lands beneath, share count ten times larger."},
        {"at": "on 'to the cent'", "event": "The two filed values are bracketed as identical, shown to the cent."},
        {"at": "on 'ninety percent crash'", "event": "The naive reading lands struck through in terracotta."},
    ], intent="Rebuild of pantry/w6-split.png, first row. The unchanged dollar value is the evidence, so it is bracketed rather than stated."),
))

# ── B08 · SAME SHAPE, THREE CAUSES ────────────────────────────────────────────
beats.append(beat(
    "B08", "THREE CAUSES", "REMOTION",
    "Three price steps tripped the same split detector. Only one was a split. SpaceX's ten "
    "times step is the same fund reporting common stock at eighty-one dollars and preferred at "
    "eight hundred and ten, on the same day. Anthropic's is an ordinary funding round, four "
    "times up over one quarter. One trigger, three different causes. A detector that treated "
    "them alike would be wrong two times out of three.",
    26,
    remotion("W6ThreeCauses", "reel-local/BuildingTheHumanReviewQueue", {
        "sparkLine": "One trigger. Three causes.",
        "eyebrow": "WEEK 6 · THREE CAUSES",
        "title": "One trigger, three different things",
        "subtitle": "every price step the split detector flagged — and what each one really was",
        "cases": [
            {
                "company": "Perplexity AI, Inc.",
                "shape": f"×{int(PERP[1]['balance'] // PERP[0]['balance'])} shares",
                "cause": "a real 10-for-1 stock split",
                "evidence": f"filed value identical at {money(PERP[0]['value_usd'])}",
                "real": True,
            },
            {
                "company": "Space Exploration Technologies Corp.",
                "shape": f"×{SPACEX_RATIO} price",
                "cause": "not a split — two share classes",
                "evidence": (
                    f"same fund, same day ({SPACEX_EC['period_end']}): common "
                    f"${SPACEX_EC['price']:,.0f} vs preferred ${SPACEX_EP['price']:,.0f}"
                ),
                "real": False,
            },
            {
                "company": "Anthropic PBC",
                "shape": f"×{round(ANTH_TO['price'] / ANTH_FROM['price'], 1)} price",
                "cause": "not a split — an ordinary funding round",
                "evidence": (
                    f"${ANTH_FROM['price']:,.2f} on {ANTH_FROM['period_end']} to "
                    f"${ANTH_TO['price']:,.2f} on {ANTH_TO['period_end']}"
                ),
                "real": False,
            },
        ],
        "realLabel": "a split",
        "notRealLabel": "not a split",
        "verdict": f"A detector that treated them alike would be wrong {WRONG_OF}.",
        "correction": (
            f"{len(SPLITS)} split questions, {sum(g['cards'] for g in SPLITS)} cards, "
            f"{sum(g['holdings'] for g in SPLITS)} holdings. An earlier write-up said four "
            f"questions and three-in-four; counted from the database it is "
            f"{len(SPLITS)} and {WRONG_OF}."
        ),
        "source": "SOURCE: figdata_week6.json — perplexity, spacex_same_day, anthropic_step",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'tripped the same split detector'", "event": "Three step glyphs land in a row, each labelled with its own magnitude."},
        {"at": "on 'only one was a split'", "event": "The first takes the accent and is labelled a split."},
        {"at": "on 'common at eighty-one, preferred at eight hundred and ten'", "event": "The second reveals its real cause beneath it."},
        {"at": "on 'an ordinary funding round'", "event": "The third reveals its cause."},
        {"at": "on 'wrong two times out of three'", "event": "The verdict lands across the foot, with the corrected count."},
    ], intent="Rebuild of pantry/w6-split.png, all three rows. The magnitudes DIFFER (x10, x10, x4.0) and are labelled as such; what the three share is the detector that flagged them, not their shape."),
))

# ── B09 · VERDICT ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B09", "VERDICT", "BOOKEND",
    "Week six on one page. Five thousand eight hundred and six holdings, every one of them "
    "decided. Seventy-eight percent by the matcher, the rest by a person. Forty-two cards "
    "collapsed into eight questions, because the answer is recorded against the company. A "
    "paused question lives in Postgres, and survived a crash nobody planned. And each decision "
    "is now a test, so a future change to the matcher cannot quietly overturn a judgment I "
    "already made.",
    32,
    remotion("ClaudeVerdictArtifact", "proven-core/ClaudeVerdictArtifact", {
        "sparkLine": "",
        "artifactTitle": f"{SEGMENT} — week 6",
        "artifactHeading": "What the queue does",
        "artifactLines": [
            f"{num(HOLDINGS)} holdings, {num(DECIDED)} decided. {num(AUTO)} ({AUTO_PCT}%) "
            f"resolved unaided; {num(HUMAN)} ({HUMAN_PCT}%) stopped and waited. None dropped.",
            f"{FIG['review_cards']} cards collapsed to {len(GROUPS)} questions. The answer is "
            f"keyed on the company, not the spelling — one answer cleared X.AI's {len(XAI)}.",
            f"interrupt() writes the whole graph state to Postgres. Paused in one process, "
            f"answered in another — and it survived an unplanned database outage intact.",
            f"{len(SPLITS)} suspected splits, {sum(g['holdings'] for g in SPLITS)} holdings. "
            f"One was real: Perplexity ×10 shares at {money(PERP[0]['value_usd'])} unchanged. "
            f"Treating all three alike would be wrong {WRONG_OF}.",
            f"{FIG['review_rows']} decisions recorded, each with a human name and a written "
            f"reason — the code rejects one missing either. Each is now a regression test.",
        ],
    }, "stagger", [
        {"at": "0.05", "event": f"The Claude artifact page opens — {SEGMENT}, week 6."},
        {"at": "each line", "event": "Five findings stagger in, one per spoken clause."},
    ]),
    lead=0.4,
))

# ── B10 · HANDOFF ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B10", "HANDOFF", "BOOKEND",
    "Your turn. Paste this into Claude. Take any place in your own work where a script gives "
    "up and asks you something. Ask yourself two questions about it. First, is the answer "
    "recorded against the thing you actually decided, or against the string that happened to "
    "arrive? And second, if the process died right now, would the question still be there when "
    "it came back? If either answer is no, you do not have a queue. You have an interruption.",
    31,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": "Your turn.",
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "Find the place in my pipeline where it gives up and asks me something. Help me key "
            "the answer on the entity I actually decided rather than the string that arrived, "
            "and persist the paused state so the question survives the process exiting. Then "
            "tell me what my design still cannot recover from."
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
    "Building the human review queue. Week six of the Private AI Valuation Agent. Next week, "
    "an actual price panel. Om Mali, for Humanitarians A I.",
    12,
    remotion("ClaudeTitleOutro", "proven-core/ClaudeTitleOutro", {
        "title": SEGMENT,
        "handle": HANDLE,
        "subline": "week 6 · the Private AI Valuation Agent",
    }, "fade", [
        {"at": "0.00", "event": "Title restates poster-style in serif with the terracotta period; handle beneath."},
    ]),
))

sheet = {
    "metadata": {
        "title": SEGMENT,
        "slug": "building-the-human-review-queue",
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
        "greeting": "Salut, HAI",
        "greeting_note": "hello lexicon: French (short form). HAI persona takes only the shortest cues (Hi · Ola · Hej · Ciao · Hallo · Salut). Rotated off weeks 1, 2, 4 and 5 so the series never repeats a language.",
        "aspect_ratio": "16:9",
        "fit": "pad",
        "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
        "color_semantics": "Claude FIDELITY skin: cream #F2F0E9 stage, warm ink #3D3929, terracotta #D97757 as the ONE accent. The Mycroft figures use red as the primary series — never 'danger' — marking the human's share of the work; that remaps onto the Claude accent grammar. Palette change only, no data change. Same treatment as weeks 1, 2, 4 and 5.",
        "series": "Private AI Valuation Agent — week 6 (follows 2026-08-28-Measuring-a-local-LLM-against-the-matcher)",
        "derived_from": "narration_script.md (human-authored, 441 spoken words, target 3:00) plus README.md's figure-to-beat map. Every on-screen figure is a prop injected by build_beat_sheet.py from figdata_week6.json, under assertions — no number is typed by hand.",
        "note": "ai-explainer / claude-hai. ILLUSTRATE LAW: the Claude UI appears at B00 (cold open, answered), B09 (verdict artifact), B10 (handoff) and B11 (outro) only — every body beat illustrates its concept as a native animated Remotion scene (REBUILD LAW). The five source PNGs and their SVG sources are REFERENCE in pantry/, never slotted as media. The script's six sections are split into eight body beats so no beat carries two ideas; the split is logged in BUILD-LOG.md. THE CENTRAL CLAIM: the software routed, grouped and presented — it decided nothing.",
        "companion_vertical": "vertical/ — the same twelve beats, same audio, rendered 9:16 at 2160×3840 from portrait compositions (never a crop).",
        "tags": ["SEC", "N-PORT", "human in the loop", "review queue", "LangGraph", "Postgres",
                 "entity resolution", "stock split", "data engineering", "Humanitarians AI", "Mycroft"],
    },
    "beats": beats,
}

out = HERE / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

words = {b["beat_id"]: len(b["narration_text"].split()) for b in beats}
print(f"[week6] wrote {out}  — {len(beats)} beats")
print("[week6] narration words:", " ".join(f"{k}={v}" for k, v in words.items()))
body = [v for k, v in words.items() if k in ("B01", "B02", "B03", "B04", "B05", "B06", "B07", "B08")]
print(f"[week6] body beats {min(body)}–{max(body)}w (band 45–70), total {sum(words.values())}w")
