# BUILD-LOG — hai-third-week-midjourney

## 2026-09-30 — first build (Windows 11, Git Bash, native toolchain)

Decisions
- New reel, not a variation: week 2 (hai-second-week) named Midjourney inside a story pipeline; week 3 is the
  hands-on how-to — prompt → generate → refine → upscale & use → check before posting. New greeting (Olá —
  Namaste/Hola/Hej/Ciao/Bonjour already used) and five new scenes; no earlier body scene reused.
- Channel: claude skin, chip **@Shubh & @HumanitariansAI** on every Claude page — beginning (B00), middle (B03),
  end (B08 verdict, B09 handoff) — and on the outro. Voice Kokoro `af_bella`, Plain register. B01 opens
  "Hi, I'm Shubh, and this video is about…" per the brief.
- Beat 2 correction: "Midjourney makes the image for you." → "for" becomes "with" (you pick, refine, re-prompt).
- EXECUTABLE-EVIDENCE fallback: Midjourney is a paid external service, so it is never run and never faked. Every
  picture is `ScenePic` (deterministic vector drawing of the drafted prompt), captioned "Illustration — not
  Midjourney output"; no Midjourney logo or UI imitation. Product facts checked against current public
  descriptions; no prices or version numbers (they date).
- TTS: "Olá" was heard as "Allah" by Whisper (wrong stress) → B00 narration respelled "Oh, lah!"; screen keeps "Olá, Shubh".
- GATE L: five searches (prompt anatomy, four-image grid, variation branches, upscale into formats, zoom-and-check)
  were misses → built `runtime/remotion/src/scenes/MidjourneySteps.tsx` (16:9) + `MidjourneySteps916.tsx` (9:16):
  PromptAnatomy, FourGrid, RefineLoop, UpscaleToUse, PostCheck, registered as `<Name>` and `<Name>916`; scene-index re-run.
- Reveal timing from faster-whisper word timestamps (`_words.json`).

QC fixes (16:9)
- Pre-render width checks: one-word swap shortened ("…bookshop on a"), format labels split to two lines, upscale
  cards widened, flaw line raised.
- GATE T §8.3b: dark buildings vs grey sky read as low-contrast text → lighter sky and street in ScenePic.
- GATE T §8.1: lowercase prompt/label text under the floor → B04 prompt 54 px, bar label 46 px, plan note 58 px.
- GATE T §8.6b: curved arrows fused the B05 frames into one blob → arrows removed (labels carry the meaning).
- GATE V underfill: B01 fontSize 210. GATE F: SHOTLIST.md added.

Portrait-only props (vertical/beat_sheet.json): composer largeText off; B01 4-line reflow at 330; B02 short part
labels/values, shape labels 16:9 · 1:1 · 9:16; B04 short prompt + labels, caption "Illustration"; B05 Subtle /
Strong, "a rainy → snowy street"; B06 short upscale labels, ar-only format tags, "Set --ar, don't crop."; B07
spark "Step 5 · Check it", short checks; B08 four short lines, textScale 2.0; B10 title on three lines.

Portrait QC note: `./art run <vertical>` defaults to --height 2160, which scales 2160×3840 media to an odd
1215 px width and pads one column (0xF3EBDD) — GATE V read that pad column as edge-bleed on B00. The raw render
was clean; the portrait review cut is run at its exact scale (`--height 1920`), where GATE V is 0/0.
Portrait polish: B04 prompt card given more room.

Environment notes
- `PYTHONUTF8=1` is required on Windows; review cuts use `ART_NO_DRAWTEXT=1`.

Gate results (final exports)
- 16:9 renders/hai-third-week-midjourney.mp4 — 3840×2160, 150.3 s; GATE L/V/T pass; receipt hai-third-week-midjourney.verified.json
- 9:16 renders/hai-third-week-midjourney-vertical.mp4 — 2160×3840, 150.3 s; GATE L/V/T pass; receipt hai-third-week-midjourney-vertical.verified.json
