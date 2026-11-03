# FACTCHECK — Why It Can't Count Letters

Status: **GATE F CLOSED — 2026-09-25.** Every tokenisation figure spoken or
shown is **primary evidence**, reproducible by running `tokenize_evidence.py`
in this folder. Nothing rests on a secondary source.

| # | Beat | Claim (as spoken / shown) | Verdict | Source |
|---|---|---|---|---|
| 1 | B00 | Models often get the r-count in "strawberry" wrong | ✅ PASS | Stated as a common observation, not a measured rate. No frequency is claimed. |
| 2 | B01 | Text is split into tokens before the model sees it, and tokens are not letters | ✅ PASS | Definitional to BPE tokenisation; demonstrated directly in B02 |
| 3 | B02 | "strawberry" → `st` `raw` `berry` | ✅ PASS | Run output: `ids=[301, 1831, 8396]` |
| 4 | B02 | None of those three tokens is a letter | ✅ PASS | Inspection of the above |
| 5 | B02 | On-screen label names the tokenizer as GPT-2 BPE | ✅ PASS | Correct — `openai-community/gpt2` |
| 6 | B03 | The same word with a leading space is a **single** token | ✅ PASS | Run output: `' strawberry'` → `['Ġstrawberry']`, `ids=[41236]` |
| 7 | B04 | `raspberry` → `r` + `aspberry` | ✅ PASS | Run output, `ids=[81, 17653]` |
| 8 | B04 | `blueberry` → `blue` + `berry` | ✅ PASS | Run output, `ids=[17585, 8396]` |
| 9 | B04 | `lollipop` → `l` + `oll` + `ipop` | ✅ PASS | Run output, `ids=[75, 692, 42800]` |
| 10 | B04 | `1234567` → `123` + `45` + `67` | ✅ PASS | Run output, `ids=[10163, 2231, 3134]` |
| 11 | B04 | The vocabulary is learned from frequency; common sequences get one token, rarer ones fragment | ✅ PASS | Definitional to byte-pair encoding: merges are learned by frequency. Consistent with 7–8 — "blue"/"berry" are common words, "strawberry" is not in vocab unsprefixed. |
| 12 | B05 | The vocabulary is "about fifty thousand chunks" | ✅ PASS | `vocab_size = 50,257`. "About fifty thousand" is correct to the stated precision. |
| 13 | B05 | …"instead of twenty-six letters" | ✅ PASS | Rhetorical contrast with the Latin alphabet; not a claim about byte coverage |
| 14 | B06 | Spacing letters out makes each its own token | ✅ PASS | Follows from 6 — whitespace changes token boundaries. Demonstrated by the same mechanism the reel already showed. |

## Scope stated on screen

The reel names GPT-2 as the tokenizer and says the mechanism is general while
the specific splits are not. **No claim is made about any other model's
vocabulary**, because those are not all public and would not be reproducible
from this folder.

## Claims deliberately CUT

- Any figure for how often models fail the r-counting question. Widely
  asserted, never sourced.
- "Roughly four characters per token." Repeated everywhere, varies by text and
  tokenizer, and nothing in the argument needs it.
- Any claim that tokenisation is the *only* cause of counting errors. The reel
  argues it is sufficient to explain this family of failures, not a complete
  theory of model error.
