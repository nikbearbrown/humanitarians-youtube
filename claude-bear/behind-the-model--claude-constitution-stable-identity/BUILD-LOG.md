# BUILD LOG — hai-simple/behind-the-model--claude-constitution-stable-identity

Redo of `anthropics/youtube/behind-the-model/claude-constitution-stable-identity`
("Identity as Infrastructure", Teardown-register, 16 beats, ~360s) as
`hai-simple` (Plain register, Humanitarians AI skin). Source folder untouched.
Built from scratch — the target reel dir contained only SUBJECT.json at the
start of this invocation.

## Source was thinner than the corrigibility-dial/many-hands precedent

Same situation as the sibling redos (`behind-the-model--claude-constitution-
corrigibility-dial`, `behind-the-model--claude-constitution-many-hands`): the
source sheet's body beats (A10–A51) were never fleshed out — each is a
`[seed] … expand from the source with a concrete instance` placeholder, not
written narration. The load-bearing facts came from the source's fully-written
beats (B00, B01, EX, VERDICT) and `metadata.one_idea`, which name the argument
precisely: the network can compute many characters, so training stabilizes
one; a self anchored in its own values resists destabilization the way firm
boundaries resist manipulation. No external source doc was found under
`anthropics/claude-constitution/` matching the referenced
`20260120-constitution.md` path — same absence noted in both prior redos.
Documented in QUESTION.md.

## What changed vs. source (per redo contract)

- **Register:** Teardown → Plain. Body compressed to one idea per beat (10
  beats: B00 writer + B01–B06 body + BCRY + BHTF + BOUT), following the
  many-hands precedent's compression ratio rather than the source's 16 seeded
  slots.
- **Cold open:** source's `ClaudeComposerAsk` direct-address ask →
  `BrutalistHesitantWriter`. Writer types "Claude's identity is just
  personality. Right?", hesitates on "personality", corrects to
  "infrastructure" — the reel's actual wrong guess, picked up and falsified
  by B03.
- **Close:** `OutroCTA` + `@HumanitariansAI`, Liam sign-off, instead of
  source's `ClaudeTitleOutro`/`@NikBearBrown`.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Facts/argument:** the five-turn "real self" pressure case (source B01,
  kept as the anchor), the many-characters/one-self mechanism and the
  manipulation-resistance mechanism (source A20/A21, A30/A31 — together
  `metadata.one_idea`), the existential-frontier honest uncertainty (source
  A10/A11, A40/A41), the trellis-not-cage framing (source A50/A51), and the
  worked example (source `EX`) all carry forward, reworded for register and
  merged into six body beats rather than told as ten separate seeded acts.
  The source's B01 key case and `EX` worked example are the same scenario in
  substance, so this redo splits them across the anchor's plant (B01) and
  payoff (B06) rather than narrating the full case twice.
- **The carry-out (source `VERDICT`) is kept near-verbatim** — it states
  mechanism and analogy, not a design judgment, so nothing needed removing
  for the Plain register.

## NO-GENAI / NO-PANTRY LAW

