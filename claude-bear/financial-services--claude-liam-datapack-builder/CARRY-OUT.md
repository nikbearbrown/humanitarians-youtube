# CARRY-OUT — financial-services--claude-liam-datapack-builder

**The line (written first, GATE C):**

> datapack-builder doesn't calculate your numbers — it extracts and
> standardizes them into one workbook, the same way every time.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses the one distinction the reel is built to land
(data extraction/standardization vs. numeric analysis/judgment), not the
topic (what a data pack is, or M&A due diligence generally).

**The wrong guess it defeats:** that asking Claude to build a data pack
means it is running the financial analysis itself — computing the numbers,
modeling the deal, the way an analyst would. It isn't. `datapack-builder`
is a folder Claude reads before it works; the SKILL.md inside it is the
full instruction set, executed step by step, in order, with no branching
unless a step says so. It pulls data from what you give it — CIMs, offering
memorandums, SEC filings, web search, MCP servers — and normalizes it into
a consistent, investment-committee-ready workbook. Give it the same source
material twice and it produces the same structure twice. It is explicitly
not built for simple financial calculations or for reworking a data pack
that's already finished — whatever isn't covered by the file's steps
simply isn't part of the job.

**GATE C — signed:** derived directly from the source sheet's own stated
facts (see QUESTION.md) — the source beat_sheet.json's narration already
states the skill's scope ("a skill is a folder," "the file is the
program," "same input → same output, every run," "know the limit: only
what the file says," "do not use for simple financial calculations"); this
line compresses it into the reel's carry-out.
