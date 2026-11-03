# Gate P mechanical pass: Week 28 work video (2026-10-25)

Tool: `gate_p_lint.py` (adapted from the topic video's lint), run with homebrew `python3.12`; phonemes from Kokoro's own
tokenizer (`kokoro_onnx`, `en-us`). **No audio was generated.** This is **not** Gate P: Gate P is a human reading every
line aloud. This clears what a machine can see, so the human read goes to rhythm and emphasis.

## What the first run found, and what was done

| Beat | Flag | Action |
|---|---|---|
| Long B01, B02, B03, B05, B06, B07, B08, B10; Short S03, S04 | 21 sentences under five words ("Tech sector crash." "Minus seventy-eight percent." "Which shocks?" "Seventy-eight." and others); Kokoro merges or mangles them | **Merged** into full sentences, keeping the voice and the order of ideas (the price-shock list became one sentence with semicolons) |
| Long B05, B06, B08; Short S04 | "weight" / "weights" (heard as "wait" / "waits"; Whisper heard "let's wait the coin" in an earlier week) | **Replaced** with "share(s)" in the narration; the word "weights" stays on screen, where it is read, not heard |
| Long B04 | "README" (an all-caps letter-string) | Kept. Kokoro's phonemes are `ɹˈiːdmiː` (REED-mee), which is how the word is said; confirm by ear |

**Second run:** no short-sentence, breath, homophone, symbol, markup, digit-chain or lone-letter flags in either
format. One remaining flag is the benign "README" above.

## Kokoro phonemes (what the voice will say)

| Phrase | Phonemes | Verdict |
|---|---|---|
| Mycroft | `mˈɪkɹɔft` (MIK-croft) | **Needs the override** `mˈaɪkɹɔft` (MY-croft), as in Week 27; the written spelling stays everywhere |
| Tanmay Kulkarni | `tˈænmeɪ kˈʌlkɑːɹni` | OK, same as earlier weeks; listen once in audio |
| Humanitarians AI | `hjˌuːmɐnɪtˈɛɹiənz ˌeɪˈaɪ` | OK |
| README | `ɹˈiːdmiː` | OK (see above) |
| Python | `pˈaɪθən` | OK |
| seventy-eight, twenty-two hundred | `sˈɛvəntiˈeɪt`, `twˈɛntitˈuː hˈʌndɹɪd` | OK |
| thirty-three point seven five percent | `θˈɜːɾiθɹˈiː pˈɔɪnt sˈɛvən fˈaɪv pɚsˈɛnt` | OK; the unit "percent" is present |
| thirty-six, plus twenty-seven, plus fifteen | `θˈɜːɾisˈɪks, plˈʌs twˈɛntisˈɛvən, plˈʌs fˈɪftiːn` | OK |
| semiconductors, volatility, stress test, scenario | all as words | OK |

**Overrides needed:** one, `Mycroft` → `mˈaɪkɹɔft`, applied at the audio step.

## Still by ear (needs audio)

- "Mycroft" with the override, "Tanmay" and "Kulkarni" in the voice, "README".
- The two digit-heavy sentences: B05 ("thirty-six, plus twenty-seven, plus fifteen makes seventy-eight") and Short S04. The Whisper check on the finished audio will confirm them.

## Sentence and rate numbers

| | Lines | Words |
|---|---|---|
| Long | 11 | 659 |
| Short | 6 | 171 |

## Update: Short draft 2 (2026-10-25)

The Short was rewritten (8 lines, 235 words) to carry more context and read less rushed. Re-run: no short-sentence,
breath, homophone, symbol, markup or digit-chain flags; new phrases phonemize cleanly (`open repository of finance
pipelines`, `named shocks, each one a percentage hit`, the two arithmetic sentences, the closing title). The Short's
read-aloud sheet is now draft 2; the long film's sheet is unchanged (draft 1.1).
