# What Actually Happens When Claude "Initiates Coverage"? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-initiating-coverage`, Teardown -> Plain).
Register: **Plain**. 7 beats.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion (no puppet host in hai-simple).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone asks whether initiating coverage means Claude produces the whole report instantly, in one pass. It doesn't. Liam is here to take you through exactly how the skill actually works, task by task." | writer types "What produces / the report — / instantly?", hesitates on "instantly", corrects to "five ordered tasks" |
| B01 | 1 stakes / 2 wrong guess, falsified | The natural guess is that initiating coverage means Claude writes the whole report in one continuous pass, choosing whatever order makes sense. But the skill runs five fixed tasks, in order — company research, financial modeling, valuation analysis, chart generation, and final report assembly — each one executed individually with its prerequisite verified first. Ask it to jump straight to valuation before a financial model exists, and there's nothing to value: task three's prerequisite isn't there, so it can't run. | a one-pass generator, struck; a five-task ordered chain, lit |
| B02 | 3 mechanism / **4 anchor planted** | What the skill actually does: task one produces company research as a markdown document, task two builds a financial model in Excel, task three runs valuation analysis from that model's numbers, task four generates charts, and task five assembles everything into a final report as a Word document. Watch the anchor: one ticker's coverage package moving through all five tasks, in order. Each task waits until the deliverable before it exists and has been verified, before it starts. | THE ANCHOR — five cards (RESEARCH / MODEL / VALUATION / CHARTS / REPORT), one ticker package traveling through all five, in order |
| B03 | **4 anchor payoff** / 5 both directions | The coverage package comes out the other side as a finished report — but every task along the way ran only because the one before it had already produced a verified deliverable. That proves the order was respected: no step started on an input that wasn't there yet. It doesn't prove the analysis inside each step was sound — a financial model can pass verification with unrealistic growth assumptions built into it. And if a task can't start because an earlier deliverable isn't ready, that's a sequencing gap, not evidence that the earlier research itself was bad. | THE ANCHOR RETURNS — the five-card chain, resting at REPORT; splits into "ran is not sound" and "blocked is not bad" |
| **BCRY** | **6 carry-out** | Initiating coverage doesn't mean Claude writes a report in one pass — it runs five fixed tasks, in order, and each one is blocked until the task before it hands over a verified deliverable. A finished report means the chain completed end to end, not that a person checked the assumptions inside it. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Pick a public company you know. Ask Claude to do three things in order: research the company, sketch a simple financial projection, then value it from that projection — and have it show you each step's output before starting the next. Then ask it to skip straight to the valuation without the projection step, and watch what happens. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | What Actually Happens When Claude Initiates Coverage? Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the wrong guess before B02 opens the mechanism |
| Wrong guess surfaced *and falsified by a case* | B01 states "writes the whole report in one continuous pass"; falsified by "jump straight to valuation before a financial model exists — task three's prerequisite isn't there, so it can't run" |
| Exactly one inference flag | none needed — every claim is stated directly from the source sheet's own facts (no inference leap) |
| One anchor, planted early, paid off late | B02 -> B03 (one ticker's coverage package moving through RESEARCH / MODEL / VALUATION / CHARTS / REPORT, in order) |
| Both failure directions | B03: "ran is not sound" (a completed task doesn't mean the analysis inside it was correct) / "blocked is not bad" (a task that can't start doesn't mean the earlier research was wrong) |
| No design judgment | B01/B02/B03 describe what the skill does and where it stops; no verdict on whether it was built well |

## Deliberately not claimed

- **Not that the skill is "wrong" or poorly designed.** Teardown's B03 in
  the source framed strengths/limits as a design-tell verdict ("gets
  right: repeatable results... bites: anything outside the spec"); Plain
  keeps only the mechanism and its two failure directions, no judgment on
  the design choice itself.
- **Not a claim about any specific company, ticker, or report format.**
  The anchor (one coverage package moving through five tasks) is a
  generic, unnamed example — no invented screen, dashboard, or output UI.
- **Not "the skill checks the analysis for you."** The whole point of the
  both-directions beat (B03) is the opposite: it enforces sequencing and
  prerequisite existence, not the soundness of the judgment calls inside
  each task.
- **Not a specific claim about what "verified prerequisite" checks
  internally.** The source states only that prerequisites are verified and
  that tasks 3–5 depend on earlier tasks — the reel states that structure
  without inventing what the verification step examines.

## Handoff prompt (BHTF, read aloud)

> "Pick a public company you know. Ask Claude to research the company,
> sketch a simple financial projection, then value it from that
> projection — and have it show you each step's output before starting
> the next. Then ask it to skip straight to the valuation without the
> projection step, and watch what happens."

Why it's worth running: watching a step refuse to produce something real
when its input is missing is the fastest way to see that the workflow
enforces order and dependency, rather than just trusting that it does.

---
**GATE P — signed:** ______________________ (human)
