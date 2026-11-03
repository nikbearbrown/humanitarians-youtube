# BUILD-PROMPT — `hussain-jboss-migrator-overview` · "Prove Nothing Broke."

Builds both 4K masters (16:9 and full-length native 9:16). Never publishes.

```bash
cd C:/Users/Hussain/Desktop/Project/Brutalist/Brut/brutalist.art
export PATH="$PWD/venv/Scripts:$PATH" ART_HOME="$PWD" PYTHONUTF8=1 PYTHONIOENCODING=utf-8 ART_CONCURRENCY=8
REEL=../jboss-migrator-videos/youtube/hussain-jboss-migrator-overview
```

1. Audio (only if narration changed): `python runtime/scripts/generate_audio_kokoro.py $REEL`
2. Pin compositions to audio: `python $REEL/sync_durations.py $REEL`
3. 16:9 beats: `python runtime/scripts/remotion_scenes.py $REEL`
4. 16:9 master: `python runtime/scripts/compile.py $REEL --height 2160`
5. Vertical: `./art vertical $REEL`, `python $REEL/sync_durations.py $REEL/vertical`,
   `python runtime/scripts/remotion_scenes.py $REEL/vertical`,
   `python runtime/scripts/compile.py $REEL/vertical --height 3840`
6. VISUAL QC: read frames at ~15/50/85% of each beat in both aspects; fix in
   `runtime/remotion/src/scenes/JbossMigratorIllus.tsx` and re-render (`--only Bxx --force`).
7. Report in `QC-STATUS.md`.

Run the two aspect passes sequentially, never in parallel.
