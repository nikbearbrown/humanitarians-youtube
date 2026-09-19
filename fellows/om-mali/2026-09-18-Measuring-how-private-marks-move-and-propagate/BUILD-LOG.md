# BUILD-LOG — measuring-how-private-marks-move-and-propagate (week 8)

Built with **brutalist.art** (`ai-explainer`, channel `claude-hai`). Free/local throughout:
Kokoro TTS + Remotion + ffmpeg. **$0.00 spent. No API key used.**

Seventh episode of the Private AI Valuation Agent series (week 1 → 2 → 4 → 5 → 6 → 7 → 8;
there is no week 3 episode). Fourth episode shipped in both orientations.

**The first episode that measures rather than builds**, and the structure follows from that:
three findings, each immediately followed by the thing that narrows it.

---

## Where the inputs came from

| File | Origin | Status |
|---|---|---|
| `narration_script.md` | Already here | input, unmodified |
| `figdata_week8.json` | Already here — queried from the marks panel at figure-build time | **the source of truth for every on-screen number** |
| `README.md` | Already here — figure-to-beat map, three things not to get wrong, four defects | input, appended with a pointer to the built reel |
| `pantry/w8-*.png` + `.svg` | Were loose in the folder root | **moved to `pantry/`** — the series keeps reference art there, and `run.sh` uses `images/` for compile OUTPUT |

---

## Every number is injected, and fourteen groups are asserted

```
guards.marks == 5479; unadjudicated_splits == 0; incomplete_runs == 0
steps 4079 + first_observation 1099 == marks 5178 == 5479 − change_blocked 301
remark.overall: 1019/4079 == 0.2498, and moved + unchanged == steps
ALL THREE widenings < 0.30 AND monotonically increasing
by_company: 10 rows, steps sum to 4079; floor 0.0%, ceiling X.AI 48.5%
same_date_stats: groups 130, median 0.1082, multi_level 92 == len(transition)
steady 38 + transition 92 == 130; p90 == 0.405 (measured, not a round number)
window: 11 rows, 8 distinct managers, 2 period ends, 140.9676 → 261.5705
window levels: >= 2 clusters, and the LAST holds more marks than the first
propagation: 37 events, median 30, max 92, 15 at zero days
(small events at zero) / 28  >  (big events at zero) / 9
```

**Two of these are doing unusual work.** The widening assertion is load-bearing for B02's
entire claim — if a future data change pushed any widened definition into the plan's 30–40%
band, the build fails rather than shipping a quieter version of the beat. And the last one
protects a *deleted* claim: the figure once said "the biggest events are the fastest", and
the inequality that disproved it is now asserted so it cannot creep back.

`python build_beat_sheet.py --check` runs the assertions and writes nothing.

---

## Two figures computed here rather than drawn from a constant

The README records both as defects in the original drawing code. Neither is fixed by
correcting a number — both are fixed by deriving it:

- **The window's price levels** come from single-linkage clustering at the findings module's
  own 2% relative gap, not from `price > 220`. That produces **four** levels rather than two:
  the old level (2 marks near $141), the new one (7 marks near $259), and **two singletons at
  $203.36 and $243.40** — managers caught mid-crossing. A binary threshold would have assigned
  those two to one side and erased the beat's actual argument.
- **The dispersion highlight** is the measured p90. It lands at 40.5%, near the old hard-coded
  0.4, which is exactly why the constant could survive unnoticed.

---

## Decisions taken during the build

| # | Decision | Why |
|---|---|---|
| 1 | **Seven script sections → eight body beats**, arranged as finding→caveat ×3. | The propagation caveat in `figdata` is not spoken in the script at all, and the guards were a closing sentence. Splitting gives each limit its own frame instead of letting three findings stack and then apologise at the end. |
| 2 | **"From zero for Groq", not "one percent for OpenAI".** | Groq's 0.0% is the true floor and is on the chart. Saying 1% over a visible 0% bar is a mismatch a viewer can see. Every bar carries its own step count so an 11-step 0% is not read as a strong result. |
| 3 | **"Disagreement is the normal state" → "different prices on the same date is the normal state".** | The README's own warning. B05 then spends a whole beat on the reading that is not disagreement. |
| 4 | **B04 and B06 deliberately share the `DotField` primitive.** | A viewer who learns to read the shape in B04 reads B06 faster, and the beats are separated by B05, which looks like neither. What differs is what the shape says: B04's mass is its width, B06's is the stack at zero. |
| 5 | **Greeting rotated to `Szia, HAI`.** | Weeks 1–7 used `Ola`, `Hej`, `Ciao`, `Hallo`, `Salut`, `Ahoj`. Hungarian short form; the lexicon never repeats a language. |
| 6 | **Kicker is `Irreducibly Human`.** | GATE L rule 7 — the fixed `claude-hai` series name. Set at authoring time, so GATE L passed on the first run for the sixth episode running. |
| 7 | **`MarksMoveAndPropagate.tsx` is self-contained.** | Same reasoning as weeks 2, 4, 5, 6 and 7: reel-local files duplicate the chrome helpers so the earlier signed masters stay re-renderable byte-identically. |

