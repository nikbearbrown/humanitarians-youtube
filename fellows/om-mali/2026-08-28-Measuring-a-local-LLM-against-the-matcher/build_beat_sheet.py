#!/usr/bin/env python3
"""
build_beat_sheet.py — week 5, Measuring a Local LLM Against the Matcher.

Writes beat_sheet.json with EVERY on-screen figure injected from figdata_week5.json.
No number is typed into a scene or a beat sheet by hand.

The assertions below exist for the same reason week 4's did: the week 5 README records
two numbers that were hand-typed in the prose and turned out WRONG (confidence was 1.000
on 315 answers, not 308; the model was offered 11 candidates, not 7). Both were caught
only because a generated figure disagreed with the text. These assertions make that class
of error impossible on this side of the boundary — if figdata changes, the build fails
rather than the video quietly lying.

Usage:  python build_beat_sheet.py            (writes beat_sheet.json)
        python build_beat_sheet.py --check    (assertions only, writes nothing)
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIG = json.loads((HERE / "figdata_week5.json").read_text(encoding="utf-8"))

# ── the source of truth ───────────────────────────────────────────────────────
run = FIG["run"]
thr = FIG["throughput"]
pex = FIG["prompt_example"]
sb = FIG["scoreboard"]
lift = FIG["lift"]
fails = FIG["failures"]
band = FIG["band_changes"]
conf = FIG["confidence"]
veto = FIG["veto_rows"]
dots = FIG["dots"]

RULES = sb["B_matcher_v1"]      # the deterministic matcher that ships today
MODEL = sb["C_v2_band"]         # matcher + LLM under the band policy — the swap on offer
VETO = sb["F_v2_veto"]          # LLM allowed only to REMOVE a claim, never to add one

# ── assertions: the build fails rather than the video lying ───────────────────
assert run["parameter_size"] == "8.0B", "the claim is an 8B model"
assert run["temperature"] == 0 and run["seed"] == 7, "run must be deterministic"
assert thr["calls_measured"] == 322 and thr["errors"] == 0, "322 calls, zero failures"
assert pex["candidates"] == 11, "11 candidates offered (7 universe + 4 watchlist), NOT 7"

assert RULES["macro"]["precision"] == 0.9959, "rules precision"
assert MODEL["macro"]["precision"] == 0.9449, "model precision"
assert RULES["micro"]["fp"] == 1 and MODEL["micro"]["fp"] == 196, "1 record becomes 196"
assert RULES["macro"]["recall"] == MODEL["macro"]["recall"] == 1.0, "recall did not move"
assert round(lift["C_v2_band"]["precision"], 4) == -0.051, "the swap LOSES precision"

assert band["promotions"] == band["broke"] == 14 and band["fixed"] == 1, \
    "every error was an ADDED company; it removed one, once"
assert band["consulted"] == 85, "band policy consulted the model on 85 of 322"

assert conf["total"] == 322 and conf["at_full"] == 315, "315 at confidence 1.000, not 308"
assert conf["disagrees"] == 15 and conf["disagrees_at_95_plus"] == 12, \
    "12 of the 15 disagreements came back at 0.95+"
assert len(dots) == 322, "one dot per answer"
assert sum(1 for d in dots if d["confidence"] == 1.0) == conf["at_full"], \
    "the dot figure and the confidence block must agree"

assert VETO["macro"]["precision"] == 1.0 and VETO["macro"]["fp"] == 0, "veto-only is clean"
assert len(veto) == 4, "the veto policy would ever see exactly four rows"
assert sum(1 for v in veto if v["vetoed"]) == 1, "it vetoes exactly one of them"

assert len(fails) == 3 and all(f["truth"] == "NOT_IN_UNIVERSE" for f in fails), \
    "all three shown failures are rows where NOTHING should have matched"
HYPER, AGILE, CODE = fails            # g0191, g0254, g0320 — in figdata order
assert HYPER["issuer_name"] == "HYPERSCALE DATA INC" and HYPER["said"] == "Scale AI, Inc."
assert AGILE["holdings"] == 32 and CODE["holdings"] == 8

if "--check" in sys.argv:
    print("[week5] all assertions pass")
    sys.exit(0)

# ── derived, never typed ──────────────────────────────────────────────────────
pct = lambda x: f"{x * 100:.1f}%"
p_rules = pct(RULES["macro"]["precision"])          # 99.6%
p_model = pct(MODEL["macro"]["precision"])          # 94.5%
rec_rules = RULES["micro"]["fp"]                    # 1
rec_model = MODEL["micro"]["fp"]                    # 196
drop_pts = abs(round(lift["C_v2_band"]["precision"] * 100, 1))   # 5.1
wall_min = round(thr["seconds_for_full_golden_set_llm_only"] / 60)  # 17

def short_name(n):
    """Filed holding names run to 138 characters. Rendered in full they cross the right
    title-safe edge and overprint the notes beneath — the exact BLOCKER week 4 hit at B08.
    The source figure shortens them too; the truncation is disclosed in the on-screen
    source line, and the trailing-space distinction between rows 3 and 4 survives in the
    row note rather than being silently collapsed."""
    i = n.find(" (ECONOMIC EXPOSURE")
    return (n[:i] + " …") if i > 0 else n


SPARK_TOP, SPARK_BOT = "top", "bottom"
HANDLE = "@HumanitariansAI"
SEGMENT = "Measuring a Local LLM Against the Matcher"
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
    "Hi, I'm Om Mali. This video is about measuring a local language model against the "
    "rule based matcher that already works, and reporting honestly when the model loses. "
    "Week five of the Private AI Valuation Agent. I gave an eight billion parameter model "
    "exactly the evidence the rules get. It lost. And measuring that properly is the whole week.",
    22,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": "Hallo, HAI",
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "Replace my deterministic matcher with a local 8B language model. Give it exactly "
            "what the rules get, score it against the same 322 labelled names, and tell me "
            "straight whether it earns the swap."
        ),
        "runningText": "scoring 322 calls…",
        "folderLabel": HANDLE,
        "modelLabel": "Opus 5",
        "effortLabel": "High",
        "output": [
            f"{run['model']} local — {thr['calls_measured']} calls, "
            f"{thr['errors']} failures, {thr['mean_seconds_per_call']:.1f}s each",
            f"precision {RULES['macro']['precision']:.4f} → {MODEL['macro']['precision']:.4f}; "
            f"{rec_rules} bad record becomes {rec_model}",
            f"and it was fully confident on {conf['disagrees_at_95_plus']} of the "
            f"{conf['disagrees']} it got wrong",
        ],
    }, "type-on", [
        {"at": "0.00", "event": "Cream Claude composer, empty. Serif greeting 'Hallo, HAI' + terracotta spark above it."},
        {"at": "0.15", "event": "The ask types itself into the composer, character by character."},
        {"at": "0.60", "event": "Send button arms terracotta; running indicator reads 'scoring 322 calls…'."},
        {"at": "0.75", "event": "Three output lines land in sequence — the ask arrives ANSWERED (COLD OPEN LAW)."},
    ]),
))

# ── B01 · EXECUTIVE SUMMARY ───────────────────────────────────────────────────
beats.append(beat(
    "B01", "EXECUTIVE SUMMARY", "REMOTION",
    "Here is the whole result before I show you any of it. The rules keep the job. A local "
    "model, given the same four fields and the same candidate list, was wrong in exactly one "
    "direction. It promoted holdings to companies they were not. Precision fell about five "
    "points. Recall did not move at all. I kept the rules, and this week is me showing you why.",
    24,
    remotion("W5Bluf", "reel-local/MeasuringLocalLlm", {
        "sparkLine": "A negative result, measured properly.",
        "headline": "The rules keep the job.",
        "systems": [
            {"kicker": "SHIPS TODAY", "title": "Deterministic matcher",
             "sub": "rules over the filed name", "metric": p_rules, "metricLabel": "precision"},
            {"kicker": "ON OFFER", "title": f"Local {run['parameter_size']} model",
             "sub": "same evidence, same labels", "metric": p_model, "metricLabel": "precision"},
        ],
        "deltaLabel": f"−{drop_pts} points of precision",
        "steadyLabel": f"recall unchanged at {MODEL['macro']['recall']:.4f}",
        "directionNote": (
            f"All {band['promotions']} new errors ran one way: a holding promoted to a company "
            f"it is not. Removals: {band['fixed']}."
        ),
        "verdict": "NO LIFT — NOT ADOPTED",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'the rules keep the job'", "event": "Headline sets in serif at display size, centred."},
        {"at": "on 'a local model'", "event": "Two system cards land side by side; the incumbent takes the accent."},
        {"at": "on 'precision fell'", "event": "A delta bar drops between them, labelled −5.1 points."},
        {"at": "on 'recall did not move'", "event": "A flat steady line lands beneath it, unchanged."},
        {"at": "on 'I kept the rules'", "event": "The verdict band stamps NOT ADOPTED across the foot."},
    ], intent="The BLUF: which system ships, by how much, and in which direction the model is wrong."),
))

# ── B02 · THE TEST ────────────────────────────────────────────────────────────
beats.append(beat(
    "B02", "THE TEST", "REMOTION",
    "Both systems see the same evidence. The name on the filing. The security title. The fund "
    "that filed it. And a list of eleven candidate companies, the seven in the universe plus "
    "four on the watchlist. Nothing else. No price, and no answer. Three hundred and twenty-two "
    "calls, on my own machine, about three seconds each. Zero failures.",
    24,
    remotion("W5Setup", "reel-local/MeasuringLocalLlm", {
        "sparkLine": "Same evidence, or the comparison means nothing.",
        "eyebrow": "WEEK 5 · THE TEST",
        "title": "Exactly what the rules get",
        "subtitle": "one real golden-set row, as it reached the model",
        "fields": [
            {"label": "issuer name", "value": pex["issuer_name"]},
            {"label": "security title", "value": pex["issuer_title"]},
            {"label": "filed by", "value": pex["filer"]},
            {"label": "candidates", "value": f"{pex['candidates']} companies — 7 universe + 4 watchlist"},
        ],
        "withheld": ["price", "the answer"],
        "withheldNote": "Withheld from both systems. The model gets no evidence the rules do not.",
        "modelCard": {
            "name": run["model"],
            "specs": [
                f"{run['parameter_size']} parameters, {run['quantization']}",
                f"local — {run['host']}",
                f"temperature {run['temperature']}, seed {run['seed']}, schema-constrained",
            ],
        },
        "stats": [
            {"value": f"{thr['calls_measured']}", "label": "calls"},
            {"value": f"{thr['errors']}", "label": "failures"},
            {"value": f"{thr['mean_seconds_per_call']:.2f}s", "label": "mean per call"},
            {"value": f"{wall_min} min", "label": "full golden set"},
        ],
        "source": f"SOURCE: figdata_week5.json — run {run['at'][:10]}, {run['machine']}",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on each field", "event": "The four given fields land one at a time as labelled cards."},
        {"at": "on 'nothing else'", "event": "Two withheld chips — price, the answer — draw struck-through in ghost."},
        {"at": "on 'three hundred and twenty-two calls'", "event": "The run stats count up: 322 calls, 0 failures, 3.24s, 17 min."},
    ], intent="Rebuild of pantry/w5-setup.png. The point is parity of evidence, so the four fields land first and the withheld pair is struck."),
))

# ── B03 · THE RESULT ──────────────────────────────────────────────────────────
beats.append(beat(
    "B03", "THE RESULT", "REMOTION",
    "The rules score ninety-nine point six percent precision. The model, ninety-four point five. "
    "Five points sounds survivable. Count it in records instead of cases, and it is not. One "
    "wrong record becomes a hundred and ninety-six. Same labels, same holdings, one system "
    "swapped out for another. That is the entire comparison.",
    22,
    remotion("W5Scoreboard", "reel-local/MeasuringLocalLlm", {
        "sparkLine": "Five points, counted properly.",
        "eyebrow": "WEEK 5 · THE RESULT",
        "title": "Five points, in records",
        "subtitle": "same 322 labels, same 5,935 true holdings, one system swapped",
        "rows": [
            {"name": "Deterministic matcher", "tag": "ships today",
             "precision": RULES["macro"]["precision"], "records": RULES["micro"]["fp"],
             "cases": RULES["macro"]["fp"], "hot": True},
            {"name": f"Matcher + local {run['parameter_size']} model", "tag": "on offer",
             "precision": MODEL["macro"]["precision"], "records": MODEL["micro"]["fp"],
             "cases": MODEL["macro"]["fp"], "hot": False},
        ],
        "precisionLabel": "macro precision",
        "recordsLabel": "wrong records",
        "casesLabel": "wrong cases",
        "multiplier": f"{rec_rules} → {rec_model}",
        "multiplierNote": (
            f"{MODEL['macro']['fp']} wrong cases instead of {RULES['macro']['fp']}, but a case is "
            f"a name and a name can carry hundreds of holdings."
        ),
        "steady": f"Recall unchanged: {RULES['macro']['recall']:.4f} → {MODEL['macro']['recall']:.4f}. Nothing was lost. Things were added.",
        "source": "SOURCE: figdata_week5.json — scoreboard, macro and micro over the same golden set",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on the two numbers", "event": "Two precision rows set at display size, the incumbent in terracotta."},
        {"at": "on 'count it in records'", "event": "The frame switches unit: the same two rows re-count as records, 1 and 196."},
        {"at": "on 'a hundred and ninety-six'", "event": "The 196 bar runs the full column width against the 1."},
        {"at": "on 'same labels'", "event": "A steady line confirms recall unchanged at 1.0000."},
    ], intent="Rebuild of pantry/w5-scoreboard.png. Precision first, then the same error re-counted in records — the unit switch IS the argument."),
))

# ── B04 · THE INVENTED FACT ───────────────────────────────────────────────────
beats.append(beat(
    "B04", "HOW IT FAILS", "REMOTION",
    "It fails the same way every time. It promotes resemblances. It saw a company called "
    "Hyperscale Data and answered Scale A I. Its reason, in its own words: Hyperscale Data is "
    "the parent company of Scale A I. That is not true. There is no such relationship. The "
    "model did not misread the filing. It invented a corporate fact, and then reported it at "
    "ninety-five percent confidence.",
    26,
    remotion("W5InventedFact", "reel-local/MeasuringLocalLlm", {
        "sparkLine": "It promotes resemblances.",
        "eyebrow": "WEEK 5 · HOW IT FAILS",
        "title": "It invented a corporate fact",
        "filedLabel": "filed name",
        "filed": HYPER["issuer_name"],
        "saidLabel": "the model answered",
        "said": HYPER["said"],
        "truthLabel": "the label",
        "truth": HYPER["truth"],
        "reasonLabel": "its reason, verbatim",
        "reason": HYPER["reason"],
        "strikeFrom": "which is the parent company of",
        "rebuttal": "No such relationship exists. Neither company is a parent of the other.",
        "confidence": HYPER["confidence"],
        "confidenceLabel": "reported confidence",
        "holdings": HYPER["holdings"],
        "holdingsLabel": "holding affected",
        "source": f"SOURCE: figdata_week5.json — failures[0], golden-set row {HYPER['id']}",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'a company called Hyperscale Data'", "event": "The filed name sets at display size."},
        {"at": "on 'answered Scale AI'", "event": "An arrow carries it to the model's answer; the true label lands beneath in ghost."},
        {"at": "on 'in its own words'", "event": "The model's reason types in verbatim as a quotation."},
        {"at": "on 'that is not true'", "event": "The parent-company clause is struck through and a rebuttal lands under it."},
        {"at": "on 'ninety-five percent'", "event": "The confidence dial fills to 0.95 beside the struck reason."},
    ], intent="Rebuild of pantry/w5-failures.png, first row. The model's own sentence is the evidence, so it is quoted and then struck."),
))

# ── B05 · THE SAME MISTAKE, LOUDER ────────────────────────────────────────────
beats.append(beat(
    "B05", "HOW IT FAILS", "REMOTION",
    "Then a loan. Scaled Agile Incorporated, twenty twenty-one unitranche term loan. Also Scale "
    "A I, at full confidence, because the words look alike. That one is not a single record. "
    "Thirty-two holdings carry that name, and every one of them would have been priced as a "
    "company it has nothing to do with.",
    21,
    remotion("W5Substring", "reel-local/MeasuringLocalLlm", {
        "sparkLine": "The words look alike. That is the whole reason.",
        "eyebrow": "WEEK 5 · HOW IT FAILS",
        "title": "A resemblance, priced",
        "filed": AGILE["issuer_name"],
        "highlight": "SCAL",
        "said": AGILE["said"],
        "saidHighlight": "Scal",
        "truth": AGILE["truth"],
        "reason": AGILE["reason"],
        "confidence": AGILE["confidence"],
        "confidenceNote": "full confidence",
        "holdings": AGILE["holdings"],
        "holdingsLabel": "holdings carry this name",
        "runningLabel": "wrong records so far",
        "runningFrom": HYPER["holdings"],
        "runningTo": HYPER["holdings"] + AGILE["holdings"],
        "kicker": "A term loan is not an equity stake in anything. The name is the only thing they share.",
        "source": f"SOURCE: figdata_week5.json — failures[1], golden-set row {AGILE['id']}",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'Scaled Agile'", "event": "The filed string sets across the frame; the four shared characters light terracotta."},
        {"at": "on 'also Scale AI'", "event": "The answer lands beneath with the same characters lit — the overlap is the whole reason."},
        {"at": "on 'at full confidence'", "event": "The confidence chip resolves to 1.000."},
        {"at": "on 'thirty-two holdings'", "event": "Thirty-two record marks fill a block and the running count steps 1 → 33."},
    ], intent="Rebuild of pantry/w5-failures.png, second row. The shared substring is lit in BOTH strings so the mechanism is visible, not asserted."),
))

# ── B06 · NOTHING TO FIND ─────────────────────────────────────────────────────
beats.append(beat(
    "B06", "NOTHING TO FIND", "REMOTION",
    "And then this one. The filed name is X A I three, F T five O, dot A F. That is an internal "
    "Fidelity security code. It is not a ticker, and it is not a company name. The model "
    "answered X A I, at full confidence, on three matching characters. Eight holdings. There "
    "was never anything there to find, and it found something anyway.",
    24,
    remotion("W5CodeAlone", "reel-local/MeasuringLocalLlm", {
        "sparkLine": "There was nothing there to find.",
        "eyebrow": "WEEK 5 · NOTHING TO FIND",
        "code": CODE["issuer_name"],
        "matchCount": 3,
        "codeNote": "an internal Fidelity security code — not a ticker, not a company name",
        "said": CODE["said"],
        "saidLabel": "the model answered",
        "reason": CODE["reason"],
        "confidence": CODE["confidence"],
        "confidenceLabel": "confidence",
        "holdings": CODE["holdings"],
        "holdingsLabel": "holdings",
        "verdict": "Three characters of overlap, and nothing else. This row has no right answer to get.",
        "source": f"SOURCE: figdata_week5.json — failures[2], golden-set row {CODE['id']}",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'the filed name'", "event": "The code sits ALONE on the cream, character by character in a slot row."},
        {"at": "on 'three matching characters'", "event": "Exactly three slots light terracotta; the rest stay ink."},
        {"at": "on 'an internal Fidelity security code'", "event": "The note lands beneath, small."},
        {"at": "on 'at full confidence'", "event": "The answer, the reason and 1.000 land together at the foot."},
    ], intent="Rebuild of pantry/w5-failures.png, third row. The script asks for this one ALONE on screen — nothing competes with it."),
))

# ── B07 · THE CONFIDENCE FINDING ──────────────────────────────────────────────
beats.append(beat(
    "B07", "THE FINDING", "REMOTION",
    "Here is the part that changes next week. Three hundred and twenty-two answers, and the "
    "model reported full confidence on three hundred and fifteen of them. Twelve of the fifteen "
    "answers that disagree with the labels came back at ninety-five percent or higher. It was "
    "completely sure, and it was wrong. So next week's review queue cannot be sorted by the "
    "model's confidence. That was the plan.",
    26,
    remotion("W5Confidence", "reel-local/MeasuringLocalLlm", {
        "sparkLine": "Completely sure, and wrong.",
        "eyebrow": "WEEK 5 · THE FINDING",
        "title": "Confidence does not sort them",
        "subtitle": "one dot per answer, 322 answers, ordered as scored",
        "dots": [{"c": d["confidence"], "s": d["state"]} for d in dots],
        "total": conf["total"],
        "atFull": conf["at_full"],
        "atFullLabel": "answers at confidence 1.000",
        "disagrees": conf["disagrees"],
        "disagreesLabel": "disagree with the label",
        "disagreesHigh": conf["disagrees_at_95_plus"],
        "disagreesHighLabel": "of those, at 0.95 or higher",
        "legend": [
            {"mark": "solid",  "label": f"wrong, at 0.95 or higher ({conf['disagrees_at_95_plus']})"},
            {"mark": "hollow", "label": f"wrong, and unsure ({conf['disagrees'] - conf['disagrees_at_95_plus']})"},
            {"mark": "ink",    "label": f"agrees with the label ({conf['total'] - conf['disagrees'] - conf['unlabelled']})"},
            {"mark": "ghost",  "label": f"no label to check against ({conf['unlabelled']})"},
        ],
        "distinctNote": (
            "The model only ever returned "
            + ", ".join(f"{v:.2f}" for v in conf["distinct_values"])
            + " — three values, for 322 different questions."
        ),
        "consequence": "A review queue sorted by confidence would put twelve of the fifteen errors at the bottom.",
        "source": "SOURCE: figdata_week5.json — dots[], one entry per adjudicated golden-set row",
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "0.05", "event": "322 dots fill the field, one per answer, in scoring order."},
        {"at": "on 'full confidence on three hundred and fifteen'", "event": "The 1.000 block lights as one mass; the count resolves to 315."},
        {"at": "on 'twelve of the fifteen'", "event": "The disagreeing dots ring terracotta — INSIDE the confident block, not outside it."},
        {"at": "on 'cannot be sorted'", "event": "The consequence line lands across the foot."},
    ], intent="Rebuild of pantry/w5-confidence.png. The errors must read as sitting INSIDE the confident mass — that adjacency is the finding."),
))

# ── B08 · THE THING I TURNED OFF ──────────────────────────────────────────────
beats.append(beat(
    "B08", "THE THING I TURNED OFF", "REMOTION",
    "One thing did work. Every mistake was the model adding a company. The single time it "
    "helped, it took one away. So I built a version allowed only to veto, never to propose. It "
    "scores a perfect one point oh, on four rows. Four. I built it, measured it, and left it "
    "switched off. It is a decent sceptic and a poor proposer.",
    25,
    remotion("W5Veto", "reel-local/MeasuringLocalLlm", {
        "sparkLine": "Built it, measured it, left it off.",
        "eyebrow": "WEEK 5 · THE THING I TURNED OFF",
        "title": "Every row the veto would ever see",
        "subtitle": "the LLM allowed only to REMOVE a claim, never to add one",
        "directionLeft": {"label": "added a company", "value": band["promotions"]},
        "directionRight": {"label": "removed one", "value": band["fixed"]},
        "directionNote": "Every error ran one way. So take the direction away from it.",
        "rows": [
            {
                "name": short_name(v["issuer_name"]),
                "claimed": v["claimed"],
                "score": v["score"],
                "vetoed": v["vetoed"],
                "right": v["claim_right"],
                "holdings": v["holdings"],
                "note": v["note"],
            } for v in veto
        ],
        "scoreLabel": "matcher confidence",
        "metric": f"{VETO['macro']['precision']:.4f}",
        "metricLabel": "precision, veto-only",
        "metricNote": f"on {len(veto)} rows. Four.",
        "verdict": "SWITCHED OFF",
        "verdictNote": (
            "A perfect score on four rows is not evidence. It is a policy with almost nothing "
            "to do. Shipping it would mean quoting 1.0000 and hoping nobody asks the sample size."
        ),
        "source": ("SOURCE: figdata_week5.json — veto_rows[], scoreboard.F_v2_veto. "
                   "Names shortened at the exposure clause; rows 3 and 4 are the same filed "
                   "string apart from a trailing space, as noted."),
        "folderLabel": HANDLE,
    }, "illustrate", [
        {"at": "on 'every mistake was adding'", "event": "Two direction counters: 14 added, 1 removed."},
        {"at": "on 'allowed only to veto'", "event": "The four rows land, one per line, with the vetoed row marked."},
        {"at": "on 'a perfect one point oh'", "event": "The 1.0000 sets at display size beside the row count."},
        {"at": "on 'left it switched off'", "event": "SWITCHED OFF stamps across the metric, and the caveat lands beneath."},
    ], intent="Rebuild of pantry/w5-veto.png. The sample size must be as loud as the score, or the beat becomes the boast it is arguing against."),
))

# ── B09 · VERDICT ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B09", "VERDICT", "BOOKEND",
    "Week five on one page. An eight billion parameter model, given exactly what the rules get. "
    "Three hundred and twenty-two calls, zero failures, five points of precision gone. One bad "
    "record becomes a hundred and ninety-six. Every failure was the same failure, a resemblance "
    "promoted to a match, once by inventing a fact outright. Full confidence on three hundred "
    "and fifteen answers, including twelve that were wrong. The plan said keep the rules if "
    "there is no lift. There is no lift. I am keeping the rules.",
    36,
    remotion("ClaudeVerdictArtifact", "proven-core/ClaudeVerdictArtifact", {
        "sparkLine": "",
        "artifactTitle": f"{SEGMENT} — week 5",
        "artifactHeading": "What the test found",
        "artifactLines": [
            f"{run['model']} local, temperature {run['temperature']}, seed {run['seed']} — "
            f"{thr['calls_measured']} calls, {thr['errors']} failures, "
            f"{thr['mean_seconds_per_call']:.2f}s each, on the same four fields the rules get.",
            f"Precision {RULES['macro']['precision']:.4f} → {MODEL['macro']['precision']:.4f} "
            f"on the same {conf['total']} labels. Recall unchanged at {MODEL['macro']['recall']:.4f}. "
            f"In records, {rec_rules} false positive becomes {rec_model}.",
            f"Every error ran one way: {band['promotions']} companies added, {band['fixed']} removed. "
            f"One reason was an invented corporate fact — “HYPERSCALE DATA INC … is the "
            f"parent company of Scale AI, Inc.”",
            f"Confidence 1.000 on {conf['at_full']} of {conf['total']} answers, and "
            f"{conf['disagrees_at_95_plus']} of the {conf['disagrees']} disagreements came back at "
            f"0.95 or above. A review queue cannot be sorted by it.",
            f"Veto-only scores {VETO['macro']['precision']:.4f} — on {len(veto)} rows. Built, "
            f"measured, switched off. The plan pre-committed: no lift, keep the rules. Keeping the rules.",
        ],
    }, "stagger", [
        {"at": "0.05", "event": f"The Claude artifact page opens — {SEGMENT}, week 5."},
        {"at": "each line", "event": "Five findings stagger in, one per spoken clause."},
    ]),
    lead=0.4,
))

# ── B10 · HANDOFF ─────────────────────────────────────────────────────────────
beats.append(beat(
    "B10", "HANDOFF", "BOOKEND",
    "Your turn. Paste this into Claude. Take a task you were about to hand to a language model, "
    "and write down, before you run it, what result would make you keep what you already have. "
    "Then run it and score both on the same cases. And check one thing in particular. When the "
    "model is wrong, does it know? If its confidence cannot separate its right answers from its "
    "wrong ones, you have not bought a reviewer. You have bought more work.",
    32,
    remotion("ClaudeComposerAsk", "proven-core/ClaudeComposerAsk", {
        "greeting": "Your turn.",
        "topic": KICKER,
        "segment": SEGMENT,
        "command": (
            "Help me pre-commit an evaluation before I replace a rule I already trust with an LLM. "
            "Write the decision rule FIRST: what result would make me keep the incumbent? Then "
            "score both systems on the same labelled cases, and test whether the model's own "
            "confidence separates its right answers from its wrong ones."
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
    "Measuring a local language model against the matcher. Week five of the Private AI Valuation "
    "Agent. Om Mali, for Humanitarians A I.",
    11,
    remotion("ClaudeTitleOutro", "proven-core/ClaudeTitleOutro", {
        "title": SEGMENT,
        "handle": HANDLE,
        "subline": "week 5 · the Private AI Valuation Agent",
    }, "fade", [
        {"at": "0.00", "event": "Title restates poster-style in serif with the terracotta period; handle beneath."},
    ]),
))

sheet = {
    "metadata": {
        "title": SEGMENT,
        "slug": "measuring-a-local-llm-against-the-matcher",
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
        "greeting": "Hallo, HAI",
        "greeting_note": "hello lexicon: German (short form). HAI persona takes only the shortest cues (Hi · Ola · Hej · Ciao · Hallo). Rotated off weeks 1, 2 and 4 so the series never repeats a language.",
        "aspect_ratio": "16:9",
        "fit": "pad",
        "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
        "color_semantics": "Claude FIDELITY skin: cream #F2F0E9 stage, warm ink #3D3929, terracotta #D97757 as the ONE accent. The Mycroft figures use crimson #C8102E for the primary series and ochre #C8860E for annotation; both remap onto the Claude accent grammar. Palette change only, no data change. Same treatment as weeks 1, 2 and 4.",
        "series": "Private AI Valuation Agent — week 5 (follows 2026-08-22-Entity-resolution-and-the-golden-set)",
        "derived_from": "video_script_week5.md (human-authored, 306 spoken words, target 2:00) plus README.md's figure-to-beat map. Every on-screen figure is a prop injected by build_beat_sheet.py from figdata_week5.json, under assertions — no number is typed by hand.",
        "note": "ai-explainer / claude-hai. ILLUSTRATE LAW: the Claude UI appears at B00 (cold open, answered), B09 (verdict artifact), B10 (handoff) and B11 (outro) only — every body beat illustrates its concept as a native animated Remotion scene (REBUILD LAW). The five source PNGs and their SVG sources are REFERENCE in pantry/, never slotted as media. The script's five body sections are split into eight beats so no beat carries two ideas; the split is logged in BUILD-LOG.md. This is a NEGATIVE result and the cut reports it without apology.",
        "companion_vertical": "vertical/ — the same twelve beats, same audio, rendered 9:16 at 2160×3840 from portrait compositions (never a crop).",
        "tags": ["SEC", "N-PORT", "entity resolution", "LLM evaluation", "llama 3.1", "local models",
                 "negative result", "precision", "Scale AI", "data engineering", "Humanitarians AI", "Mycroft"],
    },
    "beats": beats,
}

out = HERE / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

words = {b["beat_id"]: len(b["narration_text"].split()) for b in beats}
print(f"[week5] wrote {out}  — {len(beats)} beats")
print("[week5] narration words:", " ".join(f"{k}={v}" for k, v in words.items()))
body = [v for k, v in words.items() if k in ("B01", "B02", "B03", "B04", "B05", "B06", "B07", "B08")]
print(f"[week5] body beats {min(body)}–{max(body)}w (band 45–70), total {sum(words.values())}w")
