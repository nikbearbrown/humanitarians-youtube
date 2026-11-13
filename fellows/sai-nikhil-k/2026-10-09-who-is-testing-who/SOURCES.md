# SOURCES — Who Is Testing Who?

## Provenance

- **What Sai supplied (2026-10-09):** the reference URL
  https://alexgherghe.com/articles/some-unit-tests-are-useless.html as the week's second,
  general reel. He chose the ONE idea and title from Claude's proposals and asked for no
  AI angle.
- **What Claude did:** read the essay in full (saved: `research/gherghe-2026-07-13.html`),
  ported its example to Python, wrote both suites, planted the bugs and refactors, ran
  coverage and mutmut, and re-read every outside figure at its source
  (`evidence/sources_check.out`).
- **LibKey:** not authenticated this session; the two papers were checked via Crossref
  (DOIs) and the authors' PDFs.

## Sources

| # | Source | Used for | Beat |
|---|---|---|---|
| 1 | Alexandru Gherghe, "A Lot Of Unit Tests Are Worse Than Useless", 2026-07-13 | the example, the claims, the quotes, the title | B00–B03, B06, B09 |
| 2 | André Schaffer, "Testing of Microservices", Spotify Engineering, 2018-01-11 | the honeycomb | B06 |
| 3 | Inozemtseva & Holmes, "Coverage Is Not Strongly Correlated with Test Suite Effectiveness", ICSE 2014, DOI 10.1145/2568225.2568271 | coverage vs effectiveness | B04, B07 |
| 4 | Just et al., "Are Mutants a Valid Substitute for Real Faults in Software Testing?", FSE 2014, DOI 10.1145/2635868.2635929 | mutants track real faults | B04 |
| 5 | mutmut 3.8.0 (PyPI), coverage.py 7.16.2, pytest 9.1.1 | the run | B04, B05 |

## Honesty log

- The essay shows only the success-path test. The mock suite here adds three more
  tests in the same style and unit tests for each collaborator that needs no mock, so
  the comparison is against the mock style at its best, not a strawman.
- The first draft of the bug list had "security check inverted"; it was replaced with
  B3 before any run, because the mock suite's own unit test of `SecurityService` would
  catch it and it is not a query/contract bug. Recorded so the choice is visible.
- The essay's Java (Spring, Mockito, Testcontainers) is stood in for by Python
  (`unittest.mock`, in-memory SQLite). The reel says "I ported it to Python".
- Mutants set aside from B05's percentages are listed in `mutation_run.out`; the raw
  scores with them included are in FACTCHECK.md.
