# CHECKS-REPORT — tutor-they-never-had

## Chassis

User asked for a "Deep Explainer" at exactly 4:00 with no footage. The
toolkit's `deep-explainer` skill targets 5–10 minutes and requires ~20–25%
pantry/archival stills — both conflict. Built on the `ai-explainer` chassis
(cold open → presenter intro → body → handoff → outro), matching
`no-face-no-problem` and `ai-that-never-forgets`. Disclosed in beat_sheet.json
metadata.note.

## Disclosed deviations

1. **Voice/branding** — af_bella (Kokoro) + @HumanitariansAI, per the user's
   request for the most natural-sounding female voice.
2. **Self-intro** — "Hi, I'm Agrima" lives in its own B00B beat (ai-explainer
   convention); B00B also serves as the one-breath executive summary.
3. **Register** — personal, warm, neutral per the user's request, not the
   default Teardown register.
4. **Pipeline** — run.sh / compile.py / static_scene_check.py /
   manim_layout_audit.py / final_frame_check.py, as on every reel this session.

## PROOF GATE

All 12 beats classify SHOW (each names its on-screen artifact in
`visual_intent`). Arc: framework ✓ (B01–B03) · worked example/evidence ✓
(B04–B06) · falsifiability/caution ✓ (B07) · scaffolded viewer task ✓ (B09) ·
four bookends ✓ · no-source-no-verdict ✓ (every figure traced in FACTCHECK.md;
the cost comparison is hedged and flagged "one summary reports").

## GATE A / GATE B (before any pipeline run)

GATE A: zero ERROR; B00B WARN (text-only, expected). GATE B: all nine scenes
CLEAN after fixes. Fixes found by looking at rendered preview frames, not by
the gates alone:

- **B05**: the phone caption ("a math tutor on WhatsApp") ran underneath the
  first fact chip and was clipped; the "Ghana" label touched the map frame's
  border (GATE B flagged a label-on-line). Re-laid out: two-line caption, phone
  shifted left, chips narrowed, label moved inside the map, graticule removed.
- **B02**: the 16-dot card's contents touched the card's top and bottom edges;
  both cards were made taller.
- **B08**: first layout had the adult floating above the ground line, desk legs
  piercing it, and a stray diagonal line; rebuilt from a shared ground line
  with feet on the ground and one outline around the child, laptop and adult.
- Reveal pattern: cards grow first, then their contents fade in (no content
  hanging past a growing box).

## Duration

~715 narration words at ~3.0 words/second → ~238s estimated against the
exact-4:00 target; the measured mp3 total is the true figure and is reported
at delivery.
