# Weekly STEM Video: In-Context Learning — What the Prompt Can (and Can't) Teach

**Fellow:** Sai Pranavi J.
**Series:** Humanitarians AI Fellows — Weekly STEM Video (`ai-explainer`)
**Source status:** General AI/STEM topic explainer, not a report of the fellow's own engineering work. Describes a well-documented, generic capability of large language models — in-context learning, conditioning on examples/instructions given in the prompt at inference time, with no weight updates — qualitatively. No real model, vendor, or disclosed benchmark is named or resembled, no fabricated statistic is shown. The worked example (B04, a toy invented Caesar-shift substitution rule taught purely via example pairs) and its falsifiability case (B05, the same task reordered with one mapping flipped) are both fully generic/hypothetical illustrations. See `FACTCHECK.md` and `SOURCES.md`.

## Watch

- Landscape (4K 16:9): not yet uploaded — see `deliverables/landscape/InContextLearningLimits_SaiPranaviJ.mp4`
- Vertical (4K 9:16): not yet uploaded — see `deliverables/vertical/InContextLearningLimits_SaiPranaviJ.mp4`

This video teaches a reusable 3-question test — **Spot the Mapping / Shuffle the Set / Push Past the Window** — for telling what in-context learning (ICL) can actually do versus what it only looks like it's doing. The framework is taught in full before any example, walked through a worked example (a made-up Caesar-shift-by-3 rule, taught purely by 4 example pairs in a prompt, correctly applied to a brand-new input), stress-tested against a case where the same task is reordered and one mapping is flipped against the rule's own consistency (the identical new input now resolves wrong), and closed with a concrete audit task the viewer can run today against any system they have access to.

## What this covers (and what it deliberately leaves out)

Covered: a hook showing a prompt-only example set resolving a new case correctly, then posing the real question — is this learning, or locating? (B02); all 3 tests shown together, before any example (B03); a worked example (B04) where a toy rule is taught only through 4 example pairs and a new, unseen input ("RUN") resolves correctly ("UXQ"), tagged "LOCATED, NOT LEARNED"; a falsifiability case (B05) where the identical 4 examples are reordered and one mapping is flipped against the otherwise-consistent rule — the same new input now resolves wrong ("UXP"), tagged "MISMATCH"; a concrete audit task distinct from the framework card (B06); and a closing takeaway.

Deliberately left out: this is not a benchmark of any real model's in-context learning behavior, and does not name or evaluate any specific real model, vendor, or product (in-context learning — a model conditioning on prompt-given examples with no weight updates — is a well-documented, generic capability of large language models, not a single paper or vendor-specific claim). This is also a distinct topic from five adjacent, already-covered videos in this series: **not hallucination** (`2026-09-22-hallucination-why-sounding-sure-isnt-being-right`, fabrication), **not tokenization** (how text is chunked before any reasoning happens), **not lost-in-the-middle** (`2026-10-06-lost-in-the-middle-why-more-context-isnt-better`, position within a long context), **not chain-of-thought faithfulness** (`2026-10-15-chain-of-thought-why-the-reasoning-isnt-always-the-reason`, whether a stated reasoning trace caused the answer), and **not calibration** (`2026-10-21-calibration-why-confidence-isnt-accuracy`, whether a stated confidence number tracks accuracy). This video asks a different question: what can prompt-only conditioning actually teach, and where does that stop working? No specific percentage or statistic is fabricated or claimed as a real measurement anywhere — the toy substitution rule and its outcomes are illustrative.

## Illustrative content chosen for B02 / B04 / B05

**B02 (hook):** a prompt panel of 3 example pairs (a made-up letter-shift rule, never named on screen) resolving a new input ("BIG" → "ELJ") correctly, then an overlay asking the real question the rest of the video answers: is this learning, or locating? Chosen so the mechanism (pattern-completion from the prompt alone) is shown, not just asserted, before any framework is introduced.

**B04 (worked example):** the same style of toy rule, now with 4 example pairs ("CAT"→"FDW", "DOG"→"GRJ", "SUN"→"VXQ", "BIG"→"ELJ") and a brand-new, unseen input ("RUN") that resolves correctly to "UXQ" — tagged "LOCATED, NOT LEARNED" rather than implying a new fact was acquired. Chosen because a simple letter-shift cipher is a well-established, textbook-level illustrative device whose correctness is mechanically checkable on screen, with no real model/vendor named.

**B05 (falsifiability case):** the identical 4 examples, reordered, with exactly one mapping flipped against the otherwise-consistent rule ("DOG"→"GRI" instead of the consistent "GRJ"). The same new input ("RUN") is asked again — this time it resolves to "UXP" (wrong), tagged "MISMATCH". Chosen because it gives B04's clean resolution a real, visibly distinct counterpart — stress-testing the framework against a naive "a few examples always teach the model the rule" over-trigger, per `FACTCHECK.md`.

## Production state

- Plan: **approved (Gate P)** — signed 2026-10-28
- Fact-check gate: **resolved** — see `FACTCHECK.md`; kept fully generic, no real model/vendor named, no fabricated statistic
- Narration approval: **approved** — Kokoro `af_bella`, cleared 2026-10-28
- Voice: **Bella (`af_bella`)** — persistent for this fellow's whole series
- Previz: **complete** — 9/9 beats real Manim, no slates, both aspects
- Final render — **16:9 landscape:** `InContextLearningLimits_SaiPranaviJ.mp4`, **3840x2160, 24fps, h264/aac, 173.375s**. GATE V on the true clean master (verified directly, not the review slate): **0 BLOCKER, 0 MAJOR**.
- Final render — **9:16 vertical (full-length, native portrait, not a Shorts cut):** `InContextLearningLimits_SaiPranaviJ.mp4`, **2160x3840, 24fps, h264/aac, 173.375s** — identical runtime to the landscape master, all 9 beats kept, no drops, no duration cap. GATE V on the true clean master (verified directly, not the review slate): **0 BLOCKER, 0 MAJOR**.
- Publishing: **ready for review, not authorized** — masters stay in this folder only; requires fellow/PM sign-off per `brutalist/docs/FELLOWS-SUBMISSION.md`

## Built under the toolkit's new submission spec

Built under the toolkit's official spec (`brutalist/docs/FELLOWS-SUBMISSION.md`, effective 2026-09-07): `ProjectName_VolunteerName.mp4` naming (no date/aspect suffix), separate `deliverables/landscape/` and `deliverables/vertical/` folders, and a true full-length 4K 2160x3840 vertical companion built via `./art vertical` (not a <=180s Shorts-style cut) — every beat, no cuts, no added endcard.

## Useful project files

- `BEAT-SHEET.md` — the narrative beat sheet as drafted and approved
- `beat_sheet.json` / `vertical/beat_sheet.json` — the same plan in the pipeline's structured schema, both aspects
- `FACTCHECK.md` — claim-level review confirming the mechanism, worked example, and falsifiability case are generic/qualitative
- `SOURCES.md` — claim → source mapping
- `SHOTLIST.md` / `PROMPTS.md` — beat-by-beat medium/timing table and pantry/asset status (no pantry assets needed — all Manim)
- `scenes.py` / `vertical/scenes.py` — the Manim source for both aspects
- `BUILD-LOG.md` — dated build decisions, bugs found and fixed, and gate history
- `FRICTIONAL.md` — contemporaneous build log of what resisted and what Claude contributed
