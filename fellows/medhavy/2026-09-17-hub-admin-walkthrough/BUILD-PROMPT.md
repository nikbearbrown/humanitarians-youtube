# BUILD-PROMPT.md — claude-liam-medhavy-hub-walkthrough

Paste into Claude Code from `books/` to rebuild or extend this reel.

```
medhavy-walkthrough textbook /Users/bear/Documents/CoWork/bear-textbooks/books/medhavi-hub
```

Then, in order:

1. Session: `python3 brutalist.art/skills/make/medhavy-walkthrough/scripts/save_session.py` (human signs in; nothing typed by Claude).
2. Capture: `python3 brutalist.art/skills/make/medhavy-walkthrough/scripts/capture_admin.py REEL --run run-05 --plan REEL/capture/plan-run-05.json --css-size 1600x900 --dpr 2.4`
3. Author `beat_sheet.json` (textbook bookends + one FOOTAGE beat per tab with `source_capture` and `source_seconds`), `coverage.json`, `CAPTURE.md`.
4. Audio: `python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py REEL`
5. Clips + pads + jingle: `python3 brutalist.art/skills/make/medhavy-walkthrough/scripts/prepare_media.py REEL`
6. Bookends: `python3 brutalist.art/runtime/scripts/remotion_scenes.py REEL`
7. Gate: `./brutalist.art/art medhavy-walkthrough --check REEL`
8. Loudness: alimiter every per-beat track to `audio/<id>-lim.wav` (limit 0.841) and point `audio_file` at them; `runtime/scripts/loudness_check.py REEL` must PASS.
9. Captions + description: `python3 brutalist.art/skills/make/medhavy-walkthrough/scripts/build_srt_and_description.py REEL --to books/youtube/TOPOST --chapters "B00=Intro,..."`
10. Stage: `python3 brutalist.art/runtime/scripts/post.py REEL --no-topaz`, then re-run step 9 so TOPOST carries the full-text SRT and chaptered description.
8a. Review cut: `./brutalist.art/art run REEL` — inspect frames, then `./brutalist.art/art final REEL --height 2160 --fps 30 --out REEL/exports/landscape`

Rules that bit during the first build: the mask must install after `document.body` exists; the replacement address must not itself match the email regex (infinite loop); analytics tab buttons carry a count so exact-name matching fails; a leaked capture is deleted, not blurred later.

Never publish from here. Staging is `art post`; upload only from `books/youtube/TOPOST/`.
