# Mycroft Phase 3 — Building More AI Agents (9:16)

A complete, reproducible production package for Dhrumil Shah's **Mycroft Phase 3** film:
a modular multi-agent financial analytics architecture covering market structure, anomaly
detection, peer benchmarking, tail risk and liquidity, and prediction reliability.

**Runtime 2:57 (176.70 s) · 2160 × 3840 · 30 fps · native 9:16.**

## What this package is, and what it is not

This folder was built **from the author's delivered master**, `D:/mycroft_phase3_4k_9x16.mp4`.
It turns that single MP4 into a source project that can be re-rendered, re-cut and re-versioned:

| Rebuilt here | Carried over unchanged from the author's master |
|---|---|
| The 11 scenes, as a Remotion composition (`scenes/remotion/`) | The narration audio (`audio/final_mix.wav`) |
| Scene layouts, chips, tables, code cards, stat cards, the agent graph | The five notebook chart panels (`assets/charts/`) |
| Burned-in captions, cued from the audio | Every number shown on screen |
| Beat, caption and timing JSON | |

**No result in this package was recomputed.** The Phase 3 dataset, notebooks and model outputs
are not part of this folder, so every figure on screen — 0.148, 19.7%, 12 stress windows,
9,636 events (3,972 / 3,397 / 2,267), the 0.516 and 0.774 ROC-AUC values, 33/33 checks — is
reproduced exactly as it appears in the author's own film, and is attributed to the author's
Phase 3 notebook run. Nothing was re-derived, re-estimated or invented. See `FACTCHECK.md`.

The one element drawn fresh rather than measured is the peer-cohort scatter in S06; it is a
schematic and is labelled as such on screen, exactly as in the master.

## Layout

```
audio/           final_mix.wav (the author's narration) · timings.json (measured beat clock)
captions/        asr_raw.json · transcript.json · cues.json · captions.json · VALIDATION.md
assets/charts/   the author's five notebook figures + PROVENANCE.json
scenes/remotion/ MycroftPhase3_9x16.tsx · MycroftPhase3Cover9x16.tsx
scripts/         build_narration_data.py · sync_to_remotion.py · render_masters.py
docs/            SOURCE-SCRIPT.md · SHOTLIST.md · DATA-DICTIONARY.md
output/          the four delivered masters
thumbnails/      cover_1080x1920.png · cover_2160x3840.png
storyboard/      one still per beat  ·  _qc/ probes, QC sheet, late-reveal sheet, review cut
beat_sheet.json  machine-readable scene spec
```

## Reproduce

```bash
python scripts/build_narration_data.py   # transcript -> cues, captions, beat clock, script
python scripts/sync_to_remotion.py       # copy composition + audio + charts into runtime/remotion
python scripts/render_masters.py storyboard
python scripts/render_masters.py review  # 540x960 review cut
python scripts/render_masters.py late    # 95%-of-beat sheet
python scripts/render_masters.py master  # 2160x3840 + 1080/720/540
python scripts/render_masters.py cover
python scripts/render_masters.py qc      # probes + QC still sheet
```

Rendering needs the `brutalist.art-main` workspace: Remotion renders from its composition
registry (`runtime/remotion/src/Root.tsx`), so a standalone copy of this folder is a complete
source package but not a render environment.

## The eleven cells

| # | Cell | Title | Start | Length |
|---|---|---|---|---|
| 01 | — | MYCROFT — PHASE 3 | 0.00 s | 16.20 s |
| 02 | A1 · AGENT FRAMEWORK | The multi-agent foundation | 16.20 s | 18.80 s |
| 03 | A2 · DATA LAYER | One validated dataset | 35.00 s | 12.80 s |
| 04 | A3 · AGENT 1 | MarketStructureAgent | 47.80 s | 16.20 s |
| 05 | A4 · AGENT 2 | AnomalyEventAgent | 64.00 s | 17.40 s |
| 06 | A7 · AGENT 3 | PeerCohortBenchmarkAgent | 81.40 s | 11.60 s |
| 07 | A8 · AGENT 4 | TailRiskLiquidityAgent | 93.00 s | 12.80 s |
| 08 | A10 · AGENT 5 | PredictionReliabilityAgent | 105.80 s | 22.80 s |
| 09 | A11 · ORCHESTRATION | MycroftOrchestrator | 128.60 s | 11.60 s |
| 10 | A11 · AGGREGATION | Human review queue | 140.20 s | 15.40 s |
| 11 | A13 · VALIDATION | Thirty-three checks | 155.60 s | 21.10 s |

## Advisory boundary

The film states it on screen and in narration, and this package repeats it:

> Educational research output from Mycroft. Not personalised financial advice or an
> investment recommendation.

`human_decision` and `human_rationale` are created empty by design — the agents rank the
queue, a person decides.

**Not published.** A rendered master is not permission to upload.
