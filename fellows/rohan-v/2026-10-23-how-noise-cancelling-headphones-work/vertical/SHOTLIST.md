# SHOTLIST — "How Noise-Cancelling Headphones Work"

8 beats, 142.36s (2:22). Every duration is the measured Kokoro narration length (plus, where noted, the listening clips appended by mix_listen.py); the visuals are cut to fit the audio, never the other way round.

**Word-clock choreographed.** `align.py` (faster-whisper) measured when every word is spoken, `cues.json` names an anchor phrase per reveal, and `sync_cues.py` wrote the resolved fractions into `shot.remotion.props.cues`. 43 cues authored, 43 resolved.

A STEM explainer for the week of 19–23 Oct: how noise-cancelling headphones work, on a headphone I simulated (anc.py: feedforward FxLMS at 48 kHz) and measured on synthetic noise. B04 ends with the hum, ANC off then on (one clip, mix_listen.py).

| Beat | Act | In | Dur | Component | Lane |
|---|---|---|---|---|---|
| B00 | ASK | 0:00 | 13.55s | `ClaudeComposerAsk` | library |
| B01 | BACKGROUND | 0:13 | 16.64s | `AncWaves` | **new** |
| B02 | MECHANISM | 0:30 | 26.22s | `AncSystem` | **new** |
| B03 | MATH | 0:56 | 22.44s | `AncPhase` | **new** |
| B04 | MEASURED | 1:18 | 26.29s | `AncTypes` | **new** |
| B05 | THE CURVE | 1:45 | 17.19s | `AncCurve` | **new** |
| B06 | WHAT TO DO | 2:02 | 13.78s | `HaiApplyCard` | library |
| B07 | OUTRO | 2:16 | 6.25s | `HaiTitleOutro` | library |

## Choreography — what happens, and on which word

### B00 — ASK · `ClaudeComposerAsk`

> Hi, I am Row-Haan and this video is about how noise-cancelling headphones work: how they can make an engine's hum nearly disappear, but still let you hear someone talking. The trick is to add more sound, not less.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `hum` | “engine's hum” | 0.435 | 5.90s |
| `talk` | “someone talking” | 0.674 | 9.13s |
| `more` | “add more sound” | 0.844 | 11.43s |

### B01 — BACKGROUND · `AncWaves`

> Sound is a wave of pressure. Add the same wave flipped upside down, and the two cancel: every high meets a low. That flipped copy is called anti-noise. Here's an engine hum at the ear, the anti-noise my simulated headphone made for it, and what's left.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `wave` | “a wave of pressure” | 0.036 | 0.60s |
| `flip` | “flipped upside down” | 0.188 | 3.13s |
| `cancel` | “the two cancel” | 0.288 | 4.80s |
| `anti` | “called anti-noise” | 0.545 | 9.07s |
| `hum` | “Here's an engine hum” | 0.647 | 10.77s |
| `made` | “the anti-noise my simulated” | 0.759 | 12.63s |
| `left` | “what's left” | 0.954 | 15.87s |

### B02 — MECHANISM · `AncSystem`

> A microphone on the outside of the ear cup hears the noise first. A chip turns it into anti-noise and plays it through the speaker. Many headphones also have a microphone inside, listening to what's left. My simulated one uses it to keep adjusting its filter, forty-eight thousand times a second. The noise takes eighty-three microseconds to reach the ear, and the electronics take a hundred and twenty-five. So the chip has to predict a little of the future.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `outside` | “on the outside” | 0.019 | 0.50s |
| `chip` | “A chip turns it” | 0.141 | 3.70s |
| `speaker` | “through the speaker” | 0.230 | 6.03s |
| `inside` | “a microphone inside” | 0.327 | 8.57s |
| `adjust` | “keep adjusting” | 0.515 | 13.50s |
| `rate` | “forty-eight thousand” | 0.582 | 15.27s |
| `noise` | “The noise takes” | 0.674 | 17.67s |
| `elec` | “the electronics take” | 0.806 | 21.13s |
| `predict` | “predict a little” | 0.945 | 24.77s |

### B03 — MATH · `AncPhase`

> Being a little late matters more at high pitch. A timing error of a tenth of a millisecond is a tiny slice of a hundred-hertz wave: three point six degrees, and the hum still drops twenty-four decibels. At two thousand hertz, the same delay is seventy-two degrees, and the anti-noise now adds to the noise. Past sixty degrees, there's no cancellation at all.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `late` | “a little late” | 0.006 | 0.13s |
| `error` | “a tenth of a millisecond” | 0.163 | 3.67s |
| `hundred` | “a hundred-hertz wave” | 0.270 | 6.07s |
| `drops` | “still drops” | 0.444 | 9.97s |
| `two` | “At two thousand” | 0.554 | 12.43s |
| `adds` | “adds to the noise” | 0.786 | 17.63s |
| `sixty` | “Past sixty” | 0.860 | 19.30s |

### B04 — MEASURED · `AncTypes`

> I ran four kinds of noise through my simulated headphone. Engine hum: twenty-five decibels quieter. Low rumble: thirty-one. Voices: only eleven. Clatter: none at all, in fact slightly louder. Steady, low sounds are predictable, so the chip can stay ahead of them. Sudden sounds aren't. Listen: the hum without it, then with it.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `four` | “four kinds of noise” | 0.011 | 0.30s |
| `engine` | “Engine hum” | 0.134 | 3.53s |
| `rumble` | “Low rumble” | 0.255 | 6.70s |
| `voices` | “Voices” | 0.322 | 8.47s |
| `clatter` | “Clatter” | 0.389 | 10.23s |
| `steady` | “Steady, low sounds” | 0.497 | 13.07s |
| `sudden` | “Sudden sounds” | 0.648 | 17.03s |
| `listen` | “Listen” | 0.691 | 18.17s |

- listening clip **ENGINE HUM: ANC OFF, THEN ON** `engine_off_then_on.wav` 21.48–25.48s (gain -10.50 dB to the narration's level)

### B05 — THE CURVE · `AncCurve`

> Across every pitch at once, the pattern is clear. At least ten decibels quieter up to about three hundred hertz, a little quieter up to three thousand, and above that, slightly louder. Real headphones handle those high sounds the old way: the ear cups and tips simply block them.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `every` | “Across every pitch” | 0.000 | 0.00s |
| `ten` | “At least ten” | 0.188 | 3.23s |
| `little` | “a little quieter” | 0.398 | 6.83s |
| `louder` | “slightly louder” | 0.560 | 9.63s |
| `cups` | “the ear cups and tips” | 0.869 | 14.93s |

### B06 — WHAT TO DO · `HaiApplyCard`

> So use noise-cancelling for steady noise: planes, trains, air conditioning. Get a good seal, because the cups and tips do the high frequencies. And with the hum gone, turn your music down: you don't have to play over it.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `steady` | “steady noise” | 0.111 | 1.53s |
| `seal` | “good seal” | 0.426 | 5.87s |
| `down` | “turn your music down” | 0.798 | 11.00s |

### B07 — OUTRO · `HaiTitleOutro`

> Flip the wave, stay ahead of it, and let the cups do the rest. I'm Row-Haan, for Humanitarians AI.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `close` | “do the rest” | 0.368 | 2.30s |

