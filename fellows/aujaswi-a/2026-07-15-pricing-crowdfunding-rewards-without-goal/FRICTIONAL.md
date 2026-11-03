# Frictional Log — How to Price Crowdfunding Rewards Without a Confirmed Funding Goal

**Entry date:** 2026-09-24

**What I was working on:** Producing this video as part of the automated batch run covering the remaining topics, using the composer + visual-engagement-beat pipeline already fixed on the first video.

**What I tried, and what I expected:** Ran the same pipeline that had already passed cleanly on several prior topics in the batch, using a `TopicChipGrid` visual beat to list the reward-tier considerations. Expected the same clean GATE V pass.

**Where it resisted, and what I did next:** GATE V rejected the vertical cut. Root cause: `TopicChipGrid`'s chip-landing animation was scheduled as a fraction of the beat's total duration (`frame / (fps * 3)`), and this specific beat's narration audio ran only 1.64 seconds — short enough that GATE V's frame sample landed mid-fade, before the chips had finished animating in. Rewrote the animation schedule to a fixed per-chip frame offset, independent of the beat's total duration, re-rendered only the affected beat (not the whole video), recompiled, and it passed clean on the second attempt.

**What Claude contributed, what I accepted/changed/rejected:** Claude traced the GATE V failure to the exact line of animation-timing code causing it and rewrote the component logic properly, rather than reaching for the `--lenient` QC flag to bypass the failure. I accepted the real fix; did not take the shortcut.

**What I understand now, and what I still don't:** Duration-relative animation timing is unsafe for any component reused across beats of very different lengths — a fixed frame schedule is the safer default. Still open: no explicit test was run against a beat much longer than typical to confirm the fixed schedule doesn't leave dead air after the chips land early.
