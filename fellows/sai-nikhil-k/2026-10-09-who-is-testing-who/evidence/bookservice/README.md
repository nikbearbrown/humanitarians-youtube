# bookservice — the essay's example, run both ways

A Python port of the `BookService` / `BookServiceTest` listing in Alexandru Gherghe,
"A Lot Of Unit Tests Are Worse Than Useless" (2026-07-13), plus the real collaborators,
so one service can be tested with five mocks and against a real database.

| Path | What |
|---|---|
| `bookstore/service.py` | `BookService.get_book_by_id`, line for line from the essay |
| `bookstore/parts.py`, `models.py` | validator, mapper, security, metrics; Book, BookDto |
| `bookstore/repository.py` | the repository the essay's test mocks — here real (stdlib `sqlite3`) |
| `bookstore/pricing.py` | pure logic: the essay's "pricing calculator" example |
| `tests_mock/` | the essay's test, ported, + 3 more in its style + unit tests for every collaborator that needs no mock (13 test runs) |
| `tests_db/` | the same four scenarios through the real pieces and an in-memory SQLite (4 tests) |
| `tests_pricing/` | 12 unit tests on `pricing.py`, no mocks |
| `experiment.py` → `experiment.out/.json` | 5 planted bugs + 2 behaviour-preserving refactors, one at a time, against both suites |
| `mutation_run.py` → `mutation_run.out/.json` | coverage.py + mutmut 3.8 on each suite, mutants classified (behaviour / message / sql-case) |

```bash
python -m venv v && v/bin/pip install pytest coverage mutmut   # pytest 9.1.1, coverage 7.16.2, mutmut 3.8.0 used
v/bin/python -m pytest -q tests_mock tests_db tests_pricing    # 29 passed
v/bin/python experiment.py   > experiment.out
v/bin/python mutation_run.py > mutation_run.out                # ~1 min; works in scratch copies
```
