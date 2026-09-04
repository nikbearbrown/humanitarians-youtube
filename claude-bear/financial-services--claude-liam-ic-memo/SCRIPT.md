# Claude, Ic Memo. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-ic-memo`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first (CARRY-OUT.md).*

**Cold open:** BrutalistHesitantWriter (Remotion, free/local). **Narrator:** Liam, Kokoro `am_onyx`.
**Channel skin:** Humanitarians AI — outro via `OutroSeries`, handle `@HumanitariansAI`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone might ask how the ic-memo app writes investment memos on its own. It's not an app — it's a skill, a folder of instructions Claude reads first. So: how does the ic-memo skill draft the memo?" | writer types "How does the ic-memo app write our memo?", hesitates on "app", corrects to "skill" — lands "How does the ic-memo skill write our memo?" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is ic-memo. The SKILL.md contains the full instruction set — plain language, no hidden logic. Claude reads it, then acts. The file is the program. | folder tree reveal: one file, SKILL.md, 2k |
| B02 | pipeline | The pipeline is in the Steps section. Claude reads each step in order and executes it. Linear — no branching unless the step says so. | YOUR REQUEST → Read SKILL.md → Execute → RESULT |
| B03 | mechanism + scope | ic-memo is a specification written as an instruction set: draft a structured investment committee memo for PE deal approval, synthesizing due diligence findings, financial analysis, and deal terms into one document. Because Claude follows exactly what's written, the result is the same every run — and it only covers what the page says. | heading card: "What the page says, exactly." + on-screen: "Draft an IC memo from diligence, financials, and deal terms." |
| **BCRY** | **carry-out** | A Skill doesn't make Claude smarter — it makes Claude follow your steps, in order, every time. | the sentence, alone, serif, large — WantQuote |
| BHTF | your turn handoff | Your turn. Paste this into Claude: 'Explain what a Claude Skill is — then, if I wrote a three-step SKILL.md for drafting a one-page investment memo, walk me through exactly how you'd read and follow it, step by step, before you start.' Watching it name the steps before it starts is what shows you the mechanism is real. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Ic Memo. Liam, in for Bear. | OutroSeries — title restate, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | B03 states the constraint (spec, inputs, scope limit) and stops; the source's "Teardown moment" framing and "what it gets right / what it bites" verdict language are both dropped |
| Stakes → mechanism | B00 states the misconception (autonomous app vs. followed skill); B01–B02 explain the file and pipeline before B03's constraint |
| Carry-out | BCRY compresses the distinction (fixed steps, not independent judgment), not the topic |
| Wrong guess picked up | B00's "app" → "skill" correction is the same fact B01 (a skill is a folder) and BCRY (follow your steps, in order) both restate |
| Hedge words | none used — every claim is a confirmed, present-tense description of the skill's own spec, unchanged from the source |

## Deliberately not claimed

- **Not "Claude decides the deal."** The naive framing in B00 ("writes investment memos
  on its own") is stated and corrected within the same beat — the skill drafts a
  document from inputs it's given; it never claims to render the committee's actual
  approval decision.
- **No verdict on the skill's design.** The source's Teardown register judged the skill
  ("what it gets right," "what it bites"); this Plain redo describes the same constraint
  (repeatable, scoped to what the page says) without ruling on whether it was well
  designed.
- **No invented specifics.** Unlike some siblings in this family, the source sheet here
  carried real, filled-in facts (file size, the exact skill description, the verdict
  recap) rather than unfilled template placeholders — see QUESTION.md. Those facts are
  carried forward verbatim; nothing about ic-memo's actual scope was invented.

## Handoff prompt (BHTF, read aloud)

> "Explain what a Claude Skill is — then, if I wrote a three-step SKILL.md for drafting a
> one-page investment memo, walk me through exactly how you'd read and follow it, step by
> step, before you start."

Why it's worth running: viewers don't have the actual `ic-memo` SKILL.md file, so the
prompt substitutes a toy example any viewer can write themselves in three lines — and
watching Claude name the steps before executing them is the same "reads it, then acts"
mechanism B01 describes, made visible in your own session.

---
**GATE P — signed:** ______________________  (human)
