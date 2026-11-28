# FRICTIONAL — Confidently Out Of Date

A dated record of the process behind this piece of work, kept beside the
evidence it describes. Append; never rewrite an earlier entry.

---

## 2026-11-27 — the experiment said "no effect", and that was the useful part

**What I tried and expected.** Embedding staleness came off the registry's
open list, chosen partly for variety: the previous four reels had all been
measurement or pipeline failures, and this one is about retrieval and language
drift. I expected a straightforward build — index a corpus, let the language
move, watch recall fall.

**Where it resisted.**

**1. The first experiment produced a null.** Stale recall came back at 98.5%
against 100% for a freshly rebuilt index. A 1.5-point difference. No video.

The temptation at that point is obvious and I want it written down: I had the
beats sketched, I had a title, and the quickest route to the reel I had
already imagined was to make the queries more hostile — draw more heavily from
new vocabulary until the collapse appeared, then report the collapse. That
would have been a rigged query distribution reported as a finding, and it is
the same failure as the peeking reel's fixed-horizon comparison two months
ago: an experiment arranged to produce the conclusion that was already
written.

What the null actually said was worth more than the reel I had planned. The
stale index did fine **because most queries still contained old vocabulary it
knew perfectly well**, and those surviving terms carried the query on their
own. That is not a defect in the experiment. That is the reason this failure
survives in production for months without anyone noticing.

So the question changed from *does staleness hurt?* to **how much of a query
has to be new language before staleness hurts?** That has an answer, it is a
sweep rather than a single number, and the answer turned out to be a step
function: harmless at 0%, harmless at 50%, total collapse at 100%.

**2. The sweep's collapse is the boring failure.** At all-new vocabulary the
index cannot form a query vector at all — 100% of those queries return
nothing. That is loud. Somebody sees an empty page and files a bug.

The interesting case had to be added deliberately: a word that **moved**
rather than a word that is **missing**. The stale index has a confident vector
for it, pointing at the topic it used to belong to. Recall zero, similarity
0.892, every result from the wrong place. That is the title, and it did not
come out of the original design — it came out of asking what the sweep was
*not* testing.

**3. I overclaimed in my own narration and caught it in my own factcheck.**
B05 said the similarity score "never dropped at all". It drops from 0.961 to
0.892 — a move of 0.069. Small, but not nothing, and "never" is a measurable
word.

I caught it while writing the FACTCHECK row whose entire job is to hold that
sentence to account — and then, in the same row, described the move as "seven
thousandths of a point" when it is sixty-nine thousandths. An arithmetic slip
inside the correction itself. Both are now fixed, both are recorded rather
than silently repaired, and the narration states the figure instead of
reaching for an absolute.

The lesson is not "check your numbers". It is that **a sentence written to
land well resists being checked**, and the check has to be a separate pass
with a different intent, not a re-read of the thing you just wrote.

**What Claude contributed and what I accepted.** Claude chose the topic from
the open list, designed and redesigned the experiment, found the null, found
the migrated-word case, and caught both of its own overclaims. I supplied the
brief.

**What is now understood.** Three reels in a row have had the same shape: the
first version of the experiment agreed with the beat I had already written,
and the honest version disagreed with it. Peeking (rigged horizon),
training-serving skew (planned angle false), and now this (null result).

In every case the better reel was on the other side of accepting that the
first result was wrong. The practical habit that keeps paying: **when a
measurement agrees with the script you have already drafted, treat that as a
reason to re-examine the measurement, not as permission to render.**

**What is still open.** Subword tokenisation would soften the
out-of-vocabulary half of this and do nothing for the migrated-word half.
That asymmetry deserves a beat and there was no room. A future reel could take
it properly.

---

## 2026-11-27 — GATE F, again, and it was right again

The compile refused: `missing or empty SHOTLIST.md`. I had written FACTCHECK,
SOURCES and PROMPTS and gone straight to the build.

This is the **second time in three weeks** the same gate has caught the same
omission, which makes it a process defect rather than an accident. The
paperwork is an input to the build, not a write-up of it, and I keep treating
the ones the gate names as mandatory and the others as optional.

They are not optional: `./art run` checks FACTCHECK **and** SHOTLIST **and**
PROMPTS. The fix is to write all four documents before the first compile, not
to remember which one blocks.

Nothing was lost but a compile — the beats were already rendered — but it cost
a round trip for a reason that was entirely within my control, twice.
