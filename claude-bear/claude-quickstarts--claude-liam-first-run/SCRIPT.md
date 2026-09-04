# Claude, First Run. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `anthropics/claude-quickstarts/youtube/claude-liam-first-run`).*
*Register: **Plain**. 7 beats, matching the source's beat count. Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes Claude's first-run behavior is just built in — hardwired into the model. It isn't. It's written down, in a skill file Claude reads before it acts. Here's what that file actually contains." | Writer types "Claude just knows what to do first — it's built in, right?..."; "built" hesitates and corrects to "written" |
| B01 | anatomy | This particular skill is called first-run. Its SKILL.md file holds the whole instruction set, in plain language — no hidden code, no separate logic buried somewhere else. Whatever Claude does, it's written right there. | a folder labelled first-run/ opens to one file card, SKILL.md, marked as the instruction set |
| B02 | pipeline | The pipeline is in the Steps section. Claude reads each step in order and executes it. Linear — no branching unless the step says so. | three phases in sequence: Read SKILL.md → Execute each step → Return the result, request in on the left, result out on the right |
| B03 | mechanism — the scope | first-run's job, spelled out in its own words: check the environment, run one safe browser-only task, then open the trajectory viewer. Claude follows that exact sequence, every time. It has nothing to say about a task the file never described. | three steps listed inside a bounded box; outside the box, a dashed boundary marks what the file never covers |
| **BCRY** | **carry-out** | A skill isn't a built-in capability — it's a folder of plain-language instructions Claude reads before it acts, and follows exactly, only as far as the file goes. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Take any set of detailed instructions — a style guide, a runbook, a SKILL.md if you have one — paste it into Claude, and ask it to walk you through what it will do, step by step, before it does anything. That one clause, "before you do it," is what surfaces the real logic underneath. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, First Run. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-liam-first-run`, Teardown, already rendered) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Claude, First Run." | unchanged |
| Facts | a skill is a folder Claude reads before acting; SKILL.md is the full instruction set; the Steps section runs linearly; first-run's own job is env check → one safe browser-only task → open the trajectory viewer | unchanged |
| Beat count | 7 (B00, B01, B02, B03, BVDT, BHTF, BOUT) | 7 (B00, B01, B02, B03, BCRY, BHTF, BOUT) |
| B00 | `ClaudeComposerAsk` cold open (Remotion "ask" card, Claude palette) | `BrutalistHesitantWriter` (WRITER LAW), humanitarians palette |
| Register | Teardown — B03 explicitly graded the skill ("what it gets right… what it bites") | Plain — B03 states the same scope as a boundary, no grading; no-judgment audit below |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| B01/B02/B03 skin | `SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` — fixed Claude-palette Remotion, no palette override props | rebuilt as GRAPHIC (Manim) in the humanitarians palette, same teaching content, per hai-simple's channel-skin row |
| BVDT → BCRY | `ClaudeVerdictArtifact` ("Verdict" card, Claude palette) | `WantQuote` carry-out card, single compressed sentence |
| Close | `ClaudeTitleOutro`, `@NikBearBrown` | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| BHTF prompt | referenced a specific private-repo skill path (`.claude/skills/first-run/SKILL.md`) most viewers can't paste | generalized to any detailed instructions the viewer already has (style guide, runbook, or their own SKILL.md) — genuinely runnable today |

No beat in the source is `ai-video-prompt`, pantry, or a human-drop slot — the source
was already all-Remotion — so the NO-GENAI/NO-PANTRY LAW required no substitution
beyond what the WRITER LAW and channel-skin row already require.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00–B01; the Steps pipeline (B02) and first-run's own scope (B03) wait until the anatomy is established |
| Wrong guess surfaced | B00 (built in → written) |
| No design judgment | B03 states first-run's exact three steps and its boundary without grading them "right" or a "bite"; BCRY states the mechanism, not a verdict on the SKILL.md format |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that every skill is this simple.** first-run is the specimen; the reel
  never claims all skills share its exact shape.
- **Not a verdict on the SKILL.md format.** The source's B03/BVDT graded it
  ("gets right… bites"); this redo removes that judgment entirely — Plain
  explains the mechanism and its boundary, then stops.
- **Not a claim that first-run works outside what its file specifies.** B03
  states the boundary directly; BCRY repeats it as "only as far as the file goes."

## Handoff prompt (BHTF, read aloud)

> "Take any set of detailed instructions — a style guide, a runbook, a
> SKILL.md if you have one — paste it into Claude, and ask it to walk you
> through what it will do, step by step, before it does anything."

Why it's worth running: it's the reel's own claim, testable in under two
minutes, on instructions the viewer already has rather than the reel's example.

---
**GATE P — signed:** ______________________  (human)
