# SHOTLIST — "How Shazam Finds a Song"

9 beats, 202.40s (3:22). Every duration is the measured Kokoro narration length (plus, where noted, the listening clips appended by mix_listen.py); the visuals are cut to fit the audio, never the other way round.

**Word-clock choreographed.** `align.py` (faster-whisper) measured when every word is spoken, `cues.json` names an anchor phrase per reveal, and `sync_cues.py` wrote the resolved fractions into `shot.remotion.props.cues`. 56 cues authored, 56 resolved.

Six new data-driven scenes (`ShazamPeaks` … `ShazamVersions`, shared kit `scenes/shazam/`), each drawing the real output of `fingerprint.py`; three library scenes bookend them.

| Beat | Act | In | Dur | Component | Lane |
|---|---|---|---|---|---|
| B00 | ASK | 0:00 | 18.30s | `ClaudeComposerAsk` | library |
| B01 | BACKGROUND | 0:18 | 26.33s | `ShazamPeaks` | **new** |
| B02 | MECHANISM | 0:44 | 25.37s | `ShazamHashPairs` | **new** |
| B03 | MATH | 1:10 | 21.57s | `ShazamOffsetVote` | **new** |
| B04 | MEASURED | 1:31 | 36.42s | `ShazamMatch` | **new** |
| B05 | NOISE | 2:07 | 21.42s | `ShazamNoiseSweep` | **new** |
| B06 | THE CATCH | 2:29 | 23.57s | `ShazamVersions` | **new** |
| B07 | WHAT TO DO | 2:52 | 20.74s | `HaiApplyCard` | library |
| B08 | OUTRO | 3:13 | 8.68s | `HaiTitleOutro` | library |

## Choreography — what happens, and on which word

### B00 — ASK · `ClaudeComposerAsk`

> Hi, I am Row-Haan and this video is about how Shazam finds a song: how an app can hear five seconds of music in a noisy room, and name the exact recording. It doesn't listen the way you do. It doesn't know the melody or the words. It looks for a handful of loud points, and the timing between them.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `listen` | “doesn't listen the way you do” | 0.565 | 10.33s |
| `points` | “handful of loud points” | 0.834 | 15.27s |
| `timing` | “the timing between them” | 0.929 | 17.00s |

### B01 — BACKGROUND · `ShazamPeaks`

> First, the sound becomes a spectrogram. Time runs left to right, pitch runs bottom to top, and darker means louder. Then almost all of it is thrown away. Only the points that are louder than everything around them are kept: about twelve every second. The 2003 paper that described Shazam's method calls this a constellation map. In my test, with noise as loud as the music, twenty-four of these forty points survived. That's enough to work with.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `spec` | “becomes a spectrogram” | 0.033 | 0.87s |
| `time` | “Time runs left to right” | 0.098 | 2.57s |
| `pitch` | “pitch runs bottom to top” | 0.158 | 4.17s |
| `darker` | “darker means louder” | 0.215 | 5.67s |
| `thrown` | “thrown away” | 0.315 | 8.30s |
| `kept` | “are kept” | 0.447 | 11.77s |
| `twelve` | “about twelve” | 0.481 | 12.67s |
| `constellation` | “constellation map” | 0.686 | 18.07s |
| `noise` | “with noise as loud” | 0.777 | 20.47s |
| `survive` | “twenty-four of these forty” | 0.855 | 22.50s |

### B02 — MECHANISM · `ShazamHashPairs`

> One point on its own says very little. So each point becomes an anchor, and is paired with a few points just after it. Each pair gives three numbers: the first frequency, the second frequency, and the time between them. Here: seven hundred and eighty-six hertz, then eleven hundred and seventy-four hertz, five hundredths of a second later. Those three numbers are packed into one code, called a hash. My version makes about fifty-seven of them every second.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `one` | “One point on its own” | 0.000 | 0.00s |
| `anchor` | “becomes an anchor” | 0.113 | 2.87s |
| `paired` | “paired with a few points” | 0.158 | 4.00s |
| `three` | “three numbers” | 0.275 | 6.97s |
| `here` | “Here:” | 0.482 | 12.23s |
| `packed` | “packed into one code” | 0.792 | 20.10s |
| `hash` | “called a hash” | 0.845 | 21.43s |
| `rate` | “fifty-seven of them” | 0.941 | 23.87s |

### B03 — MATH · `ShazamOffsetVote`

