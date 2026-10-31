# A Comma Changed the Answer. — BRUTALIST REBUILD GUIDE

Physics Engine series, video 2 of 17. Host: Param Madan. Voice: Kokoro `af_bella`.
Video by Param Madan · Engine by Jash Shah, Harsh Gujarati, Atharva & Param Madan.

**Claim:** A language model predicts arithmetic instead of calculating it — it reads
numbers in tokenizer chunks, so just adding commas moved GPT-3.5 from 75.6% to 97.8%
on the same additions. The physics engine therefore never asks the model for a number:
SymPy does every calculation exactly, which keeps grading fair and hints readable.

Sources: Singh & Strouse 2024, arXiv:2402.14903 ·
https://github.com/jashshah127/humanitariansai/tree/2dc4aa4/physics-engine

## Video

Rendered videos are not stored in this repository.

| Cut | File | Resolution | Runtime |
|---|---|---|---:|
| 16:9 long-form | `a-comma-changed-the-answer.mp4` | 3840x2160 | 3:59 |

**Persona:** Param Madan (host) · **Voice:** Kokoro `af_bella` · **Palette:** claude (cream, warm ink, terracotta)

## Rebuild

```bash
REEL=~/books/physics-engine/youtube/a-comma-changed-the-answer
cd ~/brutalist.art
cp $REEL/src/PhysicsEngine02.tsx runtime/remotion/src/scenes/
# paste src/Root.registration.tsx: the import near the top of Root.tsx,
# the <Folder> block inside the returned fragment
./.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL     # GATE P: PEDAGOGY.md signed
./.venv/bin/python runtime/scripts/remotion_scenes.py $REEL
./art final $REEL                                                      # 3840x2160
```

## Beats

| Beat | Pattern | Job |
|---|---|---|
| B00 | ClaudeComposerAsk | cold open — commas moved accuracy 76% → 98% |
| B00B | Pe2Promise | executive summary: three things |
| B01 | Pe2Guess | BLUF — the model predicts, a calculator calculates |
| B02 | Pe2Chunks | tokens: 8302080 → 830 · 208 · 0 |
| B03 | Pe2Experiment | the comma experiment, 75.6% → 97.8% |
| B04 | Pe2NotRandom | temperature 0 — the errors are built in |
| B05 | Pe2Handoff | model reads, SymPy calculates; ten identical runs |
| B06 | Pe2Grading | same reference for every student; symbolic hints |
| B07 | Pe2Verdict | calculated or predicted? |
| B08 | ClaudeComposerAsk | your turn |
| B09 | Pe2Outro | title, name, credit line |

See SOURCES.md (every figure), PEDAGOGY.md (GATE P), BUILD-LOG.md (what broke).
