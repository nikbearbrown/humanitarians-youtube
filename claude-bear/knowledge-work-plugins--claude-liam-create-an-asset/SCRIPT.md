# Creating An Asset Isn't One Generic Template. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-create-an-asset`).*
*Register: **Plain**. 7 beats, matching the source's beat count (B00, B01, B02, B03, BVDT, BHTF, BOUT). Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes this skill just designs a deck from nothing. It doesn't — it generates one of four sales asset types from your actual deal: landing pages, decks, one-pagers, workflow demos." | Writer types "Can Claude just design decks for me?"; "design" hesitates and corrects to "generate", "decks" hesitates and corrects to "assets" |
| B01 | 1 anatomy | This kind of asset-building runs on something called a skill — a folder Claude reads before it works. Inside are three files: a README, a quick reference, and the SKILL.md that spells out the process. Claude reads it, then follows it. The file is the whole program. | a folder opens to reveal SKILL.md (highlighted), README.md, QUICKREF.md |
| B02 | 2 mechanism — pipeline | The steps run in order: read the file, work through each step exactly as written — gather your deal context, generate the asset, then return it ready to share. Nothing runs out of sequence unless a step itself says so. | three cards: Read SKILL.md -> Gather context + generate -> Return asset |
| B03 | 3 constraint | For this skill, there are exactly four asset types it covers: landing pages, decks, one-pagers, and workflow demos — each one shaped by your deal context, not invented from scratch: your prospect, your audience, your goal. Ask for a fifth kind of asset and there's no format that covers it. | four format rows filling in with checkmarks; a boundary line, faint field beyond captioned "nothing outside this list" |
| **BCRY** | **4 carry-out** | Create-an-asset doesn't invent a generic deck from nothing — it builds one of four sales formats, shaped by your actual deal: your prospect, your audience, your goal. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Ask Claude: I'm pitching my landscaping business to a property manager who cares most about reliability and price. Write me a one-page sales asset: a headline, three bullets on why we fit their goal, and one call to action — built for that prospect, not a generic template. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Creating An Asset Isn't One Generic Template. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-liam-create-an-asset`, Teardown, already rendered) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Claude, Create An Asset." — a skill-teardown title | reframed as an actually-askable question: does creating an asset mean Claude invents a generic template, or something built from your specific deal |
| Facts | `create-an-asset` generates tailored sales assets across four types — landing pages, decks, one-pagers, workflow demos — from your deal context; describe your prospect, audience, and goal, get a polished, branded asset ready to share; a skill = a folder Claude reads before acting (three files: QUICKREF.md, README.md, SKILL.md); execution is linear (read -> execute steps in order -> return); the boundary is only what the file specifies gets covered, same input same output every run | unchanged |
| Beat count | 7 (B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro) | 7 (B00 writer, B01 anatomy, B02 mechanism, B03 constraint, BCRY carry-out, BHTF your turn, BOUT outro) |
| B00 | `ClaudeComposerAsk` cold open (Remotion "ask" card, Claude palette, "Hola, Liam" greeting) | `BrutalistHesitantWriter` (WRITER LAW), humanitarians palette; wrong guess made explicit ("design decks" -> "generate assets") |
| Register | Teardown — B03 named itself "the Teardown moment" and graded the skill ("what it gets right… what it bites"); BVDT was framed as a "Verdict" card | Plain — B03 states the same four-format boundary as a fact, no grading language; BCRY states the mechanism as a carry-out sentence, not a verdict |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| B01–B03 skin | `SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` (Remotion cards, fixed Claude palette) | rebuilt as GRAPHIC (Manim) in the humanitarians palette, same teaching content, per hai-simple's established channel-skin practice |
| BVDT -> BCRY | `ClaudeVerdictArtifact` ("Verdict" card, Claude palette, four-line recap) | `WantQuote` carry-out card, single compressed sentence |
| Close | `ClaudeTitleOutro`, `@NikBearBrown`, "Hola, Liam" skin | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| BHTF prompt | garbled truncated string ("I want to generate tailored sales assets (landing pages, decks, one-pagers, work. Read the create-an-asset skill and walk me through what you will do before you do it.") referencing a skill file the general viewer won't have installed | rewritten as a clean, genuinely runnable prompt that asks Claude directly to build a one-page sales asset for a concrete small-business deal — same teaching point (deal-specific output, not a generic template), no dependency on a plugin skill file the viewer doesn't have |

No beat in the source is `ai-video-prompt`, pantry, or a human-drop slot — the source
was already all-Remotion (`ClaudeComposerAsk` × 2, three `SkillTeardown*` cards,
`ClaudeVerdictArtifact`, `ClaudeTitleOutro`) — so the NO-GENAI/NO-PANTRY LAW required
no substitution beyond the WRITER LAW and channel-skin row already require.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the wrong guess and the real stakes before B01's anatomy or B02's pipeline |
| Wrong guess surfaced | B00 ("design decks from nothing" -> "generate assets from your deal") |
| No design judgment | B03 states the four-format boundary as a fact ("nothing outside this list gets covered"), not a critique of the skill's design; BCRY states the mechanism, not a verdict on whether four formats is the right number |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that the skill guesses at your deal on its own.** The skill's whole
  point is that it needs you to describe the prospect, audience, and goal —
  no claim is made that it infers deal context from nothing.
- **Not a claim that four is a limit on sales writing in general.** The
  source scoped the skill to "only what the file specifies"; this redo keeps
  that boundary as stated fact, not as a limitation to be argued with.
- **Not a verdict on whether four formats is the right set.** The source's B03
  graded the skill ("what it gets right… what it bites"); this redo removes
  that framing per Plain register and states the boundary without grading it.

## Handoff prompt (BHTF, read aloud)

> "I'm pitching my landscaping business to a property manager who cares
> most about reliability and price. Write me a one-page sales asset: a
> headline, three bullets on why we fit their goal, and one call to
> action — built for that prospect, not a generic template."

Why it's worth running: it puts the reel's whole claim to a direct test —
paste it with your own actual deal in place of the landscaping example, and
check whether the output actually reflects your prospect and goal, or reads
like a template with the names swapped in.

---
**GATE P — signed:** ______________________  (human)
