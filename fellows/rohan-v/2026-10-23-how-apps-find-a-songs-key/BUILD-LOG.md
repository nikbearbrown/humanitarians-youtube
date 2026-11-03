# BUILD-LOG — "How Apps Find a Song's Key"

What broke, what it cost, and what changed because of it. Built 2026-10-23 for the week of 19–23 Oct.

## 1 — Toolkit update first

`git fetch` brought 4 upstream commits (37 files: the building-walkthrough, blender-build and
blender-modelbuild skills). The merge was clean; Remotion stays at 4.0.535.

## 2 — The first chroma was flat

The first run named the key right on only 27 of 60 songs, and even the C major pop song came out G major. Its
note profile was nearly flat (every note between 0.07 and 0.10): every STFT bin had been log-compressed and
added up, so the noise floor of the many quiet bins drowned the few loud ones. Chroma now sums the energy per
pitch class and scales each frame to its loudest note (as librosa's chroma does). After: 50 of 60, and the
C major profile reads C, G, E tallest.

## 3 — Four-second windows heard chords, not keys

The key-change test first used 4-second windows. At about 110 BPM that is two chords, so the windows named
the chords' keys (G major, A minor) instead of the song's. Eight-second windows (four bars or so) heard
C major, then C sharp major.

## 4 — A wrong runner-up, caught before render

The first script said C major's "closest rival" was A minor (0.69). The run's own ranking puts G major second
(0.72) and A minor third. B03 was re-voiced ("The next best, G major, only zero point seven two"), the scene now
takes the runner-up from the data, `key.py` logs it, and `export_key_data.py` asserts it.

## 5 — Rounding

`scene.json` first stored the correlations to 4 decimals, so the screen would have shown A minor as 0.885 while
the narration says 0.886 (the value is 0.88554). They are stored to 6 decimals now.

## 6 — Layouts and gates on probe stills (before any render)

- **Phone titles wrapped into the content** ("Seven Notes, One Home"): shortened ("Seven Notes", "Count the
  Notes", "Match the Shape", "Wrong Home").
- **Landscape B01 underfilled**: the piano is taller. **B05's MIREX chip ran past the right edge**: shortened.
  **B06's key-change line cut through "wrong for both"**: drawn behind the lanes.
- **Gate V underfill at mid-beat (B03, B04)**: the 24 correlation bars and the 60 squares now show as ghosts
  from the start.
- **GATE T §8.1 on the phone (72 px at 4K)**: the italic spark lines split into glyph groups, and the x-height
  part of "Same" ("ame") measured 66 px. Phone spark lines are 1.25× larger; the library `HaiApplyCard` gained
  an opt-in `sparkScale` for its phone spark.
- **B02's phone caption sat under the heatmap**: moved below it.

## Render

Masters (`./art final`, receipts `*.verified.json` beside each file; SHA-256 re-checked on copy):

| Cut | File | Size | Length | SHA-256 |
|---|---|---|---|---|
| 16:9 | `landscape/KeyDetection_RohanV.mp4` | 3840×2160 | 160.46 s | `8aaaba05dc26112ebe94a8d262eb68b3fcb209e3202559094a4a41f4291532c8` |
| 9:16 | `vertical/KeyDetection_RohanV.mp4` | 2160×3840 | 160.46 s | `3cb6c7ae32aa75f8b887bb9c2828868c078eedfaa1d3b46ae83cc023577fa7ae` |

Gates on the accepted finals: GATE F pass; GATE T pass, 0 FAILs ([TYPECHECK.md](./TYPECHECK.md),
[vertical/TYPECHECK.md](./vertical/TYPECHECK.md)); Gate V clean, 0 BLOCKER / 0 MAJOR
(18 landscape and 18 portrait frames sampled). Looked at by eye: [qc-sheet-16x9.png](./qc-sheet-16x9.png),
[qc-sheet-9x16.png](./qc-sheet-9x16.png).

Both cuts accepted on the first final, 2026-10-23.

Uploaded to Google Drive `2026-10-23/landscape/` and `2026-10-23/vertical/`; md5 of each Drive copy
matches the local master.
