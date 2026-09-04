# How Does Claude Analyze Data? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-analyze`, Teardown -> Plain).
Register: **Plain**. 7 beats.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion (no puppet host in hai-simple).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone asks whether Claude's data analysis comes from sharp instinct about what's interesting. It doesn't. Liam is here to take you through what the skill actually does, step by step." | writer types "What makes Claude's / data analysis smart — / instinct?", hesitates on "instinct", corrects to "the file" |
| B01 | 1 stakes / 2 wrong guess, falsified | The natural guess is that Claude's data analysis comes from something like an analyst's feel for what's interesting in the numbers. But the skill doesn't work that way. It reads what kind of question you're asking — a quick metric lookup, an investigation into what's driving a trend or a drop, a comparison across segments over time, or a formal report for stakeholders — then runs the steps written for that kind of question, in order. Ask it something that isn't one of those four shapes, and it has no procedure tailored to reach for. | an "analyst's feel" figure with a scattered thought-bubble, struck; a four-shape classifier card lit instead |
| B02 | 3 mechanism / **4 anchor planted** | What the skill actually does: read the question, match it to its shape, then run the file's steps in order and return one answer. Watch the anchor: weekly signups drop twelve percent. The question gets asked, matched to "what's driving a trend or drop", stepped through — pull the metric, break it down by segment, isolate what changed — and returns one answer: organic search traffic fell while paid channels held steady. | THE ANCHOR — four cards (ASKED / MATCHED / STEPPED / RETURNED), the "SIGNUPS DROP 12%" token traveling through all four, landing on "organic search fell" |
| B03 | **4 anchor payoff** / 5 both directions | That answer holds because the steps ran the same way every time — ask the same drop question twice, and the match, the steps, and the driver come back identical. But ask something outside those four shapes — say, whether to cut next quarter's marketing budget — and there's nothing tailored to reach for; the analysis stops exactly where SKILL.md's four shapes stop. | THE ANCHOR RETURNS, condensed; splits into "run twice — same driver" and "cut budget? — no shape" |
| **BCRY** | **6 carry-out** | A Claude data analysis isn't an analyst's feel for what's interesting — it's a written procedure that matches your question to one of four shapes and runs the same steps every time, and it only covers question shapes the file defines. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Tell me weekly signups dropped twelve percent, and run the analyze skill: have it match the question, walk the steps, and report the driver. Then ask for something outside those four shapes — a forecast, or a recommendation — and see whether it invents a new procedure or tells you plainly it has nothing tailored for that. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | How Does Claude Analyze Data? Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the wrong guess before B02 opens the mechanism |
| Wrong guess surfaced *and falsified by a case* | B01 states "something like an analyst's feel for what's interesting"; falsified by "ask it something outside the four shapes and it has no procedure tailored to reach for" |
| Exactly one inference flag | none needed — every claim here is stated directly from the source sheet's own facts (no inference leap) |
| One anchor, planted early, paid off late | B02 -> B03 (weekly signups drop 12%: asked → matched → stepped → returned "organic search fell", then run twice / hits a question shape outside the file) |
| Both failure directions | B03: "same input, same driver, twice" (holds) / "a question outside the four shapes has nothing tailored to reach for" (flips) |
| No design judgment | B01/B02/B03 describe what the skill does and where it stops; no verdict on whether it was built well |

## Deliberately not claimed

- **Not that the skill is "wrong" or poorly designed.** Teardown's B03/BVDT
  in the source framed strengths/limits as a design-tell verdict ("what it
  gets right: repeatable results... what it bites: anything outside the
  spec"); Plain keeps only the mechanism and its two failure directions, no
  judgment on the design choice itself.
- **Not a claim about any specific company, dataset, or metric figure.**
  The anchor (weekly signups dropping twelve percent, traced to organic
  search) is a generic, illustrative analytics scenario — no invented
  dashboard, tool, or output format beyond what the source describes.
- **Not "the skill decides what's worth investigating in this dataset."**
  The whole point of the wrong-guess/falsification pair (B01) is the
  opposite: it matches the question you asked to one of four shapes the
  file already defines, nothing it inferred independently from analyst
  instinct.

## Handoff prompt (BHTF, read aloud)

> "Tell me weekly signups dropped twelve percent, and run the analyze
> skill: match the question to its shape, walk the steps, and report the
> driver. Then ask for something outside those four shapes — a forecast or
> a recommendation."

Why it's worth running: watching whether Claude invents a bespoke line of
analysis for an unsupported question shape, or tells you plainly that it
has nothing tailored for it, is the fastest way to see that the analysis
tailors from a written file rather than private instinct — rather than
just trusting that it does.

---
**GATE P — signed:** ______________________ (human)
