# QUESTION — claude-tag-plugins--claude-liam-graphing

**Mode:** redo (`SUBJECT.json.mode == "redo"`).
**Source:** `anthropics/claude-tag-plugins/youtube/claude-liam-graphing/beat_sheet.json`
(Teardown register, 7 beats, `source_skill` field points at
`../anthropics/claude-tag-plugins/claude-tag-data-viz/skills/graphing/SKILL.md`).

## Source-file check

`../anthropics/claude-tag-plugins/claude-tag-data-viz/skills/graphing/SKILL.md`
does **not** exist on this machine (checked directly and via `find` across the
whole `claude-tag-plugins` tree — only `graphing`'s YouTube folder is present
locally, the same situation as the `grafana-api` and `datadog-api` siblings).
This is not a missing-content problem: the source `beat_sheet.json` carries no
unfilled template placeholders. Every beat's `narration_text` is a complete,
specific, fully-written Teardown of the real graphing skill (the five
chartkit primitives, the three data helpers with explicit skip conditions,
the four-step workflow, the five judgement defaults, and the source's own
five-things-right / five-gaps list). The missing file just means this build
cannot cross-check the source sheet against the original `SKILL.md` text
directly — it reuses the source sheet's own stated facts as the record,
which is what the redo contract calls for regardless. `PEDAGOGY.md` in the
source folder independently confirms the same five gaps.

## The question, translated for a newcomer

The source is written for an audience that already knows what a Claude Skill
is and wants a teardown of one specific skill's charting quirks.
`hai-simple`'s audience is a newcomer to Claude. The redo contract requires
keeping the source's question, facts, and body argument — so the question is
generalized to what a newcomer is actually asking when they see Claude
produce a well-designed chart on the first try (the same generalization
pattern used for the `grafana-api`/`datadog-api` siblings, since all three
sources are Claude-plugin skill teardowns answering the identical underlying
question):

> **Does Claude already know how to make a good chart, or does something
> have to tell it what to check?**

The wrong guess a newcomer makes: that good chart design — the right chart
type, readable colors, a title that says something — is innate taste Claude
already has. The correction: Claude is *told* what to check, by a kit it
reads before drawing, and that kit is a set of judgement defaults with
permission to deviate, not a style it already possessed.

## What carries over from the source (facts, unchanged)

- Five chartkit primitives: `theme()` (colors derived from background
  luminance — a dark background produces a correct dark chart automatically),
  `palette()` (n colors from a base hex, a cycled list, or series defaults),
  `finish()` (title/subtitle/provenance frame), `save()` (PNG/SVG), and
  `write_html()` (inlines React + Recharts from a local directory — opens
  offline, no CDN).
- Three data helpers, each with an explicit skip condition: `zero_fill_days`
  (skip when zeros would misrepresent sparse sampling), `rolling_mean`
  (trailing, not centered — early points average whatever exists so far),
  `log_floor` (lower bound for bars on log-scale axes).
- The four-step workflow: look at the data and decide what it deserves →
  infer colors from context (tailwind config, CSS variables, brand
  guidelines, semantic meaning) → write the script → render and look at the
  result before handing it over.
- Five judgement defaults with explicit permission to deviate: rotate labels
  only on collision, cap bar width for few categories, label bars with values
  under ~12 categories, rank categorical bars unless a natural order exists,
  legend only for multiple series, title states what the chart shows (not
  the chart type or column name), annotate only what matters.
- Real, documented gaps in how legible the skill makes its own traps: the
  absolute-path requirement for `sys.path` is documented but the examples
  write it as a literal `/path/to/graphing/scripts`, easy to copy verbatim;
  `GRID` and `ACCENT` in the interactive HTML template are literal
  placeholder strings, not variables, and must be substituted by hand or the
  chart renders with no grid and a string as its stroke; "render and look"
  names four criteria in one sentence with no rubric for what passes;
  `rolling_mean`'s edge behavior for windows smaller than the window size is
  one phrase ("average what exists so far"); the smoke test only confirms a
  non-empty PNG, not `theme()`/`palette()`/`finish()` individually — not a
  claim that the skill is poorly built overall.

## What changes (register, per the redo contract)

- **Teardown → Plain.** The source's `B05` beat and its component
  (`GraphingTell`) are built around an explicit "what it gets right / where
  it bites" verdict frame (`GETS_RIGHT`/`BITES` arrays are hardcoded inside
  the component's JSX, not props), and the source's `BVDT` beat is a
  `ClaudeVerdictArtifact` card literally titled "Verdict." Both are a
  design-quality judgment on the skill's documentation — exactly what Plain
  drops, and exactly the same defect shape as the `grafana-api`/`datadog-api`
  siblings' `*Tell`/`BVDT` pairs. This build keeps `B01` (`GraphingAnatomy`)
  and `B02` (`GraphingDesign`) reused verbatim — their narration and their
  components' fixed row content were already descriptive, not evaluative —
  but replaces the B05/BVDT pair with a single **both-directions** beat
  (`MedhavyTwoColumnCard`, prop-driven, no baked-in verdict framing) stating
  the same underlying facts as two directions (documented plainly / easy to
  miss) rather than a grade, and a plain carry-out sentence (`WantQuote`)
  instead of a verdict card.
- **Cold open:** source's `ClaudeComposerAsk` → `BrutalistHesitantWriter`
  (WRITER LAW).
- **Outro:** source's single `ClaudeTitleOutro` → the fixed hai-simple
  `OutroSeries` + `OutroCTA` split, Humanitarians AI skin.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
