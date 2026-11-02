# Don't Invent the Mass. — BRUTALIST REBUILD GUIDE

Physics Engine series, video 4 of 12. Host: Param Madan. Voice: Kokoro `af_bella`.
Video by Param Madan · Engine by Jash Shah, Harsh Gujarati, Atharva & Param Madan.

**Claim:** Parse is the only stage where a language model acts, and it may only read. Its rules — engine vocabulary, SI units, no constants, letters stay letters — exist because a misread number is the one error later checks can't catch. The engine once invented `m = 1.0` for symbolic problems; reporting them as symbols fixed it and let SymPy solve them exactly.

Source project: https://github.com/jashshah127/humanitariansai/tree/2dc4aa4/physics-engine

## Video

Rendered videos are not stored in this repository.

| Cut | File | Resolution | Runtime |
|---|---|---|---:|
| 16:9 long-form | `dont-invent-the-mass.mp4` | 3840x2160 | 3:26 |

**Persona:** Param Madan (host) · **Voice:** Kokoro `af_bella` · **Palette:** claude (cream, warm ink, terracotta)

## Rebuild

```bash
REEL=~/books/physics-engine/youtube/dont-invent-the-mass
cd ~/brutalist.art
cp $REEL/src/PhysicsEngine04.tsx runtime/remotion/src/scenes/
# paste src/Root.registration.tsx: the import near the top of Root.tsx,
# the <Folder> block inside the returned fragment
./.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL     # GATE P: PEDAGOGY.md signed
./.venv/bin/python runtime/scripts/remotion_scenes.py $REEL
./art final $REEL                                                      # 3840x2160
```

## Beats

| Beat | Pattern | Job |
|---|---|---|
| B00 | ClaudeComposerAsk | cold open — "mass m" became 1.0 |
| B00B | Pe4Promise | executive summary: three things |
| B01 | Pe4OneJob | BLUF — may / may not; a misread survives every check |
| B02 | Pe4Vocab | model names → engine names |
| B03 | Pe4Rules | SI, no constants, rest = 0 |
| B04 | Pe4Invented | 734 of 1,226; m = 1.0, q = 1.0 |
| B05 | Pe4Symbolic | a = g(m2 − m1)/(m1 + m2); identity check |
| B06 | Pe4Honest | traceable; parse error ≠ not covered; not proven yet |
| B07 | Pe4Verdict | check what it read |
| B08 | ClaudeComposerAsk | your turn |
| B09 | Pe4Outro | title, name, credit line |

See SOURCES.md (every figure), PEDAGOGY.md (GATE P), BUILD-LOG.md (what broke).
