# CHECKS-REPORT — foundation-search-research

## Chassis

User asked for a "Deep Explainer" at exactly 4:00 with no footage. The toolkit's
`deep-explainer` skill targets 5–10 minutes and requires ~20–25% pantry/archival
stills — both conflict. Built on the `ai-explainer` chassis (cold open → presenter
intro → body → sources note → handoff → outro), matching `chatbot-brand-check`,
`ai-colleague-quota`, `hotel-phone-helper` and `ai-done-right`. Disclosed in
beat_sheet.json metadata.note.

## Disclosed deviations

1. **Voice/branding** — af_bella (Kokoro) + @HumanitariansAI, per the user's
   request for the most natural-sounding female voice.
2. **Self-intro** — "Hi, I'm Agrima" lives in its own B00B beat (ai-explainer
   convention), which also serves as the one-breath summary.
3. **Register** — warm, simple, friendly, positive but fair, per the user's
   request, not the default Teardown register.
4. **Pipeline** — run.sh / compile.py / static_scene_check.py /
   manim_layout_audit.py / final_frame_check.py, as on every reel this session.
5. **Numbers on screen** — the user's tip allows keeping only "over 90%", "20%+" and
   "about 7 in 10" on screen if crowded. Those three are the only headline figures in
   the article, so all of them were kept; none of the scenes is crowded (B04 carries
   two, B07 one), each is labeled with its source, and the cosnova pair is badged
   company-reported.
6. **Narration trims** — the narration was shortened from a 262 s first pass to
   239.9 s to land on 4:00 (connective phrases and repeated lead-ins only; no figure,
   source, hedge or label removed). "tens of thousands" and the percentages are
   spoken as written. See FACTCHECK.md.
7. **Faces and logos** — the user asked for illustrated faces and no real logos or
   photos: the face is an abstract outline with swatch strips; the shopper and team
   are plain figures; source names appear only as plain text.

## PROOF GATE

All 13 beats classify SHOW (each Manim beat names its on-screen artifact in
`visual_intent`; composer/outro beats carry their prompts). Arc: framework ✓ (B02,
B03) · worked example ✓ (B01 late-night try-on; B05 deep-shade gap, both labeled
illustrations) · evidence ✓ (B04 cosnova, B07 PwC; each sourced and labeled) ·
falsifiability/caution ✓ (B04 company-reported, B05 narrow data, B07 privacy, B09
sources note) · scaffolded viewer task ✓ (B10) · four bookends ✓ ·
no-source-no-verdict ✓ (every claim traced in FACTCHECK.md).

## GATE A / GATE B (before any pipeline run)

GATE A: zero ERROR; B00B WARN (text-only, expected). GATE B: all ten scenes CLEAN
after two fixes found by the gates: in B01 the "new text" bubble overlapped the
phone's face outline (moved into the tab's place); in B06 the "PwC Malaysia" source
chip overlapped the "trim the long tail" label (moved under the shelf). Preview
frames of all ten scenes were viewed; one clarity fix (a "yours" marker with its own
ring in B06) came from looking at them.
