# FACTCHECK — hai-repo-sensei-week-3

Status: **GATE F — drafted 2026-10-26. 6 rows VERIFIED-LOCAL, 1 row SPEC-ASSERTED, 2 rows ARGUMENT.**

Verdict vocabulary: **VERIFIED-LOCAL** = measured on this machine during the build against the
working clone at `~/conductor/repos/repo-sensei`, reproducible by re-running the named command.
**SPEC-ASSERTED** = a statement of intent taken from the project's own README. **ARGUMENT** =
reasoning or advice, not a measurement.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B00 | repo-sensei is nine days old | **VERIFIED-LOCAL** | GitHub API `created_at` = 2026-10-17T18:40:19Z; this build ran 2026-10-26. Nine days | Restate if the cut slips past 2026-10-27 |
| 2 | B01/B02 | It indexes a codebase, answers with cited evidence, traces a feature across layers, and proposes fixes as pull requests | SPEC-ASSERTED | The repository README, verbatim: *"it indexes a codebase, answers questions about it with cited evidence, traces features across layers (UI → API → database), and proposes reviewed fixes as pull requests."* This is stated intent for a project marked "under active development", not a demonstrated capability | Keep it framed as what the project is for. Do not narrate it as a shipped feature or show a fake demo |
| 3 | B04 | 101,318 lines of Python and TypeScript | **VERIFIED-LOCAL** | `git ls-files \| grep -E "\.(py\|ts\|tsx)$" \| xargs wc -l` on the working clone at commit 34bedaf → 101318. Tracked files only; node_modules excluded by construction | Recount at publish time |
| 4 | B04 | 770 files across apps, packages and workers | **VERIFIED-LOCAL** | `git ls-files \| wc -l` → 770. Top-level split: apps 505, packages 312, workers 44, scripts 17, infra 15 (from the GitHub tree API, same commit) | — |
| 5 | B04 | 132 test files and 179 commits | **VERIFIED-LOCAL** | `git ls-files \| grep -cE "(test_.*\.py\|.*_test\.py\|.*\.test\.tsx?)"` → 132. `git log --oneline \| wc -l` → 179 | Both move daily — recount before publishing |
| 6 | B05 | It parses with tree-sitter, 18 query files, covering Python, TypeScript and JavaScript | **VERIFIED-LOCAL** | `git ls-files \| grep "\.scm$" \| wc -l` → 18. Grammar directories: python, typescript, javascript, jsx, ecma. Dependencies include `tree-sitter`, `tree-sitter-python`, `tree-sitter-typescript`, `tree-sitter-javascript` | — |
| 7 | B05 | The card shows a real query that finds every method inside a class | **VERIFIED-LOCAL** | Quoted from `packages/engine/src/sensei_engine/parse/queries/python/defs.scm`, whose own comment reads *"Methods: functions directly in a class body."* Trimmed to fit the card; structure unchanged | Re-trim rather than paraphrase if the query changes |
| 8 | B06 | An answer that cannot be checked is worse than no answer | **ARGUMENT** | The project's design position and the fellow's own, carried over from the TAssist work. Reasoning, not a measurement | Keep as a stated conviction |
| 9 | B06 | "where a confident wrong answer gets merged and ships" | **ARGUMENT** | Rhetorical justification. No incident is cited and none should be implied | — |

## Honesty notes

- **Narration is AI-generated** (Kokoro `am_onyx`), disclosed aloud in B00. The project and the
  measurements are the fellow's own.
- **Row 2 is the one to watch.** The four capabilities are the README's stated purpose for a
  project nine days old and explicitly "under active development". The reel describes what it is
  being built to do and never claims a working demonstration. No screenshot of a result is shown,
  deliberately — there is no shipped output to show yet.
- **Rows 3 through 7 are measurements**, taken from the working clone at commit `34bedaf` on
  2026-10-26, not from the README.
- **The counts are live.** Lines, files, tests and commits all change with every push. They were
  true at build time and should be re-measured if the cut is published later.