No source beat kept in this compression was AI-VIDEO, pantry, or a human-drop
slot. GATE L (`./art scenes --check` on `BrutalistHesitantWriter`, `WantQuote`,
`ClaudeComposerAsk`, `OutroCTA`) confirmed all four Remotion patterns
renderable before slating. The six body beats (B01–B06) are bespoke Manim
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`, the humanitarians palette set by the
corrigibility-dial redo and reused by many-hands).

## Three real defects found and fixed during Gate V (not just re-run)

1. **B06's "unanchored — would have conceded here" ghost label ran directly
   through the SELF glyph box.** `ghost_lbl.next_to(ghost, DOWN, buff=0.1)`
   positioned the label under the dashed line's full bounding box (which
   spans from the turn-3 marker to the line's end point), centering it over
   a region that overlapped the fixed SELF glyph. Caught via frame grab at
   t=92s (compiled timeline). Fixed by anchoring the label to
   `ghost.get_end()` instead of the line's bbox, and moving the SELF glyph
   left/down so the ghost path's endpoint clears it entirely. Re-rendered
   B06, reverified at t=87s and t=92s — clean, no overlap.
2. **B02's rotating "TONE" needle swept through the dial's own label.** The
   pressure-arrow animation rotated the needle with
   `about_point=dial.get_center()` instead of the needle's own pivot — since
   `Arc.get_center()` for a semicircle returns a point offset from the true
   circle center, this dragged the needle's base across the frame instead of
   pivoting cleanly, ending with the needle line crossing the "TONE" text
   below. Caught via frame grab at t=3s (raw beat clip) showing the needle
   struck through the label. Fixed by defining an explicit `pivot` point,
   rotating the needle about that fixed point only, moving the label well
   below the needle's (now bounded) sweep range, and reducing the total
   rotation so the needle stays within the gauge's upper arc. Re-rendered
   B02, reverified — needle stays clear of the label at every sampled frame.
3. **GATE T (type_check.py) FAIL on B02 and B03 — systematic kerning gaps in
   Montserrat-rendered text (11.4× and 9.2× expected inter-glyph advance).**
   Not a layout defect — Pango/Montserrat fallback at these specific string
   and size combinations, per type_check.py's own diagnostic ("Pango fallback
   causes SYSTEMATIC gaps ... ≥30% of inter-run gaps exceed the threshold").
   Fixed per the checker's own suggested remediation: switched every
   `Text()` call inside `SIB02Scene` and `SIB03Scene` from `font=SANS`
   (Montserrat) to `font=SERIF` (EB Garamond) — the two beats already
   flagged, leaving the four passing beats (B01, B04, B05, B06, which use the
   same Montserrat font at similar sizes without tripping the check)
   untouched to avoid risking their already-passing min-size margins.
   Re-rendered, recompiled, reran `type_check.py` — GATE T: PASS.

All three fixes were applied and reverified with frame grabs
(`ffmpeg -ss <t> -frames:v 1`) before recompiling, not assumed from a
duration match alone.

## Gates

- **TIMING LAW (B00):** narration 33 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **13.27s** (≥9s floor, ≥8s render floor). Correction
  ("personality" → "infrastructure") verified typed in terracotta at t=2.5s
  and fully settled by t=6s, well before the 13.3s clip ends.
- **GATE AUDIO:** PASS, mean_volume **-23.9 dB** (well above the -40 dB
  floor), max_volume -3.1 dB.
- **GATE T (type_check.py):** PASS after the B02/B03 font fix above.
- **Gate V (frame QC):** ten timestamps sampled across the full compiled
  master (one per beat) plus targeted re-checks after each fix; two real
  layout defects found and fixed at the root (detailed above). B00, B01,
  B04, B05, BCRY, BHTF, BOUT clean on first review.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py`
  output (10/10 beats, no violations).
- **Motion histogram:** WARNING, graphic 6/10 (60%, over the ~40% pantry
  cap). Non-blocking and structural for this skill, same disposition as
  both prior sibling redos: B00 (writer), BCRY, BHTF, BOUT are REMOTION by
  the hai-simple spine itself, and at only 6 body beats this 10-beat reel
  necessarily runs higher than 40% on the graphic side.

## Output

`behind-the-model--claude-constitution-stable-identity.mp4` — 136.9s,
3840×2160, 10/10 beats real (no slate), audible narration throughout (mean
-23.9 dB). This is the review cut (COMPLETION LAW satisfied: newer than
`beat_sheet.json`, mean_volume verified via ffprobe/compile GATE AUDIO).
`compile.py` forces a 4K master by default ("4K LAW"), so no separate low-res
pass exists for this cut.

## Delivery

Master born natively 3840x2160 via `compile.py`'s 4K LAW, copied directly to
`-4k.mp4` (no separate 4K re-render needed). Delivered via `deliver.py
--push`: staged `DELIVERY/behind-the-model--claude-constitution-stable-identity/`
(4K mp4 + description) for the Drive sync, and committed the text artifacts
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no mp3/mp4) to
`humanitarians-youtube/claude-bear/behind-the-model--claude-constitution-stable-identity/`.
Playlist: **Behind the Model** (direct family-prefix match in
`playlists.json`).
