# The Legal Briefing Isn't a News Digest. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-brief`).*
*Register: **Plain**. 7 beats, matching the source's beat count (B00–B06 equivalent: B00, B01, B02, B03, BVDT, BHTF, BOUT). Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes a legal briefing means outside news, delivered each morning. It doesn't. It's a scan of your own email, calendar, and contracts — organized around what's actually happening in your work." | Writer types "Can Claude / email me / legal news / every morning?"; "news" hesitates and corrects to "briefings" |
| B01 | 1 anatomy | This kind of briefing is built from something called a skill — a folder Claude reads before it works. Inside is one file, written in plain language, that spells out exactly what counts as a briefing here. Claude reads the file, then follows it. The file is the whole program. | a folder opens to reveal SKILL.md (highlighted), references/, scripts/ |
| B02 | 2 mechanism — pipeline | The steps run in order: read the file, work through each step exactly as written, then return the result. Nothing runs out of sequence unless a step itself says so. | three cards: Read SKILL.md -> Execute steps in order -> Return result |
| B03 | 3 constraint | For this skill, there are exactly three situations it covers: a daily scan of legal-relevant items across your email, calendar, and contracts; research on one legal question across your own internal sources; and rapid context when something urgent breaks — a breach, a litigation threat, a regulatory inquiry. Ask it about anything else and there's no mode that covers it. | three mode rows filling in with checkmarks; a boundary line, faint field beyond captioned "nothing outside this list" |
| **BCRY** | **4 carry-out** | A legal briefing here isn't outside news — it's a scan of what's already in your own email, calendar, and contracts, run through whichever of three modes the moment calls for. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Ask Claude: look through my recent emails, calendar, and any contracts I have open, and give me a short briefing — what's legal-relevant this week, organized by how urgent it is. If anything looks like it needs fast attention, put that first. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | The Legal Briefing Isn't a News Digest. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-liam-brief`, Teardown, already rendered) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Claude, Brief." — a skill-teardown title | reframed as an actually-askable question: what does a "legal briefing" from Claude actually mean |
| Facts | `brief` generates contextual briefings for legal work; a skill = a folder Claude reads before acting; SKILL.md is the instruction set; execution is linear (read -> execute steps in order -> return); the skill covers exactly three situations — daily scan across email/calendar/contracts, topic research across internal sources, incident response for a developing situation (breach, litigation threat, regulatory inquiry); the boundary is that only what the file specifies gets covered, same input same output every run | unchanged |
| Beat count | 7 (B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro) | 7 (B00 writer, B01 anatomy, B02 mechanism, B03 constraint, BCRY carry-out, BHTF your turn, BOUT outro) |
| B00 | `ClaudeComposerAsk` cold open (Remotion "ask" card, Claude palette, "Hola, Liam" greeting) | `BrutalistHesitantWriter` (WRITER LAW), humanitarians palette; wrong guess made explicit ("news" -> "briefings") |
| Register | Teardown — B03 named itself "the Teardown moment" and graded the skill ("what it gets right… what it bites"); BVDT was framed as a "Verdict" card | Plain — B03 states the same three-mode boundary as a fact, no grading language; BCRY states the mechanism as a carry-out sentence, not a verdict |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| B01–B03 skin | `SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` (Remotion cards, fixed Claude palette) | rebuilt as GRAPHIC (Manim) in the humanitarians palette, same teaching content, per hai-simple's established channel-skin practice |
| BVDT → BCRY | `ClaudeVerdictArtifact` ("Verdict" card, Claude palette, four-line recap) | `WantQuote` carry-out card, single compressed sentence |
| Close | `ClaudeTitleOutro`, `@NikBearBrown`, "Hola, Liam" skin | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| BHTF prompt | garbled truncated string ("I want to generate contextual briefings for legal work — daily summary, topic research, or. Read the brief skill and walk me through what you will do before you do it.") referencing a skill file the general viewer won't have installed | rewritten as a clean, genuinely runnable prompt that asks Claude directly to run the same triage — same teaching point, no dependency on a plugin skill file the viewer doesn't have |

No beat in the source is `ai-video-prompt`, pantry, or a human-drop slot — the source
was already all-Remotion (`ClaudeComposerAsk` × 2, three `SkillTeardown*` cards,
`ClaudeVerdictArtifact`, `ClaudeTitleOutro`) — so the NO-GENAI/NO-PANTRY LAW required
no substitution beyond the WRITER LAW and channel-skin row already require.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the wrong guess and the real stakes before B01's anatomy or B02's pipeline |
| Wrong guess surfaced | B00 ("news" -> "briefings") |
| No design judgment | B03 states the three-mode boundary as a fact ("nothing outside this list gets checked"), not a critique of the skill's design; BCRY states the mechanism, not a verdict on whether three modes is the right number |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that the skill monitors outside legal news.** It never leaves the user's own
  materials — email, calendar, contracts, internal sources. No claim of a news feed,
  RSS pull, or web search is made anywhere in this reel.
- **Not a claim that this replaces a lawyer's judgment.** The source scoped the skill
  to "only what the file specifies"; this redo keeps that boundary as stated fact,
  not as a limitation to be argued with.
- **Not a verdict on whether three modes is the right set.** The source's B03 graded
  the skill ("what it gets right… what it bites"); this redo removes that framing
  per Plain register and states the boundary without grading it.

## Handoff prompt (BHTF, read aloud)

> "Look through my recent emails, calendar, and any contracts I have open, and give
> me a short briefing — what's legal-relevant this week, organized by how urgent it
> is. If anything looks like it needs fast attention, put that first."

Why it's worth running: it's runnable today, on whatever's already in the viewer's
own inbox and calendar, with no plugin or skill file required — the same
source-bound triage the source skill automates, made into a prompt anyone can paste.

---
**GATE P — signed:** ______________________  (human)
