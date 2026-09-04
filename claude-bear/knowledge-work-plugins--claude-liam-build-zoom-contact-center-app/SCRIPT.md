# Claude Doesn't Answer Your Calls — It Builds the Contact Center App. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-contact-center-app`).*
*Register: **Plain**. 7 beats, matching the source's beat count (B00, B01, B02, B03, BVDT, BHTF, BOUT).*
*Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes a Zoom contact center build means Claude hands them a talking AI agent. It doesn't — build-zoom-contact-center-app means the app: the integration code that plugs into Zoom's existing Contact Center platform." | Writer types "Build me a / Zoom contact / center / agent?"; "agent" hesitates and corrects to "app" |
| B01 | 1 anatomy | This skill is built from a skill — a folder Claude reads before it works. Inside are eight items: a RUNBOOK and a SKILL file, plus folders for Android, iOS, core concepts, references, common scenarios, and troubleshooting. Claude reads the file, then follows it. | a folder opens to reveal SKILL.md (highlighted), RUNBOOK.md, and the six subfolders |
| B02 | 2 mechanism — pipeline | The steps run in order: read the file, work through each step exactly as written, then return the result. Nothing runs out of sequence unless a step itself says so. | three cards: Read SKILL.md -> Execute steps in order -> Return result |
| B03 | 3 constraint | For this skill, the scope is five things: app, web, or native integrations; engagement context and state handling; campaigns; callbacks; and version-drift troubleshooting. Each sits inside Zoom's existing Contact Center platform — Claude fits code around it, it doesn't replace it. Ask for something outside those five and there's no mode that covers it. | five scope rows filling in with checkmarks; a boundary line, faint field beyond captioned "nothing outside this list" |
| **BCRY** | **4 carry-out** | Build Zoom Contact Center App doesn't hand you a talking AI agent — it makes Claude build the app: integration code for engagement context, state handling, campaigns, callbacks, or version-drift fixes, fitted around Zoom's own Contact Center platform. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Ask Claude: I want to build an integration for Zoom Contact Center that handles engagement context and campaign callbacks. Walk me through the pieces I'd need, and where version-drift issues tend to show up, before writing any code. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude Doesn't Answer Your Calls — It Builds the Contact Center App. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-liam-build-zoom-contact-center-app`, Teardown, already rendered) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Claude, Build Zoom Contact Center App." — a skill-teardown title | reframed as an actually-askable question: does Claude itself talk to callers, or does it build the integration around Zoom's platform |
| Facts | `build-zoom-contact-center-app` is a *reference* skill for Zoom Contact Center; used after routing to a contact-center workflow for app/web/native integrations, engagement context and state handling, campaigns, callbacks, or version-drift troubleshooting; a skill = a folder Claude reads before acting (8 items: RUNBOOK.md, SKILL.md, android/, concepts/, ios/, references/, scenarios/, troubleshooting/); execution is linear (read -> execute steps in order -> return) | unchanged |
| Beat count | 7 (B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro) | 7 (B00 writer, B01 anatomy, B02 mechanism, B03 constraint, BCRY carry-out, BHTF your turn, BOUT outro) |
| B00 | `ClaudeComposerAsk` cold open (Remotion "ask" card, Claude palette, "Hola, Liam" greeting) | `BrutalistHesitantWriter` (WRITER LAW), humanitarians palette; wrong guess made explicit ("agent" -> "app") |
| Register | Teardown — B03 named itself "the Teardown moment" and graded the skill ("what it gets right… what it bites"); BVDT was framed as a "Verdict" card | Plain — B03 states the same five-item scope boundary as a fact, no grading language; BCRY states the mechanism as a carry-out sentence, not a verdict |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| B01–B03 skin | `SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` (Remotion cards, fixed Claude palette) | rebuilt as GRAPHIC (Manim) in the humanitarians palette, same teaching content, per hai-simple's established channel-skin practice |
| BVDT → BCRY | `ClaudeVerdictArtifact` ("Verdict" card, Claude palette, four-line recap) | `WantQuote` carry-out card, single compressed sentence |
| Close | `ClaudeTitleOutro`, `@NikBearBrown`, "Hola, Liam" skin | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| BHTF prompt | truncated/garbled string ("I want to reference skill for zoom contact center. use after routing to a contac. Read the build-zoom-contact-center-app skill and walk me through what you will do before you do it.") referencing a skill file and description cut mid-word | rewritten as a clean, genuinely runnable prompt that asks Claude directly to walk through the same architecture — no dependency on a plugin skill file the viewer doesn't have |

No beat in the source is `ai-video-prompt`, pantry, or a human-drop slot — the
source was already all-Remotion (`ClaudeComposerAsk` x2, three
`SkillTeardown*` cards, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`), so the
NO-GENAI/NO-PANTRY LAW required no substitution beyond the WRITER LAW and
channel-skin row already required.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the wrong guess and the real stakes before B01's anatomy or B02's pipeline |
| Wrong guess surfaced | B00 ("agent" -> "app") |
| No design judgment | B03 states the five-item scope boundary as a fact ("nothing outside this list"), not a critique of the skill's design; BCRY states the mechanism, not a verdict on whether five items is the right scope |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that Claude itself talks to a caller.** Every beat keeps the boundary
  that Claude writes and assembles the app's integration code; it never
  claims Claude personally engages with a customer on a contact-center call.
- **Not a claim that this replaces Zoom's own Contact Center platform.** The
  source scoped the skill to fitting code *around* the platform, not
  replacing it; this redo keeps that boundary as stated fact.
- **Not a verdict on whether five scope items is the right set.** The
  source's B03 graded the skill ("what it gets right… what it bites"); this
  redo removes that framing per Plain register and states the boundary
  without grading it.

## Handoff prompt (BHTF, read aloud)

> "I want to build an integration for Zoom Contact Center that handles
> engagement context and campaign callbacks. Walk me through the pieces I'd
> need, and where version-drift issues tend to show up, before writing any
> code."

Why it's worth running: it's a real, paste-ready Claude prompt that surfaces
the same scope (engagement context, campaigns, callbacks, version drift) the
skill automates, without requiring the viewer to have the plugin installed or
write a line of code first.

---
**GATE P — signed:** ______________________  (human)
