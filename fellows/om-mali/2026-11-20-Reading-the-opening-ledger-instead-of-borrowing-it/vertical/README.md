# vertical/ — the 9:16 cut

`reading-the-opening-ledger-instead-of-borrowing-it-916.mp4` — **2160×3840**, 24fps,
206.36s. Same twelve beats, same narration, same length as the 16:9 master.

## This is a re-layout, never a crop

Each scene is **one component with two registrations**. `useVideoConfig()` detects
orientation and an `f(landscape, portrait)` helper picks per-axis values, so portrait gets
its own column widths, type sizes and row rhythm rather than a scaled-down 16:9 frame.
Portrait compositions are registered in `Root.tsx` under the `<pattern>916` name.

Cropping the 16:9 master would cut the right-hand value column off every bar beat in the
reel. Don't.

## The audio is shared, not regenerated

`make_vertical.py` copies the same twelve mp3s across. They were verified **byte-identical
by hash** to the landscape cut's. Never run `generate_audio_kokoro.py` against this folder
— it would produce a second set of durations and silently desynchronise the two cuts.

`make_vertical.py` matches the **registration tuple shape** in `Root.tsx`, not a naming
convention. Do not "simplify" that regex to a `W<digits>` pattern.

## Rebuilding

```bash
python3 runtime/scripts/remotion_scenes.py <reel>/vertical --force
./art run <reel>/vertical --height 3840
python3 runtime/qc/final_frame_check.py <reel>/vertical \
    --mp4 <reel>/vertical/reading-the-opening-ledger-instead-of-borrowing-it-916.mp4
```

`--force` is not optional. Without it every beat whose `media/<BID>.mp4` exists is skipped
and the gate re-grades the old video. `--height 3840` is not optional either — this
sheet carries `"aspect_ratio": "9:16"`, and `--height 2160` would give a 1215-wide frame.
Pass `--mp4` explicitly: with a clean cut and a slate cut in the folder, the gate
otherwise picks the first non-slate match, which is not necessarily what you are shipping.

## Portrait-specific notes from this build

- **B05 is the densest frame in the reel** — six bars, six labels with sub-notes, a cost
  line and a verdict. It was read in 9:16 **first**, because week 5's B01 overran its
  portrait column and let the footnote rule draw through the line above it. It holds, and
  the agent/B0 recall bars still read as level with B0 very slightly the longer.
- **B07** packs 50 cells into five rows of ten and 36 into 10/10/10/6. Counts stay exact.
- **B06** keeps its landscape-only type increase. Portrait values were left alone on
  purpose — portrait was already tight, and inheriting the landscape bump would have
  pushed the rule block into the footnote.
- **B11** covers 0.73 of its safe area. Before the `ClaudeTitleOutro916` padding
  double-count fix it measured 0.52, against a 0.55 floor.

Final gate: **0 BLOCKER · 0 MAJOR**, and all twelve frames read individually at 0.95 of
their own beat duration.
