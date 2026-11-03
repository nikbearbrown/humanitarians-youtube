# How Does Claude Rank AI-Readiness Across a Portfolio? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-ai-readiness`, Teardown -> Plain).
Register: **Plain**. 7 beats.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion (no puppet host in hai-simple).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone asks whether Claude decides which portfolio company is most ready for AI using its own judgment. It doesn't. Liam is here to take you through what the skill actually does, step by step." | writer types "What decides / which portco — / judgment?", hesitates on "judgment", corrects to "the update" |
| B01 | 1 stakes / 2 wrong guess, falsified | The natural guess is that Claude decides, using its own judgment, which portfolio company is most ready for AI investment. But the skill doesn't work that way. For each company, it ingests the quarterly update and financials, and identifies the quick wins written there. Give it a company whose update never mentions an AI opportunity, and it won't invent one — there's nothing in the update to work from, so nothing gets ranked for that company this quarter. | a judgment figure vs. an ingest/identify/rank procedure card; the judgment side struck, the procedure lit |
| B02 | 3 mechanism / **4 anchor planted** | What the skill actually does: for each portfolio company, it ingests the quarterly update and financials, identifies the quick wins written there, and stacks them into one ranked action list — nothing more. Watch the anchor: one portfolio company's Q3 update. It's ingested, the quick wins are identified, they're scored against the spec's criteria, and the company lands a place in the stacked list. Then it stops, waiting. | THE ANCHOR — four cards (INGESTED / QUICK WINS FOUND / SCORED / RANKED), one company's Q3 update traveling through all four, halting at the last one |
| B03 | **4 anchor payoff** / 5 both directions | That ranking is built — ingested, scored, placed in the stack, ready for review. But a high rank only means the update scored well against the spec's criteria: it isn't the same as being the single best next AI investment across the whole portfolio. And a company that ranks low this quarter doesn't mean it has no AI opportunity — it can mean this update simply didn't mention one, which sits outside what the skill can see. Either way, the ranked list still waits for an operating partner's call before anything gets funded. | THE ANCHOR RETURNS, ranked and waiting; splits into "scored well is not best overall" and "ranked low is not no opportunity" |
| **BCRY** | **6 carry-out** | A ranked AI-readiness list isn't Claude's judgment about which portfolio company is smartest to back — it's a ranking built from what this quarter's updates actually say, waiting for an operating partner's call before anything gets funded. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Give Claude one portfolio company's latest quarterly update and financials, and ask it to run the ai-readiness skill: identify the quick wins and rank where AI investment should go first. Then hand it a company update that never mentions AI at all, and ask it to run the same skill again — watch what it does when there's nothing in the update to work from. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | How Does Claude Rank AI-Readiness Across a Portfolio? Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the wrong guess before B02 opens the mechanism |
| Wrong guess surfaced *and falsified by a case* | B01 states "decides using its own judgment"; falsified by "give it a company whose update never mentions AI and it ranks nothing for that company" |
| Exactly one inference flag | none needed — every claim here is stated directly from the source sheet's own facts (no inference leap) |
| One anchor, planted early, paid off late | B02 -> B03 (one portfolio company's Q3 update: ingested → quick wins found → scored → ranked, then stopped, waiting) |
| Both failure directions | B03: "scored well isn't the same as best overall" / "ranked low doesn't mean no opportunity" |
| No design judgment | B01/B02/B03 describe what the skill does and where it stops; no verdict on whether it was built well |

## Deliberately not claimed

- **Not that the skill is "wrong" or poorly designed.** Teardown's B03 in the
  source framed strengths/limits as a design-tell verdict ("repeatable
  results... bites: anything outside the spec"); Plain keeps only the
  mechanism and its two failure directions, no judgment on the design
  choice itself.
- **Not a claim about any specific company, dollar figure, or UI.** The
  anchor (one portfolio company's Q3 update, ranked and waiting) is a
  generic, unnamed example — no invented screen, dashboard, or output
  format.
- **Not "the skill decides which companies deserve AI investment."** The
  whole point of the wrong-guess/falsification pair (B01) is the opposite:
  it ingests and ranks only what the quarterly updates and financials
  already give it, nothing it inferred itself from general knowledge of the
  portfolio companies or their industries.

## Handoff prompt (BHTF, read aloud)

> "Give Claude one portfolio company's latest quarterly update and
> financials, and ask it to run the ai-readiness skill: identify the quick
> wins and rank where AI investment should go first. Then hand it a company
> update that never mentions AI at all, and ask it to run the same skill
> again."

Why it's worth running: watching what happens when the update has nothing
to work from is the fastest way to see that the skill ranks from what's
written, instead of judgment — rather than just trusting that it does.

---
**GATE P — signed:** ______________________ (human)
