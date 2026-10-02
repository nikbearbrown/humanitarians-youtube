# vertical/ — the 9:16 cut

**2160 × 3840, 24fps, ~217.9s.** Same twelve beats, same narration, same numbers as the 16:9
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

**Watch B05 and B06 here.** Both are name-in-a-column beats, and both had a label defect in the
landscape cut that portrait makes worse, because portrait has less horizontal room:

- **B05** keeps its **horizontal** time axis in portrait. The distance between a company's
  acquisition date and the panel's first mark for the same company IS the argument; rotating
  the axis would destroy the comparison. The company label column is sized to fit
  "Space Exploration Technologies Corp." — at the old width it truncated to
  "Space Exploration Tech…" while the same name was spelled in full lower on the same frame.
  In portrait the column is narrower and the names are abbreviated by design; read the frame if
  you change `LABEL_W`.
- **B06** is here because of a truncation. The source figure ran manager names into the next
  column — "Robinhood Ventures Fund" into "Databricks". **The layout auditor does not catch
  that**, because the two are separate text elements sharing a baseline rather than overlapping
  boxes. Each column owns its width and clips inside it, so the classes of defect cannot
  recur — but a clipped name is still a defect, so the widths are sized to the longest name in
  the set rather than to the average.

B06 also carries the one number in this reel that was wrong on screen and passed every
geometric check: `max_pct_net_assets` arrives from `figdata_week9.json` **already as a
percent** (17.918 means 17.9%). Multiplying it by 100 put "1791.81% of a fund's net assets" on
a 4K frame. Do not reintroduce the conversion.
