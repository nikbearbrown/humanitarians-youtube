# SHOTLIST — weekly-recap-never-forgets (16:9, native 4K)

## Composer / outro beats — Claude-skin Remotion

B00 · ClaudeComposerAsk — cold open, self-intro folded in ("Hi, I'm Agrima."),
      per cli-explainer's own convention
B02 · ClaudeComposerAsk — the ask: write weekly_recap_v1.py
B03 · ClaudeCodeBeat — the REAL v1 code, sparkline "One list, three lines."
B05 · ClaudeComposerAsk — the change: revise v1 -> v2, tag + count
B06 · ClaudeCodeBeat — the REAL v2 code, sparkline "Same list, now counted."
B09 · ClaudeComposerAsk — HANDOFF LAW, viewer's own recap prompt
B10 · ClaudeTitleOutro — restates the series title

## Manim GRAPHIC beats — scenes.py

B01 · B01_NotAHighlightReel — typographic card, generic framing
B04 · B04_FlatWeek — three same-weight cards:
        - mock article header ("The AI That Never Forgets" — browser dots,
          kicker, headline, byline) — the requested article-header visual
        - two-by-two video-grid card (four mini play-icon frames,
          "16:9 + 9:16") — the requested four-videos visual
        - meeting/calendar-icon card ("Team Meeting" / "attended") — the
          requested meeting/calendar visual
B07 · B07_TaggedWeek — same three cards, each now carrying a category tag
        chip (Writing / Video / Meetings), under a "This week: 3 things
        shipped" header
B08 · B08_TheLesson — typographic closing beat

## Notes

- No stock footage or screen recording used — every visual is generated
  fresh in Manim, per the user's explicit request. If more literal proof is
  wanted later, a real screenshot of the published Substack article, a
  short screen recording of an actual Brutalist build session, or a photo
  from the team meeting could replace the article-header, video-grid, or
  meeting-icon card respectively — none is required for this build.
- This week has no upcoming/next-week item (unlike the prior weekly-recap
  builds), so the v1->v2 revision is a flat-list-to-tagged-and-counted
  change, not a DONE/NEXT split — a different but equally real code change.
- Audio-first: all 11 mp3s generated via Kokoro (af_bella) before any
  rendering; durations below are the measured ground truth.
- Rendered via this toolkit's own run.sh/compile.py/static_scene_check.py/
  manim_layout_audit.py/final_frame_check.py pipeline.
- 16:9 native 4K (3840x2160, default HEIGHT=2160 already yields this for
  landscape); 9:16 cut uses --height 3840 explicitly. Total (~97s) is well
  under the 3:00 Shorts cap, so the 9:16 cut should be a full-parity
  reformat with no beats dropped.
