# Claude, Invention Intake. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-invention-intake`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first (CARRY-OUT.md).*
*Facts pulled from the REAL source SKILL.md, found on this machine (see QUESTION.md) —
not a generic reconstruction.*

**Cold open:** BrutalistHesitantWriter (Remotion, free/local). **Narrator:** Liam, Kokoro `am_onyx`.
**Channel skin:** Humanitarians AI — outro via `OutroSeries`/`OutroCTA`, handle `@HumanitariansAI`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone wondered if Claude could patent their invention outright. Not quite — it never calls an idea patentable. What it does is screen the disclosure before you reach a lawyer." | writer types "Can Claude PATENT my invention for me?", hesitates on PATENT, corrects to "screen" — lands "Can Claude screen my invention for me?" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is invention-intake. The SKILL.md file holds the full instruction set in plain language — no hidden logic. Claude reads it, then acts. The file is the program. | folder tree reveal: one file, SKILL.md, 22k |
| B02 | pipeline | The pipeline runs six screens in order — novelty, obviousness, eligibility, bar dates, detectability, strategic value — then returns one of three verdicts. | YOUR REQUEST → Intake → Six screens → BOTTOM-LINE VERDICT |
| B03 | 3 mechanism | The constraint is specific. Run all six screens, then hand back pursue, investigate, or decline. It never says patentable — that word is reserved for a prior-art search and a registered attorney this skill doesn't provide. | heading card: "The interesting constraint." + full six-screens-to-verdict statement |
| **BCRY** | **6 carry-out** | Six screens in, one verdict out — pursue, investigate, or decline. It never calls anything patentable; that call still needs a prior-art search and a lawyer this skill doesn't run. | the sentence, alone, serif, large — WantQuote |
| BHTF | your turn handoff | Your turn. Here's the prompt — read it with me. I built a new caching algorithm that picks what to evict using a small learned model instead of a fixed rule. It's an internal prototype, not yet disclosed. Read the invention-intake skill, tell me exactly what you need from me before you screen it, then run all six checks and give me the bottom-line verdict. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro series | Claude, Invention Intake. | OutroSeries — title restate |
| BCTA | outro cta | …Liam, in for Bear. | OutroCTA — handle @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | B03 states the constraint (six screens, three-word verdict, no "patentable") and stops; the source's "Teardown moment" framing and verdict-artifact "what it gets right / what it bites" language are both dropped |
| Stakes → mechanism | B00 states the misconception (Claude patents it vs. screens it); B01–B02 explain the file and pipeline before B03's constraint |
| Carry-out | BCRY compresses the distinction (a bounded triage screen vs. an actual patentability opinion), not the topic |
| Host handoff | B00 hands narration to Liam implicitly via "what it does is..."; no puppet host in hai-simple |
| Hedge words | none used outside any flag — every claim is a confirmed, present-tense description of the skill's own written behavior |

## Deliberately not claimed

- **Not "Claude decides if it's patentable."** The naive framing in B00 ("patent their
  invention outright") is stated and corrected within the same beat — the real
  SKILL.md's own guardrail is "Never say patentable," verbatim.
- **Not "the screen replaces a prior-art search."** B03 and BCRY both state, per the
  file, that a PURSUE verdict schedules a prior-art search and attorney review — the
  screen is upstream of that, not a substitute for it.
- **No verdict on the skill's design.** The source's Teardown register judged the
  skill ("what it gets right," "what it bites"); this Plain redo describes the same
  constraint without ruling on whether it was well designed.
- **No invented specifics.** Unlike this family's usual source-gap redos, the real
  SKILL.md was found on this machine (see QUESTION.md) — every fact above (six named
  screens, the three-word verdict, the "never patentable" guardrail, the file size,
  the worked cache-eviction example) is read directly from that file, not
  reconstructed.

## Handoff prompt (BHTF, read aloud)

> "I built a new caching algorithm that picks what to evict using a small learned
> model instead of a fixed rule. It's an internal prototype, not yet disclosed. Read
> the invention-intake skill, tell me exactly what you need from me before you screen
> it, then run all six checks and give me the bottom-line verdict."

Why it's worth running: it's the source SKILL.md's own worked example, and it forces
Claude to name its intake requirements (what, problem, differences, inventors,
disclosure, status, tech area) before it screens anything — the same "explain first"
pattern the family's other handoffs use to surface each skill's real constraint logic.

---
**GATE P — signed:** ______________________  (human)
