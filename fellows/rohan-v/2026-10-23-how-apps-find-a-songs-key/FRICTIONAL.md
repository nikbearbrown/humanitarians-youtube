# FRICTIONAL — How Apps Find a Song's Key

The frictional log for this piece of work: short, dated, honest entries about what was tried, where it
resisted, what was done about it and what was learned, appended as the work goes and never rewritten. What an
entry contains, and why: <https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-10-23 — A key detector, and the STEM video about it

> Written during the build (Friday 23 Oct, for the week of 19–23 Oct).

**Working on.** One of this week's two STEM explainers. I picked key detection from four suggestions; it
follows last week's tempo video.

**Tried, and expected.**
- No expected result was stated up front. The build's working assumption (Claude's) was that the classic
  method would get clean synthetic songs right and miss onto related keys.
- Western test material, as for the tempo video.

**Where it resisted, and what I did next.**
- The first detector was badly wrong (27 of 60), because its chroma was flat; fixed before anything was
  scripted (BUILD-LOG §2). After: 50 of 60.
- The misses all fell in one place, natural-minor ballads read as their relative major, so the video is built
  around that: B01 plants "same notes, different home" before the mechanism.
- A wrong runner-up (A minor instead of G major) was caught in the script before render and re-voiced.

**What Claude contributed, and what I accepted, changed or rejected.**
- Claude researched the method and scoring, wrote the detector, the songs, the scenes and the docs. I chose the
  topic and set the hours.

**What I understand now, and what I still don't.**
- Now: a key detector hears the notes well; telling a minor key from its relative major is the hard part,
  because they use the same notes.
- Still don't: how DJ apps decide; none document it, so the video doesn't say.

Evidence: [`evidence/run.log`](./evidence/run.log), [BUILD-LOG](./BUILD-LOG.md), the QC sheets.
