# SHOTLIST — Who was Max Planck? (claude-liam)

Work order for all beats. `[MACHINE]` = pipeline builds it; `[REQUEST]` = human slot.

| Beat | Act | Source | Visual | Status |
|---|---|---|---|---|
| B00 | ASK (cold open) | Remotion | `ClaudeComposerAsk` — "Hallo, Liam" / command: "Who was Max Planck?" | [MACHINE] |
| B01 | THE PROBLEM | CARD | Question card: "Why doesn't a warm oven emit infinite energy?" / sub: "The Ultraviolet Catastrophe — 1890s" | [MACHINE] |
| B02 | THE GAMBIT | Manim | `B02_Graphic`: E = hν equation + quantized energy ladder (terracotta steps on cream) | [MACHINE] |
| B03 | THE ASK | Remotion | `ClaudeComposerAsk` — "The ask," / command: "plot Planck distribution vs Rayleigh-Jeans…" | [MACHINE] |
| B04 | THE RESULT | Manim | `B04_Graphic`: Planck distribution vs Rayleigh-Jeans for 5000K blackbody | [MACHINE] |
| B05 | RELUCTANT REVOLUTIONARY | CARD | Quote card: "An act of desperation." — Planck, 1900 | [MACHINE] |
| B06 | THE LEGACY | Remotion | `ClaudeWindow` artifact: "The Quantum Century" — 6-item timeline list | [MACHINE] |
| B07 | THE MAN | CARD | Endcard: biographical summary 1858–1947, Nobel 1918, tragedy | [MACHINE] |
| B08 | HANDOFF | Remotion | `ClaudeComposerAsk` — "Your turn." / command: explain UV catastrophe prompt | [MACHINE] |
| B09 | OUTRO | Remotion | `ClaudeTitleOutro` — "Who was Max Planck." / @NikBearBrown / "Liam, in for Bear." | [MACHINE] |

## Open slots (require human action or pantry drop)
None — all beats are machine-buildable on first pass. Slate cut will show Remotion scenes, Manim renders, and CARD slates. Final cut requires all Remotion renders and both Manim scenes to complete.

## Media folder layout
```
claude-liam-who-was-max-planck/
├── beat_sheet.json          # pipeline-readable (what compile.py reads)
├── beat_sheet.claude-liam.json  # scaffolding record (brand_variant.py output)
├── scenes.py                # Manim scenes B02_Graphic + B04_Graphic
├── FACTCHECK.md
├── SHOTLIST.md   (this file)
├── PROMPTS.md
├── BUILD-PROMPT.md
├── mp3/                     # generated after GATE P approval
│   └── beat-B0X.mp3
├── media/                   # Remotion renders + compile slots
│   └── B00.mp4 … B09.mp4
├── manim/                   # Manim render outputs
│   └── B02.mp4, B04.mp4
├── clips/                   # compile.py intermediate clips
└── mp4/
    ├── who-was-max-planck-slate.mp4   # review cut with labels
    └── who-was-max-planck.mp4         # final cut
```
