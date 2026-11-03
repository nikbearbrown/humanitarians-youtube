# Claude Doesn't Drop In a Chat Widget — It Wires the SDK. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-contact-center/web`).*
*Register: **Plain**. 7 beats, matching the source's beat count (B00, B01, B02, B03, BVDT, BHTF, BOUT).*
*Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes 'Contact Center, web' means Claude drops in a ready-made chat widget. It doesn't — it wires the Zoom Web SDK's chat, video, and campaign events into your own site." | Writer types "How do I add / a chat widget / to my / website?"; "widget" hesitates and corrects to "SDK" |
| B01 | 1 anatomy | A skill is a folder Claude reads before it works. This one is contact-center, web. Inside are six items: a RUNBOOK and a SKILL file, plus folders for concepts, examples, references, and troubleshooting. Claude reads the file, then follows it. | a folder opens to reveal SKILL.md (highlighted), RUNBOOK.md, and the four subfolders |
| B02 | 2 mechanism — pipeline | The steps run in order: read the file, work through each step exactly as written, then return the result. Nothing runs out of sequence unless a step itself says so. | three cards: Read SKILL.md -> Execute steps in order -> Return result |
| B03 | 3 constraint | contact-center/web is a specification written as an instruction set. Its job: the Zoom Contact Center Web SDK — chat, video, and campaign embeds, engagement event handling, app-context integrations, and Smart Embed postMessage workflows. Follow it, and the result repeats: same input, same output, every run. Ask for anything outside that list, and there's no mode that covers it. | four scope rows filling in with checkmarks; a boundary line, faint field beyond captioned "nothing outside this list" |
| **BCRY** | **4 carry-out** | Contact Center, web doesn't hand you a drop-in chat widget — it wires the Zoom Web SDK's chat, video, and campaign embeds into your own site through events, context, and postMessage, the same way every time. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Ask Claude: walk me through adding Zoom Contact Center's web chat to my site — engagement events, app context, and Smart Embed postMessage — before I write any code. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude Doesn't Drop In a Chat Widget — It Wires the SDK. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-liam-contact-center/web`, Teardown, already rendered) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Claude, Contact Center/web." — a skill-teardown title | reframed as an actually-askable question: does Claude drop in a ready-made chat widget, or does it wire the SDK's events into your own site |
| Facts | `contact-center/web` is a partner-built (Zoom) skill for the Zoom Contact Center SDK for Web — web chat/video/campaign embeds, engagement event handling, app-context integrations, Smart Embed postMessage workflows; a skill = a folder Claude reads before acting (6 items: RUNBOOK.md, SKILL.md, concepts/, examples/, references/, troubleshooting/); execution is linear (read -> execute steps in order -> return) | unchanged |
| Beat count | 7 (B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro) | 7 (B00 writer, B01 anatomy, B02 mechanism, B03 constraint, BCRY carry-out, BHTF your turn, BOUT outro) |
| B00 | `ClaudeComposerAsk` cold open (Remotion "ask" card, Claude palette, "Hola, Liam" greeting) | `BrutalistHesitantWriter` (WRITER LAW), humanitarians palette; wrong guess made explicit ("widget" -> "SDK") |
| Register | Teardown — B03 named itself "the Teardown moment" and graded the skill ("what it gets right… what it bites"); BVDT was framed as a "Verdict" card | Plain — B03 states the same scope boundary as a fact, no grading language; BCRY states the mechanism as a carry-out sentence, not a verdict |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| B01–B03 skin | `SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` (Remotion cards, fixed Claude palette) | rebuilt as GRAPHIC (Manim) in the humanitarians palette, same teaching content, per hai-simple's established channel-skin practice |
| BVDT → BCRY | `ClaudeVerdictArtifact` ("Verdict" card, Claude palette, four-line recap) | `WantQuote` carry-out card, single compressed sentence |
| Close | `ClaudeTitleOutro`, `@NikBearBrown`, "Hola, Liam" skin | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| BHTF prompt | truncated/garbled string ("I want to zoom contact center sdk for web. use for web chat/video/campaign embed. Read the contact-center/web skill and walk me through what you will do before you do it.") referencing a skill file the general viewer won't have installed | rewritten as a clean, genuinely runnable prompt that asks Claude directly to walk through the same scope (events, context, postMessage) — no dependency on a plugin skill file |

No beat in the source is `ai-video-prompt`, pantry, or a human-drop slot — the
source was already all-Remotion (`ClaudeComposerAsk` x2, three
`SkillTeardown*` cards, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`), so the
NO-GENAI/NO-PANTRY LAW required no substitution beyond the WRITER LAW and
channel-skin row already required.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the wrong guess and the real stakes before B01's anatomy or B02's pipeline |
| Wrong guess surfaced | B00 ("widget" -> "SDK") |
| No design judgment | B03 states the scope boundary as a fact ("nothing outside this list"), not a critique of the skill's design; BCRY states the mechanism, not a verdict on whether the scope is the right one |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that Claude renders a visible chat UI itself.** Every beat keeps the
  boundary that Claude wires the SDK's events, context, and postMessage
  plumbing into the viewer's own site code; it never claims Claude paints a
  finished chat window for you.
- **Not a claim that this replaces Zoom's own Contact Center product.** The
  source scoped the skill to the *Web SDK* specifically — chat/video/campaign
  embeds, engagement events, app-context, Smart Embed postMessage — and this
  redo keeps that exact scope as stated fact, no broader claim.
- **Not a verdict on whether four use-cases is the right scope.** The
  source's B03 graded the skill ("what it gets right… what it bites"); this
  redo removes that framing per Plain register and states the boundary
  without grading it.

## Handoff prompt (BHTF, read aloud)

> "Walk me through adding Zoom Contact Center's web chat to my site —
> engagement events, app context, and Smart Embed postMessage — before I
> write any code."

Why it's worth running: it's a real, paste-ready Claude prompt that surfaces
the same scope (events, app context, postMessage) the skill automates,
without requiring the viewer to have the plugin installed or write a line of
code first.

**Revision note:** the prompt was shortened from an earlier ~240-character
draft after Gate V caught a real defect — `ClaudeComposerAsk`'s composer
card clips command text to 3 visible lines (`overflow: hidden` on the input
area), and the longer draft silently truncated mid-sentence on screen
("...Walk me through the" with the rest never appearing) even though the
narration read the full text aloud. The same defect exists unnoticed in the
`knowledge-work-plugins--claude-liam-build-zoom-contact-center-app` sibling's
BHTF beat (verified by frame pull). Fixed here by shortening the on-screen
command AND its matching narration to ≤155 characters so the full prompt
is legible on screen; the sibling's defect was not in scope for this
build and is noted here for awareness, not fixed there.

---
**GATE P — signed:** ______________________  (human)
