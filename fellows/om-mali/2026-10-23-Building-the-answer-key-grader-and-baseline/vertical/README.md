# vertical/ — the 9:16 cut

**2160 × 3840, 24fps, 204.51s.** Same twelve beats, same narration, same numbers as the 16:9
master one directory up. This is a **re-layout, not a crop**: every beat re-renders from a
portrait composition (`<pattern>916`), so nothing is cut off the sides.

Do not edit `beat_sheet.json` here by hand. It is derived:

```bash
python ../make_vertical.py      # rewires patterns to <pattern>916, copies the mp3s
python3 <toolkit>/runtime/scripts/remotion_scenes.py .
./art run . --height 3840       # --height 3840 + aspect_ratio 9:16 -> width 2160
```

`--height 2160` here would produce a 1215-wide file: `compile.py` derives the width from the
height and the sheet's `aspect_ratio`.

The narration mp3s in `mp3/` are **copies**, never regenerated. If the audio changes, rebuild
the 16:9 reel first and re-run `make_vertical.py`, so the two masters stay the same edit.

`make_vertical.py` resolved all twelve `AK*` patterns on the first run, because it matches the
**registration tuple shape** `['<Id>', <Component>, <schema>],` rather than a naming
convention. Two earlier versions hardcoded the Private AI Valuation series' `W<digits>` ids and
refused whole reels whose 916 compositions were present. Do not "simplify" that regex back.

## Portrait values here are TUNED, not inherited

The chassis arrived with week 1's portrait values already raised, which saved repeating that
work on the spark line, header, source and footnote. The beat bodies still underfilled on the
first portrait read — six of eight — and **59 `f(landscape, portrait)` values were raised**.
The landscape half of every one is unchanged, so the 16:9 master did not need re-rendering.

- **B01** — the answer key's bar was 120px tall against 1,728 safe pixels. Bar 120 → 190,
  the three counts set at the landscape size, and the legend swatches and type raised so
  "Bond by bond 900" reads at arm's length.
- **B02** — mode cards, field chips and the pairing line all raised; card padding 20 → 26.
- **B03** — the five bug rows sat in the top third. Row pitch 30 → 42, the numerals 42 → 48,
  the verdict 48 → 54.
- **B04** — bar height 58 → 74 and row pitch 34 → 48, so the two calibration bars and the one
  measured bar read as two groups rather than one block.
- **B05** — the biggest lift. The empty track was 168px tall and read as a thin strip rather
  than a void: 168 → **300**, with the word inside it at 26 → 31. The whole beat is that
  rectangle being empty, so it has to be big enough to be felt.
- **B06** — the axes were drawn at landscape proportions. Row height 112 → 158, tick height
  40 → 48, the label row pushed clear of the axis, and the per-axis pitch 92 → 124.
- **B07** — timeline height 170 → 250, with the two markers, the shift label and both readings
  spread into the extra room.

**B08 was already right** and was left alone; it inherits week 1's tuned claim/limit layout.

Beats that re-lay out rather than rescale:

- **B02**'s three mode cards stack vertically instead of sitting in a row.
- **B04**'s label/bar/value rows become two lines, because at 972px wide a label will not sit
  beside a bar and a fraction.
- **B01** keeps its partitioned bar full-width in both orientations, and the level counts stay
  in the legend. A segment 41 of 1,093 wide cannot hold a label in either aspect.
- **B05** and **B06** keep their full-width tracks; only the heights and the label rows move.

## Three things to re-read if you touch this

**B05 is supposed to be mostly empty.** The outlined, labelled track with nothing in it is the
argument. If a fill check complains, read the frame — the fix is never to put a bar in it, and
never to delete the outline either, because an absent bar reads as a rendering fault.

**B06's labels are anchored to their own ticks, and sized independently of them.** Sizing the
baseline label from the tick position collapsed it to a 2px column when the baseline is 0 —
which it always is here, that being the point — and "copying forward: 0" wrapped one word per
line. GATE V passed that frame; reading it caught it.

**Never name a scene prop something the schema does not declare.** zod drops unknown keys and
substitutes that field's default, silently; in week 10 of the earlier series that put another
project's placeholder copy on two beats of a 4K cut. `remotion_scenes.py` warns before
rendering. It stayed silent through every run of this reel, in both orientations.
