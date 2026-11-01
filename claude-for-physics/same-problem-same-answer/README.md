# Same Problem, Same Answer. — BRUTALIST REBUILD GUIDE

Physics Engine series, video 9 of 12. Host: Param Madan. Voice: Kokoro `af_bella`.
Video by Param Madan · Engine by Jash Shah, Harsh Gujarati, Atharva & Param Madan.

**Claim:** the solver is deterministic, so the engine routes each problem (one card, none, or several) before solving and returns every candidate when more than one fits.

Source project: https://github.com/jashshah127/humanitariansai/tree/2dc4aa4/physics-engine

## Video

Rendered videos are not stored in this repository.

| Cut | File | Resolution | Runtime |
|---|---|---|---:|
| 16:9 long-form | `same-problem-same-answer.mp4` | 3840x2160 | 3:20 |

**Persona:** Param Madan (host) · **Voice:** Kokoro `af_bella` · **Palette:** claude (cream, warm ink, terracotta)

## Rebuild

```bash
REEL=~/books/physics-engine/youtube/same-problem-same-answer
cd ~/brutalist.art
cp $REEL/src/PhysicsEngine09.tsx runtime/remotion/src/scenes/
# paste src/Root.registration.tsx: the import near the top of Root.tsx,
# the <Folder> block inside the returned fragment
./.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL     # GATE P: PEDAGOGY.md signed
./.venv/bin/python runtime/scripts/remotion_scenes.py $REEL
./art final $REEL                                                      # 3840x2160
```

## Beats

| Beat | Pattern | Job |
|---|---|---|
| B00 | ClaudeComposerAsk | Ask: same problem, same answer? |
| B00B | Pe9Promise | Promise: three things |
| B01 | Pe9Solver | SymPy has no randomness |
| B02 | Pe9Sources | Selection or an LLM: the only two sources |
| B03 | Pe9Routes | deterministic / no path / ambiguous |
| B04 | Pe9Ambiguous | Car vs spring: 30 vs 2.37 m/s |
| B05 | Pe9Why | Fairness, debuggability, cost |
| B06 | Pe9Limit | Parsing can still vary |
| B07 | Pe9Verdict | Explainable consistency |
| B08 | ClaudeComposerAsk | Viewer task |
| B09 | Pe9Outro | Outro + credits |

See SOURCES.md (every figure), PEDAGOGY.md (GATE P), BUILD-LOG.md (what broke).
