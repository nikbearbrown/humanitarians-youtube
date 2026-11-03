# PROMPTS — The Tails Go First

## On-screen prompts

**B00 — the ask.**

> If I keep training each model on the last model's output, what breaks first?

Output lines: `Not the average.` · `The rare cases.`

**B07 — the handoff.** Read aloud verbatim, then discussed.

> My training set includes model-generated examples. Help me work out which
> parts of my real distribution are underrepresented in it, and what I would
> have to keep sampling from the real world to avoid losing them.

Why this prompt: the reel's finding is only actionable if you know which parts
of your own distribution are thin, and the mitigation the paper points at is
keeping real data in the loop. The second clause is the one that does work;
the narration says so rather than leaving it to be noticed.

## Build prompt

**`DistributionShape` / `DistributionShape916`**

> A density silhouette taking its heights as data, with one region of the x axis
> fillable in terracotta and labelled, and — the part that matters — an optional
> `ghost` array drawn behind it as a dashed outline. The component has to be
> able to show a shape that has LOST something: draw it once with the region
> present, then again with the region gone and the original ghosted behind, so
> the absence is visible rather than asserted. A `stats` row underneath carries
> summary numbers, for the case where those numbers look fine while the shape
> does not. Portrait re-lays-out and never crops: the argument lives at the
> right-hand end of the axis.

## Evidence script

`collapse_evidence.py` was written and run **before** any narration existed, and
corrected twice when its output did not support the claim — once because the
model inflated variance instead of collapsing it, once because the metric let
bulk outliers masquerade as the rare subpopulation. See `FACTCHECK.md` →
"Changed during the build".
