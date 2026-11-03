# FACTCHECK.md — zero-for-sixteen (GATE F)

This file satisfies the toolkit's GATE F requirement (`require_paperwork` in
`build_safety.py`), which did not exist in `fellows/divij-pawar/CLAUDE.md`'s
documented pipeline when this reel's authoring paperwork (`SOURCES.md`,
`CHECKS-REPORT.md`) was first written. Rather than duplicate that work under
a new filename, this is the condensed fact-check record GATE F expects; the
full independent-verification narrative, the beat-by-beat claim mapping, and
the one flagged git-state discrepancy live in `SOURCES.md` in this same
folder — read that file for the complete account.

## Primary source

`zero-for-sixteen.md` (this folder) — the source script, with its own
31-row fact-check table and "things this script deliberately refuses to
say" list in its PRODUCTION NOTES. This reel's claims were independently
re-verified against the live checkout at `D:\Code\mycroft\verification-layer`
(2026-09-08), per `fellows/divij-pawar/CLAUDE.md` §4.

## Sources confirmed directly against the live checkout

| Ref | Document / module | Status |
|---|---|---|
| S1 | `web/self_report.py` | CONFIRMED PRESENT — 14 `KNOWN_ISSUES` entries, exact status vocabulary, `LIVE_MODEL_TESTS` list all verified |
| S2 | `logs/RUN_LOG.md` | CONFIRMED PRESENT — four entries dated 2026-09-04 (×3) and 2026-09-07 located exactly as described |
| S3 | `divij/cross-agent-validation-status.md` | CONFIRMED PRESENT — §3.4 quote matches verbatim |
| S7 | `producers/earnings.py` | CONFIRMED PRESENT — "deliberately disjoint from `producers/financial.py`'s" is a verbatim docstring match |
| S8 | `tests/test_layering.py` | CONFIRMED PRESENT — 6 real AST-based test methods |
| S9 | `tests/fixtures/cross_agent_real_runs_corpus.json` | CONFIRMED PRESENT — exactly 31 entries, matching the "thirty-one runs" claim |
| S11 | `git log`/`git status` on the live checkout | Run directly; last commit `c53746a` confirmed exact |

## Verbatim quote law (highest-stakes strings, confirmed exact)

1. **B01:** `"web/static/index.html and app.js are, as of this document,
   completely unmodified for Cross-Agent Validation."` — exact match,
   `divij/cross-agent-validation-status.md` line 276.
2. **B09:** `"…deliberately disjoint…"` — exact match, `producers/earnings.py`
   line 10.
3. **B11:** `"13,971,000,000.0"` → `"000.0"` — exact match,
   `self_report.py`'s `regex-truncates-comma-grouped-numbers` entry, run
   `515f263a`.

## One flagged discrepancy (not a contradiction)

`git status --short` at drafting time (2026-09-08) returned **57** lines,
not the script's stated **56**. The last commit hash (`c53746a`) is exact.
This build kept the script's own number (56), since it describes a
measurement taken for a specific period, not a live counter — see
`SOURCES.md` "Git state" for the full reasoning.

## Claims deliberately NOT made

- That the UI is "done" or "shipped" — nothing is committed.
- That the comparator "now catches fabrications" — only made one fabrication
  *visible*; the comparator's rule is unchanged.
- That the over-flagging is "fixed" — the fix is upstream, out of scope.
- That "224 tests" is evidence of correctness — used only as a delta.
- That the retry path is "proven" — only *rendered*, still unproven against
  live failures.
- That "zero for sixteen" means the comparator doesn't work — the narrower,
  correct claim (two producers never asked the same question) is what B14
  states.

Full independent re-verification, the complete 16-beat claim mapping, and
the declared simplifications are in `SOURCES.md`.
