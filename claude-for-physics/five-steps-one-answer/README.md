# Five Steps, One Answer. — BRUTALIST REBUILD GUIDE

Physics Engine series, video 3 of 17. Host: Param Madan. Voice: Kokoro `af_bella`.
Video by Param Madan · Engine by Jash Shah, Harsh Gujarati, Atharva & Param Madan.

**Claim:** The engine solves every problem in five steps — parse, retrieve, plan,
solve, verify — and only parse uses a language model. One golden-set problem
(MECH-001: 2.5 m/s² for 12 s from rest → 30 m/s, 180 m) is carried through all five,
including the closure check that rejects five of six candidate cards.

Source project: https://github.com/jashshah127/humanitariansai/tree/2dc4aa4/physics-engine

## Video

Rendered videos are not stored in this repository.

| Cut | File | Resolution | Runtime |
|---|---|---|---:|
| 16:9 long-form | `five-steps-one-answer.mp4` | 3840x2160 | 3:43 |

**Persona:** Param Madan (host) · **Voice:** Kokoro `af_bella` · **Palette:** claude (cream, warm ink, terracotta)

## Rebuild

```bash
REEL=~/books/physics-engine/youtube/five-steps-one-answer
cd ~/brutalist.art
cp $REEL/src/PhysicsEngine03.tsx runtime/remotion/src/scenes/
# paste src/Root.registration.tsx: the import near the top of Root.tsx,
# the <Folder> block inside the returned fragment
./.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL     # GATE P: PEDAGOGY.md signed
./.venv/bin/python runtime/scripts/remotion_scenes.py $REEL
./art final $REEL                                                      # 3840x2160
```

## Beats

| Beat | Pattern | Job |
|---|---|---|
| B00 | ClaudeComposerAsk | cold open — the car problem |
| B00B | Pe3Promise | executive summary: three things |
| B01 | Pe3Steps | BLUF — five steps, one job each; only parse uses a model |
| B02 | Pe3Parse | knowns with their source phrases; "starts from rest" → v0 = 0 |
| B03 | Pe3Retrieve | 31 cards; six can give a speed or a distance |
| B04 | Pe3Plan | closure check — five gaps, one card closes |
| B05 | Pe3Solve | SymPy: 30 m/s, 180 m |
| B06 | Pe3Verify | plug back in; second path v² = v0² + 2as |
| B07 | Pe3Verdict | the solution object; three questions for any AI |
| B08 | ClaudeComposerAsk | your turn |
| B09 | Pe3Outro | title, name, credit line |

A shared five-step rail runs across B02–B06 so the viewer always knows where they are.

See SOURCES.md (every figure), PEDAGOGY.md (GATE P), BUILD-LOG.md (what broke).
