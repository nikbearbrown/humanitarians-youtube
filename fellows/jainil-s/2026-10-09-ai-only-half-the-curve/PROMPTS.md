# PROMPTS — You're Only Seeing Half the Curve

## On-screen prompts (the ASK→RESULT pairs)

**B00 — the ask.** Typed into the composer, answered by two output lines.

> I added parameters, my validation error went up, so I stopped there. Did I
> stop too early?

Output lines shown:
- `Depends where you stopped.`
- `There is a second descent past the peak.`

**B07 — the handoff.** Read aloud verbatim and discussed before the pause.

> I stopped scaling a model because validation error started rising. Help me
> work out whether I stopped before or after the interpolation threshold —
> parameters versus training examples — and design the cheapest experiment to
> check whether pushing well past it would do better.

Why this prompt and not "learn more about double descent": it makes the viewer
name a real model they abandoned and compute one ratio. The episode's claim is
only actionable if you know where on the curve you stopped, and almost nobody
has checked.

## Build prompts (how the new components were specified)

**`DoubleDescentCurve` / `DoubleDescentCurve916`**

> A test-error-against-model-size plot on log-log axes. It must support a
> staged reveal — a `stopAtX` prop that draws only the classical half — so one
> beat can state the textbook rule before another shows what it omits. Mark the
> interpolation threshold with a terracotta dashed vertical and a label. Support
> a dashed horizontal reference at the classical best so the second descent can
> be seen landing below it. Support an optional second series for training error,
> with values at or below a floor pinned to the axis rather than running off a
> log scale, so an error of 1e-27 draws truthfully as "flat on zero". Compute
> the domain from every point the component may draw, not just the revealed
> ones. Portrait re-lays out — it does not crop — and spends surplus height on
> the plot so the spike reads taller rather than narrower.

**`InterpolatorChoice` / `InterpolatorChoice916`**

> Two panels over identical data points. Left: exactly enough parameters, so
> exactly one curve exists and it swings wildly between the points. Right: far
> more than enough, so several faint candidates pass through the same points and
> one smooth terracotta curve is selected over them. Every candidate must pass
> *exactly* through every data point — construct them as a smooth base plus
> `A·sin(π(n−1)qt)`, which is identically zero at every data site for integer q,
> so adding wobble can never move a dot. Portrait stacks the panels; a centre
> crop would delete one panel and with it the entire argument.

## Evidence script

`double_descent_evidence.py` was written and run **before** any narration
existed, and rewritten twice when its output did not support the pitched claim.
See `FACTCHECK.md` → "Changed during the build".
