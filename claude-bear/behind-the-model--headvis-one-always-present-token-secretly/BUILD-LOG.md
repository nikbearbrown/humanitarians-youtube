# BUILD LOG — hai-simple/behind-the-model--headvis-one-always-present-token-secretly

Redo of `anthropics/youtube/behind-the-model/headvis-one-always-present-token-secretly`
("Why one always-present token secretly hijacks every attention statistic",
Teardown-register `ai-explainer` scaffold — B00–B05 + YOURTURN + OUTRO, all
beats `SLATE`/never rendered but fully authored narration, ~102s estimated)
as `hai-simple` (Plain register, Humanitarians AI skin). Source folder
untouched. Built from scratch — the target reel dir contained only
SUBJECT.json at the start of this invocation.

## What changed vs. source (per redo contract)

- **Register:** Teardown-flavored `ai-explainer` scaffold → Plain. Body
  compressed to one idea per beat, kept every fact.
- **Cold open:** source's stat-card `FormBCard` cold open (the layer-4/head-3
  concrete case, read cold) → `BrutalistHesitantWriter`. Writer types "Token
  zero keeps / winning the attention / max — that must be / the real signal,
  right?", hesitates on "signal", corrects to "sink" — the reel's actual
  wrong guess (winning the max by default is not the same as carrying
  meaning), picked up and falsified by B03.
- **Close:** source's recap beat + `ClaudeComposerAsk` YOURTURN + `ClaudeTitleOutro`
  → `WantQuote` carry-out → `ClaudeComposerAsk` your-turn → `OutroCTA` +
  `@HumanitariansAI`, Liam sign-off.
- **Style:** source's `FormBCard` stat-card beats (B00–B03, B05) → bespoke
  Manim GRAPHIC beats per NO-GENAI/NO-PANTRY LAW — a drawn attention heatmap
  and its mechanism, not text cards.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Facts/argument:** the concrete case (layer 4, head 3, 50,000 sequences,
  91% max-share, weight > 0.55, verb→subject dependency only visible once
  position 0 is excluded, source B00) is the reel's anchor, planted B01 and
  paid off B06. The source's question (why one position should absorb the
  plurality of mass across diverse inputs, B01) becomes the wrong-guess setup.
  The tension line (B02, "including a single structural token... makes every
  meaningful attention pattern invisible") and the mechanism (B03, "when no
  key is strongly preferred, softmax must still spend its probability
  somewhere...") carry forward near-verbatim — both already state mechanism,
  not judgment, so nothing needed removing. The worked example (B04: weights
  [0.58, 0.04, 0.12, 0.09,...], 94% raw max, 68% after exclusion) carries
  forward unchanged. Source's YOURTURN ask (what is token 0 doing — delimiter,
  start token, routing sink — and how to distinguish genuine signal from a
  parked head) carries forward as BHTF, reworded for Liam/HAI.

## NO-GENAI / NO-PANTRY LAW

