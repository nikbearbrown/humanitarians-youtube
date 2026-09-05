# SHOTLIST — "Unblocking the Team."

Six beats, 119.75s. Every duration is the measured Kokoro narration length —
the visuals were cut to fit these, not the other way round.

| Beat | Act | In | Dur | Component | Lane | On screen |
|---|---|---|---|---|---|---|
| B00 | ASK | 0:00 | 19.35s | `ClaudeComposerAsk` | chassis | Claude composer card; the week's question typed in; three output lines resolve |
| B01 | BLOCKER | 0:19 | 24.11s | `HaiProgressBlocker` | **new** | Three finished-work chips left, ink wall labelled GITHUB centre, dashed SUBMITTED zone right; wall parts at ~46%, bridge draws, chips cross |
| B02 | SHIPPED | 0:43 | 30.27s | `HaiProgressSeriesCards` | **new** | Three part-cards, each with waveform, runtime, 4K badge, DONE chip; terracotta total bar counts 0:00 → 10:35 |
| B03 | IN FLIGHT | 1:13 | 22.68s | `HaiProgressSignupChain` | **new** | Four tool cards in brand hues, linked by a drawn connector; documentation sheet slides in beneath, stamped IN PROGRESS |
| B04 | NEXT | 1:36 | 12.63s | `HaiProgressRoadmap` | **new** | Timeline, solid left / dashed right, NOW pin drops; two shipped cards, two committed cards with due chips |
| B05 | OUTRO | 1:49 | 10.71s | `ClaudeTitleOutro` | chassis | Title, `@HumanitariansAI`, `Rohan Vijaykumar` |

## Visual rhythm

No two consecutive body beats share a shape. B01 is a left-to-right journey
with an obstacle. B02 is a static lineup with a counter. B03 is a chain with a
layer arriving underneath. B04 is a split timeline. The opener and outro are the
shared chassis, unchanged from week-01.

## Motion budget

Each new scene has exactly one thing that *happens* — a single event the viewer
can point at — plus stagger-in for its elements:

| Beat | The event | When |
|---|---|---|
| B01 | The wall comes apart and the work crosses | `durationInFrames × 0.46` |
| B02 | The total bar counts up to the real figure | frames 122–178 |
| B03 | The documentation sheet slides in under the chain | `max(120, durationInFrames × 0.42)` |
| B04 | The NOW pin drops and splits the timeline | frame 92 |

B01 and B03 key their event off `durationInFrames` rather than a fixed frame, so
if narration is re-recorded at a different length the reveal stays mid-beat.
B02 and B04 settle early and hold, which is safe at any duration ≥ 7s.

## Consistency against week-01

| | Week-01 reels | This reel |
|---|---|---|
| Opener component | `ClaudeComposerAsk` | `ClaudeComposerAsk` ✓ |
| Outro component | `ClaudeTitleOutro` | `ClaudeTitleOutro` ✓ |
| Opener narration | "Hi, I'm Rohan, for Humanitarians AI." | identical ✓ |
| Closing narration | "I'm Rohan Vijaykumar, for Humanitarians AI." | identical ✓ |
| Palette | `claude` token set | identical ✓ |
| Eyebrow grammar | `HUMANITARIANS AI · <SECTION>` | `HUMANITARIANS AI · WEEKLY PROGRESS` ✓ |
| Spark line | serif italic, terracotta rule, bottom left | identical ✓ |
| Slates | none | none ✓ |

## 9:16 — a native portrait re-render, not a crop

The vertical cut is **not** derived from the landscape master. Per brutalist's
**ONDA CHECK** (`shorts.py`), every Remotion beat is rewired to a native
`<Pattern>916` composition registered at 1080×1920 and re-rendered portrait.
Scaling or padding the 16:9 master is explicitly not the method — it wastes
~60% of the frame and makes the content unreadable on a phone.

| Beat | Landscape composition | Portrait composition |
|---|---|---|
| B00 | `ClaudeComposerAsk` | `ClaudeComposerAsk916` (already in library) |
| B01 | `HaiProgressBlocker` | `HaiProgressBlocker916` **(new)** |
| B02 | `HaiProgressSeriesCards` | `HaiProgressSeriesCards916` **(new)** |
| B03 | `HaiProgressSignupChain` | `HaiProgressSignupChain916` **(new)** |
| B04 | `HaiProgressRoadmap` | `HaiProgressRoadmap916` **(new)** |
| B05 | `ClaudeTitleOutro` | `ClaudeTitleOutro916` (already in library) |

Each 916 sibling re-exports the landscape schema, so props are identical and the
beat sheet needs no per-format content.

### How each beat reflows

Reflow means rotating the composition's logic, not shrinking it:

| Beat | Landscape layout | Portrait layout |
|---|---|---|
| B01 | left → wall → right, horizontal | work on **top**, wall a full-width band across the middle, submitted **below**; the wall parts sideways and the bridge runs downward |
| B02 | 3 cards side by side | 3 cards **stacked**, each full width, badge + name + skill left, runtime + 4K right, waveform on the card's base |
| B03 | 4 cards in a row, connector horizontal | 4 cards **stacked**, connector runs vertically through the hue dots — reads as a sequence of steps |
| B04 | horizontal spine, shipped left / next right | **vertical spine** down the left gutter, shipped above the NOW pin, committed below; top-to-bottom is forward in time |

### Portrait safe area

Content lives in the active band **y 230–1440, x 54–1026** — the top 12% and
bottom 25% of a 1080×1920 frame are reserved for platform UI (captions, buttons,
handles). Nothing is centred in the full 1920, or it would sit under that
furniture. Every font size derives from `height`, so type fills the frame rather
than being inherited at landscape scale.
