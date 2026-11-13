# Frictional log — the check verb, and a denominator that flattered the result

**Date:** 2026-10-15 · **Branch:** `feat/snickerdoodle-cli` · **File:** `scripts/snickerdoodle.mjs`

> A frictional log is a short, dated, honest record of what was tried, where the work
> resisted, what was done about it, and what was learned. It lives beside the evidence
> it describes.

## What was tried

Add `snickerdoodle check`: compare what a recipe documents against what its scripts
implement, without running anything, so the recipe/script mismatches found while building
`run` could be measured across all 97 recipes instead of discovered one failed run at a
time.

## Where the work resisted

- **The recipe I had already "fixed" was not clean.** Checking market-sentiment found five
  findings, including `--no-write` advertised on verify-provenance and never implemented —
  missed when I added `--sample` to that same script an hour earlier, because I fixed the
  flag that broke the run rather than the contract.

- **The first repo-wide summary understated the thing it was built to measure.** It
  reported `documented-not-built` at **4%**, reading as rare. The rate was 4% only because
  94 of 97 recipes have no scripts at all, so their flags cannot be compared — they were
  sitting in the denominator as implicit passes. Scored against the recipes where the
  finding is observable, it is **100%**.

- **The first correction was also wrong, and said so out loud.** Changing the denominator
  to "recipes with no missing scripts" produced `4/2 = 200%`, because a recipe can have
  some scripts present and others absent. The absurd number was the only reason I looked
  again; a plausible-but-wrong denominator would have shipped.

## What was done about it

- Scored each finding against the population it could be found in: flag findings against
  recipes with at least one script on disk, structural findings against all 97. The output
  states the denominator and why it differs, so the number cannot be read as the other one.

- Had the summary say what a share *means* — a finding in 97% of recipes is one defect in
  the template they share, not 94 defects — because the count alone invites filing 94
  tickets for one problem.

- Excluded `--input`/`--output` as plumbing. Every script has them and no Step Commands
  table documents them; counting them would have buried five real findings under six lines
  of noise per recipe.

- Read flags by parsing `add_argument` out of the source rather than running each script
  with `--help`. 582 scripts is a lot of subprocesses, and executing a file to find out
  what it accepts is a side effect a checker should not need.

## What was learned

**A denominator is a claim.** Both wrong versions produced a number that looked like a
measurement: 4% said "rare", 200% said "impossible". Only the second was obviously broken.
The first would have been quoted.

**The check found what the amended commit message had predicted.** That message said the
flag gap "almost certainly exists across all 97" and named this verb as the way to
establish it rather than guess. The guess was right, which is pleasant and entirely beside
the point — it is now measured, with the measurement's own limits stated.

**Building a tool to find a defect class found more of it in the code I had just written
than anywhere else.** The five findings in market-sentiment are all mine, from this week.
