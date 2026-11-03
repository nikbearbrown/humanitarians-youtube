# FRICTIONAL — How AI Voices Read a Script

The frictional log for this piece of work: short, dated, honest entries about what was tried, where it
resisted, what was done about it and what was learned, appended as the work goes and never rewritten. What an
entry contains, and why: <https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-11-01 — Our narrator's pronunciation step, and the STEM video about it

> Written during the build (Sunday 1 Nov, for the week of 26–30 Oct).

**Working on.** One of this week's two STEM explainers. I picked AI voices from four suggestions; the evidence is
the voice that narrates all our videos.

**Tried, and expected.**
- No expected result was stated up front. The build's working assumption (Claude's) was that the pronunciation
  step would trip on words spelled the same but said two ways, and on names, as it had on mine.
- Western test material: everyday English sentences. The Indian instrument names appear only as real past
  mistakes from the week-08 video.

**Where it resisted, and what I did next.**
- The research first assumed the wrong pronunciation step (misaki); ours is espeak-ng inside kokoro-onnx. It was
  corrected before anything was measured (BUILD-LOG §2).
- Two narration lines would have shown the problem instead of explaining it: "read and read" sounded the same,
  and the B05 line would have misread dhol and sitar. Both were rewritten, the first re-voiced (BUILD-LOG §3, §4).
- The recogniser writes my name the same way for both readings, so it can't confirm the respelling; the video
  relies on the phonemes and the two clips instead.

**What Claude contributed, and what I accepted, changed or rejected.**
- Claude researched the pipeline, wrote the test, the scenes and the docs. I chose the week and both topics and
  set the hours.

**What I understand now, and what I still don't.**
- Now: the voice never sees my spelling. Every mistake I found came from the step that turns words into sounds,
  and respelling works because it changes the sounds.
- Still don't: whether Kokoro would sound better fed misaki's phonemes than espeak's; nothing I found settles it,
  so the video doesn't say.

Evidence: [`evidence/run.log`](./evidence/run.log), [BUILD-LOG](./BUILD-LOG.md), the QC sheets.
