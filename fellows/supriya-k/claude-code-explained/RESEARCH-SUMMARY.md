# RESEARCH-SUMMARY — claude-code-explained

## Sources

All in this toolkit; `v2/` = `projects/banking-data-analyst-interview-prep/banking-domain-interview-end-to-end-v2/`.

- `HOW-TO.md` §1 — the conductor model.
  > "Claude cannot watch the video. It has never sat in the audience… But flip it around: Claude
  > is superhuman at the build."
- `v2/PLAN.md` — the plan that held the cycle-1 assumption and the v1 measurements.
  > "Frame-fill: `ClaudeComposerAsk` is already portrait-aware" (line 119)
  > v1 9:16 "2160×3840 | **139.5 kbps**"; "text filling only ~15–20% of frame height" (lines 27–33)
- `v2/STATUS.md` — gate 3 and the 9:16 fix log (both cycles).
  > "`ClaudeComposerAsk916` (B00) FAILED its first sanity render — … content clustered in the top
  > ~55% of frame… Re-rendered: content now spans topic-to-rule ≈86% of frame height (was ≈55%),
  > bitrate 341kbps (was 276kbps)."
  > "`manim -r 2160,3840` does NOT recalculate `config.frame_width`/`frame_height`… silently
  > compressed all 4 portrait Manim scenes into roughly the center 25-28% of the real canvas —
  > despite every scene passing Gate B… because that audit tool manually overrides these same two
  > config values in its OWN separate process"
- `runtime/remotion/src/scenes/ClaudeComposerAsk916.tsx` — B04 code (lines 46, 50–51, 87–92).
- `v2/short/scenes.py` — B07 code (lines 27–34).

## The through-line

Both bugs share one shape: **something said "fine" without looking at the frame**. In cycle 1 it
was a plan's assumption; in cycle 2 an automated audit that checked a different coordinate space.
Both were caught by the verify step — rendering and looking. That's the case for keeping a human in
the gate and the look, and Claude in the build.

## Synthesis flagged as synthesis

"Both bugs looked fine on paper" (B09) is this reel's framing of the two STATUS entries, not a
quote.
