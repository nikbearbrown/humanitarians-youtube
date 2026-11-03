# SOURCES.md — zero-for-sixteen (Video 4)

**DOUBLE-CHECK LAW.** Every factual claim spoken in this reel traces to the
source script, and through it to the code and logs it describes. This is a
weekly-update reel making claims about a real codebase, so every number here
is re-verifiable against the repository — if a figure cannot be reproduced,
cut the claim rather than hedging it.

**Primary source:** `zero-for-sixteen.md`, in this same folder — the script
itself, which ships its own fact-check table and a "things this script
deliberately refuses to say" list in its own PRODUCTION NOTES section. This
file does not duplicate that table blindly; it restates the beat-level
mapping against this build's B00–B15 numbering and adds an independent
verification pass done directly against the live checkout at
`D:\Code\mycroft\verification-layer` (2026-09-08), per this channel's
authoring discipline ("verify claims about any real external project against
the live source" — `fellows/divij-pawar/CLAUDE.md` §4).

**This reel is unusually well-sourced compared to the series' prior entries.**
Where the-number-that-wasnt-there (Mycroft5) found most of its specific run
figures sourced only to files absent from its checkout, every file this
script cites was found present and readable in `D:\Code\mycroft\verification-layer`
during this build.

---

## Sources confirmed directly against the live checkout

| Ref | Document / module | Status |
|---|---|---|
| S1 | `web/self_report.py` | **CONFIRMED PRESENT**, read in full — the ledger's 14 `KNOWN_ISSUES` entries, their exact status vocabulary, and the `LIVE_MODEL_TESTS` list all independently verified |
| S2 | `logs/RUN_LOG.md` | **CONFIRMED PRESENT** — the four entries dated 2026-09-04 (×3) and 2026-09-07 all located exactly as the script describes (headings grepped directly) |
| S3 | `divij/cross-agent-validation-status.md` | **CONFIRMED PRESENT** — §3.4's quote read and matches the script's citation verbatim, character for character |
| S4 | `divij/cross-agent-validation-disjoint-concepts-diagnosis.md` | **CONFIRMED PRESENT** |
| S5 | `divij/weekly-update-2026-09-04-to-2026-09-07.md` | **CONFIRMED PRESENT** — §6.4 (the stale-ledger finding) and §7 (ledger counts) read directly and match the script |
| S6 | `divij/work.md` | **CONFIRMED PRESENT** |
| S7 | `producers/earnings.py` | **CONFIRMED PRESENT**, docstring read directly — "deliberately disjoint from `producers/financial.py`'s" is a verbatim match |
| S8 | `tests/test_layering.py` | **CONFIRMED PRESENT**, six real test methods including `test_every_package_only_imports_its_allowed_layers` and `test_root_has_no_python_modules_other_than_init` |
| S9 | `tests/fixtures/cross_agent_real_runs_corpus.json` | **CONFIRMED PRESENT**, loaded directly — **exactly 31 entries**, matching the script's "thirty-one runs" claim precisely |
| S10 | `web/server.py`, `web/step_trace.py`, `web/static/` (JS) | **CONFIRMED PRESENT** |
| S11 | `git log` / `git status` on `D:\Code\mycroft\verification-layer` | Run directly (see "Git state" below) |

---

## Fact-check table, transplanted from the script

The script's own PRODUCTION NOTES section carries its own 31-row fact-check
table with per-claim sources. Rather than re-list all 31 rows (see
`zero-for-sixteen.md`'s own table for the full list), this section records
this build's *independent re-verification* of the highest-stakes and most
specific claims:

| Claim in VO | Independent verification |
|---|---|
| 16 of 31 stored runs are disjoint-concept false positives; 0 are genuine conflicts | **CONFIRMED**: `self_report.py`'s `disjoint-concepts` entry states this exact figure verbatim ("Quantified against all 31 real stored runs on 2026-09-07: 16 labeled disjoint_concepts, 0 labeled genuine_conflict") |
| The historic true positive `f4a4c782` would not flag today; the both-sides-non-empty gate is the suppressing mechanism | **CONFIRMED**: `self_report.py`'s `asymmetry-fix-suppresses-historic-true-positive` entry names run `f4a4c782` and the `bool(a_set) and bool(b_set)` gate explicitly |
| `"13,971,000,000.0"` truncates to `"000.0"`, run `515f263a` | **CONFIRMED**: `self_report.py`'s `regex-truncates-comma-grouped-numbers` entry names run `515f263a` (ticker V) explicitly |
| §3.4 verbatim quote ("completely unmodified") | **CONFIRMED**: `divij/cross-agent-validation-status.md` line 276, exact match |
| Earnings producer's docstring calls the disjointness deliberate | **CONFIRMED**: `producers/earnings.py` line 10, "The concept set is deliberately disjoint from `producers/financial.py`'s" |
| `test_layering.py` reads imports as a syntax tree | **CONFIRMED**: present, 6 test methods, AST-based (module read directly) |
| 224 tests passing | **RE-RUN at this build's drafting** (2026-09-08): `python -m unittest discover -s tests -t .` → **224 tests, OK** — exact match |
| 14 ledger entries; 12 open/unverified; 1 critical | **CONFIRMED, recomputed independently**: `self_report.py`'s `KNOWN_ISSUES` list has exactly 14 entries — 11 `OPEN` + 1 `UNVERIFIED` (`retry-halt-unproven`) = 12 open-or-unverified; 1 `RESOLVED` (`claim-verification`, historical entry in `LIVE_MODEL_TESTS`, not `KNOWN_ISSUES`); 2 `BY_DESIGN`; exactly 1 `severity: critical` (`audit-criticals`) |
| Stale `http-no-model-override` detail text | **CONFIRMED**: `divij/weekly-update-2026-09-04-to-2026-09-07.md` §6.4 states this exactly, including that the entry's `status` was deliberately left `OPEN` while its detail text went stale |
| Nothing committed; last commit `c53746a` | **CONFIRMED**: `git log --oneline -1` in `D:\Code\mycroft\verification-layer` returns `c53746a Add Cross-Agent Validation v1: flag numeric contradictions between two agents` |
| 56 changed or new files | **NOT an exact match at build time — see "Git state" below** |
| Corpus labels are AI-assigned, unreviewed | Carried as the script's own framing; not independently falsifiable from the checkout alone (a label-provenance claim, not a code fact) |

---

## Git state — one honest discrepancy

Running `git status --short` directly in `D:\Code\mycroft\verification-layer`
at this build's drafting time (2026-09-08) returns **57** lines (changed +
untracked files), not the script's stated **56**. The last commit is
confirmed exactly as `c53746a`. This one-file drift is consistent with
ordinary continued work between when the script was drafted (citing
`git status --short -- verification-layer | wc -l`) and when this build ran
— it is not a contradiction of the script's claim, and is not evidence the
script's count was wrong *at the time it was measured*. **This build kept
the script's own number (56) in the narration and end-card text**, since the
claim describes a measurement taken for a specific period rather than a
live counter that should track whatever the checkout happens to show on any
given day. Flagged for the human reviewer at GATE P — see PEDAGOGY.md "Known
deviations" #6.

---

## Beat-level claim mapping (B00–B15)

| Beat | Claim | Status |
|---|---|---|
| B00 | 16 flagged, 0 genuine conflicts, replayed against today's code; the one true positive is suppressed today | **Confirmed** — S1 (self_report.py), S9 (corpus fixture) |
| B01 | CAV mechanism; accountability layer; 7/12 over-flag (prior, unmeasured); §3.4 verbatim quote | **Confirmed** — S3 |
| B02 | self_report.py as single source of truth; live unittest discovery; stale "143 tests" claim; generated caveat; null vs. false | **Confirmed** — S1, and the README's stale-count fix is named in `logs/RUN_LOG.md`'s 2026-09-04 SOLID-restructure entry |
| B03 | Exactly one EDGAR fetch; both producers share the identical data object; sequential not concurrent; retry path rendered live | Script cites S2 ("Verifying the critique" section); mechanism (shared fetch, sequential execution) is a code-level claim about `web/server.py`'s `/api/compare` route, consistent with the script's own description. **The 766ms/812ms timings were cut from this beat** in the 2026-09-08 runtime-cut pass (script's own cut-to-6:00 guidance, item 2) — the timings were a single measured sample, not independently re-timed in this pass, and are recorded here as cut content, not shown on screen |
| B04 | `$383.266 billion` reconciles to `Assets: 383266000000.0`; `0.34` is absent from input | Script's own claim, sourced to the UI v2 session's manual verification (S2); the underlying data (Apple's `Assets` XBRL fact) is a real SEC EDGAR value, consistent with the script's framing |
| B05 | 16 flat root modules; `parser.py` shadows stdlib; 8 incremental moves; byte-identical 9-call snapshot | Script cites S2 (2026-09-04 SOLID entry); the six-layer target structure (`core/adapters/pipeline/datasources/producers/validation`) is **independently confirmed** — these are exactly the top-level packages present in the live checkout |
| B06 | Regex duplicated 3× across `claims.py`/`consistency.py`/`verification.py` | Script cites S2; the described modules (`validation/claims.py`, `validation/consistency.py`, `validation/verification.py`) are **confirmed present** at their described post-refactor locations. The `_latest_value` cross-producer-import case (also cited to S2) **was cut from this beat** in the 2026-09-08 runtime-cut pass (script's own cut-to-6:00 guidance, item 1) — recorded here as cut content, not shown on screen |
| B07 | +47 tests; `test_layering.py` AST-based; 3 deliberate violations each producing a named failure | **Independently confirmed present**: `test_layering.py` exists with 6 test methods; the specific "broke it 3 times, restored" narrative is sourced to S2, not independently re-run in this pass (would require checking out the pre-fix state) |
| B08 | 31 runs, versioned fixture, replayed via `fixture_adapter`; 16/31 disjoint, 0/31 genuine | **Independently confirmed** — S9 loaded directly, exactly 31 entries |
| B09 | Producer A vs. B concept vocabularies never intersect; docstring calls it deliberate; fix is upstream; +8 tests | **Independently confirmed** — S7 (docstring, verbatim) |
| B10 | `f4a4c782` replay: two same-day August fixes, both-sides-non-empty gate suppresses the flag | **Independently confirmed** — S1's `asymmetry-fix-suppresses-historic-true-positive` entry names this run and mechanism exactly |
| B11 | `"13,971,000,000.0"` → `"000.0"`, run `515f263a` | **Independently confirmed** — S1's `regex-truncates-comma-grouped-numbers` entry (run `515f263a`). The stale `http-no-model-override` detail-text finding (S5 §6.4, also independently confirmed) **was cut from this beat** in the 2026-09-08 runtime-cut pass (script's own cut-to-6:00 guidance, item 3) — recorded here as cut content, not shown on screen |
| B12 | "True now" list — 7 specific gains this period | Each item traces to a specific prior beat's own confirmed claim (B02–B09); the 224-vs-169 test-count delta is confirmed via S1's live discovery mechanism plus this build's own re-run (224, OK) |
| B13 | "Still not true" list; 14/12/1 ledger counts; nothing committed, `c53746a`, 56 (scripted) / 57 (measured) files | **Confirmed** — S1 (ledger counts, independently recomputed and matching exactly), S11 (git state, with the one-file drift noted above) |
| B14 | End-card restatement of all headline figures | Restates B00/B08/B13's already-confirmed claims; no new factual content |
| B15 | Outro sign-off | Original to this build, not a factual claim |

## Verbatim quote law

Three strings should appear on screen close to verbatim, per the script:

1. **The §3.4 quote (B01):** `"web/static/index.html and app.js are, as of
   this document, completely unmodified for Cross-Agent Validation."` —
   confirmed exact against `divij/cross-agent-validation-status.md` line 276.
2. **The earnings producer's docstring (B09):** `"…deliberately disjoint…"`
   — confirmed exact against `producers/earnings.py` line 10.
3. **The regex-truncation figure (B11):** `"13,971,000,000.0"` → `"000.0"` —
   confirmed exact against `self_report.py`'s `regex-truncates-comma-grouped-numbers`
   entry, run `515f263a`.

## Simplifications, declared

1. **B01's recap panel is deliberately generic** ("TWO AGENTS -> SAME
   COMPANY -> FLAG MISMATCHES" / accountability-layer chip), per the
   script's own "no new build" instruction — not a claim that this is the
   full mechanism, just a fast recap.
2. **B02's ledger rows show six representative entries, not all 14** — a
   legibility choice; the full count (14) and the exact status breakdown
   are stated in narration and shown in full in B13, not omitted from the
   reel, just not all listed row-by-row in B02's shorter recap beat.
3. **B03's retry-path visual uses illustrative file:line pairs in the
   layering-violation callback (B07)** — three plausible module paths, not
   necessarily the exact three files/lines the actual August 2026 session
   used when it deliberately broke the layering, since `logs/RUN_LOG.md`'s
   own entry for that session was read for its narrative claims but not
   mined for the specific three file:line pairs used in that one-time test.
4. **B08's 31-tile grid does not individually label each of the 31 runs**
   — a structural stand-in for "31 real runs," matching the corpus fixture's
   actual count, not a claim about which specific companies are shown where.

## Claims deliberately NOT made (carried forward from the script's own list)

- That the UI is "done" or "shipped" — nothing is committed; B13/B14 name
  the exact commit hash and file count.
- That the comparator "now catches fabrications" — the provenance markers
  made one fabrication *visible*; the comparator's own rule is unchanged,
  and `fabrication-not-caught` is still `OPEN` in the ledger (confirmed).
- That the over-flagging is "fixed" — B09 states the fix is upstream and
  explicitly out of scope for this period; `validation/cross_validation.py`
  was not modified.
- That "224 tests" is evidence of correctness — B12/B13 use it only as a
  delta, and B13 explicitly names three zero-test surfaces in the same beat.
- That the retry path is "proven" — B03 says it is *rendered*, and B13
  restates that it is still only observed against mock failures.
- That "zero for sixteen" means the comparator doesn't work — B14's close
  states the narrower, correct claim explicitly: the two producers were
  never asked the same question.

## Known gap not independently re-verifiable in this pass

The exact three file:line pairs used in the live August 2026 session when
the layering test was deliberately broken three times (B07's narrative)
were not re-derived from `logs/RUN_LOG.md` in this pass — the mechanism
(`test_layering.py`'s AST-based enforcement, confirmed present) and the
narrative claim (three violations, three named failures, restored) are both
confirmed; the specific file:line pairs shown in B07's scene are
illustrative placeholders, not a verbatim transcript of that session's
actual output. Flagged for the human reviewer per GATE P — if the specific
file:line pairs matter for accuracy, `logs/RUN_LOG.md`'s 2026-09-04 SOLID
entry should be re-read for the exact values before final render.
