# Claude, Leave Tracker. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-leave-tracker`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first (CARRY-OUT.md).*

**Cold open:** BrutalistHesitantWriter (Remotion, free/local). **Narrator:** Liam, Kokoro `am_onyx`.
**Channel skin:** Humanitarians AI — outro via `OutroSeries`/`OutroCTA`, handle `@HumanitariansAI`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone wondered: can Claude approve my leave request? Not quite — it checks the request against a fixed policy and reports what it finds. Here's what actually happens when you run it." | writer types "Can Claude APPROVE my leave request?", hesitates on APPROVE, corrects to "check" — lands "Can Claude check my leave request?" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is leave-tracker. The SKILL.md file holds the full instruction set in plain language — no hidden logic. Claude reads it, then acts. The file is the program. | folder tree reveal: one file, SKILL.md, 1k |
| B02 | pipeline | The pipeline sits in the Steps section. Claude reads each step in order, then runs it. Linear — no branching unless a step says so. | YOUR REQUEST → Read SKILL.md → Execute → LEAVE REPORT |
| B03 | 3 mechanism | The constraint is specific. Check the requested or logged absence against the accrual rules, eligibility windows, and blackout dates the file specifies, then flag anything that doesn't fit. Stay inside that policy, and the report holds its shape every time. | heading card: "The interesting constraint." + full policy-check statement |
| **BCRY** | **6 carry-out** | Same policy in, same leave report out, every time. Approving the leave is still yours. | the sentence, alone, serif, large — WantQuote |
| BHTF | your turn handoff | Your turn. Here's the prompt — read it with me. I want to check my remaining leave balance under my company's PTO policy. Read the leave-tracker skill, tell me exactly what you need from me before you run any check, then tell me what it flags and why. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro series | Claude, Leave Tracker. | OutroSeries — title restate |
| BCTA | outro cta | …Liam, in for Bear. | OutroCTA — handle @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | B03 states the constraint (accrual rules, eligibility windows, blackout dates, flag mismatches) and stops; the source's "Teardown moment" framing and "what it gets right / what it bites" verdict language are both dropped |
| Stakes → mechanism | B00 states the misconception (approval vs. a policy check); B01–B02 explain the file and pipeline before B03's constraint |
| Carry-out | BCRY compresses the distinction (repeatable policy check vs. who approves), not the topic |
| Host handoff | B00 hands narration to Liam implicitly via "here's what actually happens"; no puppet host in hai-simple |
| Hedge words | none used outside any flag — every claim is a confirmed, present-tense description of the skill's own spec |

## Deliberately not claimed

- **Not "Claude approves the leave."** The naive framing in B00 ("approve my leave
  request") is stated and corrected within the same beat — the skill checks against a
  policy, it never issues an approval or denial.
- **Not "the report is the final answer."** B03 and BCRY both stay inside what a
  leave-tracker skill's own SKILL.md would specify: accrual rules, eligibility windows,
  blackout dates. Neither beat claims the report substitutes for a manager's or HR's
  sign-off — that decision is stated as the reader's job, not implied to be handled.
- **No verdict on the skill's design.** The source's Teardown register judged the skill
  ("what it gets right," "what it bites"); this Plain redo describes the same constraint
  without ruling on whether it was well designed.
- **No invented specifics.** The source's narration carried unfilled `>` placeholders at
  every skill-specific fact, and its `source_skill` path does not exist on this machine
  (see QUESTION.md). No specific jurisdiction's leave law, HRIS integration, or leave
  type is asserted — the policy-check / leave-report account here is a generic,
  defensible description of what any leave-tracker skill does.

## Handoff prompt (BHTF, read aloud)

> "I want to check my remaining leave balance under my company's PTO policy. Read the
> leave-tracker skill, tell me exactly what you need from me before you run any check,
> then tell me what it flags and why."

Why it's worth running: it forces Claude to name its own input requirements before it
checks anything — the same "explain first" clause the source reel's own handoff used to
surface the skill's real constraint logic.

---
**GATE P — signed:** ______________________  (human)
