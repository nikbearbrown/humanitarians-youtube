# Frictional Log — Mycroft: Evidence Freshness

**Week of 2026-09-25** · Adwait Changan · Mycroft track
Topic: a financial report carries two hidden ages that never show up in any figure.

**What I built this week**
- Measured two gaps separately: *arrival lag* (period close → data produced) and *shelf age* (produced → used).
- Pointed it at the project's own shipped pack and left the unflattering answer as it was, rather than regenerating it to look better.
- Refused two cases outright: a pack with no provenance, and a pack created before its own period had ended.

**The one idea it teaches**
- Freshness is two different problems, and a single "is it fresh?" number hides both.

**Where it pushed back (and what I did)**
- QC: the verdict wasn't reproducible from what was on screen (it showed STALE with no limits; at the obvious limits it's actually EXPIRED). Fixed by printing the supplied limits on the artifact — the numbers were already right.

**What I learned**
- A verdict you can't reproduce from the screen isn't evidence yet. Show the limits.

_Hours this week: ~20 (across the two videos built this week)._
