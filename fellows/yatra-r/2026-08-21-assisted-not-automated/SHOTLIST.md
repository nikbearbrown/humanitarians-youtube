# SHOTLIST — Assisted, Not Automated.

Typed work order. Durations are MEASURED Kokoro lengths — audio is the master clock.

Total: **24 beats · 327.6s · 5:27.6**

| Beat | Dur | Frames | motion | Composition | Act |
|---|---|---|---|---|---|
| B00 | 13.61s | 408 | type-on | `ClaudeComposerAsk` | ASK |
| B01 | 24.53s | 736 | diverge | `SeoLead` | EXECUTIVE SUMMARY (BLUF) |
| B02 | 3.05s | 92 | card | `SeoAct` | ACT One CARD |
| B03 | 14.49s | 435 | grow | `SeoCompare` | STAT — ADOPTION |
| B04 | 17.58s | 527 | reveal | `SeoReasons` | WHY — STRUCTURAL |
| B05 | 16.53s | 496 | stack | `SeoStakes` | NUANCE |
| B06 | 3.58s | 107 | card | `SeoAct` | ACT Two CARD |
| B07 | 16.00s | 480 | grow | `SeoCompare` | STAT — SPEND & INTENT |
| B08 | 14.44s | 433 | collapse | `SeoDrop` | STAT — THE COLLAPSE |
| B09 | 17.09s | 513 | ledger | `SeoSplit` | CONSEQUENCE |
| B10 | 3.52s | 106 | card | `SeoAct` | ACT Three CARD |
| B11 | 9.28s | 278 | type-on | `ClaudeComposerAsk` | ASK (ask→result pair) |
| B12 | 14.59s | 438 | nest | `SeoShare` | RESULT — THE SPLIT |
| B13 | 14.53s | 436 | count | `SeoStat` | STAT — AT THE TOP |
| B14 | 14.40s | 432 | ledger | `SeoSplit` | THE TWIST |
| B15 | 3.56s | 107 | card | `SeoAct` | ACT Four CARD |
| B16 | 14.55s | 436 | count | `SeoStat` | STAT — PRICING |
| B17 | 15.04s | 451 | reveal | `SeoStakes` | THE NEW SHAPE |
| B18 | 16.34s | 490 | ledger | `SeoSplit` | ROLES |
| B19 | 19.16s | 575 | reveal | `SeoWatch` | FALSIFIABILITY |
| B20 | 12.42s | 373 | stagger | `SeoSources` | SOURCES |
| B21 | 22.66s | 680 | stagger | `ClaudeVerdictArtifact` | VERDICT |
| B22 | 21.31s | 639 | type-on | `ClaudeComposerAsk` | HANDOFF |
| B23 | 5.38s | 161 | fade | `ClaudeTitleOutro` | OUTRO |

## Human slots: NONE

Every beat is machine-renderable. There is no `pantry/` shopping list — which is itself the
genre deviation recorded in `BUILD-LOG.md`: a compliant `deep-explainer` would have 20–25%
VOX beats waiting on human-supplied stills and a Gate D2 SHOPPING.md to match. Neither
exists here because vox sourcing is unavailable on this machine, so there is nothing to
shop for.

## Composition sharing — why frame counts are set to the SHORTEST beat

Several beats share one composition (`SeoAct` ×4, `SeoSplit` ×3, `SeoCompare` ×2,
`SeoStat` ×2, `SeoStakes` ×2). A Remotion composition has a single `durationInFrames`, so
the shared value was set to the **shortest** beat each composition backs.

That direction matters. `remotion_scenes.py` freeze-extends a clip that is shorter than its
beat (lossless), while `compile.py`'s duration ladder trims one that is longer (lossy).
Sizing to the longest beat would therefore have cut the tail off every shorter beat — and
on these scenes the source citation lands at 80–90% of the span, so the trimmed material
would have been exactly the citations. Sizing to the shortest means longer beats hold their
completed final frame instead.

## Lane histogram

```
Claude UI (bookends + ask micro)   5 beats   B00 B11 B21 B22 B23
Stat scenes (cited figures)        6 beats   B03 B07 B08 B12 B13 B16
Structural / ledger / list         8 beats   B01 B04 B05 B09 B14 B17 B18 B19
Act cards                          4 beats   B02 B06 B10 B15
Sources card                       1 beat    B20
```

Motion languages: card 4 · type-on 3 · reveal 3 · ledger 3 · grow 2 · count 2 · stagger 2 ·
diverge · stack · collapse · nest · fade — none over MOTION.md's ~40% cap.

## Formats

- **16:9** — 3840×2160, delivered.
- **9:16** — full length for TikTok, derived with `./art shorts --drop` (explicit empty drop
  plan) so the 3:00 auto-cut does not fire. Deliberately too long for YouTube Shorts and
  Instagram Reels.
