# CHECKS-REPORT — ai-done-right

## Chassis

User asked for a "Deep Explainer" at exactly 4:00 with no footage. The
toolkit's `deep-explainer` skill targets 5–10 minutes and requires ~20–25%
pantry/archival stills — both conflict. Built on the `ai-explainer` chassis
(cold open → presenter intro → body → handoff → outro), matching
`tutor-they-never-had`, `ai-that-never-forgets` and `no-face-no-problem`.
Disclosed in beat_sheet.json metadata.note.

## Disclosed deviations

1. **Voice/branding** — af_bella (Kokoro) + @HumanitariansAI, per the user's
   request for the most natural-sounding female voice.
2. **Self-intro** — "Hi, I'm Agrima" lives in its own B00B beat (ai-explainer
   convention); B00B also serves as the one-breath executive summary.
3. **Register** — simple, observational, relatable, neutral and fair, per the
   user's request, not the default Teardown register.
4. **Pipeline** — run.sh / compile.py / static_scene_check.py /
   manim_layout_audit.py / final_frame_check.py, as on every reel this session.

## PROOF GATE

All 13 beats classify SHOW (each names its on-screen artifact in
`visual_intent`). Arc: framework ✓ (B01–B02) · worked example ✓ (B03, Adalat
AI) · evidence ✓ (B04–B07) · falsifiability/caution ✓ (B08: self-reported,
already-AI users, Google.org-supported, Bridgespan) · scaffolded viewer task ✓
(B10) · four bookends ✓ · no-source-no-verdict ✓ (every figure traced in
FACTCHECK.md; every percentage framed as self-reported).

## GATE A / GATE B (before any pipeline run)

GATE A: zero ERROR; B00B WARN (text-only, expected). GATE B: all ten scenes
CLEAN after fixes found by running them and by looking at rendered preview
frames:

- **B02**: the static check crashed on a list-vs-array division in a heading
  position; replaced with explicit coordinates. A duplicate "AI on the side"
  heading (outer label and card title) was removed.
- **B03 / B05 / B08**: footers sat in the bottom margin (GATE B WARN); moved up.
- **B04**: the three identical cards registered a "shapes never change" ERROR
  (GATE A); fixed by fading each card in as a whole group across separate
  plays.
- **B07**: the "about 24%" label ran off the right edge (frame ERROR); bars
  shortened and shifted left.
- Multi-line card labels were left-aligned under centered numbers; rebuilt as
  stacked centered lines. One B08 bullet had shrunk to a smaller font than its
  siblings; the fit-to-width clamp was removed.
- Reveal pattern: cards grow first, then their contents fade in.

## Duration

684 narration words at ~2.85 words/second; the measured mp3 total is
**240.02 s (4:00.0)**, so no narration correction was needed.
