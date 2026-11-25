# FACTCHECK — How AI Voices Read a Script

Every spoken and on-screen claim, its source, and its verdict. Checked 2026-11-01. "The run" means `voice.py` →
`evidence/run.log` / `evidence/results.json` and the four clips in `evidence/` (SHA-256 in `MEASUREMENTS.txt`).
The pronunciation step tested is **our narrator's own**: `generate_audio_kokoro.phonemize()`, which is espeak-ng
through `phonemizer`, inside kokoro-onnx 0.6.1 (not misaki). The clips are Kokoro af_bella, checked by
faster-whisper base. No recording is used. Outside facts, with URLs and confidence levels:
`week-10/_research/facts-tts.md` (summarised in SOURCES.md).

| # | Beat | Claim | Source | Verdict |
|---|---|---|---|---|
| 1 | B00 | Opening line "Hi, I am … and this video is about …" | `docs/FELLOWS-SUBMISSION.md` | ✅ verbatim |
| 2 | B00 | AI narration disclosed, "including the one reading this to you" | on-screen disclosure + `metadata.ai_disclosure`; narration is Kokoro af_bella (`_audio.log`) | ✅ |
| 3 | B00 | First it turns the words into sounds, and that step is where most of its mistakes happen | every mistake this run found is in that step (heteronyms, the price, the names); facts-tts §1.2, §1.4 (normalisation is hard; phoneme input is used to avoid mispronunciation). No measured share of all TTS errors | ⚠️ scoped: true of my test, not a measured general share |
| 4 | B01 | Three steps: clean up the text, turn words into phonemes, then the voice model makes audio | facts-tts §1.1, §1.3; our pipeline: espeak-ng does the first two, Kokoro the third (§0.2a, §0.2b) | ✅ |
| 5 | B01 | "Doctor, not D R dot" | run: `Dr. Smith -> dˈɑːktɚ. smˈɪθ` (the scene's worked example) | ✅ measured |
| 6 | B01 | English has about forty-four phonemes, depending on accent | *Dictionary of the British English Spelling System* (2015): RP has 44, the count varies by accent (facts-tts §5.2) | ✅ hedged as the facts file says |
| 7 | B01 | This voice, Kokoro, never sees the spelling; it only gets the sounds | Kokoro's input is a phoneme string (facts-tts §0.5a); kokoro-onnx phonemizes before the model (§0.2a) | ✅ |
| 8 | B02 | The middle step is called G to P: graphemes to phonemes | facts-tts §1.3, §0.1 | ✅ |
| 9 | B02 | Ours uses a program called e-speak | kokoro-onnx 0.6.1 `tokenizer.py` → `phonemizer` → espeak-ng 1.52.0 (facts-tts §0.2a) | ✅ |
| 10 | B02 | It looks a word up in a dictionary, and if it isn't there, guesses from letter rules | espeak-ng `en_list` (dictionary) and `en_rules` (letter-to-sound rules) (facts-tts §0.3a) | ✅ |
| 11 | B02 | On screen: four words and their sounds | run EXAMPLES: `book -> bˈʊk; night -> nˈaɪt; phoneme -> fˈoʊniːm; Boston -> bˈɔstən` | ✅ measured |
| 12 | B03 | I tested eight of them, each in a sentence that makes its meaning clear | `voice.py HETERONYMS`: read, lead, live, record, close, wind, tears, present; two sentences each | ✅ |
| 13 | B03 | "Read", which can be reed or red | facts-tts §3, §0.4b (`read ri:d` / `read rEd $past`) | ✅ |
| 14 | B03 | Sixteen sentences, ten right | run: "10 of 16 sentences got the right pronunciation"; screen "10 / 16" | ✅ measured |
| 15 | B03 | Only two words came out right both ways | run: "both meanings right for 2 of 8 words" (live, tears); screen "2 / 8" | ✅ measured |
| 16 | B03 | "Last night I read a book" comes out with reed, not red | run: `past: WRONG (lˈæst nˈaɪt aɪ ɹˈiːd ɐ bˈʊk.)`, expected `ɹˈɛd` | ✅ measured |
| 17 | B03 | There's no grammar check behind it, only a few clues from the word just before | espeak-ng has no part-of-speech tagger; `$verbf`/`$nounf`/`$pastf` flags set by the previous word (facts-tts §0.4a, §0.4c) | ✅ |
| 18 | B04 | Doctor, street, one thousand twenty-four, the fifth of May: all right | run: `Dr. Smith -> dˈɑːktɚ. smˈɪθ`; `Main St. -> mˈeɪnstɹˌiːt.`; `1,024 bytes -> wˈʌn θˈaʊzənd twˈɛnti fˈɔːɹ bˈaɪts`; `the 5th of May -> ðə fˈɪfθ ʌv mˈeɪ`. Caught in review: the first narration said "one thousand and twenty-four", which the run never read; reworded and re-voiced to match | ✅ measured |
| 19 | B04 | On screen: "Six of seven right. Prices aren't." | `export_voice_data.py READ`: six cases marked right, the price wrong. Two are judgment calls: `in 2026 -> ɪn tˈuː θˈaʊzənd twˈɛnti sˈɪks` ("two thousand twenty-six"; `voice.py`'s own reference reading was "twenty twenty-six") and `at 10:30 -> æt tˈɛn:θˈɜːɾi` ("ten thirty") were both counted right | ✅ measured, with those two calls |
| 20 | B04 | "It costs three dollars fifty" comes out as dollar, three, fifty | run: `It costs $3.50. -> ɪt kˈɔsts dˈɑːlɚ θɹˈiː. fˈɪfti` | ✅ measured |
| 21 | B04 | The listening clip is that price | `evidence/price.wav`, appended unedited by `mix_listen.py` (level matched only, −2.7 dB) | ✅ |
| 22 | B05 | The fix is to spell a word the way it sounds | respelling is a verified fix in our pipeline (facts-tts §4.3); misaki's `[word](/phonemes/)` syntax does not work for us (§0.5d) and is not mentioned | ✅ |
| 23 | B05 | This voice got my name wrong, so every script spells it "Row dash Haan" | run: `Rohan ɹˈoʊhæn` (short a, as in "cat"; facts-tts §4.2) → respelled `ɹˈoʊhˈɑːn` | ✅ measured |
| 24 | B05 | It read the dhol as "dee haal" and the sitar as "sitter", until I respelled them | run: `dhol dˈiːhˈɑːl`, `sitar sˈɪɾɚ`; respelled `dhole dˈoʊl`, `sitaar sɪtˈɑːɹ` (week-08 progress video). The narration itself uses the respellings ("dhole", "sitaar") so it says them right | ✅ measured |
| 25 | B05 | On screen: a fourth row, tabla | run: `tabla tˈæblə -> tubla tˈʌblə` (week-08 progress video) | ✅ measured |
| 26 | B05 | The two clips: my name as the pronunciation step reads it, then respelled | `evidence/name_default.wav` and `name_fixed.wav`, appended unedited (level matched only, −4.2 and −3.4 dB) | ✅ |
| 27 | B06 | Write numbers and prices out as words; respell names; listen for words with two meanings and reword | follows from B03–B05 | ✅ as advice |
| 28 | B07 | "Clean the text, turn it into sounds, and check the sounds" | summary of B01–B06 | ✅ |

## The audio check, stated as what it shows

faster-whisper base heard `'Last night, I read a book.'`, `'It costs $3.50.'`, and `'Hi, I am Rohan.'` for **both**
name clips. The recogniser writes the expected spelling either way, so it cannot tell the two readings of the name
apart; the respelling is shown by its phonemes and by the clips the viewer hears. The video makes no claim that the
recogniser confirmed the fix. (The captions reel uses this check in its B05.)

## Not claimed

- That our narrator uses misaki, Kokoro's official G2P, or that misaki's `[word](/phonemes/)` override works for us
  (in our pipeline espeak reads it aloud; facts-tts §0.5d).
- That espeak-ng understands grammar or tags parts of speech; that "St." always reads as "street" (in "Elm St." it
  reads as "saint"; facts-tts §0.6).
- That YouTube requires AI narration to be labelled. The disclosure is an editorial choice (facts-tts §6.4).
- That Kokoro would sound better with misaki's phonemes; that Kokoro is "human-level" or clones voices.
- That these counts hold for other TTS systems: they are the run's, on our narrator's pronunciation step.
