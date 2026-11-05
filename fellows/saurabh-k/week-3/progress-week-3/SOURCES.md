# SOURCES — hai-repo-sensei-v2

Every number on screen was measured against the working clone at commit `34bedaf` on
2026-10-26, not read off the README. Claim-level verdicts are in [FACTCHECK.md](FACTCHECK.md).

## The project

**repo-sensei** — <https://github.com/K-sau07/repo-sensei>, created 2026-10-17T18:40:19Z.
The reel was built 2026-10-26, hence "nine days".

## What it is for (B02)

The repository README, verbatim:

> it indexes a codebase, answers questions about it with cited evidence, traces features
> across layers (UI → API → database), and proposes reviewed fixes as pull requests.

This is **stated intent** for a project the README marks "under active development", not a
demonstrated capability. The reel describes what it is being built to do and never claims a
working demonstration. No product screenshot appears anywhere, deliberately.

## The measurements (B13)

| Figure | Command |
|---|---|
| 101,318 lines | `git ls-files \| grep -E "\.(py\|ts\|tsx)$" \| xargs wc -l` |
| 770 files | `git ls-files \| wc -l` |
| 132 test files | `git ls-files \| grep -cE "(test_.*\.py\|.*_test\.py\|.*\.test\.tsx?)"` |
| 179 commits | `git log --oneline \| wc -l` |

Tracked files only, so `node_modules` is excluded by construction. All four move with every
push and should be re-measured if this is published later.

## The monorepo (B14)

Top-level split from the GitHub tree API at the same commit: `apps` 505 files,
`packages` 312, `workers` 44, `scripts` 17, `infra` 15. The four boxes shown are
`apps/web`, `apps/api`, `packages/engine` and `workers`.

## The parser (B07, B08, B15)

Dependencies include `tree-sitter`, `tree-sitter-python`, `tree-sitter-typescript` and
`tree-sitter-javascript`. `git ls-files | grep "\.scm$" | wc -l` → **18** query files,
under grammar directories `python`, `typescript`, `javascript`, `jsx`, `ecma`. The four
chips shown — defs, calls, imports, refs — match the four kinds the narration names.

The query on screen is quoted from
`packages/engine/src/sensei_engine/parse/queries/python/defs.scm`, whose own comment reads
*"Methods: functions directly in a class body."* It is trimmed to fit the card; the
structure is unchanged.

## Stack

FastAPI, Celery, Redis, Postgres (asyncpg, SQLAlchemy, alembic), Anthropic, tiktoken,
sqlglot, OpenTelemetry, structlog, Sentry, SSE, pydantic — read from the package manifests.

## Narration

Kokoro `am_onyx`, generated locally at $0.00, disclosed aloud in B00.
