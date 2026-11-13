# SHOTLIST — "How AI Music Generators Turn Text Into Audio"

9 beats, 209.13s (3:29). Every duration is the measured Kokoro narration length (plus, where noted, the listening clips appended by mix_listen.py); the visuals are cut to fit the audio, never the other way round.

**Word-clock choreographed.** `align.py` (faster-whisper) measured when every word is spoken, `cues.json` names an anchor phrase per reveal, and `sync_cues.py` wrote the resolved fractions into `shot.remotion.props.cues`. 49 cues authored, 49 resolved.

Six new data-driven scenes (`TokSampleCount` … `TokTextSteer`, shared kit `scenes/tokens/`), each drawing the real output of `codec.py`; three library scenes bookend them.

| Beat | Act | In | Dur | Component | Lane |
|---|---|---|---|---|---|
| B00 | ASK | 0:00 | 21.12s | `ClaudeComposerAsk` | library |
| B01 | BACKGROUND | 0:21 | 20.57s | `TokSampleCount` | **new** |
| B02 | MECHANISM | 0:41 | 23.74s | `TokCodebook` | **new** |
| B03 | MATH | 1:05 | 20.59s | `TokResidual` | **new** |
| B04 | MEASURED | 1:26 | 36.75s | `TokCodecQuality` | **new** |
| B05 | PREDICT | 2:02 | 21.93s | `TokNextGuess` | **new** |
| B06 | THE TEXT | 2:24 | 35.51s | `TokTextSteer` | **new** |
| B07 | WHAT TO DO | 3:00 | 20.69s | `HaiApplyCard` | library |
| B08 | OUTRO | 3:20 | 8.23s | `HaiTitleOutro` | library |

## Choreography — what happens, and on which word

### B00 — ASK · `ClaudeComposerAsk`

> Hi, I am Row-Haan and this video is about how AI music generators turn text into audio. You type a few words, and a minute later there's a song. Suno hasn't published how its own model works. But many published music generators share one idea: turn sound into tokens, and predict them one at a time, the way a chatbot writes words.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `type` | “You type a few words” | 0.276 | 5.83s |
| `suno` | “Suno hasn't published” | 0.432 | 9.13s |
| `tokens` | “turn sound into tokens” | 0.740 | 15.63s |
| `predict` | “predict them one at a time” | 0.832 | 17.57s |

### B01 — BACKGROUND · `TokSampleCount`

> Here's the problem. Digital audio is a long list of numbers, one for every tiny moment. A CD stores forty-four thousand one hundred of them every second, for each ear. A three-minute song is almost sixteen million numbers. That's far too many to predict one by one. So first, the sound has to be squeezed into a much shorter list.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `problem` | “Here's the problem” | 0.000 | 0.00s |
| `list` | “long list of numbers” | 0.120 | 2.47s |
| `cd` | “A CD stores” | 0.293 | 6.03s |
| `song` | “A three-minute song” | 0.519 | 10.67s |
| `many` | “far too many” | 0.703 | 14.47s |
| `squeezed` | “squeezed into a much shorter list” | 0.901 | 18.53s |

### B02 — MECHANISM · `TokCodebook`

> That's the job of a codec. It cuts the sound into short frames, about a hundredth of a second each. It compares each frame with a codebook: a list of one thousand and twenty-four typical sound shapes, learned from music. Then it writes down only the number of the closest one. That number is a token. A whole frame of sound becomes one number between zero and one thousand and twenty-three.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `codec` | “the job of a codec” | 0.010 | 0.23s |
| `frames` | “short frames” | 0.124 | 2.93s |
| `codebook` | “compares each frame with a codebook” | 0.272 | 6.47s |
| `learned` | “learned from music” | 0.522 | 12.40s |
| `closest` | “number of the closest one” | 0.642 | 15.23s |
| `token` | “That number is a token” | 0.718 | 17.03s |
| `range` | “between zero and one thousand” | 0.885 | 21.00s |

### B03 — MATH · `TokResidual`

> One guess is rough, so a second codebook codes what the first one missed, and a third codes what's still left. Add the pieces together, and you get closer each time. My codec makes about ninety-four frames a second. With four codebooks, that's three hundred and seventy-five tokens a second: nearly four hundred times less data than a CD.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `rough` | “One guess is rough” | 0.000 | 0.00s |
| `second` | “a second codebook” | 0.071 | 1.47s |
| `third` | “a third codes” | 0.209 | 4.30s |
| `add` | “Add the pieces” | 0.334 | 6.87s |
| `frames` | “ninety-four frames” | 0.570 | 11.73s |
| `four` | “With four codebooks” | 0.659 | 13.57s |
| `cd` | “nearly four hundred times” | 0.868 | 17.87s |

