# CHECKS-REPORT — we-ask-the-ai-now

## Chassis

User asked for a "Deep Explainer" at exactly 4:00 with no footage. The toolkit's
`deep-explainer` skill targets 5–10 minutes and requires ~20–25% pantry/archival
stills — both conflict. Built on the `ai-explainer` chassis (cold open → presenter
intro → body → sources note → handoff → outro), matching `real-art-new-light`,
`foundation-search-research` and `chatbot-brand-check`. Disclosed in
beat_sheet.json metadata.note.

## Disclosed deviations

1. **Voice/branding** — af_bella (Kokoro) + @HumanitariansAI, per the user's request
   for the most natural-sounding female voice.
2. **Self-intro** — "Hi, I'm Agrima" lives in its own B00B beat (ai-explainer
   convention), which also serves as the one-breath summary.
3. **Register** — warm, simple, friendly; fair and curious, per the user's request, not
   the default Teardown register.
4. **Pacing** — the brief asked for about 25–30 seconds per numbered part. Measured:
   opening 19.0, split 33.9, hand-over 34.7, answer on top 26.9, younger people 17.3,
   trust 20.5, being found 26.3, closing 21.5. The two number-heavy parts run a few
   seconds over, and the lighter ones (opening, younger people, trust, closing) run
   under, so that all eight parts, the sources note, the handoff and the outro land on
   exactly 4:00 (239.6 s).
5. **Numbers on screen** — every figure the user listed is kept, each on its own card
   with its source chip; the surveys are on separate cards and never merged (the user's
   "do not compare directly" rule). Where many cards share a beat (B02, B03, B04) they
   are split left and right by survey.
6. **Pipeline** — run.sh / compile.py / static_scene_check.py /
   manim_layout_audit.py / final_frame_check.py, as on every reel this session.
7. **No logos** — search and chat icons are generic; Google, Bain, Orbit Media and
   Future appear only as plain text.
8. **Narration trims** — 243.8 s first pass to 239.6 s; see FACTCHECK.md.

## PROOF GATE

All 13 beats classify SHOW (each Manim beat names its on-screen artifact in
`visual_intent`; composer/outro beats carry their prompts). Arc: framework ✓ (B02
split) · worked example ✓ (B01 trip illustration, B08 two example questions) ·
evidence ✓ (B02–B06, each figure sourced and labeled) · falsifiability/caution ✓ (B02
"Google use hasn't declined", B03 the local-search exception and the 2025 date, B04
"a study Orbit cites", B06 doubt, B09 sources note, B01/B07 labels) · scaffolded
viewer task ✓ (B10) · four bookends ✓ · no-source-no-verdict ✓ (every figure traced in
FACTCHECK.md).

## GATE A / GATE B (before any pipeline run)

GATE A: zero ERROR; B00B WARN (text-only, expected). GATE B: all ten scenes CLEAN after
fixes found by the gates and by viewing preview frames: B05's bar label ran into the
"older" arrow label (bars shortened, arrow moved); B07's title ran past the left edge;
by eye: B04's two closing chips overlapped and its caption sat on the page border, B03's
Future header touched its card, B06's gauge arcs were built from the wrong centre (so the
colored arc sat off the dial) with the 0 and 100 labels swapped, B06's title ran into its
source chip, and B09's references were scaled too small (re-broken into short lines).
