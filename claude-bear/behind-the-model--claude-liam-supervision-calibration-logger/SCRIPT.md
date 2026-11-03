# How Do You Know If You're Supervising Claude Enough? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-supervision-calibration-logger`,
CLI-explainer → Plain). Register: **Plain**. 9 beats.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion (no puppet host in hai-simple).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone wonders if they're careful enough with Claude. That's the wrong question — carefulness doesn't scale by task. What matters is whether your checking effort matches how much you're trusting it to decide. Liam explains." | writer types "Am I being / careful enough / with Claude?", hesitates on "careful", corrects to "calibrated" |
| B01 | 1 stakes / 2 wrong guess, falsified | The natural assumption is that supervision is one habit — either you double-check things or you don't, and that habit follows you everywhere. But not every task hands Claude the same amount of trust: some are quick copy-paste edits, others are real decisions made mostly by the model. A flat habit can't track that difference. Only logging how much you actually verified, task by task, can — and the mismatch stays invisible until you do. | left: "ONE FLAT HABIT" — a single unchanging gauge, struck; right: "LOGGED, TASK BY TASK" — three entries, levels against minutes checked |
| B02 | 3 mechanism | The fix isn't trying harder to be careful — it's building something to log it. A small tool that does three things: log each interaction as it happens, classify how much decision-making you actually handed to Claude — a quick edit, an assisted task, or a real decision made mostly by the model — and once a week, audit for the gap: high-autonomy interactions that got almost no verification time. | a three-step flow card: LOG → CLASSIFY → AUDIT |
| B03 | **4 anchor planted** | Run it on a real week: twelve interactions, plotted on a grid — how much you relied on Claude across the bottom, how long you actually spent checking up the side. Most land near the diagonal, right where usage and verification match. Three sit in the danger corner: heavy reliance, almost no time spent checking at all. | THE ANCHOR — 12-dot usage/supervision grid, diagonal line, 3 red dots in the danger corner |
| B04 | 3 mechanism, continued | The three danger-corner interactions get named, not just counted. Each one gets a suggested next step, matched to what it actually was: a quick code check for a script that was never reviewed, a second opinion for a decision that leaned hard on Claude's judgment. The log turns from a report into a to-do list. | the 3 danger-corner dots, each tagged with a recommended-step label |
| B05 | **4 anchor payoff** / 5 both directions | Run the audit again in two weeks, and the danger corner should empty out — that's real progress, the gap closing. But a rising score only proves you logged more checking time against those interactions; it doesn't prove the checking itself caught anything. And an interaction outside the danger corner isn't automatically fine — it just means this week's tool didn't flag it. | THE ANCHOR RETURNS — same grid, danger corner shrinks; splits into "score rising ≠ verified well" and "not flagged ≠ automatically fine" |
| **BCRY** | **6 carry-out** | Supervision isn't one habit you either have or don't — it's the gap between how much you're trusting Claude and how long you actually checked, and that gap stays invisible until you log it. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Log ten interactions you've had with Claude this week, one sentence each. For each, note how much decision-making you handed over, and how many minutes you actually spent checking the result. Then look for the pattern: is your longest checking time going to the highest-trust interactions, or somewhere else? Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | How Do You Know If You're Supervising Claude Enough? Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the wrong guess before B02 opens the mechanism |
| Wrong guess surfaced *and falsified by a case* | B01 states "supervision is one habit... follows you everywhere"; falsified by "not every task hands Claude the same amount of trust... a flat habit can't track that difference" |
| Exactly one inference flag | none needed — every claim here is stated directly from the source sheet's own facts (log/classify/audit mechanism, the 12-interaction demo, the revision loop, the two-week re-audit) — no inference leap beyond the source |
| One anchor, planted early, paid off late | B03 → B05 (the 12-interaction usage/supervision grid, 3 danger-corner dots) |
| Both failure directions | B05: "a rising score only proves more logged checking time, not that the checking caught anything" / "not flagged isn't automatically fine, it just wasn't caught by this pass" |
| No design judgment | B01/B02/B04 describe what the log does and where it stops; no verdict on whether the practice is well designed |

## Deliberately not claimed

- **Not that "careful" is meaningless.** B00's correction is that carefulness
  isn't *measurable* as a flat trait — the reel never claims caring doesn't
  matter, only that it needs to be matched to task-level trust to be useful.
- **Not a claim about any specific product UI or command syntax.** The
  source describes an actual `log`/`classify`/`audit` CLI tool with a
  named classifier model; this redo keeps the mechanism (record, classify
  by level, audit for the gap) as plain narration and drops the terminal
  commands and the model name — general audience, no invented or stale
  product specifics.
- **Not "a passing score means you're safe."** B05 is the explicit guard
  against that reading: the score measures logged verification time
  against a threshold, not verification quality.

## Handoff prompt (BHTF, read aloud)

> "Log ten interactions I've had with Claude this week, one sentence each.
> For each, note how much decision-making I handed over and how many
> minutes I actually spent checking the result. Help me see whether my
> longest checks are going to the highest-trust interactions — or
> somewhere else."

Why it's worth running: the pattern (or its absence) is the whole point —
most people assume their checking effort already tracks the stakes, and a
ten-entry log is usually enough to show whether it actually does.

---
**GATE P — signed:** ______________________ (human)
