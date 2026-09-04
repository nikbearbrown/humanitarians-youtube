# Drafting an Offer Isn't Just the Letter. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-draft-offer`).*
*Register: **Plain**. 7 beats, matching the source's beat count (B00, B01, B02, B03, BVDT, BHTF, BOUT). Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes drafting an offer means writing the congratulatory letter. It's more than that — it's the full comp package: base, equity, signing bonus, the letter, and guidance for the hiring manager." | Writer types "Can Claude / just write the / offer letter / for a hire?"; "letter" hesitates and corrects to "package" |
| B01 | 1 anatomy | This kind of drafting is built from something called a skill — a folder Claude reads before it works. Inside is one file, written in plain language, that spells out exactly what counts as a finished offer. Claude reads the file, then follows it. The file is the whole program. | a folder opens to reveal SKILL.md (highlighted), references/, scripts/ |
| B02 | 2 mechanism — pipeline | The steps run in order: read the file, work through each step exactly as written, then return the result. Nothing runs out of sequence unless a step itself says so. | three cards: Read SKILL.md -> Execute steps in order -> Return result |
| B03 | 3 constraint | For this skill, there are exactly three things it covers once a candidate is ready for an offer: assembling the total comp package — base, equity, signing bonus; writing the offer letter text itself; and prepping negotiation guidance for the hiring manager. Ask it about anything else and there's no mode that covers it. | three rows filling in with checkmarks; a boundary line, faint field beyond captioned "nothing outside this list" |
| **BCRY** | **4 carry-out** | Drafting an offer here isn't just the congratulatory letter — it's the full comp package, the letter itself, and negotiation guidance for the hiring manager, once a candidate's ready to hire. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Ask Claude: I'm hiring a software engineer at a hundred forty thousand dollar base. Help me draft a complete offer — the total comp package with base, equity, and signing bonus, the offer letter text itself, and negotiation talking points for the hiring manager. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Drafting an Offer Isn't Just the Letter. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-liam-draft-offer`, Teardown, already rendered) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Claude, Draft Offer." — a skill-teardown title | reframed as an actually-askable question: is drafting an offer just the letter, or more |
| Facts | `draft-offer` drafts an offer letter with comp details and terms; a skill = a folder Claude reads before acting; SKILL.md is the instruction set; execution is linear (read -> execute steps in order -> return); the skill covers exactly three things once a candidate is ready for an offer — assembling the total comp package (base, equity, signing bonus), writing the offer letter text itself, and prepping negotiation guidance for the hiring manager; the boundary is that only what the file specifies gets covered, same input same output every run | unchanged |
| Beat count | 7 (B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro) | 7 (B00 writer, B01 anatomy, B02 mechanism, B03 constraint, BCRY carry-out, BHTF your turn, BOUT outro) |
| B00 | `ClaudeComposerAsk` cold open (Remotion "ask" card, Claude palette, "Hola, Liam" greeting) | `BrutalistHesitantWriter` (WRITER LAW), humanitarians palette; wrong guess made explicit ("letter" -> "package") |
| Register | Teardown — B03 named itself "the Teardown moment" and graded the skill ("what it gets right… what it bites"); BVDT was framed as a "Verdict" card | Plain — B03 states the same three-part boundary as a fact, no grading language; BCRY states the mechanism as a carry-out sentence, not a verdict |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| B01–B03 skin | `SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` (Remotion cards, fixed Claude palette) | rebuilt as GRAPHIC (Manim) in the humanitarians palette, same teaching content, per hai-simple's established channel-skin practice |
| BVDT → BCRY | `ClaudeVerdictArtifact` ("Verdict" card, Claude palette, four-line recap) | `WantQuote` carry-out card, single compressed sentence |
| Close | `ClaudeTitleOutro`, `@NikBearBrown`, "Hola, Liam" skin | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| BHTF prompt | truncated string ("I want to draft an offer letter with comp details and terms. use when a candidat. Read the draft-offer skill and walk me through what you will do before you do it.") referencing a skill file the general viewer won't have installed | rewritten as a clean, genuinely runnable prompt that asks Claude directly to draft a comp package, letter, and negotiation notes for a concrete hypothetical hire — same teaching point, no dependency on a plugin skill file the viewer doesn't have |

No beat in the source is `ai-video-prompt`, pantry, or a human-drop slot — the source
was already all-Remotion (`ClaudeComposerAsk` × 2, three `SkillTeardown*` cards,
`ClaudeVerdictArtifact`, `ClaudeTitleOutro`) — so the NO-GENAI/NO-PANTRY LAW required
no substitution beyond the WRITER LAW and channel-skin row already require.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the wrong guess and the real stakes before B01's anatomy or B02's pipeline |
| Wrong guess surfaced | B00 ("letter" -> "package") |
| No design judgment | B03 states the three-part boundary as a fact ("nothing outside this list gets covered"), not a critique of the skill's design; BCRY states the mechanism, not a verdict on whether three parts is the right number |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that the skill negotiates directly with the candidate.** The source scoped
  negotiation guidance to the hiring manager, not the candidate; this redo keeps
  that boundary exactly as stated, with no expansion.
- **Not a claim that this replaces HR or legal review.** The source scoped the
  skill to "only what the file specifies"; this redo keeps that boundary as
  stated fact, not as a limitation to be argued with.
- **Not a verdict on whether three parts is the right set.** The source's B03
  named itself "the Teardown moment" and graded the skill ("what it gets right…
  what it bites"); this redo removes that framing per Plain register and states
  the boundary without grading it.

## Handoff prompt (BHTF, read aloud)

> "I'm hiring a software engineer at a $140,000 base. Help me draft a complete
> offer — the total comp package with base, equity, and signing bonus, the
> offer letter text itself, and negotiation talking points for the hiring
> manager."

Why it's worth running: it's paste-ready today even for a viewer who isn't
currently hiring — a concrete hypothetical that exercises all three parts of
the skill (comp package, letter, negotiation guidance) in one pass, with no
plugin or skill file required.

---
**GATE P — signed:** ______________________  (human)
