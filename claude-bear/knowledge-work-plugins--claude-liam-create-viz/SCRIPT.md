# Create-Viz Isn't About Making It Pretty. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-create-viz`).*
*Register: **Plain**. 7 beats, matching the source's beat count (B00, B01, B02, B03, BVDT, BHTF, BOUT). Carry-out written first (CARRY-OUT.md, GATE C).*

**Source note:** the source sheet's own narration was truncated mid-thought
in its design-tell and handoff beats (B03 cut the skill description short as
`"Use when turning query results or a DataFrame."`; BHTF broke off mid-word
as `"use when turning query re."`) — the same batch-build defect the sibling
reel `knowledge-work-plugins--claude-liam-content-strategy` found and worked
around, and its `source_skill` path is not present in this local tree. The
real facts below were re-sourced from the actual public file,
`anthropics/knowledge-work-plugins/data/skills/create-viz/SKILL.md` on
`github.com/anthropics/knowledge-work-plugins` — no fact here is invented.

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes this skill's whole job is making a chart look pretty. It isn't — it's a decision procedure: which chart type fits the data, and rules that keep the chart honest, before anything gets styled." | Writer types "Claude, make my chart pretty."; "pretty" hesitates and corrects to "honest" |
| B01 | 1 anatomy | This kind of work runs on something called a skill — a folder Claude reads before it acts. Inside, one file spells out how a query result or a pasted table becomes a chart: read the request, load the data, pick a chart type, write the code, then save and hand it back. The file is the whole program. | a folder opens to reveal SKILL.md (highlighted), reference contents |
| B02 | 2 mechanism — chart-type table | Before any styling, it matches chart to relationship: a trend over time gets a line, a comparison across categories gets a bar, a part of a whole gets a stacked bar, a distribution gets a histogram, two variables that move together get a scatter plot. The type comes from what the data is doing, not from what looks nice. | a table pairing data relationships to chart types, filling in one row at a time |
| B03 | 3 constraint — break the wrong guess | And it won't style around the truth. Bar charts have to start at zero. Axis breaks can't hide the size of a change. Colors have to be readable by someone colorblind, and they mean something — they don't just decorate. A title has to state the actual finding, not just name the numbers. Pretty was never the first requirement; honest was. | a bar chart with its baseline forced to zero; a colorblind-safe palette swatch; a title that states a finding, not a metric |
| **BCRY** | **4 carry-out** | Create-viz doesn't start by making a chart pretty — it starts by matching the chart type to what the data actually shows. Style comes after accuracy, never instead of it. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Here's some made-up monthly revenue for six months. Before you make this pretty, tell me what chart type it calls for and why, then build it with the axis kept honest. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Create-Viz Isn't About Making It Pretty. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-liam-create-viz`, Teardown, already rendered) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Claude, Create Viz." — a skill-teardown title, its own narration truncated mid-thought in B03 and mid-word in BHTF | reframed as an actually-askable question: does create-viz mean Claude makes your chart pretty, or something else |
| Facts | re-sourced from the real public SKILL.md (source sheet's own facts were incomplete/truncated): reads request (data source, chart type, purpose, audience) -> loads data into a DataFrame -> picks chart type from a fixed relationship table (trend->line, comparison->bar, part-to-whole->stacked/area, distribution->histogram/box, correlation->scatter, geographic->choropleth, ranking->horizontal bar, flow->Sankey, matrix->heatmap) -> writes matplotlib+seaborn (default, static) or plotly (interactive, on request) -> applies accuracy rules (zero-baseline bars, no hidden axis breaks, colorblind-safe meaningful color, insight-stating titles, stripped chart junk) -> saves PNG at 150 DPI, hands back code, suggests variations | unchanged (now complete, since the source's own copy was truncated) |
| Beat count | 7 (B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro) | 7 (B00 writer, B01 anatomy, B02 mechanism, B03 constraint, BCRY carry-out, BHTF your turn, BOUT outro) |
| B00 | `ClaudeComposerAsk` cold open (Remotion "ask" card, Claude palette, "Hola, Liam" greeting) | `BrutalistHesitantWriter` (WRITER LAW), humanitarians palette; wrong guess made explicit ("make my chart pretty" -> "make my chart honest") |
| Register | Teardown — B03 named itself "the Teardown moment" and graded the skill ("What it gets right… What it bites"); BVDT was framed as a "Verdict" card | Plain — B03 states the same accuracy constraints as fact, no grading language; BCRY states the mechanism as a carry-out sentence, not a verdict |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| B01–B03 skin | `SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` (Remotion cards, fixed Claude palette) | rebuilt as GRAPHIC (Manim) in the humanitarians palette, same teaching content, per hai-simple's established channel-skin practice |
| BVDT -> BCRY | `ClaudeVerdictArtifact` ("Verdict" card, Claude palette, four-line recap) | `WantQuote` carry-out card, single compressed sentence |
| Close | `ClaudeTitleOutro`, `@NikBearBrown`, "Hola, Liam" skin | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| BHTF prompt | broken template string (`"I want to create publication-quality visualizations with python. use when turning query re. Read the create-viz skill..."`) referencing a skill file and a connected data warehouse the general viewer won't have | rewritten as a clean, genuinely runnable prompt: paste six made-up monthly numbers, ask Claude to name the chart type and reasoning before styling, and keep the axis honest — same teaching point, no dependency on a plugin skill or a connected data source |

No beat in the source is `ai-video-prompt`, pantry, or a human-drop slot — the source
was already all-Remotion (`ClaudeComposerAsk` x2, three `SkillTeardown*` cards,
`ClaudeVerdictArtifact`, `ClaudeTitleOutro`) — so the NO-GENAI/NO-PANTRY LAW required
no substitution beyond the WRITER LAW and channel-skin row already require.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the wrong guess and the real stakes before B01's anatomy or B02's chart-type table |
| Wrong guess surfaced *and falsified by a case* | B00 ("make my chart pretty" -> "make my chart honest"); B03 falsifies it with concrete cases — zero-baseline bars, undisclosed axis breaks refused, colorblind-safe color required |
| No design judgment | B03 states the accuracy constraints as facts ("bar charts have to start at zero"), not a critique of the skill's design; BCRY states the mechanism, not a verdict on whether the constraint is a good idea |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that style never matters.** The skill still applies typography,
  color, and layout practice (Section 5 of the real SKILL.md) — the claim
  here is about *order*: chart-type selection and accuracy constraints come
  first, style choices are layered on afterward, not that style is absent.
- **Not a claim that this is the only correct chart-type mapping in
  general.** The source scoped the skill to its own fixed table (trend ->
  line, comparison -> bar, etc.); this redo keeps that table as the skill's
  stated behavior, not as a universal visualization law to argue with.
- **Not a verdict on whether matplotlib/seaborn-by-default, plotly-on-request
  is the right design.** The source's B03 graded the skill ("what it gets
  right… what it bites"); this redo removes that framing per Plain register
  and states the default/interactive split without grading it.

## Handoff prompt (BHTF, read aloud)

> "Here's some made-up monthly revenue for the last six months: Jan 12000,
> Feb 15000, Mar 11000, Apr 18000, May 21000, Jun 19000. Before you make this
> pretty, tell me what chart type this data calls for and why, then build it
> with the axis kept honest."

Why it's worth running: it puts the reel's whole claim to a direct test —
paste six made-up numbers, and check whether Claude actually leads with the
chart-type reasoning and an honest axis instead of jumping straight to
styling.

---
**GATE P — signed:** ______________________  (human)
