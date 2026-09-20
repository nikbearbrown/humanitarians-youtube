# SHOTLIST — weekly-recap-suffolk (16:9, native 4K)

## Composer / outro beats — Claude-skin Remotion

B00 · ClaudeComposerAsk — cold open, self-intro folded in ("Hi, I'm Agrima."),
      per cli-explainer's own convention (not split into a B00B beat — that's
      the ai-explainer-chassis convention, a different skill)
B02 · ClaudeComposerAsk — the ask: write weekly_recap_v1.py
B03 · ClaudeCodeBeat — the REAL v1 code + its real terminal output as sparkline
B05 · ClaudeComposerAsk — the change: revise v1 -> v2 (split DONE/NEXT)
B06 · ClaudeCodeBeat — the REAL v2 code
B09 · ClaudeComposerAsk — HANDOFF LAW, viewer's own recap prompt
B10 · ClaudeTitleOutro — restates the series title

## Manim GRAPHIC beats — scenes.py

B01 · B01_NotAHighlightReel — typographic card, generic framing
B04 · B04_FlatWeek — three same-weight cards:
        - mock article header ("No Face, No Problem" — browser dots,
          kicker, headline, byline) — the requested article-header visual
        - two-by-two video-grid card (four mini play-icon frames,
          "16:9 + 9:16") — the requested four-videos visual
        - Suffolk-lecture card (presentation-slide + podium icon,
          "lecture · with Yatra") — the requested calendar/podium/slide
          visual
B07 · B07_SplitWeek — same three cards, regrouped under DONE THIS WEEK
        (article + four-videos) vs STARTING NEXT WEEK (Suffolk lecture),
        divider line
B08 · B08_TheLesson — typographic closing beat

## Notes

- No stock footage or screen recording used — every visual is generated
  fresh in Manim, per the user's explicit request. If more literal proof is
  wanted later, a real screenshot of the published Substack article, a
  short screen recording of an actual Brutalist terminal session, or the
  actual presentation draft could replace the article-header, video-grid,
  or Suffolk-lecture card respectively — none is required for this build.
- Audio-first: all 11 mp3s generated via Kokoro (af_bella) before any
  rendering; durations below are the measured ground truth.
- Rendered via this toolkit's own run.sh/compile.py/static_scene_check.py/
  manim_layout_audit.py/final_frame_check.py pipeline — the cli-explainer
  skill's documented vox_run.sh/vox_compile.py/type_check.py do not exist
  anywhere in this install (re-verified for this build).
- 16:9 native 4K (3840x2160, default HEIGHT=2160 already yields this for
  landscape); 9:16 cut uses --height 3840 explicitly, per this session's
  established true-4K-vertical fix.
