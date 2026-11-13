# Compiling Is Not Migrating.

*An overview of my SQL Server → Snowflake migration project (`snowshift`).*

- **Status:** built · not published · GATE P pending presenter review
- **Presenter:** Mohammed Hussain (first person) · voice Kokoro `am_onyx`
- **Resolution:** 3840×2160 (16:9) · 2160×3840 (9:16, native reflow)
- **Runtime:** 3:14
- **Built with:** `ai-explainer` (brutalist toolkit) · Register: Teardown
- **Cost:** $0.00 — Kokoro + Remotion, local, no API key

## The idea

A migration is not done when the SQL compiles on the new engine. It is done when
you can prove it behaves the same, and the dangerous differences are the ones
that raise no error. The test the reel leaves: *run it twice; if anything
doubles, it is not migrated.*

## Deliverables

| File | Aspect |
|---|---|
| `hussain-snowshift-migration-overview-4k-16x9.mp4` | 16:9 · 3840×2160 |
| `hussain-snowshift-migration-overview-4k-9x16.mp4` | 9:16 · 2160×3840 |

## Structure

```
B00  ASK        "Hi, I am Hussain…" — the ask lands answered
B01  BLUF       Migrating is proving. Compiling is the start.
B02  PROBLEM    one 1,244-line file → 29 files in 8 ordered stages
B03  LINT       27 rules, each with its fix · the real SELECT TOP 10 catch
B04  ASK        deploy in order, dry-run first, stop at first failure
B05  RESULT     the stage rail: in order, then stop
B06  PARITY     aggregates on both engines · DECIMAL that landed FLOAT
B07  GAP        UNIQUE declared, not enforced · import twice, budget doubles
B08  FIX        the import checks for itself · three smoke runs
B09  TEARDOWN   not run live yet · concurrent imports · placeholders
B10  VERDICT    one-page recap
B11  HANDOFF    the prompt to run on your own procedure
B12  OUTRO      title restate
```

## Paperwork

`beat_sheet.json` (the reel) · `FACTCHECK.md` · `SOURCES.md` · `SHOTLIST.md` ·
`PROMPTS.md` · `CHECKS-REPORT.md` · `PEDAGOGY.md` (pending sign-off) ·
`QC-STATUS.md` (gate results and known issues) · `BUILD-PROMPT.md` (rebuild).
Scene source: `brutalist.art/runtime/remotion/src/scenes/SnowshiftIllus.tsx`.
