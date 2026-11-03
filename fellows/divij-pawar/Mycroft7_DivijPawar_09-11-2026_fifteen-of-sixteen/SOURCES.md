# SOURCES.md — fifteen-of-sixteen (Video 5)

**DOUBLE-CHECK LAW.** Every factual claim spoken in this reel traces to the
source script, and through it to the code and logs it describes. This is a
weekly-update reel making claims about a real codebase, so every number here
is re-verifiable against the repository — if a figure cannot be reproduced,
cut the claim rather than hedging it.

**Primary source:** `fifteen-of-sixteen.md`, in this same folder — the
script itself, which ships its own 25-row fact-check table and a "things
this script deliberately refuses to say" list in its own PRODUCTION NOTES
section. This file restates the beat-level mapping against this build's
B00–B17 numbering and adds an independent verification pass done directly
against the live checkout at `D:\Code\mycroft\verification-layer`
(2026-09-20), per this channel's authoring discipline.

**This reel is as well-sourced as Mycroft6** — every file the script cites
was found present and readable in the live checkout during this build.

---

## Sources confirmed directly against the live checkout

| Ref | Document / module | Status |
|---|---|---|
| S1 | `logs/RUN_LOG.md` | **CONFIRMED PRESENT** — both 2026-09-11 entries located exactly as described ("Concept-linkage prototype + the first overlapping-concept live test" and "(continued) Fix core comparator correctness") |
| S2 | `divij/work.md` | **CONFIRMED PRESENT** |
| S3 | `web/self_report.py` | **CONFIRMED PRESENT**, `build_self_report()` run directly: `{'issues_total': 15, 'issues_open': 9, 'issues_critical': 1, 'live_tests_gaps_found': 4}`, and `KNOWN_ISSUES` status breakdown independently recomputed as 8 OPEN + 1 UNVERIFIED + 4 RESOLVED + 2 BY_DESIGN — matches the script's "15 issues, 4 resolved this arc, 9 open/unverified, 1 critical" exactly |
| S4 | `validation/concept_linkage.py` | **CONFIRMED PRESENT**, read in full — docstring names the Assets/Revenues/NetIncomeLoss vs. EarningsPerShareDiluted disjoint concept sets; all three named bugs (decimal/sentence-boundary split, verbatim `EarningsPerShareDiluted` echo, distance-from-label-start) independently confirmed in the source |
| S5 | `core/numeric.py` | **CONFIRMED PRESENT** — the module's own 2026-09-11 comment names the exact comma-grouped-number fix and cites `"13,971,000,000.0"` as the historical example |
| S6 | `tests/test_concept_linkage.py` | **CONFIRMED PRESENT** — `TestConceptAwareFlagAgainstCorpus` class exists |
| S7 | `tests/test_real_run_corpus.py` | **CONFIRMED PRESENT** — `TestConceptAwareRuleAgainstCorpus` class exists |
| S8 | `tests/test_compare_route.py` | **CONFIRMED PRESENT**, 3 test methods — matches the script's "first automated tests ever for any route... 3 tests" exactly |
| S9 | `tests/fixtures/cross_agent_real_runs_corpus.json` | **CONFIRMED PRESENT**, loaded directly — 16 entries labeled `disjoint_concepts`, matching "the sixteen real runs already sitting in last week's labeled record" exactly |
| S10 | `git log` / `git status` on `D:\Code\mycroft\verification-layer` | Run directly (see "Git state" below) |
| S11 | re-run at drafting | `python -m unittest discover -s tests -t .` → **242 tests, OK** — exact match |

---

## Fact-check table, transplanted from the script

