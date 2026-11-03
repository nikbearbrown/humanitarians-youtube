# Claude, Diligence Issue Extraction. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-diligence-issue-extraction`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first (CARRY-OUT.md).*

**Cold open:** BrutalistHesitantWriter (Remotion, free/local). **Narrator:** Liam, Kokoro `am_onyx`.
**Channel skin:** Humanitarians AI — outro via `OutroSeries`/`OutroCTA`, handle `@HumanitariansAI`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone wondered: can Claude decide which contract issues kill a deal? Not quite — it screens the documents against a fixed issue list and reports what it finds. Here's what actually happens when you run it." | writer types "Can Claude DECIDE which issues kill this deal?", hesitates on DECIDE, corrects to "flag" — lands "Can Claude flag which issues kill this deal?" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is diligence-issue-extraction. The SKILL.md file holds the full instruction set in plain language — no hidden logic. Claude reads it, then acts. The file is the program. | folder tree reveal: one file, SKILL.md, 12k |
| B02 | pipeline | The pipeline sits in the Steps section. Claude reads each step in order, then runs it. Linear — no branching unless a step says so. | YOUR REQUEST → Read SKILL.md → Execute → ISSUES REPORT |
| B03 | 3 mechanism | The constraint is specific. Read each document against the categories the file specifies — things like change-of-control clauses, missing consents, expired licenses — and flag anything that matches. Stay inside that list, and the issues report holds its shape every time. | heading card: "The interesting constraint." + full checklist statement |
| **BCRY** | **6 carry-out** | Same documents in, same issues report out, every time. Deciding which issues actually kill the deal is still yours. | the sentence, alone, serif, large — WantQuote |
| BHTF | your turn handoff | Your turn. Here's the prompt — read it with me. I'm reviewing a batch of vendor contracts before a deal closes, and I need every issue flagged — missing consents, change-of-control clauses, anything past its renewal date. Read the diligence-issue-extraction skill, tell me exactly what you need from me before you run any check, then screen these contracts and tell me what it flags and why. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro series | Claude, Diligence Issue Extraction. | OutroSeries — title restate |
| BCTA | outro cta | …Liam, in for Bear. | OutroCTA — handle @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | B03 states the constraint (checklist categories, flag matches) and stops; the source's "Teardown moment" framing and "what it gets right / what it bites" verdict language are both dropped |
| Stakes → mechanism | B00 states the misconception (deciding what kills the deal vs. a screening pass); B01–B02 explain the file and pipeline before B03's constraint |
| Carry-out | BCRY compresses the distinction (repeatable extraction vs. who judges materiality), not the topic |
| Host handoff | B00 hands narration to Liam implicitly via "here's what actually happens"; no puppet host in hai-simple |
| Hedge words | none used outside any flag — every claim is a confirmed, present-tense description of the skill's own spec |

## Deliberately not claimed

- **Not "Claude decides which issues kill the deal."** The naive framing in B00 ("decide
  which contract issues kill a deal") is stated and corrected within the same beat — the
  skill screens against a checklist, it never renders a judgment about deal risk.
- **Not "the report is the final answer."** B03 and BCRY both stay inside what a
  diligence-extraction skill's own SKILL.md would specify: categories to check, criteria
  for a match. Neither beat claims the report is a substitute for counsel's judgment —
  that decision is stated as the reader's job, not implied to be handled.
- **No verdict on the skill's design.** The source's Teardown register judged the skill
  ("what it gets right," "what it bites"); this Plain redo describes the same constraint
  without ruling on whether it was well designed.
- **No invented specifics.** The source's narration carried unfilled `>` placeholders at
  every skill-specific fact, and its `source_skill` path does not exist on this machine
  (see QUESTION.md). The document-screening / issues-report account here is a generic,
  defensible description of what any diligence issue-extraction skill does — no specific
  document type, database, or deal outcome is asserted.

## Handoff prompt (BHTF, read aloud)

> "I'm reviewing a batch of vendor contracts before a deal closes, and I need every issue
> flagged — missing consents, change-of-control clauses, anything past its renewal date.
> Read the diligence-issue-extraction skill, tell me exactly what you need from me before
> you run any check, then screen these contracts and tell me what it flags and why."

Why it's worth running: it forces Claude to name its own input requirements before it
screens anything — the same "explain first" clause the source reel's own handoff used to
surface the skill's real constraint logic.

---
**GATE P — signed:** ______________________  (human)
