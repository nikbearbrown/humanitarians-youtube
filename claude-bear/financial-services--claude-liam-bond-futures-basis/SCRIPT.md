# How Does Claude Find the Cheapest Bond to Deliver? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-bond-futures-basis`, Teardown -> Plain).
Register: **Plain**. 7 beats.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion (no puppet host in hai-simple).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone asks whether Claude picks the cheapest bond to deliver by feel, the way a trader might. It doesn't. Liam is here to take you through the actual comparison, step by step." | writer types "How does Claude / pick the cheapest / bond to deliver — / by feel?", hesitates on "feel", corrects to "the math" |
| B01 | 1 stakes / 2 wrong guess, falsified | The natural guess is that finding the cheapest bond to deliver takes a trader's judgment — a feel for which bond will perform best. But the skill doesn't work that way. It prices every eligible bond against the futures contract using its conversion factor, and ranks them by actual delivery cost. Ask it to favor a bond because you like its prospects, and it won't — it only reports the one that's numerically cheapest to deliver. | a trader's-feel figure vs. a priced-and-ranked checklist; the feel side struck, the ranked list lit |
| B02 | 3 mechanism / **4 anchor planted** | What the skill actually does is price one bond at a time. Watch the anchor: the futures price and the bond's conversion factor combine into its delivery cost, and that cost converts into a single number — the implied repo rate, the return you'd earn buying the bond, holding it, and delivering it into the contract. | THE ANCHOR — three cards (FUTURES PRICE / DELIVERABLE BOND / IMPLIED REPO RATE), delivery cost traveling card to card as a single highlighted line |
| B03 | **4 anchor payoff** / 5 both directions | That comparison is now built — price, conversion factor, and implied repo rate all line up for the cheapest bond. But finding the cheapest bond to deliver isn't the same as finding a profitable trade: the implied repo rate can still sit below the market's actual financing cost, meaning the basis trade loses money. And a bond that ranks expensive today isn't ruled out for good — yields move, so the ranking gets rerun, not assumed fixed. | THE ANCHOR RETURNS, connected; splits into "cheapest ≠ profitable" and "expensive today ≠ excluded forever" |
| **BCRY** | **6 carry-out** | The cheapest bond to deliver is whichever one comes out lowest in a fixed comparison across the whole deliverable basket — not the bond Claude favors. It ranks delivery cost against the curve; it doesn't call whether the trade is worth putting on. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Give Claude a small basket of deliverable bonds — a price and conversion factor for each — along with the futures price and the market's repo rate, and ask it to run the bond-futures-basis skill to find the cheapest one to deliver. Then change one bond's price and watch whether the ranking flips. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | How Does Claude Find the Cheapest Bond to Deliver? Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the wrong guess before B02 opens the mechanism |
| Wrong guess surfaced *and falsified by a case* | B01 states "trading feel"; falsified by "ask it to favor a bond because you like its prospects, and it won't" |
| Exactly one inference flag | none needed — every claim here is stated directly from the source sheet's own facts (no inference leap) |
| One anchor, planted early, paid off late | B02 -> B03 (one bond's price + conversion factor -> delivery cost -> implied repo rate) |
| Both failure directions | B03: "cheapest to deliver isn't the same as profitable" / "expensive today isn't excluded forever" |
| No design judgment | B01/B02/B03 describe what the skill does and where it stops; no verdict on whether it was built well |

## Deliberately not claimed

- **Not that the skill is "wrong" or poorly designed.** Teardown's B03 in the
  source framed strengths/limits as a design-tell verdict ("what it gets
  right... what it bites"); Plain keeps only the mechanism and its two
  failure directions, no judgment on the design choice itself.
- **Not a claim about any specific bonds, prices, or UI.** The anchor (price
  + conversion factor -> delivery cost -> implied repo rate) is the standard
  structural relationship behind cheapest-to-deliver analysis, described
  generically — no invented screen, output format, or numeric example.
- **Not "the skill decides which trade to make."** The whole point of the
  wrong-guess/falsification pair (B01) and the both-directions beat (B03) is
  the opposite: it ranks and computes; it does not judge whether a trade is
  worth putting on.

## Handoff prompt (BHTF, read aloud)

> "Give Claude a small basket of deliverable bonds — a price and conversion
> factor for each — along with the futures price and the market's repo
> rate, and ask it to run the bond-futures-basis skill to find the cheapest
> one to deliver. Then change one bond's price and watch whether the
> ranking flips."

Why it's worth running: watching whether the ranking flips when a single
bond's price changes is the fastest way to see that the skill is comparing
numbers, not forming an opinion about which bond is "best."

---
**GATE P — signed:** ______________________ (human)
