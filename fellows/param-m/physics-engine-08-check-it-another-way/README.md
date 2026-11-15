# Check It Another Way. — BRUTALIST REBUILD GUIDE

Physics Engine series, video 8 of 12. Host: Param Madan. Voice: Kokoro `af_bella`.
Video by Param Madan · Engine by Jash Shah, Harsh Gujarati, Atharva & Param Madan.

**Claim:** every engine answer is substituted back, sign-checked, and (on 11 of 31 cards) re-derived another way; anything that fails is flagged, not hidden.

Source project: https://github.com/jashshah127/humanitariansai/tree/2dc4aa4/physics-engine

## Video

Rendered videos are not stored in this repository.

| Cut | File | Resolution | Runtime |
|---|---|---|---:|
| 16:9 long-form | `check-it-another-way.mp4` | 3840x2160 | 3:02 |

**Persona:** Param Madan (host) · **Voice:** Kokoro `af_bella` · **Palette:** claude (cream, warm ink, terracotta)

## Rebuild

```bash
REEL=~/books/physics-engine/youtube/check-it-another-way
cd ~/brutalist.art
cp $REEL/src/PhysicsEngine08.tsx runtime/remotion/src/scenes/
# paste src/Root.registration.tsx: the import near the top of Root.tsx,
# the <Folder> block inside the returned fragment
./.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL     # GATE P: PEDAGOGY.md signed
./.venv/bin/python runtime/scripts/remotion_scenes.py $REEL
./art final $REEL                                                      # 3840x2160
```

## Beats

| Beat | Pattern | Job |
|---|---|---|
| B00 | ClaudeComposerAsk | Ask: how do you know it is right? |
| B00B | Pe8Promise | Promise: three checks |
| B01 | Pe8Three | The three checks |
| B02 | Pe8Residual | Residual: plug back in, < 1e-4 |
| B03 | Pe8Positive | Positivity: no negative mass |
| B04 | Pe8Second | Independent path: KCL, RC at tau, orbit |
| B05 | Pe8Laws | Laws as unit tests: sqrt 2, Carnot |
| B06 | Pe8Labels | 11 of 31 cards have verify_fn |
| B07 | Pe8Verdict | verified vs flagged |
| B08 | ClaudeComposerAsk | Viewer task |
| B09 | Pe8Outro | Outro + credits |

See SOURCES.md (every figure), PEDAGOGY.md (GATE P), BUILD-LOG.md (what broke).
