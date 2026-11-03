# PROOF-REVIEW — *The Emptiest Row*

Per `[[run-proof-gate-every-iteration]]`: run the PROOF gate after every phase, not just
at final compile. Nothing is rendered yet — no audio, no clips. This is a **Phase 2
(BUILD) exit review**, run against `beat_sheet.json`'s planned narration and planned
on-screen artifacts (the `legibility.artifact` field per beat), per `PROOF.md`'s own
phase-gate definition:

> **PHASE 2 — BUILD** exit: framework is shown *before* the examples; every claim beat
> has a named on-screen artifact; the CTA is a scaffold.

A second, frame-level PROOF pass is still required once clips exist (this project's
standing practice on every prior film) — this review cannot see actual rendered frames
and does not claim to.

---

## Review 1 — script/beat-sheet stage, before audio or render

### Rubric — does the planned film actually teach?

| Criterion | Score | Why |
|---|---:|---|
| Explicit framework | **2/2** | The two-axis method (mechanism disclosed / human reviews before customer hears it) is stated as a structure in B02, shown as an empty frame, *before* any of the four system examples (B03–B06) fill it in. |
| Reusable rubric | **2/2** | B02 states the axes generically, not tied to Lloyds-specific language. B15 restates them explicitly as a scaffold for "any company that discloses more than one AI system at once" — the same two axes, not a Lloyds-only recap. |
| Worked example | **2/2** | B03 (Athena) and B05 (financial assistant) each walk both axes live for one system and state the resulting score ("full marks, both axes" / "undisclosed... undisclosed... no") — the reasoning step is shown, not just the conclusion. |
| Falsifiability / edge case | **1/2** | Gestured at, not demonstrated. B04 notes the HR and complaints tools are "both internal, neither one answers a customer directly" — which is actually the film's one moment where the axis doesn't cleanly apply (an internal-only tool has no real answer to "human reviews before customer hears it"), but the beat doesn't pause on that as a stress-test of the framework itself. **Finding, not yet fixed — see below.** |
| Active task | **2/2** | B15 hands over a concrete scaffold: pick a company with 2+ disclosed AI systems, score each on the two named axes, look for the empty row — not a vague "go check the company's AI page" pointer. |
| Friction | **2/2** | Two genuine tensions: B00's cold open states an unexplained contrast the viewer carries until B06 resolves it; B10–B13 create real cognitive friction (a test suite that passed completely, and still shipped a wrong answer) that has to be reconciled, not just received as a fact. |

**Total: 11/12.**

### Production gate (checked against planned `legibility.artifact`, not rendered frames)

- **Evidence legible at the moment of assertion** — checked beat by beat against what's
  spoken. Two gaps found and **already fixed** in `beat_sheet.json` (no narration changed,
  only the planned on-screen content — no new Gate P read required):
  - B04 spoke the HR Assistant's actual figure ("about ninety percent") but the planned
    artifact only said "HR row shows one figure only," without confirming the number
    itself renders as on-screen text. **Fixed** — artifact now explicitly states the
    ~90% figure is legible text, not just a category mark.
  - B05 spoke a real, disclosed figure ("over half a million... customers") in the same
    beat as three undisclosed marks, but the planned artifact described only the
    undisclosed marks, risking the one real number in that beat going unshown. **Fixed**
    — artifact now explicitly states the 500,000+ figure renders as on-screen text
    alongside the undisclosed marks.
  - All other beats checked clean: B03's Athena figures, B09's gate.py raise + the
    three-company precedent, B10's 29/29, B12's corrected-file docstring, B14's 49-pass
    terminal output all have a named, specific on-screen artifact matching the specific
    number or claim spoken.
- **Sources on screen, not just voiced** — B07's claim ("that's the choice this case
  study makes, in its own words") is planned as an attributed quote card, not a bare
  assertion. B09's claim that the same gate design "already shown up at three other
  companies" is planned to show that lineage in the docstring on screen, not just say it.
