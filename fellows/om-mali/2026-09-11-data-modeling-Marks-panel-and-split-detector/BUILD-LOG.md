# BUILD-LOG — building-the-marks-panel-and-the-split-detector (week 7)

Built with **brutalist.art** (`ai-explainer`, channel `claude-hai`). Free/local throughout:
Kokoro TTS + Remotion + ffmpeg. **$0.00 spent. No API key used.**

Sixth episode of the Private AI Valuation Agent series (week 1 → 2 → 4 → 5 → 6 → 7; there is
no week 3 episode). Third episode shipped in both orientations.

---

## Where the inputs came from

Everything arrived in this folder already — script, figure data, and five rendered figures
with their SVG sources.

| File | Origin | Status |
|---|---|---|
| `narration_script.md` | Already here | input, unmodified |
| `figdata_week7.json` | Already here — queried from the marks panel at figure-build time | **the source of truth for every on-screen number but one** |
| `README.md` | Already here — figure-to-beat map, the two things not to get wrong, the four corrections | input, appended with a pointer to the built reel |
| `pantry/w7-*.png` + `.svg` | Were loose in the folder root | **moved to `pantry/`** — the series keeps reference art there, and `run.sh` uses `images/` for compile OUTPUT |

---

## Every number is injected, and fourteen groups are asserted

`build_beat_sheet.py` reads `figdata_week7.json` directly; no figure is typed into a scene or a
beat sheet by hand. The assertions run at injection and fail the build if violated:

```
5806 − 28 − 72 == 5706 == coverage.lines_in_marks    # and B02 performs this on screen
totals.marks == 5479
blocks[] sums to totals.blocked == 301
exactly ONE block reason is the confirmed split, holding 7 marks
priced + unpriceable(294) == marks    # the 7 split marks are priced but held out
tolerance == 0.01                     # RELATIVE, the rule that ships
7 quarantine rows, all adjudicated, every note carries the reviewer's name
3 distinct companies; BOTH verdicts present
the COM row: ratio 11.9300, factor 10.0000 — and they DIFFER
perplexity: shares ×10, value identical at "13488132.50", still carrying decimals
anthropic: ONE share count across 13 rows, and the step REVERSES next quarter
spacex: constant shares, value exactly doubled
checks: 7 total, 6 True, 0 False, 1 None — counted, never typed
agreement.families == 10 == sum(clusters)
```

Four of these exist because the README records the figure being wrong until it was built: the
evidence figure quoting the smallest position rather than the largest, a value rounded in a way
that flattered "the same dollars", red used as a warning colour, and a title hardcoding "0 fail"
while its own table disagreed. The check counts are now **computed** (`passed is True/False/
None`), so the title cannot drift from the rows again.

`python build_beat_sheet.py --check` runs the assertions and writes nothing.

---

## The one number with no artifact behind it

`figdata_week7.json` carries the tolerance that **ships** — a relative 1% window. It does not
carry the **old** absolute window, ±0.02. That comes from `narration_script.md` and `plan.md`.

It is passed into the build as a named constant `OLD_WINDOW` rather than smuggled into a
string, and B04's on-screen source line says where it came from instead of citing a file that
does not contain it. This matters beyond bookkeeping: B04's "missed by a factor of three" is
0.07 ÷ 0.02, so if the old window was not 0.02 the beat's headline number changes with it.
`FACTCHECK.md` row 9 is the row to read; row 12 is the one that depends on it.

That attribution habit came out of week 6, where two source lines cited figdata for claims it
did not contain.

---

## Decisions taken during the build

