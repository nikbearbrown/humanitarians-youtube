# SHOTLIST — The Bottleneck Moved.

Typed work order. `shot.type` is locked (presentation form — never changes when media
swaps); `shot.source` is late-bound (provenance — swappable). Durations are MEASURED
Kokoro lengths, not estimates: audio is the master clock.

Total: **10 beats · 140.5s · 2:20.5**

| Beat | Dur | type | source | motion | Composition | Fills from | Status |
|---|---|---|---|---|---|---|---|
| B00 | 12.16s | GRAPHIC | remotion | type-on | `ClaudeComposerAsk` | pipeline | machine |
| B01 | 16.64s | GRAPHIC | remotion | illustrate | `BnkSplit` | pipeline | machine |
| B02 | 14.31s | GRAPHIC | remotion | illustrate | `BnkCosts` | pipeline | machine |
| B03 | 6.04s | GRAPHIC | remotion | type-on | `ClaudeComposerAsk` | pipeline | machine |
| B04 | 14.06s | GRAPHIC | remotion | illustrate | `BnkFunnel` | pipeline | machine |
| B05 | 16.62s | GRAPHIC | remotion | illustrate | `BnkCutoff` | pipeline | machine |
| B06 | 16.64s | GRAPHIC | remotion | illustrate | `BnkBranch` | pipeline | machine |
| B07 | 18.82s | GRAPHIC | remotion | stagger | `ClaudeVerdictArtifact` | pipeline | machine |
| B08 | 19.22s | GRAPHIC | remotion | type-on | `ClaudeComposerAsk` | pipeline | machine |
| B09 | 5.95s | GRAPHIC | remotion | fade | `ClaudeTitleOutro` | pipeline | machine |

## Human slots: NONE

There is no `pantry/` shopping list for this reel and no archive request card, by design.
Every beat is machine-renderable, which `./art todo` confirms independently: **10/10 routed
to the pipeline, 0 human slots, 0 "free fallback (Higgsfield would upgrade this)" beats.**

That is the correct outcome under `nopunt`'s one rule: a HOLD is legitimate only when a beat
needs a genuine archival **photograph** of a real person, place, document, or event. This
reel argues from a model — it has no such beat. A still or a stock image anywhere in this
sheet would have been a PUNT, not a HOLD.

## Provenance

No sidecars required — no `archive` or `ai` sourced media. Every frame is a deterministic
render of committed scene source (`source: remotion`), so the reel is reproducible from the
repo alone: same beat sheet + same commit → identical frames.

## Lane histogram

```
remotion (claude UI, bookends)  5 beats   B00 B03 B07 B08 B09    62.19s   44%
remotion (illustration, C2)     5 beats   B01 B02 B04 B05 B06    78.27s   56%
manim                           0 beats
vox / pantry stills             0 beats
```

Rhythm check: no more than two consecutive beats share a visual scheme. The UI beats are
spaced by ILLUSTRATE LAW (cold open, ask micro-beat, verdict, handoff, outro) and never sit
adjacent except at the B07→B08→B09 close, which is the invariant bookend run.

## Duration ladder risk

Each `Bnk*` composition is registered at exactly its beat's measured frame count, so
`compile.py`'s conform step should be a no-op rather than a retime. Any beat that reports a
retime or freeze-pad at compile means a composition's `durationInFrames` drifted from the
mp3 — regenerate audio and re-register, never hand-tune.
