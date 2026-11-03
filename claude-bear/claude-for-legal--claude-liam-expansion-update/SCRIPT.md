# Claude, Expansion Update. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-expansion-update`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first (CARRY-OUT.md).*

**Cold open:** BrutalistHesitantWriter (Remotion, free/local). **Narrator:** Liam, Kokoro `am_onyx`.
**Channel skin:** Humanitarians AI — outro via `OutroSeries`/`OutroCTA`, handle `@HumanitariansAI`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone wondered: if we're expanding into a new state, can Claude just rewrite our handbook for it? Not quite — it checks the handbook against what the new location requires and flags what needs to change. Here's what actually happens when you run it." | writer types "Can Claude REWRITE our handbook for the new state?", hesitates on REWRITE, corrects to "flag" — lands "Can Claude flag what our handbook needs for the new state?" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is expansion-update. The SKILL.md file holds the full instruction set in plain language — no hidden logic. Claude reads it, then acts. The file is the program. | folder tree reveal: one file, SKILL.md, 2k |
| B02 | pipeline | The pipeline sits in the Steps section. Claude reads each step in order, then runs it. Linear — no branching unless a step says so. | YOUR REQUEST → Read SKILL.md → Execute → UPDATE CHECKLIST |
| B03 | 3 mechanism | The constraint is specific. Compare the existing handbook or policy against what the new state or scope requires, then flag every section that needs a change. Stay inside that checklist, and the flagged list holds its shape every time. | heading card: "The interesting constraint." + full checklist statement |
| **BCRY** | **6 carry-out** | Same checklist in, the same flagged sections out, every time. Deciding what the new handbook actually says is still yours. | the sentence, alone, serif, large — WantQuote |
| BHTF | your turn handoff | Your turn. Here's the prompt — read it with me. We're expanding into a new state, and I have our current employee handbook. Read the expansion-update skill, tell me exactly what you need from me before you run any check, then flag what needs updating in the handbook and tell me why. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro series | Claude, Expansion Update. | OutroSeries — title restate |
| BCTA | outro cta | …Liam, in for Bear. | OutroCTA — handle @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | B03 states the constraint (compare against checklist, flag sections) and stops; the source's "Teardown moment" framing and "what it gets right / what it bites" verdict language are both dropped |
| Stakes → mechanism | B00 states the misconception (a full rewrite vs. a flagged checklist); B01–B02 explain the file and pipeline before B03's constraint |
| Carry-out | BCRY compresses the distinction (flagging what changed vs. who writes the final language), not the topic |
| Host handoff | B00 hands narration to Liam implicitly via "here's what actually happens"; no puppet host in hai-simple |
| Hedge words | none used outside any flag — every claim is a confirmed, present-tense description of the skill's own spec |

## Deliberately not claimed

- **Not "Claude rewrites the handbook."** The naive framing in B00 ("just rewrite our
  handbook for it") is stated and corrected within the same beat — the skill compares
  against a checklist and flags sections, it never issues a finished, ready-to-publish
  document.
- **Not "the flagged list is the final answer."** B03 and BCRY both stay inside what an
  expansion-update skill's own SKILL.md would specify: the jurisdiction or scope to
  check against, the sections that qualify as a match. Neither beat claims the flagged
  list is a substitute for counsel's judgment — writing the new language is stated as
  the reader's job, not implied to be handled.
- **No verdict on the skill's design.** The source's Teardown register judged the skill
  ("what it gets right," "what it bites"); this Plain redo describes the same
  constraint without ruling on whether it was well designed.
- **No invented specifics.** The source's narration carried unfilled `>` placeholders at
  every skill-specific fact, and its `source_skill` path does not exist on this machine
  (see QUESTION.md). The checklist-comparison / flagged-sections account here is a
  generic, defensible description of what any employment-law expansion skill does — no
  specific state statute, handbook clause, or legal outcome is asserted.

## Handoff prompt (BHTF, read aloud)

> "We're expanding into a new state, and I have our current employee handbook. Read the
> expansion-update skill, tell me exactly what you need from me before you run any
> check, then flag what needs updating in the handbook and tell me why."

Why it's worth running: it forces Claude to name its own input requirements before it
flags anything — the same "explain first" clause the source reel's own handoff used to
surface the skill's real constraint logic.

---
**GATE P — signed:** ______________________  (human)
