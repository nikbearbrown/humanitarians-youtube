# CHECKS-REPORT — hotel-phone-helper

## Chassis

User asked for a "Deep Explainer" at exactly 4:00 with no footage. The
toolkit's `deep-explainer` skill targets 5–10 minutes and requires ~20–25%
pantry/archival stills — both conflict. Built on the `ai-explainer` chassis
(cold open → presenter intro → body → handoff → outro), matching
`ai-done-right`, `tutor-they-never-had` and `ai-that-never-forgets`. Disclosed
in beat_sheet.json metadata.note.

## Disclosed deviations

1. **Voice/branding** — af_bella (Kokoro) + @HumanitariansAI, per the user's
   request for the most natural-sounding female voice.
2. **Self-intro** — "Hi, I'm Agrima" lives in its own B00B beat (ai-explainer
   convention); B00B also serves as the one-breath executive summary.
3. **Register** — warm, simple, friendly, positive but fair, per the user's
   request, not the default Teardown register.
4. **Pipeline** — run.sh / compile.py / static_scene_check.py /
   manim_layout_audit.py / final_frame_check.py, as on every reel this session.

## PROOF GATE

All 15 beats classify SHOW (each names its on-screen artifact in
`visual_intent`). Arc: framework ✓ (B02–B04) · worked example ✓ (B06 case
study) · evidence ✓ (B05, B06) · falsifiability/caution ✓ (B05 hedge, B09 rules
differ, B11 company-reported) · scaffolded viewer task ✓ (B12) · four
bookends ✓ · no-source-no-verdict ✓ (every figure traced in FACTCHECK.md and
labeled company-reported or report-based).

## GATE A / GATE B (before any pipeline run)

GATE A: zero ERROR; B00B WARN (text-only, expected). GATE B: all twelve scenes
CLEAN after fixes found by running them and by viewing preview frames:

- **B01**: the "an illustration, not a reported case" label overlapped the
  window (GATE B WARN); moved onto the floor strip.
- **B02**: the "early morning" tag overlapped the time-zone chip (GATE B
  ERROR); tags re-spaced under their hours.
- **B03**: the result chips collided with the overnight lane and ran off the
  right edge; they now sit in their own row below both lanes.
- **B06**: the case-study chips spilled past the card's bottom border (a
  shape-overflow the gates cannot see); both cards were made taller and the
  hotel grid smaller.
- **B04 / B08**: flow card widened; lane graphics enlarged.

## Duration

Narration was first 718 words / 246.73 s (6.7 s over the exact-4:00 target);
four small phrases were trimmed (none carrying a figure or a hedge), and the
measured mp3 total is **239.56 s (3:59.6)**.
