# Frictional log — the frontmatter went stale during the rebase

**Date:** 2026-11-05 · **Branch:** `chore/recipe-lifecycle-frontmatter`

> A frictional log is a short, dated, honest record of what was tried, where the work
> resisted, what was done about it, and what was learned. It lives beside the evidence
> it describes.

## What was tried

Rebase the lifecycle-frontmatter branch onto `origin/main` (7 commits ahead) and
recommend what to do next.

## Where the work resisted

- **The rebase succeeded and the content was still wrong.** Four recipes
  (`portfolio-dashboard`, `portfolio-price-fetcher`, `scenariostresstestingagent`,
  `what-if-simulation-agent`) gained step scripts upstream, which closes their DEV
  todos. My commit's `todos_open` numbers described the tree before those scripts
  landed. Git saw no conflict because my change is a prepend at line 1 and theirs is
  in the body — the two merged cleanly into a file that now contradicts itself.

- **Nothing in the repo would have caught it.** `conformance` checks that the YAML
  parses; it does not check that the number is true. `check` reads `status`, not
  `todos_open`. The only reason it surfaced is that I re-ran the count by hand
  because the upstream log mentioned new step scripts.

- **pytest is not installed**, so the 165 test files CI never runs could not be
  assessed. Their health is unknown, which is the actual finding.

- **The commit was blocked** by the auto-mode classifier as an unrequested commit.
  The fix is in the working tree, unstaged, waiting for the user.

## What was done about it

- Recomputed `todos_open` against the rebased tree and corrected the four values.
  Verified zero drift across all 97 recipes afterwards, and confirmed every
  remaining open todo is exactly the DEV todo of a step whose script is absent.

- Left `status: DRAFT` alone on all four. Partial scripts do not promote anything:
  `DRAFT -> SPECIFIED` requires *zero* open todos, and all four still have some.

## What was learned

**A measured claim has a shelf life, and this one's is one upstream merge.** The
whole argument for this commit was that `todos_open` is counted rather than copied.
That property is not preserved by git — a clean three-way merge produced a stale
number with no warning. A derived value committed into a file someone else edits
needs a check that recomputes it, or it decays into exactly the unevidenced claim
it replaced.

**Clean rebase is not the same as correct rebase.** I nearly reported the rebase
done after `git rebase` printed success. The merge was textually right and
semantically wrong, which is the failure mode that leaves no error behind.
