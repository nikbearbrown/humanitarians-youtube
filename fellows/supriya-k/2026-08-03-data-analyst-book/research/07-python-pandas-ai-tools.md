# Research — Ch. 7: Python & pandas for Analysts (+ AI tools)

*Phase 1 notes and sources. No chapter prose.*

## Key claims & sources

- **pandas is a Python library for data manipulation and analysis;** the name derives from "panel data" and "Python data analysis."
  Source: Wikipedia, "pandas (software)," https://en.wikipedia.org/wiki/Pandas_(software) (accessed 2026-07-15). *Tertiary/secondary reference.*
- **Core structures:** `Series` (1-D labeled array) and `DataFrame` (2-D labeled table; each column is a Series and can hold a different type). DataFrames can be built from dicts, arrays, or files (CSV, Excel, JSON, SQL, Parquet).
  Source: Wikipedia, "pandas (software)" (as above).
- **Core operations:** boolean filtering (`df[df['col'] > 5]`), `groupby()` (split-apply-combine), `merge()` (one-to-one/one-to-many/many-to-many joins on keys), reshaping/`concat()`, time-series ops, and descriptive statistics (with NaN handling).
  Source: Wikipedia, "pandas (software)" (as above).
- **Limitation:** pandas holds datasets in RAM and does not optimize query plans or parallelize across cores.
  Source: Wikipedia, "pandas (software)" (as above).

## AI-tools section (2026 trend — sourced to trends notes)
- Interviewers may ask how candidates use AI tools (e.g. ChatGPT, Cursor) responsibly; the valued skill is judgment — knowing when to trust vs. read a generated query line by line, because AI output can pass a surface smell test but be subtly wrong.
  Source: `../blueprint-trends-notes.md` (sourced to DataCamp, Exponent, KORE1 2026 guides). *Secondary/editorial.*

## Interview-craft (editorial)
- Narrate approach during coding rounds; SQL↔pandas translation of the same question.

## Original worked example
- Invented "library checkouts" CSV; plus an AI-generated version of the code with a seeded subtle bug (filter applied after aggregation) — fully invented.

## [UNVERIFIED] list
- Exact current pandas method signatures/version specifics — confirm against pandas official docs (pandas.pydata.org) when writing code so examples run.
