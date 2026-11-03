# SHOTLIST — ai-that-never-forgets (16:9, native 4K)

## Composer / outro beats — Claude-skin Remotion

B00 · ClaudeComposerAsk — cold open, ask shown answered, no self-intro here
      (see B00B)
B07 · ClaudeComposerAsk — HANDOFF LAW, viewer's own memory-check prompt
B08 · ClaudeTitleOutro — restates the series title

## Manim GRAPHIC beats — scenes.py

B00B · B00B_AgrimaIntro     — presenter card: "Hi, I'm Agrima." + topic lead-in
                              (doubles as the executive-summary beat)
B01  · B01_TheOldSystem     — you -> cookie -> three site cards, the same
                              shoe icon following across each (retargeting)
B02  · B02_WhatsChanging    — old-vs-new split card (guesses from clicks /
                              remembers what you said), Gemini + ChatGPT
                              chips, market-size stat line
B03  · B03_WhyItMatters     — three conversation fragments (half marathon /
                              flat feet / tight budget) assembling into one
                              assistant-profile card, productivity stat line
B04  · B04_TheOtherSide     — personalization-model vs identity-model
                              comparison card, three open-question chips
                              (who sees it / corrected / deleted)
B05  · B05_ResponsibleTools — a Memory settings panel: View / Edit / Clear,
                              clearly visible, not hidden in menus
B06  · B06_ClosingFraming   — quiet typographic closing beat: the tradeoff,
                              not a verdict

## Notes

- No stock footage, screen recording, or screenshots — every visual is
  generated fresh in Manim, per the user's explicit materials note that no
  dedicated footage exists for this topic. If the user later wants a screen
  recording of an actual AI assistant's memory settings (e.g. ChatGPT's
  "Manage Memories" panel, or Gemini's "Personal context" settings), that
  could replace B05's generated settings-panel card directly — no other beat
  needs it.
- Audio-first: all 9 mp3s generated via Kokoro (af_bella) before any
  rendering; durations below are the measured ground truth.
- Rendered via this toolkit's own run.sh/compile.py/static_scene_check.py/
  manim_layout_audit.py/final_frame_check.py pipeline — the ai-explainer
  chassis substitution (see beat_sheet.json metadata.note) means this build
  never touches deep-explainer's pantry/shopping-list machinery.
- 16:9 native 4K (3840x2160, default HEIGHT=2160 already yields this for
  landscape); 9:16 cut uses --height 3840 explicitly, per this session's
  established true-4K-vertical fix.
