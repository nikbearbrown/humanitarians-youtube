# SCRIPT.md — Claude, Form Generation. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-form-generation` (Teardown, skill-teardown format) —
question and true generic facts carried over; narration re-registered to
Plain (explain, then stop); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

**Source-fidelity note:** the source never filled in form-generation's
specific "Claude's job: ___" line (literal `>` placeholder survives in four
spots), and its SKILL.md is not reachable from this machine (see
QUESTION.md / BUILD-LOG.md). This script keeps every fact the source DOES
establish — a skill is a folder Claude reads before it acts; it executes
the file's steps in order; it is a specification with a payoff and a
limit — and uses "form-generation" only as the named anchor example (a
skill-shaped folder aimed at filling a form's fields from case facts),
never asserting invented detail about the actual legal-clinic procedure
inside its unread SKILL.md.

## B00 — cold open (BrutalistHesitantWriter)
You'd guess Claude designed the legal form itself, using a skill called
form-generation. It didn't — it was handed a file of instructions.
Form-generation just names one such file. Let's see what's actually inside
it.

## Act I — the wrong guess

**B01 — Sounds like a drafting upgrade**
Hear "Claude has a form-generation skill" and it sounds like a drafting
upgrade — like it can compose any legal form from a blank page.

**B02 — Broken, with a case** (pays off B00)
But nothing about drafting changes. Delete the skill's folder and Claude
can still write a sentence — it just stops following that one fixed
checklist of fields for this particular form.

## Act II — the mechanism

**B03 — One file** (ANCHOR PLANTED)
Here's what a skill actually is: one file. Form-generation, for instance,
is a folder holding a single SKILL.md — instructions for which fields a
form needs and where the case facts go, written in plain language Claude
reads before it starts.

**B04 — Read it, then follow it in order**
Claude reads that file top to bottom and fills each field in the order
it's listed — no branching, unless the file itself says branch.

**B05 — Spec, not power**
That makes a skill a specification, not drafting talent. The payoff: the
same field layout, every form. The limit: any field the file never
listed, and Claude has no instructions for it.

**B06 — The anchor returns** (ANCHOR PAYOFF)
So form-generation never taught Claude how to draft a legal document from
nothing. It just guarantees that every time it runs, Claude reads that
same checklist and fills the same fields, in the same order — that's the
whole trick.

## Act III — both directions

**B07 — Neither one is proof**
Watching Claude fill out a clean form doesn't prove it understood the
underlying request — it may have just followed the checklist on a case it
never really parsed. And watching it leave a field wrong or empty doesn't
prove the skill is broken — it may be a case that checklist doesn't cover.

## Close

**BCRY — carry-out**
A skill doesn't teach Claude to draft a legal document from nothing — it's
a checklist of fields Claude reads before it starts, so every form comes
out with the same structure, every time.

**BHTF — your turn**
Your turn. Paste this into Claude: pick one form or document I fill out
the same way every time. Write me a SKILL.md for it — plain language, the
fields in order — then read it back to me and walk me through exactly what
you'll do, before you do it.

**BOUT — outro**
Claude, Form Generation. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–B01 | "a form-generation skill" sounds like a drafting upgrade |
| Wrong guess | B00 → B02 | "designs" corrected to "was given"; broken with the delete-the-folder case |
| Mechanism | B03–B05 | one file, read top to bottom, spec not power |
| Anchor | B03 → B06 | form-generation's single SKILL.md, planted then returned to |
| Both directions | B07 | a clean form proves nothing about understanding; a wrong field proves nothing about breakage |
| Carry-out | BCRY | one sentence, survives repetition |

## Beat-count note (redo)

Source is 7 beats (B00, B01 anatomy, B02 pipeline, B03 design tell, BVDT
verdict, BHTF your-turn, BOUT outro) — a compact skill-teardown format with
no explicit wrong-guess, anchor, or both-directions beat. hai-simple's
spine requires all three as their own beats (WRONG-GUESS LAW / ANCHOR LAW /
BOTH-DIRECTIONS LAW), so this redo expands modestly: B01 (stakes) and B02
(wrong guess, broken) are new; B03/B04/B05 carry the source's
anatomy/pipeline/design-tell facts across to the anchor; B06 is a new
anchor-payoff beat restating the design tell against the named anchor; B07
(both directions) is new. Result: B00 + 7 body beats + BCRY/BHTF/BOUT = 11
beats — a small, proportionate expansion of a 7-beat source, identical in
shape to the `claude-for-legal--claude-liam-case-brief` sibling redo, which
hit the same source-fidelity gap. No new legal-specific fact was invented
anywhere in this expansion beyond the well-known generic shape of a
fillable legal form (parties, dates, signatures).

## One-flag audit

No inference-flag beat: every claim here is about the generic, verifiable
mechanism of a Claude skill (folder + SKILL.md, read-then-execute,
specification semantics) plus the well-known, generic shape of a fillable
legal form — not an inference about an unread source. Nothing in this
script asserts what form-generation's specific legal-clinic procedure
actually fills or how.
