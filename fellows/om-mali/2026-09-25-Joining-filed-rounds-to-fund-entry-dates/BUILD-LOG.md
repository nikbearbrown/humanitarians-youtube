# BUILD-LOG — joining-filed-rounds-to-fund-entry-dates (week 9)

Built with **brutalist.art** (`ai-explainer`, channel `claude-hai`). Free/local throughout:
Kokoro TTS + Remotion + ffmpeg. **$0.00 spent. No API key used.**

Eighth episode of the Private AI Valuation Agent series (week 1 → 2 → 4 → 5 → 6 → 7 → 8 → 9;
there is no week 3 episode). Fifth episode shipped in both orientations.

**This is a join episode**, and the structure follows from that: two beats of why the obvious
join is wrong, one beat of the mess the second source is actually in, and only then two beats
of what the join bought.

---

## Where the inputs came from

| File | Origin | Status |
|---|---|---|
| `narration_script.md` | Already here | input, unmodified |
| `figdata_week9.json` | Already here — queried from the project database at figure-build time | **the source of truth for every on-screen number**, with three named exceptions |
| `README.md` | Already here — figure-to-beat map, three things not to get wrong, the exposure-figure defect | input, appended with a pointer to the built reel |
| `pantry/w9-*.png` + `.svg` | Were loose in the folder root | **moved to `pantry/`** — the series keeps reference art there, and `run.sh` uses `images/` for compile OUTPUT |
| `lock_durations.py`, `make_vertical.py` | Copied from week 8 | unchanged; `make_vertical.py` already matches `W\d[A-Za-z]+` patterns generically |

---

## Every number is injected, and these groups are asserted

```
form_d: quarters_scanned == 49, rows == 706
by_class: pooled 595 + candidate 111 == 706, and 595/706 == 0.8428
pooled_rows > candidate_rows * 5           <- the FRAMING assertion
lots 249, position_cost 227, fund_cost 22, and 227 + 22 == 249
exactly ONE filer has fund_cost > 0 and position_cost == 0
entry_vs_mark: 7 rows, exactly 3 with first_entry < first_mark
earliest first_entry == "2015-01-20"
corroboration: dates_in_window 18, hits["0"] 10, and the 18 pairs[] rows
  contain exactly 10 with gap_days == 0
the Databricks row: gap_days 0, registrants 5   (found by company+date, not by index)
dates_outside_window sums to 12, and 10 / (18 + 12) == 0.3333
exposure: 90 rows, 30 managers, 10 companies
```

**The framing assertion is the load-bearing one.** B02's claim is that a name scan is
*overwhelmingly* wrong, and B03 derives the join key from that. If a future data change made
feeders merely a plurality, the build fails rather than shipping a beat whose framing had
quietly gone stale while its arithmetic still held. This is the same shape as week 8's widening
assertion: it protects an argument, not a number.

**Two more protect corrections made during this build.** The three-of-seven reach-back count is
asserted, because the source figure was titled as though all seven reached back. And the
Databricks corroboration row is looked up by company and date rather than by position in the
array, so a reordering of the data cannot silently put a different case on screen under the
Databricks caption.

`python build_beat_sheet.py --check` runs the assertions and writes nothing.

---

## Three values that are NOT in the figure data

`figdata_week9.json` carries filer counts, lot counts and date sets. It does not carry:

| Constant | Value | Used by |
|---|---|---|
| `XAI_COLLISION` | the 2014 filer that normalises to the same string as X.AI | B03 |
| `LAYOUT_COUNT` | four tables, one with no table, a sixth that needed no new code | B04 |
| `DBX_ROUND_USD` | the $400M Databricks reported selling in October 2019 | B07 |

All three come from `narration_script.md` and the filings behind it. Each is a named constant
at the top of `build_beat_sheet.py` rather than a string typed into a beat, and **each beat that
uses one says so in its on-screen source line** rather than citing a file that does not contain
it. `FACTCHECK.md` rows 6, 9 and 18.

Row 6 carries weight beyond attribution: the collision is the evidence that no better string
normalisation would have fixed the join, which is the entire justification for a human
confirming each identifier. If it is not real, B03 needs rebuilding rather than rewording.

