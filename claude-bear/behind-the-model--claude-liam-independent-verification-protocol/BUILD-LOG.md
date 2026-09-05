# BUILD LOG — hai-simple/behind-the-model--claude-liam-independent-verification-protocol

Redo of `anthropics/youtube/behind-the-model/claude-liam-independent-verification-protocol`
("Build an Independent Verification Protocol for Agent Outputs with Claude", Teardown
register, CLI-style, 11 beats, ~99s estimated) as `hai-simple` (Plain register,
Humanitarians AI skin). Source folder untouched. Built from scratch — the target reel
dir contained only SUBJECT.json at the start of this invocation.

## Source was fully written, unlike the constitution-family redos

Unlike the sibling `behind-the-model--claude-constitution-*` redos, this source sheet's
body beats (B01–B08) were fully authored narration, not seeded placeholders — the facts
carried forward largely intact, compressed for the Plain register and the hai-simple
ten-beat shape (B00 writer + B01–B06 body + BCRY + BHTF + BOUT). Documented in
QUESTION.md.

## What changed vs. source (per redo contract)

- **Register:** Teardown → Plain. Body compressed to one idea per beat.
- **Cold open:** source's `NikBearBrownOpen` title-card ask →
  `BrutalistHesitantWriter`. Writer types "The agent says it's verified. Verified
  means true. Right?", hesitates on "true", corrects to "checkable" — the reel's
  actual wrong guess, picked up and falsified by B03.
- **Close:** `OutroCTA` + `@HumanitariansAI`, Liam sign-off, instead of source's
  `ClaudeTitleOutro`/`@NikBearBrown`.
- **Style:** source's CLI/terminal beats (`NikBearBrownTerminalAsk`, `FormBCard`) →
  bespoke Manim GRAPHIC beats per NO-GENAI/NO-PANTRY LAW — no terminal chrome, no
  code-editor simulation, drawn figures only.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Facts/argument:** the falsifying case (a citation matched against training data
  instead of the actual document, re-confirmed as "verified" by the same process,
  source B01), the four-field protocol (output type / independent evidence / key
  check / required artifact, source B02/B03), the research-task fill (source B04),
  the code-task fill (source B05/B06), and the summary lesson (source B07, kept
  near-verbatim as the carry-out) all carry forward, reworded for register. Source
  B08 (next steps) folded into the carry-out and the your-turn handoff rather than
  narrated as a separate beat.

## NO-GENAI / NO-PANTRY LAW

