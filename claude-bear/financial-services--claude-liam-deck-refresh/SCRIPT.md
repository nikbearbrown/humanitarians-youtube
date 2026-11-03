# How Does Claude Refresh a Deck? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-deck-refresh`, Teardown → Plain).
Register: **Plain**. 7 beats.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion (no puppet host in hai-simple).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone asks whether refreshing a deck means Claude rewrites the story. It doesn't — it swaps the numbers. Liam is here to walk through exactly what the skill changes, and what it leaves alone." | writer types "Refresh the deck — / does Claude rewrite / the story?", hesitates on "story", corrects to "numbers" |
| B01 | 1 stakes / 2 wrong guess, falsified | The natural guess is that refreshing a deck means Claude reconsiders the numbers — updating the commentary, the trend language, maybe the whole slide's framing along with the figure. But the skill doesn't reconsider anything. It's a fixed swap: find every place one figure appears, and replace it with another. Ask it to also rewrite the sentence built around that number, and it won't — that's outside the step. | a figure "reconsidering" the story, struck; a numbered find-and-replace checklist, lit |
| B02 | 3 mechanism / **4 anchor planted** | What the skill actually does is read the deck slide by slide, in order, and swap one exact figure for another wherever it finds it. Watch the anchor: four hundred eighty-five million appears in the executive summary, again in the comps table, and again in a footnote — three separate slides. One by one, each becomes five hundred twelve million. | THE ANCHOR — three slide cards (EXEC SUMMARY / COMPS TABLE / FOOTNOTE), each holding $485M; a scan cursor visits each in order, recoloring and swapping the figure to $512M |
| B03 | **4 anchor payoff** / 5 both directions | The refresh is done — five hundred twelve million now sits in all three places where four hundred eighty-five million used to. But a deck where every figure changed isn't the same as a deck that's still true: a sentence that said "still below four hundred eighty-five million" doesn't get rewritten just because the number did. And a leftover four hundred eighty-five million isn't always a miss — sometimes that instance was never the target figure at all. | THE ANCHOR RETURNS, all three slides now $512M, tied; splits into "number changed, sentence didn't" and "leftover isn't always a miss" |
| **BCRY** | **6 carry-out** | A deck refresh isn't Claude rewriting the story — it's one figure, swapped everywhere the step says to swap it, and left alone everywhere else. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Give Claude a few sentences that repeat one figure in different contexts, and ask it to swap that one figure for another, and change nothing else. Then check whether a nearby sentence built on the old number is still true, or whether the figure moved while the sentence around it stayed exactly where it was. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | How Does Claude Refresh a Deck? Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the wrong guess before B02 opens the mechanism |
| Wrong guess surfaced *and falsified by a case* | B01 states "reconsiders the numbers... updates the commentary"; falsified by "ask it to also rewrite the sentence... and it won't" |
| Exactly one inference flag | none needed — every claim here is stated directly from the source sheet's own facts (no inference leap) |
| One anchor, planted early, paid off late | B02 → B03 ($485M → $512M: executive summary → comps table → footnote, the source's own worked example) |
| Both failure directions | B03: "number changed, sentence didn't" / "leftover isn't always a miss" |
| No design judgment | B01/B02/B03 describe what the skill does and where it stops; no verdict on whether it was built well |

## Deliberately not claimed

- **Not that the skill is "wrong" or poorly designed.** The source's B03
  framed strengths/limits as a design-tell verdict ("what it gets right...
  what it bites"); Plain keeps only the mechanism and its two failure
  directions, no judgment on the design choice itself.
- **Not a claim about any specific deck, template, or UI.** $485M → $512M
  is the source sheet's own literal worked example, kept because it's the
  concrete case the source itself names — not an invented screen or
  button.
- **Not "the skill decides what the deck should say."** The whole point of
  the wrong-guess/falsification pair (B01) is the opposite: it swaps a
  figure you named, nothing it inferred about the story that figure tells.

## Handoff prompt (BHTF, read aloud)

> "Give Claude a few sentences that repeat one figure in different
> contexts — say, '$485M in revenue, up from $420M last quarter... book
> value near $485M...' — and ask it to replace every instance of $485M
> with $512M, and change nothing else. Then check whether a nearby
> sentence built on the old number is still literally true, or whether the
> figure moved while the sentence around it stayed exactly where it was."

Why it's worth running: watching whether the surrounding sentence keeps up
with the number is the fastest way to see the boundary of a figure swap,
instead of assuming the whole passage got reconsidered along with it.

---
**GATE P — signed:** ______________________ (human)
