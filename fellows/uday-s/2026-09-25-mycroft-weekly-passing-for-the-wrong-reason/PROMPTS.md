# PROMPTS — Passing For The Wrong Reason

## Open slots: none

## The ask that found this episode

The previous four episodes each found their subject a different way. This one
was handed over by the series itself: episode 4 ended with a task for the
viewer, and this commit is that task run on the repo. So the useful ask was
simply to check whether the criticism had been answered — and then to go
further than the commit message:

```
claude "run the OLD version of this test against the CURRENT tree. Does it
still pass? If so, show me what it passes on."
```

It does still pass, on template text, with no approval record anywhere and a
`gate-decisions/` folder holding four real records for other gates. That is a
demonstration rather than an assertion, and it is stronger than anything the
commit message claims.

**The move: don't just read that a bug was fixed — re-run the old code against
the new tree and watch it still be wrong.**

## The ask that produced the falsifiability beat

```
claude "the fix passes. Enumerate every reason it could be passing, and tell
me which one is actually true right now."
```

Answer: not "a human cleared it" but "live mode is unimplemented, so the
failing condition cannot occur". Same green, entirely different meaning — and
the commit was already honest about it, which is what made it usable.

## The series, five episodes on

Each title came from a rule or a finding in the source:

```
ep 1  Build the Defects First        the corpus before the validators
ep 2  Transport, Do Not Repair       ingest's own docstring
ep 3  Both Sets Scored 64            a live comparison of two runs
ep 4  It Never Says Pass             the report's own rule
ep 5  Passing For The Wrong Reason   the gate's own honesty about itself
```

## Reusable spine — stable at five episodes

```
claude "author a cli-explainer beat sheet for <commit>: INTRO (name), PROBLEM
(carry the previous episode's thread forward), FRAMEWORK (a reusable rubric
shown BEFORE any example), two CLI→CODE→OUTPUT cycles, a falsifiability beat
the framework PREDICTS, SUMMARY (the ledger), NEXT STEPS, OUTRO. Re-derive
every number by running something, never from the commit message."
```
