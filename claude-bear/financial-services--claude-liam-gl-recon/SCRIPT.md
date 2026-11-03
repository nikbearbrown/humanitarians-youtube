# SCRIPT.md — Claude, Gl Recon. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-gl-recon` (Teardown, skill-teardown format) — question
and true facts carried over verbatim from the source; narration
re-registered to Plain (explain, then stop); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

**Source-fidelity note:** the source's job line survives verbatim across its
B00/B03/BVDT beats: "Reconcile general ledger to subledger for a trade date
or period — match at the position or transaction level, surface breaks, and
classify each break by likely cause. Use for daily or month-end recon runs
across asset classes." The source's anatomy beat (B01) lists exactly one
file: `SKILL.md` (2k, accented) — unlike some siblings, no second file is
ever named, so none is invented here. Linear pipeline (read SKILL.md →
execute → return output) and specification semantics (repeatable results, a
limit at the file's edge) also carry over unchanged.

## B00 — cold open (BrutalistHesitantWriter)
You'd guess Claude decides which ledger is right when it runs the gl-recon
skill. It doesn't — it surfaces where they disagree and classifies why.
Let's see how that actually works.

## Act I — the wrong guess

**B01 — Sounds like an audit**
Hear "Claude has a reconciliation skill" and it sounds like Claude is
auditing the books — comparing two ledgers and deciding which number is
true.

**B02 — Broken, with a case** (pays off B00)
But it never edits either ledger. Run it on a period with a known break, and
the general ledger number and the subledger number are exactly what they
were before the run — only a classified break sits between them.

## Act II — the mechanism

**B03 — A break, surfaced** (ANCHOR PLANTED)
Here's the anchor: a break. Say the GL shows one hundred four thousand for a
position and the subledger shows one hundred thousand. gl-recon lines up the
two records, flags the four-thousand-dollar gap, and tags it with a likely
cause — here, a late trade.

**B04 — Match, then classify, in order**
It works trade date or period, position or transaction level, matching
record to record in a fixed order — the steps don't branch unless the
SKILL.md itself says to.

**B05 — Matcher, not fixer**
That makes it a matcher and a classifier, not a fixer. The payoff: the same
breaks caught the same way, run after run. The limit: it never decides which
ledger is correct — that call is still yours.

**B06 — The anchor returns** (ANCHOR PAYOFF)
So back to that break: gl-recon never picked a winner between the ledgers.
It surfaced the four-thousand-dollar gap and named a likely cause. The
number stays open until you resolve it.

## Act III — both directions

**B07 — Neither proves the other**
A break classified as a likely timing difference doesn't prove the trade
will settle and the gap will close on its own. And a period that reconciles
clean end to end doesn't prove there's no error in it — it only means every
difference happened to net to zero this time.

## Close

**BCRY — carry-out**
gl-recon doesn't decide which ledger is right — it matches GL to subledger,
surfaces every break, and tags a likely cause; resolving the break is still
on you.

**BHTF — your turn**
Your turn. Paste this into Claude: I want to reconcile general ledger to
subledger for a trade date or period — match at the position or transaction
level, surface breaks, and classify each by likely cause. Read the gl-recon
skill and walk me through what you will do, before you do it. That way
you'll see exactly which fields it matches on, before a single break gets
classified.

**BOUT — outro**
Claude, Gl Recon. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–B01 | "a reconciliation skill" sounds like Claude is auditing and judging the books |
| Wrong guess | B00 → B02 | "decides" corrected to "surfaces"; broken with the run-on-a-known-break case |
| Mechanism | B03–B05 | a break defined and classified, matched in a fixed order, matcher not fixer |
| Anchor | B03 → B06 | the $4,000 GL/subledger break, planted then returned to |
| Both directions | B07 | a timing classification proves nothing about self-resolution; a clean recon proves nothing about hidden error |
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
`financial-services--claude-liam-earnings-preview-single` sibling redo. No
financial detail was invented beyond an illustrative example ($104,000 vs
$100,000, tagged "late trade") built to visualize the source's own literal
job line — not a claim about a real reconciliation the skill has processed.

## One-flag audit

No inference-flag beat: every claim here is about the generic, verifiable
mechanism of a Claude skill (folder + SKILL.md, read-then-execute,
specification semantics) plus the source's own stated job description — not
an inference about the unread SKILL.md's internal instruction text.
