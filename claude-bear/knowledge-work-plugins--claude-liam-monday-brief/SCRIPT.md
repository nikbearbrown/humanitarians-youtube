# The Monday Brief Isn't Memory. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-monday-brief`).*
*Register: **Plain**. 7 beats, matching the source's beat count (B00, B01, B02, B03, BVDT, BHTF, BOUT). Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes Claude already knows their numbers every Monday, like it's memorized the business. It doesn't. It checks — reading a written file that spells out exactly what a Monday brief means here." | Writer types "Does Claude / just know / my numbers / on Monday?"; "know" hesitates and corrects to "check" |
| B01 | 1 anatomy | This kind of briefing runs from something called a skill — a single file, written in plain language, that Claude reads before it starts. It isn't pulling from memory. It's following the file. The file is the whole program. | a folder opens to reveal one file, SKILL.md (highlighted), captioned "1 file total" |
| B02 | 2 mechanism — pipeline | The steps run in a fixed order: read the file, work through each step exactly as written, then hand back the result. Nothing runs out of sequence unless a step itself says so. | three cards: Read SKILL.md -> Execute each step in order -> Return output |
| B03 | 3 constraint | For this skill, the file specifies exactly what belongs on the page: cash, sales, and pipeline; the week ahead; and your top three to-dos. It can also take where to post the result, or where to save it. Ask for anything the file doesn't list, and there's no step that covers it. | three checklist rows filling in; a boundary line; "plus where to post it, or save it — nothing else" beneath |
| **BCRY** | **4 carry-out** | Claude doesn't already know your Monday numbers — it checks them, against a written file that says exactly what counts, and returns exactly that, the same way every time. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Pull together a one-page Monday brief for me: cash and sales, what's moving in the pipeline, what's on deck this week, and my top three to-dos. Tell me if anything's missing that you'd need from me first. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | The Monday Brief Isn't Memory. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-liam-monday-brief`, Teardown, already rendered) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Claude, Monday Brief." — a skill-teardown title | reframed as an actually-askable question: does Claude already know your numbers, or does it check them |
| Facts | `monday-brief` generates a one-page Monday morning briefing — cash, sales, pipeline, week ahead, top three to-dos; accepts optional post-destination and save-to arguments; a skill = one file (SKILL.md, ~2k, "1 file total") Claude reads before acting; execution is linear (read -> execute steps in order -> return); boundary is that only what the file specifies gets covered, same input same output every run | unchanged |
| Beat count | 7 (B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro) | 7 (B00 writer, B01 anatomy, B02 mechanism, B03 constraint, BCRY carry-out, BHTF your turn, BOUT outro) |
| B00 | `ClaudeComposerAsk` cold open (Remotion "ask" card, Claude palette, "Hola, Liam" greeting) | `BrutalistHesitantWriter` (WRITER LAW), humanitarians palette; wrong guess made explicit ("know" -> "check") |
| Register | Teardown — B03 named itself "the Teardown moment" and graded the skill ("what it gets right… what it bites"); BVDT was framed as a "Verdict" card | Plain — B03 states the same five-item boundary as a fact, no grading language; BCRY states the mechanism as a carry-out sentence, not a verdict |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| B01–B03 skin | `SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` (Remotion cards, fixed Claude palette) | rebuilt as GRAPHIC (Manim) in the humanitarians palette, same teaching content, per hai-simple's established channel-skin practice |
| BVDT → BCRY | `ClaudeVerdictArtifact` ("Verdict" card, Claude palette, four-line recap) | `WantQuote` carry-out card, single compressed sentence |
| Close | `ClaudeTitleOutro`, `@NikBearBrown`, "Hola, Liam" skin | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| BHTF prompt | garbled truncated string ("I want to generates a one-page monday morning briefing — cash, sales, pipeline, . Read the monday-brief skill and walk me through what you will do before you do it.") referencing a skill file the general viewer won't have installed | rewritten as a clean, genuinely runnable prompt that asks Claude directly to assemble the same brief — same teaching point, no dependency on a plugin skill file the viewer doesn't have |

No beat in the source is `ai-video-prompt`, pantry, or a human-drop slot — the source
was already all-Remotion (`ClaudeComposerAsk` x2, three `SkillTeardown*` cards,
`ClaudeVerdictArtifact`, `ClaudeTitleOutro`) — so the NO-GENAI/NO-PANTRY LAW required
no substitution beyond the WRITER LAW and channel-skin row already require.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the wrong guess and the real stakes before B01's anatomy or B02's pipeline |
| Wrong guess surfaced | B00 ("know" -> "check") |
| No design judgment | B03 states the five-item boundary as a fact ("nothing else gets checked"), not a critique of the skill's design; BCRY states the mechanism, not a verdict on whether five items is the right set |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that Claude retains your numbers between runs.** The source scoped the
  skill to reading the file fresh each time; this redo states that as the
  corrected mechanism (B00), not as a limitation to argue with.
- **Not a claim about where the numbers come from.** The source doesn't specify
  a data source for cash/sales/pipeline beyond "the file specifies it" — this
  reel doesn't invent one (no CRM, no accounting tool named).
- **Not a verdict on whether five items is the right set.** The source's B03
  graded the skill ("what it gets right… what it bites"); this redo removes
  that framing per Plain register and states the boundary without grading it.

## Handoff prompt (BHTF, read aloud)

> "Pull together a one-page Monday brief for me: cash and sales, what's
> moving in the pipeline, what's on deck this week, and my top three to-dos.
> Tell me if anything's missing that you'd need from me first."

Why it's worth running: it's runnable today, on whatever numbers the viewer
can hand Claude directly, with no plugin or skill file required — the same
fixed five-item check the source skill automates, made into a prompt anyone
can paste, and it surfaces the mechanism itself (Claude has to ask what it's
missing, because it isn't recalling anything).

---
**GATE P — signed:** ______________________  (human)
