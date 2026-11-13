# BUILD-LOG — Mycroft Phase 3 (16:9)

| Item | Value |
|---|---|
| Build date | 2026-09-30 |
| Builder | Claude (Claude Code) for Dhrumil Shah |
| Input | `C:/Users/dhrum/Downloads/mycroft_phase3_4k_16x9.mp4` — the author's delivered landscape master (3840 × 2160, 30 fps, 176.70 s, H.264 + AAC) |
| Composition | `MycroftPhase3-16x9` · cover `MycroftPhase3Cover16x9` (registered in `runtime/remotion/src/Root.tsx`, folder Mycroft-Phase-3-16x9) |
| Remotion namespaces | `src/mycroft-phase3-16x9/`, `public-mycroft-phase3-16x9/` — the 9:16 namespaces are untouched |
| Design canvas | 1920 × 1080, **native 16:9** — every cell re-laid out, not a crop or letterbox of the vertical cut |
| Master method | `--scale=2` → 3840 × 2160, H.264 CRF 16, AAC 320 kbps; smaller masters Lanczos-downscaled |
| FPS | 30 |

## What was rebuilt, and what was carried over

| Rebuilt from scratch | Carried over from the author's master, unchanged |
|---|---|
| The 11 cells as a landscape Remotion composition | The narration audio (`audio/final_mix.wav`) |
| Two-column layouts, chips, tables, code cards, stat cards, the agent graph, the S06 schematic | The five notebook chart panels (`assets/charts/`) |
| The thumbnail | Every number shown on screen |

**No result was recomputed.** The Phase 3 dataset and notebooks are not part of this package, so
every figure — 0.148, 19.7%, 12, 9,636 (3,972 / 3,397 / 2,267), 0.516, 0.774, the per-agent stage
runtimes, 33/33 — is reproduced exactly as it appears in the author's film and attributed to the
author's notebook run. See `FACTCHECK.md`.

## Relationship to the 9:16 cut

Established by measurement, not assumption:

| Check | Result |
|---|---|
| Audio | **Bit-identical** to the 9:16 master — 16,963,200 samples, max absolute sample difference 0, same MD5 |
| Cell boundaries | Measured independently from this master's own header band at 5 fps: 0 · 16.2 · 35.0 · 47.8 · 64.0 · 81.4 · 93.0 · 105.8 · 128.6 · 140.2 · 155.6 s — **identical** to the 9:16 cut |
| Chart crossfades | S04 at ~59.0 s, S08 at ~118.2 s — identical |

So the narration, beat clock, transcript and all 70 caption cues were reused as-is; no
re-transcription was needed and none was done. Only the layout was rebuilt.

## Landscape-only elements found in this master

| Cell | Element |
|---|---|
| S01 | Title set in **teal**; the five agents sit in one horizontal row beneath the hub rather than ringing it |
| S05 | **No** tag under the attribution bars (the 9:16 cut has one) |
| S07 | Tag `Measuring downside tail risk` |
| S08 | Tag `Testing model reliability by segment` |
| S09 | Per-agent runtimes (complete · 1.61s; attention_required · 1.95 / 0.22 / 0.49 / 13.23s), the `Coordinating specialized agents` tag, and the **Degrade, don't stop** note card |
| S10 | A **Sector** column in the review queue |

Each was read off the master frame by frame and reproduced; none was invented. The stage
runtimes are recorded in `FACTCHECK.md` as F14 with the caveat that they are one run's
wall-clock times, not a benchmark.

## Landscape layout rules

| Rule | Value |
|---|---|
| Safe margins | left/right 90 px; rule y 77, kicker y 100, title y 138, content from y 230 |
| Two-column grid | left x 90 w 830 · right x 990 w 840 — both end on the right safe margin at x 1830 |
| Chip stacks | inset 26 px from the rule, as in the master |
| Captions | burned in at y 916–980, centred, max 1300 px wide, 32 px semibold |
| Charts | left column in S04, S05 (chart 3 right), S08; crossfades 12 frames |

## How the timings were recovered

| Artefact | Method |
|---|---|
| Beat boundaries | The master's header band cropped and sampled at 5 fps; a mean-absolute-difference threshold located every cell change |
| Narration | Reused from the 9:16 package after proving the audio bit-identical |
| Chart panels | Bright-region detection on clean (non-crossfade) frames at t = 54, 61, 78, 111, 124 s; cropped losslessly. Recorded in `assets/charts/PROVENANCE.json`. This master renders the figures larger than the vertical one (e.g. chart 1 at 1644 × 962 vs 1466 × 860), so they were re-extracted here rather than copied |
| Palette | Reused from the vertical package; sampled from master pixels |

