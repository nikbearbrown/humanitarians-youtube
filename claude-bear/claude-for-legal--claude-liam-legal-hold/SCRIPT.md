# SCRIPT.md — Claude, Legal Hold. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-legal-hold` (Teardown, skill-teardown format) — question
and facts carried over; narration re-registered to Plain (explain, then
stop); cold open replaced with the BrutalistHesitantWriter; close carries
the Humanitarians AI skin.

**Source-fidelity note:** the actual `legal-hold` SKILL.md was found and
read in full at
`/Users/nik/Documents/Cowork/anthropics/claude-for-legal/litigation-legal/skills/legal-hold/SKILL.md`
(see QUESTION.md). Every fact below is sourced from it directly, not
reconstructed from the source reel's narration alone.

## B00 — cold open (BrutalistHesitantWriter)
You'd guess Claude decides who's on legal hold, from a skill called
legal-hold. It didn't — it was handed a file of instructions. Legal-hold
just names one such file. Let's see what's actually inside it.

## Act I — the wrong guess

**B01 — Sounds like Claude's call**
Hear "Claude issues legal holds" and it sounds like Claude decides, on its
own, when documents need to be frozen for a lawsuit.

**B02 — Broken, with a case** (pays off B00)
But before it issues or releases a hold, the skill stops and asks: have you
reviewed this with an attorney? Say no, and it hands you a one-page brief to
take to one, instead of sending anything.

## Act II — the mechanism

**B03 — One file** (ANCHOR PLANTED)
Here's what a skill actually is: one file. Legal-hold, for instance, is a
folder holding a single SKILL.md — instructions for drafting the hold
notice, logging the case fields, and calendaring the next refresh, all
written in plain language Claude reads before it starts.

**B04 — Four modes, one file**
That file routes by flag — issue, refresh, release, or status — then
follows that one mode's steps in order: capture the details, draft the
file, update the log.

**B05 — The payoff, and the limit**
The spec draws its own edges too: it drafts, it logs, it calendars — but it
doesn't enforce preservation, doesn't set scope alone, and doesn't send the
notice. A person still does every one of those.

**B06 — The anchor returns** (ANCHOR PAYOFF)
So legal-hold never taught Claude when a lawsuit calls for a hold. It just
guarantees that once a person says issue, refresh, or release, Claude reads
that same file and produces the same notice, the same log update, the same
next date — every time.

## Act III — both directions

**B07 — Neither one is proof**
Watching Claude draft a clean, on-time hold notice doesn't prove it
understood the lawsuit — a file can be followed to the letter on a case it
never grasped. And watching it stall on a request doesn't prove the skill
is broken — it may just be asking for something the written steps don't
cover.

## Close

**BCRY — carry-out**
A legal-hold skill doesn't give Claude legal judgment — it gives it a file
that drafts the notice, then waits for a person to say yes.

**BHTF — your turn**
Your turn. Paste this into Claude: pick one document or process I do the
same way every time. Write me a SKILL.md for it — plain language, ordered
steps — then read it back to me and walk me through exactly what you'll
do, before you do it.

**BOUT — outro**
Claude, Legal Hold. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–B01 | "Claude issues legal holds" sounds like an autonomous legal decision |
| Wrong guess | B00 → B02 | "decides" corrected to "was told"; broken with the SKILL.md's own confirmation-gate quote |
| Mechanism | B03–B05 | one file, four modes routed by flag, explicit payoff/limit from "What this skill does not do" |
| Anchor | B03 → B06 | legal-hold's single SKILL.md, planted then returned to |
| Both directions | B07 | a clean notice proves nothing about understanding; a stall proves nothing about breakage |
| Carry-out | BCRY | one sentence, survives repetition |

## Beat-count note (redo)

Source is 7 beats (B00, B01 anatomy, B02 pipeline, B03 design tell, BVDT
verdict, BHTF your-turn, BOUT outro) — a compact skill-teardown format with
no explicit wrong-guess, anchor, or both-directions beat. hai-simple's spine
requires all three as their own beats (WRONG-GUESS LAW / ANCHOR LAW /
BOTH-DIRECTIONS LAW), so this redo expands modestly, identically in shape to
the `case-brief` and `build-guide` sibling redos: B01 (stakes) and B02
(wrong guess, broken) are new; B03/B04/B05 carry the source's anatomy/
pipeline/design-tell facts forward to the anchor (now grounded in the real
SKILL.md rather than the source's compressed summary); B06 is a new
anchor-payoff beat; B07 (both directions) is new. Result: B00 + 7 body beats
+ BCRY/BHTF/BOUT = 11 beats.

## One-flag audit

No inference-flag beat: every claim is either the generic, verifiable
mechanism of a Claude skill (folder + SKILL.md, read-then-execute,
specification semantics) or a direct quote/paraphrase of the legal-hold
SKILL.md itself (the confirmation gate, the four flags, the "what this
skill does not do" edge list) — nothing here is an inference about an
unread source.
