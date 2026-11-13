# SOURCES — Inside the Black Box, Part 1

## Provenance

Sai supplied the topic and one URL on 2026-10-25, chose the "Inside the Black
Box" angle and approved the image licence terms. On 2026-10-26 he asked for the
reel to be split into two parts; Part 2 is `../2026-10-23-inside-the-black-box-part-2/`.

## Source

| What | Where | Used for |
|---|---|---|
| Stephen Wolfram, "What Is ChatGPT Doing … and Why Does It Work?", 14 Feb 2023 | https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/ · archived as `research/wolfram-2023-02-14-what-is-chatgpt-doing.html` | every quotation and paraphrase; all 6 figures |
| Licence of the essay | page footer: "Open content: CC BY-NC-SA 4.0 (code: CC BY-SA 4.0)" | the figures' terms |
| Our training run | `evidence/train_nets.py` → `evidence/train_nets.out` (2026-10-26) | B05, B06 |

## The figures (6)

| Beat | Slug | Original file | Essay section |
|---|---|---|---|
| B01 | `neuron_net` | `sw021423img46.png` | Neural Nets |
| B01 | `activations` | `sw021423img48.png` | Neural Nets |
| B01 | `net_formula` | `sw021423img49.png` | Neural Nets |
| B03 | `descent` | `sw021423img71.png` | Machine Learning, and the Training of Neural Nets |
| B03 | `examples` | `sw021423img62.png` | Machine Learning, and the Training of Neural Nets |
| B03 | `extrapolate` | `sw021423img73.png` | Machine Learning, and the Training of Neural Nets |

Sidecars `images/src/<slug>.json` hold page, file URL, context, licence evidence,
sha256 and fetch time. Figures are the published ~2× PNGs, enlarged ≤ 2.2× with
Lanczos; nothing regenerated or AI-upscaled.

## Honesty log

- **The ten-net task is constructed** (a step function shaped like Wolfram's
  example, 400 points on [−1, 1]). All ten seeds are reported; none dropped.
- **"ChatGPT" means the 2023 model** (GPT-3, 175 billion weights); the narration
  dates it and uses his "billions of terms".
- **GELU, not ReLU, in GPT-2**; stated on the B02 card.
- **Split from one reel (2026-10-26).** B01–B04 kept their narration, audio and
  renders; the single-reel masters are in `_superseded/`.
