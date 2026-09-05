# QUESTION — behind-the-model--claude-liam-supervision-calibration-logger

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/youtube/behind-the-model/claude-liam-supervision-calibration-logger/beat_sheet.json`.
That source sheet is a CLI-explainer ("CONDUCTING AI") build: it walks
through building a small command-line supervision log with three
commands — `log` (record an AI interaction with a timestamp), `classify`
(call a model to label each entry Level I / II / III and estimate a fair
verification time in minutes), and `audit` (print a weekly report: level
breakdown, average verify time, and the top "gap" interactions — Level III
usage with under two minutes of verification). It demos a 12-interaction
week on a usage/supervision grid, finds a 50% calibration score with three
"danger corner" interactions (heavy reliance, almost no verification), asks
for a revision (each gap interaction gets a recommended verification step),
re-runs, and closes with a next-steps beat: run the logger for a week, and
if the score is below 70%, add verification to the top three gaps and
re-audit in two weeks.

**What changes in this redo:** register Teardown/CLI → Plain, general
audience — no terminal commands, no named model, no invented product UI.
The source's CLI spine (INTRO / PROBLEM / ASK / CODE / OUTPUT / CHANGE /
OUTPUT-revised / SUMMARY / NEXT STEPS / outro, ~10 beats plus BOOKEND
verdict/handoff/outro lanes) doesn't carry a WRONG-GUESS or ANCHOR beat in
the Plain sense — it states the problem and builds toward it directly,
which is normal for a CLI walkthrough but not for hai-simple's spine. This
redo adds both: the wrong guess (a newcomer assumes supervision is one
flat personal habit — careful or not — rather than something that should
scale with how much decision-making a given task hands to Claude),
falsified by the source's own claim that the mismatch is invisible until
logged; the anchor is the source's own worked example, literalized — the
12-interaction usage/supervision grid with three danger-corner dots
(B03), returned at B05 after the revision loop closes it partway, split
into the two both-directions cautions (a rising score proves more logged
checking time, not that the checking caught anything; an un-flagged
interaction isn't automatically fine, it just wasn't caught by this pass).
The source's CODE beat (an actual Python snippet) is dropped — Plain
register doesn't show code to a general audience — and its content
(the list-comprehension gap definition) is carried instead as plain
mechanism narration in B02/B04. The source's classify command named a
specific model (`claude-3-5-haiku`); dropped per the no-invented-model-
names rule — the redo says "Claude" generically. B00 replaced the source's
`NikBearBrownOpen` cold open (already a Remotion title card, not a
generated puppet — no NO-GENAI violation in the source, but not the
WRITER LAW shape hai-simple requires) with `BrutalistHesitantWriter`:
"careful" → "calibrated", landing on the reel's own key term. Close
re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off, per
hai-simple's channel skin. Beat count changed from the source's ~10-plus-
bookend CLI spine to a 9-beat Plain spine (B00, B01–B05, BCRY, BHTF, BOUT)
— compressed, not padded, since the source's CODE beat is dropped and its
OUTPUT/CHANGE/OUTPUT-revised/SUMMARY/NEXT-STEPS beats collapse into the
anchor-planted/mechanism/anchor-payoff arc that Plain's spine requires.

**Question this reel actually answers:** How do you know whether you're
supervising Claude enough — and is "being careful" even the right thing to
measure?

**Who asked, where:** nobody — this is a factory redo of a published
CLI-explainer reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
