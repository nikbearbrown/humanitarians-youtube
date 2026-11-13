# SHOTLIST — ai-that-never-forgets (short, 9:16, true 4K vertical)

Auto-plan dropped B02 ("what's changing" — Gemini/ChatGPT/market stat) and
B04 ("the other side" — identity-model framing) to fit the 3:00 Shorts cap.
9 beats kept + a silent branded end card.

## Composer / outro beats — Claude-skin Remotion (916 compositions)

B00 · ClaudeComposerAsk916 — cold open, ask shown answered
B07 · ClaudeComposerAsk916 — HANDOFF LAW, viewer's own memory-check prompt
B08 · ClaudeTitleOutro916 — restates the series title; narration rewritten
      (see below) since the auto-generated outro was a broken sentence
      fragment stitched from the two dropped beats' opening words

## Manim GRAPHIC beats — short/scenes.py (portrait ports of the parent scenes)

B00B · B00B_AgrimaIntro     — presenter card: "Hi, I'm Agrima." + topic lead-in
B01  · B01_TheOldSystem     — you -> cookie -> three site cards (retargeting)
B03  · B03_WhyItMatters     — three conversation fragments assembling into
                              one assistant-profile card, productivity stat
B05  · B05_ResponsibleTools — Memory settings panel: View / Edit / Clear
B06  · B06_ClosingFraming   — quiet typographic closing beat: the tradeoff

END · silent branded end card (4.5s)

## Notes

- No stock footage — every visual is a portrait port of the parent's
  generated Manim graphics, re-laid-out for the 9:16 safe area
  (portrait audit: safe_w≈1.95, safe_h≈3.4 for a 4.5x8 frame).
- The outro (B08) was rewritten from the auto-stitched fragment to a
  coherent sentence pointing viewers to the full video for "the specific
  tools, the market size, and the privacy side" — see FACTCHECK.md.
- Audio-first: all mp3s except the rewritten B08 are reused verbatim from
  the parent cut (full-parity beats keep their original narration and
  timing); only B08's mp3 needs regenerating.
- Rendered via this toolkit's own run.sh/compile.py/static_scene_check.py/
  manim_layout_audit.py/final_frame_check.py pipeline, at --height 3840 for
  true 4K vertical (not the default 1920), per this session's established
  fix for the true-4K-vertical requirement.
- Endcard font: this machine's `find_serif()` Windows gap recurs on every
  build — short/media/END.png needs manual regeneration with Georgia at
  true 2160x3840 resolution (128pt handle / 88pt tease) before final QC.
