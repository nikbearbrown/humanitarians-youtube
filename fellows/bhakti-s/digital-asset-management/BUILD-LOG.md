# BUILD-LOG.md — claude-hai-profile-bhakti-save

## 2026-08-29 — initial build

- GATE L (beat-mix lint): FAILED on first run — `claude-hai` channel requires
  the fixed kicker "Irreducibly Human"; beat sheet had a per-video custom
  topic string. Fixed by setting `metadata.topic` and both `ClaudeComposerAsk`
  beats' `topic` prop to the required fixed value. Re-ran: **clean**.
- Audio generated via `generate_audio_kokoro.py` — 9 beats, Kokoro `am_onyx`,
  $0.00 cost. Real per-beat durations replaced the estimated durations used
  when the beat sheet was first authored (biggest delta: B03 lifecycle beat,
  estimated 24s vs. actual 19.75s — `DamLifecycleReveal`'s hardcoded
  `revealFrames` were recomputed proportionally against the real duration
  before first render).
- `remotion_scenes.py` — all 9 beats rendered clean on first pass (no crashes)
  once the `defaultProps={{}}` bug (see below) was caught and fixed pre-build.
- GATE V (visual QC): first full-reel run — 0 BLOCKER, 12 MAJOR (`underfill`)
  across B01, B02, B04, B05 (all 5 custom-authored components) plus BOUT,
  BVDT (2 shared toolkit components).

## Component-fill remediation

- **B01 (DamExecSummary), B04 (DamSopsChips), B05 (DamComparisonGrid):**
  enlarged fonts and spread content across more of the safe area (larger
  type, wider grids, taller cards). Fixed on first attempt — re-render
  confirmed **clean**.
- **B02 (DamStatCard):** required three iterations.
  1. First attempt: enlarged fonts in place, centered layout unchanged.
     Fill improved 16% → 45%, still short of the 55% minimum.
  2. Second attempt: restructured to a left/right split (giant stat left,
     label+body right) to use more of the frame *width*. Fill regressed to
     38% — the split didn't address the real problem, which was vertical
     centering leaving large top/bottom margins on both halves.
  3. Third attempt: anchored content to the top and bottom of the safe area
     (`justify-content: space-between` spanning ~76% of frame height) instead
     of centering, and enlarged the stat glyph substantially. This introduced
     a new, more serious defect — the enlarged serif numeral's natural
     leftward overshoot stroke clipped off the left edge of frame at
     `fontSize: height * 0.68`. Caught by visual inspection (screenshot),
     not GATE V, before it reached the pipeline. Fixed by reducing to
     `height * 0.52` and adding a 1.5x left-padding buffer specifically for
     the glyph's overshoot. Re-rendered: no edge bleed, good height coverage.
     Passed GATE V clean on the following full-reel run.
- **BOUT, BVDT:** pre-existing shared toolkit components (`ClaudeTitleOutro`,
  `ClaudeVerdictArtifact`), not authored for this reel. Fixed-pixel sizing,
  not relative to frame height — underfill is a pre-existing characteristic
  of these components at short content lengths, not something introduced by
  this build. Decision: accept via `ART_STRICT=0` rather than resize shared
  components used by other reels. See CHECKS-REPORT.md.

## Bugs caught during authoring (not visible in final output, logged for
## anyone touching these components later)

- All 5 new components initially registered in `Root.tsx` with
  `defaultProps={{}}`. Remotion's zod `.default()` values are not applied on
  `still` renders — array-prop components (steps/teams/platforms) crashed
  with `Cannot read properties of undefined`; string-prop components
  (DamExecSummary, DamStatCard) rendered silently blank instead of crashing,
  which delayed catching the same root cause in both. Fixed by writing out
  explicit `defaultProps` for every new Composition entry.
- Two full pipeline re-runs (`run.sh`) reported the beat-fix files as "filled
  already (skip)" despite source changes, because `remotion_scenes.py` checks
  for the existing rendered `.mp4` on disk, not just the beat sheet's `build`
  metadata. Clearing `build` status in beat_sheet.json alone was insufficient
  — the stale `media/<beat>.mp4` also had to be deleted before a re-render
  would actually pick up source changes.

## Final state (2026-08-29)
GATE L: clean. GATE V: 0 BLOCKER, 0 unresolved MAJOR (4 remaining MAJOR
findings on BOUT/BVDT accepted via `ART_STRICT=0`, documented above). Final
cut: `claude-hai-profile-bhakti-save.mp4`, 115.6s.

## 2026-08-31 — B01 revision: added personal self-introduction

- Subject requested a personal self-intro added to beat 2 (B01): "Hi, I'm
  Bhakti Save, Creative Project Manager" plus a one-line hook into the
  video's topic, applied consistently across all three videos in this
  reel's family (this DAM video, plus the two "Built From Zero" reels).
- First draft replaced both the narration *and* the on-screen
  `DamExecSummary` card content with the self-intro. Re-render on the
  companion thesis video surfaced a new GATE V finding on B01 (55% fill
  against the 55% minimum — right on the boundary), specific to that
  video's particular subline length. Rather than chase a marginal
  per-video fill issue, the subject's actual preference was clarified:
  keep the self-intro in the **narration only** — the on-screen card
  should stay exactly as it was before this change.
- Reverted `DamExecSummary`'s `eyebrow`/`headline`/`subline` props to
  their original content; kept the new self-intro text in
  `narration_text` only. Re-generated audio for B01 (narration changed),
  cleared the stale B01 render, and re-ran the full pipeline.
- Re-render confirmed: MAJOR count returned to this video's known
  baseline (4 — BOUT/BVDT only), confirming the revert introduced no new
  defect. Runtime changed slightly (112.7s, was 115.6s) due to the new,
  differently-timed narration in B01.
- Net effect: viewers now hear a personal introduction in beat 2 that
  doesn't appear as on-screen text — a deliberate choice, not an
  oversight.
