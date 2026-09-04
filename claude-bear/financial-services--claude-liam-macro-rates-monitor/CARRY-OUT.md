# CARRY-OUT — financial-services--claude-liam-macro-rates-monitor

**The line (written first, GATE C):**

> A macro rates dashboard from Claude isn't an original economic call — it's
> four named inputs, macro indicators, the yield curve, breakevens, and swap
> rates, combined by one fixed, repeatable procedure. A finished dashboard
> means the combination ran correctly, not that reality will follow it.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses the one distinction the reel is built to land (a
fixed four-input combination procedure vs. an original forecast, and
combination-completed vs. economically-correct), not the topic (macro
economics generally).

**The wrong guess it defeats:** that asking Claude for a macro rates monitor
dashboard means it is forming its own view on where rates are headed — reading
the data like an analyst and telling you what's coming. It isn't. The
`macro-rates-monitor` skill reads a written SKILL.md and combines exactly four
named inputs — macro indicators, the yield curve, inflation breakevens, and
swap rates — using the definitions already written for them. Ask it instead to
forecast what the central bank will actually do next quarter, and there's
nothing to run: a genuine forecast isn't one of the four things the spec
combines.

**GATE C — signed:** derived directly from the source sheet's own stated
facts (see QUESTION.md) — the source beat_sheet.json's narration already
states the skill's four-input scope and its "same input, same output, only
what the file says" limit; this line compresses it into the reel's carry-out.
