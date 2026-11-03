# FEEDBACK — "16-bit or 24-bit: What Bit Depth Does"

Reviewer notes. Empty until someone reviews it.

## How to leave feedback

Point at a beat by its ID. Narration durations are the master clock, so a note
that changes narration forces regenerating that beat's audio, re-running
`align.py` and `sync_cues.py` (the word clock moves with the words),
re-rendering the scene to its new duration, and recompiling both cuts.

| Beat | Act | What it does |
|---|---|---|
| B00 | ASK | The export box asks 16 or 24 |
| B01 | BACKGROUND | Sound is movement; a file is numbers; two questions |
| B02 | ANALOGY → IDEA | A ruler, then that ruler on a wave |
| B03 | MECHANISM | The leftover gap is a hiss; coarser ruler, louder hiss |
| B04 | THE NUMBERS | -53 vs -101 dB, and what 100 dB means in a room |
| B05 | WHAT TO DO | 24 to work in, 16 to ship, never step down then up |
| B06 | OUTRO | Sign-off |

If a **number** is disputed, check [MEASUREMENTS.txt](./MEASUREMENTS.txt) — every
figure on screen has a line in it, and re-running the experiment is one command:
`python3 measure_bitdepth.py`.

## Before re-raising these, read the note

Three things were already argued through during the build and are recorded:

1. **"The video takes too long to get to the point."** It is deliberate. The
   subject arrives at 1:01 of 2:07 because of an explicit instruction to assume
   no audio background. See [PEDAGOGY.md](./PEDAGOGY.md) and the first quote in
   [SOURCE-brief.md](./SOURCE-brief.md).
2. **"Where is 24-bit in the comparison?"** Measured (-149.56 dBFS), logged, and
   cut on purpose — three columns is a table, two is a decision. See
   [FACTCHECK.md](./FACTCHECK.md), *honesty notes*.
3. **"A hundred decibels isn't whisper-to-concert."** Correct that published
   tables put it at 70-100 dB. That is why the narration says *roughly*, the
   label says *approximately*, and the on-screen ladder is relative to full
   volume rather than absolute SPL. Recorded as a hedged pass, not a clean one,
   in [FACTCHECK.md](./FACTCHECK.md) claim 12.

## What a reviewer should check first

- **B04's room line.** It is the beat's payload and the one thing a viewer can
  act on. If it does not read instantly, that is the note worth making.
- **B02's ruler-to-wave transition.** The whole reel hinges on the analogy
  becoming the mechanism in one frame.
- **The portrait cut on an actual phone.** It is a native re-render, not a
  scaled-down landscape, and portrait layout decisions are listed in
  [SHOTLIST.md](./SHOTLIST.md#916) — but a phone is the only real test.

## Notes

_(none yet)_

## Resolved

_(none yet)_
