# FRICTIONAL.md -- Week 11: How A/B Testing Can Lie to You

**Date:** 2026-10-12
*(Written retrospectively on 2026-10-19.)*

**What I worked on:** An explainer on how an A/B test can look
significant and still be wrong, using a real sample-ratio-mismatch case
from Microsoft (Fabijan et al. 2019) and a real peeking/early-stopping
study (Johari et al. 2015).

**What I tried, and what I expected:** Expected finding a real, verifiable
SRM case with public numbers would be the hard part, same as prior
videos.

**Where it resisted:** A planning-stage source figure (a 0.001 alert
threshold) couldn't be verified in the actual paper and was dropped
rather than guessed at. The source PDFs carried a no-redistribution
notice, which meant keeping them out of this public repo entirely and
replacing them with a citations-only README instead. Several layout bugs
surfaced only by looking at real 4K frames: a shared default leaking
"SQL" into portrait code cards that should have read "PYTHON," small
italic text losing its word spacing at 4K, and an outro that underfilled
at the same scale setting the previous reel used, requiring a
per-video adjustment instead of a fixed value.

**What Claude contributed:** Ran all three simulation scripts and the shared stats helper itself
and traced every on-screen number to either the simulation output or the
papers directly; caught the redistribution restriction on the source
PDFs before committing anything; caught the "SQL"-default leak and the
underfill before I had to.

**What I understand now, and what I still don't:** I understand now that
a visual setting that worked for one video's content (outro scale) isn't
guaranteed to work for the next one with a different title length -- it
needs checking per video, not assumed from precedent. I still don't fully
understand why the automated speech-to-text check for listening to the
narration keeps being unavailable.