---

## Toolkit defects found and fixed

Both live in the **shared** `ClaudeVerdictArtifact` card, and week 8 is simply the first reel
whose verdict was long enough — and whose first character was a digit — to expose them.

| Defect | Effect | Fix |
|---|---|---|
| The landscape card's type scale is fixed and its height is content-driven, with no overflow guard | A five-clause recap grew past the title-safe bottom edge. **GATE V caught this one** — 2 BLOCKERs, `edge-bleed`, the first time the gate has fired in this series | Same guarded fit as `ClaudeVerdictArtifact916` got in week 5: estimate the wrapped row count and shrink the line type only as far as needed. Content that already fits keeps scale 1.0 exactly, so every earlier reel renders identically. |
| `stripLeadNum` — there to remove a manually typed "1. " — used `/^\s*\d+\s*[.)\-–—:]\s*/` | It ate the leading digits of any line **starting with a decimal**: `25.0% of 4,079 …` rendered as **`0% of 4,079 …`**. A wrong figure on screen, and GATE V passed the frame | The trailing `\s+` is now required, so `1. Chat: …` is still stripped and `25.0%` is untouched. Verified against the real lines from weeks 4–8; none of them was affected, which is why it survived seven episodes. |

The comment above the landscape card's sizing block records it being *enlarged* in an earlier
pass to clear an `underfill` gate. That is precisely why it later overflowed: the two gates
push in opposite directions and nothing was fitting the content between them.

**The known footgun bit again**, as every week since week 5: `remotion_scenes.py` loads the
beat sheet at the start of a run and rewrites it at the end, so edits made during the render
are silently lost. Recovered by re-running `build_beat_sheet.py` and `lock_durations.py`.

---

## Visual QC — what LOOKING at the frames caught

GATE V reported **2 BLOCKERs** (see above) and then 0/0. Reading the frames found six more it
did not see, two of which put wrong numbers on screen.

| Beat | Defect | Severity | Fix |
|---|---|---|---|
| B09 | **`25.0%` rendered as `0%`** — the shared card's list-number stripper ate the decimal | **MAJOR, missed by GATE V** | See the toolkit table above. |
| B03 | **The sample-size note quoted the wrong two numbers** — "171 steps for X.AI against 10 for the smallest". 171 is the *hottest* bar, not the largest sample; the real span is 10 (Perplexity) to 1,812 (Databricks) | **MAJOR, missed by GATE V** | The note now derives both extremes of `steps` rather than reusing the extremes of `share`. `FACTCHECK.md` row 12 corrected with it. |
| B05 | **Five manager labels overprinting.** Four managers price at $259.1364 on the same date, so their dots and labels landed on one y and the right column rendered as an illegible smear | **MAJOR, missed by GATE V** | Dots sharing a y are fanned horizontally so the count is visible; labels are pushed down greedily to a minimum gap with a leader line back to the dot that moved. |
| B03 | The panel-wide rule was drawn straight through the step-count labels of the two longest bars | **MAJOR, missed by GATE V** | The bar now sits in a fixed-width track with the labels after it, permanently clear of the rule. |
| B04 | The note claimed the 92 transition groups "are the ones in the chart's tail". Only ~13 sit above the p90; the 38 steady groups are the stack at zero | MINOR (a wrong reading of the chart beneath it) | Rewritten to describe what the chart actually shows. |
| B05 | The lowest pushed-down label sat on the period-end caption | MINOR | Axis row given its own clearance. |
| B06 | Rendered "90  median 90 days to reach ALL holders" — the numeral twice | MINOR | Label no longer repeats the value it labels. |

**GATE V's record, eight episodes in.** It fired for the first time this week, on `edge-bleed`,
and it was right. It still cannot see overlap (weeks 1, 4, 6, 7, 8), cannot tell whether a
number on screen is the right number (weeks 5, 7, 8), and cannot tell whether a caption
describes the chart under it (week 8). Two of this week's three wrong-number defects were in
text the gate rendered perfectly.

