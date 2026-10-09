# FACTCHECK — Who Is Testing Who?

Figure by figure. Every number is asserted by `build_beats.py --check`, which reads
`evidence/bookservice/experiment.json` and `mutation_run.json` directly. Runs: Python
3.11.5, pytest 9.1.1, coverage 7.16.2, mutmut 3.8.0, 2026-10-09, this MacBook Pro.

## The essay (B00, B01, B02, B03, B06, B09)

Quotes re-read in the saved copy (`research/gherghe-2026-07-13.html`); verbatim text in
`evidence/sources_check.out`.

| On screen / spoken | Essay | Result |
|---|---|---|
| title "A Lot of Unit Tests Are Worse Than Useless", Alexandru Gherghe | page title, byline, 2026-07-13 | ✔ |
| B01 "it mirrors the method's implementation, not its behaviour" | "All this test does is to mirror the implementation of the method, not the behavior of the method." | ✔ paraphrase, attributed ("His point") |
| B02 "his broken assumptions about what would be returned" | "bugs in the queries or broken assumptions about what would be returned" | ✔ verbatim fragment |
| B03 "if a refactor means rewriting the tests, what assurance do they give anymore?" | "since refactoring means that we need to rewrite the tests anyways, what assurance do they give anymore?" | ✔ paraphrase, attributed ("He asks") |
| B06 pricing calculator as pure logic | "a pricing calculator that applies discounts based on a set of rules" | ✔ |
| B09 / title "Who is testing who?" | "you really have to ask yourself: who is testing who?" | ✔ |
| B06 "He is not against unit tests" | "I'm not saying that unit tests are always useless. They absolutely have their place." | ✔ |

## The port (B01)

`bookstore/service.py` reproduces `getBookById` line for line (validate → permission →
find → not-found → metric → map). `tests_mock/test_book_service_mock.py::
test_get_book_by_id_success` reproduces the essay's test: the same stubs, `assertNotNull`
→ `is not None`, `assertEquals(title)`, and five `verify(..., times(1))` →
`assert_called_once_with`. B01's chips are those five verifies plus the title assert.
"the title it told the mock mapper to return": the test stubs `to_dto` to return a DTO
titled "Book One" and asserts that title. ✔

## Bugs and refactors (B00, B02, B03, B07) — `experiment.out`

| Change | Mock suite (13 runs) | DB suite (4) |
|---|---|---|
| B1 query columns in the wrong order | passed | **caught** |
| B2 repository returns the raw row, not a Book | passed | **caught** |
| B3 missing id raises IndexError, not None | passed | **caught** |
| B4 metric name misspelled | **caught** | **caught** |
| B5 fetch counted before the existence check | **caught** | **caught** |
| R1 not-found check moved into the repository | **failed** | passed |
| R2 reply built in the service, not the mapper | **failed** | passed |

Mocks: caught 2/5, failed 2/2 refactors. DB: caught 5/5, failed 0/2. ✔ (asserted)
"Thirteen mock tests" = 13 pytest runs (10 functions; `test_validator_rejects` is
parametrized over 4 values). "Four tests" = 4 functions, 4 runs. Baseline: both suites
pass on the unchanged code (`experiment.out` first line). The changes are text patches
in `experiment.py`, each asserted to apply exactly once.

## The metric (B04) — algebra

- coverage = lines run / lines — coverage.py statement coverage (`num_statements`,
  `covered_lines`). service.py under the mock suite: 17 of 17 = 100%. ✔ (asserted)
- mutation score = mutants caught / mutants — mutmut's "killed" (a test failed on the
  mutant) over all mutants generated. ✔
- "Across thirty-one thousand test suites, once their size was held fixed, coverage was
  only weakly to moderately tied to catching faults": Inozemtseva & Holmes (ICSE 2014):
  "31,000 test suites" … "low to moderate correlation between coverage and effectiveness
  when the number of test cases in the suite is controlled for". ✔
- Card: "catching mutants tracks catching real faults": Just et al. (FSE 2014): "a
  statistically significant correlation between mutant detection and real fault
  detection, independently of code coverage" (357 real faults, 5 programs). ✔

## The run (B05) — `mutation_run.out`

| Row | Caught / behaviour mutants | % | Raw score (all mutants) |
|---|---|---|---|
| mocks, whole service | 33 / 42 | **78.6** | 33/55 = 60.0% |
| real DB, whole service | 41 / 42 | **97.6** | 41/55 = 74.5% |
| mocks, query code (repository.py) | 0 / 9 | **0** | 0/11 ("no tests": coverage 0/9 lines) |
| unit tests, pricing | 28 / 30 | **93.3** | 28/33 = 84.8% |

Set aside by `classify()`: 11 mutants that only change an exception message's text (no
suite checks messages) and 2 that only change the SQL's letter case (equivalent: SQLite
keywords and these identifiers are case-insensitive). Pricing: 3 message mutants.

- "Every mutant the mocks missed sits in that query code": the 9 behaviour mutants the
  mock suite did not kill are all in `repository.py`, all "no tests". ✔ (asserted)
- The DB suite's one miss: `self.counters[name] += 1 → = 1` in `MetricsService` (its
  tests increment once). The mock suite's unit test increments twice and kills it.
- Pricing's two misses: `p < 0 → p <= 0` and `p < 0 → p < 1` — no test has a
  zero-price item, a real gap (B06 "missed: a zero price"). ✔ (asserted)

## B06 — Spotify

"Spotify's testing honeycomb, which the essay cites, puts most tests there, at
integration": Schaffer, Spotify Engineering, 2018-01-11 — "we should focus on
Integration Tests, have a few Implementation Detail Tests and even fewer Integrated
Tests." The essay links it. ✔

## Verdict lines (B07)

Each line restates a figure above. No line starts with a digit.

## Rendered-frame math review (MATH-TYPESETTING.md) — both aspects

Looked at B04 in `media/B04.mp4` (3840×2160) at each reveal + 0.2 s (1.13, 2.98, 7.0 s —
reveals at 0.86 / 2.61 / 6.39) and at 15 / 66 / 97 %, and in `vertical/media/B04.mp4`
(2160×3840) at 50 / 97 %:

- Row 1 `coverage = lines run / lines`: upright roman words, bar spans both. ✔
- Row 2 `17/17 = 100% (service, mock tests)`: first render read "mock tests :" (mathtext
  spaces a colon as a relation); recast with the label in parentheses and re-rendered,
  2026-10-09. The % sign renders. ✔
- Row 3 `mutation score = mutants caught / mutants`: bar spans "mutants caught". ✔
- Rows reveal on their cue words and stay; last reveal 6.39 s, inside the 15 s comp. ✔
- Portrait: row 2 is the widest (width-limited to ~0.84 W) and still reads at 1080p; the
  title wraps to two lines clear of row 1; note and conditions clear the rows. ✔
