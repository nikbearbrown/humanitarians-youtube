# Frictional log — building the CLI that 97 recipes already documented

**Date:** 2026-10-15 · **Branch:** `feat/snickerdoodle-cli` · **File:** `scripts/snickerdoodle.mjs`

> A frictional log is a short, dated, honest record of what was tried, where the work
> resisted, what was done about it, and what was learned. It lives beside the evidence
> it describes.

## What was tried

Build `snickerdoodle run` and `snickerdoodle gate` — the commands 97 of 99 recipes tell
the reader to run, and which had never existed. In practice the steps were being invoked
by hand as `python3 scripts/<layer>/<recipe>-<step>.py`.

## Where the work resisted

- **The spec existed 1444 times and had to be read, not invented.** Extracting the
  documented command shapes gave exactly two verbs — `run R --step S` (576 instances) and
  `gate R --gate N --decision approve --note T` (576) — with six step slugs identical
  across all 96 recipes. Writing a CLI from imagination would have produced something
  subtly different from what every recipe promises.

- **The recipe promised flags the scripts never implemented.** Every Step Commands row
  advertises `--sample`; not one of the six scripts accepted it. The first full run died
  at step 1 on `unrecognized arguments`.

- **And the scripts had a flag the recipe never documented.** `--fixture-set` exists in
  five of them and appears in no recipe. A mismatch in both directions at once.

- **My own fix made it worse.** I special-cased `--fixture-set` to "ride along wherever
  `--sample` is allowed", reasoning it was an argument to `--sample` rather than a
  capability. It was then passed straight to the one step that does not implement it —
  precisely the guessing the flag filter exists to prevent.

- **The gate tests failed for a reason that had nothing to do with the gates.** Gate 3
  reported exit 1 under the CLI and exit 0 in the shell. Node's `shell: true` uses
  cmd.exe on Windows, which cannot run `find ... -exec ... \;`. A shell mismatch was
  about to be recorded as real gate evidence.

- **The CLI let me approve the live-action gate with `--note "x"`.** Gate 5 authorises a
  model call, a Slack message and an email. Its test passes because nothing has performed
  a live call — which is evidence that nothing *has* run, never evidence that running is
  approved. The first version happily recorded that as an approval.

- **Testing the gate verb overwrote real gate records.** Five hand-written decisions,
  carrying evidence hashes and residual risk, were replaced by records whose note was `x`.

## What was done about it

- Read the spec out of the recipes and built to it, rather than designing a CLI and
  hoping the recipes matched.

- Made the recipe the configuration. No config file, no recipe registry: steps, scripts,
  gates and tests are parsed from the four tables every recipe already carries, so there
  is nothing that can drift from it.

- Resolved both flag mismatches **towards the recipe**, since P6 makes it authoritative
  for intent: added `--sample` to all six scripts, and documented `--fixture-set` in the
  recipe for the five that implement it. Then deleted the ride-along special case, so the
  table decides and the CLI guesses nothing.

- Made `--sample` an assertion rather than a no-op: it reads the run envelope and refuses
  to run if the mode is anything but sample, so the flag cannot ride along on a live run.

- Ran gate tests in a POSIX shell explicitly, and made an unavailable shell report itself
  as such instead of as a failed gate.

- Made approving a live-action gate require a second deliberate act, `--authorize-live`,
  and derived *which* gates those are from the recipe's own wording rather than hardcoding
  gate 5 — the number is a fact about this template, not about gates.

- Restored all five gate records from git and verified 0 modified.

## What was learned

**A passing test is not always evidence for the thing being approved.** Gate 5's test is
negative by construction: it passes while nothing has run. Treating "the test is green"
as grounds for approval inverts its meaning. That distinction has no general detector —
it had to be read out of what the gate actually governs.

**Writing the runner is what exposed the recipe/script mismatches.** Both flag
disagreements had been sitting in the repo for weeks, invisible because every invocation
was typed by hand, by someone who knew what the scripts accepted. The documented interface
was never exercised, so nothing tested whether it was true.

**The special case was the bug.** Every genuine problem here was solved by deferring to
the recipe; the one thing that broke was the moment I decided I knew better than the table
and let a flag through on a rule of my own.
