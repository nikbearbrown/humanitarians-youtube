# README-RUN-THIS — hai-brutalist-week-2

Built against brutalist.art at `4115560`.

```bash
cd <path-to>/brutalist.art
source .venv/bin/activate
python3 runtime/scripts/generate_audio_kokoro.py <reel-dir>   # narration is the clock
./art run <reel-dir>                                          # render + GATE L/V
./art final <reel-dir>                                        # GATE T, then the master
```

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
