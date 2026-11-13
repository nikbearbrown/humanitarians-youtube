# CHECKS-REPORT — ai-colleague-quota

## Chassis

User asked for a "Deep Explainer" at exactly 4:00 with no footage. The
toolkit's `deep-explainer` skill targets 5–10 minutes and requires ~20–25%
pantry/archival stills — both conflict. Built on the `ai-explainer` chassis
(cold open → presenter intro → body → handoff → outro), matching
`hotel-phone-helper`, `ai-done-right` and `tutor-they-never-had`. Disclosed in
beat_sheet.json metadata.note.

## Disclosed deviations

1. **Voice/branding** — af_bella (Kokoro) + @HumanitariansAI, per the user's
   request for the most natural-sounding female voice.
2. **Self-intro** — "Hi, I'm Agrima" lives in its own B00B beat (ai-explainer
   convention); B00B also serves as the one-breath executive summary.
3. **Register** — warm, simple, friendly, positive but fair, per the user's
   request, not the default Teardown register.
4. **Pipeline** — run.sh / compile.py / static_scene_check.py /
   manim_layout_audit.py / final_frame_check.py, as on every reel this session.
5. **Numbers on screen** — the user's tip allows keeping only 87%, 54% and 46%
   on screen if crowded. All the article's figures (87%, 1.7x, 94%, 54%, 34%,
   46%, about a third) were kept, spread over four stat scenes (B04, B05, B06,
   B07) so no scene carries more than three; each is labeled with its source.

## PROOF GATE

All 14 beats classify SHOW (each names its on-screen artifact in
`visual_intent`). Arc: framework ✓ (B02–B03) · worked example ✓ (B06 Siemens) ·
evidence ✓ (B04–B07, each labeled company-reported) · falsifiability/caution ✓
(B05 surveys differ, B07 data quality, B10 industry-reported) · scaffolded
viewer task ✓ (B11) · four bookends ✓ · no-source-no-verdict ✓ (every figure
traced in FACTCHECK.md).

## GATE A / GATE B (before any pipeline run)

GATE A: zero ERROR; B00B WARN (text-only, expected). GATE B: all eleven scenes
CLEAN on the first run. Preview frames of all ten body scenes were viewed; no
shape or text overflow found.

## Duration

First narration pass measured 696 words / 252.53 s (12.5 s over the exact-4:00
target); eight small connective phrases were trimmed (none carrying a figure, a
source, or a hedge), and the measured mp3 total is **239.42 s (3:59.4)**.
