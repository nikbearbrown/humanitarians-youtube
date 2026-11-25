# FRICTIONAL — How Auto-Captions Find Each Word

The frictional log for this piece of work: short, dated, honest entries about what was tried, where it
resisted, what was done about it and what was learned, appended as the work goes and never rewritten. What an
entry contains, and why: <https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-11-01 — Testing the recogniser our videos use, and the STEM video about it

> Written during the build (Sunday 1 Nov, for the week of 26–30 Oct).

**Working on.** The second of this week's two STEM explainers. I picked auto-captions from four suggestions; the
recogniser tested is the one that times every animation in our videos.

**Tried, and expected.**
- No expected result was stated up front. The build's working assumption (Claude's) was that Whisper would be
  near-perfect on clean speech and get worse in noise, as its paper reports.
- Western test material: 24 everyday English sentences, built from our narrator's voice.

**Where it resisted, and what I did next.**
- The first timing result was wrong (+848 ms), because the audio was read at the wrong sample rate; and the error
  rate was inflated by "9" against "nine". Both were fixed before anything was scripted (BUILD-LOG §2, §3).
- A slicing bug in the misheard-sentence list was fixed (BUILD-LOG §4).
- A second run moved the two noisiest results. Instead of quoting either run exactly, the narration says "over
  seventy percent" and "over three hundred words", which holds for both (BUILD-LOG §5).

**What Claude contributed, and what I accepted, changed or rejected.**
- Claude researched the model and the timing method, wrote the test, the scenes and the docs. I chose the week
  and both topics and set the hours.

**What I understand now, and what I still don't.**
- Now: the recogniser times words from where it was looking, and in my test its starts were about a quarter of a
  second early; it holds up until the noise is within a few decibels of the speech, and then it writes things
  nobody said.
- Still don't: why the starts come out early, Whisper's timing or the way my test speech was built; and what
  YouTube's own captions use, which it doesn't say.

Evidence: [`evidence/run.log`](./evidence/run.log), [BUILD-LOG](./BUILD-LOG.md), the QC sheets.
