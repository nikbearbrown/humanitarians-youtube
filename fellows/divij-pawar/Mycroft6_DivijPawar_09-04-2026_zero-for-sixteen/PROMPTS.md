# PROMPTS.md — zero-for-sixteen (GATE F)

This file satisfies the toolkit's GATE F requirement. It is the real,
paste-ready command sequence used to build this reel's current revision
(narration rewrite for Kokoro's one-clause-per-sentence rule, retiming,
outro handle/subline fix) — the fuller per-step commentary and the
first-build history are in `BUILD-PROMPT.md`.

## Audio (Kokoro, ground-truth durations)

```bash
python3 "$TOOLKIT/runtime/scripts/generate_audio_kokoro.py" "$REEL"
```

## Retime Manim `TARGET` constants to the fresh Kokoro durations

Applied via a one-off script reading each beat's `actual_duration_s` from
`beat_sheet.json` and substituting each Scene class's `TARGET = ...` line in
`scenes.py` (see the retime pass recorded in this reel's render log).

## Render Manim (B01–B14), 4K final pass

```bash
cd "$REEL"
declare -A S=( [B01]=B01_RecapAndGap [B02]=B02_LedgerTable
               [B03]=B03_OneFetchNotTwo [B04]=B04_ProvenanceRows
               [B05]=B05_SnapshotDiff [B06]=B06_DedupCollapse
               [B07]=B07_LayeringViolations [B08]=B08_CorpusBuckets
               [B09]=B09_DisjointVocabularies [B10]=B10_TwoFixesOneRecord
               [B11]=B11_RegexTruncation [B12]=B12_TrueNowList
               [B13]=B13_StillNotTrueAndUncommitted [B14]=B14_SixteenZeroReprise )
for B in B01 B02 B03 B04 B05 B06 B07 B08 B09 B10 B11 B12 B13 B14; do
  python3 -m manim -qk --fps 30 scenes.py "${S[$B]}" -o "$B.mp4"
done
mkdir -p manim
for B in B01 B02 B03 B04 B05 B06 B07 B08 B09 B10 B11 B12 B13 B14; do
  cp "media/videos/scenes/2160p30/$B.mp4" "manim/$B.mp4"
done
```

## Render Remotion bookends (B00, B15), force-rebuilt after the outro fix

```bash
for B in B00 B15; do
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
