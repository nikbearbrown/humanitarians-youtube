# SCRIPT.md — Claude, Investigation Memo. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-investigation-memo` (Teardown, skill-teardown format) —
question and true generic facts carried over; narration re-registered to
Plain (explain, then stop); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

**Source-fidelity note:** the source never filled in investigation-memo's
specific task line — a literal `>` placeholder survives in two spots (B03
body, BHTF command), and a related truncated sentence ("Draft or update the
privileged investigation memo from the.") sits unfinished in B00's output
and BVDT's artifactLines. Its SKILL.md is not reachable from this machine
(see QUESTION.md / BUILD-LOG.md). This script keeps every fact the source
DOES establish — a skill is a folder Claude reads before it acts; it
executes the file's steps in order; it is a specification with a payoff and
a limit — and uses "investigation-memo" only as the named anchor example (a
skill-shaped folder aimed at writing up an investigation in a fixed
structure), never asserting invented detail about the actual
employment-legal procedure inside its unread SKILL.md.

## B00 — cold open (BrutalistHesitantWriter)
You'd guess Claude decides what really happened once it picks up a skill
called investigation-memo. It doesn't — it follows a written template.
Let's see what's actually inside that file.

## Act I — the wrong guess

**B01 — Sounds like investigative authority**
Hear "Claude has an investigation-memo skill" and it sounds like Claude
itself got investigative authority — like it can determine what happened
and who's responsible.

**B02 — Broken, with a case** (pays off B00)
But nothing in the model changes. Delete the skill's folder and Claude
doesn't lose any investigative judgment — there was none to begin with. It
just stops following that one template.

## Act II — the mechanism

**B03 — One file** (ANCHOR PLANTED)
Here's what a skill actually is: one file. Investigation-memo, for
instance, is a folder holding a single SKILL.md — instructions for writing
up an investigation in a fixed structure, written in plain language Claude
reads before it starts.

**B04 — Read it, then follow it in order**
Claude reads that file top to bottom and works through it step by step, in
the order it's written — no branching, unless the file itself says branch.

**B05 — Spec, not judgment**
That makes a skill a specification, not new judgment. The payoff: the same
memo structure, every investigation, every time. The limit: anything
outside those written steps, and Claude has no special opinion about it.

**B06 — The anchor returns** (ANCHOR PAYOFF)
So investigation-memo never gave Claude judgment about what happened. It
just guarantees that every time investigation-memo runs, Claude reads that
same file and follows the same structure — that's the whole trick.

## Act III — both directions

**B07 — Neither one is proof**
Watching Claude produce a thorough memo doesn't prove it correctly
understood the investigation — it may have just filled in the template's
headings. And watching it produce a thin memo doesn't prove there's nothing
there — it may be a case the template's steps don't reach.

## Close

**BCRY — carry-out**
A skill named investigation-memo doesn't hand Claude judgment about what
happened — it's a template Claude reads before it starts, so the same
structure comes out every time, and anything outside those steps is still
on you.

**BHTF — your turn**
Your turn. Paste this into Claude: pick one document you always structure
the same way — an incident report, a status update, a closing summary.
Write me a SKILL.md for it: plain language, ordered steps. Then read it
back to me and walk me through exactly what you'll write, before you write
it.

**BOUT — outro**
Claude, Investigation Memo. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–B01 | "an investigation-memo skill" sounds like the model gained investigative authority |
| Wrong guess | B00 → B02 | "decides" corrected to "documents"; broken with the delete-the-folder case |
| Mechanism | B03–B05 | one file, read top to bottom, spec not judgment |
| Anchor | B03 → B06 | investigation-memo's single SKILL.md, planted then returned to |
| Both directions | B07 | a thorough memo proves nothing about understanding; a thin memo proves nothing about a clean case |
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
liam-hiring-review` sibling redo, which hit the same source-fidelity gap).
No employment-law-specific fact was invented anywhere in this expansion.

## One-flag audit

No inference-flag beat: every claim here is about the generic, verifiable
mechanism of a Claude skill (folder + SKILL.md, read-then-execute,
specification semantics) — not an inference about an unread source. Nothing
in this script asserts what investigation-memo's specific employment-legal
procedure actually contains.
