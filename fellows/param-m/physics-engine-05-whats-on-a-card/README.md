# What's on a Card. — BRUTALIST REBUILD GUIDE

Physics Engine series, video 5 of 12. Host: Param Madan. Voice: Kokoro `af_bella`.
Video by Param Madan · Engine by Jash Shah, Harsh Gujarati, Atharva & Param Madan.

**Claim:** A formula card is a small, checked package — equations, required knowns, outputs, applicability and pitfalls — and the engine can only solve what its cards cover. The applicability becomes the solution's stated assumption. New cards are built against real benchmark answers (Vibrations and Waves: zero cards → eight, all matching); the library still has footholds, not depth.

Source project: https://github.com/jashshah127/humanitariansai/tree/2dc4aa4/physics-engine

## Video

Rendered videos are not stored in this repository.

| Cut | File | Resolution | Runtime |
|---|---|---|---:|
| 16:9 long-form | `whats-on-a-card.mp4` | 3840x2160 | 3:25 |

**Persona:** Param Madan (host) · **Voice:** Kokoro `af_bella` · **Palette:** claude (cream, warm ink, terracotta)

## Rebuild

```bash
REEL=~/books/physics-engine/youtube/whats-on-a-card
cd ~/brutalist.art
cp $REEL/src/PhysicsEngine05.tsx runtime/remotion/src/scenes/
# paste src/Root.registration.tsx: the import near the top of Root.tsx,
# the <Folder> block inside the returned fragment
./.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL     # GATE P: PEDAGOGY.md signed
./.venv/bin/python runtime/scripts/remotion_scenes.py $REEL
./art final $REEL                                                      # 3840x2160
```

## Beats

| Beat | Pattern | Job |
|---|---|---|
| B00 | ClaudeComposerAsk | cold open — what is a formula card? |
| B00B | Pe5Promise | executive summary: three things |
| B01 | Pe5Package | BLUF — a small, checked package |
| B02 | Pe5Anatomy | the spring card, field by field |
| B03 | Pe5Assume | applicability → stated assumption; 2.37 m/s |
| B04 | Pe5Pitfalls | wave-number and from-rest pitfalls |
| B05 | Pe5Built | 179 problems, 0 → 8 cards, three matches |
| B06 | Pe5Thin | 180 : 1; T means two things |
| B07 | Pe5Verdict | ask when it applies |
| B08 | ClaudeComposerAsk | your turn |
| B09 | Pe5Outro | title, name, credit line |

See SOURCES.md (every figure), PEDAGOGY.md (GATE P), BUILD-LOG.md (what broke).
