# SCRIPT.md — Claude, Nav Tieout. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-nav-tieout` (Teardown, skill-teardown format) — question
and true facts carried over verbatim from the source; narration
re-registered to Plain (explain, then stop); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

**Source-fidelity note:** the source's job line survives verbatim across its
B00/B03/BVDT beats: "Tie an LP statement to the fund's NAV pack — recompute
the LP's capital account from the NAV components and flag any line that
doesn't agree. Use before LP statements are distributed." The source's
anatomy beat (B01) describes a skill as a folder Claude reads before it
works, holding one file — SKILL.md, plain language, no hidden logic — read
then acted on. Linear pipeline (read SKILL.md → execute each step in order →
return output) and specification semantics (repeatable results, a limit at
the file's edge) also carry over unchanged.

## B00 — cold open (BrutalistHesitantWriter)
You'd guess nav-tieout means Claude is proving the fund's NAV is correct.
It's not — it assumes the NAV pack, and checks whether the LP's own
statement agrees with it. Let's see how that works.

## Act I — the wrong guess

**B01 — Sounds like an audit of the NAV itself**
Hear "Claude has a nav-tieout skill" and it sounds like Claude is
independently confirming the fund's NAV is accurate — auditing the number
itself.

**B02 — Broken, with a case** (pays off B00)
But it never touches the NAV pack. Run it on a period with a known
LP-statement error, and the fund's NAV components are exactly what they were
before the run — only a flagged mismatch shows up on the LP side.

## Act II — the mechanism

**B03 — A gap, surfaced** (ANCHOR PLANTED)
Here's the anchor: say the NAV pack puts the LP's capital account at four
hundred four thousand, but the LP statement shows four hundred thousand.
nav-tieout recomputes the account from the NAV components and flags the
four-thousand-dollar gap.

**B04 — Recompute, then compare, in order**
It works one LP statement at a time: recompute the capital account straight
from the NAV components, then compare to what the LP was actually sent, then
flag differences — in a fixed order, the steps don't branch unless the
SKILL.md itself says to.

**B05 — Checker, not auditor**
That makes it a checker, not an auditor of the fund. The payoff: the same
mismatch caught the same way, every time, before the statement goes out. The
limit: it never questions whether the NAV pack itself is right.

**B06 — The anchor returns** (ANCHOR PAYOFF)
So back to that gap: nav-tieout never asked whether the NAV pack's numbers
were right. It recomputed the LP's account from them and flagged where the
statement disagreed. Fixing it is still someone's call.

## Act III — both directions

**B07 — Neither proves the other**
A flagged mismatch doesn't prove the LP statement is wrong — the NAV pack
could be the one with the error. And an LP statement that ties out clean
doesn't prove the fund's NAV was calculated correctly — it only means the two
documents agree with each other.

## Close

**BCRY — carry-out**
nav-tieout doesn't check whether the fund's NAV is right — it recomputes the
LP's capital account from the NAV pack and flags where the statement
disagrees. The NAV itself stays untested.

**BHTF — your turn**
Your turn. Paste this into Claude: I want to tie an LP statement to the
fund's NAV pack — recompute the LP's capital account from the NAV components
and flag any line that doesn't agree. Read the nav-tieout skill and walk me
through what you will do, before you do it. That way you'll see exactly
which NAV components it recomputes from, before a single line gets flagged.

**BOUT — outro**
Claude, Nav Tieout. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–B01 | "a nav-tieout skill" sounds like Claude is auditing and confirming the NAV itself |
| Wrong guess | B00 → B02 | "proves" corrected to "assumes"; broken with the run-on-a-known-LP-error case |
| Mechanism | B03–B05 | a gap defined and flagged, recomputed in a fixed order, checker not auditor |
| Anchor | B03 → B06 | the $4,000 NAV-pack/LP-statement gap, planted then returned to |
| Both directions | B07 | a flagged mismatch proves nothing about which side is wrong; a clean tie-out proves nothing about the NAV's own accuracy |
| Carry-out | BCRY | one sentence, survives repetition |

## Beat-count note (redo)

Source is 7 beats (B00, B01 anatomy, B02 pipeline, B03 design tell, BVDT
verdict, BHTF your-turn, BOUT outro) — a compact skill-teardown format with
no explicit wrong-guess, anchor, or both-directions beat. hai-simple's spine
requires all three as their own beats (WRONG-GUESS LAW / ANCHOR LAW /
BOTH-DIRECTIONS LAW), so this redo expands modestly: B01 (stakes) and B02
(wrong guess, broken) are new; B03/B04/B05 carry the source's anatomy/
pipeline/design-tell facts forward and B03 also plants the anchor; B06 is a
new anchor-payoff beat restating the design tell against the named anchor;
B07 (both directions) is new. Result: B00 + 7 body beats + BCRY/BHTF/BOUT =
11 beats — the identical proportionate expansion used on the
`financial-services--claude-liam-gl-recon` sibling redo. No financial detail
was invented beyond an illustrative example ($404,000 vs $400,000, a $4,000
gap) built to visualize the source's own literal job line — not a claim
about a real LP statement or fund the skill has processed.

## One-flag audit

No inference-flag beat: every claim here is about the generic, verifiable
mechanism of a Claude skill (folder + SKILL.md, read-then-execute,
specification semantics) plus the source's own stated job description — not
an inference about the unread SKILL.md's internal instruction text.
