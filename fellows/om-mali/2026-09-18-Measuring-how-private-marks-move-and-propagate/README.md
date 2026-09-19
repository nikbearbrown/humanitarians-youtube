# Week 8 — Measuring how private marks move and propagate

Five figures and a 3:00 narration script. The week's work: the marks panel stopped growing and
started being measured. Four questions asked of 5,479 marks — how often a price changes, whether
that rate is the same everywhere, whether managers pricing the same company on the same date
agree, and how fast a new price level travels across holders.

| File | Beat | What it shows |
|---|---|---|
| `w8-remark.png` | 0:30 | 25.0% of 4,079 consecutive observations unchanged, against a plan that expected 30–40 — and three widenings of the rule that all stay below the band |
| `w8-bycompany.png` | 1:00 | The same statistic by company: 0.0% for Groq and 1.1% for OpenAI up to 48.5% for X.AI |
| `w8-dispersion.png` | 1:30 | 130 same-date groups, median spread 10.8%, 92 of them holding more than one price level |
| `w8-window.png` | 2:05 | One real window: Anthropic preferred, 8 managers and 11 marks crossing 140.97 → 261.57 over two period ends |
| `w8-propagation.png` | 2:35 | 37 price levels adopted by three or more managers — median 30 days to half, 15 arriving on the same period end, slowest 92 |

SVG sources sit beside each PNG. PNGs are 2917 × 1750. `figdata_week8.json` is the measured data
every figure was drawn from.

## Rules

- Every number is queried from the marks panel at build time
  (`scripts/make_week8_figures.py` in the project repo) and dumped to `figdata_week8.json`
  before anything is drawn. No figure carries a hand-typed number.
- Both QA passes were run: the layout audit reports **0 errors on all five**, and each PNG was
  read and checked for substance.
- Six palette tokens from `brutalist/DESIGN.md`, nothing else. Red is the primary series, never
  a warning colour.

## The three things not to get wrong on camera

**25% is a disagreement with the plan, not a bug.** The plan predicted 30–40% of observations
would be carried forward unchanged. Measuring gave 25.0%. Widening the definition of "unchanged"
to within 0.1% gives 26.3%, and to within 1% gives 29.6% — still under the band. The finding is
that private marks move *more* than expected, and it survives every reasonable definition.

**Same-date spread is not automatically disagreement.** Some of it is a new round that some
managers have picked up and others have not. That is exactly why `w8-window` exists: it shows one
real window where both readings are visible at once. The honest claim is "managers hold different
prices on the same date", not "managers disagree about value".

**Every number sits behind a guard.** 294 unpriced marks, 301 marks on a split-blocked series and
any incomplete run are excluded before a statistic is computed. The report also carries a
"what none of this shows" section: these are fund marks, not transactions.

## Four defects the figures caught

Each of these was wrong in the drawing code until the PNG was read:

1. **A subtitle hard-coded "Nine managers"** when the window actually holds 8 managers and 11
   marks. Both counts are now derived from the rows being plotted.
2. **The red/grey split in the window figure was hard-coded at `price > 220`.** It now runs the
   same single-linkage level clustering the findings module uses, so the "new round" dots are
   whatever the clustering says they are.
3. **The dispersion highlight was hard-coded at `spread >= 0.4`.** It now marks the measured
   90th percentile.
4. **The propagation figure claimed "the biggest events are the fastest".** Checked against the
   data: events with 10+ managers have a median of 27 days to half versus 30 for the rest, and
   12 of 28 smaller events land at zero days against 3 of 9 large ones. The claim did not hold
   and was replaced with counts that do — 15 of 37 at zero days, slowest 92.

---

## The built reel

*(Appended by the brutalist.art build. Everything above is the original figure brief and is
unmodified.)*

Rebuilt as a 12-beat `ai-explainer` / `claude-hai` reel — **twelve beats, zero slates, $0.00**.
Free/local throughout: Kokoro TTS + Remotion + ffmpeg.

**Two masters, one edit.** 16:9 at 3840×2160 and 9:16 at 2160×3840, from the same components,
the same props and the same narration mp3s. The vertical cut is a re-layout, not a crop.

| Where | What |
|---|---|
| `measuring-how-private-marks-move-and-propagate.mp4` | 16:9 master, 3840×2160 |
| `vertical/measuring-how-private-marks-move-and-propagate-916.mp4` | 9:16 master, 2160×3840 |
| `*-slate.mp4` | review cuts with beat IDs and running timecode |
| `PEDAGOGY.md` | GATE P — what the author is asked to sign |
| `FACTCHECK.md` | 20 rows; read 6, 9, 18 and 20 |
| `CHECKS-REPORT.md` | PROOF GATE, written before the first compile |
| `BUILD-LOG.md` | decisions, two toolkit defects, and what reading the frames caught |
| `BUILD-PROMPT.md` | the paste-ready prompt that rebuilds both cuts |
| `build_beat_sheet.py` | the injection — every on-screen number, under assertions |

The five figures listed above were used as REFERENCE and rebuilt as native animated scenes
(REBUILD LAW). They now live in `pantry/`, were never slotted as media, and were never copied
into `images/`.

**Two of the four defects this README records are fixed by derivation, not correction.** The
window's levels come from the findings module's own single-linkage clustering rather than a
price threshold — which is what surfaces the two managers sitting *between* the old and new
level — and the dispersion highlight is the measured p90 rather than a constant that happened
to sit near it.

**The build asserts the finding's own falsifier.** B02's claim is that 25% is a result rather
than a threshold choice, so the injection asserts that all three widened definitions stay under
the plan's 30–40% band. If future data pushed one into the band, the build fails rather than
shipping a quieter version of the beat.

**Three places the frames are more careful than the script.** The floor is spoken as Groq's
0.0% rather than OpenAI's 1%, because a 0% bar is on the chart. "Disagreement" is narrowed to
"different prices on the same date", with a whole beat on the reading that is not disagreement.
And the sample-size note names the real extremes — 10 steps to 1,812 — rather than the extremes
of the statistic.
