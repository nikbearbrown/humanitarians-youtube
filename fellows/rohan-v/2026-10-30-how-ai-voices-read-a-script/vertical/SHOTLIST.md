# SHOTLIST — "How AI Voices Read a Script"

8 beats, 135.69s (2:15). Every duration is the measured Kokoro narration length (plus, where noted, the listening clips appended by mix_listen.py); the visuals are cut to fit the audio, never the other way round.

**Word-clock choreographed.** `align.py` (faster-whisper) measured when every word is spoken, `cues.json` names an anchor phrase per reveal, and `sync_cues.py` wrote the resolved fractions into `shot.remotion.props.cues`. 39 cues authored, 39 resolved.

A STEM explainer for the week of 26–30 Oct: how a text-to-speech voice turns a script into sound, tested on this series' own narrator (Kokoro-82M, espeak-ng G2P) in voice.py. B04 ends with the narrator's own reading of a price, and B05 with its reading of the presenter's name before and after respelling (mix_listen.py).

| Beat | Act | In | Dur | Component | Lane |
|---|---|---|---|---|---|
| B00 | ASK | 0:00 | 14.70s | `ClaudeComposerAsk` | library |
| B01 | BACKGROUND | 0:14 | 23.13s | `VoicePipeline` | **new** |
| B02 | MECHANISM | 0:37 | 20.84s | `VoiceG2P` | **new** |
| B03 | MEASURED | 0:58 | 19.99s | `VoiceHeteronyms` | **new** |
| B04 | NUMBERS | 1:18 | 15.89s | `VoiceNumbers` | **new** |
| B05 | THE FIX | 1:34 | 22.58s | `VoiceRespell` | **new** |
| B06 | WHAT TO DO | 1:57 | 12.27s | `HaiApplyCard` | library |
| B07 | OUTRO | 2:09 | 6.29s | `HaiTitleOutro` | library |

## Choreography — what happens, and on which word

### B00 — ASK · `ClaudeComposerAsk`

> Hi, I am Row-Haan and this video is about how an AI voice reads a script, including the one reading this to you. It doesn't read letters the way you do. First it turns the words into sounds, and that step is where most of its mistakes happen.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `reads` | “reads a script” | 0.247 | 3.63s |
| `letters` | “doesn't read letters” | 0.508 | 7.47s |
| `sounds` | “into sounds” | 0.742 | 10.90s |
| `mistakes` | “most of its mistakes” | 0.889 | 13.07s |

### B01 — BACKGROUND · `VoicePipeline`

> A text-to-speech voice works in three steps. First it cleans up the text: doctor, not D R dot. Then it turns every word into phonemes, the small sounds speech is built from; English has about forty-four, depending on accent. Only then does the voice model turn those sounds into audio. This voice, Kokoro, never sees the spelling at all. It only gets the sounds.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `three` | “three steps” | 0.072 | 1.67s |
| `clean` | “cleans up the text” | 0.146 | 3.37s |
| `phonemes` | “into phonemes” | 0.352 | 8.13s |
| `fortyfour` | “about forty-four” | 0.517 | 11.97s |
| `model` | “the voice model” | 0.672 | 15.53s |
| `never` | “never sees the spelling” | 0.856 | 19.80s |
| `only` | “only gets the sounds” | 0.945 | 21.87s |

### B02 — MECHANISM · `VoiceG2P`

> The middle step is called G to P: graphemes, the letters, to phonemes, the sounds. Ours uses a program called e-speak. It looks a word up in a dictionary, and if the word isn't there, it guesses from rules about how English letters usually sound. That works for most words. It goes wrong when the same letters make two different words.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `g2p` | “G to P” | 0.046 | 0.97s |
| `letters` | “the letters” | 0.155 | 3.23s |
| `espeak` | “called e-speak” | 0.334 | 6.97s |
| `dict` | “in a dictionary” | 0.446 | 9.30s |
| `rules` | “guesses from rules” | 0.577 | 12.03s |
| `works` | “That works” | 0.755 | 15.73s |
| `wrong` | “goes wrong” | 0.861 | 17.93s |

### B03 — MEASURED · `VoiceHeteronyms`

> I tested eight of them, like read, which can be reed or red, each in a sentence that makes its meaning clear. Sixteen sentences, ten right. Only two words came out right both ways. Last night I read a book comes out with reed, not red. There's no grammar check behind it, only a few clues from the word just before.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `eight` | “eight of them” | 0.023 | 0.47s |
| `sixteen` | “Sixteen sentences” | 0.344 | 6.87s |
| `ten` | “ten right” | 0.413 | 8.27s |
| `two` | “Only two words” | 0.467 | 9.33s |
| `last` | “Last night I read” | 0.605 | 12.10s |
| `reed` | “with reed” | 0.680 | 13.60s |
| `clues` | “a few clues” | 0.887 | 17.73s |

### B04 — NUMBERS · `VoiceNumbers`

> The clean-up step does better. Doctor, street, one thousand twenty-four, the fifth of May: all right. But a price trips it up. It costs three dollars fifty comes out as dollar, three, fifty. Listen.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `better` | “does better” | 0.044 | 0.70s |
| `list` | “Doctor, street” | 0.124 | 1.97s |
| `price` | “a price trips” | 0.399 | 6.33s |
| `dollar` | “dollar, three” | 0.665 | 10.57s |
| `listen` | “Listen” | 0.753 | 11.97s |

- listening clip **THE PRICE, AS READ** `price.wav` 13.12–15.09s (gain -2.70 dB to the narration's level)

### B05 — THE FIX · `VoiceRespell`

> The fix is to spell a word the way it sounds. This voice got my name wrong, so every script spells it Row dash Haan. It read the drum, the dhole, as dee haal, and the sitaar as sitter, until I respelled them. Here's my name as the pronunciation step reads it, then respelled.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `fix` | “The fix” | 0.000 | 0.00s |
| `name` | “got my name wrong” | 0.149 | 3.37s |
| `dhol` | “the drum” | 0.353 | 7.97s |
| `sitar` | “as sitter” | 0.499 | 11.27s |
| `here` | “Here's my name” | 0.613 | 13.83s |

- listening clip **AS READ** `name_default.wav` 18.39–19.69s (gain -4.20 dB to the narration's level)
- listening clip **RESPELLED** `name_fixed.wav` 20.39–21.78s (gain -3.40 dB to the narration's level)

### B06 — WHAT TO DO · `HaiApplyCard`

> So when you write for an AI voice, write numbers and prices out as words. Respell names until they sound right. And listen for words with two meanings, then reword the line if it picks the wrong one.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `numbers` | “numbers and prices” | 0.196 | 2.40s |
| `names` | “Respell names” | 0.407 | 5.00s |
| `two` | “two meanings” | 0.720 | 8.83s |

### B07 — OUTRO · `HaiTitleOutro`

> Clean the text, turn it into sounds, and check the sounds. I'm Row-Haan, for Humanitarians AI.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `close` | “check the sounds” | 0.360 | 2.27s |

