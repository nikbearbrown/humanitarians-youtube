# Who Does the Math. — BRUTALIST REBUILD GUIDE

Physics Engine series, video 1 of 17. Host: Param Madan. Voice: Kokoro `af_bella`.
Video by Param Madan · Engine by Jash Shah, Harsh Gujarati, Atharva & Param Madan.

**Claim:** In the physics engine, the language model reads the problem, picks the
formula and explains; a symbolic solver (SymPy + pint) does every calculation — and
the engine decides *before* solving whether its answer is final, ambiguous, or out
of scope.

Source project: https://github.com/jashshah127/humanitariansai/tree/2dc4aa4/physics-engine

## Video

Rendered videos are not stored in this repository.

| Cut | File | Resolution | Runtime |
|---|---|---|---:|
| 16:9 long-form | `who-does-the-math.mp4` | 3840x2160 | 4:12 |

**Persona:** Param Madan (host) · **Voice:** Kokoro `af_bella` · **Palette:** claude (cream, warm ink, terracotta)

## Rebuild

```bash
REEL=~/books/physics-engine/youtube/who-does-the-math
cd ~/brutalist.art
cp $REEL/src/PhysicsEngine01.tsx runtime/remotion/src/scenes/
# paste src/Root.registration.tsx: the import near the top of Root.tsx,
# the <Folder> block inside the returned fragment
./.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL     # GATE P: PEDAGOGY.md signed
./.venv/bin/python runtime/scripts/remotion_scenes.py $REEL
./art final $REEL                                                      # 3840x2160
```

## Beats

| Beat | Pattern | Job |
|---|---|---|
| B00 | ClaudeComposerAsk | cold open — who actually computed the number? |
| B00B | Pe1Promise | executive summary: who / when / what's proven |
| B01 | Pe1Split | BLUF — words to the model, math to the solver |
| B02 | Pe1NotGame | not a game engine; question in, solution object out |
| B03 | Pe1Pipeline | Parse → Retrieve → Plan → Solve → Verify |
| B04 | Pe1Routes | three routes, decided before solving |
| B05 | Pe1Proof | 16/16, ten identical runs, OpenStax 3.27 vs 3.2667 |
| B06 | Pe1Honest | what is not proven yet |
| B07 | Pe1Verdict | three questions to ask any AI answer |
| B08 | ClaudeComposerAsk | your turn |
| B09 | Pe1Outro | title, name, credit line |

See SOURCES.md (every figure), PEDAGOGY.md (GATE P), BUILD-LOG.md (what broke).
