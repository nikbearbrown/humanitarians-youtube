# SHOTLIST — "How Pitch Correction Works"

9 beats, 197.25s (3:17). Every duration is the measured Kokoro narration length (plus, where noted, the listening clips appended by mix_listen.py); the visuals are cut to fit the audio, never the other way round.

**Word-clock choreographed.** `align.py` (faster-whisper) measured when every word is spoken, `cues.json` names an anchor phrase per reveal, and `sync_cues.py` wrote the resolved fractions into `shot.remotion.props.cues`. 49 cues authored, 49 resolved.

The order is deliberate: what pitch is (B01), how it is measured (B02), how a measurement becomes a target (B03), and only then the full run (B04). B05 and B06 are the two decisions the run shows a user has to make: speed, and the key. B04 and B05 end with listening clips from the same run, so the viewer hears what the curves show.

| Beat | Act | In | Dur | Component | Lane |
|---|---|---|---|---|---|
| B00 | ASK | 0:00 | 18.35s | `ClaudeComposerAsk` | library |
| B01 | BACKGROUND | 0:18 | 22.08s | `PitchCycles` | **new** |
| B02 | MECHANISM | 0:40 | 22.91s | `PitchFindPeriod` | **new** |
| B03 | MATH | 1:03 | 20.33s | `PitchSnapCents` | **new** |
| B04 | MEASURED | 1:23 | 33.52s | `PitchMelodyFix` | **new** |
| B05 | RETUNE SPEED | 1:57 | 35.83s | `PitchRetuneSpeed` | **new** |
| B06 | THE CATCH | 2:33 | 19.67s | `PitchWrongNote` | **new** |
| B07 | WHAT TO DO | 2:52 | 16.73s | `HaiApplyCard` | library |
| B08 | OUTRO | 3:09 | 7.83s | `HaiTitleOutro` | library |

## Choreography — what happens, and on which word

### B00 — ASK · `ClaudeComposerAsk`

> Hi, I am Row-Haan and this video is about how pitch correction works: how a tool like Auto-Tune hears a note that's slightly off, and pulls it into tune. Every singer drifts a little, even good ones. The software can't hear the song the way you do. All it can do is measure, and it measures very fast.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `drift` | “Every singer drifts” | 0.507 | 9.30s |
| `measure` | “All it can do is measure” | 0.830 | 15.23s |
| `fast` | “measures very fast” | 0.923 | 16.93s |

### B01 — BACKGROUND · `PitchCycles`

> A sung note is air vibrating. The faster the vibration repeats, the higher the note sounds. The A above middle C repeats four hundred and forty times every second: four hundred and forty hertz. Double that, and you're an octave higher. Between two neighbouring piano keys, musicians count a hundred tiny steps, called cents. Pitch correction works in cents.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `air` | “air vibrating” | 0.036 | 0.80s |
| `faster` | “faster the vibration repeats” | 0.104 | 2.30s |
| `a440` | “four hundred and forty times” | 0.341 | 7.53s |
| `double` | “Double that” | 0.540 | 11.93s |
| `cents` | “called cents” | 0.848 | 18.73s |
| `works` | “Pitch correction works in cents” | 0.916 | 20.23s |

### B02 — MECHANISM · `PitchFindPeriod`

> To measure the pitch, the software slides a copy of the sound along itself. When the copy has moved by exactly one cycle, the two line up, and the difference between them drops almost to zero. That shift is one period. Here it's two point three milliseconds, so the note is four hundred and thirty hertz. The first Auto-Tune found pitch with this same idea, called autocorrelation.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `slides` | “slides a copy of the sound” | 0.071 | 1.63s |
| `lineup` | “the two line up” | 0.320 | 7.33s |
| `zero` | “drops almost to zero” | 0.422 | 9.67s |
| `period` | “That shift is one period” | 0.508 | 11.63s |
| `hz` | “four hundred and thirty hertz” | 0.720 | 16.50s |
| `first` | “The first Auto-Tune” | 0.770 | 17.63s |

### B03 — MATH · `PitchSnapCents`

> Next it turns that number into a note. Four hundred and thirty hertz sits just below A, which is four hundred and forty. How far below? Twelve hundred, times the base-two logarithm of the ratio between them: minus thirty-nine and a half cents. So the target is A, and the job is to raise this note by almost forty cents.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `note` | “turns that number into a note” | 0.018 | 0.37s |
| `below` | “just below A” | 0.200 | 4.07s |
| `how` | “How far below” | 0.359 | 7.30s |
| `log` | “base-two logarithm” | 0.515 | 10.47s |
| `minus` | “minus thirty-nine” | 0.653 | 13.27s |
| `target` | “the target is A” | 0.774 | 15.73s |

