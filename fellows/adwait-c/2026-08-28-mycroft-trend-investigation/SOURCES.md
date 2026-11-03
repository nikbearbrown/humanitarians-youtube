# SOURCES — Weekly work video

## Primary sources — the artifacts, not the summary

**1. `trend.py`** — `projects/Mycroft-Finance-Investigator/mycroft_finance_investigator/trend.py`
in `nikbearbrown/mycroft`, PR #17, branch `codex/mycroft-finance-investigator`.

- **B05** shows ten lines of `_load_run()` — the tamper check — extracted with
  `inspect.getsource()` and dedented only. No lines added, removed or reordered.
- The "fifteen refusal paths" figure is `inspect.getsource(trend._load_run).count(
  'raise TrendError')` → **15**. The module as a whole has 30; the narration scopes the claim
  to the loader.
- Module docstring, quoted here because it is the video's thesis in the author's own words:
  *"The comparison describes historical movements and recurring material variance categories.
  It does not forecast, infer business causes, or recommend action."*

**2. The generated report** —
`reports/generated/mycroft-finance-investigator-trend-week35.md`.

Both on-screen tables are copied from it:

- **B03** — Historical EBITDA. Actual 261,000.00 → 230,000.00 → 265,000.00; change −31,000.00
  then +35,000.00; movement `FIRST_PERIOD` / `DETERIORATED` / `IMPROVED`.
- **B07** — Category Pattern. revenue, cogs, opex adverse in 3 periods → `Recurring adverse:
  YES`; payroll +8,000 / +20,000 / +10,000, 0 adverse periods → `NO`.

Report header carries the classification `HISTORICAL_COMPARISON_NOT_FORECAST`, materiality
`10000.00 (DEMO_UNAPPROVED)`, and `Human gate: OPEN`. The "Current Explanation — Owner
Required" section reads *"Intentionally blank. Recurrence does not establish why a variance
occurred."*

**3. PR #17** — `https://github.com/nikbearbrown/mycroft/pull/17`. Source of the 49-passing-
test figure, which is attributed to the PR's recorded verification run rather than re-run for
this video (see FACTCHECK row 8).

## Why the report and not the PR description

The PR summary and the generated report agree on every figure used here — but the report is
what the code actually emitted, so it is the artifact of record. Where a summary and an
output could ever disagree, the output wins.

## What is synthetic, and where it is said

The finance data is a synthetic sample (`Northstar Software Sample`), the recipe is `DRAFT`,
and the materiality threshold is an unapproved demo fixture. All three are stated on screen —
in B09 and again in the verdict card — rather than buried in a disclaimer.

## Toolkit provenance

Built with `brutalist.art` (`ai-explainer`), Kokoro `am_onyx`, cost $0.00. Patterns:
`ClaudeComposerAsk`, `ClaudeScienceLayerStack`, `ClaudeScienceSourceFlow`, `ClaudeWindow`,
`CwcConceptCard`, `ClaudeCodeBeat`, `ClaudeScienceChipGrid`, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`. No new component; no retint.
