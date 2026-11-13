# FRICTIONAL — How AI Music Generators Turn Text Into Audio

The frictional log for this piece of work: short, dated, honest entries about what was tried,
where it resisted, what was done about it and what was learned, appended as the work goes and
never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-10-10 — AI music explainer (week of 5–9 Oct, STEM)

> Written during the build, with Claude, from this session's record. The decisions are mine.

**Working on.** What actually happens between typing a prompt into Suno and hearing a song: for
Lyrical Literacy fellows, who do exactly that every week.

**Tried, and expected.**
- Chose this topic (with Shazam) for this week's two STEM videos.
- Expected to explain how Suno works. That turned out not to be possible: Suno hasn't published it.

**Where it resisted, and what I did next.**
- With Suno's method unpublished, the video says so in the first beat and explains the published
  systems instead (MusicGen, MusicLM), with every number checked against their papers.
- The codec built for the evidence first fell apart on music it hadn't heard, then dropped all the
  treble, and its first quality measure was mostly measuring silence. Each was found by checking the
  numbers before using them, and fixed (BUILD-LOG §2).
- The first "generated" music was a training passage played back. The generator was changed to
  predict coarse tokens one at a time, and the video reports how much it copies: at most a quarter of
  a second.

**What Claude contributed, and what I accepted, changed or rejected.**
- Claude proposed the topics, wrote the codec, the model and the six scenes, ran the fact-check, and
  found each of the problems above.
- I chose the topic, gave the week's hours (20) and asked for no late label.
- My review of the preview: pending at the time of this entry (appended below once done).

**What I understand now, and what I still don't.**
- A music model never writes sound directly: it predicts tokens, and the prompt only tilts the odds.
  So generating several versions and choosing is the method, not a workaround.
- Still don't know how Suno's model works, or how much big models copy from their training music:
  my 0.26 s is a tiny model's number, not theirs.

Evidence: `codec.py`, `synth.py`, `evidence/run.log`, `evidence/codec.json`, `beat_sheet.json`,
`vertical/beat_sheet.json`, QC sheets.
