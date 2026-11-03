# BUILD-LOG — claude-liam-meet-muse

**Built by Claude in Claude Code.**

- **Muse interface.** No Muse capture exists, so the presenter chose a labelled generic stand-in (2026-10-13).
- **Body scenes.** Drawn by `scenes.py`, natively in 16:9 and 9:16. The library had no Blender interface or agent panel, and no dual-aspect diagrams for these ideas.
  - Type sizes meet the GATE T floors: x-height of at least 45 px in landscape and 80 px in portrait.
  - Every scene was previewed in both aspects. Overflows found in portrait (badge, command, tags, comparison cards, problem cards) were fixed before rendering.
- **Environment.** The scratchpad virtualenv and the `/tmp/espk-data` espeak workaround were rebuilt after a session restart.
- **Toolkit.** Uses the earlier one-line toolkit change in `ClaudeTitleOutro916.tsx`, which enlarged the portrait outro handle.
- **Fellows rebrand (2026-10-13).** Per the presenter: the film was refocused on what Muse is, what it can do and how it is useful, and the "next video" beat (B13) was dropped. Branding is Yeshwanth Balaji · @HumanitariansAI. The recap and outro were redrawn in `scenes.py`. Narration was regenerated, and both aspects were re-rendered and passed GATE T and Gate V. The vertical was compiled with `--height 3840`, because the default 2160 downscale caused edge-bleed.