---

## Decisions taken during the build

| # | Decision | Why |
|---|---|---|
| 1 | **Six script sections → eight body beats.** | The 0:35 section carried two different arguments (a name scan is mostly wrong; no normalisation rescues it) and the 1:55 section named two figures. Both splits give each argument its own frame. The denominator caveat was promoted from a sentence inside the corroboration section to the closing body beat. |
| 2 | **B05 shows all seven companies and accents only the three that genuinely reach back.** | The source figure is titled as though all seven predate the panel; `first_entry < first_mark` holds for three. The other four dim to 0.45 rather than disappearing, and the frame states the reason — only the latest annual and semi-annual report per registrant was fetched, so this is a floor on the record. |
| 3 | **B04 names the other 22 lots rather than leaving "227 with a cost" to imply 22 have none.** | They are one filer's, reported at fund level. The injection asserts that exactly one filer reports that way, so the sentence cannot go stale. |
| 4 | **B02 and B04 both draw bars and are separated by B03.** | B02 is ONE bar splitting into two parts, and its argument is the ratio. B04 is ten filers ranked, and its argument is that they are all different. B03 sits between them and looks like neither. |
| 5 | **B05 and B07 share a time-like axis on purpose.** | A viewer who learns in B05 that horizontal distance means time reads B07's stack at the origin immediately. The shapes are opposites, and B06's percentage bars sit between them. |
| 6 | **Greeting rotated to `Tere, HAI`.** | Weeks 1–8 used `Ola`, `Hej`, `Ciao`, `Hallo`, `Salut`, `Ahoj`, `Szia`. Estonian short form; the lexicon never repeats a language. |
| 7 | **Kicker is `Irreducibly Human`.** | GATE L rule 7 — the fixed `claude-hai` series name. Set at authoring time, so GATE L passed on the first run for the seventh episode running. |
| 8 | **`JoiningFiledRounds.tsx` is self-contained.** | Same reasoning as weeks 2, 4, 5, 6, 7 and 8: reel-local files duplicate the chrome helpers so the earlier signed masters stay re-renderable byte-identically. |

---

## Defects found by READING frames, and fixed

The visual gate checks edge bleed, canvas fill and contrast. Everything below was found by
looking at the rendered frame, which is the only method that has ever caught this class.

