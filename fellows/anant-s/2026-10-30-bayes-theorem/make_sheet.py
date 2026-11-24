"""Builds beat_sheet.json for "Bayes' Theorem: The Positive That's Usually Wrong" (tldr).

On-screen numbers are read from demo/evidence.json (produced by demo/bayes_demo.py), never typed.
Narration spells numbers as words; the asserts below tie each spoken number to the evidence.
Re-running this OVERWRITES beat_sheet.json (drops measured audio fields): rerun audio after.
Run:  python make_sheet.py
"""
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
ev = json.loads((HERE / "demo" / "evidence.json").read_text(encoding="utf-8"))
C = ev["counts"]
PPV = ev["ppv"]
SW = {d["base_rate"]: d for d in ev["base_rate_sweep"]}
TWO = ev["second_positive"]
T = ev["test"]

# The spoken numbers below are words; pin each one to the evidence so a changed run breaks the build.
assert (C["n"], C["sick"], C["healthy"]) == (10000, 100, 9900)
assert (C["tp"], C["fn"], C["fp"], C["tn"], C["positives"]) == (99, 1, 495, 9405, 594)
assert PPV["reduced"] == [1, 6] and PPV["false_alarm_share"] == "5/6"
assert (T["sensitivity_pct"], T["specificity_pct"], T["base_rate_pct"], T["fpr_pct"]) == (99, 95, 1, 5)
assert ev["bayes"]["p_pos_decimal"] == 0.0594
assert round(SW["1/1000"]["ppv_pct"]) == 2 and round(SW["1/10"]["ppv_pct"]) == 69 and round(SW["1/2"]["ppv_pct"]) == 95
assert TWO["posterior"] == "99/124" and TWO["counts_per_million"]["sick_pos_twice"] == 9801
assert TWO["counts_per_million"]["healthy_pos_twice"] == 2475

TITLE = "Bayes' Theorem: The Positive That's Usually Wrong"
SLUG = "tldr-bayes-theorem"
TOPIC = "Probability · Bayes' Theorem"
WPS = 2.6          # pace_check.py's planning pace (Kokoro am_onyx); the report also gives 3.5 w/s


def est(text, lead=0.0, tail=0.0):
    return round(len(text.split()) / WPS + lead + tail, 1)


