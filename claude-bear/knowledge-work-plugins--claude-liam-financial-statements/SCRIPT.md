# Claude, Financial Statements. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 2:10.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes Claude uses its own judgment to decide what counts as a material variance. It doesn't. It checks numbers against rules written in a file, every time. What's in that file?" | BrutalistHesitantWriter — types "Claude decides what's a material variance. Right?", corrects "decides" → "checks" |
| B01 | 1 stakes / 2 wrong guess, falsified | Open the financial-statements folder and there's no separate module for accounting judgment. One file, SKILL.md, spells out the job: build the income statement, balance sheet, and cash flow statement, compare each period to the last, and flag variances that cross a threshold the file itself sets. Claude reads that instruction and follows it — nothing is left to discretion. | a folder opens onto one file, SKILL.md, listing its job in plain language; no second "judgment" module anywhere |
| B02 | 3 mechanism / **4 anchor planted** | The pipeline lives in the Steps section, and Claude works through it top to bottom — linear, no branching unless a step says so. Ask for financial statements covering the first quarter, and it builds the income statement, balance sheet, and cash flow, lines each one up against the prior period, and flags what crosses the threshold — the same steps, every single time. | THE ANCHOR — a "financial statements · Q1" request goes in, ordered steps light up in sequence, an output card (three statements + flags) comes out |
| B03 | **4 anchor payoff / 5 both directions** | Ask for that same first-quarter statement again, and the flags come back identical — not because Claude re-judged the numbers, but because the same steps ran a second time. That cuts both ways: identical flags on identical input isn't proof Claude understood the business, it only proves the fixed steps repeated. And a different flag showing up next quarter doesn't mean the rule changed either — the same steps just ran against new numbers. | THE ANCHOR RETURNS — the same Q1 request submitted twice, two identical output cards; beside it, a Q2 request producing a different card from the same steps |
| **BCRY** | **6 carry-out** | Flagging a variance isn't Claude's judgment call — it checks the numbers against a rule someone already wrote, the same way every single time. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Open the financial-statements skill folder. Before you run anything, read me the SKILL.md and tell me, in your own words, what makes a variance count as material. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Financial Statements. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the folder's actual contents as an observable fact; the Steps mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (Claude decides materiality by judgment); B01 falsifies it with a case — the folder holds one file, SKILL.md, that spells out the job and the threshold in plain language, no separate judgment module anywhere |
| Exactly one inference flag | none needed — every claim is the source's own confirmed statement about the skill's documented job and how Agent Skills execute; the one unconfirmed thing (the exact threshold/output format) is never asserted, so there is nothing to flag (see CARRY-OUT.md) |
| One anchor, planted early, paid off late | B02 → B03 (the "financial statements · Q1" request, submitted, walked through the same steps, run twice, then Q2) |
| Both directions | B03 — identical flags on identical input isn't proof of understanding (it's the same fixed steps repeating); a different flag on different input isn't proof the rule changed (same fixed steps, new numbers) |
| No design judgment | B03 states the determinism fact and its limits, never a verdict on whether the skill's design is good |

## Deliberately not claimed

- **Not the specific threshold, GAAP line items, or output layout.** The
  source confirms the skill's job (three statements, period comparison,
  variance analysis, GAAP presentation/period-end lookups) but never the
  exact numeric threshold for "material" or the precise output format. No
  other copy of `financial-statements`'s `SKILL.md` exists on this
  machine to recover that level of detail — this reel does not invent it.
- **Not a verdict on the design.** The source's B03/BVDT framed the same
  facts as "what it gets right" / "what it bites" and a scored verdict —
  Teardown language. Plain keeps the facts (folder mechanism, the
  documented job, determinism) but states them without judging whether
  the design is good.
- **Not that every skill's judgment calls are this simple in practice.**
  Only that the mechanism itself — read the file, run the steps in order,
  check against a written rule, same input same output — is what every
  Agent Skill guarantees.

## Handoff prompt (BHTF, read aloud)

> "Open the financial-statements skill folder. Before you run anything,
> read me the SKILL.md and tell me, in your own words, what makes a
> variance count as material."

Why it's worth running: it forces Claude to surface the actual rule in
its own words before acting on it — the same explain-first habit that
turns "the AI decided this was material" into an auditable, written
threshold.

---
**GATE P — signed:** ______________________  (human)
