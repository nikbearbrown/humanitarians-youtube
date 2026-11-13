# BUILD-LOG — why-great-content-doesnt-perform

## 2026-09-30 — first build (Windows 11, Git Bash, native toolchain)

Decisions
- New reel, not a variation: previous reels covered visibility automation, repurposing, AI vs human creativity
  and Midjourney. This one explains why strong content underperforms — audience fit, distribution, timing,
  format, algorithms, paid amplification — plus a falsifiability beat (sometimes the content IS the problem).
  New greeting **Aloha** (Namaste/Hola/Hej/Ciao/Bonjour/Olá already used) and eight new scenes; no earlier body scene reused.
- Channel: claude skin, chip **@Shubh & @HumanitariansAI** on every Claude page — beginning (B00), middle (B05),
  end (B11 verdict, B12 handoff) — and on the outro. Voice Kokoro `af_bella`, Plain register. B01 opens
  "Hi, I'm Shubh, and this video is about…" per the brief. The brief's reference link was a bare youtube.com
  URL (no specific video), so no reference video was used.
- Beat 2 correction: "Great content always finds its audience." → `always`→`still`, `finds`→`has to reach`.
  BrutalistHesitantWriter matches single-word triggers only (whitespace tokens), so a phrase trigger
  ("always finds") silently never corrects. Fixed with two positional single-word swaps.
- No statistics: every chart/audience is illustrative with no numeric axis, captioned; ranking weights stated as not public.
- GATE L: searches for a chain/one-weak-link, two-audience fit, distribution paths, timing curve, format phones,
  signal loop, paid lanes and a diagnose flow found no fitting scenes → built
  `runtime/remotion/src/scenes/ContentPerformance.tsx` (dual-aspect: ReachChain, AudienceFit, DistributionPaths,
  TimingWindow, FormatFit, SignalLoop, PaidReach, DiagnoseFlow), registered as `<Name>` and `<Name>916`; scene-index re-run.
- Reveal timing from faster-whisper word timestamps (`_words.json`).

QC fixes (16:9)
- Preview stills: TimingWindow chip collided with the logo bug → chip moved to the end of the 7 PM bar; SignalLoop
  rings brushed the caption → centre/radii reduced; FormatFit dead space → larger phones; PaidReach lanes shortened.
- GATE V: B01 underfill → fontSize 250, faster typing (charMs 90); remaining 50%-sample underfill is mid-typing by design →
  `qc.sparse_by_design` with written reason. B03 low-contrast → inactive people use INK_SOFT. B06 edge-bleed → chip
  enters from the left, inset 8 px.
- Frame review: B11 six verdict lines pushed the card over the chip → five lines.
- GATE T §8.1: 40 px italic notes (B04) and "Small test group" (B08) → 46 px; B04 notes then touched the people row →
  label column 520. GATE T §8.3: accent-bordered chip read as accent text → ink border + solid accent bar.
- One transient `ffmpeg … Conversion failed!` on the first `./art run`; standalone encode succeeded and the rerun passed.

Portrait-only props (vertical/beat_sheet.json, applied by `python portrait_props.py vertical/beat_sheet.json`): composer largeText off;
B01 five-line reflow at 280; B02 "It stalls.", no caption; B03 "A budgeting guide", "Joke scrollers" / "Budget planners",
"Different room."; B06 3-label axis, "3 AM"/"7 PM", "FIRST HOUR", "→ more people"; B07 "Text wall"/"Short video",
"Point first"; B08 "Strong → it grows" / "Weak → it stops"; B09 "Boost", "Results", "Paid amplifies fit.";
B10 short questions/fixes; B11 five short lines, textScale 2.0; B13 title on three lines, scale 0.8.
Portrait layout code: B02 grid 8×2, chain rows 104, no break-slide (it crossed SAFE916); B03 rooms 460; B10 fix cards wider.

Environment notes
- `PYTHONUTF8=1` is required on Windows; review cuts use `ART_NO_DRAWTEXT=1`.

Portrait QC fixes (GATE T at 2160×3840)
- §8.1: lone person heads read as small text runs (B04, B08) → portrait people drawn as joined silhouettes; B08 people 76.
- §8.6b: B10 number discs and ink-bordered fix cards fused with the arrowhead → plain "1." numbers, hairline fix borders
  (accent kept on the last), arrowhead pulled 30 px off the card.

Gate results (final exports)
- 16:9 renders/why-great-content-doesnt-perform.mp4 — 3840×2160, 177.9 s; GATE L/V/T pass; receipt why-great-content-doesnt-perform.verified.json
- 9:16 renders/why-great-content-doesnt-perform-vertical.mp4 — 2160×3840, 177.9 s; GATE L/V/T pass; receipt why-great-content-doesnt-perform-vertical.verified.json
- Frame review: every beat at 15/50/85 % in both aspects read by eye (`_qc/beats/sheet*.png`, `vertical/_qc/beats/sheet*.png`).
