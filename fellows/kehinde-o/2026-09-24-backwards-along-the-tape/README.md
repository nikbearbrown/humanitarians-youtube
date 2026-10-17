# Backwards Along the Tape

**Volunteer:** Kehinde Obidele

A STEM explainer built on my own repo, [ember](https://github.com/Kenny0bi/ember): a tensor
autograd engine written from scratch on raw NumPy, used to train a real GPT with PyTorch
nowhere in the loop.

## Video Files

On the shared Google Drive under `Medhavy_Kehinde/STEM Topic/backwards-along-the-tape/`:

**[Google Drive folder](https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp)**

| File | Aspect | Spec |
|---|---|---|
| `backwards-along-the-tape.mp4` | 16:9 | 3840x2160, 30fps, 2m 47s |
| `backwards-along-the-tape-short.mp4` | 9:16 | 2160x3840, 30fps, native render |

## The one idea

`backward()` is a single rule applied in reverse along a recorded tape.

Multiply the local derivatives along a path. Add them where paths meet. Each operation only
ever needs to know its own local derivative; composition does the rest. That is the whole
of backpropagation, and every framework hides it behind one line.

## Why I wrote it

I could train a model without being able to say what `backward()` actually did. That is not
knowing. So the rule was: NumPy arrays and arithmetic only, everything above that is mine.

About 700 lines later that means a tensor carrying its own gradient, full broadcasting
arithmetic, batched matmul, LayerNorm, dropout, causal multi-head attention, AdamW,
global-norm clipping and a cosine schedule with warmup.

## How I know the gradients are right

A loss that goes down is not proof. A wrong gradient also goes down.

1. **Per-op checks.** Every primitive and composite runs in both engines in float64 and is
   compared at 1e-9, forward values and gradients.
2. **The parity experiment.** Same MLP, weights copied bit for bit into PyTorch, same batch
   order, 300 steps of momentum SGD, both engines side by side.

| | |
|---|---|
| Largest gap between the loss curves, over 300 steps | **2.682e-07** |
| Mean gap | 5.363e-08 |

That is float32 rounding noise.

## It trains real models

| Run | Result |
|---|---|
| MNIST MLP (784-256-128-10, AdamW) | **97.83%** test accuracy, 19 s |
| char-GPT on Tiny Shakespeare (624K params, 3 layers, 4 heads) | val loss **1.83**, 35 min, 1,625 tok/s |

Worth stating plainly: at initialisation the GPT sits at 4.49, which is slightly *worse*
than guessing uniformly over the 65-character vocabulary (ln 65 = 4.17). It has to learn
its way past guessing before anything else happens.

## The bug that taught me the most

Broadcasting. When NumPy quietly copies a tensor across rows on the way forward, every one
of those copies carries gradient on the way back, and they all belong to the same few
numbers. Forward broadcasting means backward summation. Get it wrong and nothing errors,
the model just learns slightly the wrong thing.

## A note on how the video was made

The animation in the middle is my own Manim scene (`assets/manim_chain_rule.py`),
re-rendered at 3840x2160 for this video rather than upscaled. The dark ember palette is
mine and is deliberately not retinted.

Every figure was read from the repo's committed run logs (`assets/parity_log.json`,
`shakespeare_log.json`, `mnist_log.json`) during the build, not copied from the repo
README. The trace is in `FACTCHECK.md`.

## Files in this repo

- `beat_sheet.json` — the script
- `PEDAGOGY.md` — narration gate, VERDICT: PASS
- `FACTCHECK.md` — every on-screen claim, its source, and the algebra check
- `SHOTLIST.md` — typed work order
- `PROMPTS.md` — the on-screen prompts, plus the Manim build note

Media files are not committed.
