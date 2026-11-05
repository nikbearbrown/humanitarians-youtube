# Where It Went Wrong. — BRUTALIST REBUILD GUIDE

Physics Engine series, video 10 of 12. Host: Param Madan. Voice: Kokoro `af_bella`.
Video by Param Madan · Engine by Jash Shah, Harsh Gujarati, Atharva & Param Madan.

**Claim:** grade mode compares a student's number with the verified answer and with wrong formulas built from the correct one (sign flip, reciprocal, factor of 2, sqrt 2, forgotten square root), names the match, and refuses to grade against an unverified answer.

Source project: https://github.com/jashshah127/humanitariansai/tree/2dc4aa4/physics-engine

## Video

Rendered videos are not stored in this repository.

| Cut | File | Resolution | Runtime |
|---|---|---|---:|
| 16:9 long-form | `where-it-went-wrong.mp4` | 3840x2160 | 3:12 |

**Persona:** Param Madan (host) · **Voice:** Kokoro `af_bella` · **Palette:** claude (cream, warm ink, terracotta)

## Rebuild

```bash
REEL=~/books/physics-engine/youtube/where-it-went-wrong
cd ~/brutalist.art
cp $REEL/src/PhysicsEngine10.tsx runtime/remotion/src/scenes/
# paste src/Root.registration.tsx: the import near the top of Root.tsx,
# the <Folder> block inside the returned fragment
./.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL     # GATE P: PEDAGOGY.md signed
./.venv/bin/python runtime/scripts/remotion_scenes.py $REEL
./art final $REEL                                                      # 3840x2160
```

## Beats

| Beat | Pattern | Job |
|---|---|---|
| B00 | ClaudeComposerAsk | Ask: what does grade mode say? |
| B00B | Pe10Promise | Promise: which, where, refuses |
| B01 | Pe10Diagnose | Checker vs grade mode |
| B02 | Pe10Patterns | Five mistake patterns |
| B03 | Pe10SignFlip | Atwood: -1.96 = sign_flip + pitfall |
| B04 | Pe10FirstWrong | Spinning disk: first wrong step |
| B05 | Pe10Fair | +/-2% tolerance, five statuses |
| B06 | Pe10Refuse | No unverified grading, nothing stored |
| B07 | Pe10Verdict | Wrong vs which mistake |
| B08 | ClaudeComposerAsk | Viewer task |
| B09 | Pe10Outro | Outro + credits |

See SOURCES.md (every figure), PEDAGOGY.md (GATE P), BUILD-LOG.md (what broke).
