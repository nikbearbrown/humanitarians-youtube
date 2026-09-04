# Claude, Audit Xls. — Does Auditing Mean Fixing? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-audit-xls`, Teardown -> Plain).
Register: **Plain**. 7 beats.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion (no puppet host in hai-simple).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone asks if Claude will just fix a broken spreadsheet. It won't — audit-xls checks the model and reports what's wrong. Liam takes you through what it actually does." | writer types "Can Claude / just fix / my spreadsheet?", hesitates on "fix", corrects to "audit" |
| B01 | 1 stakes / 2 wrong guess, falsified | The natural guess is that asking Claude to audit a spreadsheet means it finds the errors and fixes them while it's in there. But the skill doesn't work that way. It audits a spreadsheet for formula accuracy, errors, and common mistakes, and reports what it finds — cited by cell. Give it a sheet with a formula you already know is broken, and check the sheet again after: the formula is untouched. What changed is the report, not the spreadsheet. | a "fix it" hand reaching for a cell, struck; a report card with cell citations, lit |
| B02 | 3 mechanism / **4 anchor planted** | What it actually checks, and in what order: BS balance first — if the balance sheet doesn't balance, everything downstream is suspect. Watch the anchor: a balance sheet off by a fixed amount. It's checked first, the mismatch is found, the affected cells are cited, and a finding is reported. Then it stops — nothing is rewritten. | THE ANCHOR — four cards (SCOPE SET / BS CHECKED FIRST / MISMATCH FOUND / CITED, REPORTED), a token traveling through all four, halting at the last one |
| B03 | **4 anchor payoff** / 5 both directions | So back to that balance sheet: reported, cited, waiting for you to look. But a clean BS-balance pass doesn't mean the whole model in scope is error-free — it only clears that one check; formula errors elsewhere are checked separately. And a BS-imbalance flag doesn't mean every downstream number is individually wrong — it means they're unverified until the imbalance is resolved, not confirmed incorrect. Either way, nothing in the sheet has been changed. | THE ANCHOR RETURNS, cited and reported; splits into "balanced ≠ error-free" and "suspect ≠ wrong" |
| **BCRY** | **6 carry-out** | audit-xls checks the balance sheet first, then flags every suspect formula by cell — but it never rewrites one. Finding the problem is Claude's job here; fixing it stays yours. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Give Claude a spreadsheet with one formula you already know is wrong, and ask it to run the audit-xls skill: check balance first, then scan for formula errors, and report what it finds by cell. Then open the sheet afterward and check whether the formula itself changed. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | Claude, Audit Xls. Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the wrong guess before B02 opens the mechanism |
| Wrong guess surfaced *and falsified by a case* | B01 states "finds the errors and fixes them"; falsified by "check the sheet again after — the formula is untouched" |
| Exactly one inference flag | none needed — every claim here is stated directly from the source sheet's own facts (audit scope, BS-balance-first ordering) or is a direct reading of what "audit" (vs. "fix") means as described |
| One anchor, planted early, paid off late | B02 -> B03 (a balance sheet off by a fixed amount: checked first → mismatch found → cited → reported → stopped) |
| Both failure directions | B03: "a clean pass isn't the same as error-free elsewhere" / "a suspect flag isn't the same as confirmed wrong" |
| No design judgment | B01/B02/B03 describe what the skill checks and in what order, and where it stops; no verdict on whether checking BS-balance first was a good design choice |

## Deliberately not claimed

- **Not that the skill is "wrong" or poorly designed.** Teardown's B03 in the
  source framed the BS-balance-first ordering as "the interesting
  constraint... a deliberate trade-off baked into the instruction set";
  Plain keeps only the mechanism (checked first, because downstream
  becomes suspect if it's off) and its two failure directions, no verdict
  on the design choice itself.
- **Not a claim about any specific dollar amounts, cell references, or
  UI.** The anchor (a balance sheet off by a fixed amount) is a standard,
  generic example — no invented screen, spreadsheet software, or output
  format.
- **Not "the skill fixes what it finds."** The whole point of the
  wrong-guess/falsification pair (B01) is the opposite: it reports and
  cites; the formula in the sheet is unchanged unless a person changes it.

## Handoff prompt (BHTF, read aloud)

> "Give Claude a spreadsheet with one formula you already know is wrong,
> and ask it to run the audit-xls skill: check balance first, then scan
> for formula errors, and report what it finds by cell. Then open the
> sheet afterward and check whether the formula itself changed."

Why it's worth running: checking the sheet after is the fastest way to see
that the skill reports and cites, instead of repairing — rather than just
trusting that it does.

---
**GATE P — signed:** ______________________ (human)
