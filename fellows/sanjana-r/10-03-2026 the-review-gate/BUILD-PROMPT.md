# BUILD-PROMPT — The Review Gate

Single paste-ready prompt to rebuild the final cut end to end (never publishes).
Run from the `brutalist.art-main` tree on this Windows box (see
brutalist-art-windows-pipeline: use `python3`, Windows abs paths, `PYTHONUTF8=1`,
no `--review`).

```
Rebuild "The Review Gate" (16:9 4K + 9:16 short) for @HumanitariansAI, first-person
Sanjana Rao, voice af_bella. Data = the Sep 16-30 window of her review tracker; every
number must match SOURCES.md / FACTCHECK.md — no fabrication.

REEL = "Humanitarians AI Brutalist files/the-review-gate"

1. python3 "$REEL/build_sheet.py"                         # author beat_sheet.json
2. PYTHONUTF8=1 python3 runtime/scripts/generate_audio_kokoro.py "$REEL"   # master clock
3. Render Manim scenes.py (T02_Gate,T04_Scoreboard,T05_Breakdown,T06_GreenPass,
   T07_FixLoop,T09_Outro) at -r 3840,2160 -> "$REEL/manim/<BID>.mp4"
4. PYTHONUTF8=1 python3 runtime/scripts/remotion_scenes.py "$REEL"         # composer beats
5. Re-stamp audio_file + actual_duration_s from mp3/ if build_sheet.py was re-run.
6. PYTHONUTF8=1 python3 runtime/scripts/compile.py "$REEL" --height 2160   # conform+mux
7. ffmpeg -y -i "$REEL/clips/_work/master.wav" -c:a aac "$REEL/clips/master.m4a"
8. python3 "$REEL/add_transitions.py" "$REEL" --fade 0.35 \
     --out "The-Review-Gate__16x9_4K_YouTube.mp4"
9. VISUAL QC: sample frames (ffmpeg fps=2 + 15/50/85% per beat), READ the PNGs, audit
   the 9-point rubric; fix scene source, re-render until zero BLOCKER/MAJOR.
10. Repeat 2-8 for the short folder (beat_sheet_short.json / scenes_short.py, render
    2160x3840) -> "The-Review-Gate__9x16_Short.mp4".

Do NOT push to GitHub. Leave outputs in "$REEL".
```
