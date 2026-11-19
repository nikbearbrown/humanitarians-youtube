# PROMPTS — Embedding Model Staleness: The Index That Quietly Split in Two

## Status: no pantry assets needed — all Manim

All 10 beats are self-contained Manim scenes in `scenes.py` (landscape) and `vertical/scenes.py`
(the native-portrait companion) — no vox stills, no Remotion components, no generated/photographic
images. There is no pantry shopping list for this reel (see `beat_sheet.json`'s
`metadata.gates.shopping_list`: "N/A — all beats are self-contained Manim scenes (scenes.py); no
pantry stills or Remotion assets needed"). This file is kept as the required paperwork-set
placeholder (GATE F) and as a record that no image-generation prompts were ever needed, for either
the landscape master or the vertical companion.

Every on-screen artifact — the vector-index hook (B02), the 3-question checklist card (B03), the
corpus-split panels for the worked example and its falsifiability case (B04/B05), the verbatim
real-world code-quote card (B06, quoting mycroft's actual `rag.py`/`config.py` source), the audit
checklist (B07), and the takeaway/brand cards — is authored directly as Manim
`Text`/`Rectangle`/`Square`/`Line`/`RoundedRectangle` mobjects. Per `FACTCHECK.md` and
`SOURCES.md`, this is a general AI/STEM topic explainer: embedding-model geometry incompatibility
is a well-documented, generic architectural fact, and the worked example (an illustrative
1,000-document corpus split across two embedding models) and its falsifiability case (the identical
scenario with a full re-embed instead) are both fully original, illustrative scenarios — no real
model's production accuracy is claimed as universal anywhere. The ONE quantified claim in this
video is backed by a real, reproducible local demo (`verification/embedding_staleness_demo.py`,
output captured in `verification/demo_output.txt`), not an image-generation prompt or an external
source lookup. B06's code quotes were copied verbatim from the real `mycroft` source files,
double-checked against the live source immediately before finalizing `scenes.py`, per
`FACTCHECK.md`'s verbatim accuracy check.