---

## Gates

| Gate | State |
|---|---|
| **FACTCHECK** | 20 rows, all traced. **Rows 6, 9, 18 and 20 flagged** — the plan's 30–40% prior, the by-company floor, the window's clustered levels, and the deleted "biggest events are fastest" claim. |
| **PROOF GATE / CHECKS-REPORT** | PASS — 8 SHOW / 4 justified-HOLD / 0 PUNT. Teaching arc 6/6. Written before the first compile. |
| **GATE P (pedagogy)** | **PASS — signed by the author (Om Mali), 2026-09-18**, after reviewing the slate cuts. Covers the three structural splits, speaking Groq's 0.0% floor, narrowing "disagreement" to "different prices on the same date", FACTCHECK rows 6/9/18/20, the B10 handoff prompt, and the dual-orientation build. Audio for the pre-signature review cut was generated with `--no-gate`, recorded here rather than passed silently; the gate was re-run WITHOUT the override after signing and passes on its own. |
| **GATE L** (beat-mix lint) | PASS on the first run. |
| **GATE V** (frame-level visual QC) | **FAILED first, then PASS.** 2 BLOCKERs on B09 (`edge-bleed`), fixed at source. Re-run against the 4K masters themselves — 16:9: 24 frames, 0 BLOCKER, 0 MAJOR. 9:16: 24 frames, 0 BLOCKER, 0 MAJOR. |
| **GATE F** | Not triggered — no Manim beats. |

**One advisory, not a gate.** `compile.py` warns that `illustrate` carries 8 of 12 beats (66%)
against a ~40% cap written for reels built from pantry media. Every body beat here is a native
animated Remotion scene with its own scheme. Weeks 2, 4, 5, 6 and 7 carried the same shape.

---

## Build facts

- **12 beats**, all filled by Remotion. Zero slates.
- **Audio**: Kokoro `am_onyx` (unchanged since week 1), **225.11s narration + 0.40s lead
  (3:45.5)** — the longest episode in the series. The same mp3s drive both orientations.
- **Eight reel-local scenes**, eight different visual schemes, each laid out natively at both
  1920×1080 and 1080×1920.
- **Body beats 49–67 words** — all eight inside the 45–70 band. The length comes from
  structure, not verbosity: three of the eight body beats exist to narrow a claim made
  elsewhere.
- **The reel ends on its limits**, not its findings. B08's last line is "these are fund marks,
  not transactions".
- **Never published.** The masters stay in this folder. Publishing is a separate, explicitly
  human-authorized step that this toolkit does not perform.

---

## Finalization (2026-09-18)

GATE P signed. Four things before the masters were stamped:

1. **The signature was attributed** — author and date, with the `--no-gate` disclosure kept
   beneath it.

2. **Staleness proved per BEAT, and two beats re-rendered rather than argued about.** The 9:16
   cut was entirely current. Seven landscape beats were flagged by mtime against an edit that
   lived inside `W8Window` only, so most of the flags were false; each was re-rendered as one
   still from current source and diffed against the shipped frame at native 4K.

   **The controls were weaker this week and it showed.** The two known-current beats available
   were B05 (a sparse scatter) and B09 (a near-uniform card), scoring 0.009% and 0.208%
   differing pixels — neither is a text-dense frame, so the band they set understates the h264
   noise floor for frames that are. Five of the seven flagged beats landed inside it; **B03
   (0.437%) and B07 (0.634%), the two densest, did not.** Density is the likely explanation and
   a localisation pass would probably have shown it — but that is the same reasoning week 7
   declined to spend, and re-rendering two beats costs six minutes. Both were re-rendered.

3. **GATE P re-run without the override.** `generate_audio_kokoro.py --dry-run` passes on its
   own. `--dry-run` deliberately: regenerating audio would shift the measured durations by
   milliseconds and invalidate every render timed against them.

4. **`mp4/` refreshed by hand.** `./art final` writes only the master — the same step weeks 1,
   2, 4, 5, 6 and 7 needed.

GATE V was re-run against the two 4K masters themselves: **24 frames each, 0 BLOCKER,
0 MAJOR.**

**A note for next week on control choice.** This method is only as good as its controls, and
picking two sparse frames set a floor that two dense frames then exceeded. The fix is to choose
controls that match the flagged beats in text density, not just in recency.
