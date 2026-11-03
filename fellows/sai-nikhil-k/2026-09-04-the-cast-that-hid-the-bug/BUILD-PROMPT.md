# BUILD-PROMPT — The Cast That Hid the Bug

Paste-ready, end-to-end. Run every command from the toolkit root
(`/Users/nikhilkunapareddy/Documents/brutalist.art`).

`<reel>` = `weekly_updates/09-04-02`

```bash
REEL=weekly_updates/09-04-02
PY=.venv/bin/python          # NOT bare python3 — Kokoro lives in the venv
```

## STEP 1 — human review (GATE P)

Open `$REEL/PEDAGOGY.md`, work the review checklist, and put the approval word
in the `VERDICT:` blank at the bottom. The gate no longer hard-blocks audio
(see `VOICE-LOCK.md`), so this is a record of review, not a lock — it still
matters, because nothing else in the pipeline reads the narration critically.

## STEP 2 — narration audio (the master clock)

```bash
$PY runtime/scripts/generate_audio_kokoro.py $REEL
```

Writes `$REEL/mp3/beat-B0*.mp3` + `timings.json`. Those durations are the clock;
never hand-edit a duration downstream.

## STEP 3 — render the 16:9 beats at true 4K

```bash
$PY runtime/scripts/remotion_scenes.py $REEL
```

`remotion_scenes.py` picks `--scale` per composition so every beat lands at
3840x2160: `2x` for the 1920x1080 Claude UI scenes (B00, B05, B06, B07), `3x`
for the 1280x720 illustration and deck-pattern comps (B01, B02, B03). Add
`--force` to re-render after editing props, `--only B02` for one beat.

## STEP 4 — compile the 16:9 4K master

```bash
./art run $REEL --height 2160
```

→ `$REEL/claude-sai-the-cast-that-hid-the-bug.mp4` (clean 4K master)
→ `...-slate.mp4` (labeled review cut) and `$REEL/_qc/` — **look at the frames**.

## STEP 5 — derive the 9:16 short

```bash
$PY runtime/scripts/shorts.py $REEL
```

Writes `$REEL/short/` with its own beat sheet, rewiring each beat to its
`<Pattern>916` composition. Every pattern in this reel has a registered portrait
sibling with an identical props type, so nothing should be flagged. At ~2:22 the
reel is under the hard 3:00 Shorts cap, so no beats are cut and no outro is
rewritten — every beat reuses the parent's mp3.

## STEP 6 — render + compile the 9:16 master at true 4K

```bash
$PY runtime/scripts/remotion_scenes.py $REEL/short
./art run $REEL/short --height 3840
```

**`--height 3840`, not 1920.** `shorts.py` prints a `--height 1920` hint, which
is 1080p portrait. True 4K vertical is 2160x3840.

## Verify

```bash
for f in $REEL/*.mp4 $REEL/short/*.mp4; do
  echo "$f  $(ffprobe -v error -select_streams v:0 \
    -show_entries stream=width,height -of csv=p=0:s=x "$f")"
done
```

Expect `3840x2160` for the long and `2160x3840` for the short.
