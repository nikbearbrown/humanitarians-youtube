# Gate P mechanical pass — Week 28 (2026-10-25)

Tool: `gate_p_lint.py` (adapted from Week 26), run with homebrew `python3.12`; phonemes from Kokoro's own tokenizer (`kokoro_onnx`, `en-us`). **No audio was generated.** This is **not** Gate P: Gate P is a human reading every line aloud. This clears what a machine can see, so the human read goes to rhythm and emphasis.

## What the first run found, and what was done

| Beat | Flag | Action |
|---|---|---|
| Long B01 | 3-word sentence "We'll need them." (Kokoro merges or mangles sentences under five words) | **Merged** into the sentence before it |
| Long B03 | Two sentences of 33 and 32 words (breath) | **Split** into four sentences, none over 28 words |
| Long B03 | "Guadalajara" phonemized as `ɡwˌɑːdɐlɐdʒˈɑːɹɹə` (a "j" sound and a doubled r instead of "h") | **Dropped from the spoken line.** The on-screen source line still names UC Berkeley and the University of Guadalajara |
| Long B10 | Three sentences under five words ("Minor pulls toward blue.", "Use the strip.", "Then answer two questions.") | **Merged** into full sentences |
| Long B11 | "US" (could be voiced as the word "us") | Now "United States listeners" |
| Both | Lone-letter "a" flagged 40 times | Tool bug (the filter lacked an exemption for the word "a"); fixed, not a script issue |

**Second run:** no short-sentence, breath, acronym or digit-chain flags in either format. Remaining flags are ear checks only (below).

## Kokoro phonemes (what the voice will say)

| Phrase | Phonemes | Verdict |
|---|---|---|
| Tanmay Kulkarni | `tˈænmeɪ kˈʌlkɑːɹni` | OK, same as Weeks 26–27; listen once in audio |
| Humanitarians AI | `hjˌuːmɐnɪtˈɛɹiənz ˌeɪˈaɪ` | OK |
| Berkeley | `bˈɜːkli` | OK |
| Bach | `bˈɑːx` | OK (the "kh" ending) |
| Mozart | `mˈoʊtsɑːɹt` | OK |
| Brahms | `bɹˈɑːmz` | OK |
| Adagio | `ædˈɑːdʒɪˌoʊ` | OK; stress on the second syllable; first vowel "a" not "ah", acceptable |
| Palmer | `pˈɑːmɚ` | OK ("PAH-mer") |
| Lillard | `lˈɪlɑːɹd` | OK |
| F major / C minor | `ˈɛf mˈeɪdʒɚ` / `sˈiː mˈaɪnɚ` | OK; letters voiced as letters |
| saturated, yellower | `sˈætʃɚɹˌeɪɾᵻd`, `jˈɛloʊɚ` | OK |
| ninety seven, thirty seven, point nine seven | all as words | OK |

**Overrides needed: none.**

## Still by ear (needs audio)

- "weak" beside "strong" (could be heard as "week"); the lint flags it, the pairing makes it clear.
- "Tanmay" and "Kulkarni" in the voice; "Bach" (some voices end it with "k").
- The Whisper check on the finished audio will confirm all of the above.

## Sentence and rate numbers

| | Lines | Words | Longest sentence | Rate |
|---|---|---|---|---|
| Long | 13 | 850 | ≤ 28 words | speech about 4:17 at 3.3 wps; beat budget 388 s includes holds |
| Short | 8 | 219 | ≤ 28 words | 2.4 words per second over 92 s |
