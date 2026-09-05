# BUILD LOG — hai-simple/behind-the-model--claude-constitution-many-hands

Redo of `anthropics/youtube/behind-the-model/claude-constitution-many-hands`
("One of the Many Hands", Teardown-register, 16 beats, ~360s) as `hai-simple`
(Plain register, Humanitarians AI skin). Source folder untouched. Built from
scratch — the target reel dir contained only SUBJECT.json at the start of
this invocation.

## Source was thinner than the corrigibility-dial precedent

Unlike the sibling redo (`behind-the-model--claude-constitution-corrigibility-dial`),
this source's body beats (A10–A51) were never fleshed out — each is a `[seed]
... expand from the source with a concrete instance` placeholder, not written
narration. The load-bearing facts actually came from the source's fully-written
beats (B00, B01, EX, VERDICT) and `metadata.one_idea`, which together name the
argument precisely enough to build from: the many-hands check, and a
three-part legitimacy test (process, accountability, transparency). No
external source doc was found under `anthropics/claude-constitution/` matching
the referenced `20260120-constitution.md` path. Documented in QUESTION.md.

## What changed vs. source (per redo contract)

- **Register:** Teardown → Plain. Body compressed to one idea per beat (10
  beats: B00 writer + B01–B06 body + BCRY + BHTF + BOUT).
- **Cold open:** source's `ClaudeComposerAsk` direct-address ask →
  `BrutalistHesitantWriter`. Writer types "Isn't Claude's safety just about
  refusing malware?", hesitates on "malware", corrects to "requests that only
  look legitimate" — the reel's actual wrong guess, picked up and falsified by
  B03.
- **Close:** `OutroCTA` + `@HumanitariansAI`, Liam sign-off, instead of
  source's `ClaudeTitleOutro`/`@NikBearBrown`.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Facts/argument:** the many-hands setup, the legitimacy triage mechanism,
  and the election-vs-startup worked example all carry from the source,
  reworded for register. **Not carried:** the source's second thread
  (epistemic autonomy / homogenized belief, acts A40–A51) — a real but
  different constitutional concern from the one this source's own
  `metadata.one_idea` names; folding it in would fracture the one-anchor law.
  See QUESTION.md and SCRIPT.md "Deliberately not claimed."

## NO-GENAI / NO-PANTRY LAW

No source beat kept in this compression was AI-VIDEO, pantry, or a human-drop
slot. GATE L (`./art scenes "hands in a chain, one refusing"`) returned no
usable template — the eight candidates were all from an unrelated series
(`InYourHandsDeck` etc.) — so the body beats are bespoke Manim
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`, matching the humanitarians palette
set by the corrigibility-dial redo). Every beat in this reel is REMOTION (B00,
BCRY, BHTF, BOUT — all GATE-L-checked renderable: `BrutalistHesitantWriter`,
`WantQuote`, `ClaudeComposerAsk`, `OutroCTA`) or bespoke GRAPHIC/Manim
(B01–B06).

## Three real defects found and fixed during Gate V (not just re-run)

1. **B00's trigger-word correction never fired.** First draft's
   `triggerWords: "obviously bad requests"` (a 3-word phrase) never matched
   anything, because `BrutalistHesitantWriter.tsx`'s `buildActs()` splits text
   into whitespace-delimited word tokens and matches each token's core against
   the trigger list (`triggers.indexOf(core.toLowerCase())`) — a multi-word
   phrase can never equal a single token. Confirmed via frame grabs at 6.85s,
   12.33s (compiled timeline) and 10s/15s/17s (raw clip) — all showed the
   uncorrected text with no hesitation ever occurring. Root-caused by reading
   the component source (`runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx`
   lines 118–144), confirmed against the working corrigibility-dial precedent
   (single-word trigger `"judgment"`). Fixed by rewriting B00's text to end on
   the single word "malware" (`triggerWords: "malware"`), replaced by the
   phrase "requests that only look legitimate" — narration rewritten to match.
   Re-generated B00 audio (`--only B00`, 13.25s), re-rendered B00
   (`remotion_scenes.py --only B00`, extended to 13.2s), reverified via frame
   grabs at 5s/8s/12.5s — correction now visible and settled well before the
   clip ends.
