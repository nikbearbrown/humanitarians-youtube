# SOURCES — Monorepos vs. Polyrepos

Primary: R. Potvin & J. Levenberg, "Why Google Stores Billions of Lines of Code in a Single Repository", Communications of the ACM 59(7), 2016. DOI 10.1145/2854146. Figures are a January 2015 snapshot: ~2 billion lines of code, 9 million source files, 25,000+ developers, ~35 million commits.
Git sparse checkout: `git sparse-checkout` documentation — https://git-scm.com/docs/git-sparse-checkout (git 2.52.0 used for the evidence).
Remote caching: Bazel remote caching documentation — https://bazel.build/remote/caching (content-addressed action cache shared across machines).
Brief supplied by the requester (Likhith); the 7 points were checked against the sources above (2026-10-21).

## Executable evidence
- `evidence/mono_demo.sh` → `evidence/mono_demo.out.txt`. Throwaway toy monorepo (8 projects × 50 files + 3 source files = 403 files, fixed commit dates). One commit `a8f51ce` renames `login`→`signIn` in `libs/auth` and both callers (3 files, 3 projects). A blob-filtered clone with `git sparse-checkout set apps/web libs/auth` puts 102 of 403 files on disk. B05 and B07 show this output.
- `evidence/build_cache_toy.py` (deterministic, no randomness). Cache key = hash(sources + dependency keys). Build 1: 8 built / 0 reused; build 2 (same commit, new machine): 0 / 8; build 3 (edit libs/auth): 4 built (libs/auth, apps/web, apps/mobile, services/billing) / 4 reused. B08 shows this output.

## Corrections / de-sensationalising
- Google's Piper is not a git repository, and Google's own workflow uses CitC (a cloud workspace that fetches files on demand), not `git sparse-checkout`. The reel says "big tech" techniques and shows git's version of the idea on a toy repo; it never claims Google runs git.
- Google's numbers are dated on screen ("Jan 2015") and kept approximate ("≈2.0 billion", "25k+"); no current counts are claimed.
- "Dependencies stay in sync automatically" is softened to "stay in sync": a monorepo has one version of each internal library at any commit, but third-party pinning (e.g. a one-version policy) is a convention teams enforce, not automatic.
- B06's bars are illustrative (labelled on screen); no timings are claimed.
- B05's "still on auth v1" polyrepo row is an illustrative example of version drift, not recorded output.
