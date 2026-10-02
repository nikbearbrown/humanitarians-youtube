# vertical/ — the 9:16 cut

**2160 × 3840, 24fps, 211.96s.** Same twelve beats, same narration, same numbers as the 16:9
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

## `make_vertical.py` could not read this week's pattern names

Its composition-discovery regex was `W\d[A-Za-z]+`, which matches exactly **one** digit of week
number. `W10Bluf` parses as `W` + `1` + `0Bluf`, and `0` is not a letter — so every week-10
pattern looked unregistered and the script refused the whole reel:

```
[vertical] B06: no portrait composition W10Suppressed916 for W10Suppressed
[vertical] REFUSED — add the 916 compositions to Root.tsx. A landscape render
           centre-cut into a portrait frame is not a vertical cut.
```

The 916 compositions were in fact registered. Fixed to `W\d+[A-Za-z]\w*`, which handles W10 and
every week after it. **The refusal itself was correct** and is the reason this cut is a real
re-layout: the script would rather stop the build than centre-cut a landscape frame.

## Portrait values here are TUNED, not inherited

Week 9 shipped four beats whose 9:16 cut was the landscape composition scaled down — B05's
seven rows filled 266 of 1728 safe pixels — and only reading the portrait frames caught it.
Every week-10 component was written with both orientations in mind, and three were still
rescaled after reading the first portrait pass:

- **B02** — the figures sit BELOW the bar in both orientations. Beside the full-width landscape
  bar they ran off the right edge of the safe area; in portrait there is no width for them at
  all. Bar height and type were then raised again after the first portrait read.
- **B03** — the diverging track narrows and the rows gain vertical pitch. The first portrait
  pass used 743 of 972 safe pixels and 180 of 1728 vertically; the columns and row heights are
  now sized to the frame.
- **B07** — the guard rows **stack** in portrait, guard name above its draft above the verdict,
  rather than sitting in three columns that would each be too narrow to read.
- **B06** keeps its two count cards **side by side** in both orientations on purpose: 11 against
  10 is the comparison, and stacking them would turn a contrast into a list.

## The defect class that reached a 4K cut this week

Two beats rendered **another project's placeholder copy** — B09 as "Verdict / The split / Chat:
synchronous judgment" and B11's outro as "bot vs bot, season one". The props were misnamed, and
zod drops keys a schema does not declare and substitutes that field's default, silently. Every
geometric check passed; the text was simply not ours.

`remotion_scenes.py` now warns before rendering when a beat passes a prop name the component's
schema does not declare. If you add a beat here and see that warning, fix the spelling — do not
render through it.
