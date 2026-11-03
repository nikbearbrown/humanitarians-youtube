# SHOTLIST — "How Apps Find a Song's Key"

9 beats, 160.22s (2:40). Every duration is the measured Kokoro narration length (plus, where noted, the listening clips appended by mix_listen.py); the visuals are cut to fit the audio, never the other way round.

**Word-clock choreographed.** `align.py` (faster-whisper) measured when every word is spoken, `cues.json` names an anchor phrase per reveal, and `sync_cues.py` wrote the resolved fractions into `shot.remotion.props.cues`. 48 cues authored, 48 resolved.

A STEM explainer for the week of 19–23 Oct: how key detection works, on a detector I built (key.py) and tested on 60 synthetic Western songs. B02 ends with six seconds of the example song (mix_listen.py).

| Beat | Act | In | Dur | Component | Lane |
|---|---|---|---|---|---|
| B00 | ASK | 0:00 | 16.36s | `ClaudeComposerAsk` | library |
| B01 | BACKGROUND | 0:16 | 15.62s | `KeyNotes` | **new** |
| B02 | MECHANISM | 0:31 | 27.09s | `KeyChroma` | **new** |
| B03 | MATH | 0:59 | 25.07s | `KeyProfiles` | **new** |
| B04 | MEASURED | 1:24 | 15.38s | `KeyGrid` | **new** |
| B05 | THE CATCH | 1:39 | 23.34s | `KeyRelative` | **new** |
| B06 | KEY CHANGE | 2:02 | 17.22s | `KeyChange` | **new** |
| B07 | WHAT TO DO | 2:20 | 14.17s | `HaiApplyCard` | library |
| B08 | OUTRO | 2:34 | 5.97s | `HaiTitleOutro` | library |

## Choreography — what happens, and on which word

### B00 — ASK · `ClaudeComposerAsk`

> Hi, I am Row-Haan and this video is about how apps find a song's key: the label, like A minor or C major, that a DJ app shows next to a track. Last week it was the tempo. This time the app has to work out which note the song keeps coming home to.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `label` | “the label” | 0.265 | 4.33s |
| `tempo` | “it was the tempo” | 0.660 | 10.80s |
| `home` | “coming home to” | 0.933 | 15.27s |

### B01 — BACKGROUND · `KeyNotes`

> A key is a set of seven notes with one of them as home. C major uses the white keys of a piano, and C is home. A minor uses the very same seven notes, but its home is A. Hold on to that, because that's exactly where apps go wrong.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `seven` | “set of seven notes” | 0.038 | 0.60s |
| `white` | “the white keys” | 0.277 | 4.33s |
| `chome` | “and C is” | 0.376 | 5.87s |
| `aminor` | “A minor uses” | 0.506 | 7.90s |
| `ahome` | “its home is A” | 0.698 | 10.90s |
| `wrong` | “where apps go wrong” | 0.918 | 14.33s |

### B02 — MECHANISM · `KeyChroma`

> Step one: hear which notes are sounding. Every frequency is folded into one of twelve note names, whatever the octave. That's called chroma. Added up over the whole song, it gives twelve bars: how much of each note the song uses. In my C major pop song, C, G and E stand tallest. Here's how it sounds.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `one` | “Step one” | 0.000 | 0.00s |
| `fold` | “folded into one of twelve” | 0.132 | 3.57s |
| `octave` | “whatever the octave” | 0.209 | 5.67s |
| `chroma` | “called chroma” | 0.276 | 7.47s |
| `added` | “Added up” | 0.320 | 8.67s |
| `bars` | “twelve bars” | 0.393 | 10.63s |
| `tallest` | “stand tallest” | 0.634 | 17.17s |
| `listen` | “Here's how it sounds” | 0.687 | 18.60s |

- listening clip **POP SONG IN C MAJOR** `song_c_major_pop.wav` 20.29–26.29s (gain -8.90 dB to the narration's level)

### B03 — MATH · `KeyProfiles`

> Step two: compare it with a template. In 1982, psychologists asked listeners how well each note fits a key, and those ratings give every one of the twenty-four keys a shape. The app slides the song's bars against all twenty-four shapes, and keeps the best match, measured by correlation. C major scores zero point nine eight. The next best, G major, only zero point seven two.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `two` | “Step two” | 0.000 | 0.00s |
| `template` | “with a template” | 0.056 | 1.40s |
| `listeners` | “asked listeners” | 0.183 | 4.60s |
| `shape` | “a shape” | 0.409 | 10.27s |
| `slides` | “slides the song's bars” | 0.468 | 11.73s |
| `corr` | “measured by correlation” | 0.661 | 16.57s |
| `cmaj` | “C major scores” | 0.723 | 18.13s |
| `rival` | “The next best” | 0.852 | 21.37s |

### B04 — MEASURED · `KeyGrid`

> I built a detector this way, and tested it on sixty songs I generated: pop, rock, blues, and two kinds of minor ballad, each in all twelve keys. It named the key right on fifty of sixty. Pop, rock and blues: every single one.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `built` | “I built a detector” | 0.000 | 0.00s |
| `sixty` | “sixty songs” | 0.169 | 2.60s |
| `styles` | “pop, rock, blues” | 0.306 | 4.70s |
| `fifty` | “fifty of sixty” | 0.737 | 11.33s |
| `every` | “every single one” | 0.915 | 14.07s |

### B05 — THE CATCH · `KeyRelative`

> The ten misses were all in one place: minor ballads that only use the notes of the natural minor scale. Ten of twelve came out as the major key with the same seven notes. For A minor, the match was zero point eight eight six, against zero point eight nine one for C major. Raise one note, the seventh, and all twelve come out right. The standard test gives this mistake partial credit.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `misses` | “The ten misses” | 0.000 | 0.00s |
| `natural` | “natural minor scale” | 0.183 | 4.27s |
| `ten` | “Ten of twelve” | 0.248 | 5.80s |
| `amin` | “For A minor” | 0.428 | 10.00s |
| `cmaj` | “for C major” | 0.648 | 15.13s |
| `raise` | “Raise one note” | 0.708 | 16.53s |
| `credit` | “partial credit” | 0.951 | 22.20s |

### B06 — KEY CHANGE · `KeyChange`

> One label has a second problem: songs change key. This one moves up a semitone halfway, the classic pop key change. Asked for one key, my detector said C minor: neither of them. Listening in eight-second windows, it hears C major, then C sharp major.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `second` | “a second problem” | 0.044 | 0.77s |
| `semitone` | “up a semitone” | 0.271 | 4.67s |
| `one` | “Asked for one key” | 0.478 | 8.23s |
| `neither` | “neither of them” | 0.643 | 11.07s |
| `windows` | “eight-second windows” | 0.768 | 13.23s |
| `sharp` | “C sharp major” | 0.921 | 15.87s |

### B07 — WHAT TO DO · `HaiApplyCard`

> So when an app's key looks wrong, check the relative key first: A minor and C major share every note, and harmonic-mixing charts put them side by side. And on a song with a key change, check each section, not one label.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `wrong` | “looks wrong” | 0.068 | 0.97s |
| `relative` | “relative key first” | 0.167 | 2.37s |
| `charts` | “harmonic-mixing charts” | 0.501 | 7.10s |
| `section` | “check each section” | 0.859 | 12.17s |

### B08 — OUTRO · `HaiTitleOutro`

> Count the notes, match a shape, then check the home note. I'm Row-Haan, for Humanitarians AI.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `close` | “the home note” | 0.341 | 2.03s |

