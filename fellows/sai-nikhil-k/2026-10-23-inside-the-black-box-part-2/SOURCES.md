# SOURCES — Inside the Black Box, Part 2

## Provenance

Sai supplied the topic and one URL on 2026-10-25, chose the "Inside the Black
Box" angle and approved the image licence terms. On 2026-10-26 he asked for the
reel to be split in two and named this folder's date (2026-10-23). Part 1 is
`../2026-10-19-inside-the-black-box/`.

## Sources

| What | Where | Used for |
|---|---|---|
| Stephen Wolfram, "What Is ChatGPT Doing … and Why Does It Work?", 14 Feb 2023 | https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/ · archived as `research/wolfram-2023-02-14-what-is-chatgpt-doing.html` | quotations; all 6 figures |
| Licence of the essay | page footer: "Open content: CC BY-NC-SA 4.0 (code: CC BY-SA 4.0)" | the figures' terms |
| GPT-2 small checkpoint | Hugging Face `openai-community/gpt2` @ `607a30d7…`, `model.safetensors` sha256 `248dfc39…d3a707` (local cache) | B02, B03, B05 (`evidence/gpt2_inspect.out`) |

## The figures (6)

| Beat | Slug | Original file | Essay section |
|---|---|---|---|
| B01 | `cat_layer1` | `sw021423img56.png` | Neural Nets |
| B01 | `cat_layer10` | `sw021423img57.png` | Neural Nets |
| B04 | `word_map` | `sw021423img78.png` | The Concept of Embeddings |
| B04 | `attention` | `sw021423img89A.png` | Inside ChatGPT |
| B04 | `weights_raw` | `sw021423img90A.png` | Inside ChatGPT |
| B04 | `weights_smooth` | `sw021423img91.png` | Inside ChatGPT |

## Honesty log

- **The weight total and its breakdown are ours, not Wolfram's.** He gives 12
  blocks, 12 heads and 768; the 124,439,808 total, 50,257 tokens, 1,024
  positions and 7,087,872 per block are counted from the file. (The script's
  first count, 2026-10-25, printed 124,412,160 because its mask-buffer filter
  also dropped `c_attn.bias`; fixed and cross-checked by hand.)
- **The system `transformers` would not import** (accelerate → boto3), so the
  forward pass is written in NumPy; it reproduces Wolfram's first figure.
- **The word map is not GPT-2's embedding**; captioned accordingly.
- **Split from one reel (2026-10-26)**; B01, B02, B04 and B06 keep their narration.