| Beat | Defect | Fix |
|---|---|---|
| B01 | **The join-key chip rendered as an empty outline.** "AND THE JOIN KEY IS NOT" was followed by a bordered pill with no text in it. | The prop was named `key`. **React strips a prop called `key` before it reaches the component**, so `props.key` was `undefined` — silently, with no error from tsc, from the zod schema, or from the gate. Renamed to `joinKey` in the schema, the component and the beat sheet. |
| B01 | The footnote read "It is an EDGAR identifier a person has confirmed. **B02 is why.**" | A beat ID is a production label a viewer has no way to resolve. Changed to "Next: why a name cannot work." |
| B01 | Two cards and three short lines left a band of cream through the middle of a 4K frame. | Fixed twice. The first attempt gave the card row `flex: 1`, which grew two four-line cards to half the frame with a void inside them — worse than the gap it closed, and only visible by re-reading the re-rendered frame. The cards stay content-sized and a little roomier, and `Stage`'s `space-between` distributes the rest. |
| B04 | Every row printed its own lot count **twice** — "104 · 104 with a position cost". | The note column says WHERE the cost sits, not how many there are: "with a position cost" / "at fund level". |
| B04 | The layout list read 4 · 1 · 1 under a title saying **five** ways, summing to six. | The third row is `+1`, and `count` became a string so it can be. It is a sixth fund family whose footnote one of the four table parsers already handled. |
| B04 | **Two rows read `BlackRock` and `BLACKROCK`** — 14 lots and 10 — which looks like a duplicated row. | It is real: these groups are keyed on a case-sensitive name prefix. **Left exactly as filed**, with a line on the frame saying so. Merging them would have meant typing 24 into a reel about why name keys fail. |
| B05 | The source line said which rows reach back is "derived, **not asserted**". It *is* asserted — `len(REACH_BACK) == 3`. | Corrected to "derived from the dates, and asserted". A source line that understates its own guarantee is still a source line that is wrong. |
| B05 | "Space Exploration Tech…" truncated in the row label while the same name was spelled in full in the summary line lower on the **same frame**. | `LABEL_W` 250 → 330. |
| B06 | **"1791.81% of a fund's net assets" on a 4K frame.** Also 1585.88%, 744.94%, 696.65%. A percentage of net assets cannot exceed 100. | `max_pct_net_assets` arrives from `figdata_week9.json` **already as a percent** — 17.918 means 17.9%. The component multiplied it by 100. Every geometric check passed on every one of those frames. |
| B06 | "Space Exploration Techno…" clipped on three of the eight rows. | `CO_W` 280 → 420. Clipping is the fallback, not the layout. |
| B07 | **The caveat's rule was drawn straight through the last line of the WHY block.** `Stage` is `space-between` with every child `flexShrink: 0`, so an over-full column overlaps rather than scrolling. | Took two passes: `f(180, 200)` → `f(140, 170)` did not clear it, because the new chart note added back exactly the height the chart gave up. `f(104, 140)` plus a tighter case card does. Same failure mode as weeks 6 and 7. |
| B07 | The lone **dark** dot on top of the zero stack read as a colour glitch. | It is a 1-day gap, not an eleventh zero. Named on the frame, with the index derived from the data and asserted so the sentence cannot drift. |
| B07 | The caveat rendered "What it is not is circular **--** neither filing cites the other." | `figdata` stores an ASCII double hyphen. Normalised to an em dash at injection — typography only, the recorded wording is unchanged. |
| B07 | **The stack at the origin drew ten zeros as five dots and a smudge.** Only visible after the chart was shortened to fix the overlap above. | `DotField` clamped every row past the top edge to the same `y`, so a stack taller than its box silently collapsed into itself. It now measures the tallest column first and tightens the pitch until the whole stack fits. The stack IS the beat's argument, so a chart that cannot hold it is not a smaller chart, it is a wrong one. |

### Four portrait beats were the landscape chart shrunk, not a portrait layout

Found the same way — by reading the 9:16 frames, after both orientations had rendered and
before either compiled. GATE V passed all of them; none is a defect it can see.

| Beat | What the portrait cut actually was | Fix |
|---|---|---|
| B05 | Seven rows at a 38px pitch filled **266 of 1728** safe pixels. The chart sat as a strip in the middle of a mostly empty frame. | Row height 38 → 78, label column 175 → 230, type 17 → 24, and the right-hand reserve widened to hold the ISO date column at its portrait size. |
| B07 | The ten-dot stack at the origin was a sliver. The landscape height was carried over unchanged into a frame with far more room. | Field height 140 → 300 and dot 10 → 26, so the ten zeros and the 1-day gap above them read at a glance. |
| B06 | Ninety-row table rendered at 17px in a 580-of-972-wide block — a thumbnail of the landscape table. | Columns 150/160/96 → 208/250/128, bar 150 → 232, type 17 → 22. |
| B04 | Ten filer rows at a 2px gap, bars 230px wide. | Row gap 2 → 10, label 120 → 200, bar 230 → 330, type 16 → 21. |

The series has said since week 5 that the vertical cut is *a re-layout, not a crop*. These four
were neither: they were the landscape composition scaled down. The `f(landscape, portrait)`
helper makes that failure easy — a portrait value that was never tuned is still a **valid**
portrait value, and nothing fails. The only check is reading the frame.

### Three errors in this build's own paperwork, caught by the frames

Written before the frames existed, and corrected against them rather than left to stand:

- `PEDAGOGY.md` and `CHECKS-REPORT.md` claimed terracotta marks "the honest denominator" on
  B08. The frame accents the **56%** card, and the narration declares neither reading correct —
  it says only that the denominator is doing the work. Both documents now say that.
- `PEDAGOGY.md` said B09 "carries the Week 10 forward statement". It does not; the frame is five
  findings and nothing else. The next-week line lives in `description.txt`.
