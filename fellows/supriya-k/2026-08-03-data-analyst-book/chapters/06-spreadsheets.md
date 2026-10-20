# Chapter 6 — Spreadsheets for Analysts

Spreadsheets are still where many analyst interviews test whether you can **clean and summarize messy data quickly** — often live, often on a deadline.

> **What's tested here**
> Speed and correctness on real data: the right lookup, a fast aggregation, and the judgment to clean before you analyze.

## Formulas that earn their keep

- **Conditional aggregation:** `SUMIFS`, `COUNTIFS`, `AVERAGEIFS` — totals and counts by criteria.
- **Logic:** `IF`, nested sparingly.
- **Text/date cleanup:** `TRIM`, `LOWER`/`UPPER`, `LEFT`/`RIGHT`, date parsing.

> **Argument order (verified against Microsoft docs):** `COUNTIFS(criteria_range1, criteria1, …)` — but `SUMIFS(sum_range, criteria_range1, criteria1, …)` puts the **sum range first.** Mixing these up is a classic slip.[^xlfns]

## Lookups — and how they fail

| Function | Note | Classic failure |
|---|---|---|
| `VLOOKUP` | Lookup value must be in the **leftmost** column; **defaults to approximate match** | Silent wrong values when columns shift or the table isn't sorted |
| `INDEX`/`MATCH` | More flexible; look up in any column | More typing, easy to mismatch ranges |
| `XLOOKUP` | Modern replacement; **defaults to exact match** | Not in older Excel versions |

**Interview tip:** the most common lookup bug is `VLOOKUP`'s **approximate-match default returning the wrong row.** Prefer exact match (`FALSE` in `VLOOKUP`, the default in `XLOOKUP`) unless you mean otherwise.[^xllookup]

## Pivot tables

A **pivot table aggregates groups of values from a larger table** — sums, averages, counts by category — organized into filters, rows, columns, and values.[^pivot] It's the fastest way to answer "X by Y" without writing formulas.

## Cleaning messy data

Before any analysis, scan for: **duplicates, inconsistent categories** (`Boston` vs `boston`), **bad/mixed date formats**, and **trailing spaces**. Name what you find — interviewers want to hear you *notice* the mess.

## Choosing the tool

Spreadsheet for quick, visual, one-off summaries; SQL when the data lives in a database or is large; Python when the transform repeats or gets complex.

## Worked example

An invented **conference-signups** sheet has duplicate emails, mixed-case cities, and two date formats. Steps:
1. `TRIM`/`LOWER` the city column; standardize dates.
2. Remove duplicate emails (keep first).
3. Pivot: signups by city.

![A messy signups sheet (duplicate email, mixed case, two date formats) cleaned into a signups-by-city pivot.](images/06-spreadsheets-fig-01.png)

## Exercises

1. **(Warm-up.)** Write a `COUNTIFS` for "signups from 'Boston' in March."
2. **(Representative.)** A `VLOOKUP` returns wrong values after a colleague inserted a column. Diagnose which failure mode caused it.
3. **(Stretch.)** For a described task, decide whether it belongs in a spreadsheet, SQL, or Python — and justify in two sentences.

---

*Next:* when the interview wants code, it usually means Python and pandas — plus a new 2026 question about how you use AI tools.

[^pivot]: Wikipedia, "Pivot table," https://en.wikipedia.org/wiki/Pivot_table (accessed 2026-07-15).
[^xlfns]: Microsoft Support, "COUNTIFS function" (https://support.microsoft.com/en-us/excel/functions/countifs-function) and "SUMIFS function" (https://support.microsoft.com/en-us/office/sumifs-function-c9e748f5-7ea7-455d-9406-611cebce642b), accessed 2026-07-15.
[^xllookup]: Microsoft Support, "VLOOKUP function" (https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1) and "XLOOKUP function" (https://support.microsoft.com/en-us/excel/functions/xlookup-function), accessed 2026-07-15.
