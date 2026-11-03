# PROMPTS.md — fifteen-of-sixteen (GATE F)

This file satisfies the toolkit's GATE F requirement. It is the real,
paste-ready command sequence used to build this reel's current revision
(narration rewrite for Kokoro's one-clause-per-sentence rule, real fabricated
text swapped into B08, retiming, outro handle/subline fix) — the fuller
per-step commentary and the first-build history are in `BUILD-PROMPT.md`.

## Audio (Kokoro, ground-truth durations)

```bash
python3 "$TOOLKIT/runtime/scripts/generate_audio_kokoro.py" "$REEL"
```

## Retime Manim `TARGET` constants to the fresh Kokoro durations

Applied via a one-off script reading each beat's `actual_duration_s` from
`beat_sheet.json` and substituting each Scene class's `TARGET = ...` line in
`scenes.py`.

## Render Manim (B01–B16), 4K final pass

```bash
cd "$REEL"
declare -A S=( [B01]=B01_OpenThreads [B02]=B02_NumberTagging [B03]=B03_ThreeBugs
               [B04]=B04_ReplayThroughGate [B05]=B05_CheckedTwice [B06]=B06_TruePositivePreserved
               [B07]=B07_SharedContextFork [B08]=B08_ZeroRealNumbers [B09]=B09_SignAndMagnitude
               [B10]=B10_ModelScoreboard [B11]=B11_RouteRewire [B12]=B12_RegexFix
               [B13]=B13_VerificationRateZero [B14]=B14_TrueNowList
               [B15]=B15_StillNotTrueAndUncommitted [B16]=B16_FifteenKilledReprise )
for B in B01 B02 B03 B04 B05 B06 B07 B08 B09 B10 B11 B12 B13 B14 B15 B16; do
  python3 -m manim -qk --fps 30 scenes.py "${S[$B]}" -o "$B.mp4"
done
mkdir -p manim
for B in B01 B02 B03 B04 B05 B06 B07 B08 B09 B10 B11 B12 B13 B14 B15 B16; do
  cp "media/videos/scenes/2160p30/$B.mp4" "manim/$B.mp4"
done
```

## Render Remotion bookends (B00, B17), force-rebuilt after the outro fix

```bash
for B in B00 B17; do
  python3 "$TOOLKIT/runtime/scripts/remotion_scenes.py" "$REEL" --only "$B" --force
done
```

## Compile

```bash
# fast preview
python3 "$TOOLKIT/runtime/scripts/compile.py" "$REEL" --height 1080 --fps 30 --review
# final master (4K UHD)
python3 "$TOOLKIT/runtime/scripts/compile.py" "$REEL" --height 2160 --fps 30
```

## Captions

```bash
python3 "$TOOLKIT/runtime/scripts/align.py" "$REEL"
```

Full step-by-step (approvals, vertical companion, cleanup) is in
`BUILD-PROMPT.md`.
