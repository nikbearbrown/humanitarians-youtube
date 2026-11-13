# FRICTIONAL — One Tool a Week.

> Written 2026-11-03 from this folder's build records (README.md, FACTCHECK.md, PROMPTS.md,
> SHOTLIST.md, beat_sheet.json), not kept week by week during the build.

## 2026-08-30

**Tried / expected.** A weekly recap on the ai-explainer chassis: one Humanitarians AI tool
per week, used, then written up. This week's tool was Brandy (a brand-audit tool), with a
LinkedIn post and two Substack articles shipped, one of them on the Ogilvy copywriting
coach, and a fashion sustainability team proposed by Nina. Built from Yatra's own account of
the week, with the instruction not to invent stats or findings. Kokoro `af_bella`, Remotion,
`@Yatra`, 16:9 at 3840×2160 and a 9:16 derivative.

**Where it resisted, and what was done next.** The records are thin: there is no QC-LOG or
CHECKS-REPORT in this folder, so render or QC problems, if any, are not recorded. What the
records do show are content constraints and how they were handled:
- *Article titles arrived truncated.* Both came with an ellipsis ("I Ran Our Own Brand
  Audit Tool On…", "I Told an AI Copywriting Coach I…"). They render verbatim, ellipsis
  included; B04's narration works with the truncation rather than completing the title.
- *No findings were supplied.* The reel says the audit and the coaching were done and
  written up, and does not say what either found. `RcpCard` was built with no summary or
  findings field so there is nothing to fill.
- *The fashion team is only proposed.* `RcpTeam` requires a `status` string and renders
  "Proposed by Nina — not started yet" as the most prominent element; the verdict card
  repeats it.
- *Self-introduction placement.* At Yatra's request the spoken open starts "Hi, I'm Yatra"
  at B00 instead of in a later beat.
- *Shared composition.* `RcpCard` backs B02 and B04, so its `durationInFrames` was set to
  the shorter beat and the longer one holds its last frame instead of being trimmed.

**What Claude contributed, and what was accepted / changed.** Claude drafted the beat sheet,
narration and on-screen prompts, wrote two new scenes (`RcpCard`, `RcpTeam`) and reused
`RcpWeeks`, `RcpStatus` and `JdgSplit`, and wrote the fact-check ledger. The 9:16 cut was
derived with an explicit empty drop plan, so no beats were cut (2:30.2 with endcard). The
records do not say what Yatra changed or rejected.

**Now understood / still open.**
- Open: no frame-level QC record exists in this folder, so there is no record of the
  renders being checked by eye.
- Open: the Brandy link and the article titles are as supplied; the records do not show
  them being re-checked.
