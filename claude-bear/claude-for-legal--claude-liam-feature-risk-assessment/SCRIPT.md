# What Does a Feature-Risk-Assessment Actually Tell You? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet whose narration
carried unfilled `>` placeholders at most beats — see QUESTION.md). Register: **Plain**.
7 beats ≈ 1:55.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone wants Claude to approve a new feature before it ships — a clean yes or no. Wrong word: Claude doesn't approve features. It assesses them, against a fixed checklist. Will you assess this new feature?" | BrutalistHesitantWriter — types "Claude, will you approve this new feature?", corrects "approve" → "assess" |
| B01 | 1 stakes / 2 wrong guess, falsified | It's tempting to think a risk assessment means eyeballing a feature and calling it safe or risky. Take one that looks harmless: users upload a photo ID to prove their age. A quick look says fine — it's optional, nobody's forced to do it. But the checklist asks a different question. Where does that photo go. How long is it kept. Who can actually see it. The quick look never asked. | a feature card stamped "LOOKS FINE," then three questions land under it, one at a time, that the quick look skipped |
| B02 | 3 mechanism / **4 anchor planted** | Read the SKILL.md — one file, the instruction set, plain language. Then work through it: one step at a time, in order, no branching unless a step says otherwise. Watch the anchor: same feature, four boxes on the checklist — what's collected, where it's stored, how long it's kept, who can access it. Right now two of those boxes are blank. Nothing's been judged. Just documented, one box at a time. | THE ANCHOR — four boxes around the photo-ID card, two filled, two blank |
| B03 | **4 anchor payoff / 5 both directions** | Fill in the last two boxes and the picture completes: kept ninety days, visible to support staff. All four boxes filled — but filled in isn't the same as safe. Documenting where something goes doesn't clear it. And the reverse holds too: one flag raised here — no retention limit stated — doesn't mean the feature gets killed. It means someone now has what they need to make that call, instead of guessing. | THE ANCHOR RETURNS — all four boxes filled; splits into "all filled ≠ safe" and "one flag ≠ killed" |
| **BCRY** | **6 carry-out** | A feature-risk-assessment doesn't tell you a feature is safe. It tells you what to look at before someone decides. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Take one feature you're building or reviewing right now. Ask Claude to walk through it: what data it touches, where that data is stored, how long it's kept, and who can access it — before either of you says whether it's fine. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Feature Risk Assessment. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the quick-look-vs-checklist gap; the read-SKILL.md/four-box mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (approve = yes/no); B01 falsifies it with a concrete case — a feature that looks fine still gets the same unasked questions |
| Exactly one inference flag | none needed — the account describes the generic shape of a checklist-driven review (what/where/how-long/who), not a specific product's undocumented behavior; see QUESTION.md for why most of the source carried no facts to begin with |
| One anchor, planted early, paid off late | B02 → B03 (the photo-ID card's four boxes, two blank, then all four filled) |
| Both directions | B03 — all boxes filled doesn't prove safe (documented isn't judged); one flag raised doesn't prove the feature dies (flagged isn't killed) |
| No design judgment | B01–B03 state what the checklist asks and returns, never a verdict on whether any specific skill or feature was well designed |

## Deliberately not claimed

- **Not that Claude renders a safety verdict.** The reel is explicit that the output is a
  documented checklist, not a judgment — B03 states both directions precisely to block
  that misreading.
- **Not a specific Claude product feature's exact checklist items.** Because most of the
  source sheet's skill-specific facts were never written (see QUESTION.md), this script
  keeps only the two facts the source did state outright (one-file SKILL.md instruction
  set; linear read-execute-return pipeline) and illustrates the checklist mechanism with
  a generic, uncontroversial anchor (photo-ID upload; what/where/how-long/who) rather than
  inventing this skill's real checklist fields.
- **No accusation that any feature or team was careless.** The photo-ID example is a
  generic illustration of a checklist catching unasked questions, not a claim about any
  real product.

## Handoff prompt (BHTF, read aloud)

> "Walk through the feature I'm building or reviewing right now: what data it touches,
> where that data is stored, how long it's kept, and who can access it — before telling
> me whether it's fine."

Why it's worth running: it forces the same four questions the reel's anchor uses onto a
real feature, so the review produces a documented answer instead of a gut-check "looks
fine."

---
**GATE P — signed:** reconstructed per QUESTION.md; no human sign-off exists
for the original placeholder script.
