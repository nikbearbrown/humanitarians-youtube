# Further, But Better

**Volunteer:** Kehinde Obidele

Why the model-compression method that moves weights **furthest** from the
originals is the one that damages the model **least**.

## Video Files

On the shared Google Drive under `Medhavy_Kehinde/STEM Topic/further-but-better/`:

**[Google Drive folder](https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp)**

| File | Aspect | Spec |
|---|---|---|
| `further-but-better.mp4` | 16:9 | 3840x2160, 30fps, 2m 35s |
| `further-but-better-short.mp4` | 9:16 | 2160x3840, 30fps, native render |

## The idea

Rounding error is a move in weight space, but damage is measured in loss space,
and the loss surface around a trained layer is a tilted valley. Naive rounding
snaps each weight to the nearest step and takes whatever hit the grid dictates.
GPTQ rounds one column at a time and slides the not-yet-rounded columns to
absorb the error first.

It ends up **2.5x further** from the original weights and **2x more accurate**
in its outputs. Distance from the original is not damage to the answer.

## Measured, not rounded

| | Perplexity (lower is better) |
|---|---|
| Full size, 32 bits | 26.2 |
| 4-bit, best method | 28.5 |

Eight times less memory for roughly a 9% quality tax. At 3 bits only this method
survives (112 against 2,482 for naive per-channel rounding). At 2 bits
everything dies, and those numbers are in the repo too.

## The mistake worth reporting

My first benchmark compared GPTQ at one scale granularity against RTN at
another, so "GPTQ vs RTN" was really "algorithm vs granularity" and granularity
was winning. Rebuilt with both arms matched: granularity alone is worth 2,482 to
183, compensation alone 2,482 to 504, and stacked they reach 112.

Change one axis at a time, or the conclusion is half method and half accounting.

## Source project

https://github.com/Kenny0bi/quantlab

The animation in the video is my own `assets/manim_gptq.py`, re-rendered at 4K
from source rather than upscaled.

## Files in this repo

- `beat_sheet.json`, `PEDAGOGY.md`, `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`

Media files are not committed.
