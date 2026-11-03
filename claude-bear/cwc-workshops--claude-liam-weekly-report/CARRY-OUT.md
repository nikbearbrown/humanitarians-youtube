# CARRY-OUT

> Ask Claude for this report and it writes one script that reads every row
> once, instead of checking each SKU by hand — and which sections that
> script prints still depends on whether you asked for the full weekly
> review or the shorter daily sweep.

Test: if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses both halves of the skill (the one-script habit
that replaces per-SKU tool calls; the fact that the report's shape still
changes with what was actually asked) without overstating either.

**Wrong guess this defeats:** "Claude checks the inventory file SKU by SKU,
one tool call per row" (the natural read when a report needs to cover a
stockout, low-stock, open-PO, and forecast-risk figure for every item in a
~67,000-row file). The SKILL.md is explicit that this is exactly the
pattern it exists to prevent: one script loads every source file once,
computes every section in a single pass, and prints the finished markdown —
no per-SKU tool calls, no paging through the data row by row.
