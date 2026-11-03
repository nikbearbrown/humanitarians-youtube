# PEDAGOGY.md — the-rule-that-lost (Mycroft 8; audit-layer update, part 1 of 2)

**GATE P VERDICT: PASS** (Divij Pawar). GATE P was signed PASS by Divij Pawar on
2026-09-26. The narration was then changed at his direction (v4, "about the work, not the
working"), so that approval covers text that no longer exists. Re-approve the v4 narration
below before Kokoro runs.

> GATE P is a human checkpoint, not an agent one (`fellows/divij-pawar/CLAUDE.md` §4).
> - **To sign:** read the arc below and resolve the checklist at the end. Then change
>   `PENDING` above to `PASS`, and add your name and the date.
> - **Until then:** `generate_audio_kokoro.py` must not run. Nothing in this reel has
>   generated audio or rendered a frame yet.
> - **Voice approval is a separate gate:** `metadata.approvals.voice` in `beat_sheet.json` is
>   also `pending` (§4, `PIPELINE-SAFETY.md`).

**Files:**
- **Source script:** `the-rule-that-lost.md`, in this folder. Its Beats section is generated from
  `beat_sheet.json`, the source of truth.
- **Generator:** `build_sheets.py` writes both this reel's sheet and Mycroft 9's.
- **Evidence:** in `assets/` (see `assets/MANIFEST.md`).

---

## Where this sits

This is the sixth video in the Cross-Agent Validation weekly-update sub-series, continuing from
`fifteen-of-sixteen/` (Mycroft 7).
- **What the cold open does:** it answers Mycroft 7's headline with a correction. Part of
  "fifteen of sixteen" came from the old tagger reading "Return on **Assets**" as the Assets
  figure.
- **What it assumes:** Mycroft 3–7 are common knowledge. The script's production brief lists
  what each already taught. B01 is a fast recap, not a re-explanation. The video never
  re-teaches what cross-validation is, why disagreement beats agreement, or the disjoint-lens
  diagnosis.

## Beat breakdown — 18 beats (B00–B17)

The skeleton follows `CLAUDE.md` §9:
- **B00:** the `ClaudeComposerAsk` cold open.
- **B01:** the framework, stated before any example.
- **B02–B13:** one idea per beat.
- **B14–B15:** the honest-ledger close, with "true now" and "still not true" as two beats, as in
  Mycroft 6 and 7.
- **B16:** the dense end-card reprise.
- **B17:** a stat-free `ClaudeTitleOutro`.
- **No "Your Turn" beat:** Mycroft reels don't have one. The viewer's takeaway, the four-box
  test, is carried by B16.

| Beat | Act | Words | Est. | Starts |
|---|---|---|---|---|
| B00 | cold open | 100 | 31s | 0:00 |
| B01 | chapter 1 - recap and the four-box test | 71 | 22s | 0:31 |
| B02 | chapter 2a - period: what the agents were handed | 116 | 36s | 0:53 |
| B03 | chapter 2b - the fix, test first | 65 | 20s | 1:29 |
| B04 | chapter 2c - source: a failure recorded as ok | 82 | 26s | 1:49 |
| B05 | chapter 3 - two agents at once | 54 | 17s | 2:15 |
| B06 | chapter 4a - metric and unit: comparing figures | 130 | 41s | 2:32 |
| B07 | chapter 4b - the ratio check | 106 | 33s | 3:13 |
| B08 | chapter 4c - the correction | 71 | 22s | 3:46 |
| B09 | chapter 5a - the test it failed | 87 | 27s | 4:08 |
| B10 | chapter 5b - the decision | 58 | 18s | 4:35 |
| B11 | chapter 6 - three format failures found live | 112 | 35s | 4:53 |
| B12 | chapter 7a - the table | 65 | 20s | 5:28 |
| B13 | chapter 7b - something in common | 82 | 26s | 5:48 |
| B14 | chapter 8a - the honest ledger, true now | 44 | 14s | 6:14 |
| B15 | chapter 8b - the honest ledger, still not true | 48 | 15s | 6:28 |
| B16 | close - the smallest true claim | 70 | 22s | 6:43 |
| B17 | outro | 13 | 4s | 7:05 |
| **Total** | | **1,374** | **7:09 (429s)** | |

**How the runtime is estimated:**
- **The rate:** 3.2 words per second. That is the measured rate of actual Kokoro `am_onyx`
  audio across Mycroft 1–7 (3.11–3.56 words/s), not the 150 wpm planning figure. Mycroft 6 came
  in 35% faster than a 150 wpm estimate.
- **The target:** 6–8 minutes (human request). 7:09 of speech sits inside it; with no held beats, the estimate is the speech itself.
- **Re-check:** once real durations land.

## Narration v4 — about the work, not the working (2026-09-26)

**Human direction:** "Both videos need to be about my work not about me working." The narration
(`narration_v4.py`), the scenes (`scenes.py`) and the visual descriptions (`visual_v4.py`, applied
by `build_sheets.py`) were changed together.
- **Removed:**
  - references to earlier videos ("Mycroft six said…");
  - the commit and uncommitted-files panels;
  - test counts;
  - ledger and RUN_LOG labels;
  - roadmap and "plan approved" talk;
  - who built the gate.
- **Kept:**
  - what the system does and what it found, including the old-versus-new rule result and the
    correction, because those are findings about the work;
  - the "what works now" and "what still doesn't" beats, now listing capabilities and
    limitations of the system rather than project status. The Mycroft structure (`CLAUDE.md`
    §9) needs a limitations beat.
- **Style:** long, connected sentences with no hooks, as in v3. The sentences average 32.0
  words. There are 0 `...` holds and 0 questions.
- **Kokoro risk:** unchanged. Listen to each beat. Split a sentence that runs together at its
  connective, or slow that beat alone (`speed_if_slurred` hints in the sheet).

## Teaching arc

| Beat | What the viewer walks away holding |
|---|---|
| B00 | The headline number (6 of 16, worse than 15 of 16), and why it isn't simply a loss: it exposed two real errors and a correction. |
| B01 | The one test the video applies: metric, period, unit, source. Plus the three-tier roadmap, with this video as tier 1. |
| B02 | Period: the data layer handed agents a 2018 revenue and a nine-month EPS, unlabelled, in every Apple run of Mycroft 5–7. |
| B03 | The fix, written test-first against a real payload: facts carry period, unit, filing and accession. |
| B04 | Source: a failed search recorded as "ok", which is Mycroft 4's null-vs-false, one step worse. |
| B05 | Concurrency, proven by a test a sequential run cannot pass. Overlap is proven; speed-up is not claimed. |
| B06 | Metric and unit: figures compared by what they are, with per-family tolerances. A self-rated "90%" stops counting. |
| B07 | The ratio check answers Mycroft 7's open problem: recompute from the agent's own figures. |
| B08 | The correction: the old tagger's "Return on Assets" mis-tag. The count stands; it deserves less credit. |
| B09 | Falsifiability: the stricter rule lost its own pre-registered test, and five of its alarms can't be judged. |
| B10 | The decision: opt-in, the recorded verdict names its rule, and the evidence for switching now accumulates. |
| B11 | Three format failures found live, each measured and each tested. |
| B12 | The matrix UI, answering Mycroft 6's "zero interface tests". |
| B13 | The first real same-figure agreement, and agents still skipping the shared line. |
| B14–B15 | The honest ledger. "Still not true" is held on screen, uncleared. |
| B16 | The smallest true claim, plus the four-box test as the viewer's takeaway. |
| B17 | Title restated. Nothing else. |

## PROOF rubric self-check (pre-build; re-score from real frames before submission)

| Criterion | Where | Pre-build note |
|---|---|---|
| Explicit framework shown before examples | B01 (four boxes), reused as a corner chip B02–B07 | Stated and shown before the first example |
| Reusable rubric for a new case | The four-box test (B01, B16) | Applies to any number any system compares |
| Worked example walked live | B07: MathTex recomputation 265.6 / 383.3 = 0.693 vs stated 0.13 | Computed in `assets/evidence/out/B07_derivation_checks.json` |
| Falsifiability | B09 (lost its own bar), B08 (the correction), B15 | The reel's spine |
| Active task | B16 end card: the four questions | **Deviation:** there is no scaffolded prompt beat, because Mycroft reels have none (§9). Expect ≤1 here |
| Friction | B00/B09: a "worse" rule that is more honest; the viewer weighs it | Held open by B10's "human decision" |

Production-gate items (legibility, sources on screen, side-by-side held ≥2 s) can only be scored
from rendered frames. The side-by-side moments are B02, B07 and B13.

## Source & adaptation

This reel describes real work, so every claim was checked against
`D:\Code\mycroft\verification-layer` on 2026-09-26, and where possible recomputed by
`assets/evidence/m8_evidence.py`. See `SOURCES.md`. The evidence run changed the script in four
places:
1. **B06, Microsoft.** The "82,886,000,000 = $82.9 billion" match is a **test case** in
   `tests/test_facts.py`, built in Microsoft's filed format. It isn't a stored run. The RUN_LOG
   B1+U2 entry lists it under "Live". The narration now says "a test built from Microsoft's
   filing", and the visual labels it TEST CASE.
2. **B06, Nvidia.** The "confidence 90%" false flag is now tied to a real stored run, `2220eba0`.
   Its only divergent number under the old rule was "90%", and B1 extracts no figure from it.
3. **B07.** Google's return on assets recomputes to 18.96% against a stated 18.85%. That is 0.11
   points, so "within a tenth of a point" was wrong. It now reads "close enough", with both
   numbers spoken.
4. **B13.** The shared Apple rows state **no period**; they are compared as the run's shared
   filing period. The EPS row is "basic or diluted not stated". The narration changed from "for
   the same quarter" to "from the same filing".

Test counts (B12, B14) were re-run on 2026-09-26: **390** Python tests and **74** frontend tests,
up from the 379/60 logged at B2+B3.

## Register & tone

- **Voice:** a periodic update in the first person, in the series' calm register.
- **Honesty moves:** the video corrects its own previous headline (B08) and reports a failed test
  (B09) without spin.
- **Style checks:**
  - scanned for "it's not X, it's Y": none left in the narration;
  - no em dashes in narration, verified by the generator's assertion.

## Known deviations

1. **No "Your Turn" beat.** This is per §9. The takeaway sits in B16.
2. **B00 opens with the required intro line and an AI-narration disclosure** (§8). Mycroft 7 had
   neither. This is the first Mycroft reel to follow the newer rule.
3. **B04's "status: ok" line is a labelled reconstruction.** The pre-fix recorder stored no
   arguments. The arguments shown are real, from post-fix run `1b691654`.
4. **B11's "17 of 135" is the logged figure.** Replaying the detector today gives 18 of 184,
   because more runs have been stored since (`assets/evidence/out/B11_echo_replay_today.json`).
   The narration keeps the logged figure and the end card doesn't use it.

## What a human reviewer should check before signing

- [ ] B08's correction: "part of fifteen of sixteen came from that mistake". Is that the right
  weight? It shouldn't read as disowning Mycroft 7.
- [ ] B06: is showing a constructed test case (clearly labelled) acceptable, or should the beat
  use only stored-run evidence? The Nvidia `2220eba0` run is stored-run evidence either way.
- [ ] B09/B10: the opt-in decision is framed as "a human decision". Confirm you're comfortable
  saying on camera that it's still yours to make.
- [ ] B15/B16: "nothing here is committed". Recount on recording day (80 uncommitted paths on
  2026-09-26; last commit `c53746a`).
- [ ] Test counts (390 / 74): re-run on recording day.
- [ ] Voice: `am_onyx`, as in Mycroft 1–7. Sign `metadata.approvals.voice` separately.
- [ ] Runtime: re-check the 7:33 estimate once Kokoro durations exist.

**Once these are resolved, replace `PENDING` at the top with `PASS`, sign, and date.**
