# PROMPTS — Transport, Do Not Repair

## Open slots: none

Every beat renders from sources inside this folder — seven Remotion beats from
registered Claude components, six Manim beats from `scenes.py`.

## The weekly format, as a reusable ask

Week three of this format. The spine is now stable enough to be a swap rather
than a redesign:

```
claude "read the diff for <commit> and tell me the single idea it is evidence
for — not a list of what changed"

claude "author a cli-explainer beat sheet for <commit>: INTRO, PROBLEM,
FRAMEWORK (a reusable rubric shown BEFORE any example), two CLI→CODE→OUTPUT
cycles, a falsifiability beat the framework PREDICTS, SUMMARY, NEXT STEPS,
OUTRO. Re-derive every number from the repo, never from the commit message.
Show real source in the CODE beats."

claude "what does this work NOT establish? Find the limitation the repo already
records, and quote it rather than inventing a caveat."
```

**What produced the best beat this week:** asking what the code *refuses* to do.
The ingest script's `TRANSPORT, DO NOT REPAIR` docstring gave the episode its
title, its thesis, and its framework axis 2 — and none of that was in the
commit message's summary of what changed.
