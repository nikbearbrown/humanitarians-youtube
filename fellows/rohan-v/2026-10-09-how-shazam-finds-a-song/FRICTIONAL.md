# FRICTIONAL — How Shazam Finds a Song

The frictional log for this piece of work: short, dated, honest entries about what was tried,
where it resisted, what was done about it and what was learned, appended as the work goes and
never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-10-10 — Shazam explainer (week of 5–9 Oct, STEM)

> Written during the build, with Claude, from this session's record. The decisions are mine.

**Working on.** How a phone names a song from a few noisy seconds: for Lyrical Literacy fellows
who put music under their videos and don't know what the platforms can hear.

**Tried, and expected.**
- Asked for two STEM videos this week with everything documented. Chose Shazam (recommended)
  and AI music out of four topics.
- Expected a straightforward build: write the fingerprinter, measure it, show the numbers.

**Where it resisted, and what I did next.**
- The first noise test said a little noise was worse than a lot. Before using it, it was checked,
  and the "misses" were the right song at the wrong repeat: the test songs looped exactly. The songs
  were rebuilt with sections and human timing, and the test now scores what Shazam answers (the
  song), which gave a sensible curve and no wrong answers at all.
- The first "hum" matched, because it wasn't really a hum. It was rebuilt to wander like a person.
- One claim I'd have liked ("Shazam can't hear humming") couldn't be verified, so the video says
  what this kind of fingerprint does instead.
- The automatic checks caught small type, faint squares and labels off the edge on the phone cut
  before anything was rendered; all fixed (BUILD-LOG §6).

**What Claude contributed, and what I accepted, changed or rejected.**
- Claude proposed the topics, wrote the fingerprinter, the six scenes and the narration, checked the
  facts against the 2003 paper and YouTube's help pages, and caught both bad results above.
- I chose the topics, gave the week's hours (20) and asked for no late label.
- My review of the preview: pending at the time of this entry (appended below once done).

**What I understand now, and what I still don't.**
- A fingerprint is a recording's loudest points and their timing, so it survives noise but not a
  new key or tempo. That's also why "not matched" says nothing about permission.
- Still don't know how Shazam's production system tunes its thresholds, or how platforms handle
  covers (the paper's method doesn't).

Evidence: `fingerprint.py`, `synth.py`, `evidence/run.log`, `evidence/fingerprint.json`,
`beat_sheet.json`, `vertical/beat_sheet.json`, QC sheets.
