# PROMPTS — Both Sides Passed

## On-screen prompts

**B00 — the ask.**

> Both services validate their data and both pass. The output is still wrong.
> How?

Output lines: `Each side checks itself.` · `Nothing checks the join between them.`

**B06 — the handoff.** Read aloud verbatim, then discussed.

> Here are two services that exchange data. Help me write the contract between
> them as checks on a batch rather than on a row — ranges, allowed values, key
> uniqueness, and the shape of the distribution.

Why this prompt: "on a batch rather than on a row" is the actual move, and the
four named items are exactly the checks the experiment found necessary. The
narration points at the last one, because the shape profile is both the one
people omit and the only thing that caught the seventh defect.

## Build prompts

**None.** No component was built for this reel. `StageRail`, `ClaudeBarChart`
and `CardSet` carried the three body beats unmodified — see `SHOTLIST.md`.

## Evidence script

`boundary_evidence.py` was written and run before any narration existed. Its
first version scored 6/7 rather than 7/7 because the synthetic timestamps were
uniform across the day, which makes a timezone shift invisible to a
distribution check. The data generator was corrected — not the claim. See
`FACTCHECK.md` → "Changed during the build".
