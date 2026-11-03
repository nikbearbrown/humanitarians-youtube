# BUILD-LOG — Progressive Tool Router (16:9)

| Item | Value |
|---|---|
| Build date | 2026-09-29 |
| Builder | Claude (Claude Code) for Dhrumil Shah |
| Blueprint | `PRODUCTION-BLUEPRINT.md` (14 scenes, §A–I) — narration, claims and structure identical to the 9:16 cut |
| Beat sheet | `beat_sheet.json` — 14 beats (S01–S14) |
| Composition | `ProgressiveToolRouter16x9` · cover `PTRCover16x9` (registered in `runtime/remotion/src/Root.tsx`, folder Progressive-Tool-Router-16x9) |
| Remotion namespaces | `src/progressive-tool-router-16x9/`, `public-progressive-tool-router-16x9/` — the 9:16 film's namespaces are untouched |
| Design canvas | 1920 × 1080, **native 16:9** — every scene re-laid out, not a crop or letterbox of the vertical cut |
| Master method | `--scale=2` → 3840 × 2160, H.264 CRF 16, AAC 320 kbps; smaller masters Lanczos-downscaled |
| FPS | 30 |

## Relationship to the 9:16 cut

Reused unchanged, so the two aspect ratios are the same film: narration WAV and measured beat
timings (`audio/timings.json`), caption cues (`captions/cues.json`, `captions/captions.json`),
music bed, SFX and the final mix, the runnable router (`src/`), the benchmark harness and task set,
`FACTCHECK.md`, and the blueprint's claim discipline.

Rebuilt for landscape: the Remotion composition (all 14 scenes) and the thumbnail.

## Narration and audio (inherited, unchanged)

| Item | Value |
|---|---|
| Engine / voice | Kokoro-82M (kokoro-onnx) · `am_onyx` · speed 1.0 · 24 kHz |
| Words | 320 |
| Narration duration | 117.99 s (measured) |
| End-card hold | 2.00 s |
| Video duration | 119.99 s — blueprint target 118 s, range 90–120 s ✅ |
| Speech stretching | none |
| Final mix | −14.4 LUFS integrated · −1.4 dBTP · 48 kHz stereo |

Measured beat durations (s): S01 10.39 · S02 8.22 · S03 7.30 · S04 9.39 · S05 9.00 · S06 7.42 ·
S07 8.33 · S08 6.31 · S09 8.88 · S10 8.01 · S11 13.94 · S12 2.95 · S13 6.89 · S14 10.95

## Landscape layout rules

| Rule | Value |
|---|---|
| Safe margins | left/right 96 px, header 40 px, content 150–900 px |
| Content grid | text column x 96–876 (780 px) · visual column x 1016–1824 (808 px) |
| Captions | burned in at y 940–1030 (design px), centred, max 1400 px wide, 40 px type — below all content, above the player bar |
| Source lines | y 915, mono 15 px, never overlapped by content |
| Chains | S04 cascade and S07 router run as vertical stacks in the visual column; S12 runs as a horizontal five-block chain across the full width — the vertical cut's tall stacks would have starved the landscape frame |
| Tool cloud | 40 × 25 = exactly 1,000 dots (the vertical cut uses 25 × 40) |

## Scene-by-scene recomposition (vs. 9:16)

| Beat | 9:16 | 16:9 |
|---|---|---|
| S01 | Stacked greeting over ghost pipeline | Greeting left, five pipeline chips right |
| S02 | Count over cloud | Count + CSV card left, cloud right |
| S03 | Definition card over vertical context bar | Definition card left, horizontal context-window bar right |
| S04 | 7-link vertical cascade | Headline left, cascade right |
| S05 | Request card, cloud, chips stacked | Request card full width, cloud left, chips + counters right |
| S06 | Cloud dissolving into 4-stage stack | Cloud dissolving into three **named tool chips** left, 4-stage stack right |
| S07 | 8-row column | Headline left, 8-row column with glosses right |
| S08 | Code panel over counter | Code panel left, counter + chips right |
| S09 | A/B table full width | Plate + headline + disclaimer left, A/B table right |
| S10 | 2 × 3 chip grid | 3 × 2 chip grid |
| S11 | Server topology over cards | Topology left, tool-search / roadmap cards + verify plate right |
| S12 | Vertical word stack | Horizontal 5-block chain |
| S13 | Centred type | Centred type, wider measure |
| S14 | Stack then end card | Headline left + pipeline right, crossfading to a centred end card |

## Claim discipline in the finished film (unchanged from 9:16)

- No token, latency, cost or accuracy figure appears anywhere.
- S09 shows only counts that are literally true of the demo registry (1,000 / 3) plus qualitative
  HIGH / LOW, under a permanent `ILLUSTRATIVE EXAMPLE` plate, with an on-screen line stating that
  real values depend on schemas, model, architecture and implementation.
- S11 carries `CURRENT-DEVELOPMENT INFO — VERIFY AGAINST OFFICIAL DOCS` for the whole scene.
- S04 frames the problem as systems overhead; its source line reads "not a claim about model
  intelligence". The phrase "more tools make a model less intelligent" appears nowhere.
- Every visual is drawn at render time (SVG/DOM). No third party's branding or visual style is used.
- The demo registry is synthetic; there is no real or personal data anywhere in the package.

