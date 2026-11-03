# CARRY-OUT — financial-services--claude-liam-audit-xls

**The line (written first, GATE C):**

> audit-xls checks the balance sheet first, then flags every suspect
> formula by cell — but it never rewrites one. Finding the problem is
> Claude's job here; fixing it stays yours.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses the one distinction the reel is built to land
(audit = find and report, cited by cell, in a fixed check order; not
audit = find and repair), not the topic (spreadsheet auditing generally).

**The wrong guess it defeats:** that asking Claude to "audit" a
spreadsheet means it will find the errors and fix them while it's in
there. It doesn't. The `audit-xls` skill checks BS balance first, then
scans the scoped range, sheet, or model for formula errors and common
mistakes, and reports what it finds, cell by cell. It does not rewrite a
formula on your behalf — give it a sheet with a known broken formula and
audit it, and the formula in the sheet is unchanged afterward; what
changed is the report.

**GATE C — signed:** derived directly from the source sheet's own stated
facts (see QUESTION.md) — the source beat_sheet.json's narration already
states the skill's scope; this line compresses it into the reel's
carry-out.