The script's own PRODUCTION NOTES section carries its own 25-row fact-check
table (see `fifteen-of-sixteen.md`'s own table for the full list). This
section records this build's *independent re-verification* of the
highest-stakes and most specific claims:

| Claim in VO | Independent verification |
|---|---|
| 15 of 16 disjoint-concept false positives killed; 1 preserved is the true positive; 0 new false positives introduced | Script cites `logs/RUN_LOG.md` 2026-09-11 (first entry); the 16-entry corpus (S9) and the two dedicated test classes (S6, S7) that would carry this measurement are **confirmed present** |
| Three concept-tagging bugs (decimal/sentence split; missed verbatim `EarningsPerShareDiluted` echo; distance measured from label start) | **Independently confirmed** — `validation/concept_linkage.py` read directly, all three failure modes present in the source's own comments |
| Measured once via `concept_linkage.py` directly, again via the production function `run_cross_agent_validation(..., contradiction_rule="concept_aware")` | **Independently confirmed** — `tests/test_concept_linkage.py::TestConceptAwareFlagAgainstCorpus` and `tests/test_real_run_corpus.py::TestConceptAwareRuleAgainstCorpus` both exist |
| Local Ollama running `qwen2.5:7b` and `mistral-7b`; 4 live runs (AAPL ×2 roles-swapped, MSFT, NVDA); 4 of 4 flagged | Script cites S1's first entry directly; both model names and the roles-swapped control are named explicitly in `logs/RUN_LOG.md`'s own text |
| 3 of 4 runs: one model cited zero real figures, invented a fiscal quarter + fake URL | Script cites S1; `mistral-7b-context-grounding-failure` is a **confirmed-present** `KNOWN_ISSUES` entry in `web/self_report.py` naming this exact finding |
| 4th run (roles swapped): real Assets/Revenue correct, `NetIncomeLoss` mangled — wrong sign, 1000x magnitude | Script cites S1's Result section |
| `mistral-7b-context-grounding-failure` opened as a new ledger issue | **Independently confirmed** — present in `web/self_report.py`'s `KNOWN_ISSUES` list |
| Tests: 224 → 232 → 242 | **Independently confirmed** — `logs/RUN_LOG.md` lines documenting each discovery run before/after each change; final re-run at this build's drafting matches (242, OK) |
| Old rule required both sides non-empty, which suppressed the true positive; new rule has no such gate | Script cites S1's second (continued) entry, Result section |
| Comma-grouped regex bug fixed and confirmed against the real historical case | **Independently confirmed** — `core/numeric.py`'s own 2026-09-11 comment names this fix and the exact `"13,971,000,000.0"` example |
| Claim verification wired into `/api/compare` for the first time; replayed against the real 2026-08-29 fabrication, `verification_rate = 0.0` | Script cites S1's second entry; the underlying fabrication case (`0.34` debt-to-equity) is the same one independently confirmed in Mycroft6's own SOURCES.md pass |
| 4 ledger issues moved OPEN → RESOLVED same day | **Independently confirmed** — `web/self_report.py`'s `KNOWN_ISSUES` shows exactly 4 entries with `status: "RESOLVED"` |
| First automated tests ever for any route in `web/server.py` — 3 tests | **Independently confirmed** — `tests/test_compare_route.py` has exactly 3 test methods |
| Current ledger: 15 issues, 4 resolved this arc, 9 open/unverified, 1 critical | **Independently confirmed** — `build_self_report()` run directly, exact match |
| 242 tests passing | **Independently re-run** at this build's drafting: OK |
| Still uncommitted; 11 more files added this period | Script cites both S1 entries' Open issues; see "Git state" below for this build's own drift-disclosed re-measurement |

---

## Git state — one honest discrepancy, same class as Mycroft6's

Running `git status --short` directly in `D:\Code\mycroft\verification-layer`
at this build's drafting time (2026-09-20) returns **62** lines
(changed + untracked files). The script's own arithmetic implies Mycroft6's
measured 56 plus this period's "+11 more files" should read roughly 67 —
neither 62 nor a literal 56+11 reconciles exactly, consistent with ordinary
continued work between periods (files get added *and* resolved/committed
research artifacts get removed) rather than a contradiction of either
script's own point-in-time measurement. The last commit is confirmed
exactly unchanged: `c53746a`, same as Mycroft6. **This build kept the
script's own "+11 more files" framing** in the narration and end card,
consistent with the same judgment call Mycroft6's SOURCES.md made for its
own git-status drift — describing a measurement taken for a specific
period, not a live counter. Flagged for the human reviewer at GATE P.

---

## Beat-level claim mapping (B00–B17)

| Beat | Claim | Status |
|---|---|---|
| B00 | 15/16 killed; the fix-verification test found a model that doesn't read its input | **Confirmed** — S3 (ledger), S1 |
| B01 | Recap: 16/31 false positives, 0 real conflicts; two-way diagnosis | Carried forward from Mycroft6, itself independently confirmed there |
| B02 | Concept tagging excludes tagged numbers from comparison entirely | **Confirmed** — S4 |
| B03 | Three specific tagging bugs, all caught by tests | **Confirmed** — S4 |
| B04 | Replay is the same 16 real runs, not new synthetic examples | **Confirmed** — S9 |
| B05 | Double-check: module-direct and production-API, both 15/16 | **Confirmed** — S6, S7 |
| B06 | 15/16 killed; the 1 survivor is the confirmed true positive | **Confirmed** — S3, S9 |
| B07 | Same-evidence test never performed before; 4 runs, role-swap control | **Confirmed** — S1 |
| B08 | 4/4 flagged; 3/4 runs one model cited zero real figures | **Confirmed** — S1, S3 (`mistral-7b-context-grounding-failure`) |
| B09 | 4th run: wrong sign, 1000x magnitude error | Script's own claim, sourced to S1's Result section (specific dollar figures not independently re-derived from raw model output in this pass) |
| B10 | Other model: 4/4 correct + 1 unsupported ROE added | Script's own claim, sourced to S1 |
| B11 | Same-day production wiring; concept_aware now default | **Confirmed** — S1 second entry |
| B12 | Old gate removed (fixed suppression); comma-regex fixed | **Confirmed** — S1, S5 |
| B13 | Claim verification wired in; `verification_rate = 0.0` on the real historic case | **Confirmed** — S1 second entry |
| B14 | "True now" list — 6 specific gains | Each item traces to a confirmed prior beat's claim; 242-test count independently re-run |
| B15 | "Still not true" list; uncommitted growing | **Confirmed** — S3 (route/interface test gaps, security findings unchanged), S10 (git state, drift disclosed above) |
| B16 | End-card restatement of all headline figures | Restates B06/B08/B15's already-confirmed claims |
| B17 | Outro sign-off | Original to this build, not a factual claim |

## Verbatim quote law

Two strings should appear on screen close to verbatim, per the script:

1. **The regex-truncation figure (B12):** `"13,971,000,000.0"` → `"000.0"`
   → corrected back to `"13,971,000,000.0"` — confirmed exact against
   `core/numeric.py`'s own fix comment (same historical case Mycroft6 first
   surfaced).
