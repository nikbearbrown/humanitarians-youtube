# vertical/ — the 9:16 cut

**2160 × 3840, 24fps, 213.74s.** Same twelve beats, same narration, same numbers as the 16:9
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

## `make_vertical.py` would have refused this reel

Under the regex it shipped with in week 11 — `W\d+[A-Za-z]\w*` — `GDTBakeoff` and `GDTLevels`
look unregistered, because that pattern encodes the Private AI Valuation series' *naming
convention* rather than anything structural. It is the second time that regex has refused a
reel whose 916 compositions were in fact present (week 10 hit it when `W10Bluf` parsed as
`W` + `1` + `0Bluf`; widening it by one character then was treating the symptom).

It now matches the **registration tuple shape** Root.tsx actually uses:

```
['<Id>', <Component>, <schema>],
```

which is the part that is stable across series. That fix carries forward.

## Portrait values here are TUNED, not inherited

Six of the eight body beats underfilled on the first portrait read — not wrong, just small,
which is the failure mode caught early for the fourth week running. **73 `f(landscape,
portrait)` values were raised**; the landscape half of every one is unchanged, so the 16:9
master did not need re-rendering.

- **B01** — the bar height was the landscape 76px against 1,728 safe pixels of height. Bar,
  value, label, the 4.3× figure and the gap note all raised; row pitch 44 → 72.
- **B02** — the four stage boxes used roughly a third of the column. Padding, both type sizes
  and the gaps between boxes all raised, and the turned arrow grew with them.
- **B04** — two rows in the top third of the frame. Bar height 44 → 62 and row pitch 48 → 104,
  so the two tests read as two tests rather than one block.
- **B05** — the densest frame. Bar height 110 → 168 and the segment numerals 44 → 62, because
  the partition IS the argument and a thin band does not carry it.
- **B06** — the 495 and its two parts were set at landscape sizes. 92 → 136 and 56 → 84, and
  the gauge was capped at 790px so the 93.4% stays on the same line as the bar instead of
  wrapping beneath it.
- **B07** — bar height 46 → 62 and row pitch 40 → 82, so the one shared pass rule reads as a
  single line down three tracks rather than three separate ticks.

The shared chassis moved with them: spark line, header, subtitle, source and footnote each
gained 3–4px in portrait only. **B03 and B08 were already close**; both got a smaller lift
for consistency.

Beats that re-lay out rather than rescale:

- **B01**, **B04**, **B07** turn their label/bar/value rows into two lines, because at 972px
  wide neither a claim nor a model name fits beside a bar.
- **B02**'s pipeline runs top-to-bottom with a turned arrow (`↓`), not a squeezed row.
- **B05** keeps its single partitioned row full-width in both orientations. The three labels
  stay under their own segments, so "By deal" is still attached to the 4 it describes — a
  stacked legend would break the only thing the frame is doing.
- **B06**'s divider between the total and its two parts turns horizontal.

## Three things to re-read if you touch this

**B05 is one row of 25, partitioned, with the assumed 21 drawn as a dashed bracket over it.**
Three separate bars would invite a comparison of 15 against 4 against 6, which is not the
beat. The beat is that a fixed set splits differently once coverage is measured.

**B05's bracket caption goes ABOVE the bracket, right-aligned to its end.** Placing it to the
right of the bracket bled past the title-safe edge and failed GATE V with 2 BLOCKERs on the
16:9 cut. At 21 of 25 the bracket already reaches 84% of the content width, so there is no
room out there for a caption of any length.

**Never name a scene prop something the schema does not declare.** zod drops unknown keys and
substitutes that field's default, silently; in week 10 that put another project's placeholder
copy on two beats of a 4K cut. `remotion_scenes.py` now warns before rendering. It stayed
silent through every run of this reel, in both orientations.
