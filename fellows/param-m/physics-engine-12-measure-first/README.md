# Measure First. — BRUTALIST REBUILD GUIDE

Physics Engine series, video 12 of 12. Host: Param Madan. Voice: Kokoro `af_bella`.
Video by Param Madan · Engine by Jash Shah, Harsh Gujarati, Atharva & Param Madan.

**Claim:** fine-tuning is conditional on results plateauing below target with full card coverage; neither holds (16/16 golden set, 0 wrong on 60 UGPhysics problems, most declined), so the bottleneck is coverage, not intelligence.

Source project: https://github.com/jashshah127/humanitariansai/tree/2dc4aa4/physics-engine

## Video

Rendered videos are not stored in this repository.

| Cut | File | Resolution | Runtime |
|---|---|---|---:|
| 16:9 long-form | `measure-first.mp4` | 3840x2160 | 3:08 |

**Persona:** Param Madan (host) · **Voice:** Kokoro `af_bella` · **Palette:** claude (cream, warm ink, terracotta)

## Rebuild

```bash
REEL=~/books/physics-engine/youtube/measure-first
cd ~/brutalist.art
cp $REEL/src/PhysicsEngine12.tsx runtime/remotion/src/scenes/
# paste src/Root.registration.tsx: the import near the top of Root.tsx,
# the <Folder> block inside the returned fragment
./.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL     # GATE P: PEDAGOGY.md signed
./.venv/bin/python runtime/scripts/remotion_scenes.py $REEL
./art final $REEL                                                      # 3840x2160
```

## Beats

| Beat | Pattern | Job |
|---|---|---|
| B00 | ClaudeComposerAsk | Ask: why not fine-tune? |
| B00B | Pe12Promise | Promise: golden set, benchmark, trigger |
| B01 | Pe12Trigger | The plan's written trigger |
| B02 | Pe12Golden | 16/16 golden set; OpenStax 3.27 |
| B03 | Pe12Denominator | UGPhysics 1,226: 18% scorable, 79% ceiling |
| B04 | Pe12Bottleneck | 60 problems, 0 wrong, nearly all declined |
| B05 | Pe12Discipline | Interesting vs indicated work |
| B06 | Pe12Open | Golden set size, baseline, deployment |
| B07 | Pe12Verdict | Measure first |
| B08 | ClaudeComposerAsk | Viewer task |
| B09 | Pe12Outro | Outro + credits |

See SOURCES.md (every figure), PEDAGOGY.md (GATE P), BUILD-LOG.md (what broke).
