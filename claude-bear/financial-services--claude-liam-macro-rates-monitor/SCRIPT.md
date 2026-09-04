# Does Claude's Macro Rates Dashboard Predict Where Rates Are Headed? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-macro-rates-monitor`, Teardown -> Plain).
Register: **Plain**. 7 beats.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion (no puppet host in hai-simple).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone asks whether a macro rates dashboard means Claude is predicting where rates are headed next. It isn't. Liam is here to take you through what the skill actually combines, and what it leaves alone." | writer types "Can Claude / predict / where rates go?", hesitates on "predict", corrects to "combine four indicators about" |
| B01 | 1 stakes / 2 wrong guess, falsified | The natural guess is that asking Claude for a macro rates dashboard means it's forming its own view on where the economy is headed — reading the data and telling you what's coming. But the skill is a fixed procedure: it combines four named things — macro indicators, the yield curve, inflation breakevens, and swap rates — using the relationships already defined for them, like splitting a yield into its real and nominal parts. Ask it instead to forecast what the central bank will actually do next quarter, and there's nothing to run: that's not one of the four things the spec combines. | a forecasting analyst, struck; a four-input combination chain, lit |
| B02 | 3 mechanism / **4 anchor planted** | What the skill actually does: it takes macro indicators as one input, the shape of the yield curve as a second, inflation breakevens — the market's implied inflation expectation — as a third, and swap rates as a fourth, and combines all four into one dashboard. Watch the anchor: one pull of market data moving through all four building blocks, in order, before it reaches the dashboard. Each block uses only the definition the file gives it — nothing added, nothing guessed. | THE ANCHOR — four cards (INDICATORS / YIELD CURVE / BREAKEVENS / SWAP RATES), one data package traveling through all four, then the DASHBOARD |
| B03 | **4 anchor payoff** / 5 both directions | The data package comes out the other side as a finished dashboard — but that only proves the four building blocks were combined the way the file defines them: nothing skipped, nothing improvised. It doesn't prove the economic read inside the dashboard will hold up — a correctly computed breakeven can still turn out to be a poor predictor of actual inflation. And if swap-rate data isn't available and that block can't populate, that's a data gap, not evidence the other three blocks are wrong. | THE ANCHOR RETURNS — the four-card chain, resting at DASHBOARD; splits into "ran is not sound" and "missing is not wrong" |
| **BCRY** | **6 carry-out** | A macro rates dashboard from Claude isn't an original economic call — it's four named inputs, macro indicators, yield curve, breakevens, and swap rates, combined by one fixed, repeatable procedure. A finished dashboard means the combination ran correctly, not that reality will follow it. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Pick a country or region you follow. Ask Claude to pull together a macro rates read combining the yield curve shape, inflation breakevens, and swap rates — and have it show you the definition it's using for each piece before it combines them. Then ask it what the central bank will actually do next quarter, and watch what it can and can't answer. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | Does Claude's Macro Rates Dashboard Predict Where Rates Are Headed? Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the wrong guess before B02 opens the mechanism |
| Wrong guess surfaced *and falsified by a case* | B01 states "forming its own view on where the economy is headed"; falsified by "forecast what the central bank will actually do next quarter — that's not one of the four things the spec combines" |
| Exactly one inference flag | none needed — every claim is stated directly from the source sheet's own facts (no inference leap) |
| One anchor, planted early, paid off late | B02 -> B03 (one data package moving through INDICATORS / YIELD CURVE / BREAKEVENS / SWAP RATES, in order, resting at DASHBOARD) |
| Both failure directions | B03: "ran is not sound" (a completed dashboard doesn't mean the economic read inside it is correct) / "missing is not wrong" (a block that can't populate on missing data doesn't mean the other blocks are wrong) |
| No design judgment | B01/B02/B03 describe what the skill does and where it stops; no verdict on whether it was built well |

## Deliberately not claimed

- **Not that the skill is "wrong" or poorly designed.** Teardown's B03 in
  the source framed strengths/limits as a design-tell verdict ("gets
  right: repeatable results... bites: anything outside the spec"); Plain
  keeps only the mechanism and its two failure directions, no judgment on
  the design choice itself.
- **Not a claim about any specific country, ticker, central bank, or dashboard
  layout.** The anchor (one data package moving through four inputs) is a
  generic, unnamed example — no invented screen or specific market figures.
- **Not "the skill checks the economics for you."** The whole point of the
  both-directions beat (B03) is the opposite: it enforces the combination
  procedure, not the soundness of the economic read that results from it.
- **Not a specific claim about how the skill computes a breakeven or defines
  "financial conditions" internally.** The source states only that the skill
  combines the four named inputs per fixed definitions — the reel states that
  structure without inventing formulas the source doesn't specify.

## Handoff prompt (BHTF, read aloud)

> "Pick a country or region you follow. Ask Claude to pull together a macro
> rates read combining the yield curve shape, inflation breakevens, and swap
> rates — and have it show you the definition it's using for each piece
> before it combines them. Then ask it what the central bank will actually do
> next quarter, and watch what it can and can't answer."

Why it's worth running: watching the dashboard combine the four defined
inputs cleanly, then watching the same request stall on an actual forecast
question, is the fastest way to see the line between "combines what's
defined" and "predicts what isn't."

---
**GATE P — signed:** ______________________ (human)
