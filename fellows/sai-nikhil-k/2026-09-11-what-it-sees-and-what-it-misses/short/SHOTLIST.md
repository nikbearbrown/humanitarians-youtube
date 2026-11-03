# SHOTLIST — What It Sees, And What It Misses

Typed work order. Ten beats, two deliverables. No open slots: every beat is
either a registered Remotion composition or a still already composed by
`make_plates.py`. Nothing here is waiting on generation, purchase or approval
beyond GATE P.

**Lane key** — `remotion` = rendered by `remotion_scenes.py`; `still` = a PNG
composed locally and held.

| Beat | Act | Lane | Asset | Motion | In 9:16? |
|---|---|---|---|---|---|
| B00 | ASK | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B01 | THE SET | remotion | `ClaudeScienceChipGrid` | illustrate | yes → `ClaudeScienceChipGrid916` |
| B02 | THE EVIDENCE | still | `media/B02.png` (3840×2160) | **hold** | yes → `pantry/B02-916.png` (hand-composed) |
| B03 | RIGHT AND WRONG | remotion | `DivergentFates` | illustrate | yes → `DivergentFates916` |
| B04 | FOUR FRAMES | still | `media/B04.png` (3840×2160) | **hold** | yes → `pantry/B04-916.png` (hand-composed) |
| B05 | THE FORK | remotion | `BinaryBranch` | illustrate | yes → `BinaryBranch916` |
| B06 | THE ORDER | remotion | `ClaudeScienceChipGrid` | illustrate | **NO — `--drop B06`** |
| B07 | VERDICT | remotion | `ClaudeVerdictArtifact` | illustrate | yes → `ClaudeVerdictArtifact916` |
| B08 | HANDOFF | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B09 | OUTRO | remotion | `LogoOutro` | illustrate | yes → `LogoOutro916` |

---

## Still assets — already built

Both are produced by `python3 make_plates.py` from the two supplied mosaics,
staged into `images/`. Re-run that script after any change to the sources.

| Output | Size | Contents |
|---|---|---|
| `media/B02.png` | 3840×2160 | the whole `val_batch0_pred` sheet, 16 frames, on cream |
| `pantry/B02-916.png` | 2160×3840 | 8 of those 16 cells, re-tiled 2×4, left column near / right column far |
| `media/B04.png` | 3840×2160 | 4 panels, 2×2: FOUND · COUNTED TWICE · NOT A LOON · NOT FOUND |
| `pantry/B04-916.png` | 2160×3840 | the same 4 panels stacked 1×4, left-aligned |

**Both stills HOLD.** Neither may be given `kenburns`. `compile.py`'s zoompan
pushes roughly 8% outward, which clips the outer cells of a contact sheet, and
there is no single subject to push toward. This is set as `shot.motion: "hold"`
in the beat sheet — do not "fix" it.

**Neither still may be centre-cut for 9:16.** `shorts.py`'s centre cut keeps the
middle 37.5% of the width and would remove whole columns of evidence. The
`pantry/<beat>-916.png` slot is the human override and wins over every other
path, which is why both portrait plates live there.

---

## Render order

1. `make_plates.py` — already run; outputs listed above exist.
2. GATE P — human signs `PEDAGOGY.md`.
3. `generate_audio_kokoro.py` — narration becomes the master clock.
4. `remotion_scenes.py` — the eight Remotion beats. B02 and B04 are skipped: they
   are stills, not compositions.
5. `./art run` — 4K compile + visual QC.
6. `shorts.py --drop B06 --height 3840` — the portrait deliverable.

---

## Known lint, expected, not a defect

- **`SKIN LINT: the outro is 'LogoOutro' — OUTRO LAW wants ClaudeTitleOutro`.**
  Expected. `ClaudeTitleOutro`'s handle is hardcoded to `@NikBearBrown` and
  cannot carry this series' `@HumanitariansAI`.
- **GATE V underfill on B07 and B09.** Centred verdict and logo cards trip the
  underfill heuristic every time, and on a 9:16 cut even edge-bleed warnings are
  unreliable. Look at the frames in `_qc/` before acting on either.