## QC issues found and fixed (this cut)

| # | Stage | Issue | Fix |
|---|---|---|---|
| 1 | Storyboard | Visual column was 904 px wide at x 1016, so S02/S03/S04/S05/S07/S09/S11 bled past the right safe margin to the frame edge | `RIGHT_W` = 808 so the column ends exactly on the 1824 px margin |
| 2 | Late-reveal | S06's dissolve left three unlabelled dots floating in an empty half-frame — read as debris, not as the surviving tools | Cloud crossfades into the three **named** tool chips (CSV Reader / Data Analyzer / Chart Generator) |

Storyboard pass: 14 scenes at 70% of each beat. Review cut (960 × 540): 120.04 s, clean.
Late-reveal sheet (`_qc/late_sheet.png`, 95% of every beat): every late element lands inside its
column, captions stay in the bottom band, source lines stay clear.

## Final render and output probe

4K render time: 365 s (Remotion, `--scale=2`, concurrency 8), then Lanczos downscales.
Decode = a full `ffmpeg -f null` pass with no errors. Source: `_qc/OUTPUT-PROBE.md`.

| File | Size | Resolution | FPS | Duration | Video | Audio | Decode |
|---|---|---|---|---|---|---|---|
| Progressive-Tool-Router-4k(16x9)_Dhrumil_Shah.mp4 | 25.4 MB | 3840x2160 | 30/1 | 120.04 s | h264 | aac 48000 Hz | PASS |
| Progressive-Tool-Router-1920x1080(16x9)_Dhrumil_Shah.mp4 | 10.4 MB | 1920x1080 | 30/1 | 120.04 s | h264 | aac 48000 Hz | PASS |
| Progressive-Tool-Router-1280x720(16x9)_Dhrumil_Shah.mp4 | 6.7 MB | 1280x720 | 30/1 | 120.04 s | h264 | aac 48000 Hz | PASS |
| Progressive-Tool-Router-proxy-960x540(16x9)_Dhrumil_Shah.mp4 | 4.7 MB | 960x540 | 30/1 | 120.04 s | h264 | aac 48000 Hz | PASS |

The 0.05 s beyond 119.99 s is AAC priming/padding.

**Visual QC:** `_qc/qc-sheet.png` — 14 stills pulled from the 1920 x 1080 master at 70% of each beat.
**Storyboards:** `storyboard/beat_s01.png` … `beat_s14.png`.
**Thumbnails:** `thumbnails/cover_1920x1080.png`, `cover_3840x2160.png`.

## Blueprint §I checklist against the finished master

| # | Check | Result |
|---|---|---|
| 1 | Opens with "Hi, I am Dhrumil Shah…" | ✅ first spoken line, no prior hook |
| 2 | 3840 x 2160, 16:9 | ✅ probe |
| 3 | 30 fps, MP4 H.264, AAC 48 kHz stereo | ✅ probe |
| 4 | Runtime 90–120 s | ✅ 119.99 s (120.04 s with AAC padding) |
| 5 | Narration matches captions | ✅ same measured sentences as the 9:16 cut |
| 6 | Captions cued from measured audio | ✅ 57 cues, 0 overlaps, 0 single-word |
| 7 | Diagrams readable | ✅ reviewed at 1920-logical width and at 960 x 540 |
| 8 | Code readable | ✅ 28 px mono, ≤ 34 chars/line |
| 9 | Hypothetical metrics labelled | ✅ no metrics in the film; S09 plate + disclaimer line |
| 10 | Technical claims sourced | ✅ `FACTCHECK.md` (human re-verification still required) |
| 11 | No unsupported performance claims | ✅ none present |
| 12 | MCP terminology accurate | ✅ `tools/list`, roadmap labelled as roadmap |
| 13 | No "more tools = dumber model" framing | ✅ audited in narration and on-screen text |
| 14 | Audio clear, music subordinate | ✅ −14.4 LUFS, −1.4 dBTP, ducked bed |
| 15 | Problem → solution → implementation → takeaway | ✅ S02–S05 / S06–S07 / S08–S09 / S13–S14 |
| 16 | Safe areas respected | ✅ nothing essential outside x 96–1824 or y 150–1030 |
| 17 | Original visuals only | ✅ all SVG/DOM drawn at render time |

## Reproduce

```bash
python scripts/sync_to_remotion.py          # copy composition + audio into runtime/remotion
python scripts/render_masters.py storyboard # 14 stills
python scripts/render_masters.py review     # 960x540 review cut
python scripts/render_masters.py late       # 95%-of-beat sheet
python scripts/render_masters.py master     # 3840x2160 + 1920/1280/960
python scripts/render_masters.py cover      # thumbnails
python scripts/render_masters.py qc         # probes + QC sheet
```

Rendering requires the `brutalist.art-main` workspace: Remotion renders from its composition
registry, so a copy of this folder alone is a complete source package but not a render environment.

## Human review still required

| Gate | Status |
|---|---|
| Fact-check rows F1–F11 (`FACTCHECK.md`) re-verified on the publish date | ⏳ |
| Gate P — narration read aloud against the animatic | ⏳ |
| Benchmark run before any metric is ever added to this film | ⏳ not run; the film deliberately contains no metrics |
| Publishing | **Not authorised.** A rendered master is not permission to upload. |
