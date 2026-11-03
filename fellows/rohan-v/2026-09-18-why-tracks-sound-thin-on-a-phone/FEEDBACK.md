# FEEDBACK — "Why Your Track Sounds Thin On A Phone"

Reviewer notes. Empty until someone reviews it.

## How to leave feedback

Point at a beat by its ID. Narration durations are the master clock, so a note
that changes narration forces regenerating that beat's audio, re-running
`align.py` and `sync_cues.py` (the word clock moves with the words),
re-rendering the scene to its new duration, and recompiling both cuts.

| Beat | Act | What it does |
|---|---|---|
| B00 | ASK | Full in headphones, thin on a phone |
| B01 | BACKGROUND | Two sides; headphones keep them apart; one speaker adds |
| B02 | ANALOGY -> IDEA | Two people, one door; then the same as waves |
| B03 | MECHANISM | Measured: the centre survives, the wide layer does not |
| B04 | SUBTLER CASE | Holes, not silence |
| B05 | WHAT TO DO | The ten-second mono check, and the usual culprits |
| B06 | OUTRO | Sign-off |

If a **number** is disputed, check [MEASUREMENTS.txt](./MEASUREMENTS.txt) — every
figure on screen has a line in it, and re-running both experiments is one command
plus a shell function that is printed in the log.

## Before re-raising these, read the note

Four things were already argued through during the build and are recorded:

1. **"Where are the null frequencies?"** Measured, predicted first, and cut on
   purpose. B04's axis is labelled only LOW NOTES to HIGH NOTES because a viewer
   meeting stereo for the first time cannot use a comb-filter chart. Numbers are
   in MEASUREMENTS.txt; reasoning in [PEDAGOGY.md](./PEDAGOGY.md).
2. **"The nulls should be minus infinity."** They are about -10 dB for two stated
   reasons — a 120 Hz-wide analysis filter, and a broadband rather than tonal
   source. That result is *why* the reel says holes rather than silence. See
   [FACTCHECK.md](./FACTCHECK.md), "Why the nulls measured ~-10 dB".
3. **"This isn't a real mix."** Correct, and said on screen: B03's footnote reads
   "measured on a track built for this". A constructed signal is the only way to
   know the placement exactly rather than guess it.
4. **"Some phones have two speakers."** True, and it does not change the beat:
   B01 names "a phone, a laptop, a smart speaker" as the single-driver case, and
   a stereo phone held in landscape at arm's length still sums acoustically well
   before it reaches one ear.

## What a reviewer should check first

- **Does the door read?** The whole reel hinges on B02. If the swinging-then-
  locking sequence does not land, that is the note worth making.
- **B03's position strips.** They exist so the result reads as predictable rather
  than reported. If a viewer cannot tell "centre" from "both sides" at a glance,
  the design has failed.
- **The portrait cut on an actual phone.** It is a native re-render, not a
  scaled-down landscape, and portrait layout decisions are listed in
  [SHOTLIST.md](./SHOTLIST.md#916) — but a phone is the only real test. B01 keeps
  its two cards side by side in portrait on purpose; that is the decision most
  worth a second opinion.

## Notes

_(none yet)_

## Resolved

_(none yet)_
