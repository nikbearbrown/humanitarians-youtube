# How Does Claude Build a Due Diligence Checklist? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-dd-checklist`, Teardown -> Plain).
Register: **Plain**. 7 beats.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion (no puppet host in hai-simple).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone asks whether Claude uses its own judgment to decide what belongs in a due diligence checklist. It doesn't. Liam is here to take you through what the skill actually does, step by step." | writer types "What decides / the checklist — / judgment?", hesitates on "judgment", corrects to "the file" |
| B01 | 1 stakes / 2 wrong guess, falsified | The natural guess is that Claude sizes up this specific deal and decides, from its own judgment, which risks are worth chasing. But the skill doesn't work that way. It reads the target's sector, deal type, and complexity, then builds the checklist from workstreams the file already defines — request lists, status tracking, red-flag escalation. Hand it a sector the file never lists, and it has no independent research to reach for. | a deal-judgment figure vs. a sector/type/complexity-to-workstreams procedure card; the judgment figure struck, the procedure lit |
| B02 | 3 mechanism / **4 anchor planted** | What the skill actually does: read the deal's sector, type, and complexity, then generate the workstreams that profile calls for, each with its own request list. Watch the anchor: a software company acquisition. "Customer contracts" goes out as a request, comes back received, gets reviewed — and one clause, heavy revenue concentration in a single customer, gets flagged as a red flag for the deal team. | THE ANCHOR — four cards (REQUESTED / RECEIVED / REVIEWED / FLAGGED), the "customer contracts" token traveling through all four, landing flagged |
| B03 | **4 anchor payoff** / 5 both directions | That flag reaches the deal team because the item was on the checklist to begin with — the skill escalates what it's already tracking, it doesn't go looking beyond the list. Ask for that same software acquisition checklist twice, and the workstreams and request items come back identical both times. But ask for a deal type the file never described — say, a mineral rights transfer — and there's nothing tailored to reach for; the checklist stops exactly where SKILL.md does. | THE ANCHOR RETURNS, condensed; splits into "run twice — same checklist" and "mineral rights transfer — no template, stops there" |
| **BCRY** | **6 carry-out** | A Claude due diligence checklist isn't independent judgment about a deal's risks — it's a written procedure that tailors known workstreams to the deal's sector and type, and it only flags what it's already tracking. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Give me a deal profile — say, a software company acquisition — and run the dd-checklist skill: build the workstreams, the request lists inside each one, and where red-flag escalation would trigger. Then ask for a sector or deal type you've never mentioned supporting, and see whether new workstreams get invented or the checklist stops where the file does. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | How Does Claude Build a Due Diligence Checklist? Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the wrong guess before B02 opens the mechanism |
| Wrong guess surfaced *and falsified by a case* | B01 states "decides from its own judgment which risks are worth chasing"; falsified by "hand it a sector the file never lists and it has no independent research to reach for" |
| Exactly one inference flag | none needed — every claim here is stated directly from the source sheet's own facts (no inference leap) |
| One anchor, planted early, paid off late | B02 -> B03 (software acquisition, "customer contracts": requested → received → reviewed → flagged → then run twice / hits a deal type outside the file) |
| Both failure directions | B03: "same input, same checklist, twice" (holds) / "a deal type the file never described has nothing tailored to reach for" (flips) |
| No design judgment | B01/B02/B03 describe what the skill does and where it stops; no verdict on whether it was built well |

## Deliberately not claimed

- **Not that the skill is "wrong" or poorly designed.** Teardown's B03 in the
  source framed strengths/limits as a design-tell verdict ("repeatable
  results... bites: anything outside the spec"); Plain keeps only the
  mechanism and its two failure directions, no judgment on the design
  choice itself.
- **Not a claim about any specific deal, workstream taxonomy, or UI.** The
  anchor (a software acquisition's customer-contracts request, flagged for
  revenue concentration) is a generic, illustrative DD scenario — no
  invented screen, tool, or output format beyond what the source describes.
- **Not "the skill decides which risks matter for this deal."** The whole
  point of the wrong-guess/falsification pair (B01) is the opposite: it
  tailors from sector, deal type, and complexity against workstreams the
  file already defines, nothing it inferred independently about this
  particular deal.

## Handoff prompt (BHTF, read aloud)

> "Give me a deal profile — say, a software company acquisition — and run
> the dd-checklist skill: build the workstreams, the request lists inside
> each one, and where red-flag escalation would trigger. Then ask for a
> sector or deal type you've never mentioned supporting."

Why it's worth running: watching whether Claude invents a bespoke workstream
for an unsupported deal type, or tells you plainly that it has nothing
tailored for it, is the fastest way to see that the checklist tailors from
a written file rather than independent judgment — rather than just
trusting that it does.

---
**GATE P — signed:** ______________________ (human)
