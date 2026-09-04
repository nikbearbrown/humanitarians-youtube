# Claude Doesn't Design a New Zoom Chat App — It Assembles Into Yours. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-team-chat-app`).*
*Register: **Plain**. 7 beats, matching the source's beat count (B00, B01, B02, B03, BVDT, BHTF, BOUT). Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes Claude freely designs a brand new Zoom chat app from imagination. It doesn't. It assembles one — following a fixed instruction file that spells out exactly what to build." | Writer types "Does Claude / design a new / team chat / app?"; "design" hesitates and corrects to "assemble" |
| B01 | 1 anatomy | This assembly starts from something called a skill — a folder Claude reads before it works. Inside is one file, written in plain language, that spells out exactly what build-zoom-team-chat-app covers: messaging integrations, chatbot experiences, rich cards, buttons, slash commands, and chat webhooks. Claude reads the file, then follows it. | a folder opens to reveal SKILL.md (highlighted), references/, scripts/; caption lists the six chat surfaces |
| B02 | 2 mechanism — pipeline | The steps run in order: read the file, work through each step exactly as written, then return the result. Nothing runs out of sequence unless a step itself says so. | three cards: Read SKILL.md -> Execute steps in order -> Return result |
| B03 | 3 constraint | It only switches on after something else has already decided you're building for chat. From there its coverage is one list: user-scoped messaging integrations, chatbot experiences, rich cards, buttons, slash commands, and chat webhooks. Nothing on that list becomes a new Zoom client — every piece plugs into the chat that's already there. | six coverage rows filling in with checkmarks; a boundary line, faint field beyond captioned "nothing outside this list" |
| **BCRY** | **4 carry-out** | Build Zoom Team Chat App doesn't give Claude a blank page. It gives Claude one instruction file, and Claude assembles exactly what that file lists — bots, cards, buttons, slash commands — into the Zoom chat you already have. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Ask Claude: I want to add a bot to Zoom Team Chat that posts a rich card with buttons when someone runs a slash command. Walk me through the pieces I'd need — the message payload, the card, and the webhook — before writing any code. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude Doesn't Design a New Zoom Chat App — It Assembles Into Yours. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-liam-build-zoom-team-chat-app`, Teardown, already rendered) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Claude, Build Zoom Team Chat App." — a skill-teardown title | reframed as an actually-askable question: does Claude design a new chat app, or something narrower |
| Facts | `build-zoom-team-chat-app` is a reference skill for Zoom Team Chat, used after routing to a chat workflow, for building user-scoped messaging integrations, chatbot experiences, rich cards, buttons, slash commands, or chat webhooks; a skill = a folder Claude reads before acting; SKILL.md is the instruction set; execution is linear (read -> execute steps in order -> return); same input, same output, every run | unchanged |
| Beat count | 7 (B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro) | 7 (B00 writer, B01 anatomy, B02 mechanism, B03 constraint, BCRY carry-out, BHTF your turn, BOUT outro) |
| B00 | `ClaudeComposerAsk` cold open (Remotion "ask" card, Claude palette, "Hola, Liam" greeting) | `BrutalistHesitantWriter` (WRITER LAW), humanitarians palette; wrong guess made explicit ("design" -> "assemble") |
| Register | Teardown — B03 named itself "the Teardown moment" and graded the skill ("what it gets right… what it bites"); BVDT was framed as a "Verdict" card | Plain — B03 states the same coverage-list boundary as a fact, no grading language; BCRY states the mechanism as a carry-out sentence, not a verdict |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| B01–B03 skin | `SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` (Remotion cards, fixed Claude palette) | rebuilt as GRAPHIC (Manim) in the humanitarians palette, same teaching content, per hai-simple's established channel-skin practice |
| BVDT → BCRY | `ClaudeVerdictArtifact` ("Verdict" card, Claude palette, four-line recap) | `WantQuote` carry-out card, single compressed sentence |
| Close | `ClaudeTitleOutro`, `@NikBearBrown`, "Hola, Liam" skin | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| BHTF prompt | truncated/garbled string ("I want to reference skill for zoom team chat. use after routing to a chat workfl. Read the build-zoom-team-chat-app skill and walk me through what you will do before you do it.") referencing a skill file the general viewer won't have installed | rewritten as a clean, genuinely runnable prompt that asks Claude directly to walk through the bot/card/webhook architecture — same teaching point, no dependency on a plugin skill file the viewer doesn't have |

No beat in the source is `ai-video-prompt`, pantry, or a human-drop slot — the source
was already all-Remotion (`ClaudeComposerAsk` × 2, three `SkillTeardown*` cards,
`ClaudeVerdictArtifact`, `ClaudeTitleOutro`) — so the NO-GENAI/NO-PANTRY LAW required
no substitution beyond the WRITER LAW and channel-skin row already require.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the wrong guess and the real stakes before B01's anatomy or B02's pipeline |
| Wrong guess surfaced | B00 ("design" -> "assemble") |
| No design judgment | B03 states the six-item coverage boundary as a fact ("nothing on that list becomes a new Zoom client"), not a critique of the skill's scope; BCRY states the mechanism, not a verdict on whether the list is the right one |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that Claude designs a standalone chat client.** Every beat keeps the boundary
  that every piece Claude assembles plugs into the Zoom Team Chat that's already
  running; none of it becomes a new chat surface of its own.
- **Not a claim that this replaces a developer's own Zoom API setup.** The source
  scoped the skill to "only what the file specifies, after routing to a chat
  workflow"; this redo keeps that boundary as stated fact, not as a limitation to be
  argued with.
- **Not a verdict on whether six items is the right coverage list.** The source's B03
  graded the skill ("what it gets right… what it bites"); this redo removes that
  framing per Plain register and states the boundary without grading it.

## Handoff prompt (BHTF, read aloud)

> "I want to add a bot to Zoom Team Chat that posts a rich card with buttons when
> someone runs a slash command. Walk me through the pieces I'd need — the message
> payload, the card, and the webhook — before writing any code."

Why it's worth running: it's a real, paste-ready Claude prompt that surfaces the same
bot/card/webhook architecture the skill automates, without requiring the viewer to
have the plugin installed or write a line of code first.

---
**GATE P — signed:** ______________________  (human)
