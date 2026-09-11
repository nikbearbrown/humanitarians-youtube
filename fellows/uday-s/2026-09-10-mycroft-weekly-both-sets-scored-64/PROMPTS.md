# PROMPTS — Both Sets Scored 64

## Open slots: none

## The ask that found this episode

Episode 2's lesson was "ask what the code refuses to do". This week the useful
ask was one level further in — not what the code refuses, but what its OUTPUT
conceals:

```
claude "run this pipeline on the clean fixture set and the deliberately
corrupted one, and diff the OUTPUTS — not the logs. What is identical that
should not be?"
```

That is what surfaced the centrepiece: both sets report the same overall score.
No amount of reading the code would have produced that beat; it needed two runs
and a comparison. **Run the thing twice on different inputs and diff what it
reports.**

## Reusable spine — the Mycroft weekly, now stable at three episodes

```
claude "author a cli-explainer beat sheet for <commit>: INTRO (name), PROBLEM
(carry the previous episode's ledger forward), FRAMEWORK (a reusable rubric
shown BEFORE any example), two CLI→CODE→OUTPUT cycles, a falsifiability beat
the framework PREDICTS, SUMMARY (the ledger), NEXT STEPS, OUTRO. Re-derive
every number from a live run, never from the commit message. CODE beats show
real source."
```

Each episode's title has come from the code's own load-bearing rule
(`TRANSPORT, DO NOT REPAIR`; `FLAG, DO NOT DROP`). Look there first.
