# BUILD-LOG — one-piece-of-content-into-ten

## 2026-09-29 — first build (Windows 11, Git Bash, native toolchain)

Decisions
- New reel, not a variation of ai-content-vs-human-creativity: new angle (atoms → ten formats → reshape,
  don't copy → release runway → quality gate), new greeting (Bonjour — Namaste/Hola/Hej/Ciao already used)
  and five new scenes. None of the Social*, Repurpose* or CreativityBalance scenes are reused.
- Channel: claude skin, chip **@Shubh & @HumanitariansAI** on every Claude page — beginning (B00), middle
  (B03), end (B08 verdict, B09 handoff) — and on the outro. Voice Kokoro `af_bella`, Plain register.
  B01 opens "Hi, I'm Shubh, and this video is about…" per the brief.
- Beat 2 correction: "One long video, copied into ten posts." → "copied" becomes "reshaped" (the film's
  thesis). charMs 200 so "copied" is on screen by ~4.6 s and "reshaped" types in at ~6.7–8.4 s, over the
  spoken "copying … reshaping".
- GATE L: five searches (atoms into bins, ten-format grid + counter, same idea reshaped side by side,
  release timeline, quality gate) returned only reel-specific figures or this series' own earlier scenes →
  treated as misses. Built `runtime/remotion/src/scenes/OneIntoTen.tsx` (16:9) + `OneIntoTen916.tsx` (9:16):
  AtomSplit, TenFormats, ReshapeNotCopy, ReleaseRunway, QualityGate, each registered as `<Name>` and
  `<Name>916` in Root.tsx; `./art scene-index` re-run.
- `HandleTitleOutro` gained an opt-in `accentPunct` prop (default true = unchanged for earlier reels);
  this reel sets it false so the large "?" renders in ink (GATE T §8.3) and the spark stays the accent.
- Reveal timing: faster-whisper word timestamps (`_words.json`) placed every `*At` prop on the spoken word.
- No statistics (none in the brief). Example copy, schedule and the 7-of-10 gate are labelled illustrative.
- The brief's reference link was the YouTube home page, not a specific video — nothing taken from it.

QC fixes (16:9, from reading frames + gates)
- B04: two-line format names collided with their atom tags → taller tiles, smaller glyph, counter lifted.
- B05: shape note touched "OPENS WITH"; "How do you reuse yours?" hit the card edge → body moved down,
  taller columns. Crossfade replaced by a hand-off (pasted copy fully out before the reshaped copy in).
- B07: check 2 wrapped → "Feels native?"; gate bar overshot SAFE's right edge (GATE V BLOCKER) → sweep
  clamped inside SAFE.
- B01 / B10 underfill (GATE V MAJOR) → B01 fontSize 215; B10 scale 1.2.
- GATE T §8.6b: ink borders around chip labels read as overlapping text runs → chip / check / cut-pill
  borders use the light border colour (no checker exemption added).
- GATE T §8.3: terracotta "?" on the enlarged outro → ink punctuation via accentPunct.

Portrait-only props (vertical/beat_sheet.json, same meaning, fewer words): composer largeText off; B01
5-line reflow at fontSize 330, lineSpacing 1.65; B02 numbered chips, line "Pull the atoms out first.";
B04 short format names; B05 short example copy, "Same idea, 3 shapes.", caption "Example copy"; B06 spark
"Not all on day one.", anchor "Long video · Day 1", "All ten point back."; B07 checks "Stands alone? ·
Native? · Scroll-stopping?", verdict "Seven strong beat ten weak."; B08 four short lines, textScale 2.0;
B10 title on three lines.

Portrait QC fixes: B01 enlarged (underfill); B04 tiles shortened so "pieces" clears the logo bug; B06
accent ring moved from the whole anchor card (crossed SAFE, GATE T §8.3) to the video glyph; B07 checks
moved under each tile (tile 10's check crossed SAFE's right edge).

Environment notes
- `PYTHONUTF8=1` is required on Windows; review cuts use `ART_NO_DRAWTEXT=1`.

Gate results (final exports)
- 16:9 renders/one-piece-of-content-into-ten.mp4 — 3840×2160, 145.7 s; GATE L/V/T pass; receipt one-piece-of-content-into-ten.verified.json
- 9:16 renders/one-piece-of-content-into-ten-vertical.mp4 — 2160×3840, 145.7 s; GATE L/V/T pass; receipt one-piece-of-content-into-ten-vertical.verified.json
