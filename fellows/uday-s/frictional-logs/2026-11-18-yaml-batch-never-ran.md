# Frictional log — the YAML batch had never run, and my fix proved it

**Date:** 2026-11-18 · **Branch:** `fix/conformance-multidoc-yaml`

> A frictional log is a short, dated, honest record of what was tried, where the work
> resisted, what was done about it, and what was learned.

## What was tried

Week 2: switch conformance's YAML check from `safe_load` to `safe_load_all` so three valid
multi-document Kubernetes manifests stop failing, then widen `DEFAULT_PATHS` to the
contributor subsystems the week-1 map listed.

## Where the work resisted

- **The rebase conflicted on the one file I keep local.** Upstream changed `.gitignore`
  (pantry made local-only) and my stashed `frictional-logs/` entry collided with it. Resolved
  to upstream's committed file plus my two lines, left unstaged, and confirmed the folder is
  still ignored.

- **The fix did nothing.** After the one-line change, the valid multi-document test file
  still failed. The error text gave it away: the batch prints only the first line of an
  exception, and what came back was a later line — the per-file fallback's format. So the
  batch was not running at all.

- **It had never run.** An instrumented scratch copy showed `SyntaxError: unexpected
  character after line continuation character`. The runner built a shell string and turned
  each newline into a literal backslash-n, so Python got one line. Every YAML batch since I
  wrote it on 2026-10-09 threw and fell back silently. It looked correct the whole time
  because the fallback is correct for single-document files.

- **My probe lied to me first.** A standalone reproduction of the runner reported success,
  which briefly pointed me away from the real cause. Only instrumenting the actual code path
  settled it. I still do not know why the probe differed, and I have not chased it.

- **The ownership rule cut through one function.** The batch line was mine; the per-file
  fallback line was last changed by Divij in August, inside the six-month window; the
  shared import line is nikbearbrown's. So I fixed the batch, left his fallback on
  `safe_load`, and imported `execFileSync` on a new line instead of editing the old one. The
  fallback now runs only when the batch cannot start at all.

- **`safe_load_all` is lazy.** Swapping the call alone would parse nothing and pass every
  file — a fix that turns a false failure into a false pass. It needed `list()`, and a test
  whose only error is in the second document.

- **Another escape got eaten.** A Python string written through a heredoc left a single
  backslash in a YAML double-quoted value, which YAML read as a newline. Caught by parsing
  the file back; reworded so no escape is needed.

- **My own status file went stale within the hour.** I wrote "5 defects" into `status.md`,
  then `check --all` said 15 — ten undocumented flags that arrived upstream with #90. That
  recipe is someone else's recent work, so it is recorded, not edited.

## What was done about it

- Batch runner now passes its script with `execFileSync` and no shell; uses
  `list(yaml.safe_load_all(...))`. Verified both directions, and verified the batch path
  itself ran.
- Eight subsystems added to `DEFAULT_PATHS` (1,039 -> 1,853 files, all conforming);
  `congressional-signals/` and `archive/` left out with reasons in a comment beside the list.
  Local virtualenv names added to `SKIP`.
- Map, status and handoff updated; `pantry/` drift recorded; four modified lines, all mine.

## What was learned

**A fallback that gives the right answer hides a primary path that gives none.** The batch
was dead for five weeks and every result was correct. Nothing fails loudly when the thing
that fails has a quiet understudy. The only reason it surfaced is that the understudy had a
different bug from the one I was fixing.

**Change the check, then check that the change is what ran.** Correct output was not
evidence the new code executed — the old code produced the same output. The message format
was the tell.

**Ownership by line is finer-grained than ownership by file.** One function had three
authors. Respecting that cost a duplicate import and a fallback left as it was, and both are
written down so they do not read as oversights.