No source beat kept in this compression was AI-VIDEO, pantry, or a human-drop slot.
GATE L (`./art scenes --check` on `BrutalistHesitantWriter`, `WantQuote`,
`ClaudeComposerAsk`, `OutroCTA`) confirmed all four Remotion patterns renderable
before slating. The six body beats (B01–B06) are bespoke Manim
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`, the humanitarians palette).

## Real defects found and fixed during Gate V / Gate T (not just re-run)

1. **B03's self-check-loop `CurvedArrow` rendered its arrowhead directly on top of
   the "agent's own summary" text**, making it illegible. Root cause: three
   successive geometry attempts (recentering the loop onto the card, anchoring
   right→bottom, then right→left) all still produced an arrowhead landing inside
   the card's text region — the loop was fighting the same small card's interior no
   matter which two corners it was anchored between. Fixed by removing the loop
   entirely: the strike-through card plus the physically separated "THE ACTUAL
   PAPER" card already carries the beat's point (self-check is broken, independence
   comes from outside) without a decorative arrow that had no safe path to draw.
   Verified by frame grab at t=42s/48s/54s — clean, no overlap, on the second
   attempt after the removal.
2. **B01/B06's four-field protocol card labels (`OUTPUT TYPE` / `INDEPENDENT
   EVIDENCE` / `KEY CHECK` / `REQUIRED ARTIFACT`) failed GATE T min-size §8.1** —
   all four labels rendered at ~17px height against the 20px (1.9% frame-height)
   floor. Root cause: a `cards.scale(0.85)` call after `_protocol_cards()` built
   the cards at font_size 17, uniformly shrinking every label below the floor.
   Fixed by removing the group-level `.scale(0.85)` and raising the base
   font_size to 20 (with the card widened from 3.0→4.3 units to fit "INDEPENDENT
   EVIDENCE," the longest label, natively without any per-label scale-down — a
   scaled-down label can slip under the floor even when its siblings pass, which
   is why the fix targets the font size directly rather than compensating with
   scale). Re-ran GATE T after the fix: min-size §8.1 PASS across all 10 beats.
3. **GATE T bbox-overlap §8.6b FAIL on B01/B06** after the min-size fix: each
   card's own INK-colored `RoundedRectangle` border forms a closed ring whose
   bounding box necessarily encloses its interior label (design-correct —
   labels sit inside cards on purpose). This is a long-documented false-positive
   class in `type_check.py`'s own `BBOX_OVERLAP_EXEMPT_PATTERNS` list (already
   carrying ~20 prior scene classes with the identical "bordered card encloses
   its own label" pattern, e.g. `B01Scene`, `B03_HookMechanism`, `CFB07Scene`,
   each verified by frame pull). Verified by direct frame grab across every
   sampled timestamp in B01 and B06 (before and after the font/width fixes):
   every label and value sits cleanly inside its own card with visible margin
   on all sides — no real text-on-text overlap anywhere. Added `IVPB01Scene`
   and `IVPB06Scene` to the existing exemption list with the same verification
   standard as the precedents, rather than disabling or weakening the check
   itself — the check still runs and still fails on any beat not explicitly
   verified and listed.

All three fixes were applied and reverified with frame grabs
(`ffmpeg -ss <t> -frames:v 1`) before recompiling, not assumed from a duration or
compile-success signal alone.

## Gates

- **TIMING LAW (B00):** narration 33 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **11.48s** (≥9s floor, ≥8s render floor; media/B00.mp4
  measured 11.5s). Correction ("true" → "checkable") verified visible and fully
  settled at t=9s, well before the 11.5s clip ends.
- **GATE AUDIO:** PASS, mean_volume **-23.8 dB** (well above the -40 dB floor),
  max_volume -2.9 dB.
- **GATE T (type_check.py):** PASS after the min-size and bbox-overlap fixes above.
- **Gate V (frame QC):** ten timestamps sampled across the full compiled master
  (one per beat), plus targeted re-checks after each of the three fixes above;
  two real defects found and fixed (B03 loop overlap, B01/B06 label overflow/
  scale). B00, B02, B04, B05, BCRY, BHTF, BOUT clean on first review.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output
  (10/10 beats, no violations).
- **Motion histogram:** WARNING, graphic 6/10 (60%, over the ~40% pantry cap).
  Non-blocking and structural for this skill, same disposition as the sibling
  constitution redos: B00 (writer), BCRY, BHTF, BOUT are REMOTION by the
  hai-simple spine itself, and at only 6 body beats this 10-beat reel
  necessarily runs higher than 40% on the graphic side.

## Output

`behind-the-model--claude-liam-independent-verification-protocol.mp4` — 130.9s,
3840×2160, 10/10 beats real (no slate), audible narration throughout (mean -23.8 dB).
This is the review cut (COMPLETION LAW satisfied: newer than `beat_sheet.json`,
mean_volume verified via ffprobe/compile GATE AUDIO). `compile.py` forces a 4K
master by default ("4K LAW"), so no separate low-res pass exists for this cut.

## Delivery

Master born natively 3840x2160 via `compile.py`'s 4K LAW, copied directly to
`-4k.mp4` (no separate 4K re-render needed). Delivered via `deliver.py --push`:
staged `DELIVERY/behind-the-model--claude-liam-independent-verification-protocol/`
(4K mp4 + description) for the Drive sync, and committed the text artifacts
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md, CARRY-OUT.md,
QUESTION.md — no mp3/mp4) to
`humanitarians-youtube/claude-bear/behind-the-model--claude-liam-independent-verification-protocol/`.
Playlist: **Behind the Model** (direct family-prefix match in `playlists.json`).
