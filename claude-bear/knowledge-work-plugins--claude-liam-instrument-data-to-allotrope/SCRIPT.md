# Your Lab Data Gets Converted, Not Read. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of
`anthropics/knowledge-work-plugins/youtube/claude-liam-instrument-data-to-allotrope`).*
*Register: **Plain**. 7 beats, matching the source's beat count (B00, B01, B02,
B03, BVDT, BHTF, BOUT). Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes this skill reads their lab data — understands it, judges it, the way a scientist would. It doesn't. It converts it, file by file, into one exact standard format." | Writer types "Can Claude / read my instrument / files for me?"; "read" hesitates and corrects to "convert" |
| B01 | 1 anatomy | This conversion runs on something called a skill — a folder Claude reads before it works. Inside sit five files: a license, a requirements list, two supporting folders, and one instruction file, SKILL.md, that spells out exactly how a lab file becomes a standard record. Claude reads it, then follows it. | a folder opens to reveal SKILL.md (highlighted), references/, scripts/ |
| B02 | 2 mechanism — pipeline | The steps run in order: read the file, work through each step exactly as written, then return the result. Nothing runs out of sequence unless a step itself says so. | three cards: Read SKILL.md -> Execute steps in order -> Return result |
| B03 | 3 constraint | For this skill there's one job: turn a lab instrument's output — PDF, CSV, Excel, or plain text — into one of two standard shapes: full Allotrope JSON, or a flattened CSV you can import anywhere. It figures out which instrument produced the file on its own. Ask it to interpret results or flag something scientifically odd, and there's no step written for that. | input formats fill in, arrow to two output shapes; boundary line, "no interpretation past this line" |
| **BCRY** | **4 carry-out** | This skill doesn't interpret your lab results — it detects the instrument and converts the file into one exact standard shape, the same way every time. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Ask Claude: I have a plain CSV export from a lab instrument, with columns like sample ID, measurement, units, and timestamp. Convert each row into one clean JSON record with consistent field names and ISO-format timestamps, and tell me the schema you used. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Your Lab Data Gets Converted, Not Read. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-liam-instrument-data-to-allotrope`, Teardown, already rendered) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Claude, Instrument Data To Allotrope." — a raw skill-invocation title | reframed as an actually-askable question: does the skill understand lab results, or just reformat the file |
| Facts | converts laboratory instrument output files (PDF, CSV, Excel, TXT) to Allotrope Simple Model (ASM) JSON or flattened 2D CSV; auto-detects instrument type; outputs full ASM JSON, flattened CSV, and exportable Python parser code; used to standardize instrument data for LIMS systems, data lakes, downstream analysis; a skill = a folder Claude reads before acting (LICENSE.txt, requirements.txt, SKILL.md, references/, scripts/ — 5 files, SKILL.md is the instruction set); execution is linear (read -> execute steps in order -> return); same input -> same output every run; limit is only what the file specifies | unchanged |
| Beat count | 7 (B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro) | 7 (B00 writer, B01 anatomy, B02 mechanism, B03 constraint, BCRY carry-out, BHTF your turn, BOUT outro) |
| B00 | `ClaudeComposerAsk` cold open (Remotion "ask" card, Claude palette, "Hola, Liam" greeting, ran the skill live) | `BrutalistHesitantWriter` (WRITER LAW), humanitarians palette; wrong guess made explicit ("read" -> "convert") |
| Register | Teardown — B03 named itself "the Teardown moment" and graded the skill ("what it gets right… what it bites"); BVDT was framed as a "Verdict" card | Plain — B03 states the same input/output boundary as a fact, no grading language; BCRY states the mechanism as a carry-out sentence, not a verdict |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| B01–B03 skin | `SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` (Remotion cards, fixed Claude palette) | rebuilt as GRAPHIC (Manim) in the humanitarians palette, same teaching content, per hai-simple's established channel-skin practice (matches the `knowledge-work-plugins--claude-liam-brief` sibling) |
| BVDT → BCRY | `ClaudeVerdictArtifact` ("Verdict" card, Claude palette, four-line recap) | `WantQuote` carry-out card, single compressed sentence |
| Close | `ClaudeTitleOutro`, `@NikBearBrown`, no subline | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| BHTF prompt | a live run of the actual skill against a real lab file — the general viewer doesn't have the skill installed or a matching source file | rewritten as a clean, genuinely runnable prompt: any messy instrument-style CSV export, converted to structured JSON — same teaching point (structured conversion, not interpretation), no dependency on the plugin |

No beat in the source is `ai-video-prompt`, pantry, or a human-drop slot — the
source was already all-Remotion (`ClaudeComposerAsk` x2, three `SkillTeardown*`
cards, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`) — so the NO-GENAI/NO-PANTRY
LAW required no substitution beyond the WRITER LAW and channel-skin row already
require.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the wrong guess and the real stakes before B01's anatomy or B02's pipeline |
| Wrong guess surfaced | B00 ("read" -> "convert") |
| No design judgment | B03 states the input/output boundary as a fact ("no step written for that"), not a critique of the skill's design; BCRY states the mechanism, not a verdict on whether the skill should interpret data |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that the skill performs any scientific judgment.** It never claims to
  flag anomalies, validate results, or assess data quality — B03 states plainly
  that interpretation is outside its spec.
- **Not a claim that auto-detection is perfect.** The source doesn't qualify
  the auto-detect claim, so this redo states it as the source did — a stated
  capability, not a guarantee reel or accuracy figure invented for effect.
- **Not a verdict on whether interpretation *should* be in scope.** The source's
  B03 graded the skill ("what it gets right… what it bites"); this redo removes
  that framing per Plain register and states the boundary without grading it.

## Handoff prompt (BHTF, read aloud)

> "I have a plain CSV export from a lab instrument, with columns like sample ID,
> measurement, units, and timestamp. Convert each row into one clean JSON record
> with consistent field names and ISO-format timestamps, and tell me the schema
> you used."

Why it's worth running: it's runnable today, on any messy tabular export already
sitting on the viewer's machine, with no plugin or skill file required — the same
detect-and-convert mechanism the source skill automates, made into a prompt
anyone can paste.

---
**GATE P — signed:** ______________________  (human)
