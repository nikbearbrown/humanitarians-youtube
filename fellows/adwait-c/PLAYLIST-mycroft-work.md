# Playlist — Mycroft Finance Investigator: the weekly work video

**Fellow:** Adwait Changan · **Channel:** @HumanitariansAI · **Voice:** Kokoro `am_onyx`
**Cadence:** one video every Friday, paired with that week's STEM episode.

## What this track is

The second of the two videos due each week. Where the STEM track teaches a concept, this
one reports what was actually built on the
[Mycroft Finance Investigator](https://github.com/nikbearbrown/mycroft) that week: the
feature, the real run against this project's own committed data, and the thing it still
cannot do.

The through-line across the whole track is a single question — **what must a finance agent
refuse to do on its own?** Each week adds one refusal and pays for it honestly.

| Friday | Title | The feature | The refusal it adds |
|---|---|---|---|
| 2026-07-27 | Building the Mycroft Finance Investigator | the investigator itself | — |
| 2026-07-31 | The Finance Agent That Cannot Approve Itself | human review gate | the agent cannot sign off on its own findings |
| 2026-08-07 | How Do You Test a Finance Agent? | evaluation harness | break the books on purpose, then check it notices |
| 2026-08-14 | What-If Analysis Without AI Guessing | scenario engine | no invented numbers; every figure is derived |
| 2026-08-21 | Can You Prove What Your Finance Agent Actually Did? | audit bundle | a claim without a recomputable hash is not evidence |
| 2026-08-28 | Trend Investigation | recurring-gap detection | a repeated gap is a finding, not noise |
| 2026-09-04 | One Agent, or a Team? | supervisor and specialists | every ranked gap is blocked on a human owner |
| 2026-09-11 | Checking Its Own Work | re-investigation loop | an exact replay still does not close a finding |
| 2026-09-18 | Who Approves the Threshold? | materiality approval | the agent cannot approve its own threshold |
| 2026-09-25 | How Old Is the Evidence? | freshness assessment | missing provenance is refused, not assumed fresh |
| 2026-10-02 | When the Reviewer Disagrees | disagreement log | a reviewer may not restate the engine's number |
| 2026-10-09 | Citations Nobody Checks | evidence coverage | an unparseable reference raises, never skipped |
| 2026-10-16 | Whose Failure Is It? | ownership triage | prove whose failure it is before fixing it |
| 2026-10-23 | May This Leave the System? | distribution gate | blocked by default; cleared only on evidence |

Every video ships in **both** aspect ratios: a 16:9 master at 3840×2160 and a 9:16
derivative cut at 2160×3840, named `Mycroft_AdwaitChangan_YYYY-MM-DD.mp4`.

## Rules specific to this track

1. **Every figure on screen comes from a real run** against the project's own committed
   data, captured in that reel's `SOURCES.md`. Totals are not enough: read the emitted
   artifact, because a headline number can be right while the breakdown under it is wrong.
2. **No fabricated approval, review or dissent.** Where a named approver or reviewer
   appears on screen it is a **test fixture and the screen says so**. No approval record
   attributable to a real person is committed anywhere in the Mycroft repository.
3. **Never show code attributed to a file it is not in.** Code beat props are generated
   from the real file at authoring time.
4. **Name the limit.** Every verdict card states what the week's feature still cannot do.
   A gate that cannot stop anyone is described as exactly that.
5. **Dates describe the week of work, not the day it was edited.** Build dates are recorded
   as they happened in each `BUILD-LOG.md`; nothing backdates a commit.

## Where the work lives

Source, tests and run logs: `projects/Mycroft-Finance-Investigator/` in
`nikbearbrown/mycroft`. This repository holds only the videos' beat sheets and paperwork.
Masters go to the Drive by hand. Media is gitignored and never committed here.
