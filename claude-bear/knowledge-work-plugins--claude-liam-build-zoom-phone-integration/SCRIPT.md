# Claude Doesn't Answer Your Zoom Calls — It Builds the Integration. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of
`anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-phone-integration`).*
*Register: **Plain**. 7 beats, matching the source's beat count (B00, B01, B02,
B03, BVDT, BHTF, BOUT). Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes Claude can personally be the Zoom phone integration, taking calls itself. It can't. What it builds is the integration — the OAuth, webhooks, and dialer wiring that connect Zoom Phone to your CRM." | Writer types "Can Claude / be my / Zoom phone / integration?"; "be" hesitates and corrects to "build" |
| B01 | 1 anatomy | This one is built from something called a skill — a folder Claude reads before it works. Inside, one file spells out exactly what build-zoom-phone-integration covers: OAuth, the Phone APIs, webhooks, Smart Embed events, URI schemes, and CRM or CTI dialer wiring. Claude reads the file, then follows it. | a folder opens to reveal SKILL.md (highlighted), examples/, troubleshooting/ |
| B02 | 2 mechanism — pipeline | The steps run in order: read the file, work through each step exactly as written, then return the result. Nothing runs out of sequence unless a step itself says so. | three cards: Read SKILL.md -> Execute steps in order -> Return result |
| B03 | 3 constraint | This one isn't a single build — it's a reference file, used once a request already leans toward Zoom Phone. It covers seven areas: OAuth, the Phone APIs, webhooks, Smart Embed events, URI schemes, CRM or CTI dialer wiring, and call handling automation. Ask about anything outside that list and there's nothing here that covers it. | seven-item checklist filling in with checkmarks; a boundary line, faint field beyond captioned "nothing outside this list" |
| **BCRY** | **4 carry-out** | Build Zoom Phone Integration doesn't make Claude answer your calls — it makes Claude wire the connection: the OAuth, the webhooks, and the CRM or CTI dialer code that handles the call for you. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Ask Claude: I want my CRM to show customer info automatically when a call comes in through Zoom Phone. Walk me through the pieces I'd need — the OAuth connection, the incoming-call webhook, and the CTI dialer wiring — before writing any code. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude Doesn't Answer Your Zoom Calls — It Builds the Integration. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-liam-build-zoom-phone-integration`, Teardown, already rendered) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Claude, Build Zoom Phone Integration." — a skill-teardown title | reframed as an actually-askable question: does Claude itself pick up or route the call, or does it build the software that does |
| Facts | `build-zoom-phone-integration` is a reference skill for Zoom Phone, used after routing to a phone workflow, covering OAuth, Phone APIs, webhooks, Smart Embed events, URI schemes, CRM or CTI dialers, and call handling automation; a skill = a folder Claude reads before acting; SKILL.md is the instruction set; execution is linear (read -> execute steps in order -> return); same input, same output, every run | unchanged |
| Beat count | 7 (B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro) | 7 (B00 writer, B01 anatomy, B02 mechanism, B03 constraint, BCRY carry-out, BHTF your turn, BOUT outro) |
| B00 | `ClaudeComposerAsk` cold open (Remotion "ask" card, Claude palette, "Hola, Liam" greeting) | `BrutalistHesitantWriter` (WRITER LAW), humanitarians palette; wrong guess made explicit ("be" -> "build") |
| Register | Teardown — B03 named itself "the Teardown moment" and graded the skill ("what it gets right… what it bites"); BVDT was framed as a "Verdict" card | Plain — B03 states the same seven-area boundary as a fact, no grading language; BCRY states the mechanism as a carry-out sentence, not a verdict |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| B01–B03 skin | `SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` (Remotion cards, fixed Claude palette) | rebuilt as GRAPHIC (Manim) in the humanitarians palette, same teaching content, per hai-simple's established channel-skin practice |
| BVDT → BCRY | `ClaudeVerdictArtifact` ("Verdict" card, Claude palette, four-line recap) | `WantQuote` carry-out card, single compressed sentence |
| Close | `ClaudeTitleOutro`, `@NikBearBrown`, "Hola, Liam" skin | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| BHTF prompt | truncated/garbled string ("I want to reference skill for zoom phone. use after routing to a phone workflow when imple. Read the build-zoom-phone-integration skill and walk me through what you will do before you do it.") referencing a skill file the general viewer won't have installed | rewritten as a clean, genuinely runnable prompt that asks Claude directly to walk through the architecture — same teaching point, no dependency on a plugin skill file the viewer doesn't have |

No beat in the source is `ai-video-prompt`, pantry, or a human-drop slot — the
source was already all-Remotion (`ClaudeComposerAsk` × 2, three
`SkillTeardown*` cards, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`) — so the
NO-GENAI/NO-PANTRY LAW required no substitution beyond the WRITER LAW and
channel-skin row already require.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the wrong guess and the real stakes before B01's anatomy or B02's pipeline |
| Wrong guess surfaced | B00 ("be" -> "build") |
| No design judgment | B03 states the seven-area boundary as a fact ("nothing outside this list gets covered"), not a critique of the skill's design; BCRY states the mechanism, not a verdict on whether seven areas is the right scope |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that Claude itself picks up, routes, or sits on a live Zoom Phone
  call.** Every beat keeps the boundary that Claude writes and wires the
  integration's code; it never claims Claude personally handles a call.
- **Not a claim that this replaces a developer's own Zoom Phone / OAuth
  setup.** The source scoped the skill to "only what the file specifies";
  this redo keeps that boundary as stated fact, not as a limitation to be
  argued with.
- **Not a verdict on whether seven areas is the right scope for a reference
  skill.** The source's B03 graded the skill ("what it gets right… what it
  bites"); this redo removes that framing per Plain register and states the
  boundary without grading it.

## Handoff prompt (BHTF, read aloud)

> "I want my CRM to show customer info automatically when a call comes in
> through Zoom Phone. Walk me through the pieces I'd need — the OAuth
> connection, the incoming-call webhook, and the CTI dialer wiring — before
> writing any code."

Why it's worth running: it's a real, paste-ready Claude prompt that surfaces
the same three-piece architecture (OAuth, webhooks, CTI dialer) the skill
automates, without requiring the viewer to have the plugin installed or write
a line of code first.

---
**GATE P — signed:** ______________________  (human)
