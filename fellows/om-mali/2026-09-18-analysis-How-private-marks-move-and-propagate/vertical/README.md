# vertical/ — the 9:16 cut

**2160 × 3840, 24fps, 225.1s.** Same twelve beats, same narration, same numbers as the 16:9
master one directory up. This is a **re-layout, not a crop**: every beat re-renders from a
portrait composition (`<pattern>916`), so nothing is cut off the sides.

Do not edit `beat_sheet.json` here by hand. It is derived:

```bash
python ../make_vertical.py      # rewires patterns to <pattern>916, copies the mp3s
python ../lock_durations.py ../beat_sheet.json beat_sheet.json
python3 <toolkit>/runtime/scripts/remotion_scenes.py .
./art final . --height 3840     # --height 3840 + aspect_ratio 9:16 -> width 2160
```

`--height 2160` here would produce a 1215-wide file: `compile.py` derives the width from the
height and the sheet's `aspect_ratio`.

The narration mp3s in `mp3/` are **copies**, never regenerated. If the audio changes, rebuild
the 16:9 reel first and re-run `make_vertical.py`, so the two masters stay the same edit.

**Watch B05 here.** Four managers price at $259.1364 on the same date, so their dots and labels
share a y. The component fans colliding dots horizontally and pushes labels to a minimum gap
with a leader line — in portrait the plot is narrower, so if you change its height or the label
size, re-read that frame before shipping. B05 keeps its two period-end columns side by side in
both orientations on purpose: the crossing between them is the argument, and stacking them
would destroy it.
