# FRICTIONAL — Significant On Tuesday

A dated record of the process behind this piece of work, kept beside the
evidence it describes. Append; never rewrite an earlier entry.

---

## 2026-11-07 — the comparison that was rigged in my own favour

**What I tried and expected.** The topic was chosen from the registry's open
options: repeated significance testing on an A/B test. I expected the shape of
the result in advance — peeking inflates the false-positive rate, a corrected
boundary fixes it — and I expected to spend most of the build on the visuals
rather than the evidence.

**Where it resisted.** Three times, and each one mattered.

**1. The fix looked like a pure penalty.** The first version of §7 compared a
group-sequential test to a fixed test *at the same horizon* and reported power
dropping from 52.9% to 37.5%. I nearly wrote that into the script as "the cost
of doing it properly." It is a rigged comparison: a stricter boundary at a
fixed horizon can only lose power, so the result was guaranteed before I ran
it. The honest question is what each design *spends at the same power*, which
needed a sweep rather than a single run. That sweep produced a better finding
than the one I was going to ship: sequential testing costs more visitors below
roughly 65% power and saves 19% at 80%. The crossover is the interesting part,
and I would have missed it by not questioning a number that flattered my
narrative in the direction of "the correct method is expensive".

**2. A sixth of the data was being thrown away silently.** The winner's-curse
density was binned over ±8 pp. `np.histogram` drops out-of-range values
without a warning, and 16.5% of the mass was beyond ±8 — so both lobes
rendered as if they ended exactly where the axis did. The plot looked *good*.
It was the thing I was most pleased with visually, which is presumably why I
nearly shipped it: nothing about a clean-looking chart suggests it is lying.
Caught by asking why the edge bins were suspiciously tall. Fixed by widening
to ±15 pp, clipping the residual 0.24% into the end bins rather than
discarding it, and adding `assert hist.sum() == len(signed)` so the script
fails rather than quietly misdraws if it happens again.

**3. A number drifted between my head and the beat sheet.** I hand-typed the
40-element density array into `beat_sheet.json`. Then I wrote a reconciliation
pass that rewrites every data prop from `beat_data.json` and prints whether
each one already matched. The bar values, boundary values and hero series all
matched. The density array did **not**. I have no idea which element I got
wrong and it does not matter — the point is that the only reason I know is
that I checked mechanically instead of by eye. That pass is now part of the
build and is documented in `PROMPTS.md`.

**What Claude contributed and what I accepted.** Claude proposed four topics
with the trade-offs of each; I picked this one and gave no further direction
until the cuts were delivered. Everything below the topic choice — the A/A
framing, the evidence scripts, the component, the beat sheet — is Claude's,
and all three problems above were found and fixed by Claude mid-build rather
than raised by me in review. That is worth recording accurately: this entry is
not a story about a human catching a model's errors. It is a record of a build
that checked its own numbers, and of the one check (the mechanical
reconciliation) that caught what reading could not.

**What is now understood.** The failure mode in this toolkit is consistent and
it showed up twice more today: **the dangerous errors are silent**. A rigged
comparison exits 0. A histogram that drops a sixth of its mass exits 0, probes
clean, and renders a handsome chart. A retyped array passes every gate. None
of GATE F, GATE V or GATE T would have caught any of the three. The only
things that caught them were asking where a number came from, and refusing to
trust a transcription I had made myself five minutes earlier.

**What is still open.** The crossover between 50% and 65% power was bracketed,
not resolved — two measured points, no bisection. The reel says "about 65%"
and `FACTCHECK.md` records it as a bracket. Resolving it properly would be
maybe twenty lines of simulation and would let a future reel state a number
instead of an approximation.

---

## 2026-11-07 — the chart was legible, and it said the opposite

Two more, both found by looking at frames rather than at logs.

**The band highlighted the wrong side of its own threshold.** `ThresholdWalk`
drew the decision band as a tinted rectangle *between* the two boundary lines.
Read the frame and the terracotta region says "this is the interesting zone" —
but between the lines is exactly the region that means nothing happened. The
chart was clean, well composed, passed GATE V and GATE T, and asserted the
opposite of the narration playing over it. It was worse on B06, the beat the
whole argument builds to, because the scale headroom (`×1.15`) squeezed the
outside-the-band region to a sliver precisely when the band was widest. Fixed
by tinting the two outer regions instead and raising the headroom to `×1.25`.
Logged as A19.

**I compiled a 720p file and called it a master.** `compile.py` defaults to
`--height 720`; the 4K master comes from `./art final`, which is the same
script with `--height 2160`. The compile reported success, the slot table said
9/9 filled, and the folder looked finished. Caught by reading the command's
own `--help` rather than trusting that "compile" means "compile the
deliverable". Logged as A20, along with the related trap that `drawtext: yes`
in the log does not mean labels were burned in — it only reports that ffmpeg
*has* the filter, and review labels are gated on `--review`.

**Then the portrait cut, which the gate blessed.** `ThresholdWalk916`'s first
version had the title sitting on `n = 100 per arm`, the `ship it?` callout
also on the title, and `nothing here` on the axis caption. GATE V reported
**18 frames, 0 BLOCKER, 0 MAJOR**. It is not a bug in the gate: it measures
the content bounding box, and two labels that overlap each other are both
still inside it and both still count toward fill. The cause was mine — I had
positioned those labels as absolutes precisely so they would not cost stack
height, which also meant the layout engine could not see them. They are real
rows now and the plot height came down to pay for it (A22).

One more pass on the same beat: with the *wide* calibrated band, the
right-hand boundary line runs directly under the word "significant" and the
dashes cross the glyphs. A page-colour knockout, the same trick the callouts
already used.

**The pattern held for every single defect in this build.** A comparison that
proved what it assumed. A histogram that discarded a sixth of its data. A
chart that inverted its own meaning. A master at a third of its resolution.
Three labels stacked on top of each other. Only one — the card overflow —
failed a command, and that was because it crossed the frame edge rather than
because anything understood what the frame said. The habit that caught the
rest is the same one each time: ask what the artifact actually *says*, not
whether the command exited 0.

The sharpest version of the lesson, worth carrying forward: **a clean GATE V
means the frame is correctly sized, not that it is readable.**

---

## 2026-11-07 — a punt that paid for itself before it shipped

GATE L found nothing for "a line wandering across a threshold over time". The
near hits were instructive about *why* a library this size still misses:
`PositionCurve` and `DoubleDescentCurve` are both line plots with reference
marks, and both are welded to the argument they were built for — one lights
the minimum, the other reads as log-log error against capacity. Everything
else was a single-reel figure exposing only a `sparkLine`.

So `ThresholdWalk` was built generic: a series, a symmetric band, callouts on
the first excursion and the last point. It carries any argument where a
measurement is watched rather than taken once.

It paid for itself inside the same reel. B06 replays B02's **identical twenty
numbers** against a wider band, and the run that looked like a winner never
reaches the line. That beat only works because the component takes the band as
a prop — a figure hardcoded to one threshold would have needed a second
component, or worse, a second dataset, which would have proved nothing.

I also wrote the ledger the skill assumes exists. `TEMPLATE-MISSES.md` is
referenced by both `CLAUDE.md` and the ai-explainer SKILL.md as the place
punts are recorded automatically — and it did not exist, because the automatic
logging only fires when `./art scenes` is called with `--reel`, which no build
had done. Created it, logged this miss, and backfilled the two earlier punts I
could document from their own reels (`SheetFill`, `StageRail`), marked as
recorded late.
