# SHOTLIST — "Homes of Hope Songs: Proof of Concept Progress"

7 beats, 83.75s (1:23). Every duration is the measured Kokoro narration length (plus, where noted, the listening clips appended by mix_listen.py); the visuals are cut to fit the audio, never the other way round.

**Word-clock choreographed.** `align.py` (faster-whisper) measured when every word is spoken, `cues.json` names an anchor phrase per reveal, and `sync_cues.py` wrote the resolved fractions into `shot.remotion.props.cues`. 27 cues authored, 27 resolved.

The progress update for the week of 12–16 Oct: the Lyrical Literacy × Homes of Hope English + Hindi proof of concept, from Rohan V.'s project summary. Under 90 s by request; visuals only.

| Beat | Act | In | Dur | Component | Lane |
|---|---|---|---|---|---|
| B00 | ASK | 0:00 | 13.29s | `ClaudeComposerAsk` | library |
| B01 | THE METHOD | 0:13 | 10.28s | `HohCallResponse` | **new** |
| B02 | TWO TIERS | 0:23 | 13.63s | `HohTiers` | **new** |
| B03 | THE SOUND | 0:37 | 15.83s | `HaiProgressOverturned` | library |
| B04 | SAFEGUARDS | 0:53 | 14.10s | `HaiVerdictSplit` | library |
| B05 | NEXT | 1:07 | 11.48s | `HaiProgressRoadmap` | library |
| B06 | OUTRO | 1:18 | 5.14s | `HaiTitleOutro` | library |

## Choreography — what happens, and on which word

### B00 — ASK · `ClaudeComposerAsk`

> Hi, I am Row-Haan and this video is about the proof of concept we're building for Homes of Hope: songs in a girl's own language that build real English as she sings. This round is one pairing, English and Hindi.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `songs` | “songs in” | 0.419 | 5.57s |
| `english` | “build real English” | 0.564 | 7.50s |
| `pair` | “one pairing” | 0.815 | 10.83s |

### B01 — THE METHOD · `HohCallResponse`

> The method is call and response. The lead sings a line in Hindi, and the group answers with the same line in English. So every English phrase arrives with its meaning.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `method` | “call and response” | 0.058 | 0.60s |
| `lead` | “The lead sings” | 0.221 | 2.27s |
| `group` | “the group answers” | 0.454 | 4.67s |
| `meaning` | “arrives with its meaning” | 0.853 | 8.77s |

### B02 — TWO TIERS · `HohTiers`

> Each song comes in two tiers. Tier one is half Hindi, half English. Tier two is mostly English, with Hindi as a warm thread. The melody stays the same, so a girl can move up without leaving her song behind.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `two` | “two tiers” | 0.071 | 0.97s |
| `t1` | “Tier one” | 0.166 | 2.27s |
| `t2` | “Tier two” | 0.377 | 5.13s |
| `thread` | “warm thread” | 0.575 | 7.83s |
| `melody` | “The melody stays the same” | 0.665 | 9.07s |
| `up` | “move up” | 0.839 | 11.43s |

### B03 — THE SOUND · `HaiProgressOverturned`

> Two themes, four songs, drafted with Claude and generated in Suno. The first versions leaned on violin and felt too soft. I rebuilt I Will Be around dhole, tubla and sitaar, a little faster, with a strong lead and a big group answer.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `r0` | “leaned on violin” | 0.383 | 6.07s |
| `r1` | “felt too soft” | 0.461 | 7.30s |
| `r2` | “a little faster” | 0.779 | 12.33s |
| `r3` | “strong lead” | 0.868 | 13.73s |

### B04 — SAFEGUARDS · `HaiVerdictSplit`

> These are girls in care, so the songs sing about dreams and daily routines, never names, places or backstories. No real girl's voice or likeness is used. Lines about home life go to staff review first.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `showed` | “girls in care” | 0.019 | 0.27s |
| `good` | “dreams and daily” | 0.187 | 2.63s |
| `visuals` | “never names” | 0.350 | 4.93s |
| `fourk` | “No real girl's voice” | 0.570 | 8.03s |
| `pending` | “staff review” | 0.903 | 12.73s |

### B05 — NEXT · `HaiProgressRoadmap`

> The team is now choosing the strongest versions. Next: a native Hindi review, then a short proof of concept video for the pitch. If you speak Hindi fluently, I'd welcome your review.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `choosing` | “choosing the strongest” | 0.067 | 0.77s |
| `review` | “native Hindi review” | 0.357 | 4.10s |
| `video` | “proof of concept video” | 0.517 | 5.93s |
| `you` | “If you speak Hindi” | 0.726 | 8.33s |

### B06 — OUTRO · `HaiTitleOutro`

> One song, two languages, two levels. I'm Row-Haan, for Humanitarians AI.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `close` | “two levels” | 0.318 | 1.63s |

