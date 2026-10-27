# README-RUN-THIS — hai-repo-sensei-v2

Built against brutalist.art at `4115560`.

```bash
cd <path-to>/brutalist.art
source .venv/bin/activate
python3 runtime/scripts/generate_audio_kokoro.py <reel-dir>   # narration is the clock
./art run <reel-dir>                                          # render + GATE L/V
./art final <reel-dir>                                        # GATE T, then the master
```

## Manim

This reel's figures are authored in `scenes.py`, one `Scene` class per beat — the class
name's prefix is the beat id (`B06_Pipeline` fills beat `B06`). `run.sh` discovers them by
regex, so each class must inherit `Scene` directly.

**A scene must match its beat's length.** The compiler stretches a short scene to fill its
beat, which slows every animation; build fast, then hold. Check with:

```bash
ffprobe -v error -show_entries format=duration -of csv=p=0 manim/<BID>.mp4
```

`manim` must be importable inside the toolkit venv, not only on PATH — GATE B imports it.

## Gate T is not optional and not silent

`./art final` prints `GATE T skipped — missing deps (pip install pillow numpy scipy)` and
exits zero when those are missing. A skipped gate is not a passing gate. The checker also
needs Python 3.10+, so run it from the venv rather than the system interpreter.

## Vertical

```bash
./art vertical <reel-dir>
python3 runtime/scripts/compile.py <reel-dir>/vertical --height 3840
```

Portrait is its own design, not a crop, and carries its own GATE T run. Do not run
`art final` after the 3840 compile — it can re-encode the master at a lower resolution.
