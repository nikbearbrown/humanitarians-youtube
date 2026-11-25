# SOURCES — It Never Ran

Every figure in this reel comes from one of two places: the mycroft repository
at a named commit, or a standalone interpreter run outside it.

## Primary — the repository

| # | Source | Access | Used for |
|---|---|---|---|
| 1 | `D:\Projects\mycroft` @ `08b92d3`, branch `fix/conformance-multidoc-yaml` | local, read-only (`git show`, `git blame`, `git ls-tree`) | the whole reel |
| 2 | `scripts/conformance.mjs` @ `08b92d3^` (the parent) | `git show` | B04 — the verbatim mangling line |
| 3 | `scripts/conformance.mjs` @ `08b92d3` | `git show` | B05 `list()` fix, B07 import discipline, B09 `DEFAULT_PATHS`/`SKIP` |
| 4 | the commit message of `08b92d3` | `git log -1` | B09 exclusions and the untested-version note; B08 the 1,039 -> 1,853 totals |
| 5 | `git blame scripts/conformance.mjs` @ `08b92d3^` | local | B06, B07, B08 — the 2026-10-09 date and authorship |
| 6 | mycroft @ `b425b19` (episode 12's subject) | local | B01 — the continuity premise |

## Reproduction — run standalone, outside the repository

| # | What | Where | Used for |
|---|---|---|---|
| 7 | `yaml.safe_load()` on a two-document fixture | session scratchpad, `python -c` | B05 panel 1 — `ComposerError` |
| 8 | the mangled one-line script, reconstructed from the parent's transform | session scratchpad, `python -c` | B04, B05 panel 2 — `SyntaxError` |
| 9 | `yaml.safe_load_all()` without `list()` on an invalid file | session scratchpad, `python -c` | B05 panel 3 — the silent pass |

Fixtures were written to the session scratchpad and nothing was written into
`D:\Projects\mycroft`.

## Not run, on purpose

- `snickerdoodle gate` — writes a decision record into the repository.
- `node scripts/conformance.mjs` — compiles Python and leaves `__pycache__`.

Both are the reason the 1,039 -> 1,853 totals are attributed rather than
reproduced. See FACTCHECK.md.

## Not used

No external source, no web page, no third-party claim. This is a work report
about one commit in one repository.