### B04 — MEASURED · `TokCodecQuality`

> So I built one, and trained its codebooks on thirty-six short pieces of music I generated. Then I coded a piece it had never heard. With one codebook, it's dull and smeared: the treble is down by seventeen decibels. With four, clearer. With twelve, the treble is down by less than six. Listen: one codebook, four, twelve, then the original.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `built` | “So I built one” | 0.000 | 0.00s |
| `never` | “never heard” | 0.180 | 6.63s |
| `one` | “With one codebook” | 0.214 | 7.87s |
| `treble` | “the treble is down” | 0.281 | 10.33s |
| `four` | “With four, clearer” | 0.349 | 12.83s |
| `twelve` | “With twelve” | 0.396 | 14.53s |
| `listen` | “Listen: one codebook” | 0.483 | 17.76s |

- listening clip **1 CODEBOOK** `codec_01_books.wav` 21.85–24.85s (gain -0.80 dB to the narration's level)
- listening clip **4 CODEBOOKS** `codec_04_books.wav` 25.55–28.55s (gain -2.10 dB to the narration's level)
- listening clip **12 CODEBOOKS** `codec_12_books.wav` 29.25–32.25s (gain -2.30 dB to the narration's level)
- listening clip **ORIGINAL** `original.wav` 32.95–35.95s (gain -2.50 dB to the narration's level)

### B05 — PREDICT · `TokNextGuess`

> Now the model. A music model reads tokens and guesses the next one. Mine is tiny: it just counts which token tends to follow each pair. On music it had never heard, it guessed the next token right sixteen and a half percent of the time. A blind guess would be right one time in a thousand. That's the whole trick, at a vastly bigger scale: learn what comes next.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `model` | “Now the model” | 0.000 | 0.00s |
| `reads` | “reads tokens” | 0.084 | 1.83s |
| `tiny` | “Mine is tiny” | 0.211 | 4.63s |
| `right` | “guessed the next token right” | 0.502 | 11.00s |
| `blind` | “A blind guess” | 0.667 | 14.63s |
| `trick` | “That's the whole trick” | 0.810 | 17.77s |

### B06 — THE TEXT · `TokTextSteer`

> And the text? In published systems, a text encoder turns your prompt into numbers that tilt every prediction. Meta's MusicGen does this: four codebooks, fifty frames a second, and a text encoder called T5 steering the model. In my toy, the words only pick which music it learned from. Calm piano, then busy drums. Neither is copied: the longest stretch it repeats from its training music is a quarter of a second.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `text` | “And the text” | 0.000 | 0.00s |
| `encoder` | “a text encoder turns your prompt” | 0.068 | 2.40s |
| `musicgen` | “Meta's MusicGen” | 0.182 | 6.47s |
| `t5` | “called T5” | 0.336 | 11.93s |
| `toy` | “In my toy” | 0.401 | 14.23s |
| `calm` | “Calm piano” | 0.497 | 17.67s |
| `copied` | “Neither is copied” | 0.568 | 20.17s |

- listening clip **CALM PIANO** `generated_piano.wav` 26.01–30.01s (gain -6.50 dB to the narration's level)
- listening clip **BUSY DRUMS** `generated_drums.wav` 30.71–34.71s (gain -4.80 dB to the narration's level)

### B07 — WHAT TO DO · `HaiApplyCard`

> So when you prompt Suno for a Lyrical Literacy track, remember: the words shift the odds, they don't write the notes. Generate a few versions and choose. Name the instruments, the mood and the tempo, because those are what the text can steer. And check the treble on headphones: when sound is squeezed into tokens, the high end is the first thing to go.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `odds` | “the words shift the odds” | 0.172 | 3.57s |
| `versions` | “Generate a few versions” | 0.325 | 6.73s |
| `name` | “Name the instruments” | 0.443 | 9.17s |
| `treble` | “check the treble” | 0.690 | 14.27s |

### B08 — OUTRO · `HaiTitleOutro`

> Sound becomes tokens, a model predicts the next one, and the words tilt the odds. I'm Row-Haan, for Humanitarians AI.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `close` | “the words tilt the odds” | 0.429 | 3.53s |

