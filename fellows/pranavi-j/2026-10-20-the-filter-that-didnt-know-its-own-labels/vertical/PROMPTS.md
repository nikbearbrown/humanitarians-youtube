# PROMPTS — The Filter That Didn't Know Its Own Labels

## Status: no pantry assets needed — all Manim

All 9 beats are self-contained Manim scenes in `scenes.py` (landscape) and
`vertical/scenes.py` (the native-portrait companion) — no vox stills, no
Remotion components, no generated/photographic images. There is no pantry
shopping list for this reel (see `beat_sheet.json`'s
`metadata.gates.shopping_list`: "N/A — all beats are self-contained Manim
scenes (scenes.py); no pantry stills or Remotion assets needed"). This file
is kept as the required paperwork-set placeholder (GATE F) and as a record
that no image-generation prompts were ever needed, for either the landscape
master or the vertical companion.

Every on-screen artifact (the 5-vs-6-label hook tiles, the real `SourceFeed`
enum, the real `identifySource()` dynamic-label branch, the real 2-line diff,
the real before/after TestClient table, the 2 honest-limit cards, and the
statement/brand cards) is authored directly as Manim `Text`/`MONO` mobjects,
quoted verbatim where the source material is quoted, from the real files
cited in `SOURCES.md` — `Regulatory_QA/backend/app/models.py`,
`scripts/regulatory-intel/workflow.dev.json`, `feeds.py` (commit `565e84e`),
and this session's own `verification/verify_source_feed_output.txt`.
