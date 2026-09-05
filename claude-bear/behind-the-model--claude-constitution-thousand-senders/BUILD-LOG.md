# BUILD LOG — hai-simple/behind-the-model--claude-constitution-thousand-senders

Redo of `anthropics/youtube/behind-the-model/claude-constitution-thousand-senders`
("One Question, A Thousand Askers", Teardown-register, `genre: "deep-explainer"`,
16 beats, ~360s target) as `hai-simple` (Plain register, Humanitarians AI skin).
Source folder untouched. Built entirely from scratch — the target reel dir
contained only SUBJECT.json at the start of this invocation.

## Source had more real material than the corrigibility-dial/stable-identity precedent

Unlike those sibling redos, whose source body beats were pure `[seed] …`
placeholders, this source's body beats (A11/A21/A31/A41/A51) were ALSO
unfleshed seeds, but its five act TITLES (from `BUILD-PROMPT.md`'s Acts
list) are real, distinct ideas: (1) the cost-benefit ledger, (2) from
choice to policy: the 1,000 senders, (3) context that shifts the burden,
(4) instructable behaviors & the permission stack, (5) hard constraints as
filters, not weights. Combined with the source's fully-written `B00`/`B01`
(cold-open question, key case), `EX` (worked example), and
`metadata.one_idea` (carry-out), there was enough real, distinct content to
justify one more body beat than the 6-beat sibling precedent — 7 body beats
instead of 6, documented in QUESTION.md.

## What changed vs. source (per redo contract)

- **Register:** Teardown → Plain. Body compressed to one idea per beat: 11
  beats total (B00 writer + B01–B07 body + BCRY + BHTF + BOUT) vs. the
  source's 16 seeded slots.
- **Cold open:** source's `ClaudeComposerAsk` direct-address ask →
  `BrutalistHesitantWriter`. Writer types "It's a verdict on me. Right?",
  hesitates on "verdict", corrects to "policy" — the reel's actual wrong
  guess (that Claude personally judges the asker), picked up and falsified
  in B02→B03.
- **Close:** `OutroCTA` + `@HumanitariansAI`, Liam sign-off, instead of
  source's `ClaudeTitleOutro`/`@NikBearBrown`.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Facts/argument:** the household-chemicals key case (source `B01`, kept
  as the anchor), the wrong guess (Claude reads the individual asker), the
  policy-over-senders reframe (source Act 2 title), the cost-benefit-ledger
  mechanism (source Act 1 title), context/permission shifting the ledger
  (source Acts 3+4 titles, merged), the worked example with its 950/50
  numbers (source `EX`, unchanged), the hard-constraint filter (source Act
  5 title + `EX`'s bioweapon-uplift line), and the carry-out (source
  `VERDICT`, kept verbatim) all carry forward.
- **The carry-out (source `VERDICT`) is kept verbatim** — it states
  mechanism, not a design judgment, so nothing needed removing for the
  Plain register.

## NO-GENAI / NO-PANTRY LAW

No source beat kept in this compression was AI-VIDEO, pantry, or a human-drop
slot. GATE L (`./art scenes --check` on `BrutalistHesitantWriter`, `WantQuote`,
`ClaudeComposerAsk`, `OutroCTA`) confirmed all four Remotion patterns
renderable before slating. The seven body beats (B01–B07) are bespoke Manim
(humanitarians palette `#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`, this reel's
own `scenes.py`, scene class prefix `TSB0x`).

## Real defects found and fixed (Gate V and Gate T), not just re-run

Gate V (frame pulls at one per beat across the full compiled timeline, plus
targeted re-checks after each fix) caught two real legibility defects on
the FIRST compile, before any GATE T run:

1. **B02's "STATED REASON" label ran directly through the figure's body
   outline.** The magnifying-lens circle had no fill, so the silhouette
   glyph underneath showed through and its trapezoid body edge crossed the
   label text. Fixed by giving the lens a solid `fill_color=GROUND,
   fill_opacity=1` so it occludes the figure beneath it (an inspection-lens
   read), and nudging the TONE/STATED REASON labels to sit centered inside
   the now-opaque lens. Re-rendered, reverified — clean.
2. **B03's nine tiled message-copies overlapped each other with cut-off
   text.** The tiles were full-text copies of the question bubble scaled to
   ~55% then further scaled to 90% on placement (final ~2.3 units wide),
   but the grid's column spacing was only 1.7 units — narrower than the
   tiles themselves, so neighboring boxes visually overlapped and their
   sentence text was illegible/clipped. Fixed by replacing the tiled
   full-text copies with abstract placeholder "mini-doc" cards (a bordered
   box + three short line-strokes, no real text) sized and spaced to fit
   cleanly in the 3×3 grid — conveys "many identical copies" without
   requiring nine legible sentence-length text blocks. Re-rendered,
   reverified — nine clean, non-overlapping tiles.

