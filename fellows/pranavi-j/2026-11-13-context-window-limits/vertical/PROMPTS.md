# PROMPTS — Context Window Limits: The Budget That Doesn't Grow

## Status: no pantry assets needed — all Manim

All 9 beats are self-contained Manim scenes in `scenes.py` (landscape) and `vertical/scenes.py`
(the native-portrait companion) — no vox stills, no Remotion components, no generated/photographic
images. There is no pantry shopping list for this reel (see `beat_sheet.json`'s
`metadata.gates.shopping_list`: "N/A — all beats are self-contained Manim scenes (scenes.py); no
pantry stills or Remotion assets needed"). This file is kept as the required paperwork-set
placeholder (GATE F) and as a record that no image-generation prompts were ever needed, for either
the landscape master or the vertical companion.

Every on-screen artifact — the fixed-budget hook (B02), the 3-question checklist card (B03), the
budget panels for the worked example and its falsifiability case (B04/B05), the audit checklist
(B06), and the takeaway/brand cards — is authored directly as Manim
`Text`/`Rectangle`/`Square`/`Line`/`RoundedRectangle` mobjects. Per `FACTCHECK.md` and
`SOURCES.md`, this is a general AI/STEM topic explainer: context-window capacity and overflow
behavior are well-documented, generic architectural facts, and the worked example (an illustrative
1,000-token budget shared by fixed instructions, a pasted-in document, and a growing conversation)
and its falsifiability case (the identical scenario with an explicit-error system instead) are both
fully original, illustrative scenarios — no real model, vendor, or disclosed benchmark is named,
resembled, or quoted for a specific context-window size. No image generation or external source
lookup was needed or used.
