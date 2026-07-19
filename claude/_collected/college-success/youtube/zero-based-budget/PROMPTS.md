# PROMPTS.md — zero-based-budget

## Beat-prefixed prompts for open slots

### B01 — PROBLEM slate
Visual: title card showing "Income − Expenses = 0" with two-column layout.
Left: "Normal month — budget holds". Right: "Restaurants/Phone/Gas +20% — budget breaks."
No terminal. Teardown palette. Fade in.

### B04 — Manim B04_BudgetBars
Rendered from vox_scenes.py class B04_BudgetBars.
Grouped bar chart: before/after stress for Restaurants ($100→$120), Phone ($120→$144), Gas ($200→$240).
Baseline bars PASS_CLR (#2A7A2A), stressed bars CRIMSON (#C8102E).
Deficit label at bottom: "Stress test deficit: -$190".
7 play() calls. Gate A: clean. Gate B: run post-render.

### B06 — revised output slate
Screen recording of budget_tool.py output showing:
- Stressed budget table with deficit highlighted
- "Emergency fund exhausted in 2.6 months at current stress level."
Record actual script run or fill with annotated still.

### B07 — summary slate
Card: "Budget = assignment system. Stress test = find the break."
Deficit: $190/month. Fund exhaustion: 2.6 months. Teardown palette.

### B08 — next steps slate
Card with three numbered items:
1. Plug in your actual numbers
2. Run stress test on your top 3 variable expenses
3. Find break-even months
Teardown palette.
