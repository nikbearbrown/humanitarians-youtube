# Weekly STEM Video: Hallucination — Why Sounding Sure Isn't the Same as Being Right

**Fellow:** Sai Pranavi Jeedigunta
**Series:** Humanitarians AI Fellows — Weekly STEM Video (`ai-explainer`)
**Source status:** General AI/STEM topic explainer, not a report of the fellow's own engineering work. Both the worked example (B04, a fabricated citation) and the falsifiability case (B05, boiling point of water) are fully generic/hypothetical illustrations — no real model, vendor, or actual paper is named or resembled. See `FACTCHECK.md` and `SOURCES.md`.

## Watch

- Landscape (4K 16:9): [Drive link](https://drive.google.com/open?id=1ToeCppowIP5ejLVhgak-G1VN-E1UYZgw)
- Vertical (4K 9:16): [Drive link](https://drive.google.com/open?id=1HYOarSjx1vokyRpw39Z2VtPrxG6c9RDi)

This video teaches a reusable 3-question rubric — **Checkable? / Would it hedge? / Does confidence track difficulty?** — for telling a model's genuine certainty apart from fluent-sounding phrasing that merely resembles certainty. The framework is shown fully before any example, walked through a worked example (a fabricated citation delivered in exactly the same confident tone as a real one), then stress-tested against a case where fluent, confident phrasing is actually warranted (a well-established fact answered correctly) so the rubric doesn't over-trigger on tone alone. It closes on a concrete task the viewer can run today.

## What this covers (and what it deliberately leaves out)

Covered: the 3-question rubric stated in full before any example; a fabricated citation and a real citation shown in visually identical fluent styling (the point is they're indistinguishable by tone alone) before one resolves "DOESN'T EXIST"; a falsifiability stress-test using a genuinely true, easy fact so the rubric doesn't collapse into "confident tone = hallucination"; a concrete audit checklist distinct from the framework card; and a closing takeaway.

Deliberately left out: this is not a benchmark of any real model's hallucination rate, and does not name or evaluate any specific real model, vendor, or product. Both illustrative examples (B04, B05) are original and generic, matching the pattern used in this fellow's prior STEM videos (prompt injection, embeddings, RAG).

## Production state

- Plan: **approved (Gate P)** — signed 2026-10-02
- Fact-check gate: **resolved** — see `FACTCHECK.md`; both B04's fabricated citation and B05's falsifiability example confirmed fully generic, no resemblance to a real disclosed incident
- Narration approval: **approved** — Kokoro `af_bella`, cleared 2026-10-02
- Voice: **Bella (`af_bella`)** — persistent for this fellow's whole series
- Previz: **complete** — 9/9 beats real Manim, no slates, both aspects
- Final render — **16:9 landscape:** `HallucinationConfidence_SaiPranaviJeedigunta.mp4`, 3840x2160, 24fps, h264/aac, **142.375s**. GATE V on the true clean master: **0 BLOCKER, 0 MAJOR**.
- Final render — **9:16 vertical (full-length, native portrait, not a Shorts cut):** `HallucinationConfidence_SaiPranaviJeedigunta.mp4`, 2160x3840, 24fps, h264/aac, **142.375s** (identical runtime to the landscape master — all 9 beats kept, no drops, no duration cap). GATE V on the true clean master: **0 BLOCKER, 0 MAJOR**.
- Personally re-verified (not just trusting the build report): extracted and viewed real frames from both masters — B02's reveal ("REAL"/"FABRICATED"), B03's 3-questions card, B04's citation pair, B05's falsifiability card, B06's checklist, B07's statement card, and B08's brand card. No text-rendering artifacts anywhere; both masters hold up at steady state.
- Publishing: **ready for review, not authorized** — masters stay in this folder only; requires fellow/PM sign-off per `FELLOWS-SUBMISSION.md`

## Built under the toolkit's new submission spec

Built under the toolkit's official spec (`brutalist/docs/FELLOWS-SUBMISSION.md`, effective 2026-09-07): `ProjectName_VolunteerName.mp4` naming (no date/aspect suffix), separate `deliverables/landscape/` and `deliverables/vertical/` folders, and a true full-length 4K 2160x3840 vertical companion built via `./art vertical` (not a ≤180s Shorts-style cut) — every beat, no cuts, no added endcard.

## Useful project files

- `BEAT-SHEET.md` — the narrative beat sheet as drafted and approved
- `beat_sheet.json` / `vertical/beat_sheet.json` — the same plan in the pipeline's structured schema, both aspects
- `FACTCHECK.md` — claim-level review confirming both illustrative examples are generic
- `SOURCES.md` — claim → source mapping
- `SHOTLIST.md` / `PROMPTS.md` — beat-by-beat medium/timing table and pantry/asset status (no pantry assets needed — all Manim)
- `scenes.py` / `vertical/scenes.py` — the Manim source for both aspects
- `BUILD-LOG.md` — dated build decisions, bugs found and fixed, and gate history
