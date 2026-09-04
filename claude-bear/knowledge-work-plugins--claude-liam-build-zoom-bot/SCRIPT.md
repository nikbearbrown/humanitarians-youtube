# Claude Doesn't Join Your Zoom Calls — It Builds the Bot. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-bot`).*
*Register: **Plain**. 7 beats, matching the source's beat count (B00–B06 equivalent: B00, B01, B02, B03, BVDT, BHTF, BOUT). Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes Claude can personally be the Zoom bot, joining meetings itself. It can't. What it builds is the bot — the code for a meeting recorder or real-time media workflow that you run." | Writer types "Can Claude / be my / Zoom meeting / bot?"; "be" hesitates and corrects to "build" |
| B01 | 1 anatomy | This skill is built from something called a skill — a folder Claude reads before it works. Inside is one file, written in plain language, that spells out exactly what build-zoom-bot covers: joining meetings, recording them, or wiring up real-time media and backend services. Claude reads the file, then follows it. | a folder opens to reveal SKILL.md (highlighted), references/, scripts/ |
| B02 | 2 mechanism — pipeline | The steps run in order: read the file, work through each step exactly as written, then return the result. Nothing runs out of sequence unless a step itself says so. | three cards: Read SKILL.md -> Execute steps in order -> Return result |
| B03 | 3 constraint | For this skill, there are exactly three things it builds: a meeting bot that joins a call, a recorder that captures the session, or a real-time media workflow that processes audio and video as it happens. Each is assembled from the same three pieces — Zoom's Meeting SDK, its real-time media streams, and your own backend service. Ask it to build something outside those three and there's no mode that covers it. | three build-target rows filling in with checkmarks; a boundary line, faint field beyond captioned "nothing outside this list" |
| **BCRY** | **4 carry-out** | Build Zoom Bot doesn't make Claude join your meetings itself — it makes Claude build the bot: a meeting bot, a recorder, or a real-time media workflow, assembled from Zoom's own Meeting SDK, RTMS, and your backend. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Ask Claude: I want to build a Zoom bot that joins a call and saves the transcript. Walk me through the pieces I'd need — the Meeting SDK, real-time media streams, and my own backend — before writing any code. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude Doesn't Join Your Zoom Calls — It Builds the Bot. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-liam-build-zoom-bot`, Teardown, already rendered) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Claude, Build Zoom Bot." — a skill-teardown title | reframed as an actually-askable question: does Claude itself join the call, or does it build the software that does |
| Facts | `build-zoom-bot` builds a Zoom meeting bot, recorder, or real-time media workflow; applies when joining meetings programmatically, processing live media/transcripts, or combining Meeting SDK, RTMS, and backend services; a skill = a folder Claude reads before acting; SKILL.md is the instruction set; execution is linear (read -> execute steps in order -> return); same input, same output, every run | unchanged |
| Beat count | 7 (B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro) | 7 (B00 writer, B01 anatomy, B02 mechanism, B03 constraint, BCRY carry-out, BHTF your turn, BOUT outro) |
| B00 | `ClaudeComposerAsk` cold open (Remotion "ask" card, Claude palette, "Hola, Liam" greeting) | `BrutalistHesitantWriter` (WRITER LAW), humanitarians palette; wrong guess made explicit ("be" -> "build") |
| Register | Teardown — B03 named itself "the Teardown moment" and graded the skill ("what it gets right… what it bites"); BVDT was framed as a "Verdict" card | Plain — B03 states the same three-build-target boundary as a fact, no grading language; BCRY states the mechanism as a carry-out sentence, not a verdict |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| B01–B03 skin | `SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` (Remotion cards, fixed Claude palette) | rebuilt as GRAPHIC (Manim) in the humanitarians palette, same teaching content, per hai-simple's established channel-skin practice |
| BVDT → BCRY | `ClaudeVerdictArtifact` ("Verdict" card, Claude palette, four-line recap) | `WantQuote` carry-out card, single compressed sentence |
| Close | `ClaudeTitleOutro`, `@NikBearBrown`, "Hola, Liam" skin | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| BHTF prompt | truncated/garbled string ("I want to build a zoom meeting bot, recorder, or real-time media workflow. use when joinin. Read the build-zoom-bot skill and walk me through what you will do before you do it.") referencing a skill file the general viewer won't have installed | rewritten as a clean, genuinely runnable prompt that asks Claude directly to walk through the architecture — same teaching point, no dependency on a plugin skill file the viewer doesn't have |

No beat in the source is `ai-video-prompt`, pantry, or a human-drop slot — the source
was already all-Remotion (`ClaudeComposerAsk` × 2, three `SkillTeardown*` cards,
`ClaudeVerdictArtifact`, `ClaudeTitleOutro`) — so the NO-GENAI/NO-PANTRY LAW required
no substitution beyond the WRITER LAW and channel-skin row already require.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the wrong guess and the real stakes before B01's anatomy or B02's pipeline |
| Wrong guess surfaced | B00 ("be" -> "build") |
| No design judgment | B03 states the three-build-target boundary as a fact ("nothing outside this list gets built"), not a critique of the skill's design; BCRY states the mechanism, not a verdict on whether three targets is the right number |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that Claude itself dials into or attends a live Zoom call.** Every beat keeps
  the boundary that Claude writes and assembles the bot's code; it never claims Claude
  personally joins a meeting as a participant.
- **Not a claim that this replaces a developer's Zoom API setup.** The source scoped
  the skill to "only what the file specifies"; this redo keeps that boundary as stated
  fact, not as a limitation to be argued with.
- **Not a verdict on whether three build targets is the right set.** The source's B03
  graded the skill ("what it gets right… what it bites"); this redo removes that
  framing per Plain register and states the boundary without grading it.

## Handoff prompt (BHTF, read aloud)

> "I want to build a Zoom bot that joins a call and saves the transcript. Walk me
> through the pieces I'd need — the Meeting SDK, real-time media streams, and my own
> backend — before writing any code."

Why it's worth running: it's a real, paste-ready Claude prompt that surfaces the same
three-piece architecture (Meeting SDK, RTMS, backend) the skill automates, without
requiring the viewer to have the plugin installed or write a line of code first.

---
**GATE P — signed:** ______________________  (human)
