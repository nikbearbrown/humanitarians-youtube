# Checking a Pitch Deck Before It Goes Out. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `anthropics/financial-services/youtube/claude-liam-ib-check-deck`).*
*Register: **Plain**. 7 beats, matching the source's beat count (B00–B06 equivalent: B00, B01, B02, B03, BVDT, BHTF, BOUT). Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes checking a deck before sending it just means running a spellcheck. It doesn't. The real risk is numbers that stop matching across slides. Here's what an actual check catches." | Writer types "Can Claude / spellcheck my / pitch deck / before I send it?"; "spellcheck" hesitates and corrects to "check" |
| B01 | 1 anatomy | This kind of check is built from something called a skill — a folder Claude reads before it works. Inside is one file, written in plain language, that spells out exactly what to look for. Claude reads the file, then follows it. The file is the whole program. | a folder opens to reveal SKILL.md (highlighted), references/, scripts/ |
| B02 | 2 mechanism — pipeline | The steps run in order: read the file, work through each step exactly as written, then return the result. Nothing runs out of sequence unless a step itself says so. | three cards: Read SKILL.md -> Execute steps in order -> Return result |
| B03 | 3 constraint | For this skill, the checklist itself is four things: do the numbers agree across every slide, does the story match the underlying data, does the language hold up against IB standards, and is the formatting clean. Run it on the same deck twice and it flags the same four things — nothing outside that list gets checked. | four checklist rows filling in with checkmarks; a boundary line, faint field beyond captioned "nothing outside this list" |
| **BCRY** | **4 carry-out** | A skill like this doesn't proofread a deck — it reconciles it: the same four checks, every slide, every run, and nothing outside that checklist gets caught. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Ask Claude: check this pitch deck for four things — numbers that don't match across slides, claims that don't match the underlying data, language that doesn't fit the audience it's going to, and any formatting that's inconsistent. List exactly what to fix before it goes out. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Checking a Pitch Deck Before It Goes Out. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-liam-ib-check-deck`, Teardown, already rendered) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Claude, Ib Check Deck." — a skill-teardown title | reframed as an actually-askable question: what does checking a deck with Claude mean |
| Facts | `ib-check-deck` is an IB pitch-deck quality checker; a skill = a folder Claude reads before acting; SKILL.md is the instruction set; execution is linear (read -> execute steps in order -> return); the check covers exactly four things — number consistency across slides, data-narrative alignment, language polish against IB standards, visual/formatting QC; the boundary is that only what the file specifies gets checked | unchanged |
| Beat count | 7 (B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro) | 7 (B00 writer, B01 anatomy, B02 mechanism, B03 constraint, BCRY carry-out, BHTF your turn, BOUT outro) |
| B00 | `ClaudeComposerAsk` cold open (Remotion "ask" card, Claude palette, "Hola, Liam" greeting) | `BrutalistHesitantWriter` (WRITER LAW), humanitarians palette; wrong guess made explicit ("spellcheck" -> "check") |
| Register | Teardown — B03 named itself "the Teardown moment" and graded the skill ("what it gets right… what it bites"); BVDT was framed as a "Verdict" card | Plain — B03 states the same four-check boundary as a fact, no grading language; BCRY states the mechanism as a carry-out sentence, not a verdict |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| B01–B03 skin | `SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` (Remotion cards, fixed Claude palette) | rebuilt as GRAPHIC (Manim) in the humanitarians palette, same teaching content, per hai-simple's established channel-skin practice |
| BVDT → BCRY | `ClaudeVerdictArtifact` ("Verdict" card, Claude palette, four-line recap) | `WantQuote` carry-out card, single compressed sentence |
| Close | `ClaudeTitleOutro`, `@NikBearBrown`, "Hola, Liam" skin | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| BHTF prompt | garbled truncated string ("I want to investment banking presentation quality checker. reviews a pitch deck or client-…") referencing a skill file the general viewer won't have installed | rewritten as a clean, genuinely runnable prompt that asks Claude directly to run the same four-part check — same teaching point, no dependency on a plugin skill file the viewer doesn't have |

No beat in the source is `ai-video-prompt`, pantry, or a human-drop slot — the source
was already all-Remotion (`ClaudeComposerAsk` × 2, three `SkillTeardown*` cards,
`ClaudeVerdictArtifact`, `ClaudeTitleOutro`) — so the NO-GENAI/NO-PANTRY LAW required
no substitution beyond the WRITER LAW and channel-skin row already require.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the wrong guess and the real risk before B01's anatomy or B02's pipeline |
| Wrong guess surfaced | B00 ("spellcheck" -> "check") |
| No design judgment | B03 states the four-check boundary as a fact ("nothing outside that list gets checked"), not a critique of the skill's design; BCRY states the mechanism, not a verdict on whether four checks is the right number |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that the skill grades deck quality.** It runs a fixed, four-part
  reconciliation checklist — it doesn't judge whether the pitch itself is good.
- **Not a claim that this replaces human review.** The source scoped the skill to
  "only what the file specifies"; this redo keeps that boundary as stated fact,
  not as a limitation to be argued with.
- **Not a verdict on whether four checks is the right set.** The source's B03
  graded the skill ("what it gets right… what it bites"); this redo removes that
  framing per Plain register and states the boundary without grading it.

## Handoff prompt (BHTF, read aloud)

> "Check this pitch deck for four things — numbers that don't match across
> slides, claims that don't match the underlying data, language that doesn't
> fit the audience it's going to, and any formatting that's inconsistent. List
> exactly what to fix before it goes out."

Why it's worth running: it's runnable on any deck the viewer already has open,
today, with no plugin or skill file required — the same four-part reconciliation
the source skill automates, made into a prompt anyone can paste.

---
**GATE P — signed:** ______________________  (human)
