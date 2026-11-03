# FACTCHECK — "Claude, Ingested." (Week 1)

| Claim (beat) | Verdict | Source |
|---|---|---|
| Manual `Accept-Encoding` header defeats Go's transparent gzip decode (B03/B04) | ✓ | `secclient.go`, commit `314ce1d` (buggy) vs `f640349` (fixed); `RUN_LOG.md` "Bugs found and fixed" table, row 1 |
| Archive URL needs the subject company's CIK, not the accession-prefix filer CIK (B05/B06) | ✓ | `edgar_fts.go` diff, same two commits; `RUN_LOG.md` row 2 |
| 97 events stored, all `edgar_atom`, FTS correctly returns 0 on a Sunday (B07) | ✓ | `RUN_LOG.md` "Week 1 first run" section |
| Offset rewind → replay → `inserted 0, skipped_dupe 97` (B07) | ✓ | `RUN_LOG.md` PRE_REGISTRATION verification table, idempotency row — PASS |
| A 3-day FTS lookback silently absorbed the whole Atom feed (B08) | ✓ | `RUN_LOG.md` "Finding — FTS lookback subsumes the atom feed" |
| Recipe stays `DRAFT`, `todos_open: 6` at this point in the project (B09) | ✓ | `git show f640349:recipes/finance-event-signals.md` frontmatter |

## Corrections applied

None needed — every claim traces directly to a commit diff or a RUN_LOG.md
entry from the underlying project; nothing was paraphrased from a
secondary source.

## Numbers on screen

None invented. "97 events," "0 duplicates," "6 gates" are all counts
pulled directly from the sources above.
