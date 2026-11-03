# SHOTLIST — "How Auto-Captions Find Each Word"

8 beats, 136.73s (2:16). Every duration is the measured Kokoro narration length (plus, where noted, the listening clips appended by mix_listen.py); the visuals are cut to fit the audio, never the other way round.

**Word-clock choreographed.** `align.py` (faster-whisper) measured when every word is spoken, `cues.json` names an anchor phrase per reveal, and `sync_cues.py` wrote the resolved fractions into `shot.remotion.props.cues`. 42 cues authored, 42 resolved.

A STEM explainer for the week of 26–30 Oct: how speech recognition writes captions and times each word, tested in captions.py with faster-whisper base (the model this toolkit's align.py uses) on 24 sentences built from the narrator's voice, clean and in pink noise. B04 ends with the run's own 0 dB sentence (mix_listen.py).

| Beat | Act | In | Dur | Component | Lane |
|---|---|---|---|---|---|
| B00 | ASK | 0:00 | 14.21s | `ClaudeComposerAsk` | library |
| B01 | BACKGROUND | 0:14 | 19.65s | `CapSpectro` | **new** |
| B02 | MECHANISM | 0:33 | 16.38s | `CapTiming` | **new** |
| B03 | MEASURED | 0:50 | 20.71s | `CapAccuracy` | **new** |
| B04 | NOISE | 1:10 | 25.07s | `CapNoise` | **new** |
| B05 | THE CATCH | 1:36 | 20.48s | `CapCatch` | **new** |
| B06 | WHAT TO DO | 1:56 | 13.40s | `HaiApplyCard` | library |
| B07 | OUTRO | 2:09 | 6.83s | `HaiTitleOutro` | library |

## Choreography — what happens, and on which word

### B00 — ASK · `ClaudeComposerAsk`

> Hi, I am Row-Haan and this video is about how auto-captions find each word: how an app turns speech into text, and works out when each word was said. Our own videos depend on it. Every animation you see here is timed by it.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `text` | “speech into text” | 0.394 | 5.60s |
| `when` | “when each word was said” | 0.535 | 7.60s |
| `ours` | “Our own videos” | 0.664 | 9.43s |
| `timed` | “timed by it” | 0.934 | 13.27s |

### B01 — BACKGROUND · `CapSpectro`

> First, the sound becomes a picture: a spectrogram with eighty frequency bands, read in thirty-second chunks. The model our videos use is Whisper, an open model first trained on six hundred and eighty thousand hours of audio from the web. It looks at the picture and predicts the text, one small piece at a time.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `picture` | “becomes a picture” | 0.048 | 0.93s |
| `eighty` | “eighty frequency bands” | 0.180 | 3.53s |
| `chunks` | “thirty-second” | 0.307 | 6.03s |
| `whisper` | “is Whisper” | 0.444 | 8.73s |
| `hours` | “six hundred and eighty” | 0.606 | 11.90s |
| `predicts` | “predicts the text” | 0.847 | 16.63s |
| `piece` | “one small piece” | 0.897 | 17.63s |

### B02 — MECHANISM · `CapTiming`

> To find when each word was said, it checks where in the sound it was looking while it wrote each word, then lines those moments up in order. That method is called dynamic time warping. Here's one sentence: when each word really starts, and when Whisper says it starts.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `find` | “To find when” | 0.000 | 0.00s |
| `looking` | “where in the sound” | 0.144 | 2.37s |
| `order` | “lines those moments” | 0.352 | 5.77s |
| `dtw` | “dynamic time warping” | 0.560 | 9.17s |
| `one` | “Here's one sentence” | 0.690 | 11.30s |
| `really` | “really starts” | 0.822 | 13.47s |
| `says` | “Whisper says” | 0.912 | 14.93s |

### B03 — MEASURED · `CapAccuracy`

> I built twenty-four sentences from this narrator's voice, word by word, so I know exactly when each word starts. Whisper's base model, the one our pipeline uses, got two hundred and thirty-four of the two hundred and thirty-eight words right. Its word starts came about a quarter of a second early, and nine in ten were within three tenths of a second.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `built` | “I built twenty-four” | 0.000 | 0.00s |
| `know` | “I know exactly” | 0.222 | 4.60s |
| `base` | “base model” | 0.375 | 7.77s |
| `words` | “two hundred and thirty-four” | 0.531 | 11.00s |
| `early` | “a quarter of a second early” | 0.784 | 16.23s |
| `nine` | “nine in ten” | 0.879 | 18.20s |

### B04 — NOISE · `CapNoise`

> Then I added noise. With the speech ten decibels louder than the noise, it still got ninety-seven percent of the words. At five decibels, eighty-nine percent. With noise as loud as the speech, it fell apart: an error rate of over seventy percent. Listen to that sentence, and what it wrote.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `noise` | “added noise” | 0.013 | 0.33s |
| `ten` | “ten decibels louder” | 0.093 | 2.33s |
| `five` | “At five decibels” | 0.290 | 7.27s |
| `equal` | “as loud as the speech” | 0.421 | 10.57s |
| `rate` | “an error rate” | 0.524 | 13.13s |
| `listen` | “Listen to that sentence” | 0.612 | 15.33s |

- listening clip **NOISE AS LOUD AS THE SPEECH** `sentence_1_0db.wav` 18.54–24.27s (gain -4.10 dB to the narration's level)

### B05 — THE CATCH · `CapCatch`

> Louder noise didn't make it stop. It wrote words that were never said: over three hundred words for two hundred and thirty-eight, with phrases repeated over and over. And even on clean speech it writes what it expects. My narrator says Row-Haan, and it writes Rohan. It hears dollar, three, fifty, and writes a neat price with a dollar sign.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `stop` | “didn't make it stop” | 0.031 | 0.63s |
| `never` | “never said” | 0.153 | 3.13s |
| `count` | “over three hundred” | 0.203 | 4.17s |
| `repeat` | “repeated over and over” | 0.369 | 7.57s |
| `expects` | “writes what it expects” | 0.539 | 11.03s |
| `name` | “My narrator says” | 0.623 | 12.77s |
| `price` | “dollar, three, fifty” | 0.797 | 16.33s |

### B06 — WHAT TO DO · `HaiApplyCard`

> So read auto-captions before you publish, especially names and numbers. YouTube itself says automatic captions can get words wrong. And record somewhere quiet: a few decibels of noise make a big difference.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `read` | “read auto-captions” | 0.015 | 0.20s |
| `names` | “names and numbers” | 0.241 | 3.23s |
| `youtube` | “YouTube itself” | 0.371 | 4.97s |
| `quiet` | “somewhere quiet” | 0.707 | 9.47s |

### B07 — OUTRO · `HaiTitleOutro`

> Picture the sound, predict the words, line them up, and then check them. I'm Row-Haan, for Humanitarians AI.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `close` | “check them” | 0.444 | 3.03s |

