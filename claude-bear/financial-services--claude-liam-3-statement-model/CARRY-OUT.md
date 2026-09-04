# CARRY-OUT — financial-services--claude-liam-3-statement-model

**The line (written first, GATE C):**

> A filled-in model isn't Claude's financial judgment — it's the numbers you
> gave it, linked by a fixed set of steps. The model only connects what the
> template told it to connect.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses the one distinction the reel is built to land
(a written procedure that links numbers vs. an analyst's judgment about
what belongs in the model), not the topic (financial modeling generally).

**The wrong guess it defeats:** that asking Claude to "fill in" a 3-statement
model means it reasons about the business the way an analyst would —
weighing what revenue drivers matter, what assumptions are reasonable, what
belongs in the model at all. It doesn't. The `3-statement-model` skill reads
a written SKILL.md and executes a fixed list of steps that link an existing
Income Statement / Balance Sheet / Cash Flow Statement template together.
Ask it for something those steps don't cover and it will not improvise a
fix from general financial knowledge — it stays exactly inside what's
written.

**GATE C — signed:** derived directly from the source sheet's own stated
facts (see QUESTION.md) — the source beat_sheet.json's narration already
states the skill's scope; this line compresses it into the reel's carry-out.
