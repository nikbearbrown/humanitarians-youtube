# VISUAL QC — `ai-data-quality` · "The Rule, Not The Report."

> **Note on filenames.** GATE V (`final_frame_check.py`) *overwrites*
> `_qc/REPORT.md` with its own raw output every run, so the curated record
> lives here in `_qc/VISUAL-QC.md`. `_qc/REPORT.md` is the machine's last run;
> this file is the human-facing verdict.

Three passes, per VISUAL QC LAW. The mp4 probe is a file check and never
counts as QC; every finding below came from reading rendered PNGs.

| Pass | What | Where |
|---|---|---|
| 1 | Single frames of all 7 bespoke scenes at p≈0.95, BOTH aspects (14 stills) — *before* committing render time | `_qc/preview/` |
| 2 | Per-beat frames at 15/50/85% of each beat's measured span, from the compiled masters, both aspects (72 frames) | `_qc/beats/`, `916/_qc/beats916/` |
| 3 | GATE V over each compiled master, plus targeted corner/region zooms | `_qc/corner/` |

Rubric (9 points): edge bleed/clipping · title-safe margins · container
overflow · collision · offscreen anchors · legibility · brand bug placement ·
aspect · canvas fill.

---

## FINAL VERDICT

| Cut | Resolution | Duration | GATE V BLOCKER | GATE V MAJOR | Verdict |
|---|---|---|---|---|---|
| `ai-data-quality.mp4` | 3840×2160 | 187.49s | **0** | 6 — all adjudicated benign | **PASS** |
| `916/ai-data-quality-916.mp4` | 2160×3840 | 187.49s | **0** | 6 — all adjudicated benign | **PASS** |

Zero BLOCKER and zero unadjudicated MAJOR defects in either aspect.

---

## The gate points at the wrong file by default — read this first

`final_frame_check.py`'s candidate glob **prefers `*-slate.mp4`**, the *review*
cut. `compile.py` deliberately burns a timecode into that cut *outside*
title-safe (`x=w-text_w-16:y=16`), and `BURN_IN_EXCLUDE` masks only the
bottom-left strip (x 0–60%, y 94–100%). The top-right timecode is therefore
never excluded, and the gate flags it on **every frame**.

Run against the slate, this reel scored **24 BLOCKERs / 24 frames** — one per
sample, all `edge-bleed … right/top edge`. That uniformity was the tell:
twelve independently authored scenes do not fail identically in the same
corner. Verified by cropping the same corner from both cuts:

- `_qc/corner/slate-topright.png` — the `00:01:00.000` timecode hard against the frame edge
- `_qc/corner/master-topright.png` — empty cream

Re-run as `final_frame_check.py <reel> --mp4 <slug>.mp4` → **0 BLOCKERs**.

**Consequence for `run.sh`:** its built-in GATE V invocation will always fail
any reel whose review cut carries a timecode, and that failure says nothing
about the deliverable. Always re-run the gate against the master before
believing it.

---

## Pass 1 — scene preview (before rendering)

Doing this first was worth it: it caught two BLOCKERs that would each have
cost a full render cycle.

