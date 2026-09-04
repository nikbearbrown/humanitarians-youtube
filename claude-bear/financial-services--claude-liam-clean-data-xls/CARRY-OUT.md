# CARRY-OUT — financial-services--claude-liam-clean-data-xls

**The line (written first, GATE C):**

> Clean this data doesn't mean Claude judges what looks messy and fixes it —
> it runs one fixed checklist, in order, and anything outside that list is
> untouched. A column that comes back clean has been reformatted, not
> fact-checked.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses the one distinction the reel is built to land (a
fixed, six-item checklist vs. open-ended judgment about what "messy" means,
and reformatted vs. verified-correct), not the topic (spreadsheet cleanup
generally).

**The wrong guess it defeats:** that asking Claude to "clean this data"
means it will look over the sheet, notice whatever seems off, and fix it
using its own judgment about what "clean" ought to mean. It doesn't. The
`clean-data-xls` skill reads a written SKILL.md and runs exactly six fixed
operations — trim whitespace, fix inconsistent casing, convert numbers
stored as text, standardize dates, remove duplicates, flag mixed-type
columns — nothing more. Give it a column where the same currency symbol
covers two different currencies and there's no step for that; it comes out
exactly as ambiguous as it went in.

**GATE C — signed:** derived directly from the source sheet's own stated
facts (see QUESTION.md) — the source beat_sheet.json's narration already
states the skill's six-item scope; this line compresses it into the reel's
carry-out.