### B04 — MEASURED · `PitchMelodyFix`

> So I wrote one. I synthesised seven sung notes, each a little off, with a scoop up into every note and vibrato on the long ones. On average, forty cents out. My detector measured the pitch every six milliseconds, and the corrector pulled each note to its target. Measured again afterwards, it's under three cents out. Listen: first as sung, then corrected.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `wrote` | “So I wrote one” | 0.000 | 0.00s |
| `seven` | “seven sung notes” | 0.066 | 2.20s |
| `scoop` | “scoop up into every note” | 0.136 | 4.57s |
| `average` | “On average” | 0.236 | 7.90s |
| `measured` | “detector measured the pitch” | 0.308 | 10.33s |
| `pulled` | “pulled each note” | 0.407 | 13.63s |
| `again` | “Measured again afterwards” | 0.470 | 15.77s |
| `listen` | “Listen: first as sung” | 0.553 | 18.53s |

- listening clip **AS SUNG** `sung.wav` 22.38–27.20s (gain -14.90 dB to the narration's level)
- listening clip **CORRECTED** `corrected_instant.wav` 27.90–32.72s (gain -14.90 dB to the narration's level)

### B05 — RETUNE SPEED · `PitchRetuneSpeed`

> The setting that matters most is speed: how quickly the pitch is pulled to the target. Pull it instantly, and the slides and the vibrato vanish, leaving flat steps. That's the robotic sound Cher's song Believe made famous in 1998. Pull it slowly, over a quarter of a second, and the vibrato survives. It's nineteen cents from perfect, but it still moves like a voice. Instant, then slow.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `speed` | “matters most is speed” | 0.015 | 0.53s |
| `instantly` | “Pull it instantly” | 0.135 | 4.83s |
| `vanish` | “vibrato vanish” | 0.192 | 6.87s |
| `robotic` | “robotic sound” | 0.280 | 10.03s |
| `slowly` | “Pull it slowly” | 0.411 | 14.73s |
| `survives` | “the vibrato survives” | 0.474 | 17.00s |
| `nineteen` | “nineteen cents from perfect” | 0.531 | 19.03s |
| `listen` | “Instant, then slow” | 0.627 | 22.47s |

- listening clip **INSTANT** `corrected_instant.wav` 24.68–29.50s (gain -15.10 dB to the narration's level)
- listening clip **SLOW** `corrected_natural.wav` 30.20–35.02s (gain -15.10 dB to the narration's level)

### B06 — THE CATCH · `PitchWrongNote`

> Here's what it can't do: know which note you meant. My last note is seventy-five cents below G, which puts it closer to F sharp. Let the corrector pick from every note, and it lands, perfectly in tune, on F sharp. The wrong note. Tell it the song is in C major, where F sharp isn't allowed, and it goes to G.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `cant` | “what it can't do” | 0.015 | 0.30s |
| `seventyfive` | “seventy-five cents below G” | 0.219 | 4.30s |
| `closer` | “closer to F sharp” | 0.334 | 6.57s |
| `every` | “pick from every note” | 0.456 | 8.97s |
| `wrong` | “The wrong note” | 0.683 | 13.43s |
| `major` | “in C major” | 0.796 | 15.67s |
| `g` | “it goes to G” | 0.947 | 18.63s |

### B07 — WHAT TO DO · `HaiApplyCard`

> So if you tune a vocal for a Lyrical Literacy track, set the key and scale first. Keep the speed slow for a natural voice, and go fast only when you want the effect. Then listen all the way through. A corrector can put every note in tune. It can't make them the right notes.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `key` | “set the key and scale” | 0.183 | 3.07s |
| `slow` | “Keep the speed slow” | 0.309 | 5.17s |
| `listen` | “listen all the way through” | 0.645 | 10.80s |
| `right` | “the right notes” | 0.946 | 15.83s |

### B08 — OUTRO · `HaiTitleOutro`

> Pitch correction measures, snaps and pulls. You decide which note, and how fast. I'm Row-Haan, for Humanitarians AI.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `close` | “You decide which note” | 0.366 | 2.87s |

