# SHOTLIST — "Use the Tool First."

Six beats, 122.10s. Every duration is the measured Kokoro narration length;
the visuals were cut to fit these.

| Beat | Act | In | Dur | Component | Lane | On screen |
|---|---|---|---|---|---|---|
| B00 | ASK | 0:00 | 18.97s | `ClaudeComposerAsk` | chassis | Composer card; the week's question typed in; three output lines resolve |
| B01 | SHIPPED | 0:18 | 22.72s | `HaiProgressSeriesGrid` | **new** | Six part-cards in a 3×2 grid, each with number badge, title, runtime, 4K badge, DONE check; terracotta bar counts 0:00 → 18:59 |
| B02 | CORRECTION | 0:41 | 24.43s | `HaiProgressOverturned` | **new** | Five assumptions on the left, each struck through in terracotta as its correction lands on a bordered card to the right |
| B03 | KIT | 1:06 | 23.55s | `HaiProgressKitGrid` | **new** | Counting total (23), three supporting stats, and all 23 component names as monospace chips |
| B04 | NEXT | 1:29 | 21.93s | `HaiProgressRoadmap` | **reused** | Timeline with NOW pin: two shipped items solid, two committed items dashed with due chips |
| B05 | OUTRO | 1:51 | 10.50s | `ClaudeTitleOutro` | chassis | Title, `@HumanitariansAI`, `Rohan Vijaykumar` |

## Visual rhythm

No two consecutive body beats share a shape. B01 is a grid. B02 is a paired
left-right list with a destructive motion. B03 is one big number plus a field
of small chips. B04 is a split timeline. The opener and outro are the shared
chassis, unchanged across every reel on the channel.

## Motion budget

Each new scene has exactly one thing that *happens*:

| Beat | The event | When |
|---|---|---|
| B01 | The total bar counts up to the real 18:59 | frames 116–172 |
| B02 | Each assumption is struck out as its correction arrives | staggered, 12–30 frames after each row lands |
| B03 | The component count ticks 0 → 23 | frames 20–76 |
| B04 | The NOW pin drops and splits the timeline | frame 92 (inherited) |

B02's strike-through is the only destructive motion in the reel, which is
deliberate: it is the one beat whose subject is being wrong.

## 9:16 — a native portrait re-render, not a crop

Per THE ONDA CHECK (`shorts.py`), every beat is rewired to a `916` sibling
registered at 1080×1920 and re-rendered. Each sibling re-exports the landscape
schema, so props are identical and the beat sheet carries no format-specific
content.

| Beat | Landscape | Portrait |
|---|---|---|
| B00 | `ClaudeComposerAsk` | `ClaudeComposerAsk916` (library) |
| B01 | `HaiProgressSeriesGrid` | `HaiProgressSeriesGrid916` **(new)** |
| B02 | `HaiProgressOverturned` | `HaiProgressOverturned916` **(new)** |
| B03 | `HaiProgressKitGrid` | `HaiProgressKitGrid916` **(new)** |
| B04 | `HaiProgressRoadmap` | `HaiProgressRoadmap916` (library) |
| B05 | `ClaudeTitleOutro` | `ClaudeTitleOutro916` (library) |

### How each beat reflows

| Beat | Landscape | Portrait |
|---|---|---|
| B01 | 3 columns × 2 rows | **2 × 3** — three tall rows read as a list you scan down, and each card keeps its title on one line |
| B02 | assumption and correction side by side | each pair **stacks**: struck line on top, correction card directly beneath. The two column headers collapse to one legend line |
| B03 | big count in a left column beside the chips | count becomes a **full-width banner**, the three stats a row of three beneath it, chips wrap below at smaller type |
| B04 | horizontal spine | vertical spine in the left gutter (inherited from the library sibling) |

### Portrait safe area

Content sits in the active band **y 230–1440** of 1080×1920; the top 12% and
bottom 25% are reserved for platform UI. Font sizes derive from `height`.