| # | Beat | Aspect | Severity | Defect | Root cause | Fix |
|---|---|---|---|---|---|---|
| 1 | ALL | both | **BLOCKER** | Scenes positioned against the safe box while actually living in a flex child ~13% shorter; in 9:16 `DqPipelineGate` put its destination box past the bottom edge | `useGeo()` returns SAFE, but the stage's spark row and footer strip consume part of it before a scene sees it | Added `useBox()` → the real content box (CW/CH). `DqStage` sizes its content div from the same function, so the two cannot disagree |
| 2 | B02 | 16:9 | **BLOCKER** | `STALE IN 90 DAYS` — the beat's closing line — clipped off the bottom | Grid height was a guessed fraction (`CH*0.58`); header + grid + arithmetic summed to 808px in an 805px box | Grid budget derived as `CH − header − arithmetic`, with a bounded step-up loop so cell rounding can't overshoot |
| 3 | B02 | 9:16 | MAJOR | ~400px dead band between field and arithmetic | same guessed fraction, failing the other way | same fix |
| 4 | B02 | 9:16 | MINOR | the two coverage labels nearly collided | row layout at portrait width | labels stack in portrait |
| 5 | B05 | 9:16 | MAJOR | five bars spread over the full frame height — stopped reading as a chart | bar list was `flex:1` + `space-between`, absorbing all slack | chart is `flex:0 0 auto` with explicit row gap; the column distributes slack between sections instead |
| 6 | B06 | both | MAJOR | every lane's pile showed 3–4 cards, so 218 and 41 looked identical | pile spread the slot index on one axis only | pile is a centred grid (`pileCols`) — a lane holding 25 of 36 now looks like it |
| 7 | B06 | 16:9 | MINOR | dead band down the leading edge | gate sat at 26% of width; nothing remains inbound once cards pass | gate → 17%, lanes and piles rebalanced |
| 8 | B07 | both | **MAJOR** | loose dots near boxes read as a scatter, not a pipeline; diverted dots landed on the QUARANTINE card's text | no drawn pipe — the path was implied by dot motion alone, and nothing reserved the dots' space | Rebuilt: real drawn rail + real elbow branch (SVG), rows riding *inside* the bore |
| 9 | B07 | 9:16 | **MAJOR** | diverted rows slid straight down, off the branch | post-elbow slide applied to the `along` axis; the branch is horizontal in *both* layouts | slide applied to x in both aspects |
| 10 | B07 | 16:9 | MAJOR | gate label rendered as the single word "LOAD" | label hung above the rail, wrapped to 3 lines, ran past y=0, stage overflow ate the rest | label anchored to the top of the flow area, wider `maxWidth` |
| 11 | B08 | both | MAJOR | hollow cards — body clung to the top | body was `flex:1` with text at its start | body centres in its slack; title/body sizes raised |
| 12 | B03 | 9:16 | MINOR | empty band above the first clause, reading like a render fault | `space-around` adds half-gaps at the ends | `space-between` + card padding; portrait mono/tag sizes raised |

All 14 stills re-rendered and re-read after fixing. Zero BLOCKER/MAJOR
remaining at preview stage.

## Pass 2/3 — compiled masters

### The collision GATE V cannot see

**GATE V has no collision check.** It measures edge-bleed, canvas fill and
contrast only — so text on top of text scores *clean*. The beats at risk are
those where an absolutely-positioned block moved relative to a sibling during
pass 1: **B06** and **B07**. Both were read specifically for overlap.

**B07 (9:16) — MAJOR, found by eye, gate said clean.** The diverted rows
crossed the quarantine card's left border and sat on the `country_code`
descenders. Two causes, both real bugs:

1. The row offset was applied through the generic cross axis, which is *x* in
   portrait — so every diverted row shared one *y* and they rendered as a
   single line rather than a cluster.
2. The slide included the elbow radius `r` plus a 2-per-column spread, which
   overshot `quar.left`.

Fixed by positioning the diverted rows as an explicit 4×2 grid on the correct
axes, with a hard ceiling at `quar.left − dot*2.2`, and by running the
portrait branch pipe all the way to the card so the rows ride inside a pipe
that visibly connects. B07 re-rendered in both aspects and both masters
recompiled. Verified: `_qc/corner/916-B07-zoom.png`, `_qc/corner/169-B07-zoom.png`.

**B06 — clean.** No overlap in either aspect; piles read proportionally
(25 / 7 / 4 blocks for 218 / 59 / 41).

### Adjudicated MAJORs — identical in both aspects

Inspected as frames; none is a defect. Recorded rather than "fixed", because
inflating type or adding ink to satisfy a metric would be the actual defect.

