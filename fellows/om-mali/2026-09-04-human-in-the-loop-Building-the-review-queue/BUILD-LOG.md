# BUILD-LOG — building-the-human-review-queue (week 6)

Built with **brutalist.art** (`ai-explainer`, channel `claude-hai`). Free/local throughout:
Kokoro TTS + Remotion + ffmpeg. **$0.00 spent. No API key used.**

Fifth episode of the Private AI Valuation Agent series (week 1 → 2 → 4 → 5 → 6; there is no
week 3 episode). Second episode shipped in both orientations.

---

## Where the inputs came from

Everything arrived in this folder already — script, figure data, and five rendered figures
with their SVG sources. Nothing was fetched from the Mycroft repo.

| File | Origin | Status |
|---|---|---|
| `narration_script.md` | Already here | input, unmodified |
| `figdata_week6.json` | Already here — queried from the project Postgres at figure-build time | **the source of truth for every on-screen number** |
| `README.md` | Already here — figure-to-beat map, the three corrections, the colour note | input, appended with a pointer to the built reel |
| `pantry/w6-*.png` + `.svg` | Were loose in the folder root | **moved to `pantry/`** — the series keeps reference art there, and `run.sh` uses `images/` for compile OUTPUT |

**Note on the tree.** This reel was built in
`D:/study_other/new_humanitarians/humanitarians-youtube/…`, which is a different root from
weeks 1–5 (`D:/study_other/humanitarians-youtube/…`). The new tree carries the paperwork for
the earlier weeks but not their rendered masters. Nothing was moved or copied between trees.

---

## Every number is injected, and eleven groups are asserted

`build_beat_sheet.py` reads `figdata_week6.json` directly; no figure is typed into a scene or
a beat sheet by hand. The assertions run at injection and fail the build if violated:

```
holdings == decided == 5806              # nothing dropped, nothing pending
auto 4537 + human 1269 == 5806
non-auto triggers sum to the human share
len(review_groups) == 8, cards == 42     # the collapse IS the beat
review_rows == 45
len(split questions) == 3                # NOT four
split cards == 9, split holdings == 925
len(xai_spellings) == 24, holdings == 278
duplicate issuer names EXIST in xai_spellings
perplexity: balance x10, value_usd identical at 4228993.75
spacex_same_day: EC and EP on the SAME period_end
rejected holdings == 28                  # the canary
```

Three of these exist because the README records the PROSE being wrong until the figures were
generated: four split questions instead of three (and so "wrong three times out of four"
instead of two out of three), Perplexity's unchanged value rounded to the dollar, and the
X.AI list missing the security titles that separate three otherwise-identical rows. The
`WRONG_OF` string on screen is **derived from the asserted question count**, so the corrected
ratio cannot drift back even if someone edits the narration.

`python build_beat_sheet.py --check` runs the assertions and writes nothing.

---

## Decisions taken during the build

| # | Decision | Why |
|---|---|---|
| 1 | **Six script sections → eight body beats.** | Three sections carried two ideas each: the repetition AND the company-level key (0:55), the designed durability test AND the accidental one (1:30), the Perplexity split AND the two look-alikes (2:00). Split at those seams. |
| 2 | **The crash got its own beat.** | The script's note names it the strongest beat. A beat sharing a frame with a systems diagram is not the strongest anything, so B05 is the mechanism and B06 is the accident. |
| 3 | **The script's own cut was taken.** | The note offers the second opening paragraph as the first cut — "the project gets re-explained every week". One clause survives in B00. It is the only content dropped. |
| 4 | **The exact 4,537 is spoken, not "four and a half thousand".** | The precise figure is short enough to say and it is the one on screen; a round number beside a precise one invites the viewer to find the mismatch. |
| 5 | **"Three price steps looked identical" was dropped.** | See the QC table below — this one was caught by reading the render. Two steps are ×10; Anthropic's is ×4.0. |
| 6 | **B01 is built around a subtraction.** | The README calls "the AI decided nothing" the one thing not to get wrong on camera. Rather than a disclaimer, it is the shape of beat one: `route`, `group`, `present` land as chips and `decide` lands and is struck through. |
| 7 | **Greeting rotated to `Salut, HAI`.** | Week 1 `Ola`, week 2 `Hej`, week 4 `Ciao`, week 5 `Hallo`. French short form; the lexicon rotates so the series never repeats a language. |
| 8 | **Kicker is `Irreducibly Human`.** | GATE L rule 7 — the fixed `claude-hai` series name, and unusually apt this week. Set at authoring time, so GATE L passed on the first run for the fourth episode running. |
| 9 | **`BuildingTheHumanReviewQueue.tsx` is self-contained.** | Same reasoning as weeks 2, 4 and 5: reel-local files duplicate the chrome helpers so the earlier signed masters stay re-renderable byte-identically. |

