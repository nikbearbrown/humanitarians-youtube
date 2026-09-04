# Claude, Contracts. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-contracts`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first (CARRY-OUT.md).*

**Cold open:** BrutalistHesitantWriter (Remotion, free/local). **Narrator:** Liam, Kokoro `am_onyx`.
**Channel skin:** Humanitarians AI — outro via `OutroSeries`/`OutroCTA`, handle `@HumanitariansAI`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone wondered if Claude would approve their contract before signing. Not quite — it answers questions across the contract files and cites where each answer comes from. Here's what happens when you run it." | writer types "Will Claude APPROVE my contract before I sign it?", hesitates on APPROVE, corrects to "search" — lands "Will Claude search my contract before I sign it?" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is contracts. The SKILL.md file holds the full instruction set in plain language — no hidden logic. Claude reads it, then acts. The file is the program. | folder tree reveal: README.md 12k, SKILL.md 40k (the instruction set), sweep.mjs 17k |
| B02 | pipeline | The pipeline sits in the Steps section. Claude reads each step in order, then runs it. Linear — no branching unless a step says so. | YOUR QUESTION → Read SKILL.md → Execute → CITED ANSWER |
| B03 | 3 mechanism | The constraint is specific: answer a question across a corpus of contract documents, and cite exactly where each answer comes from. Stay inside that scope, and the citations hold their shape every time. | heading card: "The interesting constraint." + the skill's own job statement |
| **BCRY** | **6 carry-out** | Same corpus in, same cited answers out, every time — deciding whether to sign is still yours. | the sentence, alone, serif, large — WantQuote |
| BHTF | your turn handoff | Your turn. Here's the prompt — read it with me. I have a folder of contract files and a question about them. Read the contracts skill, tell me exactly what you need from me before you run anything, then answer my question across the files and cite exactly where each answer comes from. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro series | Claude, Contracts. | OutroSeries — title restate |
| BCTA | outro cta | …Liam, in for Bear. | OutroCTA — handle @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | B03 states the constraint (a corpus, a question, a cited answer) and stops; the source's "Teardown moment" framing and "what it gets right / what it bites" verdict language are both dropped |
| Stakes → mechanism | B00 states the misconception (a legal approve/reject verdict vs. cited search); B01–B02 explain the file and pipeline before B03's constraint |
| Carry-out | BCRY compresses the distinction (repeatable cited retrieval vs. who decides to sign), not the topic |
| Host handoff | B00 hands narration to Liam implicitly via "here's what happens when you run it"; no puppet host in hai-simple |
| Hedge words | none used outside any flag — every claim is a confirmed, present-tense description of the skill's own spec (real facts, not reconstructed — see QUESTION.md) |

## Deliberately not claimed

- **Not "Claude approves the contract."** The naive framing in B00 ("approve
  their contract before signing") is stated and corrected within the same
  beat — the skill answers questions with citations, it never issues a
  sign/don't-sign verdict.
- **Not "the citations are legal advice."** B03 and BCRY both stay inside
  what the source `SKILL.md` actually specifies: answer a question across
  the corpus, cite the source. Neither beat claims the answer is a
  substitute for a lawyer's read — that decision stays the reader's, stated
  plainly rather than implied.
- **No verdict on the skill's design.** The source's Teardown register judged
  the skill ("what it gets right," "what it bites"); this Plain redo
  describes the same constraint without ruling on whether it was well
  designed.
- **No invented specifics.** Unlike some `redo` siblings whose source carried
  unfilled template placeholders, this source's facts were already real and
  complete (skill name, job statement, scope, the 3-file anatomy, corpus
  constraint) — every fact here is carried over verbatim from the delivered
  source sheet, not reconstructed.

## Handoff prompt (BHTF, read aloud)

> "I have a folder of contract files and a question about them. Read the
> contracts skill, tell me exactly what you need from me before you run
> anything, then answer my question across the files and cite exactly where
> each answer comes from."

Why it's worth running: it forces Claude to name its own input requirements
before it answers anything — the same "explain first" clause the source
reel's own handoff used to surface the skill's real constraint logic.

## Beat-count note (redo)

Source is 7 beats (B00 cold open, B01 anatomy, B02 pipeline, B03 design
tell, BVDT verdict, BHTF handoff, BOUT outro). hai-simple's spine keeps that
shape in substance: B00 → B01 anatomy → B02 pipeline → B03 mechanism →
BVDT/BCRY carry-out → BHTF handoff → BOUT outro, plus the fixed hai-simple
outro split (`ClaudeTitleOutro` → `OutroSeries` + `OutroCTA`), 7 → 8 beats —
same restructuring precedent as every sibling in this family
(`claude-for-legal--claude-liam-clearance` and others).

---
**GATE P — signed:** ______________________  (human)
