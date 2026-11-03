# SHOTLIST — What It Stopped Needing

Typed work order. Nine beats, one deliverable. No open slots: every beat is
either a registered Remotion composition or a still already composed by
`make_plates.py`. Nothing is waiting on generation, purchase or approval.

**Lane key** — `remotion` = rendered by `remotion_scenes.py`; `still` = a PNG
composed locally and held.

| Beat | Act | Lane | Asset | Motion | In 9:16? |
|---|---|---|---|---|---|
| B00 | ASK | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B01 | THE OBJECT | remotion | `ClaudeScienceChipGrid` | illustrate | yes → `ClaudeScienceChipGrid916` |
| B02 | THE STATES | still | `media/B02.png` (3840×2160) | **hold** | yes → `pantry/B02-916.png` (hand-composed) |
| B03 | TWO KINDS | remotion | `DivergentFates` | illustrate | yes → `DivergentFates916` |
| B04 | THE FORK | remotion | `BinaryBranch` | illustrate | yes → `BinaryBranch916` |
| B05 | WHAT SURVIVED | remotion | `ClaudeScienceChipGrid` | illustrate | yes → `ClaudeScienceChipGrid916` |
| B06 | VERDICT | remotion | `ClaudeVerdictArtifact` | illustrate | yes → `ClaudeVerdictArtifact916` |
| B07 | HANDOFF | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B08 | OUTRO | remotion | `LogoOutro` | illustrate | yes → `LogoOutro916` |

Every pattern has a registered `916` sibling — re-verified against `Root.tsx` on
2026-09-11, not read off `scenes.json`, which lags it. The guide's default B01/B02
patterns (`ClaudeScienceLayerStack`, `ClaudeScienceSourceFlow`) still have none,
which is the only reason they are not used here.

---

## The still — already built

`media/B02.png` and `pantry/B02-916.png` are produced by `python3 make_plates.py`.
Run it under the **Anaconda `python3`** (it has Pillow; the `.venv` does not —
the audio step is the reverse).

B02 **holds**. It does not pan. The beat's argument is that the three state
strings are nearly the same width, and `compile.py`'s zoompan pushes ~8% outward,
which would destroy exactly that comparison.

The portrait plate is hand-composed rather than centre-cut. `shorts.py`'s centre
cut keeps the middle 37.5% of the width, which would slice the model and effort
text off the right of every row — i.e. remove the thing the beat is about.

**B02 is a rendering, not a screenshot**, and carries those words on its own face
in both cuts. If a real screenshot of the menu bar arrives it should replace the
plate; it must not be used to relabel the plate.

---

## Measured coverage

- landscape: ink spans 85% of frame width
- portrait: ink spans 80% of frame height

Recorded because GATE V's only check is `underfill` and these are the numbers to
compare against if it complains. Look at the frames before changing anything.