---

## Both orientations, from one source

**16:9 at 3840×2160 and 9:16 at 2160×3840**, on the machinery week 5 established.

The vertical cut is a **re-layout, not a crop.** Every week-6 component reads its orientation
from `useVideoConfig()`, and every value that differs goes through one helper,
`f(landscape, portrait)`. B05's graph chain runs across in landscape and downward in portrait;
B02's method table goes from five columns to a 3+2 grid; B03's scroller shows 9 taller rows
landscape and 10 in portrait. Both orientations render from the **same component and the same
props**, so a number cannot differ between the two masters.

`make_vertical.py` derives `vertical/beat_sheet.json`, flips `aspect_ratio`, suffixes the slug,
and rewires every `shot.remotion.pattern` to `<pattern>916`. It **refuses to run** if any
pattern lacks a portrait registration in `Root.tsx`. Its registry check was generalised this
week from `W5*` to `W\d*` so it keeps working for later weeks.

The narration mp3s are **copied, not regenerated**, so the two masters are the same edit.

---

## Visual QC — what LOOKING at the frames caught

GATE V reported **0 BLOCKER, 0 MAJOR** on the first pass and on every pass after. Reading the
frames found six defects it could not see, including one that put a wrong claim on screen.

| Beat | Defect | Severity | Fix |
|---|---|---|---|
| B08 | **The narration said the three price steps "looked identical", and the frame labelled them ×10, ×10 and ×4.0.** Anthropic's step is a quarter-on-quarter funding round, not a ten-times move — the script's "a price falling by exactly ten" is true of two of the three | **MAJOR — the reel contradicting itself** | Narration rewritten to what the data supports: three steps *tripped the same detector*. Title, spark line and shot notes follow. B08 re-voiced. Logged in `FACTCHECK.md`. |
| B02 | The FootNote rule was drawn straight through the "97 questions / 68 questions / …" line — the column was over-full, so `space-between` had no space to give | **MAJOR, missed by GATE V** | Method rows compacted to two lines (`alias · 97q`), `flexShrink: 0` on the block, and the standalone 5,806 counter removed — it said the same number the bar's two labels sum to and the footnote states outright. |
| B03 | Same collision, plus the scroller ended 15 rows away from the three shared-issuer-name rows that the narration is *about* | **MAJOR, missed by GATE V** | Scroller pinned with an explicit height and `flexShrink: 0`; the oversized counter block replaced with one inline line; and the scroll now runs down through all 24 for volume and **back to the top**, so rows 1–3 with their security titles are lit when that sentence lands. |
| B05 | The source line cited `figdata_week6.json` for claims that are **not in it** — `interrupt()`, the two-process test | MAJOR (attribution) | Source line now says so: the author's own run log, and the one part of the reel not evidenced by the figure data, pointing at FACTCHECK rows 10–11. |
| B06 | The source line implied the figure data holds a before/after pair. It holds **one** value, 42 | MAJOR (attribution) | Source line now states that the before/after identity is the author's observation of one outage, not two recorded snapshots, pointing at FACTCHECK row 12. |
| B04 | The raw `company` token sat under the company name with no label, reading as an orphaned word | MINOR | Labelled `RECORDED VERDICT`. |
| B03 (portrait) | Rows set at 17px in a 1080-wide comp — legible on a monitor, thin on a phone, which is the point of the vertical cut | MINOR (portrait only) | Fewer, taller rows: 10 at 54px, type up ~20%. |

**GATE V's blind spot, four episodes running.** The gate checks edge bleed, canvas fill and
contrast. It does not check whether one element is drawn on top of another (weeks 1, 4, 6), it
cannot tell whether a number on screen is the right number (week 5), and it cannot tell whether
a source line cites a file that actually contains the claim (week 6). A clean report is not
evidence that the frames are correct.

---

## Toolkit state

No new toolkit defects surfaced. Every UTF-8 fix from week 5 was exercised again and held —
this reel's narration and props contain curly quotes, en dashes and `×`, and nothing crashed.
Added for this reel: `runtime/remotion/src/BuildingTheHumanReviewQueue.tsx` (eight components,
registered twice each) and its folder in `Root.tsx`. Nothing else in the toolkit was modified.