| # | Decision | Why |
|---|---|---|
| 1 | **Six script sections → eight body beats.** | Two sections carried two ideas each: the stakes AND the bug (0:55), the evidence AND the judgment (1:35). Split at those seams. |
| 2 | **The bug gets its own beat, and so does the judgment.** | The script's note names "catching it is not deciding it" the strongest beat; it cannot be that while sharing a frame with a three-row table. Likewise B03 exists so a viewer feels why a detector is worth a week before B04 shows mine failing. |
| 3 | **The reconciliation paragraph was KEPT.** | The script offers it as the first cut, calling it "the least visual claim". B02 makes it the most visual thing in the beat — the subtraction is performed on screen — so the reason for cutting it does not apply. |
| 4 | **"Three looked like splits" → "three companies threw one".** | The data holds 7 quarantined series across 3 companies. "Three" alone would contradict the 7 on screen at B02. |
| 5 | **B03 and B05 name their security class.** | They are two different Perplexity securities — ARK's common line (ratio 11.93) and T. Rowe's preferred line (ratio exactly 10, the ×10 share evidence). The script says "Perplexity" for both. The frames do not. |
| 6 | **The ten-managers line gained its clusters.** | "Ten do" is true but implies exact agreement. They sit in two clusters 0.0036 apart — the same price to the cent, rounded differently by different filers. That is the more interesting fact and it is in the data. |
| 7 | **Terracotta marks the CORRECT divisor at B07.** | README correction 3: red was misused as a warning colour, which `DESIGN.md` forbids. Preserved throughout — the accent marks the right answer, the human-held marks, and the measured result that beat its expectation. Never a mistake. |
| 8 | **Greeting rotated to `Ahoj, HAI`.** | Weeks 1, 2, 4, 5, 6 used `Ola`, `Hej`, `Ciao`, `Hallo`, `Salut`. Czech short form; the lexicon rotates so the series never repeats a language. |
| 9 | **Kicker is `Irreducibly Human`.** | GATE L rule 7 — the fixed `claude-hai` series name. Set at authoring time, so GATE L passed on the first run for the fifth episode running. |
| 10 | **`MarksPanelAndSplitDetector.tsx` is self-contained.** | Same reasoning as weeks 2, 4, 5 and 6: reel-local files duplicate the chrome helpers so the earlier signed masters stay re-renderable byte-identically. |

---

## Both orientations, from one source

**16:9 at 3840×2160 and 9:16 at 2160×3840**, on the machinery weeks 5 and 6 established.

The vertical cut is a **re-layout, not a crop.** Every week-7 component reads its orientation
from `useVideoConfig()` and every value that differs goes through `f(landscape, portrait)`.
B07's decomposition runs across in landscape and downward in portrait; B05's three-column rows
become stacked blocks; B04's number line narrows and drops its second label onto its own row.
Both orientations render from the **same component and the same props**, so a number cannot
differ between the two masters, and they carry the identical narration MP3s.

---

## Visual QC — what LOOKING at the frames caught

GATE V reported **0 BLOCKER, 0 MAJOR** on the first pass and on every pass after. Reading the
frames found seven defects it could not see, two of which put a wrong claim on screen.

| Beat | Defect | Severity | Fix |
|---|---|---|---|
| B01 | The card read **"232 securities × 55 period ends × 10 companies"** under a headline claiming 5,479 marks. That product is 127,600 — the dimensions are not multiplicative, because a mark exists only where a fund actually filed that security in that period | **MAJOR — arithmetic the frame invites and cannot survive** | Listed, never multiplied: "across 232 securities, 55 period ends, 10 companies". |
| B01 | "3 suspected splits found, 3 it could not classify" read as a contradiction | MAJOR | "3 companies threw a suspected split — the ratio classifies none of them". |
| B02 | The FootNote rule was drawn across the block-reason list; the 5% terracotta segment's label wrapped onto four lines; and the raw reasons read as a stutter (`not a share price: not_a_share_price`) | **MAJOR, missed by GATE V** | Labels moved to the bar ends with `space-between`, list given `marginBottom`, and the machine token set apart in ghost mono so both halves survive without repeating. |
| B08 | Same FootNote-rule collision, across the cluster note | **MAJOR, missed by GATE V** | `marginBottom` on the agreement block. |
| B04 (portrait) | The two axis labels **overprinted each other**. They are positioned by value, and the portrait axis is 900px instead of 1500, so 11.93 and 12.00 sit close enough to collide | **MAJOR, portrait only, missed by GATE V** | Portrait drops the measured ratio onto its own row beneath the whole-number label. |
| B03 | The subtitle read **"Perplexity AI, Inc. · Perplexity AI, Inc."** — company and security title are the same string in this row | MINOR | Names the class instead, which also keeps it distinct from the preferred line B05 uses. |
| B04, B07 | `11.9300` on screen while the narration says "eleven point nine three" | MINOR | Two decimals where the number is spoken; four only where the stored field is the subject. |

**GATE V's blind spot, five episodes running.** The gate checks edge bleed, canvas fill and
contrast. It does not check whether one element is drawn on top of another (weeks 1, 4, 6, 7),
it cannot tell whether a number on screen is the right number (weeks 5, 7), and it cannot tell
whether a source line cites a file containing the claim (week 6). A clean report is not
evidence that the frames are correct — this week it was clean while a frame invited a
multiplication that gives 127,600 instead of 5,479.

---

## Toolkit state

No new toolkit defects surfaced. Added for this reel:
`runtime/remotion/src/MarksPanelAndSplitDetector.tsx` (eight components, registered twice each)
and its folder in `Root.tsx`. Nothing else in the toolkit was modified.

