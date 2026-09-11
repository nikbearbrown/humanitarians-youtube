# PEDAGOGY — mycroft-rag-walkthrough (GATE P)

Weekly WORK video. Register: Teardown. Persona: Liam, in for Ameya (Kokoro
am_onyx). Channel: @HumanitariansAI.

## Through-line
The task → the pipeline I built → three levers with real numbers (chunking,
embeddings, hybrid) → where the latency actually is → the real fusion code →
three surprises → verdict → your turn.

## Beat check
- **B00 cold open** — what I built this week + the three surprises, answered up front.
- **B01 task** — 600 docs, 1,500 chunks, a 25-question golden set. Grounds the whole video.
- **B02 pipeline** — the shared shape, with "every stage traced" as the theme.
- **B03 chunking** — the biggest lever: naive → recursive, MRR 0.833 → 1.000.
- **B04 embeddings (surprise 1)** — 384-dim beat 768-dim on every axis.
- **B05 hybrid (surprise 2)** — dense adds ranking, not recall; scoped honestly.
- **B06 latency (surprise 3)** — vector search is 0.2%; optimise the cache first.
- **B07 code** — ACTUAL-CODE LAW: the real `hybrid.py` RRF fusion.
- **B08 surprises / B09 verdict / B10 your turn / B11 outro** — recap, keepers, runnable prompt, restate.

## Honesty notes
- Corpus is synthetic — stated in SOURCES/FACTCHECK; no real disclosures implied.
- The hybrid "flat hit rate" claim is scoped to the 0.0–0.3 range, matching the data.
- Every number on screen is a measured script output, not an estimate.

## Voice
Warm, plain, first-person ("what I built", "surprised me"), non-daunting. It is a
work report, so it stays concrete and modest — results first, lessons second.

## VERDICT: PASS
Real, measured, honest about scope and about the synthetic corpus; one idea per beat.
