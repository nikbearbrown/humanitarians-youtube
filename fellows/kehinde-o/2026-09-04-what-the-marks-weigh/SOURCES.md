# SOURCES.md — What the Marks Weigh

Everything on screen, and where it comes from. All of it is Kehinde's own
published work, reproducible from the repository.

## Primary source

- Repository: https://github.com/Kenny0bi/ami
- Model: https://huggingface.co/kenny0bi/ami-yoruba-diacritics
- Licence: CC BY-NC 4.0, inherited from MENYO-20k

## Figures on screen

| Beat | Asset | Origin |
|---|---|---|
| B02, B03, B04 | `MarkBits` animation, three segments | Re-rendered at 3840x2160 from his own `assets/manim_bits.py`. The repo ships a 1080p mp4; rendering from source avoids upscaling and meets "4K at source". |
| B05 | `ALLOWED` table | The actual dict from `ami/marks.py`, trimmed to the letters that teach. ACTUAL-CODE LAW: real source, never prose restyled as code. |
| B06 | results table | His own `assets/results.svg`, rasterised at 4K. |

The Manim palette (adire indigo #1B2653, bone #F2EFE6, gold #E3B23C, coral,
teal) is deliberately NOT retinted to the Claude skin. It is his published
artifact and the indigo is a deliberate reference to adire cloth. The reel reads
Claude skin for the frame, his palette for the evidence.

## Numbers spoken or shown

| Figure | Value | Where measured |
|---|---|---|
| Entropy knowing the base letter | 1.64 bits per character | 2.0M restorable characters of the training corpus |
| Entropy knowing the word | 0.61 bits per word | same corpus |
| Per-letter entropy | e 2.56, o 2.54, a 1.57, i 1.55, u 1.46, s 0.99, n 0.53, m 0.01 | `manim_bits.py` PER_LETTER, measured |
| Unmarked baseline | 39.2% char accuracy | MENYO-20k test split, 6,573 sentences |
| Lookup baseline | 77.1% char accuracy | same split, after the regex fix described below |
| ami | 92.4% char accuracy, 86.0% word | same split |
| Model size | 1.29M parameters | char emb 64, 2x BiLSTM 192, linear head |
| Throughput | 9,600 characters per second | 12-year-old 4-core CPU |

Char accuracy is scored only on positions that can legally carry a mark, so no
system gets credit for copying consonants. Stated in the README and preserved in
the video's framing.

## The baseline is honest, and that is load bearing

The README records that his first word regex used Python's `\w`, which does not
match combining marks, so words ending in a marked vowel lost their final tone
inside the baseline's dictionary. A test caught it. Fixing it made the lookup
baseline *stronger* by roughly 16 points, and 77.1% is the fixed number.

The video quotes 77.1%. It would have been easy, and wrong, to quote the
pre-fix figure and claim a larger margin.

## Not claimed in this reel

- No state-of-the-art claim, and no comparison to Orife (2018) or any system
  not run in this repository.
- No claim that the model understands Yoruba. B07 states that tone confusions
  dominate the remaining errors.
- No performance claim for informal, code-switched or dialectal Yoruba, which
  the README explicitly lists as underrepresented.

## Papers the project stands on

- Adelani et al. (2021), MENYO-20k. The evaluation standard.
- Alabi et al. (2020), Yoruba Text C3 corpus.
- Orife (2018), attentive seq2seq diacritic restoration. Prior art.
