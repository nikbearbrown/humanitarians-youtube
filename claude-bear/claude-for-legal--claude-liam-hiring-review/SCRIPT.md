# SCRIPT.md — Claude, Hiring Review. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-hiring-review` (Teardown, skill-teardown format) —
question and true generic facts carried over; narration re-registered to
Plain (explain, then stop); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

**Source-fidelity note:** the source never filled in hiring-review's
specific "Claude's job: ___" line (literal `>` placeholder survives in
three spots), and its SKILL.md is not reachable from this machine (see
QUESTION.md / BUILD-LOG.md). This script keeps every fact the source DOES
establish — a skill is a folder Claude reads before it acts; it executes
the file's steps in order; it is a specification with a payoff and a
limit — and uses "hiring-review" only as the named anchor example (a
skill-shaped folder aimed at walking through a hiring decision), never
asserting invented detail about the actual employment-legal checklist
inside its unread SKILL.md.

## B00 — cold open (BrutalistHesitantWriter)
You'd guess Claude decides who gets hired once it picks up a skill called
hiring-review. It doesn't — it follows a written checklist. Let's see
what's actually inside that file.

## Act I — the wrong guess

**B01 — Sounds like hiring authority**
Hear "Claude has a hiring-review skill" and it sounds like Claude itself
got hiring authority — like it can screen candidates and decide who moves
forward.

**B02 — Broken, with a case** (pays off B00)
But nothing in the model changes. Delete the skill's folder and Claude
doesn't lose any hiring judgment — there was none to begin with. It just
stops following that one checklist.

## Act II — the mechanism

**B03 — One file** (ANCHOR PLANTED)
Here's what a skill actually is: one file. Hiring-review, for instance, is
a folder holding a single SKILL.md — instructions for walking through a
hiring decision step by step, written in plain language Claude reads before
it starts.

**B04 — Read it, then follow it in order**
Claude reads that file top to bottom and works through it step by step, in
the order it's written — no branching, unless the file itself says branch.

**B05 — Spec, not judgment**
That makes a skill a specification, not new judgment. The payoff: the same
checklist, every review, every time. The limit: anything outside those
written steps, and Claude has no special opinion about it.

**B06 — The anchor returns** (ANCHOR PAYOFF)
So hiring-review never gave Claude judgment about who to hire. It just
guarantees that every time hiring-review runs, Claude reads that same file
and follows the same checklist — that's the whole trick.

## Act III — both directions

**B07 — Neither one is proof**
Watching Claude flag every risk in a hiring decision doesn't prove it
understood the situation — a checklist can be followed to the letter and
still miss what it was never asked to check. And watching it flag nothing
doesn't prove the hire is clean — it may just be a case the checklist
doesn't cover.

## Close

**BCRY — carry-out**
A skill named hiring-review doesn't hand Claude judgment about who to
hire — it's a checklist Claude reads before it starts, so the same steps
run every time, and anything outside those steps is still on you.

**BHTF — your turn**
Your turn. Paste this into Claude: pick one decision you check the same way
every time — before an offer goes out, before a candidate moves to the
next round. Write me a SKILL.md for it: plain language, ordered steps. Then
read it back to me and walk me through exactly what you'll check, before
you check it.

**BOUT — outro**
Claude, Hiring Review. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–B01 | "a hiring-review skill" sounds like the model gained hiring authority |
| Wrong guess | B00 → B02 | "decides" corrected to "checks"; broken with the delete-the-folder case |
| Mechanism | B03–B05 | one file, read top to bottom, spec not judgment |
| Anchor | B03 → B06 | hiring-review's single SKILL.md, planted then returned to |
| Both directions | B07 | flagging every risk proves nothing about understanding; flagging nothing proves nothing about a clean hire |
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
a small, proportionate expansion of a 7-beat source, not a scale mismatch
(matches the identical-shape expansion on the `claude-for-legal--claude-
liam-case-brief` sibling redo, which hit the same source-fidelity gap). No
employment-law-specific fact was invented anywhere in this expansion.

## One-flag audit

No inference-flag beat: every claim here is about the generic, verifiable
mechanism of a Claude skill (folder + SKILL.md, read-then-execute,
specification semantics) — not an inference about an unread source. Nothing
in this script asserts what hiring-review's specific employment-legal
checklist actually contains.
