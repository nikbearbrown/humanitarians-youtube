# SCRIPT.md — Claude, Legal Writing. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-legal-writing` (Teardown, skill-teardown format) —
question and facts carried over; narration re-registered to Plain (explain,
then stop); cold open replaced with the BrutalistHesitantWriter; close
carries the Humanitarians AI skin.

**Source-fidelity note:** the actual `legal-writing` SKILL.md was found and
read in full at
`/Users/nik/Documents/Cowork/anthropics/claude-for-legal/law-student/skills/legal-writing/SKILL.md`
(see QUESTION.md). Every fact below is sourced from it directly — the source
reel's own beat_sheet.json had unfilled `>` placeholders standing in for the
skill's actual specifics, so this redo does not carry those placeholders
forward; it fills the same slots from the real file instead of guessing.

## B00 — cold open (BrutalistHesitantWriter)
Someone figures asking Claude for feedback means asking it to fix the memo.
It won't — legal-writing's rule is no rewriting, ever. Liam walks through
what the skill actually does.

## Act I — the wrong guess

**B01 — Sounds like a fix-it request**
Ask Claude for feedback on your memo, and it's easy to hear that as a
request to fix the memo for you.

**B02 — Broken, with a case** (pays off B00)
But legal-writing's hard rule is no rewriting, ever — ask it to rewrite
anyway and it refuses, then offers structural feedback, one labeled example,
or a drill on the rule instead.

## Act II — the mechanism

**B03 — Reads the whole draft first** (ANCHOR PLANTED)
First it reads the whole draft top to bottom before saying anything — say,
a 1L's memo arguing negligence in a car crash — and names what it actually
is: memo, brief, paper, or exam essay.

**B04 — Top-down, in that order**
Feedback then runs top-down: is the structure right, does the analysis
connect rule to fact, then clarity and citation — never sentence-level
polish before the structure is fixed.

**B05 — Confident on form, not on law**
On structure it's confident — writing is writing — but on whether that
negligence rule is actually stated right, it won't guess: it flags VERIFY
and leaves the legal call to you.

**B06 — The anchor returns** (ANCHOR PAYOFF)
So on that same negligence memo, it might say the structure runs backwards
and flag one rule to double-check — but it still won't write the fixed
paragraph. One generic example, labeled write yours, don't copy, and it
stops there.

## Act III — both directions

**B07 — Neither one is proof**
A confident structural note doesn't prove the rule inside is correct —
that's exactly what the VERIFY flag is for. And a VERIFY flag doesn't mean
the structure is fine, either — both can be broken in the same paragraph.

## Close

**BCRY — carry-out**
Legal-writing's job is to make Claude a harsher reader of your memo, never
its ghostwriter — the sentence still has to come from you.

**BHTF — your turn**
Your turn. Paste this into Claude: I'm drafting a memo. Read the
legal-writing skill and give me structural feedback — organization,
analysis depth, clarity, citation — but don't rewrite any of it. Tell me
what's weak, and flag anything you're not certain is legally correct.

**BOUT — outro**
Claude, Legal Writing. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–B01 | "feedback on my memo" sounds like a polite request to fix it |
| Wrong guess | B00 → B02 | "fix" corrected to "critique"; broken with the SKILL.md's own "Hard rule: no rewriting. Ever." |
| Mechanism | B03–B05 | reads the whole draft first, names the type, gives top-down feedback, confident on structure / VERIFY-flagged on substantive law |
| Anchor | B03 → B06 | a 1L's negligence memo (the SKILL.md's own worked example), planted then returned to |
| Both directions | B07 | a confident structural note proves nothing about the law inside; a VERIFY flag proves nothing about the structure |
| Carry-out | BCRY | one sentence, survives repetition |

## Beat-count note (redo)

Source is 7 beats (B00, B01 anatomy, B02 pipeline, B03 design tell, BVDT
verdict, BHTF your-turn, BOUT outro) — a compact skill-teardown format with
no explicit wrong-guess, anchor, or both-directions beat, and its narration
carried unfilled `>` placeholders instead of the skill's real specifics.
hai-simple's spine requires a wrong-guess, anchor, and both-directions beat
each in their own right (WRONG-GUESS LAW / ANCHOR LAW / BOTH-DIRECTIONS
LAW), so this redo expands modestly, identically in shape to the
`legal-hold` sibling redo: B01 (stakes) and B02 (wrong guess, broken) are
new; B03/B04/B05 carry the source's anatomy/pipeline/design-tell facts
forward to the anchor (now grounded in the real SKILL.md rather than its
unfilled placeholders); B06 is a new anchor-payoff beat; B07 (both
directions) is new. Result: B00 + 7 body beats + BCRY/BHTF/BOUT = 11 beats.

## One-flag audit

No inference-flag beat: every claim is either the generic, verifiable
mechanism of a Claude skill (folder + SKILL.md, read-then-execute) or a
direct quote/paraphrase of the legal-writing SKILL.md itself (the "no
rewriting, ever" guardrail, the structural-type list, the top-down feedback
order, the confidence-discipline split between structure and substantive
law, the negligence-memo worked example, the "what this skill does not do"
edge list) — nothing here is an inference about an unread source.
