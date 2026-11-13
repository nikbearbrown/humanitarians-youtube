# FRICTIONAL — How Noise-Cancelling Headphones Work

The frictional log for this piece of work: short, dated, honest entries about what was tried, where it
resisted, what was done about it and what was learned, appended as the work goes and never rewritten. What an
entry contains, and why: <https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-10-23 — A simulated headphone, and the STEM video about it

> Written during the build (Friday 23 Oct, for the week of 19–23 Oct).

**Working on.** The second of this week's two STEM explainers. I picked noise-cancelling headphones from four
suggestions.

**Tried, and expected.**
- No expected result was stated up front. The build's working assumption (Claude's) was that a simulated
  headphone would cancel steady low noise and miss high or sudden sounds.

**Where it resisted, and what I did next.**
- There's no real headphone to measure, so the evidence is a simulation, and the video says so every time it
  gives a number.
- The fact-check showed many real headphones don't adapt their filter at all; the narration was rewritten so it
  only claims that for the simulated one (BUILD-LOG §1).
- The off/on listening clip would have been levelled to equal loudness, hiding the result; it is one clip now.

**What Claude contributed, and what I accepted, changed or rejected.**
- Claude researched the physics and the product documentation, wrote the simulation, the scenes and the docs.
  I chose the topic and set the hours.

**What I understand now, and what I still don't.**
- Now: the same tiny delay is a much bigger mistake at high pitch, which is why the hum goes and voices don't.
- Still don't: how much the ear cups add on a real headphone; the simulation has no passive model yet.

Evidence: [`evidence/run.log`](./evidence/run.log), [BUILD-LOG](./BUILD-LOG.md), the QC sheets.
