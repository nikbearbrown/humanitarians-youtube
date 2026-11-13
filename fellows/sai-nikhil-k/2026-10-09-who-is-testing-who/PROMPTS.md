# PROMPTS — Who Is Testing Who?

**There are no open generation slots in this reel.** All ten beats are registered
Remotion compositions. No image model, no stock, no paid call.

## B00 — the on-screen typed ask

> This unit test mocks all five of BookService's dependencies and verifies each one was called once. What behaviour does it actually test, and which bugs would it miss?

## B08 — the handoff prompt (typed on screen and discussed in narration)

> Here is one of my unit tests and the code it tests. List every assumption its mocks make about the real dependencies. For each, show the smallest bug in that dependency my test would still pass, and the integration test that would catch it.

## The executed scripts

| Script | Produces | Deps |
|---|---|---|
| `evidence/bookservice/experiment.py` | `experiment.out`, `.json` → B00, B02, B03, B07 | pytest |
| `evidence/bookservice/mutation_run.py` | `mutation_run.out`, `.json` → B04, B05, B06, B07 | pytest, coverage, mutmut 3 |
| fetch / PyMuPDF / Crossref | `evidence/sources_check.out` → B01–B04, B06 | network |
