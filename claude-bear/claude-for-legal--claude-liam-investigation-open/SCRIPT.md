# SCRIPT.md — Claude, Investigation Open. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-investigation-open` (Teardown, skill-teardown
format) — question and true generic facts carried over; narration
re-registered to Plain (explain, then stop); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

**Source-fidelity note:** the source never filled in investigation-open's
specific "Claude's job: ___" line (literal `>` placeholder survives in
three spots), and its SKILL.md is not reachable from this machine (see
QUESTION.md / BUILD-LOG.md) — same defect class as the `case-brief`,
`hiring-review`, `internal-investigation`, and `investigation-add` sibling
redos. One fact fragment survived intact in both B00 and BVDT: "Open a new
internal investigation matter — runs intake,". This script keeps every
fact the source DOES establish — a skill is a folder Claude reads before
it acts; it executes the file's steps in order; it is a specification with
a payoff and a limit — plus that one surviving fragment (opens a new
matter, runs intake), and uses "investigation-open" only as the named
anchor example, never asserting invented detail about the actual
employment-law intake procedure inside its unread SKILL.md.

## B00 — cold open (BrutalistHesitantWriter)
You'd guess Claude launches a new investigation on its own once it picks
up a skill called investigation-open. It doesn't — it opens the case file
and runs intake. Let's see what's inside that file.

## Act I — the wrong guess

**B01 — Sounds like investigative authority**
Hear "Claude has an investigation-open skill" and it sounds like Claude
itself decides when a workplace issue becomes an investigation.

**B02 — Broken, with a case** (pays off B00)
But nothing in the model changes. Delete the skill's folder and Claude
doesn't lose any power to decide when to investigate — it never had that
power. It just stops running that one intake checklist.

## Act II — the mechanism

**B03 — One file** (ANCHOR PLANTED)
Here's what a skill actually is: one file. Investigation-open, for
instance, is a folder holding a single SKILL.md — instructions for opening
a new investigation matter and running intake, written in plain language
Claude reads before it starts.

**B04 — Read it, then follow it in order**
Claude reads that file top to bottom and works through it step by step, in
the order it's written — no branching, unless the file itself says branch.

**B05 — Spec, not judgment**
That makes a skill a specification, not new judgment. The payoff: the same
intake, every matter, every time. The limit: anything outside those
written steps, and Claude has no special opinion about it.

**B06 — The anchor returns** (ANCHOR PAYOFF)
So investigation-open never gave Claude the power to decide when to
investigate. It just guarantees that every time investigation-open runs,
Claude reads that same file and opens the matter and runs intake the same
way — that's the whole trick.

## Act III — both directions

**B07 — Neither one is proof**
Watching Claude open a matter and run a thorough intake doesn't prove it
judged the underlying issue correctly — a checklist can be followed to the
letter and still miss what it was never asked to check. And watching it
leave a matter unopened doesn't prove nothing's wrong — it may just be a
case nobody asked it to open.

## Close

**BCRY — carry-out**
A skill named investigation-open doesn't hand Claude the power to decide
when to investigate — it's a checklist Claude reads before it starts, so
the same matter gets opened and the same intake runs every time, and
anything outside those steps is still on you.

**BHTF — your turn**
Your turn. Paste this into Claude: pick one recurring record you open the
same way every time — a support ticket, an incident report, a new client
file. Write me a SKILL.md for it: plain language, ordered steps. Then read
it back to me and walk me through exactly what you'll open and log, before
you open it.

**BOUT — outro**
Claude, Investigation Open. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–B01 | "an investigation-open skill" sounds like the model gained the power to decide when to investigate |
| Wrong guess | B00 → B02 | "launches" corrected to "opens"; broken with the delete-the-folder case |
| Mechanism | B03–B05 | one file, read top to bottom, spec not judgment |
| Anchor | B03 → B06 | investigation-open's single SKILL.md, planted then returned to |
| Both directions | B07 | opening a matter and running intake proves nothing about judgment; leaving one unopened proves nothing about no wrongdoing |
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
investigation`/`investigation-add` sibling redos, which hit the same
source-fidelity gap. No employment-law-specific fact was invented anywhere
in this expansion; the one surviving fact fragment ("open a new internal
investigation matter — runs intake") anchors B03/B06.

## One-flag audit

No inference-flag beat: every claim here is about the generic, verifiable
mechanism of a Claude skill (folder + SKILL.md, read-then-execute,
specification semantics) plus the one surviving fact fragment from the
source — not an inference about an unread source. Nothing in this script
asserts what investigation-open's specific employment-law intake procedure
actually contains beyond "opens a matter, runs intake."
