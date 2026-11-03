# SCRIPT.md — Claude, Expansion Kickoff. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-expansion-kickoff` (Teardown, skill-teardown format) —
question and true generic facts carried over; narration re-registered to
Plain (explain, then stop); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

**Source-fidelity note:** the source never filled in expansion-kickoff's
specific "Claude's job: ___" line (literal `>` placeholder survives in four
spots), and its SKILL.md is not reachable from this machine (see
QUESTION.md / BUILD-LOG.md). This script keeps every fact the source DOES
establish — a skill is a folder Claude reads before it acts; it executes the
file's steps in order; it is a specification with a payoff and a limit —
and uses "expansion-kickoff" only as the named anchor example (a
skill-shaped folder aimed at starting a structured checklist), never
asserting invented detail about the actual legal-team procedure inside its
unread SKILL.md.

## B00 — cold open (BrutalistHesitantWriter)
You'd guess Claude learned expansion planning from a skill called
expansion-kickoff. It didn't — it was handed a file of instructions.
Expansion-kickoff just names one such file. Let's see what's actually
inside it.

## Act I — the wrong guess

**B01 — Sounds like a strategy upgrade**
Hear "Claude has an expansion-kickoff skill" and it sounds like a strategy
upgrade — like it studied business expansions and came back knowing
something it didn't before.

**B02 — Broken, with a case** (pays off B00)
But nothing in the model changes. Delete the skill's folder and Claude
doesn't forget how to plan an expansion — there was nothing to learn. It
just stops following that one routine.

## Act II — the mechanism

**B03 — One file** (ANCHOR PLANTED)
Here's what a skill actually is: one file. Expansion-kickoff, for instance,
is a folder holding a single SKILL.md — instructions for starting a
structured checklist when a team or business expands somewhere new,
written in plain language Claude reads before it starts.

**B04 — Read it, then follow it in order**
Claude reads that file top to bottom and works through it step by step, in
the order it's written — no branching, unless the file itself says branch.

**B05 — Spec, not power**
That makes a skill a specification, not a new power. The payoff: the same
checklist, every kickoff — the same starting steps, every time. The limit:
anything outside those written steps, and Claude is off the map.

**B06 — The anchor returns** (ANCHOR PAYOFF)
So expansion-kickoff never taught Claude how to run a real expansion. It
just guarantees that every time expansion-kickoff runs, Claude reads that
same file and starts the same structured checklist — that's the whole
trick.

## Act III — both directions

**B07 — Neither one is proof**
Watching Claude produce a tidy kickoff plan doesn't prove it understood the
business — a file can be followed to the letter on a situation it never
really grasped. And watching it produce a rough plan doesn't prove the
skill is broken — it may just be a case the file's checklist doesn't fit.

## Close

**BCRY — carry-out**
A skill doesn't teach Claude how to run an expansion — it's a file of steps
Claude reads before it starts, so every kickoff comes out with the same
checklist, every time.

**BHTF — your turn**
Your turn. Paste this into Claude: pick one process I repeat every time I
start something new. Write me a SKILL.md for it — plain language, ordered
steps — then read it back to me and walk me through exactly what you'll
do, before you do it.

**BOUT — outro**
Claude, Expansion Kickoff. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–B01 | "an expansion-kickoff skill" sounds like the model learned expansion planning |
| Wrong guess | B00 → B02 | "learned" corrected to "was given"; broken with the delete-the-folder case |
| Mechanism | B03–B05 | one file, read top to bottom, spec not power |
| Anchor | B03 → B06 | expansion-kickoff's single SKILL.md, planted then returned to |
| Both directions | B07 | a tidy plan proves nothing about understanding; a rough one proves nothing about breakage |
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
new domain-specific fact was invented anywhere in this expansion beyond the
generic, well-known idea of a starting checklist.

## One-flag audit

No inference-flag beat: every claim here is about the generic, verifiable
mechanism of a Claude skill (folder + SKILL.md, read-then-execute,
specification semantics) plus the generic, well-known idea of a kickoff
checklist — not an inference about an unread source. Nothing in this script
asserts what expansion-kickoff's specific legal-team procedure actually
does.
