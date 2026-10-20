# SHOTLIST — "How Apps Find a Song's Tempo"

9 beats, 201.83s (3:21). Every duration is the measured Kokoro narration length (plus, where noted, the listening clips appended by mix_listen.py); the visuals are cut to fit the audio, never the other way round.

**Word-clock choreographed.** `align.py` (faster-whisper) measured when every word is spoken, `cues.json` names an anchor phrase per reveal, and `sync_cues.py` wrote the resolved fractions into `shot.remotion.props.cues`. 58 cues authored, 58 resolved.

The STEM explainer for the week of 12–16 Oct: how tempo detection works, on a detector I built (tempo.py) and tested on 40 synthetic Western grooves, cross-checked against librosa. B01 ends with four seconds of the example groove (mix_listen.py).

| Beat | Act | In | Dur | Component | Lane |
|---|---|---|---|---|---|
| B00 | ASK | 0:00 | 18.05s | `ClaudeComposerAsk` | library |
| B01 | BACKGROUND | 0:18 | 22.96s | `TempoBeats` | **new** |
| B02 | MECHANISM | 0:41 | 19.05s | `TempoOnsets` | **new** |
| B03 | MATH | 1:00 | 24.51s | `TempoAutocorr` | **new** |
| B04 | MEASURED | 1:24 | 34.26s | `TempoPrior` | **new** |
| B05 | THE CATCH | 1:58 | 34.51s | `TempoGrid` | **new** |
| B06 | DRIFT | 2:33 | 26.22s | `TempoDrift` | **new** |
| B07 | WHAT TO DO | 2:59 | 16.32s | `HaiApplyCard` | library |
| B08 | OUTRO | 3:15 | 5.95s | `HaiTitleOutro` | library |

## Choreography — what happens, and on which word

### B00 — ASK · `ClaudeComposerAsk`

> Hi, I am Row-Haan and this video is about how apps find a song's tempo: the B-P-M number a DJ app or a music library shows next to a track. Nobody tells the app where the beats are. It has to hear them. And the hard part turns out not to be finding a beat. It's choosing which one.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `tells` | “Nobody tells the app” | 0.547 | 9.87s |
| `hear` | “It has to hear them” | 0.672 | 12.13s |
| `choose` | “choosing which one” | 0.938 | 16.93s |

### B01 — BACKGROUND · `TempoBeats`

> Tempo is counted in beats per minute. At a hundred and twenty B-P-M, a beat lands every half second: the place you'd tap your foot. This is four seconds of a rock groove I generated, with its beats marked. The app gets only the sound, never the marks. Here's how it sounds.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `counted` | “counted in beats per minute” | 0.028 | 0.63s |
| `half` | “every half second” | 0.232 | 5.33s |
| `tap` | “tap your foot” | 0.328 | 7.53s |
| `groove` | “four seconds of a rock groove” | 0.396 | 9.10s |
| `marked` | “with its beats marked” | 0.499 | 11.47s |
| `only` | “gets only the sound” | 0.600 | 13.77s |
| `listen` | “Here's how it sounds” | 0.711 | 16.33s |

