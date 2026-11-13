# CHECKS-REPORT — real-art-new-light

## Chassis

User asked for a "Deep Explainer" at exactly 4:00 with no footage. The toolkit's
`deep-explainer` skill targets 5–10 minutes and requires ~20–25% pantry/archival
stills — both conflict, and the user also asked for no real artworks or likenesses.
Built on the `ai-explainer` chassis (cold open → presenter intro → body → sources note →
handoff → outro), matching `foundation-search-research`, `chatbot-brand-check` and
`ai-colleague-quota`. Disclosed in beat_sheet.json metadata.note.

## Disclosed deviations

1. **Voice/branding** — af_bella (Kokoro) + @HumanitariansAI, per the user's request
   for the most natural-sounding female voice.
2. **Self-intro** — "Hi, I'm Agrima" lives in its own B00B beat (ai-explainer
   convention), which also serves as the one-breath summary.
3. **Register** — warm, simple, friendly; thoughtful and fair, with respect for the
   artworks, per the user's request, not the default Teardown register.
4. **Coverage** — per the user's instruction, Rembrandt/Rijksmuseum, the Dalí Museum
   and MoMA are covered in full; Harvard and Koblenz get one sentence each (B06); the
   habits (B02) and the borrowable ideas (B07) are short. The user's "about 25 seconds
   per example" is met for the Dalí beat (27 s) and approximated for the other two
   (Night Watch 32 s, MoMA 31 s), because the total had to land on exactly 4:00 with
   the three covered examples, the habits, the ideas and the closing.
5. **Pipeline** — run.sh / compile.py / static_scene_check.py /
   manim_layout_audit.py / final_frame_check.py, as on every reel this session.
6. **Numbers on screen** — "24 x 24 ft", "320,000" and "team of 15" are all kept on
   stat cards (the user's tip allows trimming to the headline numbers if crowded; B05
   was not crowded), each with its source chip.
7. **No real artwork or likeness** — every painting, frame, wall and portrait is a
   generic abstract graphic with a "generic / generated / not the real work" caption
   where a real work is named; the Dalí figure is a faceless silhouette; no museum or
   company logos.
8. **Narration trims** — first pass 234.3 s; two accurate details added and two phrases
   tightened to reach 239.7 s. See FACTCHECK.md.

## PROOF GATE

All 13 beats classify SHOW (each Manim beat names its on-screen artifact in
`visual_intent`; composer/outro beats carry their prompts). Arc: framework ✓ (B02 the
three habits) · worked examples ✓ (B03–B05, one per example, each sourced; B06 two
brief ones) · falsifiability/caution ✓ (B03 wire report, B04 controversy and 2019, B05
undated source, B09 sources note, B01/B07 illustration and suggestion labels) ·
scaffolded viewer task ✓ (B10) · four bookends ✓ · no-source-no-verdict ✓ (every
claim traced in FACTCHECK.md).

## GATE A / GATE B (before any pipeline run)

GATE A: zero ERROR; B00B and B09 WARN (text-only, expected). GATE B: all ten scenes
CLEAN after fixes found by the gates and by viewing preview frames: B01 closing line
below the safe area (moved up), B02 first row layout (rebuilt with explicit
positions), B06 the AI guide icon over a painting frame (moved), B07 title past the
left edge and a 'shapes never change' error (title shrunk; rows fade in as built
cards), then by eye: B01's brushstrokes ran outside their screen (scaled to fit), B02's
third row ran into its AI/real tags (text narrowed), B05's wall showed blank because its
colour blobs were hidden (now fade in with the wall) and its captions overlapped.
