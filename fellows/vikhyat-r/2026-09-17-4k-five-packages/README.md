# Five Ways to Catch a Resolution Problem — Vikhyat R

Part 1 of 2. Lays out five proposed packages for catching non-4K submissions
earlier, each with its cost and its limit. Explains a proposal; does not
advocate for one.

11 beats · 2:52 · `@HumanitariansAI` · delivered 3840×2160 and 2160×3840.
Companion: `2026-09-17-4k-three-workflows`.

Source only. The rendered masters are not in this repo.

## This week's contribution

**Question.** Fellows' videos arrive in the shared Drive folder at the wrong
resolution, and today that is only discovered by uploading each one to YouTube
and looking. Can it be found earlier, and where?

**Prediction.** That the 4K capability was missing from the toolkit.

**What I built.** I audited the toolkit first. The capability is not missing —
`./art final` produces correct 4K by default for landscape. I then built this
reel to lay out five places a check could sit, and a companion reel on how they
combine.

**Observed result.** The prediction was wrong. The failures come from four
different resolutions in circulation across the written guidance, no agreed
target for 9:16, and no check on the finished file.

**Next experiment.** A read-only report over the submissions folder, and a
resolution check at the point the toolkit writes a master.

## Human and AI work

**My decisions:** scope and framing; the register (describe, don't insist);
routing content beats through Manim rather than Remotion so the scene code
lives with the reel; every accept/reject on layout and wording; verification of
both masters.

**AI tools:** Claude Code (Opus 5) for the audit, beat sheet, Manim scenes and
the Windows Remotion shim. Narration is Kokoro TTS, `am_michael`, local and
free — AI narration is disclosed in the reel. No generative image or video:
every frame is a Manim or Remotion vector render.

**What I rejected or corrected:** six defects caught by the toolkit's own gates
and fixed at source rather than by loosening the gate — a static table that
GATE A read as a text slide, an empty band left by a transform, a title
overshoot of 0.05 units affecting every scene, white cards indistinguishable
from the cream ground, text clipped out of its card, and a card crossing the
frame edge.

**What remains unverified:** the YouTube-side 4K playback check, pending upload.

## Files

| File | What it is |
|---|---|
| `beat_sheet.json` | The script. 11 beats, narration, timing, component per beat |
| `scenes.py` | The nine Manim scenes, landscape |
| `vertical/beat_sheet.json` | Portrait sheet, derived by `./art vertical` |
| `vertical/scenes.py` | Portrait scenes — a rewrite, not a re-render |
| `FACTCHECK.md` | Every on-screen claim with its `file:line` |
| `SHOTLIST.md` | Typed work order |
| `PROMPTS.md` | Per-beat record |
| `render_remotion_win.py` | Windows stand-in for `remotion_scenes.py` |

## Reproduce

```
python3 runtime/scripts/generate_audio_kokoro.py <reel>
bash runtime/scripts/run.sh <reel>
./art final <reel> --out <dir>

./art vertical <reel>
bash runtime/scripts/run.sh <reel>/vertical --height 3840
./art final <reel>/vertical --height 3840 --out <dir>
```

`--height 3840` is required on **both** the run and the final for portrait.
Without it a 9:16 sheet compiles at 1216×2160.

**Windows prerequisites:** a `python3` shim on PATH (the name resolves to the
Microsoft Store placeholder by default); `PYTHONUTF8=1`; `PYTHONIOENCODING=utf-8`;
`ART_NO_DRAWTEXT=1`; and `render_remotion_win.py` in place of
`remotion_scenes.py`, which invokes `npx` in a way Windows cannot execute.

**Gates:** F, L, SHAPE, A, W, B and V all run at default strictness. `ART_QC`
and `ART_STRICT` were never lowered. GATE V final: 0 blockers, 0 majors.


## Verification performed

| Check | Result |
|---|---|
| Probed dimensions (file, not flag) | 3840×2160 / 2160×3840 |
| Native 4K vs upscaled | 11.6×–14.1× sharpness margin over a deliberate upscale of the same frames |
| Outro handle | `@HumanitariansAI`, confirmed by inspecting the frame, both ratios |
| Slates | none — 11/11 slots filled |
| Portrait fallback | none — every portrait beat has a purpose-built scene |

## Known deviations

1. **No burned-in channel caption on the portrait cut.** `hai/SKILL.md:227`
   asks for `metadata.channel_title`. At 2160×3840 `compile.py` renders it
   883px wide at x 638–1521 — 225px outside `final_frame_check.BURN_IN_EXCLUDE`
   (x 0–1296) and 49px below the title-safe bottom (3648), which GATE V blocks
   as edge-bleed. The same caption is 498px wide in landscape and sits inside
   the mask. The handle is carried by the outro card in both cuts.
2. **Remotion rendered through `render_remotion_win.py`** rather than
   `remotion_scenes.py`. Same CLI, same flags, foreground, props read verbatim.
3. **The outro is a Manim card, not `ClaudeTitleOutro`** — that component
   hardcodes `@NikBearBrown` (`ClaudeTitleOutro.tsx:19`, locked by
   `OUTRO-LOCK.md`) and this is an HAI reel.
   `skills/make/fellows/SKILL.md:141-142` sets the same precedent.
