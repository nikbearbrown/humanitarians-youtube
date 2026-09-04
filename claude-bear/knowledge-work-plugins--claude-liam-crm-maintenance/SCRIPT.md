# Claude, Crm Maintenance. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-crm-maintenance`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first (CARRY-OUT.md).*

**Cold open:** BrutalistHesitantWriter (Remotion, free/local). **Narrator:** Liam, Kokoro `am_onyx`.
**Channel skin:** Humanitarians AI — outro via `OutroSeries`/`OutroCTA`, handle `@HumanitariansAI`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone typed 'maintain' — as if Claude keeps tidying your CRM by itself, all the time. A skill called crm-maintenance runs a fixed set of steps once per request, the same way every time. Does Claude check my CRM by itself?" | writer types "Does Claude\nMAINTAIN my CRM\nby itself?", hesitates on MAINTAIN, corrects to "check" — lands "Does Claude check my CRM by itself?" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is crm-maintenance. It holds two items — a SKILL.md file and a reference folder. The SKILL.md is the full instruction set, in plain language — no hidden logic. Claude reads it, then acts. The file is the program. | folder tree reveal: SKILL.md + reference/ |
| B02 | pipeline | The pipeline sits in the Steps section. Claude reads each step in order, then runs it. Linear — no branching unless a step says so. | YOUR REQUEST → Read SKILL.md → Execute → RESULT |
| B03 | 3 mechanism | Here's the part worth knowing. crm-maintenance is a specification written as an instruction set, not a standing job. It runs once, when you ask, and does exactly what the file says — nothing runs in the background on its own. Ask the same thing twice, and you get the same result both times; ask for something the file doesn't cover, and the skill has nothing to say about it. | heading card: "The interesting constraint." + bounded-spec statement |
| **BCRY** | **6 carry-out** | "Maintenance" here isn't an ongoing job Claude runs by itself. It's one spec-bound check — the same steps, the same result, every time you ask. | the sentence, alone, serif, large — WantQuote |
| BHTF | your turn handoff | Your turn. Here's the prompt — read it with me. Read the crm-maintenance skill in this folder. Before you run it, tell me exactly which steps it will execute, in order, and tell me plainly if anything I ask falls outside what the file covers. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro series | Claude, Crm Maintenance. | OutroSeries — title restate |
| BCTA | outro cta | …Liam, in for Bear. | OutroCTA — handle @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | B03 states the bounded-spec scope and stops; the source's "Teardown moment," "what it gets right / what it bites," and "Verdict" framing are all dropped |
| Stakes → mechanism | B00 states the misconception (crm-maintenance = an ongoing background job); B01–B02 explain the file and pipeline before B03's scope statement |
| Carry-out | BCRY compresses the distinction (bounded, request-triggered, repeatable — not a standing autonomous process) rather than summarizing the topic |
| Host handoff | B00 hands narration to Liam implicitly; no puppet host in hai-simple |
| Hedge words | none used — every claim is a confirmed, present-tense description of how crm-maintenance and Claude Skills generally work |

## Deliberately not claimed

- **Not "Claude maintains the CRM on its own."** The naive framing in B00 ("Does Claude
  MAINTAIN my CRM by itself?") is stated and corrected within the same beat — the skill
  runs once per request, not continuously.
- **No claim about what crm-maintenance specifically checks or updates inside a CRM.**
  Unlike this family's `crm-cleanup` sibling, the source's own placeholder for that
  description (`>`) is empty in *every* beat, including B00 — there is nothing to
  recover, and the actual `SKILL.md` this source points at does not exist on this
  machine. Inventing "stale deals," "duplicate contacts," or any other specific action
  would be fabrication; this reel states only the anatomy (SKILL.md + reference/),
  pipeline (Steps section, linear), and scope guarantee (bounded spec, repeatable, silent
  outside the file) that the source's readable text actually supports. Full detail in
  QUESTION.md.
- **No verdict on the skill's design.** The source's Teardown register judged the skill
  ("what it gets right," "what it bites," "know the limit"); this Plain redo describes
  the same bounded-spec scope without ruling on whether it was well designed.

## Handoff prompt (BHTF, read aloud)

> "Read the crm-maintenance skill in this folder. Before you run it, tell me exactly
> which steps it will execute, in order, and tell me plainly if anything I ask falls
> outside what the file covers."

Why it's worth running: it forces Claude to state its own steps and boundary before
acting — the same "explain first" clause the source reel's own handoff used to surface a
skill's real constraint logic.

---
**GATE P — signed:** ______________________  (human)
