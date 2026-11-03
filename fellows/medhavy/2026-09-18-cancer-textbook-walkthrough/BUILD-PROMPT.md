# BUILD-PROMPT.md — claude-liam-medhavy-cancer-textbook-walkthrough

Paste into Claude Code from `books/`:

```
medhavy-walkthrough "Cancer textbook" /Users/bear/Documents/CoWork/bear-textbooks/books/medhavi-hub
```

Steps (all from `brutalist.art/`, REEL = this folder):

1. `python3 skills/make/medhavy-walkthrough/scripts/save_session.py` — human signs in once.
2. `python3 skills/make/medhavy-walkthrough/scripts/capture_admin.py REEL --run run-signin --plan REEL/capture/plan-signin.json --css-size 1600x900 --dpr 2.4 --no-session`
3. `python3 skills/make/medhavy-walkthrough/scripts/capture_admin.py REEL --run run-book --plan REEL/capture/plan-book.json --css-size 1600x900 --dpr 2.4` (records the hub tab and the book tab as `run-book.mp4` + `run-book-p2.mp4`; page-two offset = total − p2 duration).
4. Author `beat_sheet.json` (book beats use `source_capture: run-book-p2` with page-two seconds), `coverage.json`.
5. `python3 runtime/scripts/generate_audio_kokoro.py REEL`
6. `python3 skills/make/medhavy-walkthrough/scripts/prepare_media.py REEL`
7. `python3 runtime/scripts/remotion_scenes.py REEL`
8. `./art medhavy-walkthrough --check REEL`
9. `python3 runtime/scripts/compile.py REEL --review --fps 30 --height 2160` then `python3 runtime/qc/final_frame_check.py REEL --mp4 REEL/<slug>-slate.mp4` (declare `qc.contrast_regions` for the landing, Clerk cards, and the search dialog).
10. Limit every per-beat track to −1.5 dBTP into `audio/<id>-lim.wav`; `./art final REEL --height 2160 --fps 30 --out REEL/exports/landscape`; `runtime/scripts/loudness_check.py REEL --mp4 …`.
11. `python3 skills/make/medhavy-walkthrough/scripts/build_srt_and_description.py REEL --to books/youtube/TOPOST --chapters "B00=Intro,…"`; `python3 runtime/scripts/post.py REEL --no-topaz`; re-run the builder so TOPOST carries the full SRT and chaptered description.

For another book: change the `open_textbook` name in `plan-book.json`, the chapter button/link names, and the four questions; everything else is reusable.
