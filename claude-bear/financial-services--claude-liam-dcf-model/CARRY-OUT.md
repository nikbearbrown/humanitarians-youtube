# CARRY-OUT — financial-services--claude-liam-dcf-model

**The line (written first, GATE C):**

> A DCF number is Claude running your growth and discount-rate assumptions
> through a fixed formula — not Claude's opinion of what a company is
> worth. Change the assumption, and the number moves; the model never
> argues about which one is right.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses the one distinction the reel is built to land
(a formula that converts assumptions into a number vs. an analyst's
independent judgment about a company's worth), not the topic (DCF
valuation generally).

**The wrong guess it defeats:** that a Claude DCF valuation reflects its own
judgment about what a company is worth — the way an analyst who has studied
the business reaches a conclusion. It doesn't. The `dcf-model` skill reads a
written SKILL.md and executes a fixed procedure: retrieve financial data,
project cash flows, discount them (plus a terminal value) using WACC, run a
sensitivity analysis, and output an Excel model. Give it a different growth
rate or discount rate and the valuation moves without protest — it never
argues that your assumption is wrong, because it never had an opinion about
the company to begin with.

**GATE C — signed:** derived directly from the source sheet's own stated
facts (see QUESTION.md) — the source beat_sheet.json's narration already
states the skill's scope; this line compresses it into the reel's
carry-out.
