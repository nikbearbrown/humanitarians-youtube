# SCRIPT.md — Claude, Gaps. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-gaps` (Teardown, skill-teardown format) — question and
true facts carried over verbatim from the source narration; narration
re-registered to Plain (explain, then stop); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

**Source-fidelity note:** the source narration already states gaps's real
spec, verbatim: "Open gaps tracker — what's flagged and not yet closed. Use
when the user asks 'what gaps are open', 'gap tracker', 'remediation
status', or wants to close (--close GAP-ID) or risk-accept (--accept
GAP-ID) a tracked gap." That sentence is used here as the anchor fact. The
underlying SKILL.md file is not reachable from this machine (see
QUESTION.md / BUILD-LOG.md); nothing beyond the stated spec is asserted.

## B00 — cold open (BrutalistHesitantWriter)
You'd guess Claude learned to judge compliance risk from a skill called
gaps. It didn't — it was handed a file of instructions. Gaps just names one
such file. Let's see what's actually inside it.

## Act I — the wrong guess

**B01 — Sounds like judgment**
Hear "Claude has a gaps skill" and it sounds like it can now weigh
regulations and decide what counts as a compliance gap on its own.

**B02 — Broken, with a case** (pays off B00)
But nothing in the model changes. Delete the skill's folder and Claude
loses no compliance judgment — there was none to lose. It just stops
following that one tracking routine.

## Act II — the mechanism

**B03 — One file** (ANCHOR PLANTED)
Here's what a skill actually is: one file. Gaps, for instance, is a folder
holding a single SKILL.md — instructions for opening a tracker, reporting
what's flagged and not yet closed, and updating an item when you close it
or risk-accept it.

**B04 — Read it, then follow it in order**
Claude reads that file top to bottom and works through it step by step, in
the order it's written — no branching, unless the file itself says branch.

**B05 — Spec, not power**
That makes a skill a specification, not a new power. The payoff: the same
tracker check, every time — what's open, what's closed, what's been
risk-accepted. The limit: anything outside those written steps, and Claude
is off the map.

**B06 — The anchor returns** (ANCHOR PAYOFF)
So gaps never taught Claude how to judge a compliance risk. It just
guarantees that every time gaps runs, Claude reads that same file and
reports the tracker the same way — that's the whole trick.

## Act III — both directions

**B07 — Neither one is proof**
Watching Claude close out a gap cleanly doesn't prove it understood the
underlying risk — a file can be followed to the letter on a case it never
really evaluated. And watching it mishandle a tracker update doesn't prove
the skill is broken — it may just be a case the file's steps don't cover.

## Close

**BCRY — carry-out**
A skill doesn't teach Claude how to judge compliance risk — it's a file of
steps Claude reads before it starts, so every tracker check comes out the
same way, every time.

**BHTF — your turn**
Your turn. Paste this into Claude: pick one status check I run the same way
every time. Write me a SKILL.md for it — plain language, ordered steps —
then read it back to me and walk me through exactly what you'll do, before
you do it.

**BOUT — outro**
Claude, Gaps. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–B01 | "a gaps skill" sounds like Claude can now judge compliance risk |
| Wrong guess | B00 → B02 | "learned" corrected to "was given"; broken with the delete-the-folder case |
| Mechanism | B03–B05 | one file, read top to bottom, spec not power |
| Anchor | B03 → B06 | gaps's single SKILL.md, planted then returned to |
| Both directions | B07 | a clean close proves nothing about understanding; a mishandled update proves nothing about breakage |
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
the `claude-for-legal--claude-liam-case-brief` sibling redo. No fact beyond
the source's own stated spec (open tracker, report flagged/unclosed items,
close or risk-accept) is invented anywhere in this expansion.

## One-flag audit

No inference-flag beat: every claim here is about the generic, verifiable
mechanism of a Claude skill (folder + SKILL.md, read-then-execute,
specification semantics) plus gaps's own stated spec text, carried over
verbatim from the source narration. Nothing asserts how the unread SKILL.md
internally decides what counts as a "gap."
