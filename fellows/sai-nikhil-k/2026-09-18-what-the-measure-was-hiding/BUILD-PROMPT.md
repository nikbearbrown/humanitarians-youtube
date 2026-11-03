# BUILD-PROMPT — 09-18-2 · What the Measure Was Hiding

Paste-ready. Run every command from the toolkit root,
`/Users/nikhilkunapareddy/Documents/brutalist.art`.

```bash
REEL=weekly_updates/09-18-2

# STEP 1 — GATE P (human). Open $REEL/PEDAGOGY.md, read the full narration at
#          the bottom, work the review checklist, then sign the VERDICT line.
#          Claude must never sign it. Note: this stop is doctrine, not a machine
#          lock — the toolkit will happily generate audio on an unsigned reel.

# STEP 2 — narration audio (the master clock). Free, local, ~30s.
#          Use the venv python: the default python3 cannot see Kokoro.
.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL

# STEP 3 — render the nine beats at true 4K (--scale=2). A few minutes.
python3 runtime/scripts/remotion_scenes.py $REEL

# STEP 4 — compile the 4K master + visual QC.
./art run $REEL
#   → $REEL/claude-sai-what-the-measure-was-hiding.mp4        (clean 4K master)
#   → $REEL/claude-sai-what-the-measure-was-hiding-slate.mp4  (labelled review)
#   → $REEL/_qc/  — LOOK at these frames, do not trust the probe

# STEP 5 — the math QC pass that MATH-TYPESETTING.md requires. Inspect B02's
#          equation frames at each reveal and at 15/50/85%, in BOTH aspects.
#          Record the result in FACTCHECK.md and _qc/.

# STEP 6 — the 9:16 cut. 504 words lands near 2:35, under the 180s cap, so no
#          beat needs dropping. For the SAME film in portrait (no endcard, no
#          cap, every beat retained):
python3 runtime/scripts/shorts.py $REEL --vertical
./art run $REEL/vertical --height 3840
```

Faster 1080 preview while iterating: `./art run $REEL --height 1080`.

## If you change any wording

Audio is the clock. Never hand-edit a duration.

```bash
.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL
python3 runtime/scripts/remotion_scenes.py $REEL --force        # or --only B0X
./art run $REEL
```

If a render is killed mid-beat, delete the stray `_ext_*` file in `$REEL/media/`
before re-running, or that beat stays double-length and the next run skips it.

## Expected noise, not bugs

- SKIN LINT at B08 asking for `ClaudeTitleOutro` — wrong for this channel.
- `./art scenes --check` calling a `*916` sibling NOT RENDERABLE — stale index.
- `./art doctor` / `./setup` crashing with `declare: -A: invalid option` on
  stock macOS bash 3.2 — only the readiness table.
