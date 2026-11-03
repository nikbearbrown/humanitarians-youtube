# SHOTLIST — What It Promised, And What It Shipped

Typed work order. Nine beats, two deliverables (16:9 and a full-length 9:16
companion). **No open slots:** every beat is either a registered Remotion
composition or a still already composed by `make_plates.py`. Nothing is waiting
on generation, purchase or external approval.

**Lane key** — `remotion` = rendered by `remotion_scenes.py`; `still` = a PNG
composed locally and held.

| Beat | Act | Lane | Asset | Motion | In 9:16? |
|---|---|---|---|---|---|
| B00 | ASK | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B01 | THE BUNDLE | remotion | `ClaudeScienceChipGrid` | illustrate | yes → `ClaudeScienceChipGrid916` |
| B02 | THE APP | still | `pantry/B02.png` (3840×2160) | **hold** | yes → `pantry/B02-916.png` (hand-composed) |
| B03 | THE PROMISE KEPT | remotion | `ExecutedData` | illustrate | yes → `ExecutedData916` |
| B04 | THE ARITHMETIC | remotion | `TypesetMath` | illustrate | yes → `TypesetMath916` |
| B05 | THE FORK | remotion | `BinaryBranch` | illustrate | yes → `BinaryBranch916` |
| B06 | VERDICT | remotion | `ClaudeVerdictArtifact` | illustrate | yes → `ClaudeVerdictArtifact916` |
| B07 | HANDOFF | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B08 | OUTRO | remotion | `LogoOutro` | illustrate | yes → `LogoOutro916` |

Every pattern used has a registered `*916` sibling, so `shorts.py --vertical`
rewires with **no new TSX**. `ClaudeScienceLayerStack` and
`ClaudeScienceSourceFlow` — the WEEKLY-VIDEO-GUIDE default B01/B02 patterns —
have no portrait sibling and were avoided for that reason alone.

---

## Still assets — already built

Produced by `python3 make_plates.py` from the author's three supplied screen
captures, staged into `images/`. Re-run that script after any change to sources.

| Output | Size | Contents |
|---|---|---|
| `pantry/B02.png` | 3840×2160 | the full result screen at size, plus the history and about screens as thumbnails |
| `pantry/B02-916.png` | 2160×3840 | the same screen re-composed as three stacked blocks: verdict banner · boxed bird · confidence panel |

**B02 HOLDS.** It may not be given `kenburns`. `compile.py`'s zoompan pushes
roughly 8% outward, which walks the "PROTOTYPE FOR CONSERVATION RESEARCH" footer
and the Detection details panel out of frame — and both are quoted elsewhere in
the reel. Set as `shot.motion: "hold"` in the beat sheet.

**The portrait plate is a re-composition, not a crop.** A centre cut keeps the
middle ~37.5% of the width, which would discard the entire right-hand Detection
details panel — i.e. the 82% the narration says out loud. Because the two plates
order their blocks differently, narration carries **no positional reference**.

---

## Audio

One Kokoro `am_onyx` mp3 per beat, generated first and measured. Durations are
the master clock; the same mp3s serve both aspects.

| Beat | mp3 | measured |
|---|---|---|
| B00 | `mp3/beat-B00.mp3` | 14.45 s |
| B01 | `mp3/beat-B01.mp3` | 18.43 s |
| B02 | `mp3/beat-B02.mp3` | 15.19 s |
| B03 | `mp3/beat-B03.mp3` | 16.34 s |
| B04 | `mp3/beat-B04.mp3` | 16.73 s |
| B05 | `mp3/beat-B05.mp3` | 16.34 s |
| B06 | `mp3/beat-B06.mp3` | 13.70 s |
| B07 | `mp3/beat-B07.mp3` | 15.79 s |
| B08 | `mp3/beat-B08.mp3` | 2.90 s |
| | **total** | **129.87 s** |

Comfortably inside the 180 s Shorts cap, though the 9:16 here is a full-length
companion (`--vertical`) and is not capped.

---

## Deliverables

| Cut | Path | Size |
|---|---|---|
| 16:9 master | `claude-sai-what-it-promised-and-what-it-shipped.mp4` | 3840×2160 |
| 16:9 review slate | `claude-sai-what-it-promised-and-what-it-shipped-slate.mp4` | 3840×2160 |
| 9:16 master | `vertical/claude-sai-what-it-promised-and-what-it-shipped-vertical.mp4` | 2160×3840 |

Never published from here. Masters stay in the reel folder.
