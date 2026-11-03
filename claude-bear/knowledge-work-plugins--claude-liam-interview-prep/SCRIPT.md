# Claude, Interview Prep. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-interview-prep`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first (CARRY-OUT.md).*

**Cold open:** BrutalistHesitantWriter (Remotion, free/local). **Narrator:** Liam, Kokoro `am_onyx`.
**Channel skin:** Humanitarians AI — outro via `OutroSeries`/`OutroCTA`, handle `@HumanitariansAI`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone typed 'conduct' — but Claude doesn't run the interview. There's a skill called interview-prep: it builds a structured plan and scorecard beforehand. Does Claude prep interviews for me? Let's look inside." | writer types "Does Claude\nCONDUCT\ninterviews\nfor me?", hesitates on CONDUCT, corrects to "prep" — lands "Does Claude prep interviews for me?" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is interview-prep. The SKILL.md file holds the full instruction set in plain language — no hidden logic. Claude reads it, then acts. The file is the program. | folder tree reveal: SKILL.md (1k) |
| B02 | pipeline | The pipeline sits in the Steps section. Claude reads each step in order, then runs it. Linear — no branching unless a step says so. | YOUR REQUEST → Read SKILL.md → Execute → INTERVIEW PLAN |
| B03 | 3 mechanism | The scope is specific. interview-prep builds a structured interview plan with competency-based questions and a scorecard. It runs on phrases like "interview plan for", "interview questions for", "how should we interview", "scorecard for", or any request to prepare for interviewing candidates. Stay inside that request, and the plan comes back the same way every time; ask for anything the file doesn't cover, and the skill has nothing to say about it. | heading card: "The interesting constraint." + scope statement |
| **BCRY** | **6 carry-out** | Claude doesn't interview the candidate. It preps the plan — same role in, same questions and scorecard out, every time. | the sentence, alone, serif, large — WantQuote |
| BHTF | your turn handoff | Your turn. Here's the prompt — read it with me. Read the interview-prep skill in this folder. Before you run it, tell me exactly what sections the plan will include. Then build me an interview plan for a role I name. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro series | Claude, Interview Prep. | OutroSeries — title restate |
| BCTA | outro cta | …Liam, in for Bear. | OutroCTA — handle @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | B03 states the scope (builds one interview plan, from a role, nothing outside the request) and stops; the source's "Teardown moment," "what it gets right / what it bites," and "Verdict" framing are all dropped |
| Stakes → mechanism | B00 states the misconception (interview-prep = Claude conducts the interview); B01–B02 explain the file and pipeline before B03's scope statement |
| Carry-out | BCRY compresses the distinction (preps, doesn't conduct) rather than summarizing the topic |
| Host handoff | B00 hands narration to Liam implicitly via "Let's look inside"; no puppet host in hai-simple |
| Hedge words | none used — every claim is a confirmed, present-tense description of how interview-prep and Claude Skills generally work |

## Deliberately not claimed

- **Not "Claude conducts or sits in on the interview."** The naive framing in B00
  ("Does Claude CONDUCT interviews for me?") is stated and corrected within the same
  beat — the skill assembles the plan, questions, and scorecard beforehand; it never
  conducts the interview itself.
- **Not a claim about specific competencies or scorecard fields.** The source names
  "competency-based questions and scorecards" without listing which competencies or
  fields; B03 repeats that generic description rather than inventing specifics the
  source never gave.
- **Recovered, not invented, trigger phrases.** The source truncates its own quoted
  trigger-phrase list in B03 ("Trigger with \"inte."); the complete phrase survives
  intact in the source's own B00 and is used here instead of guessing at the cut-off
  text (see QUESTION.md).
- **No verdict on the skill's design.** The source's Teardown register judged the
  skill ("what it gets right," "what it bites," "know the limit"); this Plain redo
  describes the same scope without ruling on whether it was well designed.

## Handoff prompt (BHTF, read aloud)

> "Read the interview-prep skill in this folder. Before you run it, tell me exactly
> what sections the plan will include. Then build me an interview plan for a role I
> name."

Why it's worth running: it forces Claude to state its own scope before acting — the
same "explain first" clause the source reel's own handoff used to surface a skill's
real constraint logic.

---
**GATE P — signed:** ______________________  (human)