2. **B05/B06 gate cards — FAIL/PASS stamp overlapping the placeholder "?".**
   `_gate()` draws a permanent "?" glyph; `gate_result()` in both scenes moved
   a new "FAIL"/"PASS" `Text` to the same position without hiding the "?",
   producing garbled overlapping glyphs ("FA?IL", "PA?SS") — caught via frame
   grabs at both mid- and near-end timestamps for both beats. Fixed by adding
   `g[2].set_opacity(0)` before placing the stamp text in both `gate_result()`
   closures. Re-rendered B05 and B06, reverified — clean single-word stamps.
3. **B06 "AUTOMATED SYSTEM" text overflowed its circle, and the title/circle
   and stamp/footer pairs collided.** The circle (radius 0.6) was too small
   for its two-line label at font_size 14, and after widening it to fix that,
   the top of the circle overlapped "THE STARTUP" title, and the bottom
   "CLAUDE HELPS" stamp crowded the footer against the frame's bottom safe
   inset (`DOWN * 3.85` in an 8-unit-tall frame left only ~1.9% margin from
   the edge). Fixed by increasing circle radius to 0.75 with a smaller label
   font (13), and re-deriving every vertical position in the beat (title,
   circle, request card, stamp, footer) with explicit margin checks against
   neighbors and the frame edge. Re-rendered, reverified via frame grabs at
   104.5s and 112.9s — no overlap, footer clears the bottom edge by ~5%.

All three fixes were applied and reverified with frame grabs
(`ffmpeg -ss <t> -frames:v 1`) at both a mid-beat and near-end timestamp
before recompiling, not assumed from a duration match alone.

## A note on the compile process itself (not a content defect)

The first `remotion_scenes.py` invocation was launched with the harness's
2-minute default timeout and was killed mid-run (exit 143) after completing
only B00. A second invocation (explicit 600000ms timeout) rendered BCRY
successfully, then threw an unhandled `FileNotFoundError` inside
`extend_clip_to_duration()`'s `shutil.move` for BHTF. Despite the traceback,
all four Remotion media files (B00, BCRY, BHTF, BOUT) were found on disk
afterward with correct durations, decoded cleanly under
`ffmpeg -v error -i <f> -f null -` (no corruption), and a `ps`/`lsof` sweep
confirmed no orphaned node/chrome-headless-shell process remained tied to
this reel's working directory. Treated as a transient filesystem hiccup in
the harness's render helper, not a defect in this reel's content — logged
here per the "no post-compile sheet edit, verify then continue" rule rather
than re-running the whole pipeline speculatively.

## Gates

- **TIMING LAW (B00):** narration 33 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **13.25s** (≥9s floor, ≥8s render floor). Correction
  ("malware" → "requests that only look legitimate") verified fully typed and
  settled well before end-of-clip via frame grabs.
- **GATE AUDIO:** PASS, mean_volume **-23.9 dB** (well above the -40 dB
  floor), max_volume -2.9 dB.
- **Gate V (frame QC):** every beat checked at a mid-beat and near-end
  timestamp (26 frames total across two review passes); three real defects
  found and fixed at the root (detailed above). B01–B04, BCRY, BHTF, BOUT
  clean on first review.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py`
  output (10/10 beats, no violations).
- **Motion histogram:** WARNING, graphic 6/10 (60%, over the ~40% pantry
  cap). Non-blocking and structural for this skill: B00 (writer), BCRY, BHTF,
  BOUT are REMOTION by the hai-simple spine itself, and at only 6 body beats
  this 10-beat reel necessarily runs higher than 40% on the graphic side.
  Same disposition as the corrigibility-dial redo's histogram warning.

## Output

`behind-the-model--claude-constitution-many-hands.mp4` — 152.6s, 3840×2160,
10/10 beats real (no slate), audible narration throughout (mean -23.9 dB).
This is the review cut (COMPLETION LAW satisfied: newer than
`beat_sheet.json`, mean_volume verified via ffprobe/compile GATE AUDIO).
`compile.py` forces a 4K master by default ("4K LAW"), so no separate low-res
pass exists for this cut.
