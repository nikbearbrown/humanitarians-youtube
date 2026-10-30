# Frictional log — teaching `check` the difference between unbuilt and broken

**Date:** 2026-10-30 · **Branch:** `fix/check-status-awareness`

> A frictional log is a short, dated, honest record of what was tried, where the work
> resisted, what was done about it, and what was learned. It lives beside the evidence
> it describes.

## What was tried

Make `snickerdoodle check` read a recipe's lifecycle status, so a missing script counts as
a defect only when the recipe claims it should exist.

## Where the work resisted

- **The tool I wrote two weeks ago overstated the problem by about 4x.** It reported 725
  findings, of which 554 were "this step has no script" in recipes that are DRAFT and
  therefore correctly describing unbuilt work. The ~170 real contract defects were buried
  under them, and the headline number was the one I had been quoting.

- **Deciding where the line falls needed the constitution, not an opinion.** The answer is
  exact: a `DEV` todo closes on "script exists", and `DRAFT -> SPECIFIED` requires zero open
  todos, so scripts are required from SPECIFIED onward and their absence at DRAFT is what
  DRAFT means.

- **A heredoc replacement failed its first assertion and silently skipped the rest**, so the
  detection changed while the reporting did not — the output showed the new finding kind
  while still counting everything as a defect. The third time this session that routing an
  edit through a shell has mangled it; switching to direct edits fixed it immediately.

- **The success message then lied.** A DRAFT recipe with no defects printed "every declared
  step has a script, and its flags match what the script implements" — about six steps with
  no scripts at all.

## What was done about it

- Gave findings a severity: `defect` contradicts something the recipe claims, `expected` is
  the honest state of unbuilt work. The headline counts defects; unbuilt steps are reported
  separately with the reason they are not counted.

- Added `no-lifecycle-status` as its own defect, since the constitution requires frontmatter
  on every recipe and 91 of 97 have none. That is a real finding, not a side effect of
  measuring something else.

- Rewrote the clean message so "no defects" on an unbuilt DRAFT says what it actually means:
  nothing contradicts the recipe's claims, and 6 of its 6 steps are unbuilt.

**725 findings became 171 defects, with 554 unbuilt steps named separately.**

## What was learned

**A measurement that counts honest states as failures makes the real failures invisible.**
Nothing was wrong with the detection — every one of those 554 observations was true. The
error was in the arithmetic that treated "not done yet" and "claims to be done and is not"
as the same thing.

**Severity is part of a finding, not a presentation detail.** Adding it changed what the
tool means, not how it looks: the same 725 observations, read correctly, say something
different about the repo.

**I quoted the wrong number for two weeks**, including in a commit message and in a summary
of what to do next. The tool was confidently precise and precisely wrong.
