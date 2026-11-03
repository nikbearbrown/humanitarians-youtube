# What Does Claude Actually Do When You Say "Clean This Data"? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-clean-data-xls`, Teardown -> Plain).
Register: **Plain**. 7 beats.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion (no puppet host in hai-simple).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone asks whether cleaning messy spreadsheet data means Claude uses its own judgment. It doesn't. Liam is here to take you through exactly what the skill does, step by step." | writer types "What decides / what gets cleaned — / judgment?", hesitates on "judgment", corrects to "a checklist" |
| B01 | 1 stakes / 2 wrong guess, falsified | The natural guess is that "clean this data" means Claude decides, using its own judgment, what looks wrong and fixes it. But the skill runs one fixed checklist: trim whitespace, fix inconsistent casing, convert numbers stored as text, standardize dates, remove duplicates, and flag mixed-type columns — nothing more. Give it a column where the same currency symbol covers two different currencies, no way to tell them apart. That's not on the checklist. No step resolves currency confusion, so the column comes out exactly as ambiguous as it went in. | a judgment figure vs. a six-step checklist card; the judgment side struck, the checklist lit |
| B02 | 3 mechanism / **4 anchor planted** | What the skill actually does: it runs six fixed steps, in order — trim, fix casing, convert numbers, standardize dates, dedupe, flag mixed types — nothing beyond that list. Watch the anchor: one Revenue column holding " 1,200 ", "1300", "N/A", and " 1,400.00 ". Whitespace gets trimmed. The number-like text converts to real numbers. "N/A" can't convert, so the column gets flagged mixed-type instead. Then it stops, waiting. | THE ANCHOR — four cards (RAW / TRIMMED / CONVERTED / FLAGGED), one Revenue column traveling through all four, halting at the last one |
| B03 | **4 anchor payoff** / 5 both directions | The Revenue column comes back trimmed, converted, and flagged — "N/A" still sitting there, marked for a human to look at. But converting "1,200" to a number doesn't mean it's the *right* number: a typo that should read "12,000" converts just as cleanly. And a flagged mixed-type column isn't automatically broken — an ID column that mixes numbers and letters on purpose gets the same flag. Either way, the cleaned sheet still waits for someone to check what the checklist can't: whether the values themselves are correct. | THE ANCHOR RETURNS, trimmed/converted/flagged; splits into "converted cleanly is not correct" and "flagged is not broken" |
| **BCRY** | **6 carry-out** | Clean this data doesn't mean Claude judges what looks messy and fixes it — it runs one fixed checklist, in order, and anything outside that list is untouched. A column that comes back clean has been reformatted, not fact-checked. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Give Claude a spreadsheet with a messy column — mixed date formats, extra whitespace, a duplicate row or two — and ask it to run the clean-data-xls skill. Then add one problem that's not on its checklist, like the same currency symbol covering two different currencies, and run it again. Watch what changes, and what doesn't. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | What Does Claude Actually Do When You Say "Clean This Data"? Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the wrong guess before B02 opens the mechanism |
| Wrong guess surfaced *and falsified by a case* | B01 states "decides using its own judgment"; falsified by "a column mixing two currencies under one symbol isn't on the checklist, so it comes out unchanged" |
| Exactly one inference flag | none needed — every claim here is stated directly from the source sheet's own facts (no inference leap) |
| One anchor, planted early, paid off late | B02 -> B03 (one Revenue column: " 1,200 " / "1300" / "N/A" / " 1,400.00 " — trimmed → converted → flagged, then stopped, waiting) |
| Both failure directions | B03: "converted cleanly is not the same as correct" / "flagged is not the same as broken" |
| No design judgment | B01/B02/B03 describe what the skill does and where it stops; no verdict on whether it was built well |

## Deliberately not claimed

- **Not that the skill is "wrong" or poorly designed.** Teardown's B03 in the
  source framed strengths/limits as a design-tell verdict ("gets right:
  repeatable results... bites: anything outside the spec"); Plain keeps only
  the mechanism and its two failure directions, no judgment on the design
  choice itself.
- **Not a claim about any specific spreadsheet, company, or UI.** The anchor
  (one Revenue column with four sample values) is a generic, unnamed
  example — no invented screen, dashboard, or output format.
- **Not "the skill fixes anything messy."** The whole point of the
  wrong-guess/falsification pair (B01) is the opposite: it runs exactly the
  six operations named in the SKILL.md, nothing it inferred itself from a
  general sense of what "clean" data should look like.

## Handoff prompt (BHTF, read aloud)

> "Give Claude a spreadsheet with a messy column — mixed date formats, extra
> whitespace, a duplicate row or two — and ask it to run the
> clean-data-xls skill. Then add one problem that's not on its checklist,
> like the same currency symbol covering two different currencies, and run
> it again."

Why it's worth running: watching what does and doesn't change is the
fastest way to see that the skill runs a fixed list of operations, instead
of general-purpose judgment — rather than just trusting that it does.

---
**GATE P — signed:** ______________________ (human)
