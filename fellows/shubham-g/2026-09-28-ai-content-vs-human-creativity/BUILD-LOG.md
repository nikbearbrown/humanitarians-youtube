# BUILD-LOG — ai-content-vs-human-creativity

## 2026-09-28 — first build (Windows 11, Git Bash, native toolchain)

Decisions
- New reel, not a variation: new topic framing ("AI Content vs. Human Creativity: What Works Better?"),
  new greeting (Ciao — Hola/Namaste/Hej already used in the series) and five new scenes. None of the
  Social* scenes from earlier reels are reused.
- Channel: claude skin, chip **@Shubh & @HumanitariansAI** on every Claude page — beginning (B00), middle
  (B03), end (B08 verdict, B09 handoff) — and on the outro. Voice Kokoro `af_bella`, Plain register.
  B01 opens "Hi, I'm Shubh, and this video is about…" per the brief.
- Beat 2 correction: "AI content beats human creativity. One video makes a post." →
  "scales" / "week of posts". The writer swaps single words only, so the misconception is carried by
  two one-word triggers.
- GATE L: five searches (timeline → moments, content cascade, voice check, AI/human sort, phone clips)
  were all misses for a dual-aspect scene, so they were logged to TEMPLATE-MISSES.md. Built
  `runtime/remotion/src/scenes/ContentRepurpose.tsx` (16:9) + `ContentRepurpose916.tsx` (9:16):
  RepurposeSource, RepurposeClips, RepurposeCascade, RepurposeVoiceCheck, CreativityBalance,
  each registered as `<Name>` and `<Name>916` in Root.tsx; `./art scene-index` re-run.
- Reveal timing: word timestamps from faster-whisper (`_words.json`) placed every `*At` prop on the
  spoken word.
- No statistics (none in the brief). Example captions, voice guide and draft are labelled illustrative.
- The brief's reference link was the YouTube home page, not a specific video — nothing taken from it.

QC fixes (from reading frames + gates)
- B02: moment highlights covered the chapter labels → labels left-aligned, highlights moved to the right
  of each chapter; playhead inset so it never crosses SAFE's right edge (GATE V BLOCKER).
- B04: pick ring clipped the "TikTok" label → labels/bar moved up, pill overlaps the phone bottom.
- B05: "Newsletter" overflowed its card and the week brace hit it → wider leaf column, brace below leaves.
- B06: strike-through landed between wrapped lines → draft at 50px, flagged line kept on one line.
- B08 (16:9): `largeText` on; six lines pushed the card over the chip → five lines.
- B01: underfill (GATE V MAJOR) → fontSize 158.
- GATE T §8.1: lowercase-only fragments (x-height) under 41px → italic notes/trace line ≥ 56px serif /
  46px sans, node and chip labels 52px.
- GATE T §8.6b: an ink chip border enclosing its label read as an overlapping text run → chip borders
  stay the light border colour (no checker exemption added).

Portrait-only props (vertical/beat_sheet.json, same meaning, fewer words):
composer `largeText` off; B01 text reflowed at fontSize 255, lineSpacing 1.8 (the 916 writer scales font size by 0.5625); B02
"LONG-FORM VIDEO", chapter "Voice", moments Hook/Story/Tip, shorter job line; B04 shorter AI line;
B05 "Long Video", Title Case labels, shorter week line; B06 shorter guide values, draft lines "Made from one video." / "Guaranteed hack!",
"Try this one idea."; B07 shorter row labels/notes, verdict "The pair wins."; B08
four short lines, textScale 2.0; B10 title on three lines, scale 0.8.

Environment notes
- `PYTHONUTF8=1` is required on Windows; review cuts use `ART_NO_DRAWTEXT=1`.

Portrait QC fixes: B06 caption lifted off the logo bug; B07 verdict rule moved inside SAFE; B08 cut to
four lines (the card overran the chip); B01 enlarged for GATE V fill.

Gate results (final exports)
- 16:9 renders/ai-content-vs-human-creativity.mp4 — 3840×2160, 160.4 s; GATE L/V/T pass; receipt ai-content-vs-human-creativity.verified.json
- 9:16 renders/ai-content-vs-human-creativity-vertical.mp4 — 2160×3840, 160.4 s; GATE L/V/T pass; receipt ai-content-vs-human-creativity-vertical.verified.json
- Skin lint (advisory, same as earlier reels): HandleTitleOutro instead of the @NikBearBrown-locked ClaudeTitleOutro.
