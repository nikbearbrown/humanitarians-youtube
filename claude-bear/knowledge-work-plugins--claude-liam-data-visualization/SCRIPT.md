# Data Visualization Isn't About Making It Colorful. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-data-visualization`).*
*Register: **Plain**. 7 beats, matching the source's beat count (B00, B01, B02, B03, BVDT, BHTF, BOUT). Carry-out written first (CARRY-OUT.md, GATE C).*

**Source note:** the source sheet's own body narration is content-free
scaffolding (B01: "SKILL.md is the instruction set. 1 file total."; B02: a
generic 3-step "Read -> Execute -> Return" pipeline; B03: the skill's own
`description` field quoted and cut off mid-word, "Use when building ch.")
and its `source_skill` path is not present in this local tree. The real
facts below are re-sourced from the actual public file,
`anthropics/knowledge-work-plugins/data/skills/data-visualization/SKILL.md`
on `github.com/anthropics/knowledge-work-plugins` — no fact here is
invented. This is a distinct skill from the sibling reel
`knowledge-work-plugins--claude-liam-create-viz` (same family, redone
earlier the same day); to avoid retreading that reel's angle (chart-type
selection vs. an honest axis), this reel's wrong guess and body argument
are built around **color and accessibility** instead, which the real
`data-visualization` SKILL.md covers in depth and the `create-viz` reel did
not.

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes data visualization means picking bright colors. It isn't that — color has to encode something real, and the chart type comes first, chosen from what the data is actually doing." | Writer types "Claude, make my chart colorful."; "colorful" hesitates and corrects to "accessible" |
| B01 | 1 anatomy | This runs on a skill — a folder Claude reads before it acts. Inside, one file lays out how raw data becomes a chart: pick the chart type for the relationship in the data, write the plotting code, then apply the design and accessibility rules on top. The file is the whole program. | a folder opens to reveal SKILL.md (highlighted), reference contents |
| B02 | 2 mechanism — chart-type guide, both directions | The guide runs both ways. A ranking gets a horizontal bar, a composition over time gets a stacked area, many variables at once get a heatmap. And some charts are ruled out outright: pie charts, because people are bad at comparing angles; three-D charts, because they distort the data; dual axes, because they can imply a correlation that was never there. | a two-column list filling in: relationship -> chart type; then a second list of ruled-out charts, each struck through |
| B03 | 3 constraint — break the wrong guess | So color has to earn its place. One accent color carries the finding; everything else fades to grey. Red and green alone are out — about eight percent of men can't tell them apart — and every chart has to survive in black and white: a pattern, a label, a line style standing in for the color, never just decoration. | a chart where every color drains to grey except one accent bar; a red/green pair marked unreadable; the same chart redrawn with patterns instead of color |
| **BCRY** | **4 carry-out** | Data visualization doesn't start with a bright palette — it starts with the chart type the data's relationship calls for, and color only earns a place once it carries meaning. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Here's some made-up scores from a five-question customer survey, one to ten. Tell me what chart type this calls for, and pick colors that would still make sense to someone who's colorblind. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Data Visualization Isn't About Making It Colorful. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-liam-data-visualization`, Teardown, already rendered) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Claude, Data Visualization." — a skill-teardown title over generic template narration, never gets specific | reframed as an actually-askable question: does data visualization mean picking bright colors, or something else |
| Facts | re-sourced from the real public SKILL.md (source sheet's own facts were generic/template, never skill-specific): chart-selection-by-relationship table (trend->line, ranking->horizontal bar, composition-over-time->stacked area, many-variable correlation->heatmap, geographic->choropleth) -> explicit avoid list (pie charts, 3D charts, dual-axis charts, many-category stacked bars) -> design principles (color encodes the story, one accent + grey the rest, sequential/diverging/categorical palette rules) -> accuracy rules (bar charts start at zero, consistent scales, labeled axes) -> accessibility (never color alone, red/green fails ~8% of men, patterns/line-styles as backup, screen-reader alt text, accessibility checklist) | unchanged (now complete, since the source's own copy was generic scaffolding) |
| Beat count | 7 (B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro) | 7 (B00 writer, B01 anatomy, B02 mechanism, B03 constraint, BCRY carry-out, BHTF your turn, BOUT outro) |
| B00 | `ClaudeComposerAsk` cold open (Remotion "ask" card, Claude palette, "Hola, Liam" greeting) | `BrutalistHesitantWriter` (WRITER LAW), humanitarians palette; wrong guess made explicit ("make my chart colorful" -> "make my chart accessible") |
| Register | Teardown — B03 named itself "the Teardown moment" and graded the skill ("What it gets right… What it bites"); BVDT was framed as a "Verdict" card | Plain — B03 states the same accessibility/color constraints as fact, no grading language; BCRY states the order-of-operations as a carry-out sentence, not a verdict |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| B01–B03 skin | `SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` (Remotion cards, fixed Claude palette) | rebuilt as GRAPHIC (Manim) in the humanitarians palette, same teaching content, per hai-simple's established channel-skin practice |
| BVDT -> BCRY | `ClaudeVerdictArtifact` ("Verdict" card, Claude palette, four-line recap) | `WantQuote` carry-out card, single compressed sentence |
| Close | `ClaudeTitleOutro`, `@NikBearBrown`, "Hola, Liam" skin | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| BHTF prompt | broken template string referencing the skill file and a plotting library the general viewer would have to set up | rewritten as a clean, genuinely runnable prompt: paste five made-up survey scores, ask Claude to name the chart type and pick colorblind-safe colors — no dependency on a plugin skill or a connected data source |

No beat in the source is `ai-video-prompt`, pantry, or a human-drop slot —
the source was already all-Remotion (`ClaudeComposerAsk` x2, three
`SkillTeardown*` cards, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`) — so the
NO-GENAI/NO-PANTRY LAW required no substitution beyond the WRITER LAW and
channel-skin row it already mandates.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the wrong guess and the real stakes before B01's anatomy or B02's chart-type guide |
| Wrong guess surfaced *and falsified by a case* | B00 ("make my chart colorful" -> "make my chart accessible"); B03 falsifies it with a concrete case — red/green fails roughly 8% of men, so color alone can't be load-bearing |
| No design judgment | B02/B03 state the guide's rules as fact ("pie charts, because people are bad at comparing angles"), not a critique of whether the skill's rule set is well-chosen; BCRY states the mechanism's order, not a verdict |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that chart-type selection is unrelated to color.** The real skill
  treats both as part of one design-principles section; this reel sequences
  them (chart type, then color) because that is the order the skill's own
  guide and accuracy/accessibility sections apply in, not because they are
  unconnected steps.
- **Not a claim that every colorful chart is wrong.** The correction is
  "color has to earn its place by carrying meaning," not "never use color."
- **Not a verdict on whether the skill's specific avoid-list (pie, 3D,
  dual-axis) is the only correct rule set.** The source scoped the skill to
  its own stated guide; this redo states that guide as the skill's behavior,
  not as a universal design law to argue with.

## Handoff prompt (BHTF, read aloud)

> "Here's some made-up scores from a five-question customer survey, one to
> ten: Ease of use 8, Price 4, Support 7, Reliability 9, Design 5. Tell me
> what chart type this calls for, and pick colors that would still make
> sense to someone who's colorblind."

Why it's worth running: it tests the reel's whole claim directly — does
Claude lead with the chart-type reasoning (this is a ranking, not a trend)
and actually pick colorblind-safe colors, or default to whatever looks
nice.

---
**GATE P — signed:** ______________________  (human)
