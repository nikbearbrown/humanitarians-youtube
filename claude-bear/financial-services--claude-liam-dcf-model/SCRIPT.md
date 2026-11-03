# Is Claude's DCF Number Its Own Judgment? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-dcf-model`, Teardown -> Plain).
Register: **Plain**. 7 beats.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion (no puppet host in hai-simple).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone asks whether Claude's DCF model reflects its own judgment about what a company is worth. It doesn't. Liam is here to take you through what the skill actually computes, step by step." | writer types "What decides / what it's worth — / judgment?", hesitates on "judgment", corrects to "the formula" |
| B01 | 1 stakes / 2 wrong guess, falsified | The natural guess is that Claude's valuation reflects its own judgment about the company — like an analyst who's studied the business and reached a conclusion. But the skill doesn't have an opinion. It takes the assumptions it's given — a growth rate, a discount rate, a terminal growth rate — and runs them through a fixed formula. Feed it a different assumption and the valuation moves without protest; it never argues that your number is wrong. | an analyst figure weighing a conclusion, struck; assumptions feeding a formula box, lit |
| B02 | 3 mechanism / **4 anchor planted** | What the skill actually does is project each year's cash flow forward, then discount every one of them — plus a terminal value — back to today, using one number: the discount rate, WACC. Watch the anchor: turn that one dial, and the valuation follows it, every time. | THE ANCHOR — a discount-rate dial wired directly to a single valuation readout |
| B03 | **4 anchor payoff** / 5 both directions | That's the same dial a sensitivity analysis turns, again and again, watching the valuation swing. A number that swings a lot for a small change in the discount rate doesn't mean the model is broken — the input was never precise to begin with. And a valuation that holds steady across the sensitivity range doesn't prove it's right either — the terminal value, which usually carries most of the total, is still just a guess about the distant future. | THE ANCHOR RETURNS as a sensitivity grid; splits into "swings ≠ broken" and "steady ≠ right" |
| **BCRY** | **6 carry-out** | A DCF number is Claude running your growth and discount-rate assumptions through a fixed formula — not Claude's opinion of what a company is worth. Change the assumption, and the number moves. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Give Claude a simple set of DCF assumptions — a growth rate, a discount rate, a terminal growth rate — and ask it to run the dcf-model skill and value a hypothetical company. Then change only the discount rate by one point and watch how far the number moves. That's the fastest way to see how much of the valuation is assumption, not analysis. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | Is Claude's DCF Number Its Own Judgment? Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the wrong guess before B02 opens the mechanism |
| Wrong guess surfaced *and falsified by a case* | B01 states "reflects its own judgment, like an analyst"; falsified by "feed it a different assumption and the valuation moves without protest — it never argues that your number is wrong" |
| Exactly one inference flag | none needed — every claim here is stated directly from the source sheet's own facts (no inference leap) |
| One anchor, planted early, paid off late | B02 -> B03 (the discount-rate/WACC dial driving the single valuation readout, then turned repeatedly in the sensitivity analysis) |
| Both failure directions | B03: "swings a lot doesn't mean broken" / "holds steady doesn't mean right" |
| No design judgment | B01/B02/B03 describe what the skill does and where it stops; no verdict on whether it was built well |

## Deliberately not claimed

- **Not that the skill is "wrong" or poorly designed.** Teardown's B03 in the
  source framed strengths/limits as a design-tell verdict ("what it gets
  right... what it bites"); Plain keeps only the mechanism and its two
  failure directions, no judgment on the design choice itself.
- **Not a claim about any specific company, dollar figure, or Excel UI.**
  The anchor (discount rate -> valuation) is the standard structural
  sensitivity every DCF has, described generically — no invented screen,
  ticker, or output format.
- **Not "the skill decides the company's growth rate or discount rate."**
  The whole point of the wrong-guess/falsification pair (B01) is the
  opposite: it runs the assumptions it's given through a formula, it does
  not originate them from its own judgment about the business.

## Handoff prompt (BHTF, read aloud)

> "Give Claude a simple set of DCF assumptions — a growth rate, a discount
> rate, a terminal growth rate — and ask it to run the dcf-model skill and
> value a hypothetical company. Then change only the discount rate by one
> point and watch how far the number moves."

Why it's worth running: watching how far the valuation moves for a
one-point change in a single assumption is the fastest way to see how much
of a DCF number is assumption rather than analysis — instead of trusting
the precision of the output.

---
**GATE P — signed:** ______________________ (human)
