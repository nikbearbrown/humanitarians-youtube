# Research — Ch. 6: Spreadsheets for Analysts

*Phase 1 notes and sources. No chapter prose.*

## Key claims & sources

- **A pivot table is a table of values that are aggregations of groups of individual values from a larger table** (from databases or spreadsheets); it summarizes flat data into totals/averages/counts by category.
  Source: Wikipedia, "Pivot table," https://en.wikipedia.org/wiki/Pivot_table (accessed 2026-07-15). *Tertiary/secondary reference.*
- **Pivot tables support aggregation functions** such as sum, average, count, and standard deviation, and organize data into filters / columns / rows / values areas.
  Source: Wikipedia, "Pivot table" (as above).

## Claims to source at draft time (not yet fetched)
- **[UNVERIFIED]** Definitions/behavior of `VLOOKUP`, `INDEX`/`MATCH`, `XLOOKUP`, `SUMIFS`, `COUNTIFS` — these are vendor spreadsheet functions. Confirm against Microsoft Excel official documentation (support.microsoft.com) or Wikipedia "VLOOKUP"/"Lookup function" when drafting; do not assert exact syntax from memory.
- **[UNVERIFIED]** Common lookup failure modes (e.g. VLOOKUP requiring the lookup column to be leftmost; approximate-match default pitfalls) — verify against official docs.

## Interview-craft (editorial)
- Data-cleaning tasks: duplicates, inconsistent categories, bad date formats, trailing spaces.
- Tool-choice judgment: spreadsheet vs. SQL vs. Python — editorial guidance.

## Original worked example
- Invented "conference signups" sheet (duplicate emails, mixed-case cities, two date formats) — fully invented.

## [UNVERIFIED] list
- Exact spreadsheet-function syntax and failure modes (VLOOKUP/INDEX-MATCH/XLOOKUP/SUMIFS/COUNTIFS) — confirm against Microsoft/official docs at draft time.
