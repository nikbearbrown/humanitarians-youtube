# How Does Claude Prep for a Due Diligence Meeting? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-dd-meeting-prep`, Teardown -> Plain).
Register: **Plain**. 7 beats.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion (no puppet host in hai-simple).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone asks whether Claude just knows the sharp questions to ask on a diligence call, from instinct. It doesn't. Liam is here to take you through what the skill actually does, step by step." | writer types "What decides / the questions — / instinct?", hesitates on "instinct", corrects to "the file" |
| B01 | 1 stakes / 2 wrong guess, falsified | The natural guess is that Claude draws on some private sense of what makes a sharp diligence question, and asks whatever an experienced deal person might ask on instinct. But the skill doesn't work that way. It reads which meeting you're prepping for — a management presentation, an expert network call, a customer reference, or an advisor session — then builds a targeted question list, the benchmarks to reference, and the red flags to probe, all from what the file already defines for that meeting type. Ask it to prep a meeting type the file doesn't cover, and it has nothing tailored to reach for. | an "instinct" figure with a scattered thought-bubble, struck; a meeting-type-to-outputs procedure card lit instead |
| B02 | 3 mechanism / **4 anchor planted** | What the skill actually does: match the meeting type to its template, then generate the question list, attach the benchmarks, and mark the red flags to probe. Watch the anchor: an expert network call about a staffing company. One question — same-store margin trend — gets drafted, gets a benchmark attached, gets asked live on the call, and comes back flagged: the expert's answer leans on one large client. | THE ANCHOR — four cards (DRAFTED / BENCHMARKED / ASKED / FLAGGED), the "same-store margin" token traveling through all four, landing flagged |
| B03 | **4 anchor payoff** / 5 both directions | That flag surfaces because the question was built to probe for exactly that — the skill escalates what its template already watches for, it doesn't go hunting beyond that. Prep the same expert-network call twice, and the question list, benchmarks, and red flags come back identical both times. But ask for a meeting type the file never described — say, a regulator sit-down — and there's nothing tailored to reach for; the prep stops exactly where SKILL.md does. | THE ANCHOR RETURNS, condensed; splits into "run twice — same questions" and "regulator sit-down — no template" |
| **BCRY** | **6 carry-out** | A Claude due-diligence meeting prep isn't insider instinct about what to ask — it's a written procedure that turns the meeting type into a question list, benchmarks, and red flags to probe, and it only covers meeting types the file defines. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Tell me you're prepping for an expert network call on a staffing company, and run the dd-meeting-prep skill: build the question list, the benchmarks it attaches, and the red flags it would probe for. Then ask for a meeting type you've never mentioned supporting, and see whether new questions get invented or the prep stops where the file does. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | How Does Claude Prep for a Due Diligence Meeting? Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the wrong guess before B02 opens the mechanism |
| Wrong guess surfaced *and falsified by a case* | B01 states "asks whatever an experienced deal person might ask on instinct"; falsified by "ask it to prep a meeting type the file doesn't cover and it has nothing tailored to reach for" |
| Exactly one inference flag | none needed — every claim here is stated directly from the source sheet's own facts (no inference leap) |
| One anchor, planted early, paid off late | B02 -> B03 (expert network call, staffing company, "same-store margin trend": drafted → benchmarked → asked → flagged → then run twice / hits a meeting type outside the file) |
| Both failure directions | B03: "same input, same question list, twice" (holds) / "a meeting type the file never described has nothing tailored to reach for" (flips) |
| No design judgment | B01/B02/B03 describe what the skill does and where it stops; no verdict on whether it was built well |

## Deliberately not claimed

- **Not that the skill is "wrong" or poorly designed.** Teardown's B03 in the
  source framed strengths/limits as a design-tell verdict ("repeatable
  results... bites: anything outside the spec"); Plain keeps only the
  mechanism and its two failure directions, no judgment on the design
  choice itself.
- **Not a claim about any specific company, question, or benchmark figure.**
  The anchor (an expert network call on a staffing company, a same-store
  margin question flagged for customer concentration) is a generic,
  illustrative DD scenario — no invented screen, tool, or output format
  beyond what the source describes.
- **Not "the skill decides which questions matter for this deal."** The
  whole point of the wrong-guess/falsification pair (B01) is the opposite:
  it tailors from the meeting type against outputs the file already
  defines, nothing it inferred independently from deal-making instinct.

## Handoff prompt (BHTF, read aloud)

> "Tell me you're prepping for an expert network call on a staffing
> company, and run the dd-meeting-prep skill: build the question list, the
> benchmarks it attaches, and the red flags it would probe for. Then ask
> for a meeting type you've never mentioned supporting."

Why it's worth running: watching whether Claude invents a bespoke line of
questioning for an unsupported meeting type, or tells you plainly that it
has nothing tailored for it, is the fastest way to see that the prep
tailors from a written file rather than private instinct — rather than
just trusting that it does.

---
**GATE P — signed:** ______________________ (human)