**GATE T (type_check.py) surfaced a third, harder defect that took several
iterations to root-cause, not a font-size guess:**

3. **B07's mirrored "PERSONAL VERDICT"/"INTENT VERIFIED" strike-through
   text repeatedly failed §8.1 min-size** (readings of 15px, then 9px, then
   8px across several attempted fixes — font-size increases and diagonal
   vs. horizontal strike geometry did not resolve it). Root-caused by
   invoking `type_check.py`'s own `visible_text_mask`/`blob_bboxes`/
   `text_run_bboxes` functions directly against extracted frames (not
   guessing from the report text): an opaque terracotta strike line drawn
   literally through the letters splits each glyph's black ink into two
   thin horizontal bands (above and below the strike), and those split
   half-glyph fragments — not the strike line itself, and not the arrowhead
   tips (also tried and ruled out) — were the sub-floor blobs. No stroke
   thickness fixes this while the strike crosses through the glyph body,
   since a thicker strike only widens the cut, not the residual fragment
   height. Fixed by moving the strike to a clean underline position (a
   separate accent bar below the text with a real gap, no glyph overlap)
   instead of a literal cross-out, and separately caught and fixed a
   genuine (non-false-positive) sub-floor blob in `gate_lbl`'s lowercase
   word "not" (x-height-only glyphs at font_size 22 measured under floor)
   by setting the whole label to caps and bumping font_size to 26. Also
   fixed, same GATE T pass: B02's lens fill (already covered above, but
   also resolved a `min-size`-adjacent legibility issue), and two kerning
   FAILs (B06, B07) from Montserrat/Pango fallback at small sizes — same
   remediation as the `stable-identity` sibling's precedent: switched every
   `Text()` in the affected scenes from `font=SANS` to `font=SERIF`.
   All fixes verified by direct frame pulls and, for the min-size chase,
   by running the checker's own blob-detection code against extracted
   frames before and after each change — not assumed from a duration match.

GATE T: 3 FAILs → 2 → 1 → **PASS 0 FAILs** (final, after 4 iterations).

## Gates

- **TIMING LAW (B00):** narration 34 words + `lead_silence_s` 0.8 →
  measured `actual_duration_s` **10.54s** (≥9s floor, ≥8s render floor).
  Correction ("verdict" → "policy") verified typed in terracotta and fully
  settled by t=6s, held through clip-end at t=9s.
- **GATE AUDIO:** PASS, mean_volume **-23.9 dB** (well above the -40 dB
  floor), max_volume -2.9 dB — independently reverified via `ffmpeg
  volumedetect`, not just trusted from `compile.py`'s own report.
- **GATE T (type_check.py):** PASS after the fixes above.
- **Gate V (frame QC):** eleven timestamps sampled across the full compiled
  master (one per beat) plus targeted re-checks after each fix; two real
  layout defects found and fixed at the root (detailed above). B00, B01,
  B04, B05, B06, BCRY, BHTF, BOUT clean on first review.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py`
  output (11/11 beats, no violations).
- **Motion histogram:** WARNING, graphic 7/11 (63%, over the ~40% pantry
  cap). Non-blocking and structural for this skill, same disposition as
  the sibling redos: B00 (writer), BCRY, BHTF, BOUT are REMOTION by the
  hai-simple spine itself, and with 7 body beats (one more than the
  6-beat siblings, justified by this source's richer material) the
  graphic-side share necessarily runs higher than 40%.

## Output

`behind-the-model--claude-constitution-thousand-senders.mp4` — 146.8s,
3840×2160, 11/11 beats real (no slate), audible narration throughout (mean
-23.9 dB). This is the review cut (COMPLETION LAW satisfied: newer than
`beat_sheet.json`, mean_volume verified via ffprobe/compile GATE AUDIO).
`compile.py` forces a 4K master by default ("4K LAW"), so no separate
low-res pass exists for this cut.

## Delivery

Master born natively 3840x2160 via `compile.py`'s 4K LAW, copied directly to
`-4k.mp4` (no separate 4K re-render needed). Delivered via `deliver.py
--push`: staged
`DELIVERY/behind-the-model--claude-constitution-thousand-senders/` (4K mp4 +
description) for the Drive sync, and committed the text artifacts (README.md,
beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md, CARRY-OUT.md,
QUESTION.md — no mp3/mp4) to
`humanitarians-youtube/claude-bear/behind-the-model--claude-constitution-thousand-senders/`.
Playlist: **Behind the Model** (direct family-prefix match in
`playlists.json`).
