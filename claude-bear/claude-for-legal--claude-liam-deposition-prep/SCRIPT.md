# SCRIPT.md — Claude, Deposition Prep. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-deposition-prep` (Teardown, skill-teardown format) —
question and true, specific facts carried over verbatim; narration
re-registered to Plain (explain, then stop); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

**Source-fidelity note:** the source's beat sheet DOES carry deposition-prep's
real, specific description in full — "Build a deposition outline for a
witness — pull their documents from the eDiscovery platform, organize topics
around the case theory, and surface impeachment material" — present in B00,
B03, and BVDT. This redo keeps that description verbatim as the mechanism
beats' content; nothing about deposition-prep's actual procedure is invented.

## B00 — cold open (BrutalistHesitantWriter)
You'd guess Claude knows how to prep a deposition on its own. It doesn't —
it was handed a file of steps. Deposition-prep just names one such file.
Let's see what's actually inside it.

## Act I — the wrong guess

**B01 — Sounds like courtroom instinct**
Hear "Claude has a deposition-prep skill" and it sounds like real courtroom
instinct — like it studied depositions and came back knowing how to corner
a witness.

**B02 — Broken, with a case** (pays off B00)
But nothing in the model changes. Delete the skill's folder and Claude
doesn't forget how to question a witness — there was no instinct to lose.
It just stops following that one checklist.

## Act II — the mechanism

**B03 — One file** (ANCHOR PLANTED)
Here's what a skill actually is: one file. Deposition-prep, for instance, is
a folder holding a single SKILL.md — steps for pulling a witness's documents
from the eDiscovery platform, organizing them around the case theory, and
surfacing impeachment material, written in plain language Claude reads
before it starts.

**B04 — Read it, then follow it in order**
Claude reads that file top to bottom and works through it step by step, in
the order it's written — pull documents, sort by case theory, flag
impeachment material — no branching unless the file itself says branch.

**B05 — Spec, not instinct**
That makes a skill a specification, not courtroom judgment. The payoff: the
same organized outline, every witness. The limit: any question outside
those written steps, and Claude is off the map.

**B06 — The anchor returns** (ANCHOR PAYOFF)
So deposition-prep never taught Claude how to cross-examine anyone. It just
guarantees that every time it runs, Claude reads that same file and produces
the same organized outline — that's the whole trick.

## Act III — both directions

**B07 — Neither one is proof**
Watching Claude produce a sharp outline doesn't prove it understood the
witness — a file can be followed to the letter on a case it never really
grasped. And watching it produce a thin outline doesn't prove the skill is
broken — it may just be a case the file's structure doesn't fit.

## Close

**BCRY — carry-out**
A skill doesn't teach Claude how to depose a witness — it's a file of steps
Claude reads before it starts, so every outline comes out organized the
same way, every time.

**BHTF — your turn**
Your turn. Paste this into Claude: pick a task you do the same way every
time — an outline, a report, a checklist. Write me a SKILL.md for it — plain
language, ordered steps — then read it back to me and walk me through
exactly what you'll do, before you do it.

**BOUT — outro**
Claude, Deposition Prep. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–B01 | "a deposition-prep skill" sounds like the model gained courtroom instinct |
| Wrong guess | B00 → B02 | "knows" corrected to "was given steps for"; broken with the delete-the-folder case |
| Mechanism | B03–B05 | one file, read top to bottom, spec not instinct |
| Anchor | B03 → B06 | deposition-prep's single SKILL.md, planted then returned to |
| Both directions | B07 | a sharp outline proves nothing about understanding; a thin one proves nothing about breakage |
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
a small, proportionate expansion of a 7-beat source, identical in shape to
the `claude-for-legal--claude-liam-case-brief` sibling redo. No fact about
deposition-prep's actual procedure was invented anywhere in this expansion —
the eDiscovery/case-theory/impeachment-material description is the source's
own verbatim wording.

## One-flag audit

No inference-flag beat: every claim here is either the generic, verifiable
mechanism of a Claude skill (folder + SKILL.md, read-then-execute,
specification semantics) or deposition-prep's own stated description,
carried over verbatim from the source. Nothing here is an inference about
an unread file — the description IS present in the source, in full.