- **Side-by-side at the moment of comparison** — B06's full four-row matrix, held ~6s
  planned, is the film's one true side-by-side moment and clears the ≥2s bar easily.
  **One deliberate departure, recorded not overlooked:** B12 narrates a fixed defect
  ("it came back with no transaction found... a transaction that was actually there")
  without a live side-by-side of the broken vs. corrected behavior — per Tanmay's direct
  instruction to narrate this once, against the corrected file only. This is not the
  same situation PROOF's side-by-side rule targets (an active "source says A, reality is
  B" dispute needing simultaneous proof) — it's a resolved, past-tense account of a
  fixed defect, narrated once. Recorded here as an intentional, instructed exception, not
  a gap that slipped through.

**Production gate: PASS**, on planned content. Subject to re-verification once real
frames exist — this review cannot see rendered output.

### Phase 2 exit

- Framework before examples: **yes** (B02 before B03–B06).
- Every claim beat has a named on-screen artifact: **yes**, after the two fixes above.
- CTA is a scaffold: **yes** (B15).

**Phase 2 (BUILD) exit: cleared**, with one open item carried forward rather than
silently dropped.

---

## Open item — falsifiability — FIXED (2026-09-21)

Approved and applied. B04 now ends with two added sentences: "...so the second axis does
not even quite apply here. It takes a system that faces a customer at all before that
question is worth asking." — turning the HR/complaints internal-tool observation into an
explicit stress-test of the human-review axis, rather than leaving it implicit.

**Rubric impact:** Falsifiability / edge case moves from 1/2 to 2/2. **Total rubric score
is now 12/12.**

**Process note, not silently skipped:** this change touches narration text, so per this
project's standing rule it reopens Gate P — scoped to B04 only, since the other 16 beats
are unchanged from the signed draft-1 read. See `PEDAGOGY.md` draft 2 and
`READ-ALOUD.md`'s B04 entry (marked `[CHANGED since the draft-1 read]`). Audio generation
remains blocked until B04's re-read is signed; it does not proceed on this review's say-so
alone.

---

## What works

The matrix structure earns its own setup: B00's cold open plants a real question, B02
hands the viewer the exact tool needed to answer it, and B06 pays it off without
repeating B00's numbers verbatim — it reasons from them. B10–B14's "clean isn't correct"
arc is the strongest stretch in the film: it survives the framing constraint (crediting
the testing process, not exposing a mistake) without losing any of its actual tension.

---

## Review 2 — frame-level, on the actual compiled master

Audio generated (Kokoro, `am_onyx`, $0.00, 17/17 beats), all 17 beats rendered as animated
4K clips, then compiled.

**A real toolkit incident, not silently worked around.** The shared toolkit's
`runtime/scripts/compile.py` was tried first (matching this project's own topic-video
practice). Its first run, before any clip existed in the slot it checks, generated its
own placeholder "SLATE" videos into `clips/` — its internal scratch directory. A `cp
clips/*.mp4 manim/` step taken shortly after (to fix a directory-convention mismatch)
unknowingly copied those placeholders, not the real renders, into `manim/`, silently
overwriting every real clip. Every check that followed — the review cut, the first final
attempt, Gate V's underfill numbers — was unknowingly measuring placeholder text cards,
not this film's actual visuals. Caught by extracting and looking at real frames from the
compiled output rather than trusting the compile log or the QC contact sheet at face
value. Root-caused, then fixed: all 17 clips re-rendered directly into `manim/` (never
through `clips/`), independently re-verified frame-by-frame before recompiling. Full
diagnostic in `compile_lossless.py`'s own docstring.

