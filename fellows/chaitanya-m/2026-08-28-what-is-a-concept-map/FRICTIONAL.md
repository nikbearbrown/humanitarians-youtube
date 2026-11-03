# FRICTIONAL — What Is a Concept Map

The frictional log for this piece of work: short, dated, honest entries about
what was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-09-28 — Retrospective entry for the 2026-08-28 reel

> **Written 2026-09-28, a month after the work it describes.** The
> frictional-log rule arrived 2026-09-22, after this reel was built and merged,
> so no contemporaneous log exists. Reconstructed from this folder's
> `BUILD-LOG.md` (which is detailed, including a revision-2 section),
> `QC-REPORT.md` as it was at build time, `FACTCHECK.md` and the commit history
> — then drafted with Claude from that record. **Sections marked
> `[NOT RECORDED]` are gaps only I can fill.**

**Working on.** The first reel of the series: an audit of the Concept Map
subsystem in `medhavi-hub`, turned into a Brutalist explainer.

**Tried, and expected.** Two rules set up front, both of which shaped
everything after: every number on camera gets read off the code or the fixtures,
and the art direction is written into the script before any scene exists. I
expected the second to make the build mechanical. It did.

**Where it resisted, and what I did next.**

- The narration measured 3:48.86 against a 5:15 target — 96 seconds short. I
  did not pad it with holds, because that buys runtime with dead air. Logged
  the shortfall with three options instead of hiding it.
- The script under-specified in three places and contradicted itself in one:
  it asked for two red elements at once while its own hard rules forbid it, and
  it struck three table rows that the earlier scene had never drawn. Each
  resolved toward the script's own rules and recorded rather than silently
  patched.
- First QC pass found six defects, two major. A later pass found a seventh the
  first had missed: B04 opened on 7.5 seconds of empty chart, which reads as
  failed media. The first pass had sampled frames at 55% and 92% of each beat
  and landed on settled states both times.
- The 9:16 was initially built full-length by bypassing `shorts.py`. That was
  wrong — the 3:00 cap is a real constraint — and it was rebuilt as a proper
  short. The superseded cut is not carried in this folder.
- At port time, the fact-check found one failure: B06 shows
  `wikipedia_categories` as `["Taxanes", "Antineoplastic"]` where the fixture
  has three different values. It had been flagged as invented during the build
  and never checked. **Still unfixed.**

**What Claude contributed — accepted, changed, rejected.**

- Claude built the renderer, ran the QC passes, wrote the build log and the
  fact-check, and did the port into this repository.
- Accepted: not padding the runtime; keeping the 32px caption tier at spec even
  though it lands near 9px on a 1080p transcode, because those strings are
  technical furniture rather than content.
- Changed: the dependency edges in B08 were first drawn as one bus with a single
  arrowhead, which made "the three red edges remain" fail once the box was cut.
  Rebuilt as three independent routes.
- `[NOT RECORDED]` — what I rejected in the original plan, how many script
  drafts there were, and whether the Brutalist direction was my first choice.

**Understand now / still don't.**

- Now: sampling settled states cannot find a bad *opening*. Frame QC has to
  include t≈0 for every beat, not just the middle and the end.
- Now: "duration is an output, never a target" is not a slogan — the moment I
  treated 5:15 as a target I was reaching for holds.
- Still open: the B06 fabricated value. It is a one-line fix in
  `scenes/render_scenes.py` plus a re-render of that beat and a re-cut, and it
  has been outstanding for a month. Nothing said aloud is false, which is
  exactly why it has been easy to keep deferring.
- Still open: this reel is `am_onyx` and the series moved to `af_bella` on
  2026-09-17. It stays as the outlier.

**Evidence:** [`BUILD-LOG.md`](./BUILD-LOG.md) · [`FACTCHECK.md`](./FACTCHECK.md) ·
[`PEDAGOGY.md`](./PEDAGOGY.md) (GATE P, signed 2026-09-17) ·
[`SHOTLIST.md`](./SHOTLIST.md) · PR [#69](https://github.com/nikbearbrown/humanitarians-youtube/pull/69)
