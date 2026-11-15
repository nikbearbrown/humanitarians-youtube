# The Engine That Says No. — BRUTALIST REBUILD GUIDE

Physics Engine series, video 6 of 12. Host: Param Madan. Voice: Kokoro `af_bella`.
Video by Param Madan · Engine by Jash Shah, Harsh Gujarati, Atharva & Param Madan.

**Claim:** Before solving, the engine checks closure: can the equations pin down every unknown with what's given? If not, it stops, names the reason, marks the answer unverified and logs the gap. On 60 UGPhysics problems that meant zero wrong answers and nearly everything declined — a measure of honesty, not coverage. Sometimes declining was the bug: symbolic problems were refused only because answers were forced to decimals.

Source project: https://github.com/jashshah127/humanitariansai/tree/2dc4aa4/physics-engine

## Video

Rendered videos are not stored in this repository.

| Cut | File | Resolution | Runtime |
|---|---|---|---:|
| 16:9 long-form | `the-engine-that-says-no.mp4` | 3840x2160 | 3:07 |

**Persona:** Param Madan (host) · **Voice:** Kokoro `af_bella` · **Palette:** claude (cream, warm ink, terracotta)

## Rebuild

```bash
REEL=~/books/physics-engine/youtube/the-engine-that-says-no
cd ~/brutalist.art
cp $REEL/src/PhysicsEngine06.tsx runtime/remotion/src/scenes/
# paste src/Root.registration.tsx: the import near the top of Root.tsx,
# the <Folder> block inside the returned fragment
./.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL     # GATE P: PEDAGOGY.md signed
./.venv/bin/python runtime/scripts/remotion_scenes.py $REEL
./art final $REEL                                                      # 3840x2160
```

## Beats

| Beat | Pattern | Job |
|---|---|---|
| B00 | ClaudeComposerAsk | cold open — zero wrong by declining |
| B00B | Pe6Promise | executive summary: three things |
| B01 | Pe6Closure | BLUF — closure, yes → solve, no → stop |
| B02 | Pe6Reasons | missing knowns · solver error · no definite answer |
| B03 | Pe6Queue | damped oscillator → unverified → coverage queue |
| B04 | Pe6Sixty | 60 problems, 0 wrong, nearly all declined |
| B05 | Pe6Hidden | float() at the end hid real capability |
| B06 | Pe6Refuse | not_assessable → human review; a CI check |
| B07 | Pe6Verdict | could it have said no? |
| B08 | ClaudeComposerAsk | your turn |
| B09 | Pe6Outro | title, name, credit line |

See SOURCES.md (every figure), PEDAGOGY.md (GATE P), BUILD-LOG.md (what broke).
