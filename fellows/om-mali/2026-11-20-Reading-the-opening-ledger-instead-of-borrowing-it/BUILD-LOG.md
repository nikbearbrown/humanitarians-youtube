# BUILD-LOG — reading-the-opening-ledger-instead-of-borrowing-it

AI Debt Tracker, **week 6**. Built with `brutalist.art`, skill `ai-explainer`, channel
`claude-hai`. Free/local end to end — Kokoro TTS, Remotion, ffmpeg. **`$0.00`, no API key.**

Gate signed by the author at `PEDAGOGY.md:214` (`VERDICT: PASS`) before any audio existed.

---

## 1. Delivered

| Artifact | Spec |
|---|---|
| `Mycroft_OmMali_20_11_2026.mp4` | **3840×2160**, 24fps, 206.36s — the 16:9 master |
| `vertical/…-916.mp4` | **2160×3840**, 24fps, 206.36s — the 9:16 master |
| `…-slate.mp4` (both) | review cuts, beat IDs + running timecode |
| `mp4/` | mirror of all four |
| `_qc/REPORT.md` (both) | 0 BLOCKER · 0 MAJOR, graded with an explicit `--mp4` |

Twelve beats, zero slates, 692 narration words, body beats 57–65w.
Runtime: body 145.3s · bookends 61.1s · **3:26.4**.

Greeting rotates to **"Bula, HAI"** (Fijian). Kicker is the fixed series name
`Irreducibly Human` (GATE L rule 7). Voice `am_onyx`, unchanged across the series.

## 2. Figure-to-beat map

| Beat | Scene | Drawn from |
|---|---|---|
| B00 | `ClaudeComposerAsk` | the week's instruction; lands ANSWERED |
| B01 | `W6Merge` | `pantry/adt-w6-merge.svg` — both bars re-derive at 6.0 px/bond |
| B02 | `W6Opening` | `docs/opening_reader.md` — code → model → code |
| B03 | `W6Score` | `pantry/adt-w6-opening.svg` — all four bars re-derive |
| B04 | `W6Variance` | FRICTIONAL.md — Broadcom Jan 2025, 36 then 22 |
| B05 | `W6Gap` | `pantry/adt-w6-gap.svg` — all six bars re-derive |
| B06 | `W6Where` | `docs/agent_start.md`, DESIGN.md P60 |
| B07 | `W6Catch` | `pantry/adt-w6-catch.svg` — all three bars re-derive |
| B08 | `W6Limits` | narration_script.md notes · FRICTIONAL.md |
| B09 | `ClaudeVerdictArtifact` | recap of the five findings |
| B10 | `ClaudeComposerAsk` | HANDOFF LAW |
| B11 | `ClaudeTitleOutro` | OUTRO LAW |

Scenes live in `runtime/remotion/src/ReadingTheOpeningLedger.tsx`, registered twice in
`Root.tsx`. Ids `W6Merge/W6Opening/W6Score/W6Variance/W6Gap/W6Where/W6Catch/W6Limits`
deliberately avoid the Private AI Valuation series' `W6Bluf/W6Collapse/W6Crash/…` —
**a composition id collision is silent.**

## 3. What the build asserts

The framing assertion has **two halves** and both must hold:

```
oracle recall >  B0 recall       97.9% >  90.9%
agent  recall <= B0 recall       90.1% <= 90.9%    <- the retraction
```

Week 5 reported +7.0 points of recall over doing nothing. That number depended on every
quarter being handed an opening ledger copied from the answer key. Reading its own start,
the agent lands **level with doing nothing**. If the agent ever pulls ahead of B0 on recall
the build fails, because B00 and B05 would be announcing a cost that did not land.

Also asserted: precision rises and stays within a point of B0 ("level", never "better");
the reader's recall gain exceeds its precision gain; `graded_on 43 < reports_read 94`;
the two variance runs differ; `21+25+4 != 26` (actions, not a breakdown); caught < missed;
`agent 26 < oracle 44 < 79`.

## 4. Three traps caught before the first render

1. **A denominator trap.** README says "On 94 reports it found 89.7%"; the figure's own
   source line says `GRADED AT L1, 43 REPORTS`. **Both denominators now ride on B03.**
