# SHOTLIST — no-face-no-problem (16:9, native 4K)

## Composer / outro beats — Claude-skin Remotion

B00 · ClaudeComposerAsk — cold open, plain ask-focused hook (self-intro
      lives in its own B00B beat, per this user's ai-explainer-chassis
      precedent, not folded into B00's narration)
B08 · ClaudeComposerAsk — HANDOFF LAW, viewer's own fact-check prompt
B09 · ClaudeTitleOutro — restates the episode title + source-count note

## Manim GRAPHIC beats — scenes.py

B00B · B00B_AgrimaIntro — presenter card ("Hi, I'm Agrima." + lead-in)
B01   · B01_TheHook — DELIBERATELY not a composer/host card: an abstract
        stock-footage frame (skyline / wave / flame motifs) labeled STOCK
        FOOTAGE, with a bold TikTok-style caption overlaid and a
        "no face · no name" tag — this performs the article's own subject
        rather than illustrating it from the outside, per the user's
        explicit materials note
B02   · B02_TheStrategy — five-node flow (Topic -> Script -> AI Voice ->
        Stock Footage -> Post) with connecting arrows and a crossed-out
        camera icon
B03   · B03_TheVoiceGap — before/after AI-voice comparison card (jagged
        "GPS voice" waveform + real-cost tag vs. smoother "passes as
        human" waveform + $-per-minute tag), arrow between them, footer
        note on the detection arms race
B04   · B04_WhereItPays — five-card niche grid (Personal Finance, Tech &
        AI News, True Crime, Psychology, Self-Improvement) + ad-rate tag
B05   · B05_TrustFinding — large stat card ("more trustworthy, not less.")
        with an EXPLICIT on-screen skepticism flag (red-bordered,
        "sourced from AI-tool vendors — take with skepticism") — not just
        a spoken caveat
B06   · B06_TheReframe — a WATCH TIME meter filling, tags for
        completion/saves/shares, and a crossed-out face icon
B07   · B07_ClosingQuestion — quiet typographic closing beat, no diagram,
        ending on the article's own open question

## Notes

- No stock footage or screen recording used — every visual is generated
  fresh in Manim/Remotion, per the user's explicit request. The
  skyline/wave/flame motifs in B01 are abstract geometric stand-ins for
  the kind of stock footage faceless accounts actually use, not literal
  footage.
- Audio-first: all 11 mp3s generated via Kokoro (af_bella) before any
  rendering; durations are the measured ground truth.
- Rendered via this toolkit's run.sh/compile.py/static_scene_check.py/
  manim_layout_audit.py/final_frame_check.py pipeline (the deep-explainer
  skill's own two-gate pantry-sourcing pipeline doesn't fit a no-footage,
  fixed-duration build — see CHECKS-REPORT.md for the full chassis
  disclosure).
- 16:9 native 4K (3840x2160, default HEIGHT=2160 already yields this for
  landscape); the 9:16 cut will use --height 3840 explicitly, per this
  session's established true-4K-vertical fix.
