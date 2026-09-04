# Is Claude's Financial Plan Its Own Judgment? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-financial-plan`, Teardown -> Plain).
Register: **Plain**. 7 beats.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion (no puppet host in hai-simple).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone asks whether Claude's financial plan reflects its own judgment about what's best for the client. It doesn't. Liam is here to take you through what the skill actually does, step by step." | writer types "What decides / my financial plan — / judgment?", hesitates on "judgment", corrects to "a skill" |
| B01 | 1 stakes / 2 wrong guess, falsified | The natural guess is that Claude's plan reflects its own judgment about what's best for you — like an advisor who's gotten to know your situation and reached a conclusion. But the skill doesn't have an opinion. It only recognizes the cases the file names — onboarding, an annual review, a scenario request — and only builds the four things the file names: retirement projections, education funding, estate planning, cash flow analysis. Ask for something outside that list, and there's no independent expertise underneath to fall back on. | an advisor figure weighing a conclusion, struck; trigger tags feeding a steps card, lit; a fifth, unlisted request left dim and unconnected |
| B02 | 3 mechanism / **4 anchor planted** | What the skill actually does is read SKILL.md once, then run its steps in order for whichever case triggered it — onboarding, a review, or a scenario request — producing retirement projections, education funding, estate planning, and cash flow analysis. Watch the anchor: change one input, say the retirement age, and the plan updates by running the exact same steps again. | THE ANCHOR — a retirement-age dial wired directly to a single savings-target readout |
| B03 | **4 anchor payoff** / 5 both directions | Turn that same dial across a few scenarios, and you'll see both directions. A savings target that jumps a lot when you move the retirement age by five years doesn't mean the skill is improvising — it's still the same four steps, just fed a different number. And a savings target that barely changes between two close retirement ages doesn't mean the skill weighed them and decided both are fine — it means the inputs were close, and the same fixed steps produced a similar result. | THE ANCHOR RETURNS as a small scenario grid; splits into "jumps ≠ improvising" and "steady ≠ judged fine" |
| **BCRY** | **6 carry-out** | A financial plan from Claude is its skill running fixed steps over the inputs you gave it — not a judgment about what's best for you. Change the input, and the plan updates; that's all that happened. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Give Claude a retirement age, a target retirement income, and one planning goal — say, saving for a child's education — and ask it to run the financial-plan skill to build a plan around those inputs. Then change only the retirement age by five years and watch how much of the plan actually moves. That's the fastest way to see how much of a "plan" is really the same fixed steps, rerun. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | Is Claude's Financial Plan Its Own Judgment? Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the wrong guess before B02 opens the mechanism |
| Wrong guess surfaced *and falsified by a case* | B01 states "reflects its own judgment, like an advisor"; falsified by "ask for something outside that list, and there's no independent expertise underneath to fall back on" |
| Exactly one inference flag | none needed — every claim here is stated directly from the source sheet's own facts (no inference leap) |
| One anchor, planted early, paid off late | B02 -> B03 (the retirement-age dial driving the single savings-target readout, then turned across a small scenario grid) |
| Both failure directions | B03: "jumps a lot doesn't mean improvising" / "barely changes doesn't mean judged fine" |
| No design judgment | B01/B02/B03 describe what the skill does and where it stops; no verdict on whether it was built well |

## Deliberately not claimed

- **Not that the skill is "wrong" or poorly designed.** Teardown's B03/BVDT in
  the source framed strengths/limits as a design-tell verdict ("gets right...
  bites"); Plain keeps only the mechanism and its two failure directions, no
  judgment on the design choice itself.
- **Not a claim about any specific client, dollar figure, or Excel/PDF UI.**
  The anchor (retirement age -> savings target) is the standard structural
  sensitivity any retirement projection has, described generically — no
  invented screen, form, or output format.
- **Not "the skill decides the client's retirement age or goals."** The whole
  point of the wrong-guess/falsification pair (B01) is the opposite: it runs
  the inputs it's given through fixed steps, it does not originate them from
  its own judgment about the client.

## Handoff prompt (BHTF, read aloud)

> "Give Claude a retirement age, a target retirement income, and one planning
> goal — say, saving for a child's education — and ask it to run the
> financial-plan skill to build a plan around those inputs. Then change only
> the retirement age by five years and watch how much of the plan actually
> moves."

Why it's worth running: watching how much the plan moves for a five-year
change in a single input is the fastest way to see how much of a "plan" is
fixed procedure rather than judgment about your life — instead of trusting
the plan's apparent personalization.

---
**GATE P — signed:** ______________________ (human)
