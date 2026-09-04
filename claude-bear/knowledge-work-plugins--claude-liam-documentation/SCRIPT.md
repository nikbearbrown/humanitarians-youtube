# Claude, Documentation. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-documentation`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first.*
*Voice: Liam, Kokoro `am_onyx`. Cold open: BrutalistHesitantWriter (Remotion).*

## The question

"What actually happens when you ask Claude to document something?" — the
general-audience version of the source's teardown of Anthropic's
`documentation` skill.

## The wrong guess a newcomer makes

That "document this" triggers a freeform write-up Claude improvises fresh
each time — picking sections, length, and tone however it feels fits that
particular request, the way a person freelancing would.

## The mechanism

`documentation` is a **skill** — a folder Claude reads before it writes,
containing one file: `SKILL.md`. That file recognizes several document
shapes by name (README, runbook, onboarding guide, API docs, architecture
docs) and the phrases that trigger each ("write docs for", "document this",
"create a README", "write a runbook", "onboarding guide," or any technical
writing request). Claude reads the file, then works fixed steps in order:
read SKILL.md, execute the matching steps for the named shape, return the
finished document. Linear — it only branches when a step itself says so,
never on a whim.

## Anchor example

The request: "write a runbook for restarting the payment service." Planted
early as "hold on to that exact phrase," it returns late: the same shape —
prerequisites, steps, rollback — comes back in the same order, because the
request named a shape the file already recognizes.

## Both directions

- A generated document in a named shape is real signal: the shape it
  promised is the shape it delivered.
- But ask for something outside the file's list — some ad hoc write-up it
  doesn't name — and the guarantee ends there. That request falls back to
  Claude's general judgment, not the spec's.

## Carry-out line

> A skill is a recipe Claude reads before it writes, not a mood it
> improvises. Name a shape the file recognizes, and that's exactly what you
> get.

## Beat-by-beat

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone asks Claude to document this, expecting a freeform write-up shaped however Claude feels fits. Wrong — the shape comes from a file, not a mood. So what decides it?" | BrutalistHesitantWriter — "whatever" corrected to "what the file says" |
| S01 | 1 stakes | You ask Claude to write a runbook for restarting the payment service. Something decides what that document actually contains. | SkillTeardownMechanism — "Before it writes." |
| S02 | 2 wrong guess | The natural guess: Claude drafts it like a person would, improvising sections and picking whatever length feels right. | SkillTeardownMechanism — "Freeform draft?" |
| S03 | 2 break it | Ask for that same runbook again, another day. Nothing drifts — the same sections, same order, because a file decided them, not a mood. | SkillTeardownMechanism — verdict: SAME EVERY TIME |
| S04 | 3 mechanism | That's because documentation is a skill — a folder Claude reads before it writes. Inside sits one file: SKILL.md, the instructions, in plain language. | SkillTeardownAnatomy — SKILL.md, 1 file |
| S05 | **4 anchor planted** | Say the request is: write a runbook for restarting the payment service. Hold on to that exact phrase. | BrutalistTerminalOpen — the request + a three-item checklist |
| S06 | 3 mechanism | The file doesn't cover just any writing — it names five specific shapes, each with its own trigger phrase. | Opus5ChecklistCard — 5 named shapes |
| S07 | 3 mechanism | Then it works in order: read SKILL.md, execute the matching steps, return the finished document. No branching, no improvising. | SkillTeardownPipeline — read / execute / return |
| S08 | 3 mechanism | Linear, mostly — the file only branches when a step itself says so, never on a whim. | SkillTeardownMechanism — "Linear, mostly." |
| S09 | **4 anchor payoff** | Back to that runbook: the same three sections come back, in the same order — because the request named a shape the file already knows. | BrutalistTerminalOpen — SAME request + checklist |
| S10 | 5 direction A | A generated runbook, README, or API doc is real signal — the named shape it promised, delivered. | SkillTeardownMechanism — verdict: REAL SIGNAL |
| S11 | 5 direction B | But ask for something the file doesn't name — some ad hoc write-up outside its list — and the guarantee ends there. You're back to Claude's general judgment, not the spec's. | SkillTeardownMechanism — verdict: NO GUARANTEE |
| BCRY | 6 carry-out | A skill is a recipe Claude reads before it writes, not a mood it improvises. Name a shape the file recognizes, and that's exactly what you get. | WantQuote |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Ask Claude: before you write this runbook, tell me exactly what SKILL.md says you'll include — the shape, and the phrase that triggers it. Then ask for the same shape twice, and compare. | ClaudeComposerAsk |
| BOUT | outro | Claude, Documentation. … Liam, in for Bear. | OutroSeries + OutroCTA — Humanitarians AI skin |

## Six-move audit

| Move | Beat | Satisfied |
|---|---|---|
| 1 stakes first | S01 | yes — the runbook request, before any mechanism |
| 2 wrong guess | S02 → S03 | yes — stated, then falsified by "ask again" |
| 3 mechanism | S04, S06, S07, S08 | yes — folder/file, named shapes, linear pipeline, branch rule |
| 4 anchor | S05 → S09 | yes — same BrutalistTerminalOpen request + checklist, planted then paid off |
| 5 both directions | S10, S11 | yes — named shape delivered is signal; outside the list, no guarantee |
| 6 carry-out | BCRY | yes |

No inference flag: every claim here is what the source `SKILL.md` excerpt and
its teardown narration already stated as fact (recognized shapes, trigger
phrases, linear execution, "bites outside spec") — nothing in this reel is a
leap requiring a hedge. The runbook's three sections (prerequisites, steps,
rollback) are used only as an illustrative, generically-true example of what
a runbook contains, not an invented Claude-specific structure.
