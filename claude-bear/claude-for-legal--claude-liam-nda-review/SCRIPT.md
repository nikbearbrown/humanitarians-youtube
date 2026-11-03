# Does a Clean NDA Review Mean It's Safe to Sign? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet whose narration
was never actually written — see QUESTION.md). Register: **Plain**. 7 beats ≈ 2:00.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes an NDA review means Claude CLEARS it — a final legal sign-off. Wrong word — Claude REVIEWS it, flagging what's unusual against a standard baseline. Liam, take them through it." | BrutalistHesitantWriter — types "Can Claude CLEAR this NDA for me?", corrects "CLEAR" → "REVIEW" |
| B01 | 1 stakes / 2 wrong guess, falsified | It's tempting to think an NDA review that flags nothing means the NDA is fine to sign. But say the confidentiality clause never carves out information that later becomes public through no fault of anyone — say a competitor publishes it first. That clause reads exactly like a complete, ordinary definitions section, sitting right next to every other clause that does include the standard carve-outs. A review that only catches obvious red flags can miss the gap that's just quietly missing. | an NDA page dense with clauses; one clause gets circled in accent, then struck, with a caption revealing what's missing |
| B02 | 3 mechanism / **4 anchor planted** | An NDA review that actually works has three parts: the clauses in, a check against a baseline of standard terms — definitions, carve-outs, duration, mutuality — and a flag list of what's unusual, out. Watch the anchor: that same confidentiality clause comes back stamped in the margin. Not confirmed a problem. Flagged: no carve-out for public information. | three labeled parts lighting in turn (clauses / baseline / flag list); THE ANCHOR — an NDA clause stamped "FLAGGED — NO CARVE-OUT" |
| B03 | **4 anchor payoff / 5 both directions** | That flagged clause gets checked by someone who knows the law that actually applies — what counts as a reasonable carve-out or duration differs by state and by deal. Only then does it move from flagged to either fine after all, or something that needs to change. But nothing flagged doesn't mean nothing's wrong — a review only catches gaps against its baseline, and a clause outside that baseline slips through clean. And a heavily flagged NDA isn't automatically a bad deal either — flagging means check this, not reject this. | THE ANCHOR RETURNS — the flagged clause gets checked and the page is stamped "CHECKED — OK TO SIGN"; then splits into "no flag ≠ nothing wrong" and "flagged ≠ reject it" |
| **BCRY** | **6 carry-out** | A clean NDA review isn't a green light — it's only checked once someone reads the flagged clauses against the law that actually applies. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Paste in an NDA you're reviewing. Ask Claude to check it against standard confidentiality carve-outs — public information, independent development, prior knowledge, legally required disclosure — and flag anything missing or unusual. Then have someone who knows the law that applies check every flagged clause before you sign. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Does a Clean NDA Review Mean It's Safe to Sign? Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the clean-review-isn't-checked gap; the three-part mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (review = clearance to sign); B01 falsifies it with a concrete case — a missing carve-out that reads exactly like every ordinary clause around it |
| Exactly one inference flag | none needed — the account describes the generic shape of an NDA review (baseline check, flag, legal verification) and ordinary contract-drafting convention (confidentiality clauses carry carve-outs; what's reasonable varies by jurisdiction), not a specific product's undocumented behavior; see QUESTION.md for why the source carried no facts to begin with |
| One anchor, planted early, paid off late | B02 → B03 (the clause stamped FLAGGED becomes the clause stamped CHECKED) |
| Both directions | B03 — no flag doesn't prove nothing's wrong (a baseline check can miss what's outside it); heavy flagging doesn't prove the deal is bad (flagging means check, not reject) |
| No design judgment | B01–B03 state what an NDA review needs and why, never a verdict on whether any specific skill or tool was well designed |

## Deliberately not claimed

- **Not that Claude made an error.** B01's case is about a clause that reads
  completely and ordinarily — the failure mode is trusting a clean pass without
  checking against a baseline, not a mistake Claude specifically made.
- **Not a specific Claude product feature.** Because the source sheet's actual facts
  were never written (see QUESTION.md), this script describes the generic mechanics of
  an NDA review (clauses in, flagged baseline comparison out, legal verification step)
  rather than citing any particular skill's steps, tool, or output format.
- **No accusation that anyone was negligent.** The missing carve-out in B01 is
  presented as an ordinary risk of drafting from a template — not every template
  carries every carve-out — not a failure by a named person or team.
- **No jurisdiction-specific legal claim.** The reel says reasonableness of a carve-out
  or duration "differs by state and by deal" without naming any specific state's rule,
  because that varies and isn't the reel's claim to make.

## Handoff prompt (BHTF, read aloud)

> "Paste in an NDA I'm reviewing. Check it against standard confidentiality
> carve-outs — public information, independent development, prior knowledge,
> legally required disclosure — and flag anything missing or unusual. I'll have
> someone who knows the law that applies check every flagged clause before I sign."

Why it's worth running: it forces the pass to separate what it's confident about
(comparing clauses against a standard baseline) from what still needs a human check
(whether a flagged gap actually matters under the law that applies) — which is
exactly the boundary the reel is built around.

---
**GATE P — signed:** reconstructed per QUESTION.md; no human sign-off exists
for the original placeholder script.
