# BUILD-PROMPT — claude-liam-minirag

The single paste-ready prompt that rebuilds this reel end to end. Run it from
the directory that contains `brutalist.art/`. It never publishes.

---

## Prerequisites (once per machine)

```bash
brew install ffmpeg poppler
cd brutalist.art
uv venv --python 3.12 --seed .venv          # NOT Homebrew python@3.12 — see note
conda deactivate && source .venv/bin/activate
./setup --install
./art smoke
```

**Two machine-specific gotchas, both documented in the toolkit's plan file:**

1. Homebrew's `python@3.12` is broken on macOS 26.2 — its `pyexpat` fails to
   load, which makes `platform.mac_ver()` return `''` and crashes every `pip`
   call inside `truststore`. Use `uv`'s standalone build instead. One-line test:
   `python3 -c "import platform; print(platform.mac_ver()[0])"` must print your
   macOS version, not `''`.
2. `runtime/scripts/build_safety.py:186` needs `_` in the leading character
   class of the slug regex, or `./art smoke` cannot run at all. See SOURCES.md.

**The venv must be active for every `./art` command.** New terminal →
`conda deactivate && source .venv/bin/activate` first.

---

## The build

```bash
REEL=../hai-research/youtube/claude-liam-minirag

# 1. Audio is the master clock — always first, always regenerated from the sheet
python3 runtime/scripts/generate_audio_kokoro.py $REEL

# 2. Compile the review cut (Gate F → Gate L → render → Gate V → Gate T)
./art run $REEL

# 3. What still needs attention, and how
./art todo $REEL

# 4. Clean master, no beat markers — only after human review
./art final $REEL
```

Step 4 writes to `$ART_OUT`, else `brutalist.art/renders/`. Override per run with
`--out DIR`. **Rendering is not publishing** — the file goes to a folder and
stops there.

---

## Changing one beat without rebuilding the film

This is the whole point of the beat-sheet architecture. To fix beat B05:

```bash
# edit beat_sheet.json → beats[] → B05 → narration_text
python3 runtime/scripts/generate_audio_kokoro.py $REEL --only B05
rm $REEL/media/B05.mp4
./art run $REEL
```

Only B05's audio regenerates, only B05's visual re-renders, and the cut
recompiles around the new duration. Every approved beat is untouched.

**Never hand-time anything.** If a beat runs long, cut words from
`narration_text` and regenerate — the measured MP3 is the only clock.

---

## Changing a visual

The five reel-local components live in
`brutalist.art/runtime/remotion/src/MiniRag.tsx`, registered in `Root.tsx` under
the folder `MiniRag`. After any change:

```bash
cd brutalist.art/runtime/remotion && npx tsc --noEmit -p tsconfig.json
cd ../.. && ./art scene-index
rm $REEL/media/B0X.mp4 && ./art run $REEL
```

No component hardcodes a statistic — every figure arrives as a prop from
`beat_sheet.json`. **A wrong number is a beat-sheet fix, never a component fix.**

---

## The rules this reel is built under

- **Audio-first.** Measured MP3 durations are the master clock.
- **Library-first.** `./art scenes "<what the beat needs>"` before authoring
  anything new. GATE L findings are recorded in SHOTLIST.md.
- **Verify by LOOKING at frames** (`_qc/` + `qc-sheet.png`), never by the mp4
  probe alone.
- **REBUILD LAW.** Every figure is redrawn natively; no screenshots lifted from
  the paper.
- **DOUBLE-CHECK LAW.** Claims verified against the source and rewritten in the
  Teardown register; corrections logged in SOURCES.md.
- **Never publish.** There is no publishing machinery in this toolkit.

---

## Vertical (9:16)

Not built. A Short is a **different beat sheet, never a crop**:

```bash
./art shorts $REEL
```

writes its own sheet into `short/` and rewires each beat to a `<Pattern>916`
composition where one is registered. The five `MiniRag*` components are 16:9
only, so those beats would be flagged rather than silently centre-cut. Building
portrait variants is a separate, deliberate task — see `RENDER-TARGETS.md` §3.
