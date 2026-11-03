# FACTCHECK.md — fifteen-of-sixteen (GATE F)

This file satisfies the toolkit's GATE F requirement (`require_paperwork` in
`build_safety.py`), which did not exist in `fellows/divij-pawar/CLAUDE.md`'s
documented pipeline when this reel's authoring paperwork (`SOURCES.md`,
`CHECKS-REPORT.md`) was first written. Rather than duplicate that work under
a new filename, this is the condensed fact-check record GATE F expects; the
full independent-verification narrative, the beat-by-beat claim mapping, and
the one flagged git-state discrepancy live in `SOURCES.md` in this same
folder — read that file for the complete account.

## Primary source

`fifteen-of-sixteen.md` (this folder) — the source script, with its own
25-row fact-check table. Independently re-verified against the live
checkout at `D:\Code\mycroft\verification-layer` (2026-09-20).

## Sources confirmed directly against the live checkout

| Ref | Document / module | Status |
|---|---|---|
| S1 | `logs/RUN_LOG.md` | CONFIRMED PRESENT — both 2026-09-11 entries located exactly as described |
| S3 | `web/self_report.py` | CONFIRMED PRESENT — `build_self_report()` run directly, matches "15 issues, 4 resolved, 9 open/unverified, 1 critical" exactly |
| S4 | `validation/concept_linkage.py` | CONFIRMED PRESENT — all three named tagging bugs independently confirmed in source |
| S5 | `core/numeric.py` | CONFIRMED PRESENT — 2026-09-11 fix comment names the exact comma-grouped-number bug |
| S8 | `tests/test_compare_route.py` | CONFIRMED PRESENT — exactly 3 test methods |
| S9 | `tests/fixtures/cross_agent_real_runs_corpus.json` | CONFIRMED PRESENT — 16 entries labeled `disjoint_concepts`, exact match |
| S11 | Re-run at drafting | `python -m unittest discover -s tests -t .` → 242 tests, OK — exact match |

## Verbatim quote law

1. **B12:** `"13,971,000,000.0"` → `"000.0"` → corrected back to
   `"13,971,000,000.0"` — confirmed exact against `core/numeric.py`'s own
   fix comment.
2. **B13:** `"Calculated the debt-to-equity ratio as 0.34"` — the same
   historic thought-log line independently confirmed in Mycroft6's own
   fact-check pass, now replayed through claim verification.

## B08's fabricated text — real, not illustrative (corrected during this build)

`web/data/accountability.db` was queried directly for run `09cc72b6` (MSFT,
2026-09-11T17:42:37Z), the same run `RUN_LOG.md` describes narratively as
"invented an unrelated historical fiscal quarter and a fabricated source
URL" without quoting the exact string. B08 now shows that real string
(`"Q2 FY 2021" -- doesn't exist`) and the real struck-out URL
(`https://www.sec.gov/`) verbatim, per EXECUTABLE-EVIDENCE
(`fellows/divij-pawar/CLAUDE.md` §4). This replaces the originally authored
placeholder text and closes the gap `SOURCES.md` had previously flagged as
outstanding.

## One flagged discrepancy (not a contradiction)

`git status --short` at drafting time (2026-09-20) returned **62** lines,
not a literal reconciliation of Mycroft6's 56 plus "+11 more files" (~67).
The last commit hash (`c53746a`) is confirmed unchanged. This build kept
the script's own "+11 more files" framing — see `SOURCES.md` "Git state"
for the full reasoning.

## Claims deliberately NOT made

- That the comparator "now catches fabrication" — states it produces "a
  real, automatic signal," never "catches."
- That mistral-7b "is broken" — states "flagged, not fixed," never a
  verdict on the model in general.
- That 4-for-4 flagged "proves the tool works" without qualification —
  immediately followed by "just not the one it was built to find."
- That "fifteen of sixteen" makes the sixteenth not matter — labeled
  explicitly `TRUE POSITIVE, PRESERVED`.
- That anything is "shipped" — states the file count grew, not that
  anything shipped.

Full independent re-verification and the complete 18-beat claim mapping are
in `SOURCES.md`.