| Beat | Flag (16:9 / 9:16) | Judgement |
|---|---|---|
| B02 ×2 | `low-contrast` 0.11–0.15 / 0.10–0.14 | **Correct by design.** ~90% of the frame is the 4,000-cell coverage field, drawn in pale `GHOST` on cream *so the 12 ink cells read as the exception*. The gate averages ink-vs-background across all content pixels, so decorative mass dominates the score. Everything meant to be READ — headline, both coverage labels, the arithmetic line, the 330 counter, footer — is warm ink `#3D3929` on cream and legible at 1080p. The field is texture, not text. |
| B09 ×2 | `underfill` 46% / 42% | **Correct by design**, and not this reel's code — `ClaudeVerdictArtifact` is the house scene that renders a Claude *artifact*: a document card floating on the app page. The cream margin is the app's own page. All four verdict lines legible. |
| B11 ×2 | `underfill` 10% / 20% | **Correct by design**, house scene `ClaudeTitleOutro`. OUTRO LAW asks for a poster-style title restate on an open field. A poster card filling 55% of frame would be the wrong design. |

A peer session building an unrelated reel the same day hit the same two flags
on the same two house scenes (7% and 46%) and reached the same conclusion
independently.

### Per-beat frame read — 36 frames per aspect

| Beat | 16:9 | 9:16 | Note |
|---|---|---|---|
| B00 | ✅ | ✅ | Composer, `Namaste, Hussain`, three RESULT lines present — the ask lands answered (COLD OPEN LAW). Chip correct. Portrait type reads large and clean on a phone. |
| B01 | ✅ | ✅ | Score card, six spellings each PASS, brace, terracotta strike. |
| B02 | ✅ | ✅ | Field fills the width; closing `STALE IN 90 DAYS` present and inside the box (the pass-1 blocker). |
| B03 | ✅ | ✅ | Wish struck, four clauses typed with annotations, `block` terracotta, FAIL stamp. |
| B04 | ✅ | ✅ | Ask micro-beat, no output lines — correct; the RESULT is B05. |
| B05 | ✅ | ✅ | Bars read as a chart, proposal card, 1,284 counter terracotta. |
| B06 | ✅ | ✅ | Collision-checked. Piles proportional. |
| B07 | ✅ | ✅ | Collision-checked and **fixed** (above). Pipe + elbow read; rows inside the bore; card clear. |
| B08 | ✅ | ✅ | Three cards, bodies centred, terracotta underline on card 03. |
| B09 | ✅ | ✅ | Artifact card, four lines legible. Underfill adjudicated. |
| B10 | ✅ | ✅ | Handoff: `Your turn.`, full prompt on screen for the pause, chip correct (HANDOFF LAW). |
| B11 | ✅ | ✅ | Title restate with terracotta period. Underfill adjudicated. |

### Title-safe

Zero edge-bleed across all 24 gate samples per master. This reel cannot breach
title-safe by construction: `DqStage` positions every band inside a container
already offset by `SX`/`SY` = 5% of each axis — exactly 54px in 16:9 and 96px
in 9:16, matching SAFE and SAFE916. Nothing can start above the boundary
without a negative offset, and none is used. (A peer session breached this on
all four of its custom scenes by hand-placing a spark at y=62 against
SAFE916's 96px inset — the container approach makes that class of bug
unreachable.)

### Clip + master integrity (`verify_clips.py`)

Not visual QC, but it catches the one class no frame-reading will: a
wrong-length clip, or a plausible-looking mp4 that is truncated garbage
(`moov atom not found`) because a render or mux died mid-write. Both
`render_beat()` and a stale master gate on existence, not readability, so
either is sticky and would ship silently.

| Artefact | Result |
|---|---|
| 12 × 16:9 beat clips | all OK, lengths match `actual_duration_s` |
| 12 × 9:16 beat clips | all OK |
| `ai-data-quality.mp4` | OK — 187.49s |
| `916/ai-data-quality-916.mp4` | OK — 187.49s |

This check earned its place twice on this build: a killed compile left a
corrupt 187 KB / 786 KB master that `ls` and the build log both made look
finished. The checker was extended mid-build to probe the compiled masters,
not just the beat clips, after the second occurrence.
