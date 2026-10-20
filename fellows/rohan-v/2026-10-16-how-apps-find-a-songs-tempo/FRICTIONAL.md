# FRICTIONAL — How Apps Find a Song's Tempo

The frictional log for this piece of work: short, dated, honest entries about what was tried,
where it resisted, what was done about it and what was learned, appended as the work goes and
never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-10-17 — A tempo detector, and the STEM video about it

> Written during the build (Saturday 17 Oct, for the week of 12–16 Oct).

**Working on.** This week's STEM explainer. I picked tempo detection from four suggestions, because
BPM is a number every Lyrical Literacy song carries in its style prompt.

**Tried, and expected.**
- Asked for the topic to be tested on Western grooves only ("no Indian stuff"), so the test set is
  rock, funk, house, hip hop, slow ballads, drum and bass, waltz and jazz swing.
- No expected result was stated up front. The build's working assumption (Claude's) was that a
  classic detector would get most of forty clean drum-machine grooves right.

**Where it resisted, and what I did next.**
- It didn't: 17 of 40 exactly right. Before believing that, the run was checked three times (band
  spacing, frame timing, the autocorrelation window; BUILD-LOG §2) and then against librosa, which
  agreed on 34 of 40. The low score is real, and it became the point of the video: the method finds
  real repeats, and choosing the beat among them is the hard part.
- A new toolkit rule says any tool named on screen must show its logo. librosa had none in the
  toolkit; I approved downloading its own logo from its repository.

**What Claude contributed, and what I accepted, changed or rejected.**
- Claude researched the method and scoring (facts sheet), wrote the detector, the synthetic grooves,
  the scenes and the docs. I chose the topic and the Western-only test set, and set the hours.
- Accepted: reporting the failures as the result rather than tuning the grooves until it passed.

**What I understand now, and what I still don't.**
- Now: a tempo detector doesn't fail by hearing nothing. It hears two or three real repeats, and its
  preference near 120 BPM decides, which is exactly why slow ballads come out double.
- Still don't: how commercial apps choose. None of them document it, so the video doesn't say.

Evidence: [`evidence/run.log`](./evidence/run.log), [BUILD-LOG](./BUILD-LOG.md), the QC sheets.
