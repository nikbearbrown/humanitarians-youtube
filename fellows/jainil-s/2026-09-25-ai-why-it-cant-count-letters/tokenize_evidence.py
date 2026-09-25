#!/usr/bin/env python3
"""Reproduce every tokenisation figure used in this reel.

Primary evidence, not a citation. Run it and you get the same numbers that
appear on screen. Requires `tokenizers` and `huggingface_hub` (both ship as
faster-whisper dependencies in this toolkit's venv).

    python3 tokenize_evidence.py
"""
from huggingface_hub import hf_hub_download
from tokenizers import Tokenizer

tok = Tokenizer.from_file(hf_hub_download("openai-community/gpt2", "tokenizer.json"))
print(f"GPT-2 BPE tokenizer — vocab {tok.get_vocab_size():,}\n")

for s in ["strawberry", " strawberry", "raspberry", "blueberry",
          "lollipop", "1234567", "999+1"]:
    e = tok.encode(s)
    print(f"{s!r:>14} -> {len(e.tokens)} tok  {e.tokens}  ids={e.ids}")

print()
word = "strawberry"
e = tok.encode(word)
print("a human sees :", list(word), f"({len(word)} characters, {word.count('r')} r's)")
print("model sees   :", e.tokens, f"({len(e.tokens)} tokens)")
