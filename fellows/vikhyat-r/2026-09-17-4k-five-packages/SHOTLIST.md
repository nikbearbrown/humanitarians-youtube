# SHOTLIST.md — hai-4k-five-packages

Typed work order. Every beat is machine-renderable; there are no human-supplied
slots, so nothing here is owed by a person and no beat should fall to a slate.

Landscape renders at 3840×2160. Manim beats are rendered by `run.sh` at
`-r 3840,2160` (`runtime/scripts/run.sh:203-205`); Remotion beats render at
`--scale=2` from a 1920×1080 composition (`remotion_scenes.py:92`), which is
3840×2160 natively.

| Beat | Type | Owner | Renderer | Target |
|---|---|---|---|---|
| B00 | REMOTION | pipeline | `remotion_scenes.py` → `ClaudeComposerAsk` | `media/B00.mp4` |
| B01 | GRAPHIC | pipeline | Manim `B01_FourNumbers` | `manim/B01.mp4` |
| B02 | GRAPHIC | pipeline | Manim `B02_ThreePositions` | `manim/B02.mp4` |
| B03 | GRAPHIC | pipeline | Manim `B03_StarterKit` | `manim/B03.mp4` |
| B04 | GRAPHIC | pipeline | Manim `B04_Standardise` | `manim/B04.mp4` |
| B05 | GRAPHIC | pipeline | Manim `B05_DriveReport` | `manim/B05.mp4` |
| B06 | GRAPHIC | pipeline | Manim `B06_RealVsStretched` | `manim/B06.mp4` |
| B07 | GRAPHIC | pipeline | Manim `B07_SortFolders` | `manim/B07.mp4` |
| B08 | GRAPHIC | pipeline | Manim `B08_HonestAccounting` | `manim/B08.mp4` |
| B09 | REMOTION | pipeline | `remotion_scenes.py` → `ClaudeComposerAsk` | `media/B09.mp4` |
| B10 | GRAPHIC | pipeline | Manim `B10_Outro` | `manim/B10.mp4` |

## Scene intent, one line each

- **B01_FourNumbers** — one question, four answers. Four height values arrive in
  sequence, each with the file it came from beneath it. The two that are targets
  stay; the two that are not dim. One accent on the mismatch.
- **B02_ThreePositions** — a left-to-right spine: prevent, catch, detect. A
  marker travels it, and the count of people involved rises as it moves right.
- **B03_StarterKit** — two stacked cards, the pasted block and the checklist,
  then the limit line beneath in muted ink.
- **B04_Standardise** — a write being declined. The existing placeholder rule is
  shown beside it so the new rule reads as a sibling, not an invention.
- **B05_DriveReport** — a table filling row by row, then the dependency: the row
  can only be grouped because the name is in the filename.
- **B06_RealVsStretched** — a 1280×720 frame scaled into a 3840×2160 one, with an
  edge magnified so the softness is visible rather than asserted.
- **B07_SortFolders** — files routing into two folders, with the corrected value
  attached to the failing one.
- **B08_HonestAccounting** — five package cards collapsing into two build cards
  and a document.
- **B10_Outro** — title restate, terracotta period, `@HumanitariansAI` beneath.
  Silent by design (`audio_policy: "silence"`).

## Portrait note

The 9:16 companion re-lays out these Manim scenes in the short's own `scenes.py`
(`runtime/scripts/shorts.py:39-40`), rendered at `-r 2160,3840`
(`run.sh:204`). Side-by-side comparisons in B01, B04 and B06 stack vertically
in the portrait cut rather than being cropped.
