# SHOTLIST — weekly-recap-never-forgets (short, 9:16, true 4K vertical)

Full-parity reformat — the parent (1:30) is well under the 3:00 Shorts cap,
so all 11 beats are kept, plus a silent branded end card.

## Composer / code / outro beats — Claude-skin Remotion (916 compositions)

B00 · ClaudeComposerAsk916 — cold open, self-intro folded in
B02 · ClaudeComposerAsk916 — the ask: write weekly_recap_v1.py
B03 · ClaudeCodeBeat916 — the REAL v1 code, sparkline "One list, three lines."
B05 · ClaudeComposerAsk916 — the change: revise v1 -> v2, tag + count
B06 · ClaudeCodeBeat916 — the REAL v2 code, sparkline "Same list, now counted."
B09 · ClaudeComposerAsk916 — HANDOFF LAW, viewer's own recap prompt
B10 · ClaudeTitleOutro916 — restates the series title

## Manim GRAPHIC beats — short/scenes.py (portrait ports of the parent scenes)

B01 · B01_NotAHighlightReel — typographic card, generic framing
B04 · B04_FlatWeek — three same-weight cards, stacked vertically:
        article header / four-video grid / meeting-calendar icon
B07 · B07_TaggedWeek — same three cards, stacked, now tagged by category
        (Writing / Video / Meetings) with a shipped-count header
B08 · B08_TheLesson — typographic closing beat

END · silent branded end card (4.5s)

## Notes

- No stock footage — every visual is a portrait port of the parent's
  generated Manim graphics, restacked vertically for the 9:16 safe area
  (portrait audit: safe_w≈1.95, safe_h≈3.4 for a 4.5x8 frame).
- Audio-first: all 11 mp3s reused verbatim from the parent cut (full
  parity — same narration, same timing); only the silent END card's mp3 is
  new.
- Rendered via this toolkit's own run.sh/compile.py/static_scene_check.py/
  manim_layout_audit.py/final_frame_check.py pipeline, at --height 3840 for
  true 4K vertical.
- Endcard font: this machine's `find_serif()` Windows gap recurs on every
  build — short/media/END.png was proactively regenerated with Georgia at
  true 2160x3840 (128pt handle), correct handle (@HumanitariansAI), before
  compiling, per this session's established fix.
