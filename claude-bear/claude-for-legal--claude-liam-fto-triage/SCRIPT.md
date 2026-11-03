# Claude, Fto Triage. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-fto-triage`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first (CARRY-OUT.md).*

**Cold open:** BrutalistHesitantWriter (Remotion, free/local). **Narrator:** Liam, Kokoro `am_onyx`.
**Channel skin:** Humanitarians AI — outro via `OutroSeries`/`OutroCTA`, handle `@HumanitariansAI`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone wondered: can Claude clear a new product of patent risk? Not quite — it screens a description against a fixed checklist and flags what needs a closer look. Here's what actually happens when you run it." | writer types "Can Claude CLEAR my product for patent risk?", hesitates on CLEAR, corrects to "triage" — lands "Can Claude triage my product for patent risk?" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is fto-triage. The SKILL.md file holds the full instruction set in plain language — no hidden logic. Claude reads it, then acts. The file is the program. | folder tree reveal: one file, SKILL.md, 25k |
| B02 | pipeline | The pipeline sits in the Steps section. Claude reads each step in order, then runs it. Linear — no branching unless a step says so. | YOUR REQUEST → Read SKILL.md → Execute → TRIAGE REPORT |
| B03 | 3 mechanism | The constraint is specific. Screen the described product or feature against the claim elements, keywords, and jurisdictions the file specifies, then flag anything that matches for a closer look. Stay inside that checklist, and the report holds its shape every time. | heading card: "The interesting constraint." + full checklist statement |
| **BCRY** | **6 carry-out** | Same checklist in, same triage report out, every time. Deciding whether you're actually clear to operate is still yours. | the sentence, alone, serif, large — WantQuote |
| BHTF | your turn handoff | Your turn. Here's the prompt — read it with me. I'm about to ship a new product feature, and I have a short description of what it does. Read the fto-triage skill, tell me exactly what you need from me before you run any check, then triage my feature description against your checklist and tell me what it flags and why. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro series | Claude, Fto Triage. | OutroSeries — title restate |
| BCTA | outro cta | …Liam, in for Bear. | OutroCTA — handle @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | B03 states the constraint (checklist, claim elements/keywords/jurisdictions, flag matches) and stops; the source's "Teardown moment" framing and "what it gets right / what it bites" verdict language are both dropped |
| Stakes → mechanism | B00 states the misconception (final FTO clearance vs. a triage pass); B01–B02 explain the file and pipeline before B03's constraint |
| Carry-out | BCRY compresses the distinction (repeatable triage vs. who signs off), not the topic |
| Host handoff | B00 hands narration to Liam implicitly via "here's what actually happens"; no puppet host in hai-simple |
| Hedge words | none used outside any flag — every claim is a confirmed, present-tense description of the skill's own spec |

## Deliberately not claimed

- **Not "Claude clears the product."** The naive framing in B00 ("clear a new product of
  patent risk") is stated and corrected within the same beat — the skill screens against
  a checklist, it never issues a freedom-to-operate legal opinion.
- **Not "the report is the final answer."** B03 and BCRY both stay inside what an
  FTO-triage skill's own SKILL.md would specify: claim elements, keywords, jurisdictions
  to check, criteria for a match. Neither beat claims the report is a substitute for
  counsel's judgment — that decision is stated as the reader's job, not implied to be
  handled.
- **No verdict on the skill's design.** The source's Teardown register judged the skill
  ("what it gets right," "what it bites"); this Plain redo describes the same constraint
  without ruling on whether it was well designed.
- **No invented specifics.** The source's narration carried unfilled `>` placeholders at
  every skill-specific fact, and its `source_skill` path does not exist on this machine
  (see QUESTION.md). The triage-checklist / triage-report account here is a generic,
  defensible description of what any FTO-triage skill does — no specific patent database,
  search tool, or legal outcome is asserted.

## Handoff prompt (BHTF, read aloud)

> "I'm about to ship a new product feature, and I have a short description of what it
> does. Read the fto-triage skill, tell me exactly what you need from me before you run
> any check, then triage my feature description against your checklist and tell me what
> it flags and why."

Why it's worth running: it forces Claude to name its own input requirements before it
triages anything — the same "explain first" clause the source reel's own handoff used to
surface the skill's real constraint logic.

---
**GATE P — signed:** ______________________  (human)
