# SCRIPT.md — Claude, Investigation Query. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-investigation-query` (Teardown, skill-teardown
format) — question and true generic facts carried over; narration
re-registered to Plain (explain, then stop); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

**Source-fidelity note:** the source never filled in investigation-query's
specific "Claude's job: ___" line (literal `>` placeholder survives in two
spots), and its SKILL.md is not reachable from this machine (see
QUESTION.md / BUILD-LOG.md) — same defect class as the `case-brief`,
`hiring-review`, `internal-investigation`, `investigation-add`, and
`investigation-open` sibling redos. One fact fragment survived intact in
both B00 and BVDT: "Ask questions against an open investigation log — what
witnesses said,". This script keeps every fact the source DOES establish —
a skill is a folder Claude reads before it acts; it executes the file's
steps in order; it is a specification with a payoff and a limit — plus that
one surviving fragment (searches a log, e.g. what a witness said), and uses
"investigation-query" only as the named anchor example, never asserting
invented detail about the actual employment-law query procedure inside its
unread SKILL.md.

## B00 — cold open (BrutalistHesitantWriter)
You'd guess Claude works out what really happened once it picks up a skill
called investigation-query. It doesn't — it searches the investigation log.
Let's see what's inside that file.

## Act I — the wrong guess

**B01 — Sounds like fact-finding authority**
Hear "Claude has an investigation-query skill" and it sounds like Claude
itself can work out what really happened — cross-referencing witness
accounts and judging who's telling the truth.

**B02 — Broken, with a case** (pays off B00)
But nothing in the model changes. Delete the skill's folder and Claude
doesn't lose any power to judge witness credibility — it never had that
power. It just stops running that one search routine.

## Act II — the mechanism

**B03 — One file** (ANCHOR PLANTED)
Here's what a skill actually is: one file. Investigation-query, for
instance, is a folder holding a single SKILL.md — instructions for
searching an open investigation log, asking questions like what a given
witness said, written in plain language Claude reads before it starts.

**B04 — Read it, then follow it in order**
Claude reads that file top to bottom and works through it step by step, in
the order it's written — no branching, unless the file itself says branch.

**B05 — Spec, not judgment**
That makes a skill a specification, not new judgment. The payoff: the same
search, every question, every time. The limit: anything outside those
written steps, and Claude has no special opinion about it.

**B06 — The anchor returns** (ANCHOR PAYOFF)
So investigation-query never gave Claude the power to judge what a witness
meant. It just guarantees that every time investigation-query runs, Claude
reads that same file and searches the log the same way — that's the whole
trick.

## Act III — both directions

**B07 — Neither one is proof**
Watching Claude answer a question by finding it in the log doesn't prove it
understood what actually happened — a search can return an exact quote and
still miss the context around it. And watching it come up empty doesn't
prove nothing's there — it may just be a case nobody logged yet.

## Close

**BCRY — carry-out**
A skill named investigation-query doesn't hand Claude the power to judge
what happened — it's a checklist Claude reads before it starts, so the same
log gets searched the same way every time, and anything outside those steps
is still on you.

**BHTF — your turn**
Your turn. Paste this into Claude: pick one record you search the same way
every time — a support log, a call history, a set of meeting notes. Write
me a SKILL.md for it: plain language, ordered steps. Then read it back to
me and walk me through exactly what you'll search for, before you search.

**BOUT — outro**
Claude, Investigation Query. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–B01 | "an investigation-query skill" sounds like the model gained the power to judge what actually happened |
| Wrong guess | B00 → B02 | "investigates" corrected to "queries"; broken with the delete-the-folder case |
| Mechanism | B03–B05 | one file, read top to bottom, spec not judgment |
| Anchor | B03 → B06 | investigation-query's single SKILL.md, planted then returned to |
| Both directions | B07 | finding an answer in the log proves nothing about understanding; an empty result proves nothing about nothing being there |
| Carry-out | BCRY | one sentence, survives repetition |

## Beat-count note (redo)

Source is 7 beats (B00, B01 anatomy, B02 pipeline, B03 design tell, BVDT
verdict, BHTF your-turn, BOUT outro) — a compact skill-teardown format with
no explicit wrong-guess, anchor, or both-directions beat. hai-simple's spine
requires all three as their own beats (WRONG-GUESS LAW / ANCHOR LAW /
BOTH-DIRECTIONS LAW), so this redo expands modestly: B01 (stakes) and B02
(wrong guess, broken) are new; B03/B04/B05 carry the source's anatomy/
pipeline/design-tell facts across to the anchor; B06 is a new anchor-payoff
beat restating the design tell against the named anchor; B07 (both
directions) is new. Result: B00 + 7 body beats + BCRY/BHTF/BOUT = 11 beats —
a small, proportionate expansion of a 7-beat source, matching the identical
expansion pattern on the `case-brief`/`hiring-review`/`internal-
investigation`/`investigation-add`/`investigation-open` sibling redos, which
hit the same source-fidelity gap. No employment-law-specific fact was
invented anywhere in this expansion; the one surviving fact fragment ("ask
questions against an open investigation log — what witnesses said") anchors
B03/B06.

## One-flag audit

No inference-flag beat: every claim here is about the generic, verifiable
mechanism of a Claude skill (folder + SKILL.md, read-then-execute,
specification semantics) plus the one surviving fact fragment from the
source — not an inference about an unread source. Nothing in this script
asserts what investigation-query's specific employment-law search procedure
actually contains beyond "searches a log, e.g. what a witness said."