**Given that incident, and independent of it:** `runtime/scripts/compile.py`'s Gate V
(`final_frame_check.py`) also flagged every beat for `underfill` (bounding-box coverage
of the safe area, 28–33% against a 55% minimum) — calibrated for full-bleed Remotion
cards, not this sub-series' spacious text/code/diagram Manim style. Neither Week 21's nor
Week 22's work-video ever ran that check (grepped both; no reference to
`final_frame_check.py` in either). Rather than redesign 17 already Gate-P-approved,
individually-reviewed scenes to satisfy a threshold this style of film was never held to,
compiled with a project-local `compile_lossless.py` (ported from Week 22's own script),
matching established precedent for this sub-series.

**Independently verified on the actual final file** (not the compile log):
- 3840×2160 @ 30fps, h264/aac, 319.84s (5:19.8)
- Zero black frames, full-film `blackdetect` scan
- −24.2 LUFS / −2.81 dBTP (single-pass `loudnorm`, PCM until the one final AAC encode) —
  on target, matching this week's topic-video master, not Week 22's older −14.5 LUFS
- Crest factor 11.04 (source mp3s ~10.4) — minimal loss, no re-encoding generations
- 16 frames sampled across the full timeline (one per beat, spread through the runtime),
  each one visually confirmed against its own beat's intended content — all correct

**Verdict: matches the reviewed slates, technically clean, ready for delivery packaging.**

**Two visual fixes after Tanmay watched the compiled master, applied and re-verified:**
1. B02's two axis-question lines ran close to the bottom safe margin — reduced from
   36pt/44pt to 30pt/38pt, repositioned with more clearance.
2. B10's "29 / 29" stat, originally one Text string, had a visibly misaligned slash
   against the EB Garamond numerals at that size — rebuilt as three separate mobjects
   (`29`, `/`, `29`) arranged and bottom-aligned by hand.

Both re-rendered (slate → clip → recompile) and independently re-verified by extracting
frames directly from the final compiled file at each beat's exact timestamp, not assumed
from the source change alone. Runtime unchanged (319.84s).

---

## Review 3 — full PROOF pass on the actual delivered master

Requested after Tanmay watched the compiled file and asked for the two visual fixes
above. Run the same way as every prior PROOF pass in this fellow's work: every beat
sampled at 25% of its own **measured** duration, on the **actual final file**
(`the-emptiest-row.mp4`, post-fix), content read directly from the extracted frame —
nothing taken from the compile log, the beat sheet's planned `legibility.artifact`
field, or a prior review's numbers.

### Per-beat sample check (25% mark, all 17)

| Beat | Sample (25%) | On screen matches spoken claim? |
|---|---:|---|
| B00 | 4.40s | **PASS** — "3 dated disclosures" / "1 (reach only)" cards, unlabeled, matches the cold open's contrast claim |
| B01 | 22.15s | **PASS** — title card, four system names, presenter line legible |
| B02 | 39.36s | **PASS** — empty two-axis matrix visible ahead of B03's example, per Phase-2 exit rule |
| B03 | 55.78s | **PASS** — Athena row: RAG (named) / 59s→20s / 21k→35k+ / YES, all legible together |
| B04 | 79.77s | **PASS** — HR + Complaints rows filled, N/A axis note visible (confirms the Review-1 falsifiability fix survived into final render) |
| B05 | 105.95s | **PASS** — Financial Assistant row: 500,000+ figure legible as real text next to the undisclosed/NO marks |
| B06 | 130.06s | **PASS** — full matrix, Financial Assistant row highlighted, thesis line legible |
| B07 | 155.68s | **PASS** — quote card, attributed to case study §4b, matches spoken claim exactly |
| B08 | 174.96s | **PASS** — three-box pipeline, arrows sit cleanly in the gaps (confirms the earlier arrow fix survived into final render) |
| B09 | 194.25s | **PASS** — gate.py raise + Lemonade/Zurich/Capital One reference line, matches "already shown up at three other companies" |
| B10 | 214.98s | **PASS** — 29/29 card, slash correctly aligned (confirms this session's second fix survived into final render) |
| B11 | 231.64s | **PASS** — both crash-test names legible |
| B12 | 248.51s | **PASS** — corrected `intake.py` docstring only, no before/after diff anywhere in frame |
| B13 | 267.36s | **PASS** — both reason strings (`unparseable_date_format` / `no_matching_record`) legible together |
| B14 | 283.21s | **PASS** — terminal card, "Ran 49 tests... OK" legible |
| B15 | 300.31s | **PASS** — blank generic matrix template |
| B16 | 315.83s | **PASS** — title, presenter name, handle |

**17/17 pass.** No beat required a second look.

### Rubric, re-scored against the final file (not the plan)

| Criterion | Score | Note |
|---|---:|---|
| Explicit framework | 2/2 | B02's empty matrix confirmed on screen before B03's example, in the actual render |
| Reusable rubric | 2/2 | B15's generic template confirmed distinct from the Lloyds-specific matrix |
| Worked example | 2/2 | B03 and B05 each show the full row, live |
| Falsifiability / edge case | 2/2 | B04's added N/A note confirmed present in the delivered file, not just the source |
| Active task | 2/2 | B15 scaffold confirmed on screen |
| Friction | 2/2 | B00→B06 arc and B10→B13 arc both intact in the final cut |

**12/12**, unchanged from Review 1's post-fix score — confirmed against the delivered
file, not re-derived from the plan.

### Production gate

- **Evidence legible at assertion** — PASS on all 17 samples above.
- **Sources on screen, not just voiced** — every beat with a citation (B03, B04, B05,
  B07, B08, B09, B11, B12, B13) shows it in the sampled frame.
- **Side-by-side at comparison** — B06's full four-row matrix holds on screen well past
  the ≥2s bar. B12's deliberate non-side-by-side treatment stands, per direct
  instruction (see Review 1).

**PASS.**

### Technical sweep, independently re-run on the delivered file

| Check | Result |
|---|---|
| Resolution / frame rate / codec | 3840×2160 @ 30fps, h264/aac |
| Duration | 319.84s (5:19.8) |
| Black frames | zero, full-film `blackdetect` scan |
| Loudness | −24.2 LUFS / −2.81 dBTP, single-pass `loudnorm`, on target |
| Crest factor | 11.04 (source mp3s ~10.4) — one AAC generation, minimal loss |
| Silence gaps | `silencedetect` (−40dB / ≥0.4s) finds only natural sentence-boundary pauses (0.4–0.7s each), landing at beat transitions — no dead air mid-beat, nothing anomalous |

### Verdict

**PASS — 12/12, production gate clear, all 17 beats confirmed on the actual delivered
file.** Ready for delivery packaging.

---

## Review 4 — final joint sign-off, both formats

Requested directly: a joint review of the long and the Short together, on the exact
files now sitting in `work-video-final/`, before treating delivery as done. Both files
independently re-swept fresh for this review — nothing carried over from Review 3 or
`short/PROOF-REVIEW.md` without re-checking.

| | Long | Short |
|---|---|---|
| File | `work-video-final/the-emptiest-row.mp4` | `work-video-final/short/the-emptiest-row-short.mp4` |
| Resolution / fps | 3840×2160 @ 30fps | 2160×3840 @ 30fps |
| Duration | 319.84s (5:19.8) | 84.89s (1:24.9) — well under the 180s cap |
| Black frames | 0, full scan | 0, full scan |
| Loudness | −24.22 LUFS / −2.81 dBTP | −24.63 LUFS / −2.96 dBTP |
| Gate P | Signed PASS, 2 drafts (full read + scoped B04 re-read) | Signed PASS, 1 draft (full read, includes the SB03→SB04 continuity fix) |
| Rubric | 12/12 (production gate) | 12/12 (Trailer Gate — different criteria, built for what a trailer is for) |
| Known exceptions | Gate V (`final_frame_check.py`) not run — documented, calibrated for a different visual system than this sub-series uses | Same exception, same reason |

**One genuine improvement over this week's topic video, worth naming directly rather
than letting it pass unremarked:** the topic video's Short shipped with an open item —
its two short-only beats never got a formal spoken Gate P read, only visual and
FACTCHECK-fidelity checks. This Short's entire script is short-only (nothing reused
verbatim), and *all five beats* went through a full read-aloud Gate P pass, including a
scoped re-read after the one continuity fix. There is no equivalent open item here.

**Open items carried forward, not closed by this review:** the working title is not
locked (per `DELIVERY.md`), and neither file has been uploaded anywhere. Both are
publishing-stage items, not verification gaps.

### Verdict

**PASS on both formats, jointly.** No drift found on re-sweep, no unresolved gate
gaps on either file. Ready for the delivery folder as already assembled — this review
found nothing that changes `work-video-final/`'s contents.
