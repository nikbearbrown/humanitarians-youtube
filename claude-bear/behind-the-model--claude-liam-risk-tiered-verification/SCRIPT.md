# Reading Isn't Reviewing — Narration Script (GATE P)

*Skill: `hai-simple`. Register: **Plain**. Redo of
`anthropics/youtube/behind-the-model/claude-liam-risk-tiered-verification`
(Teardown register, CLI 10-beat spine: PROBLEM/ASK/CODE/OUTPUT/CHANGE/OUTPUT/
TEARDOWN/NEXT STEPS) — question, facts, and argument kept; body recompressed to
one idea per beat; cold open replaced; close re-skinned.*

*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (no puppet — hai-simple WRITER LAW).
**Narrator:** Liam, Kokoro `am_onyx` (unchanged from source).

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | Someone assumes that if Claude's answer looks right on a read-through, they've reviewed it. They haven't — they've only read it. So: what actually turns a read into a review? | writer types "If Claude's answer looks right, I've reviewed it — right?", hesitates on "reviewed", corrects to "read" |
| B01 | 1 stakes | Claude can hand you a citation, a number, a chart, code, or a recommendation — and every one of those can be wrong in a way that reads perfectly clean. Deciding whether an answer is actually right takes more than reading it carefully. | five output-type cards (CITATION, NUMBER, CHART, CODE, REC) converging on one "IS THIS RIGHT?" card |
| B02 | 2 wrong guess | That seems reasonable. If the wording is clean, the facts line up, and nothing looks out of place, a careful read feels like it should be enough — the same way a well-typed email doesn't need a second check. | a citation card, a magnifying glass passing over it, a checkmark forming |
| B03 | **2 BREAK IT — ANCHOR PLANTED** | Here's the case that breaks it: a fabricated citation, formatted exactly like a real one — right journal, right year, a title that sounds plausible. It reads perfectly clean. Opening the actual source is the only step that shows it doesn't exist. | THE ANCHOR — the citation card, checkmark forming, then cracking open to "SOURCE: NOT FOUND" |
| B04 | 3 mechanism | The fix is a tool, not more careful reading: `verification_gate.py` takes an output type and a risk level as arguments, and prints back three to five concrete, checkable steps — not a feeling, a list. | INPUT (type + risk level) → GEAR (the matrix) → OUTPUT (checklist) |
| B05 | 3 mechanism | The rules are specific to the combination. A citation always includes opening the actual source. A number at strict risk always includes an independent recalculation. A chart always gets its axis labels and its denominator checked. None of the six output types gets a generic checklist. | three-row table: CITATION → open the source; NUMBER@strict → recalculate; CHART → axis + denominator |
| B06 | 3 mechanism | Run it three times. Citation at strict: four steps, ending in open the source. Number at moderate: three steps — spot-check, denominator, units. Code at light: a two-step skim for obvious errors. Same tool, three genuinely different depths. | three terminal runs side by side, checklists of visibly different lengths |
| B07 | **3 ONE FLAG** | One flag — this only replaces "looks right" if every step is genuinely checkable. A step that just says "seems plausible" has quietly turned back into the exact habit it was built to replace. | THE FLAG — a checklist step reading "seems plausible ✓", cracking open to reveal nothing was actually checked |
| B08 | **3 mechanism + 5 both directions — ANCHOR PAYOFF** | Add a `--log` flag, and running the citation-at-strict case again writes out a markdown file — output type, risk level, timestamp, and each step with a checkbox, including open the source. That's the record, not just the answer. But finishing every checkbox doesn't prove the output was fully correct — the matrix catches known risks, not everything. And one failed step doesn't automatically mean it's wrong either — it means it needs a closer look. | THE ANCHOR RETURNS — the citation card's checklist, now logged with timestamp and checkboxes; beneath it, two dimmed captions: "ALL CHECKS PASSED ≠ FULLY CORRECT" / "ONE FAILED STEP ≠ WRONG" |
| **BCRY** | **6 carry-out** | Looks right isn't a review. A review is a checklist somebody can point to afterward. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. [reads prompt aloud] … Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Reading Isn't Reviewing. Liam, in for Bear. | OutroCTA, Humanitarians AI skin |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B04 |
| Wrong guess surfaced *and falsified by a case* | B02 states the read; B03 falsifies it with the fabricated-citation case — a clean read cannot catch a source that doesn't exist |
| One anchor, planted early, paid off late | B03 (the citation-at-strict card) → B08 (the same card, now logged and returned) |
| Exactly one inference flag | **B07** — the checklist only works if its steps stay genuinely checkable; this is the one place the reel notes a real edge that could undercut the fix |
| Both failure directions | B08 — what a completed checklist proves (the known risks for that tier were checked) vs. does not prove (the output is fully correct); what a failed step does not prove (that the output is wrong, rather than needing a closer look) |
| No design judgment | Beats describe why a checklist is or isn't sufficient evidence; none rules on whether any specific tool or model was built badly |

## Deliberately not claimed

- **Not "a completed checklist proves the output is correct."** B08's first direction
  bounds this: the matrix catches known risk patterns for that output type and tier,
  not every possible error.
- **Not "a failed checklist step proves the output is wrong."** B08's second direction
  bounds this: a failed step means a closer human look, not an automatic verdict.
- **No accusation of any specific model** producing worse citations, numbers, or
  charts than any other — the fabricated-citation case is a generic illustration of why
  reading cannot substitute for opening the source.

## Handoff prompt (BHTF, read aloud then discussed)

> "I want to build a risk-tiered verification checklist for my own AI workflow —
> different verification depths matched to different levels of output risk. Help me
> design three tiers, list three to five concrete checkable steps for each output type
> at each tier, and flag any step that isn't specific enough to actually check."

Why it's worth running: the "genuinely checkable" requirement only feels real once
it's applied to your own workflow. Naming your output types, picking three tiers, and
writing steps concrete enough to fail the "seems plausible" test takes a few minutes
and turns an abstract rule into a checklist you can actually use.

---
**GATE P — signed:** ______________________  (human)
