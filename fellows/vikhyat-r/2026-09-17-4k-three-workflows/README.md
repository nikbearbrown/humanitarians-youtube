# Three Workflows, and What Separates Them — Vikhyat R

Part 2 of 2. Shows how the five packages combine into three end-to-end
workflows, and spends the time on what distinguishes them rather than narrating
every step. Explains a proposal; does not advocate for one.

10 beats · 2:33 · `@HumanitariansAI` · delivered 3840×2160 and 2160×3840.
Companion: `2026-09-17-4k-five-packages`.

Source only. The rendered masters are not in this repo.

## This week's contribution

**Question.** Given five possible checks, how do they actually fit together,
and are they alternatives or a sequence?

**What I built.** Three workflows — A prevents, B describes, C organises what
B described — each shown as a flow, then a beat on what only each one does, and
a beat on why the order is the argument rather than the list.

**Observed result.** They are not three bids for the same job. A sits upstream
of B; C only makes sense once B is trusted. Someone could run all three, or
only B, or only A.

**What I was careful about.** The reel states plainly that none of this removes
the post-upload YouTube check, because our own submission guidance
(`docs/FELLOWS-SUBMISSION.md:147-148`) says a local file cannot prove how
YouTube will handle it. The proposal reduces upload cycles; it does not replace
the reviewer's judgement.

## Human and AI work

**My decisions:** the three-workflow framing; the choice to show each as a flow
rather than narrate its steps; the register; and the composition calls — B03's
funnel uses width to carry a cost argument without a number, B06 is a single
spine rather than three columns because parallel columns would read as "pick
one".

**AI tools:** Claude Code (Opus 5) for the beat sheet and Manim scenes.
Narration is Kokoro TTS, `am_michael`, local and free — disclosed in the reel.
No generative image or video.

**What I rejected or corrected:** one defect, caught by GATE V — B06 filled
only 42% of the frame against a 55% minimum. GATE A and GATE B both passed it,
because nothing overlapped or left the frame; it was simply left-heavy with
half the canvas empty. Fixed by giving each row a consequence column on the
right, which fills the frame and strengthens the beat.

Eight of eight scenes passed GATE A and GATE B on the first attempt here,
against six fix cycles on the companion reel. The difference is that this
reel's `scenes.py` carries the earlier reel's lessons as comments, applied
before anything was drawn.

**What remains unverified:** the YouTube-side 4K playback check, pending upload.

## Files

| File | What it is |
|---|---|
| `beat_sheet.json` | The script. 10 beats, narration, timing, component per beat |
| `scenes.py` | The eight Manim scenes, landscape |
| `vertical/beat_sheet.json` | Portrait sheet, derived by `./art vertical` |
| `vertical/scenes.py` | Portrait scenes — a rewrite, not a re-render |
| `FACTCHECK.md` | Every claim, marked as repo-verified or author's reasoning |
| `SHOTLIST.md` | Typed work order |
| `PROMPTS.md` | Per-beat record |
| `render_remotion_win.py` | Windows stand-in for `remotion_scenes.py` |

## Portrait is a rewrite, not a re-render

This reel leans harder on horizontal arrangements than its companion, so more
had to be restructured for a 4.5-unit-wide frame:

| Beat | Landscape | Portrait |
|---|---|---|
| B02 | flow left→right, loop underneath | flow downward, refusal loops up the left |
| B03 | funnel narrows left→right | tapers top→bottom |
| B04 | two folders side by side | stacked |
| B06 | spine left, consequence column right | one column, consequence beneath each row |
| B07 | stays / goes side by side | stacked; the lower one still fades |

`vertical/scenes.py` forces `config.frame_width = 4.5`. Manim does **not**
derive a portrait frame from a portrait pixel canvas — it keeps `frame_width`
at 14.2222 and scales the axes differently, which distorts every shape. That
override is load-bearing.

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
Without it a 9:16 sheet compiles at 1216×2160 — and GATE V reports that as
`edge-bleed` on every frame rather than as a resolution problem, which points
you at your scene layouts instead of the compile height.

**Windows prerequisites:** a `python3` shim on PATH; `PYTHONUTF8=1`;
`PYTHONIOENCODING=utf-8`; `ART_NO_DRAWTEXT=1`; and `render_remotion_win.py` in
place of `remotion_scenes.py`.

**Gates:** F, L, SHAPE, A, W, B and V all run at default strictness. `ART_QC`
and `ART_STRICT` were never lowered. GATE V final: 0 blockers, 0 majors.


## Verification performed

| Check | Result |
|---|---|
| Probed dimensions (file, not flag) | 3840×2160 / 2160×3840 |
| Native 4K vs upscaled | 11.7×–13.4× sharpness margin over a deliberate upscale of the same frames |
| Outro handle | `@HumanitariansAI`, confirmed by inspecting the frame, both ratios |
| Slates | none — 10/10 slots filled |
| Portrait fallback | none — every portrait beat has a purpose-built scene |

## Known deviations

Same three as the companion reel: no burned-in channel caption on the portrait
cut (it renders outside GATE V's mask at 2160×3840), Remotion driven through
`render_remotion_win.py` because `remotion_scenes.py` cannot invoke `npx` on
Windows, and a Manim outro rather than `ClaudeTitleOutro`, which is locked to
`@NikBearBrown`. Full measurements are in the companion reel's README.
