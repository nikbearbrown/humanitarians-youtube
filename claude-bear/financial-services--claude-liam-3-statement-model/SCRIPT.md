# How Does Claude Fill In a Financial Model? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-3-statement-model`, Teardown -> Plain).
Register: **Plain**. 7 beats.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion (no puppet host in hai-simple).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone asks whether Claude fills in a financial model using its own judgment, like an analyst would. It doesn't. Liam is here to take you through what the skill actually does, step by step." | writer types "What fills in / the model — / judgment?", hesitates on "judgment", corrects to "the steps" |
| B01 | 1 stakes / 2 wrong guess, falsified | The natural guess is that Claude reasons about your business the way an analyst would — deciding what belongs in the model from general financial knowledge. But the skill doesn't work that way. It follows a fixed list of steps written in advance. Ask it to do something those steps don't cover, and it won't improvise a fix — it stays exactly inside what's written. | an analyst figure vs. a written checklist; the analyst figure struck, the checklist lit |
| B02 | 3 mechanism / **4 anchor planted** | What the skill actually does is read a template that already lays out the three statements, and link them together. Watch the anchor: net income leaves the income statement, lands in retained earnings on the balance sheet, and then shows up again at the top of the cash flow statement. | THE ANCHOR — three statement cards (IS/BS/CF), net income traveling IS -> BS -> CF as a single highlighted line |
| B03 | **4 anchor payoff** / 5 both directions | That link is now built — the three statements tie together, and the numbers move where they're supposed to. But a model that ties out isn't the same as a model that's right: the connections can stay consistent even when the assumption feeding them is wrong. And a line that's still blank doesn't mean the run failed — it can mean the template's step for that line never got an input to connect. | THE ANCHOR RETURNS, tied; splits into "tied out ≠ right" and "blank ≠ broken" |
| **BCRY** | **6 carry-out** | A filled-in model isn't Claude's financial judgment — it's the numbers you gave it, linked by a fixed set of steps. The model only connects what the template told it to connect. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Give Claude a simple set of assumptions — one revenue line, one expense, a starting cash balance — and ask it to run the 3-statement-model skill and link the three statements. Then change one assumption and watch which lines move and which stay put. That's the fastest way to see the linkage, instead of trusting it. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | How Does Claude Fill In a Financial Model? Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the wrong guess before B02 opens the mechanism |
| Wrong guess surfaced *and falsified by a case* | B01 states "reasons like an analyst"; falsified by "ask it something the steps don't cover, and it won't improvise" |
| Exactly one inference flag | none needed — every claim here is stated directly from the source sheet's own facts (no inference leap) |
| One anchor, planted early, paid off late | B02 -> B03 (net income: income statement -> retained earnings -> cash flow statement) |
| Both failure directions | B03: "tied out isn't the same as right" / "blank doesn't mean the run failed" |
| No design judgment | B01/B02/B03 describe what the skill does and where it stops; no verdict on whether it was built well |

## Deliberately not claimed

- **Not that the skill is "wrong" or poorly designed.** Teardown's B03 in the
  source framed strengths/limits as a design-tell verdict ("what it gets
  right... what it bites"); Plain keeps only the mechanism and its two
  failure directions, no judgment on the design choice itself.
- **Not a claim about any specific numbers, templates, or UI.** The anchor
  (net income -> retained earnings -> cash flow) is the standard structural
  link between the three statements, described generically — no invented
  screen, button, or output format.
- **Not "the skill decides what belongs in the model."** The whole point of
  the wrong-guess/falsification pair (B01) is the opposite: it links what
  the template and your inputs already define, nothing it inferred itself.

## Handoff prompt (BHTF, read aloud)

> "Give Claude a simple set of assumptions — one revenue line, one expense, a
> starting cash balance — and ask it to run the 3-statement-model skill and
> link the three statements. Then change one assumption and watch which
> lines move and which stay put."

Why it's worth running: watching which lines move (and which don't) when a
single input changes is the fastest way to see the linkage the skill
actually performs, instead of just trusting that it happened.

---
**GATE P — signed:** ______________________ (human)
