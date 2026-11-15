# Force Is Not Time. — BRUTALIST REBUILD GUIDE

Physics Engine series, video 7 of 12. Host: Param Madan. Voice: Kokoro `af_bella`.
Video by Param Madan · Engine by Jash Shah, Harsh Gujarati, Atharva & Param Madan.

**Claim:** The engine verifies unit *labels*: every unit string must be a real physical dimension, and each card's unit must agree with the variable dictionary. That audit rediscovered the T tension/period collision with dimensional evidence. Units are not yet carried through the algebra, and pint — named in the plan — is not used; the team says both plainly.

Source project: https://github.com/jashshah127/humanitariansai/tree/2dc4aa4/physics-engine

## Video

Rendered videos are not stored in this repository.

| Cut | File | Resolution | Runtime |
|---|---|---|---:|
| 16:9 long-form | `force-is-not-time.mp4` | 3840x2160 | 3:04 |

**Persona:** Param Madan (host) · **Voice:** Kokoro `af_bella` · **Palette:** claude (cream, warm ink, terracotta)

## Rebuild

```bash
REEL=~/books/physics-engine/youtube/force-is-not-time
cd ~/brutalist.art
cp $REEL/src/PhysicsEngine07.tsx runtime/remotion/src/scenes/
# paste src/Root.registration.tsx: the import near the top of Root.tsx,
# the <Folder> block inside the returned fragment
./.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL     # GATE P: PEDAGOGY.md signed
./.venv/bin/python runtime/scripts/remotion_scenes.py $REEL
./art final $REEL                                                      # 3840x2160
```

## Beats

| Beat | Pattern | Job |
|---|---|---|
| B00 | ClaudeComposerAsk | cold open — T meant force and time |
| B00B | Pe7Promise | executive summary: three things |
| B01 | Pe7Labels | BLUF — checked now vs. not yet |
| B02 | Pe7Why | m/s, m, N, s; 4 cm → off by ×100 |
| B03 | Pe7Checks | real dimension; card vs. dictionary; CI |
| B04 | Pe7Collision | T: N on the pulley, s on orbit/field cards |
| B05 | Pe7Overloaded | glossary says "N or s", "m or ohm" |
| B06 | Pe7Swap | pint planned → sympy.physics.units used |
| B07 | Pe7Verdict | check the units first |
| B08 | ClaudeComposerAsk | your turn |
| B09 | Pe7Outro | title, name, credit line |

See SOURCES.md (every figure), PEDAGOGY.md (GATE P), BUILD-LOG.md (what broke).
