# Claude, Deadlines. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-deadlines`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first (CARRY-OUT.md).*

**Cold open:** BrutalistHesitantWriter (Remotion, free/local). **Narrator:** Liam, Kokoro `am_onyx`.
**Channel skin:** Humanitarians AI — outro via `OutroSeries`/`OutroCTA`, handle `@HumanitariansAI`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone wondered: can Claude just track my legal deadlines for me? Not exactly — it computes them from a rule you give it, and reports what's due. Here's what actually happens when you run it." | writer types "Can Claude TRACK my deadlines?", hesitates on TRACK, corrects to "compute" — lands "Can Claude compute my deadlines?" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is deadlines. The SKILL.md file holds the full instruction set in plain language — no hidden logic. Claude reads it, then acts. The file is the program. | folder tree reveal: one file, SKILL.md, 10k |
| B02 | pipeline | The pipeline sits in the Steps section. Claude reads each step in order, then runs it. Linear — no branching unless a step says so. | YOUR REQUEST → Read SKILL.md → Execute → DEADLINE CALENDAR |
| B03 | 3 mechanism | The constraint is specific. Take a triggering date and the rule that governs it — a filing window, a response period, a limitations period — then compute the resulting date. Stay inside that rule, and the calendar holds its shape every time. | heading card: "The interesting constraint." + full computation statement |
| **BCRY** | **6 carry-out** | Same rule in, same calendar out, every time. Knowing which rule actually governs your matter is still yours. | the sentence, alone, serif, large — WantQuote |
| BHTF | your turn handoff | Your turn. Here's the prompt — read it with me. I have a triggering date and a deadline rule from my own matter. Read the deadlines skill, tell me exactly what you need from me before you compute anything, then work out the resulting date and show me the calculation. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro series | Claude, Deadlines. | OutroSeries — title restate |
| BCTA | outro cta | …Liam, in for Bear. | OutroCTA — handle @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | B03 states the constraint (triggering date, rule, computed date) and stops; the source's "Teardown moment" framing and "what it gets right / what it bites" verdict language are both dropped |
| Stakes → mechanism | B00 states the misconception (Claude tracks/knows your deadlines vs. it computes from a rule you supply); B01–B02 explain the file and pipeline before B03's constraint |
| Carry-out | BCRY compresses the distinction (repeatable computation vs. who supplies the governing rule), not the topic |
| Host handoff | B00 hands narration to Liam implicitly via "here's what actually happens"; no puppet host in hai-simple |
| Hedge words | none used outside any flag — every claim is a confirmed, present-tense description of the skill's own spec |

## Deliberately not claimed

- **Not "Claude tracks my deadlines."** The naive framing in B00 ("just track my legal
  deadlines for me") is stated and corrected within the same beat — the skill computes
  from a rule you supply, it never independently monitors or discovers your matter's
  deadlines.
- **Not "the calendar is the final answer."** B03 and BCRY both stay inside what a
  deadlines skill's own SKILL.md would specify: a triggering date, a stated rule, a
  computed result. Neither beat claims the calendar is a substitute for confirming which
  rule actually governs — that decision is stated as the reader's job, not implied to be
  handled.
- **No verdict on the skill's design.** The source's Teardown register judged the skill
  ("what it gets right," "what it bites"); this Plain redo describes the same constraint
  without ruling on whether it was well designed.
- **No invented specifics.** The source's narration carried unfilled `>` placeholders at
  every skill-specific fact, and its `source_skill` path does not exist on this machine
  (see QUESTION.md). The rule-in / calendar-out account here is a generic, defensible
  description of what any legal-deadlines skill does — no specific jurisdiction, court
  rule, or legal outcome is asserted.

## Handoff prompt (BHTF, read aloud)

> "I have a triggering date and a deadline rule from my own matter. Read the deadlines
> skill, tell me exactly what you need from me before you compute anything, then work
> out the resulting date and show me the calculation."

Why it's worth running: it forces Claude to name its own input requirements before it
computes anything — the same "explain first" clause the source reel's own handoff used
to surface the skill's real constraint logic.

---
**GATE P — signed:** ______________________  (human)
