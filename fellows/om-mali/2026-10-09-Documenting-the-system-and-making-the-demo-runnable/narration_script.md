# Documenting the system and making the demo re-runnable

**Runtime target:** 3:00 · **Spoken words:** ~450 · **Figures:** 4

Every number spoken below is read from `figdata.json`, which is generated at build time by
querying the live database, reading the generated findings file, and running `git show HEAD`
against the working tree. No figure carries a hand-typed value, and no "before" count comes
from memory.

---

## [0:00] Opening — camera

Hi I'm Om Mali. This video is about the last week of the build: writing the documents that
explain the system, discovering a stated requirement I had met zero times, and turning the demo
into something that re-runs instead of something that was true once.

The code was finished. What was missing was the part that lets someone else understand it
without me sitting next to them.

## [0:28] I audited the docs instead of trusting them — `w12-docs.png`

The plan names six documents. Rather than assume, I checked each one against the last commit.

Three of them did not exist at all. Not thin, not stale — absent. The proposal, the system
architecture and the data architecture. The audit found them; the plan hadn't predicted them.

So I wrote all three, from the project's own measured figures rather than from the plan's
prose. The architecture document is the one I'd keep: it says where the graph framework earns
its place and where it's ceremony, and it names the exactly two places a language model sits —
neither of which touches a number.

## [1:05] A requirement sitting at zero — `w12-priorart.png`

Then the one that stung. The plan says the published documents must cite the prior-art
literature honestly. This data source isn't new — it's commercially exploited and academically
mature, and my own plan says claiming novelty wouldn't survive a literature review.

I grepped for every name. Zero. Not thin coverage — zero mentions, in either published
document.

It's in three places now, and in one of them it's load-bearing rather than decorative. Gornall
and Strebulaev established that funds write up every share class to the latest round price. I
reproduced that on this cohort, and it's the reason dispersion is measured per company with the
class recorded — overturning an earlier draft's rule.

## [1:50] What a published number has to survive — `w12-provenance.png`

The data architecture document ends with a trace. One headline — twenty-five percent of
consecutive observations unchanged — followed down eight links: the published sentence, the
generated figure, the function with its guards, the panel, the match decision, the named human
behind it, the filed position, and the archive file the SEC published.

Break any link and you have an output, not evidence. The run log says which run produced each
artifact, so the chain is datable as well as traceable.

## [2:30] A demo that re-runs — `w12-demo.png`

The plan said record a demo. I wrote a script instead. Five acts, every figure queried live, so
a transcript that disagrees with the database is a bug rather than an old file.

It writes nothing — zero write statements across the demo and the server it calls. Act two
shows a decision a named human already made and deliberately doesn't make a new one. A demo
that recorded a judgment would be a demo clearing a gate for a screenshot.

## [2:52] Close — camera

Eleven weeks, and the last one was mostly finding out what I'd assumed. Thanks for watching.
