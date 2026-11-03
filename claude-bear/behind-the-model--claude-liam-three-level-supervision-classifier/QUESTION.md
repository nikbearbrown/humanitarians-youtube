# QUESTION — behind-the-model--claude-liam-three-level-supervision-classifier

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/youtube/behind-the-model/claude-liam-three-level-supervision-classifier/beat_sheet.json`.
That source sheet is a CLI-explainer ("CONDUCTING AI") build: it walks through
asking Claude Code to write a Python script that defines eight AI interaction
descriptions, calls the Anthropic API to classify each against the
Sheridan-Verplank automation framework (Level I / II / III), and returns JSON
with the level, the supervisory demand, a verify-time estimate in minutes, and
a gap flag. It demos the classifier on Priya, a single user whose three
ordinary interactions — renaming a variable, citing a market size, proposing
a system architecture — plot on a usage-level-versus-supervision-level grid:
the rename lands on the calibrated diagonal, the market-size citation and the
architecture proposal both fall below it because both got only a quick-glance
level of checking despite very different stakes. It asks for a revision
(name the supervisory demand explicitly, color-code the flag), re-runs, finds
four of eight interactions flagged, and closes with a next-steps beat: run
the classifier on your own last ten AI interactions and, for any Level Three
result under two minutes of verification, ask what you actually checked.

**What changes in this redo:** register Teardown/CLI → Plain, general
audience — no terminal commands, no Python code, no named classifier model
(`claude-3-5-haiku` is dropped; the reel says "Claude" generically). The
source's CLI spine (INTRO / PROBLEM / ASK / CODE / OUTPUT / CHANGE /
OUTPUT-revised / SUMMARY / NEXT STEPS, ~9 body beats plus YOURTURN/outro)
doesn't carry a WRONG-GUESS beat or a planted-then-paid-off ANCHOR in the
Plain sense — it states the problem and builds straight at it, which is
normal for a CLI walkthrough but not for hai-simple's spine. This redo adds
both, using the source's own material rather than inventing new claims:

- **Wrong guess:** a newcomer assumes trusting AI "the right amount" means
  picking one fixed comfort level and keeping it steady for every task.
  Falsified by the source's own Priya example — the same quick glance
  applied to a variable rename (fine) and to a full system-architecture
  proposal (a much bigger gap) is exactly the mismatch the source describes
  in B01: "people apply the same supervision level to both... a quick
  glance, maybe a nod, and move on."
- **Anchor, planted then paid off:** the source's own Priya grid (B04 in the
  source), literalized as this redo's B03 (planted: her three interactions,
  same glance, three different levels) and returned at B05 (payoff: the
  flag fires on the two mismatched ones, and what that firing does and does
  not prove).

**One flag:** the source treats "Sheridan-Verplank, applied to AI" as a
given; this redo makes explicit that Sheridan and Verplank's 1978 framework
was built for human supervision of automation generally, not written with AI
chat in mind — applying it here is an adaptation, one inference beyond the
source's own citation, and gets exactly one flag (B04) per ONE-FLAG LAW.

**Dropped, not carried:** the actual Claude Code invocation and its exact
wording; the Python script and its `gap_flag` boolean line; the named model
`claude-3-5-haiku`; the "revise the output table" beat (B05 in the source) —
a formatting fix to a script's printed table isn't a teaching point for a
general audience and is folded into B04's plain description of what the flag
does. The core claims survive unchanged: three levels that matter (copy-paste
use, research-level use, true collaboration), the calibrated diagonal, the
gap as a mismatch between usage level and how long you actually checked, and
the next-steps instruction to audit your own recent interactions.

B00 replaced the source's `NikBearBrownOpen` title-card cold open with
`BrutalistHesitantWriter` per WRITER LAW: "same" → "right" (typed first as
"the same amount", corrected to "the right amount"), landing on the reel's
own key term and previewing the wrong guess. Close re-skinned to `OutroCTA`
(`ClaudeTitleOutro` in the sibling reels was swapped project-wide for
`OutroCTA` — same slot) / @HumanitariansAI with Liam's sign-off, per
hai-simple's channel skin. Beat count changed from the source's ~9-body-beat
CLI spine (B01–B08 plus YOURTURN) to a 9-beat Plain spine (B00, B01–B05,
BCRY, BHTF, BOUT) — compressed and restructured, not padded: the source's
CODE beat is dropped entirely, and PROBLEM/ASK/OUTPUT/CHANGE/OUTPUT-
revised/SUMMARY/NEXT-STEPS collapse into the wrong-guess / mechanism /
anchor-planted / one-flag / anchor-payoff-and-both-directions arc that
hai-simple's spine requires.

**Question this reel actually answers:** are you supervising Claude at the
right level — matched to how much of the decision you actually handed it —
or applying the same quick check to everything regardless of stakes?

**Who asked, where:** nobody — this is a factory redo of a published
CLI-explainer reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
