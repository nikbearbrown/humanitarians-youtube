# FRICTIONAL — How Spotify Picks Songs

The frictional log for this piece of work: short, dated, honest entries about what was tried, where it
resisted, what was done about it and what was learned, appended as the work goes and never rewritten. What an
entry contains, and why: <https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-11-09 — Building a small recommender, and the STEM video about it

> Written during the build (Monday 9 Nov, for the week of 2–6 Nov).

**Working on.** The first of this week's two STEM explainers: how a music app recommends songs, tested on a
made-up service because Spotify's data and recipe aren't public.

**Tried, and expected.**
- The build's working assumption (Claude's) was the familiar story: a feedback loop narrows what people are
  shown, a filter bubble.
- Western test material: 8 Western genres.

**Where it resisted, and what I did next.**
- The first made-up data was too easy: a 98% hit rate and 97.5% same-genre neighbours, and the loop showed no
  bubble. The data was made sparser, with overlapping genres; now 74.1% against 65.3% for "just the hits" and
  6.4% for random (BUILD-LOG §2).
- Even then the loop broadened the lists (genres per list 4.05 → 4.66 over 8 rounds). Instead of telling the
  expected story, the narration follows the measurement: no filter-bubble claim, and exploration shown as a
  with-and-without comparison (BUILD-LOG §3).
- The cold-start "0 of 3,000 lists" was printed as a constant, so it was checked separately before scripting
  (BUILD-LOG §4).

**What Claude contributed, and what I accepted, changed or rejected.**
- Claude researched what Spotify says and what the papers say, wrote the test, the scenes and the docs. I set the
  brief and the hours.

**What I understand now, and what I still don't.**
- Now: a recommender with no genre labels still finds genres, because the same people play the same songs; it
  is only a little better than recommending the hits, it leans on them, and a song nobody has played is
  invisible to it.
- Still don't: whether real feedback loops narrow listening, since mine didn't, and Spotify's own study shows an
  association, not a cause; and how Spotify weighs a skip or a save, which it doesn't publish.

Evidence: [`evidence/run.log`](./evidence/run.log), [BUILD-LOG](./BUILD-LOG.md).
