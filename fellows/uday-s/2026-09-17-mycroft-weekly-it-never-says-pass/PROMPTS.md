# PROMPTS — It Never Says Pass

## Open slots: none

## The ask that found this episode

Each episode's title has come from the code's own load-bearing rule, and this
one was no exception — but finding it needed the right question. Not "what does
step 6 do", which produces a feature list. Instead:

```
claude "what does this step REFUSE to conclude, and where does it say so?"
```

That surfaced the line the episode is named for — *an audit reports what it
found; it never says "pass"* — and, one level down, the gate-4 note where the
report criticises one of its own gates in writing.

## The series, four episodes on

Each title came from a rule written in the source:

```
ep 1   Build the Defects First   (the corpus, before the validators)
ep 2   Transport, Do Not Repair  (ingest's docstring)
ep 3   Both Sets Scored 64       (a live comparison, not a docstring)
ep 4   It Never Says Pass        (the report's own rule)
```

Three of four were sitting in a docstring. **Read the comments before the
code** — the load-bearing rule is usually written down, and it is usually more
interesting than the diff.

## Reusable spine — stable at four episodes

```
claude "author a cli-explainer beat sheet for <commit>: INTRO (name), PROBLEM
(carry the previous episode's ledger forward), FRAMEWORK (a reusable rubric
shown BEFORE any example), two CLI→CODE→OUTPUT cycles, a falsifiability beat
the framework PREDICTS, SUMMARY (the ledger), NEXT STEPS, OUTRO. Re-derive
every number from a live run, never from the commit message."
```
