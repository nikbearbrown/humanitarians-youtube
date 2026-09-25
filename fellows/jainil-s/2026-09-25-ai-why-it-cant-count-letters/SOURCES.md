# SOURCES — ai-why-it-cant-count-letters

This reel's central evidence is **primary and reproducible**, not cited. Every
tokenisation figure on screen is produced by `tokenize_evidence.py` in this
folder. Run it and you get the same output.

## Primary evidence — generated locally

Tokenizer: **GPT-2 BPE**, `openai-community/gpt2`, `tokenizer.json`,
vocabulary **50,257**. Verbatim output:

```
  'strawberry' -> 3 tok  ['st', 'raw', 'berry']   ids=[301, 1831, 8396]
 ' strawberry' -> 1 tok  ['Ġstrawberry']          ids=[41236]
   'raspberry' -> 2 tok  ['r', 'aspberry']        ids=[81, 17653]
   'blueberry' -> 2 tok  ['blue', 'berry']        ids=[17585, 8396]
    'lollipop' -> 3 tok  ['l', 'oll', 'ipop']     ids=[75, 692, 42800]
     '1234567' -> 3 tok  ['123', '45', '67']      ids=[10163, 2231, 3134]
       '999+1' -> 3 tok  ['999', '+', '1']        ids=[17032, 10, 16]
```

| # | Claim on screen | Supported by |
|---|---|---|
| P1 | "strawberry" is three tokens: `st` `raw` `berry` | run output above |
| P2 | None of those tokens is a letter | inspection of P1 |
| P3 | The same word with a leading space is **one** token | `' strawberry'` → `['Ġstrawberry']` |
| P4 | Similar words split differently — `raspberry` is `r`+`aspberry`, `blueberry` is `blue`+`berry` | run output above |
| P5 | Digits group arbitrarily — `1234567` → `123 45 67` | run output above |
| P6 | Vocabulary is ~50k units, not 26 letters | `vocab_size = 50,257` |

## Scope — stated plainly in the reel

GPT-2's tokenizer is used because it is small, public and reproducible. **Every
model has its own vocabulary and splits differently.** The reel says the
mechanism is general and the specific splits are GPT-2's; it never claims these
exact tokens for any other model.

## Deliberately NOT used

- Claims about any specific current model's tokenizer output. Those vocabularies
  are not all public and would not be reproducible from this folder.
- Any assertion that tokenisation is the *only* cause of counting errors. The
  reel argues it is a sufficient explanation for this family of failures, not a
  complete theory of model error.
- Round numbers like "about 4 characters per token". Widely repeated, varies by
  text and tokenizer, and nothing in the reel needs it.
