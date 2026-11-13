# BUILD-LOG — running-full-episodes-from-filings-to-ledger (AI Debt Tracker, week 5)

Built with `brutalist.art`, skill `ai-explainer`, channel `claude-hai`. Free and local end to
end: Kokoro TTS (`am_onyx`), Remotion, ffmpeg. **`$0.00` spent, no API key used.**

```
12 beats · 686 words · body 8 beats at 54–70w
narration 202.99s   ·   body 144.4s   ·   bookends 58.6s   ·   master 3:23.0
16:9  3840×2160 24fps      9:16  2160×3840 24fps      identical length, same mp3s
GATE V (explicit --mp4):  landscape BLOCKER=0 MAJOR=0  ·  portrait BLOCKER=0 MAJOR=0
```

## 1. Deliverables

| File | Spec |
|---|---|
| `Mycroft_OmMali_13_11_2026.mp4` | 3840×2160, 24fps, 202.99s — **the 16:9 master** |
| `running-full-episodes-from-filings-to-ledger-slate.mp4` | same, with beat ids + running timecode |
| `vertical/running-full-episodes-from-filings-to-ledger-916.mp4` | 2160×3840, 24fps, 202.99s |
| `vertical/…-916-slate.mp4` | same, review cut |
| `mp4/` | all four mirrored |

Author files untouched: `README.md`, `FRICTIONAL.md`, `narration_script.md`. The author's
own `description.txt` is preserved byte-identically as `description-source.txt` (verified
with `cmp` before the long-form rewrite was written over `description.txt`).

## 2. Figure → beat map

The four source figures are **reference only**, in `pantry/`. Nothing is lifted; every beat
is a native animated Remotion scene rebuilt from `figdata.json` (REBUILD LAW).

| Source figure | Becomes | Scene |
|---|---|---|
| `adt-w5-graph.*` | B01 the episode graph · B02 the ledger engine | `W5Graph`, `W5Engine` |
| `adt-w5-episodes.*` | B03 the two metrics · B04 the new bonds | `W5Versus`, `W5NewBonds` |
| `adt-w5-additions.*` | B05 the 66 additions · B06 the timing bug | `W5Added`, `W5Timing` |
| `adt-w5-fresh.*` | B07 the three fresh checks | `W5Fresh` |
| — (narration notes, FRICTIONAL.md) | B08 the limits | `W5Limits` |

Each bar's geometry in the author's SVGs was recomputed as a ratio and had to agree with its
printed fraction before the value was accepted into `figdata.json`; the checks are recorded
in each block's `_geom` field. All four `episodes` bars, all five `additions` segments, all
five `fresh` bars and the 95% line re-derive exactly.

## 3. Scene source

`runtime/remotion/src/RunningFullEpisodes.tsx` — eight components, registered twice in
`Root.tsx` (1920×1080 and 1080×1920 under `<pattern>916`). The ids avoid `W5Bluf`,
`W5Setup`, `W5Scoreboard`, `W5InventedFact`, `W5Substring`, `W5CodeAlone`, `W5Confidence`
and `W5Veto` — the Private AI Valuation series already owns those and a Composition id
collides silently.

Imports nothing from the weeks 0–4 reel files, by series convention.

## 4. What reading the frames caught that the gates did not

GATE V passed, or would have passed, every one of these.

1. **B02's closing panel was a near-empty box.** `alignItems: 'stretch'` stretched a
   two-line card to the ops column's height, leaving ~170px of empty cream under one
   sentence — which reads as a thing that failed to render. The panels now hug their
   content, and the closing panel carries a second real fact (what the ledger is graded
   against).