- `CHECKS-REPORT.md`'s B04 row described the ten filers without the case-split; it now matches
  what is on the frame.

## What the visual gate could not have caught, in this episode

Eight episodes of evidence now. The gate cannot see overlap (weeks 1, 4, 6, 7, 8), cannot tell
whether a number on screen is the RIGHT number (weeks 5, 7, 8), cannot tell whether a source
line cites a file containing the claim (week 6), and cannot tell whether a caption describes
the chart beneath it (week 8). This week adds a new one:

**It cannot tell an empty element from an intentionally empty element.** B01's join-key chip
was a correctly sized, correctly coloured, correctly positioned bordered pill containing
nothing. Every geometric check passed. The beat was missing its most important word.

And it cannot tell an **impossible** number from a real one. B06 rendered "1791.81% of a fund's
net assets" in well-formed, well-contrasted, correctly laid-out type. A percentage of net assets
cannot exceed 100, and nothing in the toolkit noticed. This is the third episode in a row where
the number on screen, not the layout, was the defect.

---

## Two toolkit defects found and fixed

Both reach outside users on Windows, and neither is specific to this reel.

1. **`compile.py` died on its own success message.** `UnicodeEncodeError: 'charmap' codec can't
   encode character '←'`. GATE L had passed, all twelve beats had compiled, and the script
   crashed printing `[art] compiled B01 VIDEO 17.8s ← B01.mp4` to a cp1252 console. `beat_lint.py`
   was already mojibaking its check mark in the same run. This is the same class as the twenty
   read/write sites fixed in week 5, but on **stdout** rather than file I/O. Nineteen scripts
   under `runtime/scripts/` and `runtime/qc/` now reconfigure stdout and stderr to UTF-8 with
   `errors="replace"`; every one that prints a non-ASCII glyph is covered.

2. **The skin lint cried wolf on every 9:16 compile.** `B00: palette=claude but the cold open is
   'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk`. A portrait cut registers the
   same component under a `916` suffix, so the law was satisfied and the lint could not tell.
   It has fired on every vertical compile since week 5, which is precisely how a reader learns
   to scroll past lint output. The check now strips the suffix before comparing.

## The recurring toolkit footgun, again

`remotion_scenes.py` loads the beat sheet at the START of a run and rewrites it at the END, so
any edit made during a 25-minute render is silently lost. It has cost an edit in every episode
since week 5. Edits made during this build's landscape render were re-applied afterwards by
re-running `build_beat_sheet.py` and `lock_durations.py`, both of which are idempotent.

---

## What shipped

| Artifact | Spec |
|---|---|
| `Mycroft_OmMali_25_09_2026.mp4` | 3840×2160, 24fps, 217.45s — the clean 16:9 master |
| `vertical/joining-filed-rounds-to-fund-entry-dates-916.mp4` | 2160×3840, 24fps, 217.45s |
| `joining-filed-rounds-to-fund-entry-dates-slate.mp4` | 16:9 review cut, beat IDs + timecode |
| `vertical/joining-filed-rounds-to-fund-entry-dates-916-slate.mp4` | 9:16 review cut |
| `mp4/` | all four under their canonical slug names |

**GATE L clean. GATE V clean on BOTH cuts** — 24 frames sampled each, 0 BLOCKER, 0 MAJOR.
GATE F never triggered: there are no Manim beats. **GATE P is signed** — `PEDAGOGY.md` carries
`VERDICT: PASS`, signed by the author (Om Mali) on 2026-09-25, and the Kokoro gate was re-run
without `--no-gate` afterwards to confirm it passes on its own. The audio was not regenerated
after signing, so the masters are the same cut GATE V cleared.

The `illustrate carries 8/12 beats (66%)` warning is expected and unchanged since week 2: all
eight body beats illustrate, which is what ILLUSTRATE LAW asks of an `ai-explainer` reel.

## Cost

`$0.00`. Kokoro TTS runs locally from a downloaded model; Remotion and ffmpeg are local. No
API key was used at any point, and no step asked for one.
