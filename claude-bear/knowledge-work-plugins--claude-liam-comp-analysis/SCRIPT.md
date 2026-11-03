# Claude, Comp Analysis. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-comp-analysis`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first (CARRY-OUT.md).*

**Cold open:** BrutalistHesitantWriter (Remotion, free/local). **Narrator:** Liam, Kokoro `am_onyx`.
**Channel skin:** Humanitarians AI — outro via `OutroSeries`, handle `@HumanitariansAI`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone might ask how the comp-analysis app decides what to pay someone. It's not an app — it's a skill, a folder of instructions Claude reads first. How does the comp-analysis skill set our pay bands?" | writer types "How does the comp-analysis app set our pay bands?", hesitates on "app", corrects to "skill" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is comp-analysis. The SKILL.md contains the full instruction set — plain language, no hidden logic. Claude reads it, then acts. The file is the program. | folder tree reveal: one file, SKILL.md, 3k |
| B02 | pipeline | The pipeline is in the Steps section. Claude reads each step in order and executes it. Linear — no branching unless the step says so. | YOUR REQUEST → Read SKILL.md → Execute → RESULT |
| B03 | mechanism + scope | comp-analysis is a specification written as an instruction set: analyze compensation by benchmarking pay, placing roles in bands, and modeling equity grants. Because Claude follows exactly what's written, the result is the same every run — and it only covers what the page says. | heading card: "What the page says, exactly." + on-screen: "Benchmark pay, place roles in bands, and model equity grants." |
| **BCRY** | **carry-out** | A Skill doesn't give Claude judgment about pay — it makes Claude run your benchmarking steps, in order, every time. | the sentence, alone, serif, large — WantQuote |
| BHTF | your turn handoff | Your turn. Paste this into Claude: 'Explain what a Claude Skill is — then, if I wrote a three-step SKILL.md for benchmarking one role's pay against a public salary range, walk me through exactly how you'd read and follow it, step by step, before you start.' Watching it name the steps before it starts is what shows you the mechanism is real. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Comp Analysis. Liam, in for Bear. | OutroSeries — title restate, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | B03 states the constraint (spec, inputs, scope limit) and stops; the source's "Teardown moment" framing and "what it gets right / what it bites" verdict language are both dropped |
| Stakes → mechanism | B00 states the misconception (autonomous app deciding pay vs. a followed skill); B01–B02 explain the file and pipeline before B03's constraint |
| Carry-out | BCRY compresses the distinction (fixed steps, not independent pay judgment), not the topic |
| Wrong guess picked up | B00's "app" → "skill" correction is the same fact B01 (a skill is a folder) and BCRY (run your steps, in order) both restate |
| Hedge words | none used — every claim is a confirmed, present-tense description of the skill's own spec, unchanged from the source |

## Deliberately not claimed

- **Not "Claude decides pay."** The naive framing in B00 ("decides what to pay someone")
  is stated and corrected within the same beat — the skill benchmarks pay, places roles
  in bands, and models equity grants from the data and roles it's given; it never claims
  to make the actual pay decision.
- **No verdict on the skill's design.** The source's Teardown register judged the skill
  ("what it gets right," "what it bites"); this Plain redo describes the same constraint
  (repeatable, scoped to what the page says) without ruling on whether it was well
  designed.
- **No invented specifics.** The source sheet carried a real, filled-in skill
  description (untruncated in its B00 beat: "Analyze compensation — benchmarking, band
  placement, and equity modeling. Trigger with 'what should we pay a [role]', 'is this
  offer competitive', 'model this equity grant', or when uploading comp data to find
  outliers and retention risks.") rather than an unfilled template placeholder — see
  QUESTION.md. Several later source beats carried a truncated/garbled copy of this same
  description; this build reuses only the untruncated version.
- **Not compensation advice.** The reel explains how a Claude Skill file works, using
  comp-analysis as the example; it makes no claim about what any role should actually be
  paid and carries the standard educational disclaimer in the description.

## Handoff prompt (BHTF, read aloud)

> "Explain what a Claude Skill is — then, if I wrote a three-step SKILL.md for
> benchmarking one role's pay against a public salary range, walk me through exactly how
> you'd read and follow it, step by step, before you start."

Why it's worth running: viewers don't have the actual `comp-analysis` SKILL.md file, so
the prompt substitutes a toy example any viewer can write themselves in three lines —
and watching Claude name the steps before executing them is the same "reads it, then
acts" mechanism B01 describes, made visible in your own session.

---
**GATE P — signed:** ______________________  (human)
