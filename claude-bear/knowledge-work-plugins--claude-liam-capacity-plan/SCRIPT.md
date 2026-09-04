# How Does Claude Plan Team Capacity? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-capacity-plan`, Teardown -> Plain).
Register: **Plain**. 7 beats.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion (no puppet host in hai-simple).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone asks whether Claude spots an overloaded team by instinct — a feel for who's stretched thin. It doesn't. Liam is here to take you through what the capacity-plan skill actually does, step by step." | writer types "How does Claude spot / an overloaded team — / instinct?", hesitates on "instinct", corrects to "the file" |
| B01 | 1 stakes / 2 wrong guess, falsified | The natural guess is that Claude senses an overloaded team the way an experienced manager would — reading strain into how a request is phrased. But the skill doesn't work that way. It runs two fixed steps: workload analysis, which totals each person's committed hours against their available capacity, then utilization forecasting, which projects that load forward across the quarter. Hand it a request with no workload or capacity numbers attached, and there's nothing for either step to run on. | a "manager's instinct" figure with a scattered thought-bubble, struck; a two-step procedure card lit instead |
| B02 | 3 mechanism / **4 anchor planted** | What the skill actually does: run the workload analysis first, then forecast utilization from it. Watch the anchor: a team heading into quarterly planning says they're slammed. The question gets asked, matched to "team feels overallocated, need the numbers", stepped through — total each person's committed hours, project the load across the quarter — and returns one answer: utilization sits at a hundred eighteen percent, hire one person or cut one project. | THE ANCHOR — four cards (ASKED / MATCHED / STEPPED / RETURNED), the "118% UTILIZATION" token traveling through all four, landing on "hire one or cut one project" |
| B03 | **4 anchor payoff** / 5 both directions | That answer holds because the same two steps run identically every time — ask again with the same workload and capacity numbers, and the same utilization figure and the same recommendation come back. But ask something outside that frame — say, whether the team's morale can take the load — and there's nothing tailored to reach for; the analysis stops exactly at the numbers those two steps compute. | THE ANCHOR RETURNS, condensed; splits into "run twice — same numbers" and "team morale? — no shape" |
| **BCRY** | **6 carry-out** | Capacity-plan isn't Claude sensing that your team is stretched thin — it's a written two-step procedure, workload analysis then utilization forecasting, run on the numbers you give it, and it only answers what those two steps compute. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Tell me your team is committed to a hundred eighteen percent of capacity heading into next quarter, and run the capacity-plan skill: have it work the workload analysis, forecast utilization, and report the number and the recommendation. Then ask something outside that frame — whether the team's morale can take it — and see whether it invents an answer or tells you plainly the two steps don't cover that. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | How Does Claude Plan Team Capacity? Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the wrong guess before B02 opens the mechanism |
| Wrong guess surfaced *and falsified by a case* | B01 states "the way an experienced manager would — reading strain into how a request is phrased"; falsified by "hand it a request with no workload or capacity numbers attached, and there's nothing for either step to run on" |
| Exactly one inference flag | none needed — every claim here is stated directly from the source sheet's own facts (no inference leap) |
| One anchor, planted early, paid off late | B02 -> B03 (team at 118% utilization heading into quarterly planning: asked → matched → stepped → returned "hire one or cut one project", then run twice / hits a question outside the file) |
| Both failure directions | B03: "same input, same numbers, twice" (holds) / "team morale has nothing tailored to reach for" (flips) |
| No design judgment | B01/B02/B03 describe what the skill does and where it stops; no verdict on whether it was built well |

## Deliberately not claimed

- **Not that the skill is "wrong" or poorly designed.** Teardown's B03/BVDT
  in the source framed strengths/limits as a design-tell verdict ("what it
  gets right: repeatable results... what it bites: anything outside the
  spec"); Plain keeps only the mechanism and its two failure directions, no
  judgment on the design choice itself.
- **Not a claim about any specific company, team, or headcount figure.**
  The anchor (a team at 118 percent utilization heading into quarterly
  planning) is a generic, illustrative capacity-planning scenario — no
  invented dashboard, tool, or output format beyond what the source
  describes.
- **Not "the skill judges whether a team is actually overworked."** The
  whole point of the wrong-guess/falsification pair (B01) is the opposite:
  it runs two fixed steps on the numbers you supply, nothing it infers
  independently from tone or manager instinct.

## Handoff prompt (BHTF, read aloud)

> "Tell me my team is committed to 118% of capacity heading into next
> quarter, and run the capacity-plan skill: work the workload analysis,
> forecast utilization, and report the number and the recommendation. Then
> ask something outside that frame — whether the team's morale can take
> it."

Why it's worth running: watching whether Claude invents a bespoke answer
for an unsupported question, or tells you plainly that it has nothing
tailored for it, is the fastest way to see that the plan comes from a
written, numbers-driven procedure rather than manager instinct — rather
than just trusting that it does.

---
**GATE P — signed:** ______________________ (human)