2. **A conflation trap.** The merge figure's 21 + 25 + 4 are *actions*, not a breakdown of
   the 26 (week 5's 26 split 10/10/4/2). 21+25+4 = 50. An assertion makes them
   unrelabelable and the frame says so in a line beneath them.
3. **A conflict between two of the author's own files.** `FRICTIONAL.md` breaks the 21
   settled questions down as 19+2; `description.txt` as 17+2+2. **No breakdown is drawn on
   any frame.** FACTCHECK row 22 — still open, still the author's call.

## 5. Visual QC — eight defects GATE V passed

Every one was found by **reading frames at 0.95 of each beat's own duration**, not by the
gate and not by the mp4 probe.

| # | Beat | Defect | Cause |
|---|---|---|---|
| 1 | B01 | `b0's opening ledger` | `str.capitalize()` uppercases the first char and **lowercases the rest**, folding figdata's correct `B0's` |
| 2 | B01 | "not better" twice in one sentence | verdict and interval strings both ended with it |
| 3 | B02 | sparkline repeated the rule block **verbatim** | two correct strings, wrong together |
| 4 | B02 | "(Not measured in figdata.json **that it was deliberate** —…)" | `NOT_IN_FIGDATA` spliced mid-sentence |
| 5 | B04 | header subtitle and bracket caption **identical** | `W6Variance` rendered `subtitle` in both slots |
| 6 | B06 | "Most of the 7.9 points **sits**" | subject/verb |
| 7 | B06 | **underfilled** — ink 0.041 vs 0.070–0.129 for every other body beat | four short rows at body-copy size; three dead bands >100px |
| 8 | B09 | "a **paired** cost of … , **paired**, …" | `GP['cost']` already contains the word |

**#7 is the documented bbox blind spot.** GATE V's `underfill` measures
`bbox_area / safe_area`, so B06's content touching all four edges scored **1.00** while the
middle of the frame was empty. Caught by measuring ink fraction per frame and comparing
across beats — a frame that is thin *relative to its siblings* is the signal, not an
absolute threshold.

Fixes: a `sentence_case()` helper replacing `.capitalize()`; a new `bracketLabel` prop on
`W6Variance`; `W6Where` landscape type scaled up (names 27→36px, text 25→32px, row rhythm
14→30px) with **portrait deliberately untouched**, since portrait was already tight.
B06 landed at 0.052 — still the thinnest beat, because it genuinely carries the least
content, and padding it further would have meant inventing.

## 6. The skip trap, carried from week 5

`remotion_scenes.py` **SKIPS** any beat whose `media/<BID>.mp4` already exists and prints
`filled already (skip)`. In week 5 two full re-render cycles were no-ops for exactly this
reason, and GATE V re-graded the untouched video and called it clean.

Every render in this build passed **`--force`**, and every log was checked to say `ok:`
and not `skip` before any gate result was believed:

```
landscape   12 ok / 0 skip        portrait  12 ok / 0 skip
re-render    5 ok / 0 skip (x2)   B02        1 ok / 0 skip (x2)
```

`--scale=2` is **hardcoded** inside `remotion_scenes.py` (line 151); passing it on the
command line is an argparse error. 4K is automatic. The per-beat intermediates render at
30fps and `./art run` normalises the master to 24 — matching week 5's delivered file.

## 7. Audio

Generated once, **never regenerated**. Both cuts share the same twelve mp3s, verified
byte-identical by hash rather than trusting `make_vertical.py`'s own report.

```
B00 18.15  B01 17.47  B02 15.42  B03 17.86  B04 18.99  B05 18.92
B06 20.57  B07 18.35  B08 17.71  B09 20.67  B10 14.74  B11  7.51
```

The sheet was regenerated three times during QC; `lock_durations.py` was re-run each time
and the total held at 206.36s with zero drift between orientations.

## 8. Final fill, all 24 shipping frames

Measured from the **compiled masters**, not the beat intermediates.

```
beat  16:9 cover / ink    9:16 cover / ink
B00     0.87 / 0.034        0.82 / 0.067
B01     0.99 / 0.069        0.95 / 0.065
B02     0.99 / 0.129        0.95 / 0.162
B03     0.99 / 0.107        0.95 / 0.092
B04     0.99 / 0.077        0.95 / 0.105
B05     0.99 / 0.126        0.95 / 0.117
B06     0.99 / 0.052        0.95 / 0.043
B07     0.99 / 0.072        0.95 / 0.123
B08     0.99 / 0.074        0.95 / 0.083
B09     1.25 / 0.344        1.19 / 0.338
B10     0.87 / 0.033        0.82 / 0.065
B11     0.60 / 0.061        0.73 / 0.083
```

Nothing below the 0.55 floor. The 9:16 outro at **0.73** is the payoff of the
`ClaudeTitleOutro916` padding double-count fix — it measured **0.52** before.

## 9. Not shown, on purpose

- **182 passing offline tests** — measures the code, not the result; B08 is already dense.
- **31 of 34 new bonds caught** — week 5's B04 was built on it; this week the beat budget
  went to the opening reader. FACTCHECK rows 29 and 30. Say the word and either goes on.

## 10. Author files

`README.md`, `FRICTIONAL.md` and `narration_script.md` were **not touched**.
`description.txt` was already a complete long-form description in the house shape, so one
build-provenance paragraph was *added*; the original is preserved byte-identically as
`description-source.txt` (verified with `cmp`).
