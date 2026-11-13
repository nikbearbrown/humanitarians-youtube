# BUILD-LOG — Progressive Tool Router (9:16)

| Item | Value |
|---|---|
| Build date | 2026-09-29 |
| Builder | Claude (Claude Code) for Dhrumil Shah |
| Blueprint | `PRODUCTION-BLUEPRINT.md` (14 scenes, §A–I) |
| Beat sheet | `beat_sheet.json` — 14 beats (S01–S14) |
| Composition | `ProgressiveToolRouter9x16` · cover `PTRCover9x16` (registered in `runtime/remotion/src/Root.tsx`, folder Progressive-Tool-Router) |
| Remotion namespaces | `src/progressive-tool-router/`, `public-progressive-tool-router/` — no other film touched |
| Design canvas | 1080 × 1920, native 9:16 (no crop, no letterbox) |
| Master method | `--scale=2` → 2160 × 3840, H.264 CRF 16, AAC 320 kbps; smaller masters Lanczos-downscaled |
| FPS | 30 |

## Narration and audio

| Item | Value |
|---|---|
| Engine / voice | Kokoro-82M (kokoro-onnx) · **`am_onyx`** · speed 1.0 · 24 kHz |
| Voice rationale | The film opens "Hi, I am Dhrumil Shah" — a male voice matches the presenter. (The two earlier films use `af_kore`; that mismatch is still open there.) |
| Words | 320 |
| Narration duration | 117.99 s (measured) |
| End-card hold | 2.00 s |
| Video duration | 119.99 s — blueprint target 118 s, range 90–120 s ✅ |
| Speech stretching | none |
| Music / SFX | code-synthesised; 22 SFX cues; music side-chain ducked under narration |
| Final mix | −14.4 LUFS integrated · −1.4 dBTP · 48 kHz stereo |

Measured beat durations (s): S01 10.39 · S02 8.22 · S03 7.30 · S04 9.39 · S05 9.00 · S06 7.42 ·
S07 8.33 · S08 6.31 · S09 8.88 · S10 8.01 · S11 13.94 · S12 2.95 · S13 6.89 · S14 10.95

## Captions

`captions/VALIDATION.md`: 67 measured sentence cues → 57 captions · 0 overlaps · shortest 1.00 s ·
longest wrapped line 24 characters · 0 single-word captions · burned in at y 1372–1540 (design px),
above the platform UI band. Keyword highlighting on: agent, tools, MCP, context, progressive,
discovery, registry, semantic, search, ranking, top-K, latency, tokens, Claude, intent, routing.

## Claim discipline in the finished film

- No token, latency, cost or accuracy figure appears anywhere on screen.
- S09 shows only counts that are literally true of the demo registry (1,000 / 3) plus qualitative
  HIGH / LOW, under a permanent `ILLUSTRATIVE EXAMPLE` plate, with an on-screen line stating that
  real values depend on schemas, model, architecture and implementation.
- S11 carries `CURRENT-DEVELOPMENT INFO — VERIFY AGAINST OFFICIAL DOCS` for the whole scene, and the
  narration itself tells viewers to check the official docs.
- S04 frames the problem as systems overhead; the source line reads "not a claim about model
  intelligence". The phrase "more tools make a model less intelligent" appears nowhere.

## QC issues found and fixed

| # | Stage | Issue | Fix |
|---|---|---|---|
| 1 | Setup | First folder-creation command died on shell quoting, so `scripts/` did not exist; the audio chain then failed on `cp` | Directories created explicitly; pipeline scripts copied and patched |
| 2 | Pipeline | Copied scripts expected `af_kore`, `beat_XX` naming, and music sections from the previous film | Patched: `am_onyx`, `beat_<id>` naming, new section map (intro/problem/turn/build/resolve), SFX aliases (swish, warn, search, rank) |
| 3 | Beat sheet | Music/SFX generator expects `sound_design.sfx`; the authored sheet had `sfx` at beat level | Wrapped on load; `end_hold_seconds` added |
| 4 | Visual S02/S05/S06 | 1,000-dot tool cloud read as texture, not tools (3.2 px at 55% opacity on a dark ground) | Dots 4.4 px, opacity 0.82; highlighted dots 9.5 px |
| 5 | Visual S08 | Tool chips overlapped the source line | Chip row lifted to y 1104, gap tightened |
| 6 | Cover | "1,000 TOOLS" overran the safe margin; "→ 3" unbalanced | 126 px headline, arrow + numeral on a baseline-aligned row |

