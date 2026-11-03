# Frictional Log — Comparing AI Voice and Audio Tools — What Each Is Actually Good At

**Entry date:** 2026-09-24

**What I was working on:** Produced as part of the ten-topic automated batch — the final topic in the batch run, and the last video completed before this reorganization pass.

**What I tried, and what I expected:** Standard pipeline run; expected a clean pass, same as the ten topics before it.

**Where it resisted, and what I did next:** No defect surfaced; passed cleanly on the first attempt per the batch log. As a final spot-check across the whole batch, one frame in this video's vertical cut appeared blank on a manual timestamp check — investigated by mapping the timestamp against the beat sheet's per-beat durations, and confirmed it was 0.2 seconds into a 2.7-second beat, before that beat's animation had started (not a defect). Re-sampled 1.7 seconds into the same beat and confirmed it rendered correctly.

**What Claude contributed, what I accepted/changed/rejected:** Claude ran the false-alarm investigation using the beat sheet's timing data rather than assuming a bug from a single bad-looking frame.

**What I understand now, and what I still don't:** A single sampled frame near a beat boundary is not reliable evidence of a defect on its own — worth checking a frame mid-beat, not just at a round-number timestamp, before concluding something is broken.