## QC issues found and fixed

| # | Stage | Issue | Fix |
|---|---|---|---|
| 1 | Storyboard | S10's verdict chips overlapped the review table's last row | Table row padding tightened to 9 px; chip/note block moved to y 548, code card to y 512 |
| 2 | Storyboard | S01's presenter line sat too close to the hub card | Title block raised to y 176, presenter spacing tightened |
| 3 | Storyboard | S05 carried the 9:16 cut's "Detecting abnormal market events" tag, which this master does not show | Tag removed, matching the landscape master |
| 4 | Cover | The MYCROFT hub card overlapped the "Building More AI Agents" subtitle | Hub lowered to y 452, edges re-anchored |

Storyboard pass: 11 cells at 70% of each beat. Review cut (960 × 540): 176.75 s, clean.
Late-reveal sheet (`_qc/late_sheet.png`, 95% of every beat): every late element lands inside its
column, captions stay in the bottom band, nothing is clipped.

## Final render and output probe

4K render time: 918 s (Remotion, `--scale=2`, concurrency 8), then Lanczos downscales.
Decode = a full `ffmpeg -f null` pass with no errors. Source: `_qc/OUTPUT-PROBE.md`.

| File | Size | Resolution | FPS | Duration | Video | Audio | Decode |
|---|---|---|---|---|---|---|---|
| Mycroft-Phase-3-4k(16x9)_Dhrumil_Shah.mp4 | 35.5 MB | 3840x2160 | 30/1 | 176.75 s | h264 | aac 48000 Hz | PASS |
| Mycroft-Phase-3-1920x1080(16x9)_Dhrumil_Shah.mp4 | 13.4 MB | 1920x1080 | 30/1 | 176.75 s | h264 | aac 48000 Hz | PASS |
| Mycroft-Phase-3-1280x720(16x9)_Dhrumil_Shah.mp4 | 8.5 MB | 1280x720 | 30/1 | 176.75 s | h264 | aac 48000 Hz | PASS |
| Mycroft-Phase-3-proxy-960x540(16x9)_Dhrumil_Shah.mp4 | 6.1 MB | 960x540 | 30/1 | 176.75 s | h264 | aac 48000 Hz | PASS |

The 0.05 s beyond the source's 176.70 s is AAC priming/padding.

**Visual QC:** `_qc/qc-sheet.png` — 11 stills pulled from the 1920 × 1080 master at 70% of each
beat. **Storyboards:** `storyboard/beat_s01.png` … `beat_s11.png`.
**Thumbnails:** `thumbnails/cover_1920x1080.png`, `cover_3840x2160.png`.

## Checklist against the delivered master

| # | Check | Result |
|---|---|---|
| 1 | Same running order, 11 cells, same numbering | ✅ headers `01/11` … `11/11` |
| 2 | Same runtime | ✅ 176.70 s composition vs 176.70 s source |
| 3 | 3840 × 2160, 16:9, 30 fps, H.264 + AAC 48 kHz | ✅ probe |
| 4 | Narration identical | ✅ the author's own audio, proven bit-identical and reused unchanged |
| 5 | Scene changes land on the master's cut points | ✅ measured from this master independently |
| 6 | Captions match the spoken words | ✅ word-level transcript of that audio |
| 7 | Figures on screen match the master | ✅ verbatim; see `FACTCHECK.md` F1–F14 |
| 8 | Notebook figures are the author's own | ✅ lossless crops, `assets/charts/PROVENANCE.json` |
| 9 | Schematic content labelled as schematic | ✅ S06 peer scatter carries its on-screen label |
| 10 | Advisory boundary present | ✅ narration, S10 advisory card, S11 end card |
| 11 | No personal or private data | ✅ public tickers and sector labels only |
| 12 | Safe areas respected | ✅ nothing essential outside x 90–1830 or y 77–980 |
| 13 | Original visuals only | ✅ all chrome drawn at render time; no third-party branding |

## Human review still required

| Gate | Status |
|---|---|
| Re-run the Phase 3 notebooks and re-verify `FACTCHECK.md` F1–F14 on the publish date | ⏳ |
| Re-measure the S09 stage runtimes before presenting them as performance | ⏳ |
| Confirm the ticker examples, sector labels and the 2026-02-11 market-state date are still appropriate | ⏳ |
| Gate P — narration read against the animatic | ⏳ |
| Publishing | **Not authorised.** A rendered master is not permission to upload. |
