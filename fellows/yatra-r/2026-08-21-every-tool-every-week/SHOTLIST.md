# SHOTLIST — Every Tool, Every Week.

Typed work order. Durations are MEASURED Kokoro lengths — audio is the master clock.

Total: **10 beats · 146.8s · 2:26.8** (33.2s under the 3:00 Shorts cap, so a 9:16
derivative needs no beats cut)

| Beat | Dur | Frames | type | source | motion | Composition | Status |
|---|---|---|---|---|---|---|---|
| B00 | 12.33s | 370 | GRAPHIC | remotion | type-on | `ClaudeComposerAsk` | machine |
| B01 | 21.42s | 643 | GRAPHIC | remotion | loop | `YtwLoop` | machine |
| B02 | 16.87s | 506 | GRAPHIC | remotion | ledger | `YtwSplit` | machine |
| B03 | 6.83s | 205 | GRAPHIC | remotion | type-on | `ClaudeComposerAsk` | machine |
| B04 | 17.26s | 518 | GRAPHIC | remotion | reveal | `YtwChecks` | machine |
| B05 | 14.95s | 448 | GRAPHIC | remotion | populate | `YtwWeeks` | machine |
| B06 | 12.37s | 371 | GRAPHIC | remotion | stagger | `YtwStatus` | machine |
| B07 | 18.50s | 555 | GRAPHIC | remotion | stagger | `ClaudeVerdictArtifact` | machine |
| B08 | 18.88s | 566 | GRAPHIC | remotion | type-on | `ClaudeComposerAsk` | machine |
| B09 | 7.40s | 222 | GRAPHIC | remotion | fade | `ClaudeTitleOutro` | machine |

## Human slots: NONE

No pantry request, no archive card. Every beat is machine-renderable.

**Deliberately not requested: screenshots of the actual tools page, the LinkedIn posts, or
the Substack draft.** Those would be the obvious "evidence" for a progress report, and they
are exactly what `nopunt` calls a HOLD only if they were archival photographs of a real
event — they aren't; they're screen captures. More importantly, REBUILD LAW says a
screenshot is a placeholder, not a visual. If real screen recordings are wanted later, the
slot contract makes it a filename swap: drop `media/B04.mp4` etc. and rebuild, no re-edit.

## Scene provenance

| Composition | Source | Note |
|---|---|---|
| `YtwLoop` | NEW — `scenes/EveryToolEveryWeek.tsx` | Four labelled steps + return arrow + break mark. |
| `YtwWeeks` | NEW — same file | One named week, open-ended run of unnamed ones. Cannot express a count. |
| `YtwStatus` | NEW — same file | Document card + done/not-done rows. Cannot imply a publish date. |
| `YtwSplit` | REUSED `JdgSplit` | Generic two-column ledger, already QC'd on the previous reel. |
| `YtwChecks` | REUSED `JdgStakes` | Generic N-items-with-a-why, already QC'd. |

## Lane histogram

```
remotion (claude UI, bookends)   5 beats  B00 B03 B07 B08 B09   63.94s  44%
remotion (illustration)          5 beats  B01 B02 B04 B05 B06   82.87s  56%
manim / pantry                   0 beats
```

Motion languages: type-on 3 · loop · ledger · reveal · populate · stagger 2 · fade —
no language over MOTION.md's ~40% cap.
