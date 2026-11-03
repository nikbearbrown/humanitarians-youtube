# SCRIPT.md — Claude, Log Leave. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-log-leave` (Teardown, skill-teardown format) — question
and true generic facts carried over; narration re-registered to Plain
(explain, then stop); cold open replaced with the BrutalistHesitantWriter;
close carries the Humanitarians AI skin.

**Source-fidelity note:** the source never filled in log-leave's specific
"Claude's job: ___" line (literal `>` placeholder survives in four spots —
B00, B03, BVDT, BHTF), and its SKILL.md is not reachable from this machine
(see QUESTION.md / BUILD-LOG.md). This script keeps every fact the source
DOES establish — a skill is a folder Claude reads before it acts; it
executes the file's steps in order; it is a specification with a payoff and
a limit — and uses "log-leave" only as the named anchor example (a
skill-shaped folder aimed at logging an employee's leave record), never
asserting invented detail about the actual employment-legal leave procedure
inside its unread SKILL.md.

## B00 — cold open (BrutalistHesitantWriter)
You'd guess Claude can approve an employee's leave request once it picks up
a skill called log-leave. It doesn't — it follows a written checklist.
Let's see what's inside that file.

## Act I — the wrong guess

**B01 — Sounds like approval authority**
Hear "Claude has a log-leave skill" and it sounds like Claude itself can
decide whether to approve someone's leave — like it's making the call.

**B02 — Broken, with a case** (pays off B00)
But nothing in the model changes. Delete the skill's folder and Claude
doesn't lose any approval authority — there was none to begin with. It just
stops following that one checklist for logging a leave request.

## Act II — the mechanism

**B03 — One file** (ANCHOR PLANTED)
Here's what a skill actually is: one file. Log-leave, for instance, is a
folder holding a single SKILL.md — instructions for logging a leave request
step by step, written in plain language Claude reads before it starts.

**B04 — Read it, then follow it in order**
Claude reads that file top to bottom and works through it step by step, in
the order it's written — no branching, unless the file itself says branch.

**B05 — Spec, not judgment**
That makes a skill a specification, not new judgment. The payoff: the same
log entry, every leave request, every time. The limit: anything outside
those written steps — like whether the leave even qualifies — and Claude
has no special opinion about it.

**B06 — The anchor returns** (ANCHOR PAYOFF)
So log-leave never gave Claude authority to approve a request. It just
guarantees that every time log-leave runs, Claude reads that same file and
logs the leave the same way — that's the whole trick.

## Act III — both directions

**B07 — Neither one is proof**
Watching Claude log a leave request cleanly doesn't prove it judged the
situation correctly — a checklist can be followed to the letter and still
miss what it was never asked to check. And watching it flag something as
incomplete doesn't prove nothing's wrong — it may just be a case the
checklist doesn't cover.

## Close

**BCRY — carry-out**
A skill named log-leave doesn't hand Claude authority to approve or judge a
leave request — it's a checklist Claude reads before it starts, so the same
entry gets logged every time, and anything outside those steps is still on
you.

**BHTF — your turn**
Your turn. Paste this into Claude: pick one record you log the same way
every time — a time-off request, an expense entry, a status update. Write
me a SKILL.md for it: plain language, ordered steps. Then read it back to
me and walk me through exactly what you'll log, before you log it.

**BOUT — outro**
Claude, Log Leave. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–B01 | "a log-leave skill" sounds like the model gained authority to approve a request |
| Wrong guess | B00 → B02 | "approves" corrected to "logs"; broken with the delete-the-folder case |
| Mechanism | B03–B05 | one file, read top to bottom, spec not judgment |
| Anchor | B03 → B06 | log-leave's single SKILL.md, planted then returned to |
| Both directions | B07 | logging cleanly proves nothing about judging right; flagging something incomplete proves nothing's wrong |
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
(matches the identical-shape expansion on the sibling `claude-for-legal`
redos, which hit the same source-fidelity gap). No employment-law-specific
fact was invented anywhere in this expansion.

## One-flag audit

No inference-flag beat: every claim here is about the generic, verifiable
mechanism of a Claude skill (folder + SKILL.md, read-then-execute,
specification semantics) — not an inference about an unread source. Nothing
in this script asserts what log-leave's specific employment-legal leave
procedure actually contains.