def remotion(bid, act, pattern, props, narration, show, proof="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": proof,
         "narration_text": narration, "voice": "am_onyx", "engine": "kokoro",
         "estimated_duration_s": est(narration, extra.get("lead_silence_s", 0), extra.get("tail_silence_s", 0)),
         "shot": {"type": "GRAPHIC", "source": "remotion", "show": show,
                  "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


def learn(bid, role, cls, content_type, lq, narration, show, visual_intent, motion_claim, **extra):
    q, a, o, i, nq = lq
    b = {"beat_id": bid, "act": "learn 1", "section": 1, "role": role, "lane": "manim",
         "content_type": content_type, "proof_gate": "SHOW",
         "learn": {"question": q, "action": a, "observation": o, "inference": i, "next_question": nq},
         "narration_text": narration, "voice": "am_onyx", "engine": "kokoro",
         "estimated_duration_s": est(narration),
         "shot": {"type": "GRAPHIC", "source": "own", "motion": "transform",
                  "manim": {"class": cls, "file": "scenes.py"},
                  "show": show, "visual_intent": visual_intent, "motion_claim": motion_claim}}
    b.update(extra)
    return b


beats = []

# ============================================================== B00 TL;DR · WHAT
n00 = ("Salaam. This is Liam, in for Bear. This film is about what a positive result really means "
       "when a test catches ninety-nine percent of cases. When the disease is rare, most positives are "
       "false alarms: in our example, five out of six. You'll see it by sorting ten thousand people, "
       "then building Bayes' theorem from the counts. The trap: reading the test's ninety-nine percent "
       "as your chance of being sick.")
beats.append(remotion("B00", "tldr · what", "ClaudeTldrWhat", {
    "eyebrow": "TL;DR", "heading": "What This Film Is About", "greeting": "Salaam, Liam", "topic": TOPIC,
    "question": "A test that catches 99% of cases says I'm positive. How likely is it that I'm sick?",
    "lines": [f"When the disease is rare, most positives are false alarms: here, {PPV['den'] - PPV['num']} of {PPV['den']}.",
              f"You will see it by sorting {C['n']:,} people, then building Bayes' theorem from the counts.",
              f"The trap: reading the test's {T['sensitivity_pct']:g}% as your chance of being sick."],
    "cues": [3.2, 10.0, 17.0, 24.5], "durationSeconds": est(n00), "folderLabel": "@NikBearBrown"},
    n00,
    [{"at": 0.0, "event": "'TL;DR.' wordmark lands; 'Salaam, Liam' + topic line"},
     {"at": 0.10, "event": "the question writes on, word by word"},
     {"at": 0.36, "event": "line 1 lands on 'most positives are false alarms'; numeral 1 terracotta"},
     {"at": 0.62, "event": "line 2 lands on 'sorting ten thousand people'; line 1 settles to ink"},
     {"at": 0.86, "event": "line 3 lands on 'The trap'"}],
    role_note="TL;DR·WHAT: IN-FOR-BEAR sign-in; gist not mechanism (paradox rule). Cues are estimates; "
              "rewrite from mp3/words.json after audio lock."))

# ============================================================== B01 TL;DR · WHY
n01 = ("Why should you care? Screening tests, spam filters and fraud alerts all raise flags, and each "
       "comes with a percentage that's easy to read backwards. Read backwards, a likely false "
       "alarm looks almost certain. When this kind of puzzle was put to doctors and students at Harvard "
       "teaching hospitals, most got it wrong. Ask first how common the thing is, and the alarm makes sense.")
beats.append(remotion("B01", "tldr · why", "ClaudeTldrWhy", {
    "eyebrow": "TL;DR", "heading": "Why You Should Care", "topic": TOPIC,
    "lead": "Screening tests, spam filters and fraud alerts all raise flags with a percentage that is easy to read backwards.",
    "lines": ["Read backwards, a likely false alarm looks almost certain.",
              "Put to doctors and students at Harvard teaching hospitals, most got a puzzle like this wrong.",
              "Ask first how common the thing is, and the alarm makes sense."],
    "cues": [1.2, 9.0, 13.5, 20.5], "durationSeconds": est(n01), "folderLabel": "@NikBearBrown"},
    n01,
    [{"at": 0.0, "event": "page turn: same header, heading 'Why You Should Care'"},
     {"at": 0.05, "event": "the stake writes on"},
     {"at": 0.35, "event": "dash 1 lands on 'Read it backwards'"},
     {"at": 0.55, "event": "dash 2 lands on 'doctors and students'"},
     {"at": 0.85, "event": "dash 3 lands on 'Ask first how common'"}],
    qc={"sparse_by_design": True, "sparse_reason": "TL;DR card two — text lands on cues by design."},
    role_note="Casscells et al. 1978: 11 of 60 correct (18%). FACTCHECK #4."))

# ============================================================== B02 THE QUESTION
n02 = ("The real question: how often is a positive right? Not how often the test is right. A test that "
       "catches ninety-nine percent of cases does not make a positive ninety-nine percent sure.")
beats.append(remotion("B02", "the question", "BrutalistHesitantWriter", {
    "text": "A test catches 99% of cases.\nMine says positive.\nHow often is the test right?",
    "triggerWords": "the test", "replacementWords": "a positive",
    "face": "serif", "fontSize": 72, "charMs": 26, "hesitateBetween": 7, "hesitateWithin": 1,
    "mistakeRate": 5, "jitter": 20, "seed": SLUG, "banner": ""},
    n02,
    [{"at": 0.0, "event": "cream page; caret; types 'A test catches 99% of cases. / Mine says positive.'"},
     {"at": 0.30, "event": "types 'How often is the test right?'; 'the test' turns terracotta"},
     {"at": 0.45, "event": "backspaces 'the test' → types 'a positive' on the spoken correction"},
     {"at": 0.80, "event": "caret holds on 'How often is a positive right?'"}],
    lead_silence_s=0.8,
    motion_claim="The writer types the naive question (test accuracy) and replaces the phrase that makes it "
                 "the wrong question (accuracy of a positive) on the spoken word.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."},
    role_note="Misconception: 'positive on a 99% test means 99% sick'. Read back corrected: "
              "'A test catches 99% of cases. Mine says positive. How often is a positive right?' — "
              "exactly the LEARN section's question. 'the test' occurs once in text (trigger is unique)."))

# ============================================================== B03 TERMS
n03 = ("Three words you'll hear. Base rate: how common the disease is among the people tested. Sensitivity: "
       "of the people who are sick, the share who test positive. Specificity: of the healthy, the share "
       "who test negative. The rest of them are false positives.")
beats.append(remotion("B03", "terms", "ClaudeDefinitions", {
    "title": "Terms In This Film",
    "terms": [{"term": "base rate", "meaning": "how common the disease is among the people tested"},
              {"term": "sensitivity", "meaning": "of the people who are sick, the share who test positive"},
              {"term": "specificity", "meaning": "of the healthy, the share who test negative; the rest are false positives"}],
    "durationSeconds": est(n03), "folderLabel": "@NikBearBrown"},
    n03,
    [{"at": 0.15, "event": "row 1 'base rate' lands terracotta"},
     {"at": 0.40, "event": "row 2 'sensitivity' lands; row 1 settles to ink"},
     {"at": 0.68, "event": "row 3 'specificity' lands; row 2 settles"}],
    proof="CARD",
    qc={"sparse_by_design": True,
        "sparse_reason": "TERMS card; prerequisites only — 'Bayes' theorem' and 'conditional probability' are earned in B16, not defined here."}))

# ============================================================== LEARN section 1 (B10–B19)
GRID = "125 × 80 isotype grid (pitch 0.068 u, 8.5 × 5.44 u, left of a counter column; IsotypeGrid pattern from explainer/manim/animated_graphics.py)"

beats.append(learn("B10", "HOOK", "B10_YouArePositive", "mechanism", (
    "A test that catches 99% of cases says positive. How likely am I to be sick?",
    "One square, 'you', on the stage; the test chip runs over it; the result stamps POSITIVE.",
    "The only numbers on screen are the 99% and the positive.",
    "Everyone's first answer is 99%; nothing on screen yet can check it.",
    "What happens if we run this test on a whole crowd, not one person?"),
    "You take a test for a rare disease. It catches ninety-nine percent of the people who have it. "
    "Your result: positive. So how worried should you be? Hold on to your first answer. We're going to count.",
    [{"at": 0.03, "event": "one ink square 'you' draws on, centre stage"},
     {"at": 0.20, "event": "test chip 'catches 99% of cases' slides across the square"},
     {"at": 0.42, "event": "result stamp 'positive' lands beside the square — the beat's terracotta"},
     {"at": 0.62, "event": "MathTex P(sick) = \\, ? writes beside it, the '?' large"},
     {"at": 0.85, "event": "the square and stamp shrink toward the top-left corner (the grid's first cell)"}],
    "One ink square ('you') with a terracotta POSITIVE stamp and an unanswered P(sick) = ?. The square is the "
    "persistent object the PAYOFF brings back.",
    "The stamp landing is the event; the closing shrink hands the square to the grid in B11 (state factory)."))

beats.append(learn("B11", "INSTANCE", "B11_TenThousand", "mechanism", (
    "What does the test do across a whole crowd?",
    f"Count up {C['n']:,} squares; mark the {C['sick']} sick (a 10 × 10 block, top left); run the test on them.",
    f"{C['tp']} of the {C['sick']} sick stay lit; {C['fn']} fades (missed).",
    "Among the sick, the 99% does exactly what it promised.",
    "And what does the same test do to everyone who is healthy?"),
    "Make it people. Ten thousand of them, one square each. One percent have the disease: one hundred "
    "squares. Run the test on them. It catches ninety-nine. One slips through. So far, the ninety-nine "
    "percent is doing exactly what it promised.",
    [{"at": 0.02, "event": f"{GRID} counts up in reading order, dim; 'you' sits in it as an outline ring"},
     {"at": 0.30, "event": f"a 10 × 10 block of {C['sick']} cells, top left, turns ink on 'one hundred squares'; label 'sick: {C['sick']}'"},
     {"at": 0.52, "event": "a scan bar sweeps the sick cells on 'Run the test'"},
     {"at": 0.68, "event": f"{C['tp']} stay ink, counter 'positive: {C['tp']}'"},
     {"at": 0.78, "event": f"{C['fn']} square fades to ghost — terracotta ring on it for the sentence 'One slips through'"}],
    f"Isotype grid of {C['n']:,} squares (125 per row, pitch 0.068 u); the sick a 10 × 10 block (top left) in ink, healthy dim, "
    "missed/cleared fade to ghost. Counters in EB Garamond from evidence.json.",
    "The grid filling, then the scan bar filtering the sick block, is the instance: sensitivity shown as a count."))

beats.append(learn("B12", "INSTANCE", "B12_FalseAlarms", "mechanism", (
    f"What does the same test do to the {C['healthy']:,} healthy people?",
    "Sweep the scan bar over the remaining healthy cells; 95% fade (cleared), 5% stay lit.",
    f"{C['fp']} healthy squares stay lit — five times as many as the sick who tested positive.",
    "A small false-alarm rate times a huge healthy crowd is a big number.",
    "So — what's the chance for someone who tested positive?"),
    "Now the other nine thousand nine hundred, the healthy ones. The test clears ninety-five percent of them. "
    "But five percent light up anyway. Five percent of nine thousand nine hundred is four hundred ninety-five "
    "false alarms. Five times as many as the sick people it caught.",
    [{"at": 0.03, "event": "scan bar returns to row 2 and sweeps down the remaining healthy cells"},
     {"at": 0.30, "event": f"{C['tn']:,} cleared squares fade to ghost as the bar passes"},
     {"at": 0.50, "event": f"{C['fp']} squares stay lit, scattered — they flash terracotta on 'light up anyway'"},
     {"at": 0.72, "event": f"counter 'false alarms: {C['fp']}' beside 'positive: {C['tp']}'"},
     {"at": 0.88, "event": "the 495 settle to dim; two counters held side by side"}],
    f"Same grid, same objects; the {C['fp']} false positives are seeded positions (seed in scenes.py) and "
    "stay lit dim after their terracotta flash.",
    "Second instance, same parameter (the test), different group: false-positive rate shown as a count."))

beats.append(learn("B13", "NAIVE", "B13_WrongCrowd", "mechanism", (
    "Isn't the answer just the 99% on the box?",
    f"Box the sick block; write {C['tp']}/{C['sick']}; then point at the {C['fp']} lit squares outside the box.",
    "The 99/100 is true — but its denominator is the sick, a crowd you don't know you're in.",
    "The 99% answers a question about the sick; yours is about the positives.",
    "What if we counted inside the crowd you actually know you're in?"),
    "The natural answer is ninety-nine percent. It's the number on the box. And it's true, for this block: "
    "ninety-nine of the one hundred who are sick tested positive. But that fraction is about people already known to "
    "be sick. All you know is that you tested positive.",
    [{"at": 0.05, "event": "rectangle draws round the sick block; label 'out of the sick'"},
     {"at": 0.30, "event": f"MathTex \\frac{{{C['tp']}}}{{{C['sick']}}} writes beside the box"},
     {"at": 0.60, "event": f"the {C['fp']} lit squares outside the box pulse once — terracotta"},
     {"at": 0.85, "event": "dim caption: 'but you only know you're positive'"}],
    "The box and its fraction are correct; the pulse of the lit squares outside it shows what the box leaves out.",
    "The natural attempt walked to its limit: the box is right and the wrong crowd."))

beats.append(learn("B14", "SHIFT", "B14_OnlyThePositives", "mechanism", (
    "What if we counted only the crowd you're in — the positives?",
    f"Fade every negative; the {C['positives']} positives fly together into one block (27 × 22), sick first.",
    f"One block: {C['tp']} ink squares, {C['fp']} dim. 'You' is somewhere in it.",
    "The representation: keep only the people who match what you know.",
    "Of these, what share are sick?"),
    "So change the crowd. Keep everyone who tested positive, and let everyone else go. Here they are: "
    "ninety-nine who are sick, four hundred ninety-five who aren't. Before we count, commit to a guess. "
    "Of these lit squares, what share are sick?",
    [{"at": 0.05, "event": "all ghost (negative) squares fade out"},
     {"at": 0.25, "event": f"the {C['positives']} positives fly into one 27 × 22 block, larger squares, sick first"},
     {"at": 0.55, "event": "'you' ring lands on the block's edge: you're one of these"},
     {"at": 0.70, "event": "HOLD ≥ 3 s — nothing moves on 'commit to a guess'"}],
    "The positives-only block (natural-frequency representation, Gigerenzer & Hoffrage 1995). "
    "Mark the simplification once: dim caption 'each square = one person; expected counts'.",
    "The re-grouping IS the reframe: the denominator changes on screen. The hold is the predict beat.",
    predict=True))

beats.append(learn("B15", "TRANSFORM", "B15_OneInSix", "equation", (
    "Of the positives, what share are sick?",
    f"The {C['tp']} ink squares stack above a fraction bar, all {C['positives']} below it; the stacks morph into "
    f"numerals {C['tp']}/{C['positives']}, which reduce to 1/6.",
    "One positive in six is sick; five in six are false alarms.",
    "The answer to 'how worried?' is about 17%, not 99%.",
    "Can we write that without counting squares?"),
    "Ninety-nine have the disease. Five hundred ninety-four in all. Watch the fraction shrink. One in six. "
    "Five out of six positives are healthy.",
    [{"at": 0.0, "event": f"the {C['tp']} ink squares slide up and stack above a growing fraction bar"},
     {"at": 0.22, "event": f"all {C['positives']} squares stream under the bar"},
     {"at": 0.45, "event": f"the stacks morph into MathTex \\frac{{{C['tp']}}}{{{C['positives']}}}"},
     {"at": 0.65, "event": "the fraction transforms to \\frac{1}{6} — the terracotta lands on it"},
     {"at": 0.85, "event": f"dim chip '≈ {PPV['pct']:g}%' under it; held"}],
    "One continuous morph: squares become the numerator and denominator, the fraction reduces. Every object "
    "persists from B14.",
    "The aha is the morph itself; narration is short sentences so run_time fills the audio."))

beats.append(learn("B16", "ABSTRACTION", "B16_BuildBayes", "equation", (
    "Can we say that in general, without squares?",
    "Divide each count by 10,000: 99 becomes 0.99 × 0.01, then P(+|D)P(D); 594 becomes P(+); "
    "assemble P(D|+); swap D, + for A, B.",
    "The equation is the fraction we just watched, written in chances.",
    "Bayes' theorem: flip a conditional chance by weighing in how common each side is.",
    "What does each symbol in that line mean?"),
    "This thing deserves a name. Divide every count by ten thousand and the counts become chances. "
    "Ninety-nine becomes the sensitivity times the base rate. Five hundred ninety-four becomes the chance "
    "of any positive. What's left is Bayes' theorem. It flips a conditional chance by weighing in how common "
    "each side is.",
    [{"at": 0.03, "event": "the \\frac{99}{594} from B15 slides left; '÷ 10,000' writes under each number"},
     {"at": 0.25, "event": "99 → \\frac{99}{10\\,000} → 0.99 \\times 0.01 → P(+\\mid D)\\,P(D) (MathTex, staged)"},
     {"at": 0.45, "event": "594 → P(+) (MathTex)"},
     {"at": 0.60, "event": "assembles P(D\\mid +) = \\frac{P(+\\mid D)\\,P(D)}{P(+)}"},
     {"at": 0.80, "event": "D, + morph to A, B: P(A\\mid B) = \\frac{P(B\\mid A)\\,P(A)}{P(B)}; serif label 'Bayes' theorem' — terracotta"}],
    "The counts transform into the notation (objects → symbols, never the other way). Every equation in MathTex.",
    "The abstraction arrives as an endpoint: the fraction the viewer watched becomes Bayes' theorem."))

beats.append(learn("B17", "TANGENT", "B17_ReadTheLine", "equation", (
    "What does each symbol mean?",
    "Equation persists left; right band writes the two sides as sentences, the '=' as a claim, a glossary, "
    "one worked value, and the values claim (the bar has a direction).",
    "Every symbol maps back to a crowd on the grid.",
    "The notation is a description of the counting.",
    "So — back to you?"),
    "Read it piece by piece. On the left: the chance of disease, given a positive. On the right: the chance "
    "of a positive, given disease, the ninety-nine percent, times the base rate, one percent, divided by "
    "the share of everyone who tests positive. Zero point nine nine times zero point zero one, over zero "
    "point zero five nine four. One sixth. The bar has a direction. Swap its sides, and you get a different number.",
    [{"at": 0.03, "event": "LHS P(A|B) boxed (box spotlight, not underline); sentence 'chance of A once you know B'"},
     {"at": 0.20, "event": "P(B|A) boxed; glossary row 'P(B|A) · sensitivity · 0.99'"},
     {"at": 0.32, "event": "P(A) boxed; row 'P(A) · base rate · 0.01'"},
     {"at": 0.42, "event": "P(B) boxed; row 'P(B) · all positives · 0.0594'"},
     {"at": 0.62, "event": "worked value: 0.99 × 0.01 / 0.0594 = 1/6 (MathTex)"},
     {"at": 0.85, "event": "values claim: P(B|A) ≠ P(A|B) — the '≠' gets the box spotlight, terracotta"}],
    "Split stage, five zones (EQUATIONS.md / animated_graphics.EquationTangent): symbolic form persists MAIN; "
    "sentences, glossary (A = disease, B = a positive test), worked example and values claim write into SIDE.",
    "One moving box spotlight across equation, sentence and glossary row; ~30–40 s, explains never derives."))

beats.append(learn("B18", "PAYOFF", "B18_BackToYou", "mechanism", (
    "So — how worried should you be?",
    "The HOOK's 'you' square with its positive stamp returns into the 594 block; the 1/6 sits beside it.",
    "You moved from 1 in 100 to 1 in 6 — a real jump, nowhere near 99%.",
    "Healthy people outnumber the sick 99 to 1, so a 5% false-alarm rate makes a crowd.",
    "How much did the base rate decide that?"),
    "Back to you. You are one of these five hundred ninety-four; one in six is sick. "
    "A positive moved you from one in a hundred to one in six: a real jump, nowhere near ninety-nine "
    "percent. The sick are outnumbered ninety-nine to one, so a small false-alarm rate makes a crowd.",
    [{"at": 0.03, "event": "the B10 'you' square + stamp return (same objects) and settle into the 594 block"},
     {"at": 0.30, "event": "MathTex \\frac{1}{100} → \\frac{1}{6} arrow beside the square"},
     {"at": 0.62, "event": "the 99:1 ratio: sick row vs the healthy mass flash once, terracotta on the healthy side"},
     {"at": 0.85, "event": "held: you, the block, 1/6"}],
    "The HOOK's persistent object resolved: the 'you' square inside the positives, its P(sick) = ? now 1/6.",
    "PAYOFF returns the HOOK object, not a redraw; the explanation check (why?) is answered on the 99:1 flash."))

curve_pts = "; ".join(f"{d['base_rate_pct']:g}% → {d['ppv_pct']:g}%" for d in ev["base_rate_sweep"])
beats.append(learn("B19", "BOUNDARY", "B19_BaseRateDial", "mechanism", (
    "How much did the base rate decide that?",
    "Plot P(D|+) against base rate (log axis); a ValueTracker slides the 1/6 marker along the curve.",
    "Same test: 0.1% → about 2%, 1% → 1/6, 10% → about 69%, 50% → 95%.",
    "The test didn't change; the crowd did. Not taught here: what a second positive does.",
    ""),
    "One number did most of that work: the base rate. Same test, rarer disease, one in a thousand: a positive "
    "means about two percent. One in ten: about sixty-nine percent. One in two: ninety-five. What this film "
    "didn't do is test you twice. That's your turn.",
    [{"at": 0.03, "event": "the 1/6 slides onto axes: base rate (log) vs chance sick given positive"},
     {"at": 0.25, "event": f"marker slides left to 0.1%: reads {SW['1/1000']['ppv_pct']:g}%"},
     {"at": 0.45, "event": f"slides right through 1% (1/6) to 10%: {SW['1/10']['ppv_pct']:g}%"},
     {"at": 0.62, "event": f"to 50%: {SW['1/2']['ppv_pct']:g}%; the full curve traced in ink, marker terracotta"},
     {"at": 0.85, "event": "dim captions: 'same test: 99% sensitive, 95% specific' · 'not taught here: a second positive'"}],
    f"Curve from evidence.json base_rate_curve (61 log-spaced points); labelled points {curve_pts}.",
    "The ValueTracker sweep makes the dependence a motion; the boundary is one dim line that hands off to BHTF."))

# ============================================================== closing three
nV = ("Let's recap with Claude. The ninety-nine percent is about the sick: ninety-nine of every hundred sick "
      "people test positive. Your question is about the positives, and only ninety-nine of five hundred "
      "ninety-four are sick: one in six. The healthy outnumber the sick ninety-nine to one, so five percent "
      "false alarms make a crowd. Bayes' theorem flips the question by weighing in the base rate.")
beats.append(remotion("BVDT", "verdict", "ClaudeVerdictArtifact", {
    "artifactTitle": "Verdict", "artifactHeading": TITLE,
    "artifactLines": [f"The {T['sensitivity_pct']:g}% is about the sick: {C['tp']} of {C['sick']} sick people test positive.",
                      f"Your question is about the positives: only {C['tp']} of {C['positives']} are sick, one in six.",
                      f"The healthy outnumber the sick 99 to 1, so {T['fpr_pct']:g}% false alarms make a crowd.",
                      "Bayes' theorem flips the question by weighing in the base rate."]},
    nV,
    [{"at": 0.0, "event": "artifact page opens"},
     {"at": 0.15, "event": "four verdict lines land in narration order"}],
    lead_silence_s=0.5,
    qc={"sparse_by_design": True, "sparse_reason": "Mandated ClaudeVerdictArtifact bookend."}))

cmd = ("A test catches 99% of people who have a disease and wrongly flags 5% of healthy people. One person in "
       "100 has the disease. Someone tests positive, then takes the same test again and tests positive a second "
       "time. Before calculating, guess the chance they are sick. Then count it out for 1,000,000 people, show "
       "the counts after each test, and say what you had to assume about the two tests.")
spoken_cmd = ("A test catches ninety-nine percent of people who have a disease and wrongly flags five percent of "
              "healthy people. One person in a hundred has the disease. Someone tests positive, then takes the same "
              "test again and tests positive a second time. Before calculating, guess the chance they are sick. Then "
              "count it out for a million people, show the counts after each test, and say what you had to assume "
              "about the two tests.")
nH = ("Your turn. Paste this into Claude: " + spoken_cmd + " Here's what to check. After one positive: one in six. "
      "After two: about four in five, because the first answer became the new base rate. And it should say the "
      "two results were assumed independent. A real repeat test often isn't.")
beats.append(remotion("BHTF", "your turn", "ClaudeComposerAsk", {
    "greeting": "Your turn.", "topic": "BAYES' THEOREM · YOUR TURN", "segment": "Test Positive Twice",
    "command": cmd, "runningText": "paste this into Claude…",
    "output": [f"check: after one positive, {C['tp']} of {C['positives']} are sick — one in six",
               f"check: after two, {TWO['counts_per_million']['sick_pos_twice']:,} of "
               f"{TWO['counts_per_million']['sick_pos_twice'] + TWO['counts_per_million']['healthy_pos_twice']:,} — about four in five",
               "check: it names the independence assumption, and doubts it"],
    "folderLabel": "@NikBearBrown", "modelLabel": "Claude", "effortLabel": "High"},
    nH,
    [{"at": 0.0, "event": "composer opens — 'Your turn.'"},
     {"at": 0.08, "event": "the prompt types in full"},
     {"at": 0.62, "event": "runningText 'paste this into Claude…'"},
     {"at": 0.72, "event": "three check lines land as each is spoken"}],
    role_note="HANDOFF LAW: the prompt (props.command) is read aloud verbatim — digits on screen, words in voice — "
              "then a three-point rubric. Transfer exercise = the BOUNDARY's untaught case."))

beats.append(remotion("BOUT", "outro", "ClaudeTitleOutro",
                      {"title": TITLE + ".", "handle": "@NikBearBrown", "slug": SLUG, "subline": ""},
                      f"{TITLE}. At Nik Bear Brown.",
                      [{"at": 0.0, "event": "title restates; handle; slug-seeded mascot. Liam reads the title, then 'At Nik Bear Brown'."}],
                      kind="outro_voice", tail_silence_s=1.0,
                      hold_note="spoken outro + 1.0 s silent tail (apad); no jingle (OUTRO-LOCK §Voice)",
                      role_note="OUTRO-LOCK: exact title restate, hardcoded handle, spoken, no music, no subline."))

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": TOPIC, "skill": "tldr", "style_preset": "tldr",
    "channel": "claude-liam", "brand": "claude-liam", "persona": "Liam (in for Bear)", "in_for_bear": True,
    "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro", "clock": "narration",
    "palette": "claude", "learn_canvas": "cream", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160, "caption_policy": "none",
    "audience": "a curious adult who has seen 'the test is 99% accurate' and wants to know what a positive means",
    "source_doc": "SOURCE.md (written for this film) — references in SOURCES.md; bookloop law: not named on screen",
    "sections": [{"n": 1, "title": "Count the Positives",
                  "key_case": "10,000 people, 1% sick, a test with 99% sensitivity and 95% specificity; one 'you' square that tested positive",
                  "representation": "the 10,000-person grid filtered to the positives only (natural frequencies)",
                  "status": "PENDING GATE S"}],
    "greeting": "Salaam, Liam", "greeting_language": "Arabic/Farsi (Salaam)",
    "folderLabel": "@NikBearBrown",
    "typography": {"serif": "EB Garamond", "ui": "system sans", "mono": "PT Mono", "math": "MathTex"},
    "outro_policy": "OUTRO-LOCK §Voice: spoken title + 'At Nik Bear Brown', 1.0 s silent tail, no jingle.",
    "bookloop_policy": "The film teaches the idea standalone; sources are not named on screen or in narration.",
    "evidence": "demo/bayes_demo.py -> demo/evidence.json, demo/RUN-LOG.txt",
    "pronounce": {"Salaam": "səlˈɑːm"},
    "tags": ["Bayes' theorem", "probability", "base rate", "false positives", "medical testing",
             "conditional probability", "3Blue1Brown style", "Claude", "Nik Bear Brown"]},
    "beats": beats}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False), encoding="utf-8")

total = 0
for b in beats:
    n = len(b["narration_text"].split())
    total += n
    print(f"{b['beat_id']:5} {b.get('role', b.get('act', '')):12} {n:4} words  ~{n / 3.5:5.1f}s @3.5  ~{n / WPS:5.1f}s @2.6")
print(f"total {total} words  ~{total / 3.5 / 60:.1f} min @3.5 w/s  ~{total / WPS / 60:.1f} min @2.6 w/s")