2. **B04's two figures did not line up.** "30 of 34" and "0 of 34" are the comparison the
   beat exists to make, and the longer baseline label pushed its figure past the midline.
   Fixed columns in landscape; the label itself shortened to `B0 · carry forward` in
   `figdata.json` (the full phrase is still spelled out on B03's legend).
3. **B08 claimed the wrong thing was borrowed.** The row read `recall 90.9% to 97.8%` beside
   a limit beginning "borrowed from the answer key…" — with no subject, that parses as *the
   recall* being borrowed. The limit now starts "the opening ledger was borrowed…". This is
   the single most important limit in the video and it was one missing noun from saying
   something false.
4. **Two frames leaked a build note.** `NOT_IN_FIGDATA` printed a file list onto B05 and
   B08. The honesty discipline it exists for is kept; the debug tail is gone.
5. **B03, B06 and B07 under-used the canvas.** Tracks widened (B03 840→1000, B07 860→1000),
   bars and figures sized up, the two reported runs on B06 spread apart.
6. **Portrait B01 drew its footnote rule through a line of text.** The portrait column
   overran its height, so `Stage`'s `space-between` had no space left to distribute and the
   accent rule landed across "All 95 of 95 development company-quarters ran end to end."
   ~120px of portrait type and padding reclaimed; landscape values untouched.
7. **Portrait B06's quarter-end rule crossed a glyph.** See §6 — two attempts.

## 5. Shared-component fix: `ClaudeTitleOutro916.tsx`

GATE V failed the portrait outro at **52% bbox fill against a 55% floor**. It is a real bug,
not a sparse-poster false positive.

```tsx
maxWidth: 1080 - PAD_X * 2,   // 936
padding: `0 ${PAD_X}px`,      // and 72 taken again from INSIDE it
```

`box-sizing` is `border-box` here, so the padding is **double-counted**: the intended 936px
column was really **792px**. Measured against the rendered frame with the real font —
the outro declares no `@font-face`, so `"Tiempos Text", "EB Garamond", …` falls through to
**Georgia Bold** — a 792px column reproduces the observed six-line break exactly, and 936px
would not. The file's own LONGEST-WORD GUARD measures against 936, and its docstring states
an active band of `x 54–1026`; both were describing a column that did not exist.

Fixed to `maxWidth: 1080` with `PAD_X` doing the insetting once. Week 5's outro went from six
ragged lines to four, and from **52% → 74%** fill.

**Blast radius, measured rather than estimated.** Simulating greedy wrap in Georgia Bold at
138px across every `beat_sheet.json` title in `fellows/om-mali/`: **14 of 17 earlier reels
would re-wrap** if their portrait outro were re-rendered — in every case to *fewer, longer*
lines. No earlier master was re-rendered and none changed on disk. Anyone who does re-render
one will get the corrected layout, not a regression; the guard's premise is now true, so a
long single word is also less likely to bleed than it was before. **This is a wider blast
radius than week 4's `ClaudeComposerAsk` fix, which affected none, and it is called out here
for that reason.**

## 6. Two wrong turns, recorded

**The re-renders that rendered nothing.** After the first QC pass, both cuts were re-rendered
and recompiled and both reported `BLOCKER=0 MAJOR=0`. Both results were worthless:
`remotion_scenes.py` skips any beat whose `media/<BID>.mp4` already exists unless `--force`
is passed, so all 24 beats were skipped and GATE V simply re-graded the untouched videos.
Every fix existed only in source. The tell was in the log all along —
`[remotion] B01: filled already (skip)` — and the gate cannot distinguish "this frame is
clean" from "this frame was never rebuilt". **Pass `--force` after any scene edit, and check
the render log says `ok:` and not `skip`.**

**The z-index that could not work.** Portrait B06's quarter-end rule crossed a glyph of a
band label. The first fix gave the label `position: relative; zIndex: 2` and the rule
`zIndex: 1`. It changed nothing, and it could not have: each band wrapper carries a
`transform`, which opens its own stacking context, so the child's z-index is scoped inside
that wrapper and can never lift it above a rule painted in the parent. The rule is now drawn
as a `Tick` **inside** the window bar and inside each band track — same x, same instant,
still visibly cutting the first run's bar, and structurally incapable of crossing a label.

## 7. Portrait

The chassis arrived with week 3's lesson built in: every bar component computes the width
given up by the columns sitting *beside* its track separately per orientation
(`W5Versus`, `W5Fresh`). No bar beat needed a portrait rescale — the second week running.

The two shapes that were new in portrait both needed work: **B01's five-node column**
(§4.6) and **B04's 9-per-row cell grid**, which ends on a ragged row of 7 and was checked to
confirm it still reads as thirty-four.

## 8. Assertions the build will fail on

`build_beat_sheet.py` refuses to write a sheet unless all of these hold:

```
FRAMING   recall_tracker > recall_baseline  AND  precision_tracker < precision_baseline
SECOND    baseline new bonds == 0,  0 < tracker 30 < issued 34
THIRD     40 real + 26 wrong == 66, five segments, summing both ways;
          3 kinds carry ids (P56–P58), the 2 misreads carry NONE
FOURTH    first-run precision < fixed-run precision, and the fixed run IS the run
          every other beat quotes
FIFTH     triage 15/15 >= 0.95 AND last week's 8/9 < 0.95;  B2 96% > reader 91% > B1 74%;
          key agreed 3 < gradable 4 < drawn 5
PLUS      174 read + 71 reused == 245 kept;  95 of 95 episodes;  53 questions;
          exactly one accented ledger operation;  body beats 45–72 words
```

## 9. Rebuild

`BUILD-PROMPT.md` is the paste-ready prompt. Order: `build_beat_sheet.py` → GATE P →
`generate_audio_kokoro.py` → `lock_durations.py` → `make_vertical.py` →
`remotion_scenes.py` **`--force`** (both) → `./art run` (both) → `final_frame_check.py` with
an explicit `--mp4` (both) → read the PNGs at ~0.95 of each beat.

Never published. The masters stay in this folder.
