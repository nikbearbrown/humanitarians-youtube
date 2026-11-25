# FRICTIONAL — This Week, Gordy.

> Written 2026-11-03 from this folder's build records (README.md, BUILD-PROMPT.md,
> CHECKS-REPORT.md, FACTCHECK.md, PROMPTS.md, QC-LOG.md, SHOTLIST.md, SOURCES.md,
> YOUTUBE.md), not kept week by week during the build.

## 2026-09-03

**Tried / expected.** The next weekly one-tool recap after Brandy: Gordy used, graphics made
for the Humanitarians AI LinkedIn page, two articles written and with Nina for review. Yatra's
constraint: do not say the articles are published, and do not invent their content. Asked
for "not a variation of any previous video." 12 beats, 2:23, Kokoro `af_bella`, `@Yatra`,
16:9 at 4K plus a full 9:16 vertical.

**Where it resisted, and what was done next.**
- *Unfinished work.* The reel was built around the week ending mid-pipeline: five stages,
  four closed, PUBLISH open. `WkReview` has no title or content prop, so the articles render
  as empty dashed slots and the Substack node stays hollow. `WkShip` draws no artwork and
  its chip says MADE, not LIVE.
- *A thin source.* Two fetches of the Gordy tool page returned one sentence; the "command
  reference" did not appear. The description renders verbatim, the "two modes" are not
  named, and B03 says on screen that one line is all the page publishes.
- *"Not a variation" vs. a series.* This could not hold literally for a series episode.
  Differentiation applied instead: seven new `Wk*` components, a different spine, narration
  checked line by line against Brandy, and a new greeting (`Jambo`).
- *Render blocked by the environment.* Two stacked faults. Remotion's bundled ffmpeg could
  not load its dylibs on no-audio beats; fixed with `DYLD_LIBRARY_PATH`, now set by
  `remotion_scenes.py`. Separately, the browser launch timed out with empty logs, and a
  control composition from the previous reel failed the same way. A `sample` of the "hung"
  process showed slow module reads on a 94%-full volume, not a deadlock, and some early runs
  had been killed while still progressing. System Chrome via `ART_CHROME` worked but still
  failed intermittently; a retry sweep re-renders missing beats one at a time.
- *A handoff mid-failure.* BUILD-PROMPT.md was written when the render stood at 0/12 beats
  with the browser fault unfixed, to hand the build to a fresh session. QC-LOG.md records
  what followed: both faults worked around, and 12/12 landscape and 12/12 portrait rendered.
- *QC.* Zero layout defects on first pass, credited to budgeting geometry against `SAFE`
  after the previous reel's four collisions. GATE V on the clean master: 0 BLOCKER, 4 MAJOR
  underfill on stock bookends, accepted. A B02 low-contrast flag on the vertical was judged
  a false positive after looking at the frame. `--handle "@Yatra"` was passed to `shorts.py`
  and the endcard checked in the encoded file.

**What Claude contributed, and what was accepted / changed.** Claude drafted the beat sheet,
narration and on-screen prompts, fetched the tool page, wrote the seven scenes, diagnosed the
render environment, changed `remotion_scenes.py` (dylib path, local Remotion binary,
`ART_SCALE`, `ART_CONCURRENCY`; defaults unchanged), ran QC and wrote the paperwork. The
records do not say what Yatra changed or rejected.

**Now understood / still open.**
- Understood: the earlier "hang" was I/O contention on a nearly full disk, not a deadlock.
- Open: a Remotion version mismatch (4.0.486 vs 4.0.490) remains unpinned.
- Open: the articles' titles, content and review outcome are not in the records.
- Open: the real LinkedIn graphics could be dropped in at `pantry/B06.png`; not done.
