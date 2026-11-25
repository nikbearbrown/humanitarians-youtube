# CHECKS-REPORT — chatbot-brand-check

## Chassis

User asked for a "Deep Explainer" at exactly 4:00 with no footage. The toolkit's
`deep-explainer` skill targets 5–10 minutes and requires ~20–25% pantry/archival
stills — both conflict. Built on the `ai-explainer` chassis (cold open →
presenter intro → body → sources note → handoff → outro), matching
`ai-colleague-quota`, `hotel-phone-helper`, `ai-done-right` and
`tutor-they-never-had`. Disclosed in beat_sheet.json metadata.note.

## Disclosed deviations

1. **Voice/branding** — af_bella (Kokoro) + @HumanitariansAI, per the user's
   request for the most natural-sounding female voice.
2. **Self-intro** — "Hi, I'm Agrima" lives in its own B00B beat (ai-explainer
   convention), which also serves as the one-breath summary.
3. **Register** — warm, simple, friendly, positive but fair, per the user's
   request, not the default Teardown register.
4. **Pipeline** — run.sh / compile.py / static_scene_check.py /
   manim_layout_audit.py / final_frame_check.py, as on every reel this session.
5. **Numbers on screen** — the user's tip allows keeping only 900 million, "3 in
   4 brands", 95% and the five steps on screen. All the article's figures were
   kept, spread over six stat scenes (B02, B03, B04, B06, B07 and the B05 side
   card) so no scene carries more than three headline numbers; each is labeled
   with its source and the whole set is labeled industry-reported.
6. **Narration trims** — the narration was shortened from a 255 s first pass to
   239.3 s to land on 4:00 (dropped examples such as "like visiting the website or
   reading reviews", which stay on the B07 card; rounded 1,704 / 32,556 / 3,848 in
   speech, exact numbers on screen). See FACTCHECK.md.

## PROOF GATE

All 14 beats classify SHOW (each names its on-screen artifact in
`visual_intent`). Arc: framework ✓ (B02, B05) · worked example ✓ (B01 bakery,
labeled illustration) · evidence ✓ (B02–B07, each sourced and labeled
industry-reported) · falsifiability/caution ✓ (B04 two numbers, B10 note) ·
scaffolded viewer task ✓ (B08 checklist, B11 prompt) · four bookends ✓ ·
no-source-no-verdict ✓ (every figure traced in FACTCHECK.md).

## GATE A / GATE B (before any pipeline run)

GATE A: zero ERROR; B00B WARN (text-only, expected) and B08 WARN (many distinct
animations, expected for a timed checklist). GATE B: all eleven scenes CLEAN. A
first pass found three problems fixed before rendering: a `NameError` in B08, the
B08 question chips running past the safe area (chip widths tightened), and a `$`
label sitting on a line in B05 (doc icon redrawn without lines). Preview frames of
all ten body scenes were viewed; no shape or text overflow found.