Storyboard pass: all 14 scenes compiled and rendered at 70% of each beat. Review cut (540×960)
rendered cleanly, 120.04 s. Late-reveal sheet (`_qc/late_sheet.png`, 95–97% of S01, S02, S04–S09,
S11–S13 plus the end card): every late element lands inside its column, captions stay in the bottom
band, source lines stay clear.

## Final render and output probe

4K render time: 377 s (Remotion, `--scale=2`, concurrency 8), then Lanczos downscales.
Decode = full `ffmpeg -f null` pass with no errors. Source: `_qc/OUTPUT-PROBE.md`.

| File | Size | Resolution | FPS | Duration | Video | Audio | Decode |
|---|---|---|---|---|---|---|---|
| `output/Progressive-Tool-Router-4k(9x16)_Dhrumil_Shah.mp4` | 24.5 MB | 2160 × 3840 | 30 | 120.04 s | H.264 | AAC 48 kHz | PASS |
| `output/Progressive-Tool-Router-1080x1920(9x16)_Dhrumil_Shah.mp4` | 9.8 MB | 1080 × 1920 | 30 | 120.04 s | H.264 | AAC 48 kHz | PASS |
| `output/Progressive-Tool-Router-720x1280(9x16)_Dhrumil_Shah.mp4` | 6.6 MB | 720 × 1280 | 30 | 120.04 s | H.264 | AAC 48 kHz | PASS |
| `output/Progressive-Tool-Router-proxy-540x960(9x16)_Dhrumil_Shah.mp4` | 3.8 MB | 540 × 960 | 30 | 120.04 s | H.264 | AAC 48 kHz | PASS |

The 0.05 s beyond 119.99 s is AAC priming/padding.

**Visual QC:** `_qc/qc-sheet.png` — 14 stills from the 1080 × 1920 master at 70% of each beat; all
fixes 4–6 present. **Storyboards:** `storyboard/beat_s01.png` … `beat_s14.png`.
**Thumbnails:** `thumbnails/cover_1080x1920.png`, `cover_2160x3840.png`.

## Blueprint §I checklist against the finished master

| # | Check | Result |
|---|---|---|
| 1 | Opens with "Hi, I am Dhrumil Shah…" | ✅ first spoken line, no prior hook |
| 2 | 2160 × 3840, 9:16 | ✅ probe |
| 3 | 30 fps, MP4 H.264, AAC 48 kHz stereo | ✅ probe |
| 4 | Runtime 90–120 s | ✅ 119.99 s (120.04 s with AAC padding) |
| 5 | Narration matches captions | ✅ captions generated from the same measured sentences |
| 6 | Captions cued from measured audio | ✅ 57 cues, 0 overlaps, 0 single-word |
| 7 | Diagrams readable on a phone | ✅ reviewed at 1080-logical width |
| 8 | Code readable on a phone | ✅ 30 px mono, ≤ 34 chars/line |
| 9 | Hypothetical metrics labelled | ✅ no metrics in the film; S09 plate + disclaimer line |
| 10 | Technical claims sourced | ✅ `FACTCHECK.md` (human re-verification still required) |
| 11 | No unsupported performance claims | ✅ none present |
| 12 | MCP terminology accurate | ✅ `tools/list`, roadmap labelled as roadmap |
| 13 | No "more tools = dumber model" framing | ✅ audited in narration and on-screen text |
| 14 | Audio clear, music subordinate | ✅ −14.4 LUFS, −1.4 dBTP, ducked bed |
| 15 | Problem → solution → implementation → takeaway | ✅ S02–S05 / S06–S07 / S08–S09 / S13–S14 |
| 16 | Safe areas respected | ✅ nothing essential above y 150, below y 1540, or right of x 940 |
| 17 | Original visuals only | ✅ all SVG/DOM drawn at render time |

## Human review still required

| Gate | Status |
|---|---|
| Fact-check rows F1–F11 (`FACTCHECK.md`) re-verified on the publish date | ⏳ |
| Gate P — narration read aloud against the animatic | ⏳ |
| Benchmark run before any metric is ever added to this film | ⏳ not run; film deliberately contains no metrics |
| Publishing | **Not authorised.** A rendered master is not permission to upload. |
