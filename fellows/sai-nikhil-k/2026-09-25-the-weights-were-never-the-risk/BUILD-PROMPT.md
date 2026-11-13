# BUILD-PROMPT — 2026-09-25-the-weights-were-never-the-risk · The Weights Were Never the Risk

Paste-ready. Run every command from the toolkit root,
`/Users/nikhilkunapareddy/Documents/brutalist.art`.

```bash
REEL=weekly_updates/2026-09-25-the-weights-were-never-the-risk
SLUG=claude-sai-the-weights-were-never-the-risk

# STEP 0 — the sheet is GENERATED. Edit build_beats.py, never beat_sheet.json:
#          it re-typesets B03's equations and re-times the B03/B04 reveals to
#          the measured audio. --check verifies algebra + string budgets only.
python3 $REEL/build_beats.py --check
python3 $REEL/build_beats.py && python3 $REEL/fill_narration.py

# STEP 1 — GATE P (human). Open $REEL/PEDAGOGY.md, read the full narration,
#          work the review checklist, then sign the VERDICT line.
#          Claude must never sign it. (Doctrine, not a machine lock.)

# STEP 2 — narration audio (the master clock). Free, local, ~30s.
#          The venv python: the default python3 cannot see Kokoro.
.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL
python3 $REEL/build_beats.py      # re-time reveals to the new durations

# STEP 3 — render the ten beats at true 4K, ONE BEAT PER CALL (a killed
#          multi-beat run leaves an unretimed clip the next run skips).
for b in B00 B01 B02 B03 B04 B05 B06 B07 B08 B09; do
  python3 runtime/scripts/remotion_scenes.py $REEL --only $b; done

# STEP 4 — review cut + GATE V (LOOK at _qc/), then the clean 4K 16:9 master.
#          ./art final writes to <toolkit>/renders/ unless --out is given.
./art run $REEL
./art final $REEL --out $REEL

# STEP 5 — the SAME film in 9:16 (every beat, no cap, no endcard), 4K portrait.
python3 runtime/scripts/shorts.py $REEL --vertical
for b in B00 B01 B02 B03 B04 B05 B06 B07 B08 B09; do
  python3 runtime/scripts/remotion_scenes.py $REEL/vertical --only $b; done
#          PORTRAIT-ONLY EDITS — re-apply after every shorts.py run (see PEDAGOGY.md):
#          B06 sparkLine "WHAT GAVIA IS FOR"; B03 note with no-break spaces.
./art run $REEL/vertical --height 3840          # 2160x3840; its slate reports 20 false edge-bleeds
./art final $REEL/vertical --height 3840 --out $REEL/vertical

# STEP 6 — math QC (MATH-TYPESETTING.md): B03 frames at each reveal and at
#          15/50/85%, in BOTH aspects. Record in FACTCHECK.md.

# STEP 7 — deliverables in the reel root
mv $REEL/$SLUG.mp4                   $REEL/0925-$SLUG.mp4
mv $REEL/vertical/$SLUG-vertical.mp4 $REEL/0925-$SLUG-vertical.mp4
```

## Re-running the evidence

The numbers on screen come from `evidence/`, not from the changelog. To
reproduce them (needs the local `loonnet_v1` split):

```bash
git clone https://github.com/nikhil-kunapareddy/gavia && cd gavia/desktop/src-tauri
cargo test --release --test parity -- --nocapture                    # parity_rust.out
cargo run --release --example evaluate -- --split ~/Documents/loonet/data/annotated/loonnet_v1/val.txt
cp <reel>/evidence/scale_probe.rs examples/ && cargo run --release --example scale_probe -- <val.txt>
git -C ../.. worktree add ../gavia-py 9cace7b^ && cd ../gavia-py        # the Python side
python3.11 -m venv v && v/bin/pip install onnxruntime==1.29.0 numpy==2.4.6 pillow==12.3.0
PYTHONPATH=backend v/bin/python backend/scripts/evaluate.py --split <val.txt>
v/bin/python <reel>/evidence/draft_factor.py <val.txt>
```

## If you change any wording

Audio is the clock. Never hand-edit a duration.

```bash
python3 $REEL/build_beats.py
.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL
python3 $REEL/build_beats.py                                   # re-time reveals
python3 runtime/scripts/remotion_scenes.py $REEL --force --only B0X
./art run $REEL
```

Then re-derive the vertical (STEP 5) — `shorts.py` rewrites `vertical/`.

## Expected noise, not bugs

- SKIN LINT at B09 asking for `ClaudeTitleOutro` — wrong for this channel.
- `./art scenes --check` calling a `*916` sibling NOT RENDERABLE — stale index.
- `./art doctor` / `./setup` crashing with `declare: -A: invalid option` on
  stock macOS bash 3.2 — only the readiness table.
