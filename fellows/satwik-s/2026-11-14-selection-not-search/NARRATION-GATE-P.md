# NARRATION — GATE P — Week 16: Selection, Not Search

Voice: Kokoro `af_bella` ("Bella"). Register: pragmatist / skeptical-explainer. Numbers spelled out for TTS; digits live in the on-screen props. Greeting "Hello, fellows"; sign-off "This is Satwik for Humanitarians AI."

- **B00 (hook/ASK):** the design claim is selection, not retrieval; the fair test — rank by similarity, see if you get the matcher's list; ablation at Stage 4b, no sequencing.
- **B01 (two arms):** retrieval = top-K by similarity / selection = shares a specific project term + role label; only difference is the selection signal.
- **B02 (two signals):** similarity (paraphrase-tolerant, imprecise, topical) vs shared vocabulary (precise); relevance is a vocabulary property, not a distance property.
- **B03 (the figure):** of the top-20 similar, 85% (17/20) LNP and 60% (12/20) photothermal share no project vocabulary.
- **B04 (robust):** K-sweep LNP 90/85/83%, photothermal 80/60/57%; holds at every K.
- **B05 (structure):** selects 32 / 26 with roles (core/method/background/optional); role from which metadata category overlapped.
- **B06 (weights):** role = category membership (structural), not a tuned threshold; weights only order within a role.
- **B07 (exclusion log):** 864 / 559 excluded; 109 / 63 high-similarity-no-vocabulary (CH28-S02-SS02 / CH28-S01); exactly what top-k would return.
- **B08 (honest boundary):** general embedder; draft metadata; two projects; isolates Stage 4b; no learning claim.
- **B09 (outro):** selection, not search; the proof is the list of what it rejected, and why.

GATE P: PASS (see PEDAGOGY.md). Cleared for audio.
