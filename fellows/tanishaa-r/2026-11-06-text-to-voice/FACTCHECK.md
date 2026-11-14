# FACTCHECK — How a Computer Turns Text into a Voice

| Beat | Claim | Verdict | Source / basis | Fix applied |
|---|---|---|---|---|
| B00 | Bella is an AI narrator; Claude drafted the script and Tanishaa approved it. | TRUE | Kokoro `af_bella`; script approved in chat 2026-11-08 ("Approved, build it"). | Says "Claude drafted and I approved", not "I wrote". |
| B01 | A TTS system works out sounds, plans length and pitch, then builds the wave sample by sample. | TRUE (general) | Standard TTS pipeline (text normalization → grapheme-to-phoneme → prosody → waveform). Kokoro (StyleTTS 2-style) predicts duration and pitch internally, then decodes audio. | none |
| B02 | "read" has two pronunciations; "Dr." can mean doctor or drive; numbers need a spoken form. | TRUE | English homographs/abbreviations; Kokoro's own output in demo/tts_output.json shows all three go wrong. | Voice-only respelling "red and reed" so Bella says both. |
| B03 | Most TTS systems follow four steps: clean up, phonemes, delivery (length/pitch/loudness), wave. | TRUE (general) | Same as B01. Kokoro merges steps 3–4 in one network; the beat says "most systems" on purpose. | Step 3 bars on screen are schematic. |
| B04 | Bella's audio is 24,000 numbers per second; a neural network predicts them; a voice is 256 numbers; swapping them changes the voice. | TRUE | demo/tts_output.json: sample_rate 24000; style_shape [510, 1, 256] (one 256-number row used per utterance, chosen by length). Samples and style numbers on screen are real. | Says "a list of 256 numbers" (a row of the table), not "the whole voice file". |
| B05 | Bella's engine said "reed" for "I read it yesterday", "Oak Doctor" for "Oak Dr.", "dollar five" for "$5"; a second voice made the same mistakes. | TRUE | demo/tts_demo.py → tts_output.json: phonemes `ɹˈiːd`, `ˈoʊk dˈɑːktɚ`, `dˈɑːlɚ fˈaɪv`; am_michael uses the same phonemizer output; faster-whisper heard "Oak Doctor" in both voices. | Script v1 predicted the right tense; changed to show the mistake. |
| B06 | It often gets names and unusual words wrong; always disclose an AI voice; don't clone a real voice without permission. | TRUE / guidance | Phonemizer guesses unknown words by rule (shown in B05); disclosure and consent are ethics guidance, phrased as advice. | none |
| B07 | Takeaway. | summary of B01–B05 | — | none |
| B08 | Your-turn prompt. | advice | — | none |

No version numbers are spoken; the on-screen footnote names kokoro-onnx 0.6.1.
