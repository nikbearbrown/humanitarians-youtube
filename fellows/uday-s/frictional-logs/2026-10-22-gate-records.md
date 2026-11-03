# Frictional log — making `gate` generate what week five wrote by hand

**Date:** 2026-10-22 · **Branch:** `feat/gate-records` · **File:** `scripts/snickerdoodle.mjs`

> A frictional log is a short, dated, honest record of what was tried, where the work
> resisted, what was done about it, and what was learned. It lives beside the evidence
> it describes.

## What was tried

Make `snickerdoodle gate` produce records equivalent to the ones written by hand in week
five, rather than a thinner summary.

## Where the work resisted

- **The task said to build `gate`, which already existed.** It was built earlier in this
  session. Diffing a generated record against the hand-written one gave the real task:
  five fields missing (`evidence_files`, `evidence_observed`, `mode`, `run_log`, `scope`)
  and a `residual_risk` that was a generic default where the human had written 290
  characters of specifics.

- **Four rebases refused on 2106 phantom modified files.** `git diff` reported one changed
  file; `git diff-index HEAD`, which `rebase` uses, reported 2106. Hashing three of them
  by hand showed worktree, index and HEAD identical. The index stat cache had gone stale
  when 2120 files were rewritten outside git during the line-ending work. `git read-tree
  HEAD` rebuilt it and the 2106 dropped to 1 — the same churn that had been misread as
  noise three times earlier in the project.

- **The evidence set was nearly empty.** Deriving it from paths named in the gate's own
  test found 2 files for gate 3, because that test names *directories* whose artifacts sit
  two levels down. One-level expansion hashed the directories' children and missed all 26
  JSON files the gate is actually about.

- **Then it recorded six files as absent that were not missing.** Gate 4's test is
  `for s in tools/verify-provenance ingest/ingest-inputs ...` — those are loop *values*,
  not paths, and gate 6's names a `[DATE]` template. Both were recorded as `exists: false`,
  which asserts a missing file.

- **The date was a day ahead.** `toISOString()` is UTC, so a decision made on the 22nd
  recorded `2026-10-23` — in a record whose entire purpose is who decided what, when.

- **A stash pop left `.gitignore` conflicted, and the de-duplication I wrote to resolve it
  deleted both copies of the local-only entry** rather than one.

## What was done about it

- Derived the evidence set from the gate's own test rather than a hand-picked list, walking
  directories to depth 6 with a 60-file cap that records when it was hit. Gate 3 went from
  2 evidence files to 32; each gate now produces a different set, because each test names
  different things.

- Replaced `exists: false` with `resolved: false` plus a note naming the ambiguity — a
  token may be a loop value, a template, or a genuinely missing file, and the record says
  it does not distinguish them.

- Used the local date.

- Made `run_log` a *check* rather than an assertion: it looks for a `## <date>` entry and
  records whether one exists, so the record cannot point at a log entry nobody wrote.

- Added `residual_risk_stated`, so a default is visibly a default rather than passing as
  someone's judgment.

## What was learned

**Checking the premise took two minutes and changed the whole task.** "Build `gate`" would
have meant rewriting a working command. The diff against the hand-written record turned it
into five concrete gaps.

**An empty evidence set and a wrong one fail differently.** Two files looked plausible —
a record with evidence in it. Six absent files looked like a finding. Neither announced
itself; both had to be read.

**The honest version of a field is sometimes "I cannot tell".** `resolved: false` with a
note saying why is worth more than `exists: false`, which is a confident claim the tool has
no grounds for.

**The stale index was the session's longest-running friction.** It blocked three branch
operations and produced walls of phantom modified files that were dismissed as noise each
time. It had a one-command fix the whole way through.