**The known footgun bit again.** `remotion_scenes.py` loads the beat sheet at the start of a
run and rewrites it at the end, so beat-sheet edits made during the 25-minute landscape render
were silently overwritten. Recovered by re-running `build_beat_sheet.py` and
`lock_durations.py`, both of which are idempotent — which is the only reason it costs minutes
rather than a rebuild.

---

## Gates

| Gate | State |
|---|---|
| **FACTCHECK** | 20 rows, all traced. **Rows 6, 12, 18 and 19 flagged** — the "code rejects a decision missing a name or a reason" claim, the accidental crash, the corrected three-not-four split count, and the canary. Two of the four are author assertions about the project's own code and run history, and are labelled as such. |
| **PROOF GATE / CHECKS-REPORT** | PASS — 8 SHOW / 4 justified-HOLD / 0 PUNT. Teaching arc 6/6. Written before the first compile. |
| **GATE P (pedagogy)** | **PASS — signed by the author (Om Mali), 2026-09-04**, after reviewing the slate cuts. Covers the three structural splits, taking the script's own cut, the five wording changes, FACTCHECK rows 6/12/18/19, the B10 handoff prompt, and the dual-orientation build. Audio for the pre-signature review cut was generated with `--no-gate`, recorded here rather than passed silently; the gate was re-run WITHOUT the override after signing and passes on its own. |
| **GATE L** (beat-mix lint) | PASS on the first run. |
| **GATE V** (frame-level visual QC) | PASS on BOTH masters, re-run against the 4K files themselves rather than the review cuts — 16:9: 24 frames, 0 BLOCKER, 0 MAJOR. 9:16: 24 frames, 0 BLOCKER, 0 MAJOR. |
| **GATE F** | Not triggered — no Manim beats. |

**One advisory, not a gate.** `compile.py` warns that `illustrate` carries 8 of 12 beats (66%)
against a ~40% cap. That cap is written for reels built from pantry media, where too much
`illustrate` means too many stills being panned. Every body beat here is a native animated
Remotion scene with its own scheme. Weeks 2, 4 and 5 carried the same shape.

---

## Build facts

- **12 beats**, all filled by Remotion. Zero slates.
- **Audio**: Kokoro `am_onyx` (the fellow's persistent voice, unchanged since week 1),
  **200.63s narration + 0.40s lead (3:21.0)**. B08 was re-voiced once after the ×10/×4.0
  correction. The same mp3s drive both orientations.
- **Eight reel-local scenes**, eight different visual schemes, each laid out natively at both
  1920×1080 and 1080×1920. No two consecutive body beats share a scheme (ILLUSTRATE LAW).
- **Body beats 48–69 words** — all eight inside the 45–70 band.
- **The claim the whole reel is built around is a negative one about the software**: it routed,
  grouped and presented, and decided nothing. That is beat one, not a disclaimer at the end.
- **Never published.** The masters stay in this folder. Publishing is a separate, explicitly
  human-authorized step that this toolkit does not perform.

---

## Finalization (2026-09-04)

GATE P signed. Four things before the masters were stamped:

1. **The signature was normalised.** It arrived as `VERDICT: PASSED`. The machine gate matches
   on the substring `VERDICT: PASS`, so it passed either way, but the line now reads in the
   series' canonical form with the author and date attached.

2. **Staleness proved per BEAT, not per file — using week 5's method, including its controls.**
   File mtimes flagged 10 of the 24 renders, because the reel-local scene file was edited after
   them. That edit was the portrait scroller bump in `W6Collapse`, and it changed only the
   PORTRAIT argument of `f(landscape, portrait)` — so most of the flags were false. Each
   flagged beat was re-rendered as one still from the current source and diffed against the
   shipped frame at native 4K.

   What makes that measurement mean anything is the **controls**: two beats known to be
   current, which scored 0.002% and 0.332% differing pixels. Every flagged beat scored
   0.186–0.443%, inside that band. The spread tracks text density rather than change — the
   0.002% control is the poster-style outro, the 0.332% one is the densest frame in the reel.
   **Nothing needed re-rendering.**

3. **GATE P re-run without the override.** `generate_audio_kokoro.py --dry-run` passes the
   PEDAGOGY check on its own. `--dry-run` deliberately: regenerating the audio would shift the
   measured durations by milliseconds and invalidate every render timed against them.

4. **`mp4/` refreshed by hand.** `./art final` writes only the master, so the mirrors go stale
   every week. The same step weeks 1, 2, 4 and 5 needed.

GATE V was re-run against the two 4K masters themselves: **24 frames each, 0 BLOCKER,
0 MAJOR.**
