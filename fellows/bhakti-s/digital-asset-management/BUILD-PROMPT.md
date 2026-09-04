# BUILD-PROMPT.md — claude-hai-profile-bhakti-save

Paste-ready prompt to rebuild this reel end to end (gate check → audio →
conform → render → visual QC → report). Never publishes — master stays in
this folder for human review.

Run from the `brutalist.art-main` repo root, e.g. under
`claude --dangerously-skip-permissions` (safe here: git-tracked, regenerable
outputs, no paid API calls in this reel — Kokoro is free/local).

```
Rebuild the reel at youtube/claude-hai-profile-bhakti-save end to end:

1. Generate audio: python3 runtime/scripts/generate_audio_kokoro.py
   youtube/claude-hai-profile-bhakti-save
   Report each beat's real duration. If B03's lifecycle reveal timing
   (DamLifecycleReveal's revealFrames prop) is more than ~1s off from a
   proportional split of the new duration against the six lifecycle lines'
   word counts, recompute and update it in beat_sheet.json before rendering.

2. Run ART_STRICT=0 bash runtime/scripts/run.sh
   youtube/claude-hai-profile-bhakti-save
   ART_STRICT=0 is intentional here — see CHECKS-REPORT.md for why BOUT and
   BVDT are accepted underfill warnings, not something to "fix" by resizing
   shared toolkit components.

3. If GATE L fails on the fixed kicker requirement, confirm
   metadata.topic and every ClaudeComposerAsk beat's topic prop still read
   exactly "Irreducibly Human" — this is a claude-hai channel requirement,
   not a per-video choice.

4. If GATE V reports new underfill/edge-bleed defects on any of the five
   custom components (DamExecSummary, DamStatCard, DamLifecycleReveal,
   DamSopsChips, DamComparisonGrid), read _qc/REPORT.md, then:
   a. Edit the component's .tsx in runtime/remotion/src/scenes/
   b. Delete the stale youtube/claude-hai-profile-bhakti-save/media/<beat>.mp4
      — remotion_scenes.py checks for the file on disk, not just beat sheet
      metadata, so a stale mp4 will be skipped even after a source edit.
   c. Clear that beat's "build" key in beat_sheet.json.
   d. Re-run step 2.
   Log what changed and why in BUILD-LOG.md, in the same style as the
   existing entries — this file has a real remediation history worth
   extending, not starting over.

5. Note: B01's narration and on-screen content deliberately diverge as of
   2026-08-31 — the spoken narration includes a personal self-introduction
   the on-screen DamExecSummary card does not show. If regenerating B01,
   preserve this split rather than "fixing" the mismatch — see BUILD-LOG.md
   and PEDAGOGY.md for why.

6. Report final GATE L / GATE V status and the output path of the compiled
   mp4. Do not publish anywhere — that's a separate human decision.
```
