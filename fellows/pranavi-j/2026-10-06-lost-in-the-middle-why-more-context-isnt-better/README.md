# Weekly STEM Video: Lost in the Middle — Why More Context Doesn't Guarantee a Better Answer

**Fellow:** Sai Pranavi J.
**Series:** Humanitarians AI Fellows — Weekly STEM Video (`ai-explainer`)
**Source status:** General AI/STEM topic explainer, not a report of the fellow's own engineering work. Describes the well-documented "lost in the middle" effect in long-context language models qualitatively — no real model or vendor is named or benchmarked, no fabricated percentage/statistic is shown. The worked example (B04, a generic onboarding document with one buried fact) and its falsifiability case (B05) are fully generic/hypothetical illustrations. See `FACTCHECK.md` and `SOURCES.md`.

## Watch

- Landscape (4K 16:9): [Drive link](https://drive.google.com/open?id=1zoL5MUv2rWUBhPaSmHxYW3hPNLM3qBMy)
- Vertical (4K 9:16): [Drive link](https://drive.google.com/open?id=1csr0G_Ogi7hQ9jFFSXlbiYSjw3hspAWx)

This video teaches a reusable 3-question rubric — **How long is the context? / Where does the key fact actually sit? / Would moving it change whether it's found?** — for noticing when a long-context prompt has put something important in a position a model is less reliable at using. The mechanism is shown as a real plotted U-shaped attention-strength curve (not just asserted in narration) before any example, walked through a worked example (the same fact, same document, same question, buried in the middle — the model misses it), stress-tested with a falsifiability case (the same fact moved to the start — the model finds it), and closed with a concrete task the viewer can run today.

## What this covers (and what it deliberately leaves out)

Covered: a real U-shaped attention-strength diagram (B03) — a horizontal bar representing a long context with a plotted curve high at both ends, dipping in the middle, no numeric axis values; a worked example (B04) where a buried fact in the middle of a generic onboarding document is missed; a falsifiability case (B05) where the identical fact, document, and question — only repositioned near the start — is reliably found; a 3-question checklist distinct from the mechanism diagram; and a closing takeaway.

Deliberately left out: this is not a benchmark of any real model's long-context behavior, and does not name or evaluate any specific real model, vendor, or product (the exact shape and severity of the effect varies by model and has shifted over time as providers have worked to mitigate it — see `SOURCES.md`). The worked example and its falsifiability case are both original and generic, matching the pattern used in this fellow's prior STEM videos (tokenization, hallucination). No specific percentage or statistic is fabricated or shown anywhere.

## Production state

- Plan: **approved (Gate P)** — signed 2026-10-06
- Fact-check gate: **resolved** — see `FACTCHECK.md`; kept fully qualitative, no specific stats, no real model named
- Narration approval: **approved** — Kokoro `af_bella`, cleared 2026-10-06
- Voice: **Bella (`af_bella`)** — persistent for this fellow's whole series
- Previz: **complete** — 9/9 beats real Manim, no slates, both aspects
- Final render — **16:9 landscape:** `LostInTheMiddle_SaiPranaviJ.mp4`, 3840x2160, 24fps, h264/aac, **140.33s**. GATE V on the true clean master: **0 BLOCKER, 0 MAJOR**.
- Final render — **9:16 vertical (full-length, native portrait, not a Shorts cut):** `LostInTheMiddle_SaiPranaviJ.mp4`, 2160x3840, 24fps, h264/aac, **140.33s** (identical runtime to the landscape master — all 9 beats kept, no drops, no duration cap). GATE V on the true clean master: **0 BLOCKER, 0 MAJOR**.
- Personally re-verified (not just trusting the build report): extracted and viewed real frames from both masters at every beat — B02's short-vs-long document reveal, B03's U-shaped attention curve, B04's buried-fact miss, B05's repositioned-fact find, B06's checklist, B07's statement card, and B08's brand card. No text-rendering artifacts anywhere; both masters hold up at steady state.
- Publishing: **ready for review, not authorized** — masters stay in this folder only; requires fellow/PM sign-off per `FELLOWS-SUBMISSION.md`

## Built under the toolkit's new submission spec

Built under the toolkit's official spec (`brutalist/docs/FELLOWS-SUBMISSION.md`, effective 2026-09-07): `ProjectName_VolunteerName.mp4` naming (no date/aspect suffix), separate `deliverables/landscape/` and `deliverables/vertical/` folders, and a true full-length 4K 2160x3840 vertical companion built via `./art vertical` (not a <=180s Shorts-style cut) — every beat, no cuts, no added endcard.

## Useful project files

- `BEAT-SHEET.md` — the narrative beat sheet as drafted and approved
- `beat_sheet.json` / `vertical/beat_sheet.json` — the same plan in the pipeline's structured schema, both aspects
- `FACTCHECK.md` — claim-level review confirming the mechanism and worked example are generic/qualitative
- `SOURCES.md` — claim → source mapping
- `SHOTLIST.md` / `PROMPTS.md` — beat-by-beat medium/timing table and pantry/asset status (no pantry assets needed — all Manim)
- `scenes.py` / `vertical/scenes.py` — the Manim source for both aspects
- `BUILD-LOG.md` — dated build decisions, bugs found and fixed, and gate history
