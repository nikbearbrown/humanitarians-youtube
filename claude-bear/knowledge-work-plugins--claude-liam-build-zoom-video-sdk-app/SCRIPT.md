# Claude Doesn't Build You a Zoom Meeting — It Builds a Custom Video App. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-video-sdk-app`).*
*Register: **Plain**. 7 beats, matching the source's beat count (B00, B01, B02, B03, BVDT, BHTF, BOUT). Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes build zoom video sdk app means an app that joins your Zoom meetings. It doesn't. It builds a custom video session — full control over the experience, on whichever platform you target." | Writer types "Can Claude / build my / Zoom meeting / app?"; "meeting" hesitates and corrects to "video" |
| B01 | 1 anatomy | This skill is built from something called a skill — a folder Claude reads before it works. Inside is one file, written in plain language, that spells out exactly what build-zoom-video-sdk-app covers: a reference for embedding Zoom's Video SDK across six platforms — Android, Flutter, iOS, Linux, macOS, and React Native. Claude reads the file, then follows it. | a folder opens to reveal SKILL.md (highlighted), six platform folders beneath it |
| B02 | 2 mechanism — pipeline | The steps run in order: read the file, work through each step exactly as written, then return the result. Nothing runs out of sequence unless a step itself says so. | three cards: Read SKILL.md -> Execute steps in order -> Return result |
| B03 | 3 constraint | This skill has exactly one condition on when it applies: after the work has already been routed to a custom-session workflow — when you need full control over the video experience, not an actual Zoom meeting. Ask for a Zoom meeting instead and this isn't the skill; ask for a custom video session, on any of six platforms, and it is. | two paths splitting from one request: "Zoom meeting" (crossed out), "custom video session" (checked); six platform chips beneath the checked path |
| **BCRY** | **4 carry-out** | Build Zoom Video SDK App doesn't build you a Zoom meeting — it builds a custom video session, full control over the experience, on whichever of six platforms your app runs. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Ask Claude: I want to build a video calling feature for my app — full control over the interface, not the standard Zoom meeting screen. Walk me through what building it with Zoom's Video SDK would involve, before writing any code. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude Doesn't Build You a Zoom Meeting — It Builds a Custom Video App. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-liam-build-zoom-video-sdk-app`, Teardown, already rendered) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Claude, Build Zoom Video Sdk App." — a skill-teardown title | reframed as an actually-askable question: does this give you a Zoom meeting, or a custom video app |
| Facts | `build-zoom-video-sdk-app` is a reference skill for Zoom's Video SDK; used after routing to a custom-session workflow when the user needs full control over the video experience rather than an actual Zoom meeting; platform surface is android/flutter/ios/linux/macos/react-native (8 files total incl. RUNBOOK.md, SKILL.md); a skill = a folder Claude reads before acting; execution is linear (read -> execute steps in order -> return); same input, same output, every run | unchanged |
| Beat count | 7 (B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro) | 7 (B00 writer, B01 anatomy, B02 mechanism, B03 constraint, BCRY carry-out, BHTF your turn, BOUT outro) |
| B00 | `ClaudeComposerAsk` cold open (Remotion "ask" card, Claude palette, "Hola, Liam" greeting) | `BrutalistHesitantWriter` (WRITER LAW), humanitarians palette; wrong guess made explicit ("meeting" -> "video") |
| Register | Teardown — B03 named itself "the Teardown moment" and graded the skill ("what it gets right… what it bites"); BVDT was framed as a "Verdict" card | Plain — B03 states the same one-condition boundary as a fact, no grading language; BCRY states the mechanism as a carry-out sentence, not a verdict |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| B01–B03 skin | `SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` (Remotion cards, fixed Claude palette) | rebuilt as GRAPHIC (Manim) in the humanitarians palette, same teaching content, per hai-simple's established channel-skin practice |
| BVDT → BCRY | `ClaudeVerdictArtifact` ("Verdict" card, Claude palette, four-line recap) | `WantQuote` carry-out card, single compressed sentence |
| Close | `ClaudeTitleOutro`, `@NikBearBrown`, "Hola, Liam" skin | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| BHTF prompt | truncated/garbled string ("I want to reference skill for zoom video sdk. use after routing to a custom-session workfl. Read the build-zoom-video-sdk-app skill and walk me through what you will do before you do it.") referencing a skill file the general viewer won't have installed | rewritten as a clean, genuinely runnable prompt that asks Claude directly to walk through building a custom video feature — same teaching point, no dependency on a plugin skill file the viewer doesn't have |

No beat in the source is `ai-video-prompt`, pantry, or a human-drop slot — the source
was already all-Remotion (`ClaudeComposerAsk` × 2, three `SkillTeardown*` cards,
`ClaudeVerdictArtifact`, `ClaudeTitleOutro`) — so the NO-GENAI/NO-PANTRY LAW required
no substitution beyond the WRITER LAW and channel-skin row already require.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the wrong guess and the real stakes before B01's anatomy or B02's pipeline |
| Wrong guess surfaced | B00 ("meeting" -> "video") |
| No design judgment | B03 states the one-condition boundary as a fact ("ask for a Zoom meeting and this isn't the skill"), not a critique of the skill's scope; BCRY states the mechanism, not a verdict on whether the scope is right |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that this skill can build you an actual Zoom meeting client.** Every beat
  keeps the boundary that it applies to CUSTOM video sessions, not the standard
  Zoom meeting experience — the two are stated as different things, never conflated.
- **Not a claim that this replaces a developer's own Zoom Video SDK setup on any one
  platform.** The source scoped the skill to "only what the file specifies"; this
  redo keeps that boundary as stated fact, not as a limitation to be argued with.
- **Not a verdict on whether six platforms is the right set, or whether a custom
  session is better than a Zoom meeting.** The source's B03 graded the skill ("what
  it gets right… what it bites"); this redo removes that framing per Plain register
  and states the boundary without grading it.

## Handoff prompt (BHTF, read aloud)

> "I want to build a video calling feature for my app — full control over the
> interface, not the standard Zoom meeting screen. Walk me through what building it
> with Zoom's Video SDK would involve, before writing any code."

Why it's worth running: it's a real, paste-ready Claude prompt that surfaces the
same meeting-vs-custom-session distinction the skill is scoped around, without
requiring the viewer to have the plugin installed or write a line of code first.

---
**GATE P — signed:** ______________________  (human)
