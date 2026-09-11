# Week 7 — Building the marks panel and the split detector

Five figures and a 3:00 narration script. The week's work: a per-share price panel computed as
value divided by share count, and a detector that catches stock splits before they enter a
price series as crashes.

| File | Beat | What it shows |
|---|---|---|
| `w7-panel.png` | 0:20 | 5,806 filed holdings → 5,479 marks, and the reconciliation that leaves nothing out |
| `w7-tolerance.png` | 0:55 | The window that missed its own test case: a ratio of 11.93 against ±0.02 |
| `w7-evidence.png` | 1:35 | Three identical-looking steps, separated by the share count |
| `w7-factor.png` | 2:20 | Ratio 11.93 decomposing into a 10:1 split and a 16% markdown |
| `w7-checks.png` | 2:45 | plan.md's seven checks: six pass, one unreachable, none failed |

SVG sources sit beside each PNG. PNGs are 2917 × 1750. `figdata_week7.json` is the measured
data every figure was drawn from.

## Rules

- Every number is queried from the marks panel at build time
  (`scripts/make_week7_figures.py` in the project repo) and dumped to `figdata_week7.json`
  before anything is drawn. No figure carries a hand-typed number.
- Both QA passes were run: `npm run audit:layout` reports **0 errors on all five**, and each
  PNG was read and checked for substance.
- Six palette tokens from `brutalist/DESIGN.md`, nothing else.

## The two things not to get wrong on camera

**The detector was not broken; it was too narrow.** It caught the Perplexity step that lands on
exactly 10.000 and missed the one at 11.93, which is the case `plan.md` itself names. "Too
narrow to catch its own test case" is the accurate phrasing.

**The splits are not adjusted.** They are detected, quarantined and now decided by a named
reviewer. Applying the factor is next month's work, and Perplexity's seven marks are still
blocked from every change series until it happens.

## Four corrections these figures forced

Worth knowing, because each one was wrong until the figure was built:

1. **The evidence figure quoted a different fund than the write-up.** It picked the smallest
   position; the RUN_LOG cites the largest. Now it selects the largest deterministically, so the
   figure and the written record quote the same row.
2. **A value was rounded in a way that flattered the claim.** $4,228,993.75 displayed as
   $4,228,994 while the caption said "the same dollars" — the rounding was doing part of the
   argument. Values now show two decimals.
3. **Red was used as a warning colour**, which `DESIGN.md` forbids: red is the primary series,
   never "danger". The two wrong choices in the factor figure are now secondary and red marks
   the correct answer, which is what the figure is about.
4. **One verification check failed because a human answered it.** It required the Perplexity
   split to be *un*adjudicated, so the adjudication broke the test — it was asserting the
   pre-review state rather than the rule. And the figure's title hardcoded "0 fail" instead of
   counting, so it disagreed with its own table. Both fixed.

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
| `building-the-marks-panel-and-the-split-detector.mp4` | 16:9 master, 3840×2160 |
| `vertical/building-the-marks-panel-and-the-split-detector-916.mp4` | 9:16 master, 2160×3840 |
| `*-slate.mp4` | review cuts with beat IDs and running timecode |
| `PEDAGOGY.md` | GATE P — what the author is asked to sign |
| `FACTCHECK.md` | 20 rows; read 9, 12, 18 and 20 |
| `CHECKS-REPORT.md` | PROOF GATE, written before the first compile |
| `BUILD-LOG.md` | decisions, and what reading the frames caught |
| `BUILD-PROMPT.md` | the paste-ready prompt that rebuilds both cuts |
| `build_beat_sheet.py` | the injection — every on-screen number, under assertions |

The five figures listed above were used as REFERENCE and rebuilt as native animated scenes
(REBUILD LAW). They now live in `pantry/`, were never slotted as media, and were never copied
into `images/`.

**One number in this reel has no artifact behind it.** `figdata_week7.json` carries the
tolerance that ships (relative 1%) but not the OLD absolute window, ±0.02 — that comes from the
narration script and `plan.md`. It is passed in as a named constant and B04's on-screen source
line says so. It matters because "missed by a factor of three" is 0.07 ÷ 0.02, so the headline
number moves with it. See `FACTCHECK.md` rows 9 and 12.

**Two places the frames are more careful than the script.** The 11.93 ratio is ARK's *common*
line; the ×10 share-count evidence is T. Rowe's *preferred* line — two different securities the
script calls "Perplexity" alike, and each beat names its class. And "ten managers agree" is
rendered as two clusters $0.0036 apart: the same price to the cent, rounded differently by
different filers.
