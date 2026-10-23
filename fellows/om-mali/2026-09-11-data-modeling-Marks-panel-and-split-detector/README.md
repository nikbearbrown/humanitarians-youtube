# 2026-09-11 - Building the price panel and the stock-split detector

**Week covered:** 2026-09-07 - 2026-09-13

**Video:** [Mycroft_OmMali_11_09_2026.mp4](https://drive.google.com/drive/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv)

**Process log:** [FRICTIONAL.md](./FRICTIONAL.md)

## Result

The Private AI Valuation Agent works out a per-share price for private companies such as Anthropic, OpenAI, SpaceX and Databricks, using the quarterly reports that US mutual funds are required to file with the SEC: a fund must disclose what a holding is worth in dollars and how many shares it owns, and dividing one by the other gives a price for a company that has no share price.

This week built that price table, and the safeguard that stops a stock split
from being mistaken for a price crash.

- **5,479 prices were produced**, one per company, fund and reporting date. The
  totals reconcile exactly against the filings they came from, and a test
  enforces it.
- **The split detector failed on the one case it was written for, while
  appearing to work.** It was tuned to spot share counts changing by a clean
  multiple; the case in question changed by 11.93 times, which it missed
  entirely. It looked correct only because a second case happened to land on
  exactly 10.
- **That 11.93 turned out to be two events at once** — a 10-for-1 split *and* a
  16% write-down in the same period. Correcting by 11.93 would have erased a
  real price movement, which is the opposite of what the detector exists to
  prevent.
- **All three suspected splits were decided by a person, using share counts
  rather than prices.** In the confirmed split the share count multiplied by
  exactly ten while the dollar value stayed identical to the cent. In a case
  that only resembled one, the fund held the same 89,078 shares across thirteen
  reporting periods and the change reversed the following quarter — and splits
  do not reverse.
- **What the detector measured and what a person decided are stored in separate
  columns**, because a measurement and a judgement are different claims.
- **A bug in this week's own code cost the reviewer a repeat.** A value typed
  on the command line was accepted and never saved. It was fixed at the cause
  and covered by tests that would have caught it.

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
