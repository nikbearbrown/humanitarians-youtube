# Frictional log — unhiding the step scripts from conformance

**Date:** 2026-10-09 · **File:** `scripts/conformance.mjs` · **Branch:** `fix/conformance-skip-list`

> A frictional log is a short, dated, honest record of what was tried, where the work
> resisted, what was done about it, and what was learned. It lives beside the evidence
> it describes.

## What was tried

Remove `data`, `ingest`, `gigo` and `tools` from the conformance skip list, so
`npm run verify` actually reads a recipe's step scripts instead of skipping all of them.

## Where the work resisted

- **The skip list was hiding 476 Python files** — the entire executable surface of 99
  recipes. The default run checked 187 files and **zero** Python. Two market-sentiment PRs
  passed CI without CI compiling a single line of their pipeline code.

- **Removing the entries made the run eleven times slower.** 6 seconds became 63. The script
  spawns one interpreter per file at roughly 130ms each, so 476 more files cost ~62s. A check
  nobody waits for is a check that stops being run — the fix would have quietly undone itself.

- **Batching appeared to work, then didn't.** Compiling all 476 in one `py_compile` call took
  1.6s in the shell. Wired into the script, the run was still 63 seconds.

- **The reason was a wrong limit.** `cmd.exe` caps a command line at **8191** characters, not
  the 32767 usually quoted for `CreateProcess`. At ~150 paths the spawn failed with "The
  command line is too long", the code fell back to per-file, and everything still passed — so
  the only symptom was the clock.

- **The skip list could not simply be emptied.** `data` also covered `data/mycroft-main`,
  which is quarantined Tier 3, and `data/private`, which must never be read. Those need
  skipping for *where they are*, which a basename rule cannot express — it would skip every
  directory of that name anywhere in the repo.

## What was done about it

- Split the rule in two: a basename `SKIP` for genuinely universal non-source (binaries,
  build scratch, dependencies), and a `SKIP_PREFIXES` list for paths skipped by location —
  the three quarantined `mycroft-main` trees and `data/private`.

- Batched the Python and YAML checks with length-aware chunking at a 6000-character budget,
  well under the real cap. On failure the batch falls back to per-file, because a batch proves
  a failure exists but cannot say which file caused it.

- Added `data/raw` and `data/verified` to the default surface. Gate 3 of every pipeline recipe
  asks whether its JSON parses; this is that check, run once for the repo.

- Verified by breaking things rather than by passing: appended a syntax error to a step script
  (caught, named), truncated a run envelope (caught, named), confirmed zero quarantined or
  private files leak in, and confirmed an explicitly-named file inside a skipped tree is still
  checked.

**Result: 187 files in 6.0s → 743 files in 3.9s.** Four times the coverage, faster than before.

## What was learned

**A skip list is a silent failure mode.** Nothing was broken, no test failed, no error was
logged. The command said "✓ all conform" while never opening the files that matter most. The
cost of the gap was invisible precisely because the check was green.

**Two different numbers are quoted for the Windows command-line limit, and the smaller one is
the real one.** 32767 is `CreateProcess`; 8191 is `cmd.exe`, which is what actually runs. The
failure mode was a performance regression, not an error — the fallback caught it and carried
on, so only timing revealed that the fast path never ran.

**Making the check faster was part of making it correct.** The honest version of this fix is
not "check more files"; it is "check more files and still finish in under four seconds".
Otherwise the next person adds the skips back, with a good reason.
