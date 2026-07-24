# PEDAGOGY — claude-liam-graphing

## Skill reviewed
`anthropics/claude-tag-plugins/claude-tag-data-viz/skills/graphing/SKILL.md`

## What learners will be able to do
- Use chartkit primitives (theme, palette, finish, save, write_html) in a matplotlib or Recharts chart script
- Follow the four-step process: look at data → infer colors → write script → render and look at result
- Apply judgement-not-flags defaults: chart type from data shape, ranked bars, labels for small datasets
- Use the three data helpers (zero_fill_days, rolling_mean, log_floor) correctly and know when to skip them
- Recognize the GRID/ACCENT placeholder substitution requirement in the interactive HTML template

## What makes this teachable
The "judgement, not flags" philosophy with explicit permission to deviate is the right framing for a charting tool. The four-step workflow (look → infer → write → look again) forces a render-and-verify loop rather than blind script execution. The data helpers address real gotchas (calendar gaps, rolling mean edge behavior, log scale) with precise remedies.

## Gaps the teardown surfaces
- /path/to/graphing/scripts must be an ABSOLUTE path — documented but easily missed when copying examples
- GRID and ACCENT are placeholder strings in the interactive HTML template, not variables — must be manually substituted
- "Render and look at the result" has no QC rubric beyond a four-word list — what specifically fails legibility?
- rolling_mean edge behavior for windows smaller than w is described in one phrase ("average what exists so far") — insufficient for understanding boundary artifacts
- Verification smoke test only confirms a non-empty PNG — doesn't test theme(), palette(), or finish() in isolation

## VERDICT: PASS

Judgement-not-flags philosophy with explicit defaults is the right design. chartkit primitives are concise and well-separated. write_html offline packaging is well specified. The GRID/ACCENT placeholder substitution gap is the key teachable pitfall for interactive charts.
