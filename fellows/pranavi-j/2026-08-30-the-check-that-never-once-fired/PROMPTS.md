# PROMPTS — The Check That Never Once Fired

## Status: no pantry assets needed

All 9 beats are self-contained Manim scenes in `scenes.py` — no vox stills,
no Remotion components, no generated/photographic images. There is no
pantry shopping list for this reel (see `beat_sheet.json`'s
`metadata.gates.shopping_list`: "N/A — all 9 beats are self-contained Manim
scenes"). This file is kept as the required paperwork-set placeholder (GATE F)
and as a record that no image-generation prompts were ever needed.

Every on-screen code artifact (the CFTC heuristic, the full
`federalregister.gov` branch, the real filing title/link, the results
table, the before/after `identifySource()` branch) is authored directly as
Manim `Text`/`MONO` mobjects in `scenes.py`, quoted verbatim from
`/Users/pranavijs/mycroft/scripts/regulatory-intel/B2-VERIFICATION.md` and
`workflow.dev.json` (commit `d59fbd5`) — see `SOURCES.md`'s claim -> source
mapping.
