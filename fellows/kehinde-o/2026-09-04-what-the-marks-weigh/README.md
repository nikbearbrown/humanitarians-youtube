# What the Marks Weigh

**Volunteer:** Kehinde Obidele

A two-and-a-half minute explainer on how much information a Yoruba diacritic
actually carries, and why that measurement decides whether the problem needs a
model at all.

## Video Files

The 4K rendered videos are on the shared Google Drive under
`Medhavy_Kehinde/What The Marks Weigh/`:

**[Google Drive folder](https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp)** (`Medhavy_Kehinde/What The Marks Weigh/`)

| File | Aspect | Spec |
|---|---|---|
| `what-the-marks-weigh.mp4` | 16:9 | 3840x2160, 30fps, 2m 39s |
| `what-the-marks-weigh-short.mp4` | 9:16 | 2160x3840, 30fps, 2m 43s, native render |

## The idea

The marks are not decoration, they are information, and information is
measurable. Knowing only the base letter, a mark costs 1.64 bits per character.
Knowing the whole word, 0.61 bits survive. That residue is exactly what sentence
context has to supply, and it is exactly the gap between a frequency lookup
table (77.1%) and a model that reads the sentence (92.4%).

Measure the problem before you model it.

## Source project

- Repository: https://github.com/Kenny0bi/ami
- Model: https://huggingface.co/kenny0bi/ami-yoruba-diacritics

The Manim animation in beats B02 to B04 is my own (`assets/manim_bits.py`),
re-rendered at 4K from source rather than upscaled from the 1080p file in the
repo. The code beat shows the real `ALLOWED` table from `ami/marks.py`.

## Files in this repo

- `beat_sheet.json` — the script. One beat per moment, everything derives from it.
- `PEDAGOGY.md` — narration gate, must read VERDICT: PASS before audio runs.
- `SOURCES.md` — every figure on screen and where it was measured.

Media files are not committed. Rendered videos live on the shared Drive.

## Rebuild

```bash
python3 runtime/scripts/generate_audio_kokoro.py books/hai/youtube/ami-yoruba-diacritics
./art run   books/hai/youtube/ami-yoruba-diacritics
./art final books/hai/youtube/ami-yoruba-diacritics --fps 30
./art shorts books/hai/youtube/ami-yoruba-diacritics
```
