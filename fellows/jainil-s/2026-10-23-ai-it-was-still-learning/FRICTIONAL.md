# FRICTIONAL — It Was Still Learning

*Draft written from the build session. Edit into your own voice before relying
on it; the facts are accurate, the framing is a starting point.*

---

## 2026-10-23 — three experiments that looked like the result

**What I tried and expected.** Grokking is a well-known result with a clean
story, so I expected the experiment to be routine: train a small network on
modular addition, watch training accuracy saturate, wait for held-out accuracy
to jump. Build the curve, write the words.

**Where it resisted.** It did not grok. Not once, in three configurations.
ReLU at P=31 over 12,000 steps: training hit 99% at step 500 exactly as
advertised, and held-out accuracy crawled up to about 53% and stopped. ReLU at
P=23: the same shape, plateauing near 60%. That is *delayed partial
generalisation*, which is a real thing and a different thing, and a plateau at
60% is not the result I had written a title about.

This is the moment where the temptation is specific and nameable: the curve
looks dramatic, the narration about "it was still learning" is already true in
a loose sense, and nobody watching would check. Softening "generalises" into
"improves substantially" would have made all three runs usable.

**What actually fixed it.** Not patience — the activation. Modular addition
has Fourier structure, and a squared activation can represent that structure
directly where a ReLU has to approximate it. With `h = u²` the same network
groks in seconds: training saturates at step 500, held-out sits at 0.5% for
another 1,500 steps, then climbs past 95% at a median step 6,125. Eight seeds
out of eight. The claim did not move; the experiment got good enough to
support it.

Because the activation is load-bearing, it is stated on screen in B02 rather
than buried in the script. A viewer who tries this with a ReLU should not be
surprised.

**What the library gave back.** Zero new components. Every beat was filled by
something built for a different subject in a previous week —
`DoubleDescentCurve` from the 2026-10-09 reel, `CardSet` from 2026-10-16,
`FormACard` from further back. This is the first reel where GATE L returned a
usable hit on every single search. Six weeks of making components take their
content as data instead of hard-coding it is what made that possible.

**What I caught looking at frames.** B03 draws training accuracy as a dashed
line and sat a dashed 95% reference line directly across it — while the
narration says "the dashed line is training accuracy". Two dashed horizontals
near the top of the frame, one at 100% and one at 95%, and the viewer has no
way to tell which one the voice means. The reference line was removed. The
render exited 0 and the probe was clean; nothing but looking at the frame would
have found it.

Then the Short refused GATE V: B04 filled 38% of a 3840px-tall frame. The cause
was not this beat. `ClaudeBarChart916` used a *fixed* row height, so four bars
claimed a little over a third of the frame where seven bars had filled it fine
last week. The height now scales with the bar count. A per-beat fix would have
hidden a bug that every future three- or four-bar chart would have hit.

**What I got wrong in my own write-up.** The first draft of `README.md` said
the crossing step ranged 5,250–7,000 across seeds. I did not measure that. I
re-ran the script: it is 4,750–7,750. The number was invented to sound like a
range, in the supporting document for a video whose entire subject is trusting
a number you have not checked. It is now in `FACTCHECK.md` as row 16, including
what the draft said, because a corrected fabrication that leaves no trace is
just a quieter one.

**What is understood now.** Every real error this week was in something that
exited 0. Three non-grokking experiments, an ambiguous dashed line, an
underfilled portrait frame, an invented range in prose — none of them failed a
gate, and the gates are good ones. The things that catch this class of error
are running the experiment before writing the words, reading the frames, and
asking of your own sentences where each number came from.

**Still open.** The reel says weight decay is what moves the network off the
memorising solution, and shows the ablation. It does not show *what the
network learns instead*, which would need mechanistic analysis this build did
not do. That is deliberately cut in `FACTCHECK.md`, and it is the obvious
follow-up.
