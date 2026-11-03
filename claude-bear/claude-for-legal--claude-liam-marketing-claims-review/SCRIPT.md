# SCRIPT.md — Claude, Marketing Claims Review. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-marketing-claims-review` (Teardown, skill-teardown
format) — question and true facts carried over; narration re-registered to
Plain (explain, then stop); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

**Source-fidelity note:** the source never filled in this skill's specific
"Claude's job: ___" line (literal `>` placeholder survives in three spots).
Unlike the sibling redos that hit an unreachable SKILL.md, this one IS
reachable — a mirrored copy lives at
`/Users/nik/Documents/Cowork/anthropics/claude-for-legal/product-legal/skills/marketing-claims-review/SKILL.md`.
Every specific fact below (the five-part claim taxonomy, the substantiation
check, the claim-by-claim call format, the attorney gate on "Ready to ship:
Yes") is read directly from that file, not invented.

## B00 — cold open (BrutalistHesitantWriter)
You'd guess Claude can just tell you if your ad is legal. It can't — no
model hands down a legal verdict. What it actually checks is whether each
claim is provable. Let's look inside.

## Act I — the wrong guess

**B01 — Sounds like a ruling**
Hear "Claude has a marketing-claims-review skill" and it sounds like Claude
will read your copy and rule: legal, or not.

**B02 — Broken, with a case** (pays off B00)
But run the skill and nothing gets ruled legal or illegal. Every claim gets
sorted instead — fine, needs proof, needs a rewrite, or cut — and the skill
never hands down that ruling itself.

## Act II — the mechanism

**B03 — One real claim** (ANCHOR PLANTED)
Take one line from real ad copy: "Trusted by ten thousand companies."
Follow that claim through the skill.

**B04 — First: classify it**
First, it classifies. That line is a specific, factual claim — measurable,
and something a reader could reasonably rely on.

**B05 — Then: check the proof**
Then it checks substantiation — not whether some number exists on file, but
whether ten thousand is the actual current count, not old lifetime signups
dressed up as trust.

**B06 — A call, not a verdict**
The output is a call, never a verdict: fine, needs proof, needs rewording,
or cut — plus a suggested fix that keeps the energy. Same categories, every
single run. And before any claim ships as "ready," a non-lawyer user hits
one more gate: has an attorney actually seen this?

**B07 — The anchor returns** (ANCHOR PAYOFF)
So back to "trusted by ten thousand companies": the skill doesn't say yes or
no. It flags "needs substantiation" and asks for the current count —
whether that's enough to ship is still a person's call.

## Act III — both directions

**B08 — Neither one is proof**
A flag doesn't mean a claim is false — it can be entirely true and still
need the number on file. And a clean pass doesn't mean risk-free forever —
the product can change after the copy ships, and nothing rechecks it on its
own.

## Close

**BCRY — carry-out**
Marketing-claims-review doesn't rule on your ad — it sorts each claim by
what needs proof. Whether that's enough to ship is still a person's call.

**BHTF — your turn**
Your turn. Paste this into Claude: "Here's a line from my landing page:
'Trusted by 10,000 companies — the fastest way to manage your projects.'
Read the marketing-claims-review skill and walk me through what you will do
before you do it. Then classify each claim, tell me which ones need
substantiation, and suggest a fix that keeps the energy."

**BOUT — outro series**
Claude, Marketing Claims Review. This is Claude Basics, from Humanitarians
AI.

**BOUTCTA — outro CTA**
Find more at humanitarians.ai. …Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–B01 | "a marketing-claims-review skill" sounds like Claude will rule the ad legal or not |
| Wrong guess | B00 → B02 | "legal" corrected to "provable"; broken with the real output shape — a sort, never a ruling |
| Mechanism | B03–B06 | one real claim, classified, checked for substantiation, then called — plus the attorney gate |
| Anchor | B03 → B07 | "Trusted by 10,000 companies," planted then returned to |
| Both directions | B08 | a flag proves nothing about falsity; a clean pass proves nothing about permanence |
| Carry-out | BCRY | one sentence, survives repetition |

## Beat-count note (redo)

Source is 7 beats (B00, B01 anatomy, B02 pipeline, B03 design tell, BVDT
verdict, BHTF your-turn, BOUT outro) — a compact skill-teardown format with
no explicit wrong-guess, anchor, or both-directions beat. hai-simple's spine
requires all three as their own beats (WRONG-GUESS LAW / ANCHOR LAW /
BOTH-DIRECTIONS LAW), so this redo expands: B01 (stakes) and B02 (wrong
guess, broken) are new; B03 anchors a real claim (new, but drawn straight
from the SKILL.md's own worked example); B04/B05/B06 carry the source's
anatomy/pipeline/design-tell facts forward, split across classify /
substantiate / call-format because the real SKILL.md supports that much
specific detail; B07 (anchor payoff) and B08 (both directions) are new.
Result: B00 + 8 body beats (B01–B08) + BCRY/BHTF/BOUT/BOUTCTA = 13 beats — a
proportionate expansion, same shape-class as the `hiring-review`/
`case-brief`/`build-guide` sibling redos, just slightly larger because this
source's underlying skill was actually readable and supplied more real,
citable mechanism than those siblings had access to.

## One-flag audit

No inference-flag beat: every claim here is read directly from the mirrored
`marketing-claims-review/SKILL.md` (taxonomy, substantiation check, call
format, attorney gate) — nothing is inferred about unread material.
