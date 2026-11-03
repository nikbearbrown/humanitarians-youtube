# SCRIPT.md — Claude, Investigation Summary. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-investigation-summary` (Teardown, skill-teardown
format) — question and true generic facts carried over; narration
re-registered to Plain (explain, then stop); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

**Source-fidelity note:** the source never filled in the skill's specific
"Claude's job: ___" line (literal `>` placeholder survives in four spots),
and its SKILL.md is not reachable from this machine (see QUESTION.md /
BUILD-LOG.md). Unlike a fully-blank gap, one real sentence DOES survive:
the source's own B00 states the skill's job plainly — "Draft an
audience-specific summary from the privileged investigation." This script
builds entirely from that one sentence plus the generic, verifiable
mechanics of any Claude skill (folder + SKILL.md, read-then-execute,
specification semantics), never asserting invented procedural detail about
the actual unread employment-legal SKILL.md.

## B00 — cold open (BrutalistHesitantWriter)
You'd guess a skill called investigation-summary writes one summary for
everyone. It doesn't — it changes per audience. Let's see what should
actually change.

## Act I — the wrong guess

**B01 — Sounds like one clean write-up**
Hear "Claude has an investigation-summary skill" and it sounds like one
clean write-up of what happened — the same document, handed to whoever
asks for it.

**B02 — Broken, with a case** (pays off B00)
But the investigation is privileged, and not every reader is entitled to
the same amount of it. Send the version written for outside counsel to the
workforce, and you'd hand over the very analysis the privilege exists to
protect.

## Act II — the mechanism

**B03 — One file** (ANCHOR PLANTED)
Here's what the skill actually is: one file. investigation-summary is a
folder holding a single SKILL.md — instructions for drafting an
audience-specific summary from one underlying privileged investigation,
written in plain language Claude reads before it starts.

**B04 — Read it, then follow it in order**
Claude reads that file top to bottom and works through it step by step:
read the investigation record, draft to the audience it's given, return
that one output — no branching, unless the file itself says branch.

**B05 — Spec, not judgment**
That makes it a specification, not judgment about privilege. The payoff:
the same audience gets the same shape of summary, every run. The limit: a
reader the file never anticipated gets no guidance on where the line
should sit.

**B06 — The anchor returns** (ANCHOR PAYOFF)
So investigation-summary never writes "the" summary of an investigation.
It writes one summary, once per audience, drawn from the same privileged
record each time — the file, not the reader, decides where the line falls.

## Act III — both directions

**B07 — Neither one is proof**
A summary that reads as plain fact doesn't prove privileged material was
stripped out — it might just be a case with little to redact. And a
summary that withholds a lot doesn't prove the boundary was drawn right —
it might have cut more, or less, than that audience was owed.

## Close

**BCRY — carry-out**
investigation-summary never hands out one summary of an investigation — it
draws a different line for each audience from the same privileged record,
so what one reader sees is never a safe stand-in for what another gets.

**BHTF — your turn**
Your turn. Paste this into Claude: pick one document from work I need to
share with two different audiences. Write me a SKILL.md that defines what
each audience should and shouldn't see from it — then read it back to me
and walk me through exactly what you'll do, before you do it.

**BOUT — outro**
Claude, Investigation Summary. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–B01 | "an investigation-summary skill" sounds like one clean write-up for everyone |
| Wrong guess | B00 → B02 | "everyone" corrected to "each audience"; broken with the leaked-privilege case |
| Mechanism | B03–B05 | one file, read top to bottom, spec not judgment |
| Anchor | B03 → B06 | investigation-summary's single SKILL.md, planted then returned to |
| Both directions | B07 | plain-fact prose proves nothing about stripping; heavy redaction proves nothing about correctness |
| Carry-out | BCRY | one sentence, survives repetition |

## Beat-count note (redo)

Source is 7 beats (B00, B01 anatomy, B02 pipeline, B03 design tell, BVDT
verdict, BHTF your-turn, BOUT outro) — a compact skill-teardown format with
no explicit wrong-guess, anchor, or both-directions beat. hai-simple's
spine requires all three as their own beats (WRONG-GUESS LAW / ANCHOR LAW /
BOTH-DIRECTIONS LAW), so this redo expands modestly: B01 (stakes) and B02
(wrong guess, broken) are new; B03/B04/B05 carry the source's anatomy/
pipeline/design-tell facts across to the anchor; B06 is a new anchor-payoff
beat restating the design tell against the named anchor; B07 (both
directions) is new. Result: B00 + 7 body beats + BCRY/BHTF/BOUT = 11
beats — a small, proportionate expansion of a 7-beat source, identical in
shape to the `claude-for-legal--claude-liam-case-brief` and `-build-guide`
sibling redos, which hit the same source-fidelity gap. No new legal-specific
fact was invented anywhere in this expansion beyond the one sentence the
source itself supplies (audience-specific summary from a privileged
investigation) and the generic, well-known meaning of "privileged."

## One-flag audit

No inference-flag beat: every claim here is either (a) the generic,
verifiable mechanism of a Claude skill (folder + SKILL.md, read-then-
execute, specification semantics), or (b) the source's own stated job for
this skill (an audience-specific summary from a privileged investigation)
plus the generic, well-known meaning of legal privilege — that not every
reader is entitled to the same amount of privileged material. Nothing in
this script asserts what investigation-summary's specific employment-legal
procedure actually does.
