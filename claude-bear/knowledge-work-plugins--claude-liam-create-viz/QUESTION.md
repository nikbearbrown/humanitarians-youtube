# QUESTION.md

**Question (as redone for hai-simple):** When Claude "creates a visualization"
with this skill, is the job making the chart look pretty, or something else?

**Source:** redo of
`anthropics/knowledge-work-plugins/youtube/claude-liam-create-viz`
(a rendered Teardown-register `claude-liam` reel walking through the
`create-viz` Anthropic skill — the `data` plugin's chart-generation tool).
The source sheet's own narration was truncated mid-thought in its design-tell
and handoff beats (B03: `"...into a chart, selecting the right chart type for
a trend or comparison, generating a plot for a report or presentation, or
needing an interactive chart with hover and zoom.."` cut short as `"Use when
turning query results or a DataFrame."`; BHTF: `"...use when turning query
re."` truncated mid-word) — the same batch-build defect the sibling reel
`knowledge-work-plugins--claude-liam-content-strategy` found and worked
around. Its `source_skill` path
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/...`) also
does not exist in this local tree. Per the REDO LAW, the facts were
re-sourced directly from the real, public skill file:
`anthropics/knowledge-work-plugins/data/skills/create-viz/SKILL.md` on
`github.com/anthropics/knowledge-work-plugins` (fetched this invocation via
`curl` against `raw.githubusercontent.com`, confirmed genuine via WebSearch).

**Asker:** nobody named — the source reel framed this as a general skill
teardown, not a specific person's question. Name not applicable.

**Locked facts carried over (do not alter):** create-viz turns a data source
(a query result, a pasted table, an uploaded file, or data already in the
conversation) into a chart. Before touching style, it picks the chart type
from the *relationship* in the data — trend over time → line, comparison
across categories → bar, part-to-whole → stacked bar or area (not pie unless
under six categories), distribution → histogram or box plot, correlation →
scatter, geographic → choropleth, ranking → horizontal bar, flow → Sankey,
matrix of relationships → heatmap. It writes the chart in matplotlib +
seaborn by default (static, publication-quality) or plotly when interactivity
(hover, zoom) is requested. It then enforces accuracy rules regardless of
which library: bar charts start at zero, axis breaks are never hidden,
colors are colorblind-safe and used meaningfully (not decoratively), titles
state the insight ("Revenue grew 23% YoY") rather than just the metric name,
and chart junk (top/right spines, unnecessary decoration) is stripped. It
saves a PNG at 150 DPI, hands back the Python code so the chart can be
modified, and suggests variations. Styling is the last step, not the first —
and it happens inside constraints the skill won't relax.
