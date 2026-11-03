# BUILD-LOG — Mycroft Phase 3 (9:16)

| Item | Value |
|---|---|
| Build date | 2026-09-30 |
| Builder | Claude (Claude Code) for Dhrumil Shah |
| Input | `D:/mycroft_phase3_4k_9x16.mp4` — the author's delivered master (2160 × 3840, 30 fps, 176.70 s, H.264 + AAC 222 kbps) |
| Composition | `MycroftPhase3-9x16` · cover `MycroftPhase3Cover9x16` (registered in `runtime/remotion/src/Root.tsx`, folder Mycroft-Phase-3) |
| Remotion namespaces | `src/mycroft-phase3-9x16/`, `public-mycroft-phase3-9x16/` — no other film in the workspace touched |
| Design canvas | 1080 × 1920, native 9:16 |
| Master method | `--scale=2` → 2160 × 3840, H.264 CRF 16, AAC 320 kbps; smaller masters Lanczos-downscaled |
| FPS | 30 |

## What was rebuilt, and what was carried over

This package turns a single delivered MP4 into a re-renderable source project.

| Rebuilt from scratch | Carried over from the author's master, unchanged |
|---|---|
| The 11 scenes as a Remotion composition | The narration audio (`audio/final_mix.wav`, extracted losslessly to 48 kHz stereo PCM) |
| Layouts, chips, tables, code cards, stat cards, the agent graph, the S06 schematic | The five notebook chart panels (`assets/charts/`) |
| Burned-in captions | Every number shown on screen |
| All timing, caption and beat JSON | |

**No result was recomputed.** The Phase 3 dataset and notebooks are not part of this package, so
every figure — 0.148, 19.7%, 12, 9,636 (3,972 / 3,397 / 2,267), 0.516, 0.774, 33/33 — is
reproduced exactly as it appears in the author's film and attributed to the author's notebook
run. See `FACTCHECK.md`.

## How the timings were recovered