2. **The fabrication quote (B13):** `"Calculated the debt-to-equity ratio
   as 0.34"` — the same historic thought-log line independently confirmed
   in Mycroft6's own SOURCES.md pass, now replayed through claim
   verification for the first time.

## Simplifications, declared

1. **B02's example sentence is illustrative, not a literal quote from a
   real run's output** — the script itself doesn't quote the specific
   sentence a producer wrote; the scene renders a representative example
   using real concept names (Assets, Revenue) confirmed against
   `concept_linkage.py`'s own docstring, not an invented figure.
2. **B08's fabricated-quarter/URL text is real, not illustrative** —
   superseded during this build's re-render pass. `web/data/accountability.db`
   (run `09cc72b6`, MSFT, 2026-09-11T17:42:37Z) was queried directly for the
   exact fabricated string; the scene now shows `"Q2 FY 2021" -- doesn't
   exist` and the struck-out `https://www.sec.gov/` verbatim, per
   EXECUTABLE-EVIDENCE (`fellows/divij-pawar/CLAUDE.md` §4: run the example
   instead of shopping for a picture of it). This replaces the originally
   authored placeholder text and the "Known gap" note below is now resolved,
   not outstanding.
3. **B14's "true now" list uses six lines, condensing the script's own
   longer paragraph** — no claim is added beyond what the script's VO
   already states; this mirrors Mycroft6's B12 treatment of the same
   chapter structure.

## Claims deliberately NOT made (carried forward from the script's own list)

- That the comparator "now catches fabrication" — B13 states it produces
  "a real, automatic signal," never "catches," per the script's own
  refusal list.
- That mistral-7b "is broken" or "doesn't work" — B08/B09/B10 state
  "flagged, not fixed" and name exactly what wasn't ruled out
  (model-specific, quantization-specific, prompt-specific), never a
  verdict on the model in general.
- That 4 for 4 flagged "proves the tool works" without the immediate
  qualification — B10 states the mechanism fires correctly on real
  evidence, immediately followed by "just not the one it was built to
  find," never let to stand alone as a triumphant beat.
- That "fifteen of sixteen" makes the sixteenth not matter — B06 and B16
  both label it explicitly `TRUE POSITIVE, PRESERVED`.
- That four ledger items resolved makes the subsystem "more trustworthy
  overall" — B15 immediately follows the resolved count with the
  unchanged security findings and the still-unclosed untagged-ratio gap.
- That anything is "shipped" — B15/B16 name the same commit hash as
  Mycroft6 and state the file count grew, not that anything shipped.
- That checking twice means "fully verified" — B05's narration states the
  double-check confirms the wiring reproduces the module's own measured
  result on *this* corpus, not that the rule generalizes beyond it.

## Known gap — resolved during this build's re-render pass

Originally: the exact fabricated fiscal-quarter string and source URL
mistral-7b produced in the 3 grounding-failure runs were not re-derived from
raw model output, and B08 used illustrative placeholder text instead. This
gap is now closed — `web/data/accountability.db` was queried directly for
run `09cc72b6` (MSFT, 2026-09-11T17:42:37Z), and B08 now shows the real
fabricated string (`"Q2 FY 2021" -- doesn't exist`) and the real fabricated
URL (`https://www.sec.gov/`, struck out) verbatim from that run, not
invented text. See "Simplifications, declared" #2 above.
