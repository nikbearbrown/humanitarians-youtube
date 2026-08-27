# Gemma 4, Unified?

**Fellow:** Ritik B. · **Built:** 2026-08-05 · **Voice:** Kokoro `am_onyx` ·
**Playlist:** Claude for Education

A 3m02s teardown of **Gemma 4 12B's encoder-free architecture**: what Google
deleted from the front of the model, and why the technical report does not
establish that deleting it was free.

> Gemma 4's newest member reasons about images and sound with almost no
> perception hardware in front of it — a 550M-parameter vision encoder became a
> 35M-parameter matrix multiply, and the audio encoder was removed outright —
> but nobody has run the experiment that would show that's a good idea.

MMMU-Pro puts the encoder-free 12B at 69.1 against 76.9 for the 31B — worse.
FLEURS ASR puts it at 0.067 WER against 0.075 for E4B — better. Both
comparisons move parameter count *and* architecture at once, and Table 5
benchmarks the 12B against Gemma 3 rather than against its own siblings, so
parity with encoders is unproven in either direction. The film says that out
loud as an ARGUMENT beat rather than smuggling it in as a finding.

Two framings the fact-check rejected and the narration cuts: Gemma 4 is not
"any-to-any" (it emits text only; the label is a HuggingFace pipeline name for
*input* modalities), and this is not generator/discriminator convergence (no
generative visual head, no discriminator). What it demonstrates is *encoder*
convergence.

## Production state

- 12 beats, all filled, no slates
- Fact-check: 31 claims against primary sources, verified 2026-08-02 — `FACTCHECK.md`
- Gate P narration review: PASS — `PEDAGOGY.md`
- PROOF review: teaching 12/12, production gate PASS (first cut was 10/12 and a
  FAIL; revision 4 fixed it) — `PROOF-REVIEW.md`
- Master: 181.80s · 3840×2160 @ 24fps · AAC mono 24kHz · GATE V clean
  (24 frames, 0 BLOCKER / 0 MAJOR)
- Publishing: **not authorized, never published**

The master MP4 and all build intermediates are excluded per the root
`.gitignore`. `qc-sheet.png` is the contact sheet for the clean master. The
master is reproducible from the files here.

## Contents

```
beat_sheet.json       narration, shot per beat, scene props — source of truth
NARRATION.md          the spoken script (12 beats)
FACTCHECK.md          31 claims, primary sources, verdicts
PEDAGOGY.md           GATE P — thesis, act structure, human narration verdict
BUILD-LOG.md          build record, every defect found and fixed
PROOF-REVIEW.md       review against the PROOF protocol
scenes.py             intentionally empty of Manim scenes — this reel is pure Remotion
qc-sheet.png          QC contact sheet for the clean master
remotion/scenes/      the Remotion scenes written for this reel
patches/              modifications to the upstream brutalist.art toolkit
```

Scenes: `GemmaEncoderStack.tsx` (three input lanes into a decoder; focus states
walk the deletion), `GemmaScoreboard.tsx` (MMMU-Pro vs FLEURS; `confound` state
reveals parameter counts), `GemmaConvergenceThread.tsx` (the two-convergences
reframe), `GemmaExecSummary.tsx` (presenter, thesis, three-card roadmap),
`PredictCardBeat.tsx` (predict beat wrapper).

## Rebuild

The toolkit is not vendored — clone it and apply the patch:

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
```

```bash
cd brutalist.art && git checkout b2b1185 && git apply /path/to/this/folder/patches/brutalist-toolkit.patch
```

Copy `remotion/scenes/*.tsx` into `runtime/remotion/src/scenes/`, place this
folder at `<book>/youtube/gemma4-unified/`, then:

```bash
./setup --install
```

```bash
./art run /path/to/youtube/gemma4-unified
```

Audio-first: narration MP3s are generated and measured before anything renders,
and their durations become the master clock. Two build notes that cost real
time:

- **Never run the audio step while renders are in flight.** `remotion_scenes.py`
  does an unlocked read-modify-write of `beat_sheet.json` per beat, so a render
  that loaded the sheet before the audio write will save its stale copy back
  over `actual_duration_s`. `mp3/timings.json` keeps the ground truth if it
  happens.
- **Scene `durationInFrames` is the animation length.** These scenes drive
  everything off `useP()` (`frame/durationInFrames`) and clips are truncated to
  their beat length, so each registered duration must be at or under the
  *shortest* measured beat that uses that scene.

Cost to produce: $0.00, no API keys.

## Attribution

Built with the [brutalist.art](https://github.com/nikbearbrown/brutalist.art)
toolkit by Nik Bear Brown. It carries no LICENSE file, so it is not
redistributed here — only a patch of local modifications and the scene files
written for this reel. Kokoro-82M (`am_onyx`) produced the narration. Gemma 4
is Google DeepMind's; figures come from the sources cited in `FACTCHECK.md`.

Upstream source repo: <https://github.com/RITIK-12/HAI_Gemma_4_arch>
