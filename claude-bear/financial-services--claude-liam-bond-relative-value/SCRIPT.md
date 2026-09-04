# How Does Claude Tell Whether a Bond Is Rich or Cheap? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-bond-relative-value`, Teardown -> Plain).
Register: **Plain**. 7 beats.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion (no puppet host in hai-simple).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone asks whether Claude picks a rich or cheap bond by trader's feel, the way a trader might. It doesn't. Liam is here to take you through what the skill actually computes, step by step." | writer types "Which bond is / rich or cheap — / by feel?", hesitates on "feel", corrects to "a curve" |
| B01 | 1 stakes / 2 wrong guess, falsified | The natural guess is that Claude judges whether a bond is rich or cheap using its own market feel. But the skill doesn't work that way. It computes a relative-value read from four fixed inputs: the bond's price, the yield curve it sits on, the credit spread over that curve, and a stress-tested rate shock. Give it a bond with no yield curve to compare against, and it won't invent one — there's nothing to spread it against, so there's nothing to read. | a trader's-feel figure vs. a priced/curve/spread/stress checklist; the feel side struck, the procedure side lit |
| B02 | 3 mechanism / **4 anchor planted** | What the skill actually does: it combines the bond's price, the yield curve context, and the credit spread over that curve, then runs a stress-tested rate shock across the result. Watch the anchor: a ten-year corporate bond trading forty basis points over the curve. It's priced, the curve is read, the spread is decomposed, and the stress scenario is run. Then it stops — with a single read, cheap by eight basis points, waiting. | THE ANCHOR — four cards (PRICED / CURVE READ / SPREAD DECOMPOSED / STRESS RUN), the bond token traveling through all four, halting at the last one |
| B03 | **4 anchor payoff** / 5 both directions | That read is built — priced, curved, spread-decomposed, and stress-tested. But a bond that comes back cheap by the read isn't the same as a bond worth buying: the read only reflects the curve you gave it, and a stale curve makes a wrong read look just as confident. And a bond that comes back rich by the read isn't automatically one to avoid — the stress scenario can still favor holding it. Either way, the read waits for a trader's decision before anything trades. | THE ANCHOR RETURNS, resting at the read; splits into "cheap ≠ worth buying" and "rich ≠ avoid it" |
| **BCRY** | **6 carry-out** | A computed rich-or-cheap read isn't Claude's call on what to buy — it's a number built from price, the curve, the spread, and a stress test, waiting for a trader's decision. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Give Claude one bond, its price, and a yield curve to compare it against, and ask it to run the bond-relative-value skill: decompose the spread and stress-test it against a rate shock. Then swap in a different curve for the same bond, and watch how much the read moves. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | How Does Claude Tell Whether a Bond Is Rich or Cheap? Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the wrong guess before B02 opens the mechanism |
| Wrong guess surfaced *and falsified by a case* | B01 states "judges using its own market feel"; falsified by "give it a bond with no yield curve to compare against and it has nothing to spread it against, so it has nothing to read" |
| Exactly one inference flag | none needed — every claim here is stated directly from the source sheet's own facts (no inference leap) |
| One anchor, planted early, paid off late | B02 -> B03 (ten-year corporate bond, +40bp over curve: priced → curve read → spread decomposed → stress run → a computed read, waiting) |
| Both failure directions | B03: "cheap by the read isn't the same as worth buying" / "rich by the read doesn't mean avoid it" |
| No design judgment | B01/B02/B03 describe what the skill does and where it stops; no verdict on whether it was built well |

## Deliberately not claimed

- **Not that the skill is "wrong" or poorly designed.** Teardown's B03 in the
  source framed strengths/limits as a design-tell verdict ("repeatable
  results... bites: anything outside the spec"); Plain keeps only the
  mechanism and its two failure directions, no judgment on the design
  choice itself.
- **Not a claim about any specific bond, issuer, or trading desk.** The
  anchor (a ten-year corporate bond, +40bp over curve) is a standard,
  generic relative-value example — no invented screen, dataset, or output
  format.
- **Not "the skill decides which bond to buy."** The whole point of the
  wrong-guess/falsification pair (B01) is the opposite: it computes and
  reports a read from price, curve, spread, and stress scenario — nothing
  it inferred from general market sense, and no trade decision of its own.

## Handoff prompt (BHTF, read aloud)

> "Give Claude one bond, its price, and a yield curve to compare it
> against, and ask it to run the bond-relative-value skill: decompose the
> spread and stress-test it against a rate shock. Then swap in a different
> curve for the same bond."

Why it's worth running: watching the read move when the curve changes is
the fastest way to see that the skill computes from the inputs you give
it, instead of a fixed opinion about the bond — rather than just trusting
that it does.

---
**GATE P — signed:** ______________________ (human)
