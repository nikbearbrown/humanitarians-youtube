# The Dashboard Isn't a Live App. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of
`anthropics/knowledge-work-plugins/youtube/claude-liam-build-dashboard`).*
*Register: **Plain**. 7 beats, matching the source's beat count (B00, B01,
B02, B03, BVDT, BHTF, BOUT). Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no
generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes building a dashboard means a live app, running on a server somewhere. It doesn't. It's one self-contained file — charts, filters, and a table, already wired together, that opens straight in a browser." | Writer types "Can Claude / build me a / live dashboard / app?"; "app" hesitates and corrects to "file" |
| B01 | 1 anatomy | This dashboard is built from something called a skill — a folder Claude reads before it works. Inside is one file, written in plain language, that spells out exactly what counts as a dashboard here. Claude reads the file, then follows it. The file is the whole program. | a folder opens to reveal SKILL.md (highlighted), references/, scripts/ |
| B02 | 2 mechanism — pipeline | The steps run in order: read the file, work through each step exactly as written, then return the result. Nothing runs out of sequence unless a step itself says so. | three cards: Read SKILL.md -> Execute steps in order -> Return result |
| B03 | 3 constraint | It covers four situations: an executive overview with KPI cards, a query result turned into a shareable report, a team's monitoring snapshot, or several charts with filters bundled into one file. Ask for something outside that list, and there's no template for it. | four situation rows filling in with checkmarks; a boundary line, faint field beyond captioned "nothing outside this list" |
| **BCRY** | **4 carry-out** | A dashboard here isn't a live app — it's one self-contained HTML file, built once from your data, with its charts, filters, and table already wired together to open and share. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Take a table of data you already have, and ask Claude: build me one self-contained HTML dashboard from this — charts, filters, and a table — that I can just open in a browser and share, no server needed. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | The Dashboard Isn't a Live App. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-liam-build-dashboard`, Teardown, already rendered) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Claude, Build Dashboard." — a skill-teardown title | reframed as an actually-askable question: is building a dashboard a live app, or something else |
| Facts | `build-dashboard` builds an interactive HTML dashboard with charts, filters, and tables; a skill = a folder Claude reads before acting; SKILL.md is the instruction set; execution is linear (read -> execute steps in order -> return); the skill covers exactly four situations — executive overview with KPI cards, query results turned into a shareable self-contained report, team monitoring snapshot, multiple charts with filters in one browser-openable file; the boundary is that only what the file specifies gets covered, same input same output every run | unchanged |
| Beat count | 7 (B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro) | 7 (B00 writer, B01 anatomy, B02 mechanism, B03 constraint, BCRY carry-out, BHTF your turn, BOUT outro) |
| B00 | `ClaudeComposerAsk` cold open (Remotion "ask" card, Claude palette, "Hola, Liam" greeting) | `BrutalistHesitantWriter` (WRITER LAW), humanitarians palette; wrong guess made explicit ("app" -> "file") |
| Register | Teardown — B03 named itself "the Teardown moment" and graded the skill ("what it gets right… what it bites"); BVDT was framed as a "Verdict" card | Plain — B03 states the same four-situation boundary as a fact, no grading language; BCRY states the mechanism as a carry-out sentence, not a verdict |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| B01–B03 skin | `SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` (Remotion cards, fixed Claude palette) | rebuilt as GRAPHIC (Manim) in the humanitarians palette, same teaching content, per hai-simple's established channel-skin practice |
| BVDT → BCRY | `ClaudeVerdictArtifact` ("Verdict" card, Claude palette, four-line recap) | `WantQuote` carry-out card, single compressed sentence |
| Close | `ClaudeTitleOutro`, `@NikBearBrown`, "Hola, Liam" skin | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| BHTF prompt | referenced the internal `build-dashboard` skill file by name and truncated its own use-case list mid-sentence ("...an executive. Read the build-dashboard skill and walk me through...") | rewritten as a clean, genuinely runnable prompt that asks Claude directly to build a dashboard from data the viewer already has — same teaching point, no dependency on a plugin skill file the viewer doesn't have |

No beat in the source is `ai-video-prompt`, pantry, or a human-drop slot — the
source was already all-Remotion (`ClaudeComposerAsk` × 2, three
`SkillTeardown*` cards, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`) — so the
NO-GENAI/NO-PANTRY LAW required no substitution beyond the WRITER LAW and
channel-skin row already require.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the wrong guess and the real stakes before B01's anatomy or B02's pipeline |
| Wrong guess surfaced | B00 ("app" -> "file") |
| No design judgment | B03 states the four-situation boundary as a fact ("nothing outside this list gets a template"), not a critique of the skill's design; BCRY states the mechanism, not a verdict on whether four situations is the right number |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that the dashboard stays connected to a live data source.** The
  artifact is built once, from whatever data it's given at build time; no
  claim of a live database connection, a running server, or a refreshing
  feed is made anywhere in this reel.
- **Not a claim about hosting.** The source's own trigger conditions call
  the output "shareable" and "browser-openable" — this redo states that as
  the boundary, not as a limitation to be argued with.
- **Not a verdict on whether four situations is the right set.** The
  source's B03 graded the skill ("what it gets right… what it bites"); this
  redo removes that framing per Plain register and states the boundary
  without grading it.

## Handoff prompt (BHTF, read aloud)

> "Build me one self-contained HTML dashboard from this data — charts,
> filters, and a table — that I can just open in a browser and share. No
> server needed."

Why it's worth running: it's runnable today, on whatever table of data the
viewer already has sitting around, with no plugin or skill file required —
the same one-file artifact the source skill automates, made into a prompt
anyone can paste.

---
**GATE P — signed:** ______________________  (human)