**The known footgun bit again**, as it has every week since week 5: `remotion_scenes.py` loads
the beat sheet at the start of a run and rewrites it at the end, so beat-sheet edits made
during the 25-minute landscape render were silently overwritten. Recovered by re-running
`build_beat_sheet.py` and `lock_durations.py`, both idempotent.

---

## Gates

| Gate | State |
|---|---|
| **FACTCHECK** | 20 rows, all traced. **Rows 9, 12, 18 and 20 flagged** — the old ±0.02 window having no artifact behind it, the "factor of three" that depends on it, the adjudication requirement, and the agreement clusters. |
| **PROOF GATE / CHECKS-REPORT** | PASS — 8 SHOW / 4 justified-HOLD / 0 PUNT. Teaching arc 6/6. Written before the first compile. |
| **GATE P (pedagogy)** | **PASS — signed by the author (Om Mali), 2026-09-11**, after reviewing the slate cuts. Covers the three structural splits, keeping the reconciliation paragraph, the four wording changes, FACTCHECK rows 9/12/18/20, the B10 handoff prompt, and the dual-orientation build. Audio for the pre-signature review cut was generated with `--no-gate`, recorded here rather than passed silently; the gate was re-run WITHOUT the override after signing and passes on its own. |
| **GATE L** (beat-mix lint) | PASS on the first run. |
| **GATE V** (frame-level visual QC) | PASS on BOTH masters, re-run against the 4K files themselves rather than the review cuts — 16:9: 24 frames, 0 BLOCKER, 0 MAJOR. 9:16: 24 frames, 0 BLOCKER, 0 MAJOR. |
| **GATE F** | Not triggered — no Manim beats. |

**One advisory, not a gate.** `compile.py` warns that `illustrate` carries 8 of 12 beats (66%)
against a ~40% cap written for reels built from pantry media. Every body beat here is a native
animated Remotion scene with its own scheme. Weeks 2, 4, 5 and 6 carried the same shape.

---

## Build facts

- **12 beats**, all filled by Remotion. Zero slates.
- **Audio**: Kokoro `am_onyx` (the fellow's persistent voice, unchanged since week 1),
  **214.52s narration + 0.40s lead (3:34.9)**. The same mp3s drive both orientations.
- **Eight reel-local scenes**, eight different visual schemes, each laid out natively at both
  1920×1080 and 1080×1920. No two consecutive body beats share a scheme (ILLUSTRATE LAW).
- **Body beats 48–69 words** — all eight inside the 45–70 band.
- **The spine of the episode is the author's own bug**, measured on a number line rather than
  confessed in a sentence — and the beat also shows why it looked fine, which is the part
  worth keeping.
- **Never published.** The masters stay in this folder. Publishing is a separate, explicitly
  human-authorized step that this toolkit does not perform.

---

## Finalization (2026-09-11)

GATE P signed. Four things before the masters were stamped:

1. **The signature was attributed.** It arrived as a bare `VERDICT: PASS`; the line now carries
   the author and the date, and the `--no-gate` disclosure survives beneath it.

2. **Staleness proved per BEAT, not per file — and one beat was re-rendered rather than
   argued about.** File mtimes flagged 10 of the 24 renders, because the reel-local scene file
   was edited after them. That edit was the portrait label separation in `W7Tolerance`, which
   changed only PORTRAIT arguments of `f(landscape, portrait)`, so most flags were false. Each
   flagged beat was re-rendered as one still from the current source and diffed against the
   shipped frame at native 4K, with **controls** — two beats known to be current — setting the
   noise floor at 0.017%–0.313% differing pixels.

   Nine of the ten landed inside that band. **16:9 B08 came in at 0.512%, just above it.** It
   is the densest frame in the reel, so density rather than change is the likely explanation —
   but "likely" is not a standard to ship a signed master on, and re-rendering one beat costs
   three minutes. It was re-rendered. No further analysis was spent on it.

3. **GATE P re-run without the override.** `generate_audio_kokoro.py --dry-run` passes the
   PEDAGOGY check on its own. `--dry-run` deliberately: regenerating the audio would shift the
   measured durations by milliseconds and invalidate every render timed against them.

4. **`mp4/` refreshed by hand.** `./art final` writes only the master, so the mirrors go stale
   every week — the same step weeks 1, 2, 4, 5 and 6 needed.

GATE V was re-run against the two 4K masters themselves: **24 frames each, 0 BLOCKER,
0 MAJOR.**
