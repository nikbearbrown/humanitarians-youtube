# Claude, Lead Triage. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-lead-triage`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first (CARRY-OUT.md).*

**Cold open:** BrutalistHesitantWriter (Remotion, free/local). **Narrator:** Liam, Kokoro `am_onyx`.
**Channel skin:** Humanitarians AI — outro via `OutroSeries`/`OutroCTA`, handle `@HumanitariansAI`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone typed 'judge' — as if Claude decides which leads are worth chasing. A skill called lead-triage runs one fixed routine per request — same input, same result. Does Claude sort my leads by itself?" | writer types "Does Claude\nJUDGE my leads\nby itself?", hesitates on JUDGE, corrects to "sort" — lands "Does Claude sort my leads by itself?" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is lead-triage. It holds two items — a SKILL.md file and a reference folder. The SKILL.md is the full instruction set, in plain language — no hidden logic. Claude reads it, then acts. The file is the program. | folder tree reveal: SKILL.md (3k) + reference/ |
| B02 | pipeline | The pipeline sits in the Steps section. Claude reads each step in order, then runs it. Linear — no branching unless a step says so. | YOUR REQUEST → Read SKILL.md → Execute → RESULT |
| B03 | 3 mechanism | Here's the part worth knowing. lead-triage is a specification written as an instruction set, not an autonomous verdict. It runs once, when you ask, and does exactly what the file says — nothing runs in the background on its own. Ask the same thing twice, and you get the same result both times; ask for something the file doesn't cover, and the skill has nothing to say about it. | heading card: "The interesting constraint." + bounded-spec statement |
| **BCRY** | **6 carry-out** | "Triage" here isn't Claude judging your leads on its own. It's one spec-bound sort — the same steps, the same result, every time you ask. | the sentence, alone, serif, large — WantQuote |
| BHTF | your turn handoff | Your turn. Here's the prompt — read it with me. Read the lead-triage skill in this folder. Before you run it, tell me exactly which steps it will execute, in order, and tell me plainly if anything I ask falls outside what the file covers. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro series | Claude, Lead Triage. | OutroSeries — title restate |
| BCTA | outro cta | …Liam, in for Bear. | OutroCTA — handle @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | B03 states the bounded-spec scope and stops; the source's "Teardown moment," "what it gets right / what it bites," and "Verdict" framing are all dropped |
| Stakes → mechanism | B00 states the misconception (lead-triage = Claude autonomously judging leads); B01–B02 explain the file and pipeline before B03's scope statement |
| Carry-out | BCRY compresses the distinction that matters (bounded, request-triggered, repeatable — not an autonomous verdict) rather than summarizing the topic |
| Host handoff | B00 hands narration to Liam implicitly; no puppet host in hai-simple |
| Hedge words | none used — every claim is a confirmed, present-tense description of how lead-triage and Claude Skills generally work |

## Deliberately not claimed

- **Not "Claude decides which leads matter on its own."** The naive framing in B00
  ("Does Claude JUDGE my leads by itself?") is stated and corrected within the same
  beat — the skill runs once per request, not as an ongoing autonomous judgment.
- **No claim about what lead-triage specifically scores, ranks, or routes a lead by.**
  The source's own placeholder for that description (`>`) is empty in *every* beat,
  including B00 — there is nothing to recover, and the actual `SKILL.md` this source
  points at does not exist on this machine. Inventing a scoring rubric, a field list, or
  a routing destination would be fabrication; this reel states only the anatomy
  (SKILL.md + reference/, 2 files), pipeline (Steps section, linear), and scope
  guarantee (bounded spec, repeatable, silent outside the file) that the source's
  readable text actually supports. Full detail in QUESTION.md.
- **No verdict on the skill's design.** The source's Teardown register judged the skill
  ("what it gets right," "what it bites," "know the limit"); this Plain redo describes
  the same bounded-spec scope without ruling on whether it was well designed.

## Handoff prompt (BHTF, read aloud)

> "Read the lead-triage skill in this folder. Before you run it, tell me exactly which
> steps it will execute, in order, and tell me plainly if anything I ask falls outside
> what the file covers."

Why it's worth running: it forces Claude to state its own steps and boundary before
acting — the same "explain first" clause the source reel's own handoff used to surface a
skill's real constraint logic.

---
**GATE P — signed:** ______________________  (human)
