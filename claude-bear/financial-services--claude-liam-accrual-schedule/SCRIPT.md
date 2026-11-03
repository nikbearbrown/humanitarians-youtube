# How Does Claude Build an Accrual Schedule? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-accrual-schedule`, Teardown -> Plain).
Register: **Plain**. 7 beats.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion (no puppet host in hai-simple).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone asks whether Claude decides which expenses to accrue using its own accounting judgment. It doesn't. Liam is here to take you through what the skill actually does, step by step." | writer types "What decides / an accrual — / judgment?", hesitates on "judgment", corrects to "the support" |
| B01 | 1 stakes / 2 wrong guess, falsified | The natural guess is that Claude decides, using its own accounting judgment, which expenses and revenues belong in this period's accrual schedule. But the skill doesn't work that way. For each accrual, it computes the entry and cites the support that backs it. Give it an expense with no supporting document, and it won't invent a number — there's nothing for it to cite, so there's nothing to draft. | an accounting-judgment figure vs. a compute/cite/draft procedure card; the judgment figure struck, the procedure lit |
| B02 | 3 mechanism / **4 anchor planted** | What the skill actually does: for each accrual, it computes the entry, cites the support document behind it, and drafts the journal entry — nothing more. Watch the anchor: a December utility bill that won't be billed until January. It's identified, the entry is computed, the utility contract is cited as support, and a draft JE is created. Then it stops, waiting. | THE ANCHOR — four cards (IDENTIFIED / COMPUTED / CITED / DRAFTED), the bill token traveling through all four, halting at the last one |
| B03 | **4 anchor payoff** / 5 both directions | That draft is built — computed, cited, ready to review. But a drafted JE with a citation isn't the same as a correct entry: it only reflects what the cited document says, and a wrong document produces a wrong entry, cited correctly. And an accrual with no draft this period doesn't mean something broke — it can mean that expense has no qualifying support yet. Either way, the draft still waits for a controller before anything posts. | THE ANCHOR RETURNS, drafted and waiting; splits into "cited ≠ correct" and "no draft ≠ broken" |
| **BCRY** | **6 carry-out** | A drafted accrual JE isn't Claude's judgment about what you owe — it's a computed entry, tied to cited support, waiting for a controller's approval before anything posts. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Give Claude one expense that belongs in this period's close, with the invoice or contract as its support, and ask it to run the accrual-schedule skill: compute the entry, cite that document, and draft the JE. Then remove the supporting document and ask it to try the same accrual again, and watch what it does when there's nothing left to cite. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | How Does Claude Build an Accrual Schedule? Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the wrong guess before B02 opens the mechanism |
| Wrong guess surfaced *and falsified by a case* | B01 states "decides using its own accounting judgment"; falsified by "give it an expense with no supporting document and it drafts nothing" |
| Exactly one inference flag | none needed — every claim here is stated directly from the source sheet's own facts (no inference leap) |
| One anchor, planted early, paid off late | B02 -> B03 (December utility bill: identified → computed → cited → drafted → stopped, waiting) |
| Both failure directions | B03: "a cited entry isn't the same as a correct one" / "no draft doesn't mean the run failed" |
| No design judgment | B01/B02/B03 describe what the skill does and where it stops; no verdict on whether it was built well |

## Deliberately not claimed

- **Not that the skill is "wrong" or poorly designed.** Teardown's B03 in the
  source framed strengths/limits as a design-tell verdict ("repeatable
  results... bites: anything outside the spec"); Plain keeps only the
  mechanism and its two failure directions, no judgment on the design
  choice itself.
- **Not a claim about any specific dollar amounts, accounts, or UI.** The
  anchor (a December utility bill accrued into January) is a standard,
  generic period-end accrual example — no invented screen, ledger, or
  output format.
- **Not "the skill decides what counts as an accrual."** The whole point of
  the wrong-guess/falsification pair (B01) is the opposite: it computes and
  cites only what you and the supporting documents already give it,
  nothing it inferred itself.

## Handoff prompt (BHTF, read aloud)

> "Give Claude one expense that belongs in this period's close, with the
> invoice or contract as its support, and ask it to run the
> accrual-schedule skill: compute the entry, cite that document, and draft
> the JE. Then remove the supporting document and ask it to try the same
> accrual again."

Why it's worth running: watching what happens when the cited document
disappears is the fastest way to see that the skill computes from support,
instead of judgment — rather than just trusting that it does.

---
**GATE P — signed:** ______________________ (human)
