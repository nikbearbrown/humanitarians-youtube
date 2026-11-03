# FACTCHECK — Compiling Is Not Migrating.

Every claim the reel makes, spoken or on screen, checked against the source:
the `snowshift` repository at `C:/Users/Hussain/Desktop/Project/snowshift`,
commits `eb342d4` (restructure + tooling) and `7ba5900` (duplicate-key fixes).

| # | Claim (beat) | Verdict | Source | Fix applied |
|---|---|---|---|---|
| 1 | The migration arrived as one 1,244-line `Main.sql` plus a procedures folder that had drifted out of sync (B00, B02) | TRUE | commit `eb342d4` message | — |
| 2 | Split into 29 files across 8 ordered stages (B00, B02, B04) | TRUE | `sql/` listing: 3+8+3+2+4+6+1+2 = 29; `manifest.yaml` declares 8 stages | — |
| 3 | Per-stage file counts 3 / 8 / 3 / 2 / 4 / 6 / 1 / 2 (B02, B05) | TRUE | `ls sql/*/` | — |
| 4 | 32 CREATE statements in, each exactly once out (B02) | TRUE as of the split | commit `eb342d4`: "all 32 CREATE statements from the original appear exactly once" | Stated as the split's check, not a live count of today's tree (which now has more CREATE lines, e.g. roles). |
| 5 | The linter has 27 rules, three severities, each carrying the Snowflake fix (B03) | TRUE | `src/snowshift/lint/rules.py` (27 entries after `7ba5900`); severities error/warning/info | — |
| 6 | The four on-screen pairs are real rule remedies (B03) | TRUE | SS001 GETDATE→CURRENT_TIMESTAMP; SS003 ISNULL→IFNULL/COALESCE; SS010 NVARCHAR; SS009 IDENTITY→AUTOINCREMENT | — |
| 7 | It found a real `SELECT TOP 10` in the seed script that would have failed on execution, fixed to `ORDER BY … LIMIT 10` (B03) | TRUE | commit `eb342d4` message | — |
| 8 | Deploy runs stages in manifest order, supports dry-run, halts on first failure and marks the rest skipped (B04, B05) | TRUE | `snowshift deploy --help`; `src/snowshift/deploy/runner.py`; commit `eb342d4` | — |
| 9 | Seed and tests are optional stages, so a production run cannot load sample data (B05) | TRUE | `manifest.yaml` `optional: true` on seed and tests | — |
| 10 | The FAIL on `views` in B05 | ILLUSTRATIVE | — | Footnote on screen: "The failure shown is illustrative". No real file is named as failing. |
| 11 | Parity compares row counts plus COUNT/SUM/MIN/MAX on declared columns, using aggregates with the same semantics on both engines (B06) | TRUE | `parity.yaml` header; commit `eb342d4` | — |
| 12 | Columns are declared, not introspected, because a DECIMAL(19,4) that landed as FLOAT compares equal under introspection and then drifts (B06) | TRUE | `parity.yaml` header comment | — |
| 13 | The parity values on screen (250, 48,213,907.52, 2024-01-01, 7.4000 / 7.399999999999999) | ILLUSTRATIVE | — | Footnote: "Worked example · illustrative values". Parity has not been run against both engines. |
| 14 | Snowflake declares but does not enforce PRIMARY KEY / UNIQUE (B07) | TRUE | Snowflake documentation (constraints are informational, except NOT NULL); `docs/migration-notes.md` §Constraints | — |
| 15 | The constraint shown is the real natural key on BudgetLineItem (B07) | TRUE | `sql/10_tables/06_BudgetLineItem.sql` | — |
| 16 | Running the same import twice would double the budget (B07) | TRUE in mechanism; multiple illustrative | `docs/migration-notes.md` (7ba5900) | Footnote: "Budget multiple is illustrative". |
| 17 | The import now resolves codes to IDs, rejects keys repeated within a payload, applies REJECT/UPDATE to existing lines, in one transaction (B08) | TRUE | `sql/50_procedures/01_usp_BulkImportBudgetData.sql` at `7ba5900` | — |
| 18 | The three smoke runs and their expected results (B08) | TRUE as written assertions | `sql/90_tests/02_procedure_smoke_tests.sql` Test 1a/1b/1c | B09 states plainly that these have not run live. |
| 19 | Not run against a live Snowflake account yet; 103 tests pass and none touch a database (B09) | TRUE on 2026-10-07 | `pytest` → 103 passed; deploy blocked on missing credentials | Will date: update B09 after the first live run. |
| 20 | Concurrent imports can both pass the existence check (B09) | TRUE | `docs/migration-notes.md` (7ba5900), last paragraph | — |
| 21 | Two converted procedures are still placeholders (B09) | TRUE | `usp_GenerateRollingForecast`, `usp_ReconcileIntercompanyBalances` | — |

## Corrections applied while scripting

- "Duplicate journals on re-run" was **not** used as a migration regression:
  SQL Server would also have accepted a second run seconds later. Only the
  unenforced-constraint gap is presented as something Snowflake changed.
- Nothing is claimed as working in production. The reel's falsifiability beat
  (B09) leads with "not run live yet".
- No model version numbers or tool versions appear on screen.

## Things that will date this reel

B09 "not run live yet" and "103 tests". Re-record B09 (and B10's recap) after
the first live deploy.
