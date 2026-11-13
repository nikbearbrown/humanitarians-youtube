# Weekly STEM Video: Calibration — Why Confidence Isn't Accuracy

**Fellow:** Sai Pranavi J.
**Series:** Humanitarians AI Fellows — Weekly STEM Video (`ai-explainer`)
**Source status:** General AI/STEM topic explainer, not a report of the fellow's own engineering work. Describes a well-documented, generic property of predictive models — calibration, whether stated confidence tracks real accuracy — qualitatively. No real model, vendor, or disclosed benchmark is named or resembled, no fabricated statistic is shown. The worked example (B04, a "~90% confident" answer bucket that's actually right 60% of the time) and its falsifiability case (B05, a "~90% confident" bucket that's actually right ~90% of the time) are both fully generic/hypothetical illustrations with round numbers chosen for teaching clarity. See `FACTCHECK.md` and `SOURCES.md`.

## Watch

- Landscape (4K 16:9): not yet uploaded — see `deliverables/landscape/CalibrationConfidence_SaiPranaviJ.mp4`
- Vertical (4K 9:16): not yet uploaded — see `deliverables/vertical/CalibrationConfidence_SaiPranaviJ.mp4`

This video teaches a reusable 3-question test — **Bucket the Claims / Count the Cases / Spot the Bluff** — for telling whether a model's stated or implied confidence in an answer actually tracks how often that answer is right, or just sounds equally confident whether it's correct or wrong. The framework is taught in full before any example, walked through a worked example (a "90% confident" answer bucket that's actually right only 60% of the time — overconfident), stress-tested against a case where the same bucketing shows a genuinely well-calibrated result (a "90% confident" bucket that really is right about 90% of the time), and closed with a concrete task the viewer can run today.

## What this covers (and what it deliberately leaves out)

Covered: two answer cards that sound equally confident with opposite outcomes (B02); all 3 tests shown together, before any example (B03); a worked example (B04) where a "~90% confident" bucket of 10 answers is only right 60% of the time — a real, visible gap between the STATED bar and the ACTUAL bar; a falsifiability case (B05) where a different "~90% confident" bucket really is right about 90% of the time — the bars nearly match; a concrete audit task distinct from the framework card (B06); and a closing takeaway.

Deliberately left out: this is not a benchmark of any real model's calibration, and does not name or evaluate any specific real model, vendor, or product (model calibration — comparing stated confidence against observed accuracy per confidence bucket — is a well-documented, generic property of predictive models, not a single paper or vendor-specific claim). This is also a distinct topic from two adjacent, already-covered videos in this series: **not hallucination** (`2026-09-22-hallucination-why-sounding-sure-isnt-being-right`, which is about whether a claim is fabricated at all) and **not chain-of-thought faithfulness** (`2026-10-15-chain-of-thought-why-the-reasoning-isnt-always-the-reason`, which is about whether a stated reasoning trace caused the answer). This video asks a narrower, different question: does a stated confidence number track real accuracy? No specific percentage or statistic is fabricated or claimed as a real measurement anywhere — the 90%/60% and 90%/90% pairs are illustrative round numbers.

## Illustrative content chosen for B04 / B05

**B04 (worked example):** a "~90% confident" bucket — every answer a hypothetical model gave at roughly the same stated confidence across many different questions, bucketed together. Ten answer chips (6 correct, 4 wrong — 60% actual accuracy) sit under the bucket label; a STATED bar (90%, gold) and an ACTUAL bar (60%, teal) drawn to the same scale make the gap directly visible, not just asserted. Chosen because round numbers make the mismatch legible at a glance, and because the bar-pair idiom directly visualizes the rubric's first test (Bucket the Claims), per the Legibility Contract.

**B05 (falsifiability case):** the identical bucket-and-bars layout, this time well-calibrated — 9 correct / 1 wrong (90% actual accuracy) under a "~90% stated confidence" bucket, so the STATED and ACTUAL bars land at nearly the same length. Chosen because it gives B04's gap a real, visibly distinct counterpart (bars that line up, not a mismatch) — stress-testing the framework against a naive "any confident answer is overconfident" over-trigger, per FACTCHECK.md.

## Production state

- Plan: **approved (Gate P)** — signed 2026-10-21
- Fact-check gate: **resolved** — see `FACTCHECK.md`; kept fully generic, no real model/vendor named, no fabricated statistic
- Narration approval: **approved** — Kokoro `af_bella`, cleared 2026-10-21
- Voice: **Bella (`af_bella`)** — persistent for this fellow's whole series
- Previz: **complete** — 9/9 beats real Manim, no slates, both aspects
- Final render — **16:9 landscape:** `CalibrationConfidence_SaiPranaviJ.mp4`, 3840x2160, 24fps, h264/aac, **147.5s**. GATE V on the true clean master: **0 BLOCKER, 0 MAJOR**.
- Final render — **9:16 vertical (full-length, native portrait, not a Shorts cut):** `CalibrationConfidence_SaiPranaviJ.mp4`, 2160x3840, 24fps, h264/aac, **147.5s** (identical runtime to the landscape master — all 9 beats kept, no drops, no duration cap). GATE V on the true clean master: **0 BLOCKER, 0 MAJOR**.
- Personally re-verified (not just trusting the build report): extracted and viewed real frames from both masters at every beat that had a geometry fix during the build (B02, B04, B05, B07, B08 in both aspects), plus a full contact-sheet review of all 9 beats in both aspects. No text-rendering artifacts, no clipping, no off-canvas content found on any inspected frame.
- Publishing: **ready for review, not authorized** — masters stay in this folder only; requires fellow/PM sign-off per `FELLOWS-SUBMISSION.md`

## Built under the toolkit's new submission spec

Built under the toolkit's official spec (`brutalist/docs/FELLOWS-SUBMISSION.md`, effective 2026-09-07): `ProjectName_VolunteerName.mp4` naming (no date/aspect suffix), separate `deliverables/landscape/` and `deliverables/vertical/` folders, and a true full-length 4K 2160x3840 vertical companion built via `./art vertical` + `./art final --height 3840` (not a <=180s Shorts-style cut) — every beat, no cuts, no added endcard.

## Useful project files

- `BEAT-SHEET.md` — the narrative beat sheet as drafted and approved
- `beat_sheet.json` / `vertical/beat_sheet.json` — the same plan in the pipeline's structured schema, both aspects
- `FACTCHECK.md` — claim-level review confirming the mechanism, worked example, and falsifiability case are generic/qualitative
- `SOURCES.md` — claim → source mapping
- `SHOTLIST.md` / `PROMPTS.md` — beat-by-beat medium/timing table and pantry/asset status (no pantry assets needed — all Manim)
- `scenes.py` / `vertical/scenes.py` — the Manim source for both aspects
- `BUILD-LOG.md` — dated build decisions, bugs found and fixed, and gate history
- `FRICTIONAL.md` — contemporaneous build log of what resisted and what Claude contributed
