# The Skill Doesn't Already Know Your Data. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of
`anthropics/knowledge-work-plugins/youtube/claude-liam-data-context-extractor`).*
*Register: **Plain**. 7 beats, matching the source's beat count (B00, B01,
B02, B03, BVDT, BHTF, BOUT). Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no
generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes Claude already reads their company's data automatically. It doesn't. It reads a file — one you write once, that spells out your data's definitions — and follows that instead." | Writer types "Does Claude / read my company's / data / automatically?"; "automatically" hesitates and corrects to "once I write it down" |
| B01 | 1 anatomy | This skill is called data-context-extractor. Like every skill, it's a folder Claude reads before it works, and inside is one file, written in plain language, that spells out the job: generate or improve a data-analysis skill built around your company's own data. Claude reads that file, then follows it. | a folder opens to reveal SKILL.md (highlighted), references/, scripts/ |
| B02 | 2 mechanism — pipeline | The steps run in order: read the file, work through each step exactly as written, then return the result. Nothing runs out of sequence unless a step itself says so. | three cards: Read SKILL.md -> Execute steps in order -> Return result |
| B03 | 3 constraint | What comes out is a skill built around one company's own definitions — not a general-purpose one. Feed it data or questions outside the context it was given, and there's no fallback: it still returns the same output for the same input, but only for what the file actually specifies. | one company's definitions filling a file; a boundary line, faint field beyond captioned "outside the file's context" |
| **BCRY** | **4 carry-out** | It doesn't make Claude already know your data — it writes your data's context into a skill file, once, so every analysis after that uses your definitions instead of a guess. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Give Claude a quick rundown of your own data — what your key tables and columns actually mean — and ask it to turn that into a written skill file, so every future analysis uses those exact definitions, not a guess. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | The Skill Doesn't Already Know Your Data. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-liam-data-context-extractor`, Teardown, already rendered) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Claude, Data Context Extractor." — a skill-teardown title | reframed as an actually-askable question: does Claude already know your data, or does something have to teach it first |
| Source defect | four beats (B00, B03, BVDT, BHTF) each carry a template slot for the skill's one-line description that was never filled in — it reads as a bare `>`. The one confirmed fragment (not a placeholder) is "Generate or improve a company-specific data analysis skill by" | carried forward as-is; the missing completion is NOT invented, and no fabricated use-case list is added (unlike `build-dashboard`'s source, which had a real enumerated list to preserve, this source has none on record) |
| Facts | a skill = a folder Claude reads before acting; SKILL.md is the instruction set; execution is linear (read -> execute steps in order -> return); the boundary is that only what the file specifies gets covered, same input same output every run; the skill's confirmed job is to generate or improve a company-specific data-analysis skill | unchanged |
| Beat count | 7 (B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro) | 7 (B00 writer, B01 anatomy, B02 mechanism, B03 constraint, BCRY carry-out, BHTF your turn, BOUT outro) |
| B00 | `ClaudeComposerAsk` cold open (Remotion "ask" card, Claude palette, "Hola, Liam" greeting) | `BrutalistHesitantWriter` (WRITER LAW), humanitarians palette; wrong guess made explicit ("automatically" -> "once I write it down") |
| Register | Teardown — B03 named itself "the Teardown moment" and graded the skill ("what it gets right… what it bites"); BVDT was framed as a "Verdict" card | Plain — B03 states the same definitions-only boundary as a fact, no grading language; BCRY states the mechanism as a carry-out sentence, not a verdict |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| B01–B03 skin | `SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` (Remotion cards, fixed Claude palette) | rebuilt as GRAPHIC (Manim) in the humanitarians palette, same teaching content, per hai-simple's established channel-skin practice |
| BVDT → BCRY | `ClaudeVerdictArtifact` ("Verdict" card, Claude palette, four-line recap, itself carrying the broken `>` fragment) | `WantQuote` carry-out card, single compressed sentence, no broken fragment |
| Close | `ClaudeTitleOutro`, `@NikBearBrown`, "Hola, Liam" skin | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| BHTF prompt | referenced the internal `data-context-extractor` skill file by name and the broken `>` fragment mid-sentence ("I want to >. Read the data-context-extractor skill...") | rewritten as a clean, genuinely runnable prompt: hand Claude a plain rundown of your own data and ask for a written skill file back — no dependency on a plugin skill file the viewer doesn't have |

No beat in the source is `ai-video-prompt`, pantry, or a human-drop slot —
the source was already all-Remotion (`ClaudeComposerAsk` × 2, three
`SkillTeardown*` cards, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`) — so
the NO-GENAI/NO-PANTRY LAW required no substitution beyond the WRITER LAW
and channel-skin row already require.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the wrong guess and the real stakes before B01's anatomy or B02's pipeline |
| Wrong guess surfaced | B00 ("automatically" -> "once I write it down") |
| No design judgment | B03 states the definitions-only boundary as a fact ("nothing outside the file's context"), not a critique of the skill's design; BCRY states the mechanism, not a verdict |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that Claude reads a live, connected database.** The artifact is a
  written file, produced once from whatever data context it's given; no
  claim of a live database connection or a continuously updating source is
  made anywhere in this reel.
- **Not a specific list of use cases.** The source's own description of
  what "by ___" (the method) means was never filled in — this redo does not
  invent one. It states only the confirmed job ("generate or improve a
  company-specific data-analysis skill") and the generic skill mechanics
  that are true of every skill.
- **Not a verdict on whether the skill is well-scoped.** The source's B03
  graded the skill ("what it gets right… what it bites"); this redo removes
  that framing per Plain register and states the boundary without grading
  it.

## Handoff prompt (BHTF, read aloud)

> "Here's a quick rundown of my company's data — what my key tables and
> columns actually mean. Turn this into a written skill file so every
> future analysis of my data uses these exact definitions, not a guess."

Why it's worth running: it's runnable today, on whatever data definitions
the viewer already knows off the top of their head, with no plugin or
skill file required — the same one-time, written-context idea the source
skill automates, made into a prompt anyone can paste.

---
**GATE P — signed:** ______________________  (human)
