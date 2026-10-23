# vertical/ — the 9:16 cut

**2160 × 3840, 24fps, 212.17s.** Same twelve beats, same narration, same numbers as the 16:9
master one directory up. This is a **re-layout, not a crop**: every beat re-renders from a
portrait composition (`<pattern>916`), so nothing is cut off the sides.

Do not edit `beat_sheet.json` here by hand. It is derived:

```bash
python ../make_vertical.py      # rewires patterns to <pattern>916, copies the mp3s
python ../lock_durations.py ../beat_sheet.json beat_sheet.json
python3 <toolkit>/runtime/scripts/remotion_scenes.py .
./art run . --height 3840       # --height 3840 + aspect_ratio 9:16 -> width 2160
```

`--height 2160` here would produce a 1215-wide file: `compile.py` derives the width from the
height and the sheet's `aspect_ratio`.

The narration mp3s in `mp3/` are **copies**, never regenerated. If the audio changes, rebuild
the 16:9 reel first and re-run `make_vertical.py`, so the two masters stay the same edit.

`make_vertical.py` resolved all twelve `W11*` patterns on the first run. Week 10 hit a hard
refusal at this exact step, because the script's composition-discovery regex matched only one
digit of week number and `W10Bluf` parses as `W` + `1` + `0Bluf`. That fix carries forward.

## Portrait values here are TUNED, not inherited

Week 9 shipped four beats whose 9:16 cut was the landscape composition scaled down. Every
week-11 component was written with both orientations in mind, and three were still rescaled
after reading the first portrait pass — underfilled rather than wrong, which is the failure
mode caught early for the second week running:

- **B02** — the document table used roughly 155 of 1,728 safe pixels and 520 of 972 wide.
  Columns, row pitch, bar height and type all raised.
- **B06** — the eight-link chain used about 340 of 1,728. The dot, the connecting segment and
  the row pitch all grew, because the chain reading as a chain is the beat's whole argument.
- **B08** — the claim/limit pairs ran small and tight; both columns raised.

Beats that re-lay out rather than rescale:

- **B03** stacks each document name above its before-and-after pair in portrait instead of
  sitting in columns, and keeps the dashed rule that separates the two real zeroes from the one
  that is not a finding. That separation is the beat.
- **B04** and **B08** turn their claim/limit and step/text pairs from two columns into two
  lines, because at 972px neither column would hold a sentence.
- **B05** keeps its three layer cards stacked and full-width; the mutability word leads each
  card in both orientations.
- **B06**'s link names wrap rather than ellipsing. The names are the evidence — a truncated
  `src/signal/findings.p…` would undercut "break any link".

## Two things to re-read if you touch this

**B02's bars are stacked, and the stacking is the argument.** The pale segment is what was
already there; the solid segment is what this week added. A single bar scaled to total lines
gave `entity_resolution.md` — which grew 60 lines of 1,016 — the longest bar on a frame whose
claim is that three documents were written from nothing, and gave those three the shortest
bars. Do not revert it to a single bar.

**Never name a scene prop something the schema does not declare.** zod drops unknown keys and
substitutes that field's default, silently; in week 10 that put another project's placeholder
copy on two beats of a 4K cut. `remotion_scenes.py` now warns before rendering. It stayed
silent through every run of this reel.
