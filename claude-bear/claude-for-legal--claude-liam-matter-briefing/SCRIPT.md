# SCRIPT.md — Claude, Matter Briefing. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-matter-briefing` (Teardown, skill-teardown format) —
question and true facts carried over; narration re-registered to Plain
(explain, then stop); cold open replaced with the BrutalistHesitantWriter;
close carries the Humanitarians AI skin.

**Source-fidelity note:** the source SKILL.md is not reachable from this
machine (see QUESTION.md / BUILD-LOG.md), but — unlike the `case-brief`
sibling — the source's own beat_sheet.json narration was fully filled in,
spelling out the job in full: "Deep briefing on one matter — current
posture, what's changed, next deadline, open questions, and a risk
re-assessment check, ready before a GC update or outside counsel call. Use
when the user says 'brief me on [matter]', 'where are we on [matter]', or
needs a read on a specific matter." Every specific claim below about what
matter-briefing produces traces to that sentence. This script never asserts
anything about the unread SKILL.md's internal steps beyond that.

## B00 — cold open (BrutalistHesitantWriter)
You'd guess Claude has been quietly tracking this legal matter as it
develops. It hasn't — it was handed a file on the matter, once, when you
asked. Let's see what's actually inside that file.

## Act I — the wrong guess

**B01 — Sounds like it's been keeping tabs**
Hear "Claude has a matter-briefing skill" and it sounds like it's been
quietly keeping tabs on this case the whole time — building up a memory of
it as things happen.

**B02 — Broken, with a case** (pays off B00)
But there's no ongoing memory to lose. Delete the skill's folder and Claude
doesn't forget one update on this matter — because it was never storing
any. It just stops running that one routine.

## Act II — the mechanism

**B03 — One file** (ANCHOR PLANTED)
Here's what a skill actually is: one file. Matter-briefing is a folder
holding a single SKILL.md — instructions for turning whatever's currently
on record into one structured read: posture, what's changed, next
deadline, open questions, and a risk check.

**B04 — Read it, then follow it in order**
Claude reads that file top to bottom and works through it step by step, in
the order it's written — no branching, unless the file itself says branch.

**B05 — Spec, not power**
That makes a skill a specification, not an ongoing watch. The payoff: the
same five-part read, every time — posture, changes, deadline, questions,
risk. The limit: anything that wasn't already on the record when you asked.

**B06 — The anchor returns** (ANCHOR PAYOFF)
So matter-briefing never gave Claude a memory of this case's history. It
just guarantees that every time it runs, Claude reads that same file and
produces the same five-part read — that's the whole trick.

## Act III — both directions

**B07 — Neither one is proof**
Watching Claude produce a sharp, complete-looking briefing doesn't prove it
caught every development — the file only compiles what's already on
record, and a gap in the record is a gap in the briefing. And a briefing
that misses something obvious doesn't prove the skill is broken — the
record it was given may never have had it.

## Close

**BCRY — carry-out**
A skill doesn't give Claude a memory of the case — it's a file of steps it
runs on whatever's on record right now, so every briefing comes out with
the same five parts, every time.

**BHTF — your turn**
Your turn. Paste this into Claude: pick one thing you brief me on
regularly — a project, a matter, a case. Write me a SKILL.md for it:
current status, what's changed, next deadline, open questions, and risk.
Then read it back to me and walk me through exactly what you'll do, before
you do it.

**BOUT — outro**
Claude, Matter Briefing. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–B01 | "a matter-briefing skill" sounds like ongoing case memory |
| Wrong guess | B00 → B02 | "tracking" corrected to "handed a file on"; broken with the delete-the-folder case |
| Mechanism | B03–B05 | one file, read top to bottom, spec not an ongoing watch |
| Anchor | B03 → B06 | matter-briefing's single SKILL.md, planted then returned to |
| Both directions | B07 | a sharp briefing proves nothing about completeness; a gap proves nothing about the skill being broken |
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
the identical-shape expansion used on the `case-brief` and `gaps` sibling
redos, which hit the same compact-source-format situation. No new
legal-specific fact was invented anywhere in this expansion beyond what the
source's own B00 narration already established.

## One-flag audit

No inference-flag beat: every claim here traces either to the generic,
verifiable mechanism of a Claude skill (folder + SKILL.md, read-then-
execute, specification semantics) or to the source's own fully-stated
description of matter-briefing's job (the five-part read: posture, changes,
deadline, questions, risk). Nothing in this script asserts what the actual,
unread SKILL.md's internal steps are.