No source beat kept in this compression was AI-VIDEO, pantry, or a human-drop
slot — the source's cold open and body were already Remotion `FormBCard` stat
cards. GATE L (`./art scenes --check` on `BrutalistHesitantWriter`, `WantQuote`,
`ClaudeComposerAsk`, `OutroCTA`) confirmed all four Remotion patterns
renderable before slating. The six body beats (B01–B06) are bespoke Manim
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`, the humanitarians palette).

## BOTH-DIRECTIONS LAW — added, not in the source scaffold

The source never authored a both-directions beat. B05 (direction A: a
dominant sink doesn't mean the head learned nothing — the real signal can
still be in the non-max mass) and B06 (direction B: a head that avoids
token 0 isn't automatically clean either — it may be parking on a different
low-information filler) are new content, added to satisfy the law without
contradicting any source claim.

## Real defects found and fixed during Gate T / Gate V (not just re-run)

Two independent defect classes surfaced, both traced to root cause rather
than exempted blind:

1. **A small-font Pango/EB-Garamond glyph-shaping bug.** Standalone words
   render fine, but a full sentence at font_size ≤22 intermittently opened a
   large false gap inside specific words (observed: "the real signal?" →
   "the real sig[gap]nal?", "must sum to 1" and "always present, no meaning
   — cheapest seat" losing inter-word spacing) — reproduced in isolation
   (font_test1–4.py) and confirmed it clears at font_size ≥24 regardless of
   font (EB Garamond/Montserrat) or weight. Root-caused, not patched around:
   every caption/label in scenes.py bumped to ≥22–28pt (the digit-heavy
   short labels — bar values, column names, stat lines — needed the higher
   end, since digit/x-height-only runs measure shorter ink-height than
   letter runs at the same nominal size). This is the same font-rendering
   class already logged against sibling `behind-the-model` hai-simple redos
   in `HAILOOP-LOG.md` (e.g. "pi cks A" in `claude-liam-correlated-failure-research`).
2. **A false-positive §8.4 kerning FAIL and a false-positive §8.3 contrast
   FAIL**, both traced to non-text vector geometry, not typography: B02's
   six empty-stroke `Rectangle` "icon" placeholders were misread as a
   389px-gap glyph run — replaced with filled `Dot()` markers, which read
   the same pedagogically (six sentences, converging on token 0) without
   tripping the text-run heuristic. B03's `sink_fill` TERRA probability-bar
   segment (a structural data encoding, aspect ratio ~9.2×, below the 15×
   flat-bar auto-exempt filter) was flagged as low-contrast "accent text" —
   verified by direct frame pull that all real text in the beat is INK, then
   added `HVB03Scene` to `type_check.py`'s `STRUCTURAL_TERRACOTTA_PATTERNS`,
   same documented class as the sibling `SVAB01Scene`/`SVAB04Scene`/`SVAB06Scene`
   precedent (solve-verify's ratio-ladder bars).
3. **A real visual overlap Gate V caught that GATE T did not**: after
   bumping column-label font size to clear the §8.1 floor, "BOS" and "The"
   ran together ("BOSThe") in the heatmap header — the shared column pitch
   (`CELL + GAP`) was too tight for the wider labels. Fixed at the root by
   splitting one shared `GAP` into `GAP_X` (0.32, column pitch) and `GAP_Y`
   (0.08, row pitch, unaffected) in `_heatmap_grid()` — widening only the
   axis that needed it, so the grid's height (and B06's "MASKED" label
   clearance under the title) stayed unchanged. Re-verified by direct frame
   pull on both B01 and B06 after the fix.

GATE T re-run after each batch of fixes: 6 FAILs (font-size + kerning +
contrast) → 4 → 1 → **PASS**. The column-label overlap was caught by Gate V's
frame read after GATE T had already gone green — a reminder that the
automated gate and the human-equivalent frame read catch different defect
classes.

## Gates

- **TIMING LAW (B00):** narration 28 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **9.11s** (≥9s floor, ≥8s render floor — media/B00.mp4
  measured 9.13s). Correction ("signal" → "sink") verified visible and fully
  settled at t=8.5s via direct frame pull.
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (well above the -40 dB
  floor), max_volume -2.7 dB — independently reverified with `ffmpeg
  -af volumedetect` against the final compiled master, not just compile.py's
  own report.
- **GATE T (type_check.py):** PASS after the fixes above.
- **Gate V (frame QC):** thirteen timestamps sampled across the full
  compiled master (t=3,12,20,33,47,55,65,80,95,105,115,130,145s) — legible,
  correct palette, no text overlap, safe-inset respected, `@HumanitariansAI`
  channel identity present on B00/BHTF/BOUT. One real defect (the B01/B06
  column-label overlap) caught and fixed at this stage, re-verified after.
- **Motion histogram advisory:** `graphic:6 remotion:4` — 60% GRAPHIC beats,
  over the toolkit's ~40% pantry-cap guideline (MOTION.md). Not treated as a
  blocker: matches every sibling `behind-the-model` hai-simple redo (6
  bespoke-Manim body beats is the established shape for this family), and
  GRAPHIC here means drawn figures via the standard Manim pipeline, not a
  pantry/human-drop asset — the NO-GENAI/NO-PANTRY LAW this ratio actually
  guards against is satisfied.

## Deliverable

`behind-the-model--headvis-one-always-present-token-secretly.mp4` —
3840×2160, 146.9s, all 10 beats real (no slates), mp4 mtime newer than
beat_sheet.json. `<slug>.md` YouTube metadata written per
`hai-simple`/`hai` conventions (channel @HumanitariansAI, playlist "Behind
the Model" per `playlists.json`'s `behind-the-model` → `Behind the Model`
mapping, AI disclosure, code link).