- listening clip **ROCK GROOVE, 120 BPM** `groove_rock_120.wav` 18.16–22.16s (gain -0.80 dB to the narration's level)

### B02 — MECHANISM · `TempoOnsets`

> Step one: find where new sounds start. The sound is split into forty frequency bands, and at every moment the app asks how much louder each band just got. Add those jumps up, and you get the onset curve. A drum hit makes a spike. A held chord adds almost nothing. This is called spectral flux.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `one` | “Step one” | 0.000 | 0.00s |
| `bands` | “forty frequency bands” | 0.213 | 4.07s |
| `louder` | “how much louder” | 0.382 | 7.27s |
| `add` | “Add those jumps up” | 0.520 | 9.90s |
| `curve` | “the onset curve” | 0.607 | 11.57s |
| `spike` | “makes a spike” | 0.723 | 13.77s |
| `chord` | “A held chord” | 0.791 | 15.07s |
| `flux` | “spectral flux” | 0.940 | 17.90s |

### B03 — MATH · `TempoAutocorr`

> Step two: slide the curve against a copy of itself. At most shifts, spikes miss spikes. At some, they land on top of each other, and the match jumps. This is called autocorrelation. Here, it matches at half a second, and even better at one second. Sixty divided by half a second is a hundred and twenty beats per minute. But sixty divided by one second is sixty. Both are real repeats. So which one is the beat?

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `two` | “Step two” | 0.000 | 0.00s |
| `miss` | “spikes miss spikes” | 0.171 | 4.20s |
| `land` | “land on top” | 0.253 | 6.20s |
| `auto` | “called autocorrelation” | 0.377 | 9.23s |
| `half` | “matches at half a second” | 0.476 | 11.67s |
| `one` | “even better at one second” | 0.528 | 12.93s |
| `div` | “Sixty divided by half” | 0.598 | 14.67s |
| `sixty` | “divided by one second is sixty” | 0.779 | 19.10s |
| `which` | “which one is the beat” | 0.960 | 23.53s |

### B04 — MEASURED · `TempoPrior`

> I built a detector this way and tested it on forty grooves: rock, funk, house, hip hop, slow ballads, drum and bass, waltzes and jazz swing, five tempos each. Picking the strongest repeat, it got the tempo right on thirteen of forty. Most misses were exactly half: it locked onto the kick and snare pattern, which repeats every two beats. So, like the free library librosa, it adds a preference: tempos near a hundred and twenty count for more, roughly where people tend to tap. Now the rock grooves come out right, five of five.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `built` | “I built a detector” | 0.000 | 0.00s |
| `forty` | “forty grooves” | 0.069 | 2.37s |
| `strongest` | “Picking the strongest repeat” | 0.341 | 11.67s |
| `thirteen` | “thirteen of forty” | 0.431 | 14.77s |
| `halfmiss` | “exactly half” | 0.490 | 16.80s |
| `pattern` | “kick and snare pattern” | 0.553 | 18.93s |
| `pref` | “adds a preference” | 0.728 | 24.93s |
| `tap` | “people tend to tap” | 0.865 | 29.63s |
| `rock` | “five of five” | 0.963 | 33.00s |

### B05 — THE CATCH · `TempoGrid`

> But that preference cuts both ways. Every slow ballad came out double: sixty became a hundred and twenty. Every drum and bass groove came out half: a hundred and seventy became eighty-five. And funk's off-beat kicks pulled it to a different repeat altogether. In all: seventeen of forty exactly right, and thirty-three of forty either right or exactly double or half. librosa, run on the same forty, gave the same verdict on thirty-four. The mistake is so common it has a name, the octave error, and the standard tests score it separately.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `cuts` | “cuts both ways” | 0.018 | 0.63s |
| `ballad` | “Every slow ballad” | 0.066 | 2.27s |
| `dnb` | “Every drum and bass” | 0.207 | 7.13s |
| `funk` | “funk's off-beat” | 0.365 | 12.60s |
| `all` | “In all” | 0.474 | 16.37s |
| `octave` | “thirty-three of forty” | 0.567 | 19.57s |
| `librosa` | “run on the same forty” | 0.702 | 24.23s |
| `name` | “the octave error” | 0.903 | 31.17s |
| `tests` | “score it separately” | 0.963 | 33.23s |

### B06 — DRIFT · `TempoDrift`

> A single number has a second problem: real drummers drift. This groove starts at a hundred and twenty and ends near a hundred and twenty-three. A beat grid at one fixed tempo is more than fifty milliseconds off within six seconds, and up to a hundred and forty. A beat tracker places each beat on a strong hit while keeping the spacing steady. That's the method librosa uses, from a 2007 research paper. Half its beats land within six milliseconds.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `drift` | “real drummers drift” | 0.079 | 2.07s |
| `starts` | “starts at a hundred and twenty” | 0.160 | 4.20s |
| `grid` | “A beat grid” | 0.311 | 8.17s |
| `fifty` | “within six seconds” | 0.440 | 11.53s |
| `max` | “up to a hundred and forty” | 0.497 | 13.03s |
| `tracker` | “A beat tracker” | 0.566 | 14.83s |
| `ellis` | “2007 research paper” | 0.823 | 21.57s |
| `within` | “within six milliseconds” | 0.946 | 24.80s |

### B07 — WHAT TO DO · `HaiApplyCard`

> So when your app shows a tempo that feels wrong, check whether it's exactly half or double what you'd tap. DJ apps let you halve or double the number, or set a B-P-M range so it can't happen. And for a live recording, check the beat grid, not just the number.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `wrong` | “feels wrong” | 0.108 | 1.77s |
| `halve` | “halve or double” | 0.476 | 7.77s |
| `range` | “B-P-M range” | 0.603 | 9.83s |
| `live` | “live recording” | 0.786 | 12.83s |

### B08 — OUTRO · `HaiTitleOutro`

> Find the hits, find the repeat, then choose the beat. I'm Row-Haan, for Humanitarians AI.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `close` | “choose the beat” | 0.331 | 1.97s |

