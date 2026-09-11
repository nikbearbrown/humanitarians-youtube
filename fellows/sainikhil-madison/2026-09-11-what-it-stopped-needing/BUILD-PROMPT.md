# BUILD-PROMPT — claude-sai-what-it-stopped-needing

Paste-ready. Run every command from the toolkit root
(`/Users/nikhilkunapareddy/Documents/brutalist.art`).

```bash
REEL=weekly_updates/09-11-2

# STEP 0 — the B02 plate. Already built, but this regenerates it after any edit.
#          ANACONDA python3: it has Pillow, the .venv does not.
python3 $REEL/make_plates.py

# STEP 1 — GATE P (human). Open $REEL/PEDAGOGY.md, review the narration, and
#          replace the VERDICT line's blank with the word that means approved.
#          Audio refuses to run until that line is signed. Claude must not sign it.

# STEP 2 — narration audio, the master clock. Free, local, ~30s.
#          .venv/bin/python — the default python3 is Anaconda and has no kokoro_onnx.
.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL

# STEP 3 — render the beats (true 4K; renders at --scale=2). A few minutes.
python3 runtime/scripts/remotion_scenes.py $REEL

# STEP 4 — compile the 4K master + visual QC.
./art run $REEL
#   → $REEL/claude-sai-what-it-stopped-needing.mp4          (clean 4K master)
#   → $REEL/claude-sai-what-it-stopped-needing-slate.mp4    (labelled review cut)
#   → $REEL/_qc/                                            (frames + REPORT.md — LOOK at these)

# Fast 1080 preview first (optional):
./art run $REEL --height 1080

# STEP 5 — the 9:16 short, derived from the finished long. NOT a crop.
python3 runtime/scripts/shorts.py $REEL
./art run $REEL/short --height 3840     # 4K vertical is 2160x3840; the printed hint says 1920, which is 1080p
```

## Expected, not errors

- **`SKIN LINT: B08 … OUTRO LAW wants ClaudeTitleOutro`** — wrong for this
  channel. `ClaudeTitleOutro` hardcodes `@NikBearBrown`; this series is
  `@HumanitariansAI`, so B08 is `LogoOutro`. Ignore it.
- **`./art doctor` reporting audio blocked** — a false negative. It checks the
  Anaconda `python3`, which has no `kokoro_onnx`. `.venv/bin/python` does.
- **GATE V underfill on the B02 stills** — the plates measure 85% horizontal ink
  (landscape) and 80% vertical (portrait). Look at the frames before changing
  anything.

## After edits

Change `narration_text` → re-run STEP 2 → STEP 3 with `--force` → STEP 4.
Never hand-edit a duration; audio is the clock.
