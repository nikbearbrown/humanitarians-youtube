# Is Claude's Duration Number Its Own Judgment? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-fixed-income-portfolio`, Teardown -> Plain).
Register: **Plain**. 7 beats.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion (no puppet host in hai-simple).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone asks whether Claude judges how risky a bond portfolio is. It doesn't. It computes duration and DV01 from the numbers you give it. Liam is here to take you through what it actually computes." | writer types "What decides / a portfolio's risk — / judgment?", hesitates on "judgment", corrects to "the numbers" |
| B01 | 1 stakes / 2 wrong guess, falsified | The natural guess is that Claude decides how risky this bond portfolio is — the way an analyst forms an opinion after studying it. But the skill doesn't have an opinion. It takes the numbers it's given for each bond — coupon, maturity, current price — and computes duration and DV01 from them. Feed it a different price, and the numbers move without protest; it never argues that your bond is too risky. | an analyst figure weighing a conclusion, struck; reference-data tags feeding a numbers box, lit |
| B02 | 3 mechanism / **4 anchor planted** | What the skill actually does is take DV01 — the dollar change in a bond's price for a one basis point move in rates — and add it up across every bond in the portfolio. Watch the anchor: shock the portfolio by 100 basis points, and DV01 says exactly how many dollars that move costs or gains. No opinion, just arithmetic. | THE ANCHOR — a rate-shock dial wired directly to a single portfolio P&L readout |
| B03 | **4 anchor payoff** / 5 both directions | That same shock is what a scenario analysis runs, again and again, at different sizes. A portfolio that swings hard under one rate scenario isn't necessarily poorly built — a large DV01 can be an intentional, hedged position. And a portfolio that holds steady under that one scenario doesn't mean it's safe from rate risk generally — a bigger move, or a shift that isn't parallel across the curve, can still hurt it. | THE ANCHOR RETURNS as a three-scenario grid; splits into "swings ≠ broken" and "steady ≠ safe" |
| **BCRY** | **6 carry-out** | A portfolio's duration and DV01 aren't Claude's judgment about how risky it is — they're computed sensitivities to a rate move you specify. Change the size of that move, and the numbers change with it. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Give Claude a small bond portfolio — coupon, maturity, and current price for two or three bonds — and ask it to run the fixed-income-portfolio skill: compute duration and DV01, then stress test a 100 basis point rate move. Then double the shock size and watch how the dollar impact scales. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | Is Claude's Duration Number Its Own Judgment? Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the wrong guess before B02 opens the mechanism |
| Wrong guess surfaced *and falsified by a case* | B01 states "decides how risky, like an analyst"; falsified by "feed it a different price and the numbers move without protest — it never argues that your bond is too risky" |
| Exactly one inference flag | none needed — every claim here is stated directly from the source sheet's own facts (no inference leap) |
| One anchor, planted early, paid off late | B02 -> B03 (DV01 summed across the portfolio, a rate shock driving one P&L readout, then the same shock resized in the scenario analysis) |
| Both failure directions | B03: "swings a lot doesn't mean poorly built" / "holds steady doesn't mean safe" |
| No design judgment | B01/B02/B03 describe what the skill does and where it stops; no verdict on whether it was built well |

## Deliberately not claimed

- **Not that the skill is "wrong" or poorly designed.** Teardown's B03 in the
  source framed strengths/limits as a design-tell verdict ("what it gets
  right... what it bites"); Plain keeps only the mechanism and its two
  failure directions, no judgment on the design choice itself.
- **Not a claim about any specific bond, dollar figure, or Excel UI.** The
  anchor (a basis-point shock driving a DV01-based P&L number) is the
  standard structural sensitivity every bond portfolio has, described
  generically — no invented screen, ticker, or output format.
- **Not "the skill decides which bonds belong in the portfolio or what the
  right shock size is."** The whole point of the wrong-guess/falsification
  pair (B01) is the opposite: it computes from the reference data and the
  scenario it's given, it does not originate a risk opinion from its own
  judgment about the holdings.

## Handoff prompt (BHTF, read aloud)

> "Give Claude a small bond portfolio — coupon, maturity, and current
> price for two or three bonds — and ask it to run the
> fixed-income-portfolio skill: compute duration and DV01, then stress
> test a 100 basis point rate move. Then double the shock size and watch
> how the dollar impact scales."

Why it's worth running: watching the dollar impact scale linearly with
the shock size is the fastest way to see that DV01 is a fixed sensitivity
number, not a risk verdict — rather than just trusting that it is.

---
**GATE P — signed:** ______________________ (human)
