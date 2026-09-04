# Claude Doesn't Build a New Video App — It Wires In Zoom's SDK. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-meeting-app`).*
*Register: **Plain**. 7 beats, matching the source's beat count (B00, B01, B02, B03, BVDT, BHTF, BOUT). Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes Claude writes a whole new video calling system. It doesn't. build-zoom-meeting-app wires Zoom's own Meeting SDK into an app you already have — meeting joins, embeds, lifecycle flows." | Writer types "Does Claude / write a new / video calling / system?"; "new" hesitates and corrects to "Zoom" |
| B01 | 1 anatomy | This skill is built from something called a skill — a folder Claude reads before it works. Inside is one file, written in plain language, that spells out exactly what build-zoom-meeting-app covers: Meeting SDK joins, web or mobile embeds, and the lifecycle around a meeting. Claude reads the file, then follows it. | a folder opens to reveal SKILL.md (highlighted), references/, scripts/ |
| B02 | 2 mechanism — pipeline | The steps run in order: read the file, work through each step exactly as written, then return the result. Nothing runs out of sequence unless a step itself says so. | three cards: Read SKILL.md -> Execute steps in order -> Return result |
| B03 | 3 constraint | For this skill, there are exactly four situations it covers: implementing a Meeting SDK join, embedding a meeting in a web or mobile app, handling the lifecycle around a meeting — starting, waiting, ending — or deciding between the Meeting SDK and the Video SDK. Each stays inside Zoom's own developer tools. Ask for something outside those four and there's no mode that covers it. | four rows filling in with checkmarks: SDK join, web/mobile embed, lifecycle, SDK choice; a boundary line, faint field beyond captioned "nothing outside this list" |
| **BCRY** | **4 carry-out** | build-zoom-meeting-app doesn't hand Claude a video-calling engine to invent — it hands Claude Zoom's own Meeting SDK, wired into an app you already have as a join flow, an embed, or the lifecycle around the call. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Ask Claude: I want to add a 'Join Meeting' button to my web app using Zoom's Meeting SDK. Walk me through the pieces I'd need — the SDK, the meeting lifecycle events, and when I'd reach for the Video SDK instead — before writing any code. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude Doesn't Build a New Video App — It Wires In Zoom's SDK. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-liam-build-zoom-meeting-app`, Teardown, already rendered) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Claude, Build Zoom Meeting App." — a skill-teardown title | reframed as an actually-askable question: does Claude write a new video-calling engine, or wire in Zoom's existing SDK |
| Facts | `build-zoom-meeting-app` builds or embeds a Zoom meeting flow; applies to Meeting SDK joins, web/mobile embeds, meeting lifecycle flows, or choosing between Meeting SDK and Video SDK; a skill = a folder Claude reads before acting; SKILL.md is the instruction set; execution is linear (read -> execute steps in order -> return); same input, same output, every run | unchanged |
| Beat count | 7 (B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro) | 7 (B00 writer, B01 anatomy, B02 mechanism, B03 constraint, BCRY carry-out, BHTF your turn, BOUT outro) |
| B00 | `ClaudeComposerAsk` cold open (Remotion "ask" card, Claude palette, "Hola, Liam" greeting) | `BrutalistHesitantWriter` (WRITER LAW), humanitarians palette; wrong guess made explicit ("new" -> "Zoom") |
| Register | Teardown — B03 named itself "the Teardown moment" and graded the skill ("what it gets right… what it bites"); BVDT was framed as a "Verdict" card | Plain — B03 states the same four-situation boundary as a fact, no grading language; BCRY states the mechanism as a carry-out sentence, not a verdict |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| B01–B03 skin | `SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` (Remotion cards, fixed Claude palette) | rebuilt as GRAPHIC (Manim) in the humanitarians palette, same teaching content, per hai-simple's established channel-skin practice |
| BVDT → BCRY | `ClaudeVerdictArtifact` ("Verdict" card, Claude palette, four-line recap) | `WantQuote` carry-out card, single compressed sentence |
| Close | `ClaudeTitleOutro`, `@NikBearBrown`, "Hola, Liam" skin | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| BHTF prompt | garbled string ("I want to build or embed a zoom meeting flow. use when implementing meeting sdk joins, web. Read the build-zoom-meeting-app skill and walk me through what you will do before you do it.") referencing a skill file the general viewer won't have installed | rewritten as a clean, genuinely runnable prompt that asks Claude directly to add a Join Meeting button using the Meeting SDK — same teaching point, no dependency on a plugin skill file the viewer doesn't have |

No beat in the source is `ai-video-prompt`, pantry, or a human-drop slot — the source
was already all-Remotion (`ClaudeComposerAsk` × 2, three `SkillTeardown*` cards,
`ClaudeVerdictArtifact`, `ClaudeTitleOutro`) — so the NO-GENAI/NO-PANTRY LAW required
no substitution beyond the WRITER LAW and channel-skin row already require.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the wrong guess and the real stakes before B01's anatomy or B02's pipeline |
| Wrong guess surfaced | B00 ("new" -> "Zoom") |
| No design judgment | B03 states the four-situation boundary as a fact ("nothing outside this list gets covered"), not a critique of the skill's design; BCRY states the mechanism, not a verdict on whether four situations is the right scope |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that Claude writes its own video-calling engine.** Every beat keeps the
  boundary that Claude wires Zoom's own Meeting SDK (or Video SDK) into an app that
  already exists; it never claims Claude invents signaling or media transport itself.
- **Not a claim that this replaces a developer's own Zoom API account/setup.** The
  source scoped the skill to "only what the file specifies"; this redo keeps that
  boundary as stated fact, not as a limitation to be argued with.
- **Not a verdict on whether four situations is the right set.** The source's B03
  graded the skill ("what it gets right… what it bites"); this redo removes that
  framing per Plain register and states the boundary without grading it.

## Handoff prompt (BHTF, read aloud)

> "I want to add a 'Join Meeting' button to my web app using Zoom's Meeting SDK.
> Walk me through the pieces I'd need — the SDK, the meeting lifecycle events, and
> when I'd reach for the Video SDK instead — before writing any code."

Why it's worth running: it's a real, paste-ready Claude prompt that surfaces the
same SDK-vs-SDK and lifecycle boundary the skill automates, without requiring the
viewer to have the plugin installed or write a line of code first.

---
**GATE P — signed:** ______________________  (human)
