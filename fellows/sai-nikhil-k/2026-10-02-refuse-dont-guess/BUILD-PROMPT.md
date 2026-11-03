# BUILD-PROMPT — 2026-10-02-refuse-dont-guess · Refuse, Don't Guess

Paste-ready, from the toolkit root. Free end to end (Kokoro, Remotion, ffmpeg).

```bash
REEL=weekly_updates/2026-10-02-refuse-dont-guess

# STEP 0 — the sheet is GENERATED. Edit build_beats.py, never beat_sheet.json:
#          it re-typesets B03's equations, re-times the B03/B04 reveals and the
#          B01/B05 UI cues to the measured audio, and asserts every reveal lands
#          inside the 15 s TypesetMath/ExecutedData compositions.
python3 $REEL/build_beats.py --check && python3 $REEL/build_beats.py && python3 $REEL/fill_narration.py

# STEP 1 — GATE P (human). Sai reads PEDAGOGY.md, works the checklist and signs
#          the VERDICT line. Claude never signs it.

# STEP 2 — narration audio (the master clock). The venv python: the default
#          python3 cannot see Kokoro.
.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL
python3 $REEL/build_beats.py           # re-cue reveals to the measured durations

# STEP 3a — the two screen-recording beats, both aspects (Pillow → system python3).
#          Reads ui/takes/*.mp4; writes media/B01.mp4, media/B05.mp4 and
#          pantry/B01-916.mp4, pantry/B05-916.mp4. ~40 s each.
python3 $REEL/make_ui.py

# STEP 3b — the eight Remotion beats at true 4K, ONE BEAT PER CALL.
for b in B00 B02 B03 B04 B06 B07 B08 B09; do python3 runtime/scripts/remotion_scenes.py $REEL --only $b; done

# STEP 4 — review cut + GATE V (LOOK at _qc/), then the clean 4K 16:9 master.
./art run $REEL
./art final $REEL --out $REEL
mv $REEL/claude-sai-refuse-dont-guess.mp4 $REEL/1002-claude-sai-refuse-dont-guess.mp4
mv $REEL/claude-sai-refuse-dont-guess.verified.json $REEL/1002-claude-sai-refuse-dont-guess.verified.json

# STEP 5 — the SAME film in 9:16 (every beat, no cap, no endcard), 4K portrait.
#          B01/B05 come from pantry/ automatically.
python3 runtime/scripts/shorts.py $REEL --vertical
#          PORTRAIT-ONLY EDITS — re-apply after every shorts.py run (PEDAGOGY.md lists them).
for b in B00 B02 B03 B04 B06 B07 B08 B09; do python3 runtime/scripts/remotion_scenes.py $REEL/vertical --only $b; done
./art run $REEL/vertical --height 3840
./art final $REEL/vertical --height 3840 --out $REEL
#          then rename to 1002-claude-sai-refuse-dont-guess-vertical.mp4 (+ .verified.json)

# STEP 6 — math QC (MATH-TYPESETTING.md): B03 frames at each reveal and at
#          15/50/85%, in BOTH aspects. Record in FACTCHECK.md.

# STEP 7 — deliverables
ffprobe -v error -show_entries stream=width,height -of csv=p=0 $REEL/1002-claude-sai-refuse-dont-guess*.mp4
#          → 3840,2160 and 2160,3840
```

## Re-running the evidence

```bash
S=<scratch>; git clone https://github.com/nikhil-kunapareddy/gavia $S/gavia && cd $S/gavia && git checkout 760e465
cd desktop && npm ci && npx vitest run                       # → evidence/vitest.out (257/257)
(cd src-tauri && cargo test --release)                        # → evidence/cargo_test.out (115/115)
cp <reel>/evidence/batch_rules.test.ts src/lib/ && REEL=<reel> npx vitest run src/lib/batch_rules.test.ts; rm src/lib/batch_rules.test.ts
bash <reel>/evidence/release_and_ci.sh > <reel>/evidence/release_and_ci.out
# photos: cd <reel>/evidence && python3 fetch_photos.py && python3 make_survey.py
```

## Re-recording the app (only if the takes must change)

Needs macOS with **Screen Recording for Terminal.app** (the recorder runs through
Terminal) and Accessibility for the shell running the scripts. The takes drive
the real pointer and keyboard for ~2 minutes: nobody may touch the Mac.

```bash
cd <reel>/ui/rec && for f in mouse win wins allwins2 axval; do swiftc -O $f.swift -o $f; done
./take_batch.sh     # launches Gavia with GAVIA_DATA_DIR=<scratch>; records batch.mp4
./take_updates.sh   # Settings → Updates; turns the switch OFF on camera
./axval press       # turn it back ON (the switch is shared with the real install); ./axval to confirm value= 1
```

Known traps, each of which cost a take:
- `screencapture -v` stops when it receives keystrokes — use `rec2.sh` (ffmpeg).
- The macOS open panel can take >5 s to appear; the script waits for Gavia's
  layer-8 window before typing.
- Opening, cancelling and reopening the panel quickly **crashed Gavia 0.3.1**
  (`unexpected NULL returned from +[NSOpenPanel openPanel]`) — no warm-up.
- After that crash, macOS's crash dialog steals focus; dismiss it first.
- Timeline `click` marks precede a 0.7 s pointer glide; measure timings from the video.

## If you change any wording

Edit `build_beats.py` → `generate_audio_kokoro.py` → `build_beats.py` →
`make_ui.py --only B0X` (UI beats) or `remotion_scenes.py --force --only B0X` →
`./art run` → re-derive the vertical. If B01's or B05's audio length changes,
re-check `make_ui.py`'s segment and camera times against the new cue times
(`beat_sheet.json` → `shot.ui.cues`). Never hand-edit a duration.

## Expected noise, not bugs

- SKIN LINT wants `ClaudeTitleOutro` for B09 — wrong for this channel.
- GATE V underfill on centred cards; B09 has `qc.sparse`.
- The portrait slate's own burn-in reports edge-bleed; trust `./art final`'s gate.