| Artefact | Method |
|---|---|
| Beat boundaries | The master's header band (`CELL Ax · SECTION · nn/11`) was cropped and sampled at 5 fps; a mean-absolute-difference threshold located every cell change. Result: 0 · 16.2 · 35.0 · 47.8 · 64.0 · 81.4 · 93.0 · 105.8 · 128.6 · 140.2 · 155.6 s. |
| Narration | faster-whisper `base.en`, word-level timestamps, on the master's own audio. 439 words, 27 sentences. |
| In-scene chart swaps | Frame sampling located the S04 crossfade at ~59.0 s and the S08 crossfade at ~118.2 s. |
| Chart panels | Bright-region detection on clean (non-crossfade) frames at t = 54, 61, 80, 113, 126 s; cropped losslessly. Recorded in `assets/charts/PROVENANCE.json`. |
| Palette | Sampled directly from master pixels (background gradient #060D1B → #172037, grid, rule, kicker teal, caption plate #05070D). |

Transcript corrections were limited to words the recogniser misheard — Dhrumil, Mycroft, Amihud,
variance, and the agent/class names. Each correction inherits the matched span's timing, so a
correction can never shift a caption off the audio. The correction tables are in
`scripts/build_narration_data.py`.

## Narration and audio

| Item | Value |
|---|---|
| Source | the author's own recording, reused unchanged — **not re-synthesised, re-timed or re-voiced** |
| Words | 439 |
| Sentences | 27 |
| Speech span | 0.00 s → 176.14 s |
| Video duration | 176.70 s (2:57) |

Measured beat durations (s): S01 16.20 · S02 18.80 · S03 12.80 · S04 16.20 · S05 17.40 ·
S06 11.60 · S07 12.80 · S08 22.80 · S09 11.60 · S10 15.40 · S11 21.10

## Captions

`captions/VALIDATION.md`: 27 sentence cues → 70 burned-in captions · 0 overlaps · 0 captions
under 3 words · shortest 0.48 s · one centred line, white on #05070D at y 1378–1445, clear of
the platform UI band.

## QC issues found and fixed

| # | Stage | Issue | Fix |
|---|---|---|---|
| 1 | Registry | Remotion rejects `_` in a composition id (`MycroftPhase3_9x16`) | id renamed `MycroftPhase3-9x16`; the React component keeps its name |
| 2 | Storyboard | S01 was missing the header rule/kicker the master shows on the title card, and the title block collided with the presenter name | kicker `MYCROFT · PHASE 3 · 01/11` restored; title block moved to y 330, graph to y 620 |
| 3 | Storyboard | The chart panels already contain their own white card, so the extra card fill rendered as grey bars beside chart 10 | chart card background set transparent |
| 4 | Storyboard | S07's code card ran under the caption band | lower block lifted to y 940, code size 17, tighter gap |
| 5 | Captions | "Amihud" survived as the recogniser's "armi-hood" — the fix was a single-token rule but the recogniser emitted two tokens | moved to the phrase-level pass, which runs after hyphen joining |

Storyboard pass: 11 scenes at 70% of each beat. Review cut (540 × 960): 176.75 s, clean.
Late-reveal sheet (`_qc/late_sheet.png`, 95% of every beat): every late element lands inside its
column, captions stay in the bottom band, nothing is clipped.

## Final render and output probe

4K render time: 505 s (Remotion, `--scale=2`, concurrency 8), then Lanczos downscales.
Decode = a full `ffmpeg -f null` pass with no errors. Source: `_qc/OUTPUT-PROBE.md`.

| File | Size | Resolution | FPS | Duration | Video | Audio | Decode |
|---|---|---|---|---|---|---|---|
| `output/Mycroft-Phase-3-4k(9x16)_Dhrumil_Shah.mp4` | 33.5 MB | 2160 × 3840 | 30 | 176.75 s | H.264 | AAC 48 kHz | PASS |
| `output/Mycroft-Phase-3-1080x1920(9x16)_Dhrumil_Shah.mp4` | 12.6 MB | 1080 × 1920 | 30 | 176.75 s | H.264 | AAC 48 kHz | PASS |
| `output/Mycroft-Phase-3-720x1280(9x16)_Dhrumil_Shah.mp4` | 7.9 MB | 720 × 1280 | 30 | 176.75 s | H.264 | AAC 48 kHz | PASS |
| `output/Mycroft-Phase-3-proxy-540x960(9x16)_Dhrumil_Shah.mp4` | 4.8 MB | 540 × 960 | 30 | 176.75 s | H.264 | AAC 48 kHz | PASS |

The 0.05 s beyond the source's 176.70 s is AAC priming/padding.

**Visual QC:** `_qc/qc-sheet.png` — 11 stills pulled from the 1080 × 1920 master at 70% of each
beat. **Storyboards:** `storyboard/beat_s01.png` … `beat_s11.png`.
**Thumbnails:** `thumbnails/cover_1080x1920.png`, `cover_2160x3840.png`.

## Checklist against the delivered master

| # | Check | Result |
|---|---|---|
| 1 | Same running order, 11 cells, same numbering | ✅ headers `01/11` … `11/11` |
| 2 | Same runtime | ✅ 176.70 s composition (176.75 s with AAC padding) vs 176.70 s source |
| 3 | 2160 × 3840, 9:16, 30 fps, H.264 + AAC 48 kHz | ✅ probe |
| 4 | Narration identical | ✅ the author's own audio, reused unchanged |
| 5 | Scene changes land on the master's cut points | ✅ measured from the master, not estimated |
| 6 | Captions match the spoken words | ✅ cut from a word-level transcript of that audio |
| 7 | Figures on screen match the master | ✅ verbatim; see `FACTCHECK.md` F1–F12 |
| 8 | Notebook figures are the author's own | ✅ lossless crops, `assets/charts/PROVENANCE.json` |
| 9 | Schematic content labelled as schematic | ✅ S06 peer scatter carries its on-screen label |
| 10 | Advisory boundary present | ✅ narration, S10 advisory card, S11 end card |
| 11 | No personal or private data | ✅ public tickers only |
| 12 | Safe areas respected | ✅ nothing essential above y 199 or below y 1445 |
| 13 | Original visuals only | ✅ all chrome drawn at render time; no third-party branding |

## Human review still required

| Gate | Status |
|---|---|
| Re-run the Phase 3 notebooks and re-verify `FACTCHECK.md` F1–F11 on the publish date | ⏳ |
| Confirm the ticker examples and the 2026-02-11 market-state date are still appropriate | ⏳ |
| Gate P — narration read against the animatic | ⏳ |
| Publishing | **Not authorised.** A rendered master is not permission to upload. |
