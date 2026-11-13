# vertical/ — the 9:16 cut

`running-full-episodes-from-filings-to-ledger-916.mp4` · **2160×3840**, 24fps, 202.99s — the
same length as the 16:9 master, to the frame.

## It is a re-layout, never a crop

Every scene in `RunningFullEpisodes.tsx` lays itself out natively at both sizes through one
helper:

```tsx
const { f } = useStage();     // f(landscape, portrait)
const BAR_W = Math.min(SAFE.w - BESIDE, f(1000, 660));
```

Each component is registered twice in `Root.tsx` — once at 1920×1080 and once at 1080×1920
under its `<pattern>916` name — so there is one component and two registrations, not two
components. Nothing is cropped, letterboxed or scaled down. B01's five graph nodes turn from
a row with `→` into a column with `↓`; B02's two ledger panels stop sitting either side of
the operation list and stack above and below it; B04's 34 cells go from 17 per row to 9.

## The audio is the same audio

`make_vertical.py` derives `vertical/beat_sheet.json` from the landscape one and **copies the
twelve mp3s across**. Narration is never regenerated for this cut, so no number, no word and
no duration can differ between the two masters.

It matches the registration tuple shape in `Root.tsx`, not a naming convention — do not
"simplify" that regex back to a `W<digits>` pattern, which has silently missed a whole series
twice before.

## No bar beat needed a portrait rescale

Second week running. Both bar components compute the width given up by everything sitting
*beside* the track separately per orientation:

```tsx
const BESIDE = f(400 + 26 + 156 + 40, 150 + 18 + 40);
```

In landscape the name column sits beside the track and pays for the value column. In portrait
it stacks *above* the track and pays for nothing — which is precisely what clipped every
figure on week 3's B04. Writing it into the component instead of rediscovering it in QC is
the whole of the saving.

## What portrait did break

Three things, none of which landscape showed.

1. **B01 ran out of column.** `Stage` distributes with `space-between`; an over-full column
   leaves it nothing to distribute, and the FootNote's accent rule then drew straight across
   "All 95 of 95 development company-quarters ran end to end." ~120px of portrait type and
   padding reclaimed. Landscape values untouched.
2. **B06's quarter-end rule crossed a glyph.** In portrait the band label wraps to two lines
   and the full-height rule met it. A z-index could not fix this — the band wrapper's
   `transform` opens its own stacking context — so the boundary is now a `Tick` drawn inside
   the window bar and inside each band track. Same x, same instant, no text crossed.
3. **B11, the shared outro, failed GATE V at 52% fill.** A padding double-count in
   `scenes/ClaudeTitleOutro916.tsx` made the title column 792px where the file's own guard
   assumed 936. Fixed; 52% → **74%**. See `../BUILD-LOG.md` §5 for the measured blast radius —
   it is wider than week 4's and is documented rather than waved through.

## Gates

```
GATE V (explicit --mp4):  frames=24  BLOCKER=0  MAJOR=0
```

Check `_qc/REPORT.md` and `_qc/contact_sheet.png` here, not the landscape ones — GATE V can
pass 16:9 and fail 9:16 on the very same scene, and this week it did, twice.
