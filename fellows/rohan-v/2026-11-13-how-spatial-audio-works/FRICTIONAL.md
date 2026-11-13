# FRICTIONAL — How Spatial Audio Works

The frictional log for this piece of work: short, dated, honest entries about what was tried, where it
resisted, what was done about it and what was learned, appended as the work goes and never rewritten. What an
entry contains, and why: <https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-11-10 — Building a head that hears, and a three.js stage for it

> Written during the build (9–10 Nov, for the week of 9–13 Nov).

**Working on.** One of this week's two STEM explainers: how spatial audio works, the AirPods kind. I asked for an
audio-related topic and chose this one. The evidence is a textbook spherical head that renders sound and measures
the cues, and B04 plays its output so viewers can hear it. I chose HyperFrames for both of this week's videos,
then asked for three.js and "beautiful motion designs".

**Tried, and expected.**
- No prediction was written down before the run. The working assumption (Claude's, from the fact sheet) was that
  the sphere would give about two thirds of a millisecond at the side, much more shadow for high sounds than low,
  and no way to tell front from back without an outer-ear cue. All three held: 0.661 ms; 14.0 dB against 2.3 dB;
  0.00 dB between front and back.
- Expected: that eight seconds of the sphere's own render, played in B04, would be heard as one turn around the
  head on headphones.

**Where it resisted, and what I did next.**
- The front/back result is true by construction of a symmetric sphere, so it confirms the code rather than
  discovering anything. The narration says "in my model", and the docs say so (BUILD-LOG §1).
- The circling clip was first rendered without the outer-ear filter, so its back half gave the ears the same cues
  as its front half, the very ambiguity B03 teaches. It now has the filter on for the half behind the ears, and
  every measured number stayed the same. Whether it reads as a turn on ordinary earbuds is still open; it's the
  first question in FEEDBACK.
- The fact check flagged three things on screen: a "3200 POINTS" counter on the ear scan that no source supports
  (removed), a spark line that came close to saying Apple measures your HRTF (reworded), and a filter chart that
  didn't say it was my model's (relabelled) (BUILD-LOG §6).
- The binaural cue lives in the left/right difference, so B04's audio had to be mixed in stereo at 48 kHz and the
  compile had to stay stereo (BUILD-LOG §3).
- A word-clock cue failed: the anchor "dummy head" didn't match "dummy head's" because of the apostrophe. The
  anchor is now "inside a dummy" (BUILD-LOG §3).
- Snapshot review found overlapping HUD panels, phone titles wrapping into the 3D stage, text past the right edge,
  a camera in B03 that hid the behind source, and a phone in B06 invisible against the dark ground. The gate
  pre-check found the background gradient counted as ink past the safe edge, labels under the 4K size floor, and
  one phone panel past the bottom inset. Each was fixed before the finals (BUILD-LOG §5).

**What Claude contributed, and what I accepted, changed or rejected.**
- Claude suggested topics, researched what Apple, Dolby and the hearing research say (the graded fact sheet),
  wrote the head model, the stereo mix, the three.js scenes and the docs, and recommended three.js for the 3D stage
  with the HUD kept in HTML. I chose the topic, chose HyperFrames for both videos, asked for three.js and
  beautiful motion, approved downloading three.js 0.187.0, and carried over my week-11 rule for the phone: no
  overlapping panels or text; if it doesn't fit, remove text from the bottom and use the room to space the panels.
  Review of the 4K finals was pending at the time of writing.

**What I understand now, and what I still don't.**
- Now: the gap between the ears is under a millisecond and still enough to tell left from right; the head's
  shadow matters for high sounds, not low ones; timing and loudness can't separate a sound from its mirror behind
  you, which is the outer ear's job; and head tracking works by turning the sound the opposite way to your head.
- Still don't: how Apple turns the camera scan into a profile, which it hasn't published; how much a personal
  profile actually helps, for which the research found no published independent measurement; and whether my clip circles for someone on
  ordinary earbuds.

Evidence: [`evidence/run.log`](./evidence/run.log), [BUILD-LOG](./BUILD-LOG.md).

**Added after the 4K finals (same night, 2026-11-10).** Looking at the phone QC sheet, B05 and B06 still had
panels touching: the phone type is large, and the column was full (18 px gaps; B03 and B05 ran past the safe
bottom). Following my phone rule, the 3D stage was made a little shorter, B03's head-only chart and B06's
FRONT ⇄ BEHIND row were dropped on the phone (the cards above already say it), and two lines were set smaller.
Measured again in a browser, every phone column now has 37–146 px between panels; all six phone clips were
re-rendered and the vertical final rebuilt. The landscape cut was unchanged. QC sheet:
[`qc-sheet-9x16.png`](./qc-sheet-9x16.png).
