# FRICTIONAL — Every Group Went The Other Way

A dated record of the process behind this piece of work, kept beside the
evidence it describes. Append; never rewrite an earlier entry.

---

## 2026-11-13 — four failures, and only one of them tripped a gate

**What I tried and expected.** The topic came off the registry's open list.
Simpson's paradox is famous, which was the main argument against it — the risk
was a re-teach of something the audience has already seen. Two things made it
worth doing: the evidence could be **real published data** rather than another
simulation written for the episode, and the honest landing is not the one most
explainers reach for.

**Where it resisted.**

**1. GATE F refused the compile, and it was right.** I had written the weekly
report's paperwork and gone straight from the beat sheet to rendering this
reel, with no FACTCHECK.md. The gate blocked the final cut. All nine master
beats had already rendered, so nothing was lost but a compile — but the gate
exists precisely because the paperwork is an *input* to the build, not a
write-up of it. Writing the factcheck is where the next failure got caught,
which is the whole argument for the ordering.

**2. The reel had two different "overall" numbers in it.** B00 opened on the
famous headline figures — about 44% of men and 35% of women admitted in 1973 —
while every other beat analyses the six largest departments, where the figures
are 44.5% and 30.4%. Both are correct. They describe **different
populations**. I only noticed while writing the factcheck row for B00 and
having to say which population it referred to.

A reel whose entire thesis is *people misread aggregates* cannot itself put
two different aggregates in front of a viewer and hope nobody checks. I
rescoped B00 to the six departments so the whole thing speaks about one
population, and labelled B02's total row "All six" rather than "overall". The
famous numbers now appear nowhere.

**3. An invented percentage, sitting where the automated check cannot look.**
B04's card read "74% applied to C, E or F". The data says 72.3%. I typed it
from memory; nothing produced it.

The reconciliation pass that rewrites every numeric prop from the generated
JSON ran clean — and it was *correct* to. That figure lived inside a card
line, which is prose. The pass sees `{"value": 72.3}`; it cannot see
`"74% applied to C, E or F."` This is a real limit of a check I had come to
trust, and the fix is procedural: **any sentence containing a number is
unverified until someone reads it against the source.** Written into
`PROMPTS.md` so the next reel treats it as its own pass.

**4. The new component coloured by who won instead of by which series.**
`PairedBars` printed a legend saying *men = ink, women = terracotta*, then
accented the women's bar **only on rows where women led**. On Dept C, Dept E
and the total row — the three rows the argument turns on — the women's bar
rendered in the men's colour. Two grey bars, distinguishable only by row order.

I had keyed the accent to the comparison result, so hue encoded *who is ahead*
while the legend promised it encoded *which series*. Caught by reading the
first rendered frame. Fixed so the B series always wears its colour and the
lead is carried by a text marker. Logged as A24, with the rule: a colour may
encode a category or a result, never both.

**What Claude contributed and what I accepted.** Claude proposed four topics
with the trade-offs; I picked this one and gave no further direction. The
Berkeley framing, the standardisation, the component, the landing beat and all
four corrections above are Claude's, found mid-build.

**What is now understood.** This build sharpened the pattern the last two
recorded. Of four defects, exactly one — the missing factcheck — failed a
command. The other three were a correct-looking reel with two incompatible
populations in it, a fabricated number in a position the automated check is
structurally blind to, and a chart contradicting its own legend. None would
ever throw.

The useful generalisation is about **where checks do not reach**. GATE V reads
geometry, not meaning. GATE T reads type, not sense. The reconciliation pass
reads props, not prose. Every one of them is good at its job and silent about
everything else, and the gap between "passed every gate" and "is correct" is
exactly where this week's work lived.

**What is still open.** The simulation establishing that a reversal needs a
confounder is shipped but not shown — there was no room, and a synthetic
figure beside real data is a misreading waiting to happen. A future reel could
earn it properly.

---

## 2026-11-13 — a punt that paid for itself in three days

GATE L found nothing for "two series across categories with a contradicting
total". The near hits were the usual shape: `ClaudeBarChart` does one series,
and the library's only real grouped chart is welded to another reel with a
`sparkLine` prop and nothing else.

So `PairedBars` was built generic — rows, an optional total, a lead marker per
row — and the separation was made the point: the aggregate sits *outside* the
block of rows, behind a rule, because drawing it as another row would assert
it is one of them.

The weekly report for the same week reuses it unchanged for its video beat.
That is the second week running that a punt from the educational reel paid for
itself immediately in the report, and the third component in the shared
library (`StageRail`, `ThresholdWalk`, now `PairedBars`) to be reused by an
argument it was not built for.
