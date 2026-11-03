# BUILD-LOG.md — claude-hai-built-from-zero-compliance

## 2026-08-29 — build (third video of the "Built From Zero" series)

- Audio generated via Kokoro `am_onyx`, 8 beats. B03's `revealFrames`
  recomputed against real duration for 3 steps (word-count method).
- First full pipeline pass: GATE L clean. GATE V: 9 MAJOR — more than
  either prior video in the series, and not simply a repeat of already-
  fixed issues.

## GATE V remediation — two real, distinct bugs found

- **B03 (3 steps):** flagged only at the 50% sample, same pattern as the
  thesis video. Confirmed as the same reveal-timing artifact, not a new
  issue. Accepted as-is, consistent with the earlier decision.

- **B04 (DamSopsChips, 3 chips):** flagged at *both* samples — a real
  regression the thesis video's fix didn't cover. Root cause: that fix's
  scale formula (`sqrt(4/n)`, capped at 1.7) gives a strong boost at n=2
  (1.41x) but only a weak one at n=3 (1.15x) — not enough to close the
  gap. Fixed by switching to a linear formula (`4/n`, capped at 1.8),
  which gives a meaningfully larger boost at n=3 (1.33x), and by adding a
  bottom-anchored floor for the closing line's position (`max(computed
  position, 72% of frame height)`) so it never sits too high regardless of
  how short the chip row ends up. Verified via test render before
  re-running.

- **B01 (DamExecSummary):** a genuinely new gap, not seen on either prior
  video. The DAM video's original headline (~72 characters) wrapped into
  two nearly full-width lines at the component's fixed font size. This
  video's shorter headline (~56 characters) wrapped to two lines that each
  fell well short of the container edge, at the same font size — visible
  underused width on both lines. Root cause: font size was never made a
  function of headline length. Fixed by scaling headline font size
  inversely with character count, calibrated against the original DAM
  headline as the baseline (72 chars → 1.0x), capped at 1.5x for very
  short headlines. Verified via test render before re-running.

- Re-render confirmed both fixes worked: MAJOR count dropped from 9 to 5,
  with the remaining 5 all previously-accepted findings (B03 timing
  artifact, BOUT/BVDT shared-component warnings) — no new defects
  introduced by either fix.

## Final state (2026-08-29)
GATE L: clean. GATE V: 0 BLOCKER, 0 unresolved MAJOR (5 accepted per
CHECKS-REPORT.md). Both component fixes made in this build (`DamSopsChips`
v3, `DamExecSummary` headline scaling) also apply retroactively to any
future reuse of these components — see the thesis video's BUILD-LOG.md
for the earlier, insufficient version of the chips fix this one replaces.

## 2026-08-31 — B01 revision: added personal self-introduction

- Same series-wide request as the DAM video: add a personal self-intro
  ("Hi, I'm Bhakti Save, Creative Project Manager...") to beat 2 (B01)
  across all three videos.
- First draft replaced both narration and the on-screen `DamExecSummary`
  content. Re-render on the companion thesis video surfaced a marginal
  GATE V finding (55% fill against the 55% minimum — right on the
  boundary) specific to that video's subline length. Rather than chase a
  per-video fill edge case, the subject clarified her actual preference:
  keep the self-intro in **narration only**, revert the on-screen card to
  its original content.
- Reverted `DamExecSummary`'s `eyebrow`/`headline`/`subline` props to the
  original values ("CAMPAIGN COMPLIANCE" / "Marketing doesn't end when
  the campaign gets approved." / "The riskiest hours are often the ones
  nobody's watching."). Kept the self-intro in `narration_text` only.
  Regenerated audio for B01 (narration text had changed), cleared the
  stale render, re-ran the full pipeline.
- Re-render confirmed: MAJOR count returned to this video's known
  baseline (5 — B03 timing artifact + BOUT/BVDT), confirming the revert
  introduced no new defect.