> To search, the app makes hashes from your clip and looks each one up. Plenty of songs share a few hashes by chance. The trick is timing. For every match, take the time in the song and subtract the time in your clip. If the clip really comes from that song, the answers agree: they all point to the same moment. A real match is one tall spike. Chance matches are scattered.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `search` | “To search” | 0.000 | 0.00s |
| `chance` | “by chance” | 0.244 | 5.27s |
| `timing` | “The trick is timing” | 0.298 | 6.43s |
| `subtract` | “subtract the time” | 0.470 | 10.13s |
| `agree` | “the answers agree” | 0.655 | 14.13s |
| `spike` | “one tall spike” | 0.852 | 18.37s |
| `scattered` | “Chance matches are scattered” | 0.933 | 20.13s |

### B04 — MEASURED · `ShazamMatch`

> So I built one. I made six songs from scratch, forty seconds each, and indexed them: about fourteen thousand hashes. Then I took five seconds of Song C, starting at twelve seconds, and buried it in cafe noise as loud as the music, through a phone-quality filter. Song C got thirty-three votes, at exactly twelve seconds. The next best song got two. Listen: the noisy clip, then the original.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `built` | “So I built one” | 0.000 | 0.00s |
| `six` | “six songs from scratch” | 0.044 | 1.60s |
| `indexed` | “indexed them” | 0.114 | 4.13s |
| `took` | “five seconds of Song C” | 0.216 | 7.87s |
| `buried` | “buried it in cafe noise” | 0.306 | 11.13s |
| `votes` | “thirty-three votes” | 0.465 | 16.93s |
| `next` | “The next best song” | 0.537 | 19.57s |
| `listen` | “Listen: the noisy clip” | 0.595 | 21.67s |

- listening clip **NOISY CLIP** `clip_cafe.wav` 24.92–29.92s (gain +3.30 dB to the narration's level)
- listening clip **ORIGINAL** `original_segment.wav` 30.62–35.62s (gain +2.90 dB to the narration's level)

### B05 — NOISE · `ShazamNoiseSweep`

> How much noise can it take? I ran thirty random clips at each noise level. With the music ten decibels louder than the noise, all thirty were found. With noise as loud as the music, twenty-nine. With the noise five decibels louder, twenty-two. Ten decibels louder, nine. And when it failed, it said no match. It never named the wrong song.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `how` | “How much noise” | 0.000 | 0.00s |
| `ran` | “thirty random clips” | 0.101 | 2.17s |
| `ten` | “ten decibels louder than the noise” | 0.249 | 5.33s |
| `zero` | “noise as loud as the music” | 0.423 | 9.07s |
| `five` | “five decibels louder, twenty-two” | 0.601 | 12.87s |
| `tenl` | “Ten decibels louder, nine” | 0.702 | 15.03s |
| `failed` | “when it failed” | 0.823 | 17.63s |
| `never` | “It never named” | 0.923 | 19.77s |

### B06 — THE CATCH · `ShazamVersions`

> Here's what this kind of fingerprint can't do: it matches one exact recording, not the song. I played the same song again, one semitone higher: one vote. Six percent faster: four. The melody alone, hummed: one. To the fingerprint, those are different recordings, because every frequency and every gap has moved. Apps that recognise humming use a different kind of fingerprint, built on the melody.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `cant` | “can't do” | 0.045 | 1.07s |
| `exact` | “one exact recording” | 0.113 | 2.67s |
| `semitone` | “one semitone higher” | 0.283 | 6.67s |
| `faster` | “Six percent faster” | 0.388 | 9.13s |
| `hummed` | “The melody alone, hummed” | 0.482 | 11.37s |
| `moved` | “every gap has moved” | 0.743 | 17.50s |
| `apps` | “Apps that recognise humming” | 0.820 | 19.33s |

### B07 — WHAT TO DO · `HaiApplyCard`

> So for your Lyrical Literacy videos: a recording playing under your voice can still be matched, even under loud talking. Upload checks like YouTube's Content ID compare your audio with files that copyright owners submit. And not being matched isn't the same as being allowed. Use music you made, or music you're licensed to use.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `under` | “under your voice” | 0.151 | 3.13s |
| `upload` | “Upload checks” | 0.355 | 7.37s |
| `allowed` | “isn't the same as being allowed” | 0.727 | 15.07s |
| `licensed` | “licensed to use” | 0.947 | 19.63s |

### B08 — OUTRO · `HaiTitleOutro`

> Shazam keeps the loudest points, turns pairs of them into codes, and lets the timing vote. I'm Row-Haan, for Humanitarians AI.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `close` | “lets the timing vote” | 0.472 | 4.10s |

