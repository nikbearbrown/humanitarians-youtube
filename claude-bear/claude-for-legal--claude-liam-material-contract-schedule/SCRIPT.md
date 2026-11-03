# SCRIPT.md — Claude, Material Contract Schedule. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-material-contract-schedule` (Teardown, skill-teardown
format) — question and true generic facts carried over; narration
re-registered to Plain (explain, then stop); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

**Source-fidelity note:** the source never filled in this skill's specific
"Claude's job: ___" line (literal `>` placeholder survives in four spots),
and its SKILL.md is not reachable from this machine (see QUESTION.md /
BUILD-LOG.md). This script keeps every fact the source DOES establish — a
skill is a folder Claude reads before it acts; it executes the file's steps
in order; it is a specification with a payoff and a limit — and uses
"material-contract-schedule" only as the named anchor example (a
skill-shaped folder aimed at producing the well-known document shape: a
schedule of contracts material to a deal, built during diligence), never
asserting invented detail about the actual corporate-legal procedure inside
its unread SKILL.md.

## B00 — cold open (BrutalistHesitantWriter)
You'd guess Claude learned contract law from a skill called
material-contract-schedule. It didn't — it was handed a file of
instructions. Material-contract-schedule just names one such file. Let's
see what's actually inside it.

## Act I — the wrong guess

**B01 — Sounds like a deal-review upgrade**
Hear "Claude has a material-contract-schedule skill" and it sounds like a
deal-review upgrade — like it studied M&A contracts and came back knowing
something it didn't before.

**B02 — Broken, with a case** (pays off B00)
But nothing in the model changes. Delete the skill's folder and Claude
doesn't forget contract law — there was nothing to learn. It just stops
following that one routine.

## Act II — the mechanism

**B03 — One file** (ANCHOR PLANTED)
Here's what a skill actually is: one file. Material-contract-schedule, for
instance, is a folder holding a single SKILL.md — instructions for turning
a stack of contracts into a structured disclosure schedule, written in
plain language Claude reads before it starts.

**B04 — Read it, then follow it in order**
Claude reads that file top to bottom and works through it step by step, in
the order it's written — no branching, unless the file itself says branch.

**B05 — Spec, not power**
That makes a skill a specification, not a new power. The payoff: the same
schedule structure, every time — one row per contract, the same columns
filled in. The limit: anything outside those written steps, and Claude is
off the map.

**B06 — The anchor returns** (ANCHOR PAYOFF)
So material-contract-schedule never taught Claude how to judge a contract.
It just guarantees that every time material-contract-schedule runs, Claude
reads that same file and produces the same schedule structure — that's the
whole trick.

## Act III — both directions

**B07 — Neither one is proof**
Watching Claude produce a schedule with every row filled in doesn't prove
every contract was actually checked against the file's criteria — a cell
can be filled in without a fact behind it. And a schedule with gaps in it
doesn't prove the skill is broken — it may just mean the file asked for
something the contracts never said.

## Close

**BCRY — carry-out**
A skill doesn't teach Claude what counts as a material contract — it's a
file of steps Claude reads before it starts, so the schedule comes out in
the same shape, every time.

**BHTF — your turn**
Your turn. Paste this into Claude: pick one document I produce the same
way every time. Write me a SKILL.md for it — plain language, ordered
steps — then read it back to me and walk me through exactly what you'll
do, before you do it.

**BOUT — outro**
Claude, Material Contract Schedule. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–B01 | "a material-contract-schedule skill" sounds like the model learned deal-review judgment |
| Wrong guess | B00 → B02 | "learned" corrected to "was given"; broken with the delete-the-folder case |
| Mechanism | B03–B05 | one file, read top to bottom, spec not power |
| Anchor | B03 → B06 | material-contract-schedule's single SKILL.md, planted then returned to |
| Both directions | B07 | a filled-in schedule proves nothing about completeness; a gappy one proves nothing about breakage |
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
(identical in shape to the `claude-for-legal--claude-liam-case-brief` and
`...-build-guide` sibling redos, which hit the same source-fidelity gap).
No new legal-specific fact was invented anywhere in this expansion beyond
the well-known generic shape of a material contracts disclosure schedule
(a document listing contracts material to a deal, produced during
diligence).

## One-flag audit

No inference-flag beat: every claim here is about the generic, verifiable
mechanism of a Claude skill (folder + SKILL.md, read-then-execute,
specification semantics) plus the well-known, generic shape of a material
contracts disclosure schedule — not an inference about an unread source.
Nothing in this script asserts what material-contract-schedule's specific
corporate-legal procedure actually does.
