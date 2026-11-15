# Hints, Not Answers. — BRUTALIST REBUILD GUIDE

Physics Engine series, video 11 of 12. Host: Param Madan. Voice: Kokoro `af_bella`.
Video by Param Madan · Engine by Jash Shah, Harsh Gujarati, Atharva & Param Madan.

**Claim:** with Physics Engine mode on every answer wears a badge (verified, needs review, unverified), and tutor mode reveals a verified solution one rung at a time, holding back the answer, the equations and even the card name until their rung.

Source project: https://github.com/jashshah127/humanitariansai/tree/2dc4aa4/physics-engine

## Video

Rendered videos are not stored in this repository.

| Cut | File | Resolution | Runtime |
|---|---|---|---:|
| 16:9 long-form | `hints-not-answers.mp4` | 3840x2160 | 3:11 |

**Persona:** Param Madan (host) · **Voice:** Kokoro `af_bella` · **Palette:** claude (cream, warm ink, terracotta)

## Rebuild

```bash
REEL=~/books/physics-engine/youtube/hints-not-answers
cd ~/brutalist.art
cp $REEL/src/PhysicsEngine11.tsx runtime/remotion/src/scenes/
# paste src/Root.registration.tsx: the import near the top of Root.tsx,
# the <Folder> block inside the returned fragment
./.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL     # GATE P: PEDAGOGY.md signed
./.venv/bin/python runtime/scripts/remotion_scenes.py $REEL
./art final $REEL                                                      # 3840x2160
```

## Beats

| Beat | Pattern | Job |
|---|---|---|
| B00 | ClaudeComposerAsk | Ask: hints without the answer? |
| B00B | Pe11Promise | Promise: badge, ladder, symbolic |
| B01 | Pe11Badges | Verified / needs review / unverified |
| B02 | Pe11Floor | Unverified = switch off, labeled |
| B03 | Pe11Rungs1 | Atwood hints 1-4 |
| B04 | Pe11Rungs2 | Hints 5-7: pitfall, formula, answer |
| B05 | Pe11Design | No second model call; holds back |
| B06 | Pe11Better | Symbolic hints; 11.04 -> 6.30 ms |
| B07 | Pe11Verdict | Next step, not the last |
| B08 | ClaudeComposerAsk | Viewer task |
| B09 | Pe11Outro | Outro + credits |

See SOURCES.md (every figure), PEDAGOGY.md (GATE P), BUILD-LOG.md (what broke).
