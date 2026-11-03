# BUILD-LOG.md — claude-hai-built-from-zero-thesis

## 2026-08-29 — build (second video of the "Built From Zero" series)

- GATE L: ran `./art scene-index` before searching, since the DAM video's
  5 custom components had never been indexed (no header comment — same
  "derived text" gap `DamStatCard` was already flagged with). Search
  results confirmed only `DamStatCard` reliably surfaces via search;
  `DamLifecycleReveal`, `DamSopsChips` did not appear for reasonable query
  terms. Proceeded with direct reuse by name anyway, since these were
  authored in-session and their schemas were already known — but the
  header-comment gap is a real, unresolved discoverability issue worth
  fixing separately (not done as part of this build).
- Identified a real risk before building: `DamLifecycleReveal` was tuned
  for exactly 6 steps (the DAM video). This video needed 4. Fixed the
  component to scale box height inversely with step count *before*
  authoring the beat sheet on top of it — verified via test renders at
  both 3 and 6 steps (screenshots) to confirm no regression to the
  original DAM video's layout.
- Audio generated via Kokoro `am_onyx`, 8 beats, real durations replacing
  estimates. B03's `revealFrames` recomputed proportionally against real
  duration (word-count method, same as the DAM video).

## GATE V remediation

- First full pass: 7 MAJOR — `B03_50` (accepted, see CHECKS-REPORT.md),
  `B04` (both samples), `BOUT`/`BVDT` (accepted, shared components).
- **B04 (DamSopsChips, 2 chips instead of the original 4):** genuine
  structural underfill — large empty band between chip row and closing
  text at reduced chip count. Fixed by scaling chip size/padding inversely
  with team count and anchoring the closing line to the actual bottom of
  the chip row instead of a fixed offset. Verified via test render before
  re-running the pipeline. Re-render confirmed clean.
- Final state after this pass: GATE L clean, GATE V 0 BLOCKER / 0
  unresolved MAJOR (5 remaining accepted per CHECKS-REPORT.md).

## Note for future reels reusing these components
This build is what first exposed `DamSopsChips`'s scaling gap at n=2. That
fix's formula (`sqrt(4/n)`, capped at 1.7) turned out to still be too weak
at n=3 — this was caught and fixed again during the *next* video in this
series (`claude-hai-built-from-zero-compliance`); see that reel's
BUILD-LOG.md for the stronger linear-scale fix.

## 2026-08-31 — B01 revision: added personal self-introduction, then
## reverted the on-screen half of it (this video is where that got decided)

- Series-wide request: add a personal self-intro ("Hi, I'm Bhakti Save,
  Creative Project Manager...") to beat 2 (B01) across all three videos.
- First draft replaced both narration and the on-screen `DamExecSummary`
  content in all three videos. Re-running the pipeline on *this* video
  specifically surfaced a new GATE V finding: `B01` at exactly 55% fill
  against the 55% minimum threshold — sitting right on the boundary, not
  a clear underfill defect, but not passing clean either. Investigated
  via a targeted test render before deciding how to respond, rather than
  assuming it needed a component-level fix like the earlier B01/B04
  issues in this series.
- This specific finding is what prompted clarifying the subject's actual
  intent: she wanted the self-intro **heard**, not necessarily **shown
  on screen**. Once confirmed, the fix was to revert `DamExecSummary`'s
  `eyebrow`/`headline`/`subline` props to their original content (across
  all three videos in the series, for consistency) while keeping the
  self-intro text in `narration_text` only.
- Regenerated audio for B01 (narration had changed earlier in this
  process), cleared the stale render, re-ran the full pipeline.
- Re-render confirmed: MAJOR count returned to this video's known
  baseline (5 — B03 timing artifact + BOUT/BVDT), and the marginal B01
  finding disappeared entirely along with the reverted visual.
