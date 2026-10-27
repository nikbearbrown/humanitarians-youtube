# Frictional Log — Mycroft: Evidence Coverage

**Week of 2026-10-09** · Adwait Changan · Mycroft track
Topic: findings had carried evidence references for weeks — but nothing had ever opened the files to check.

**What I built this week**
- Split the word "unsourced" into three different failures: no citation at all, a citation to a file not in the pack, and a citation to a row that isn't there.
- Made an unparseable reference *raise* rather than get skipped quietly.
- Ran it against the real February investigation: all 21 references across 4 findings resolve.

**The one idea it teaches**
- A reference that looks like proof isn't proof until something opens the file.

**Where it pushed back (and what I did)**
- QC: the per-claim split shown on screen was fabricated — the breakdown was wrong even though it summed to the right total (21), which is exactly why it survived the first pass. Caught it by re-running `cli coverage` and reading `per_claim` instead of trusting the beat sheet; re-rendered both beats.

**What I learned**
- Resolving a reference proves the row exists — it proves nothing about whether it supports the claim. And a correct total can hide a wrong breakdown.

_Hours this week: ~20 (across the two videos built this week)._
