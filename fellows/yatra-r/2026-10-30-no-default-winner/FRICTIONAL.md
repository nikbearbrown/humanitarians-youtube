# FRICTIONAL — No Default Winner.

## 2026-10-30

**Tried / expected.** A 1–3 minute ai-explainer on customers no longer trusting the human
rep by default when an AI tool disagrees — five supplied figures, one source (Capacity,
October 2026), "Bella, in for Yatra" intro, `@Yatra` bug, true 4K in 16:9 and 9:16. Built
with Claude Code on the brutalist.art toolkit, same pipeline as `ads-in-the-picture`.

**Where it resisted, and what was done next.**
- *A finding with no number.* "Equally likely to trust either" came without a figure. The
  scale scene was built with no numeric prop, so it settles level and prints nothing — a
  50/50 label would have been an invented statistic.
- *The arc's claim isn't data.* "Most companies haven't caught up" is not in the Capacity
  figures, so the narration owns it as a read, and the screen labels it as interpretation
  twice.
- *Icons that editorialised.* The first person icon read as a frowning face; redrawn as a
  neutral silhouette before render.
- *Render timeouts.* Two portrait beats timed out at 4K — orphaned headless-Chrome processes
  plus high machine load. Cleared and re-rendered at lower concurrency with a longer
  per-frame timeout.

**What Claude contributed, and what was accepted / changed.** Claude drafted the beat sheet
and narration (it fit the brief on the first audio pass, 2:42), wrote the eight `Ctr*`
scenes, ran audio/render/compile, and did the frame-level QC. Nothing beyond the five
supplied figures was added.

**Now understood / still open.**
- Open: the Capacity release itself was not re-checked in this build.
- Masters are local (not committed): `~/Downloads/brutalist-reels/youtube/yatra-no-default-winner/`.
