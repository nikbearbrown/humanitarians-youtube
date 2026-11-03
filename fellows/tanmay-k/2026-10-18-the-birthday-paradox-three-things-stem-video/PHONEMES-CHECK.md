# Kokoro phoneme check, Week 27 (2026-10-16)

Method: Kokoro's own tokenizer (`kokoro_onnx.tokenizer.Tokenizer`, `en-us`, homebrew `python3.12`) phonemized each phrase. **No audio was generated.** The IPA below is what Kokoro will speak. Narration text was not changed, so Gate P is unaffected.

| Where | Phrase | Kokoro phonemes | Verdict |
|---|---|---|---|
| B02, B18 | Tanmay Kulkarni | `tˈænmeɪ kˈʌlkɑːɹni` | **OK, same as Week 26.** "Kulkarni" is the signed `kul-KAR-nee` string (`kˈʌlkɑːɹni`). "Tanmay" has no override in any earlier film. Still worth a listen once audio exists |
| B02, B18 | Humanitarians AI | `hjˌuːmɐnɪtˈɛɹiənz ˌeɪˈaɪ` | OK |
| B11 | fortnight | `fˈɔːɹtnaɪt` | OK ("FORT-night") |
| B06 | February twenty ninth | `fˈɛbɹuːˌɛɹi twˈɛnti nˈaɪnθ` | OK. Standard "FEB-roo-air-ee"; "ninth" has the θ |
| B13, B15, B17 | one point two, plus a half | `wˈʌn pˈɔɪnt tˈuː, plˈʌs ɐ hˈæf` | OK. "Add a half" is `ˈæd ɐ hˈæf` |
| B06 | National Center for Health Statistics | `nˈæʃənəl sˈɛntɚ fɔːɹ hˈɛlθ stɐtˈɪstɪks` | OK |
| B06 | Social Security Administration | `sˈoʊʃəl sᵻkjˈʊɹɹᵻɾi ɐdmˌɪnɪstɹˈeɪʃən` | **Listen:** "Security" has a doubled `ɹɹ`. Probably inaudible; confirm by ear |
| B04, B07, B09, B10, B17 | fifty point seven / eight percent; ninety five point four percent; better than ninety nine point nine percent; twelve / seventy one / ninety seven percent; fifty three percent | all contain `pɚsˈɛnt` after the number | OK. The unit is present in every phrase checked, so no unit-drop |
| B07 | "Fifty point eight" | `fˈɪfti pˈɔɪnt ˈeɪt` | OK. "eight" is stressed and may sound close to "A" after "point": listen once |
| B03 | two hundred and fifty three | `tˈuː hˈʌndɹɪd ænd fˈɪfti θɹˈiː` | OK |

**Overrides needed: none.** No `OVERRIDES` entries are required for this film.

**Still by ear (needs audio):** "Tanmay" and "Kulkarni" in your own voice, the doubled `ɹɹ` in "Security", and "point eight" in B07.
