# BUILD LOG — hai-simple/behind-the-model--claude-liam-correlated-failure-research

Redo of `anthropics/youtube/behind-the-model/claude-liam-correlated-failure-research`
("Correlated Failure in AI Auditing — Consensus Is Not Verification", Teardown-register
CLI 10-beat spine, `register: "Teardown"`, `voice: "am_onyx"` already) as `hai-simple`
(Plain register, Humanitarians AI skin). Source folder untouched. Built from scratch —
the target reel dir contained only SUBJECT.json at the start of this invocation.

## What changed vs. source (per redo contract)

- **Register:** Teardown (CLI-explainer PROBLEM/ASK/CODE/OUTPUT/CHANGE/OUTPUT/SUMMARY/
  NEXT-STEPS spine, terminal-ask beats) → Plain (hai-simple's writer-open + one-idea-per-
  beat body + carry-out + your-turn + outro spine). Body recompressed from the source's
  10-beat CLI structure into 8 body beats (B01–B08) carrying the same facts and argument.
- **Cold open:** source's `NikBearBrownOpen` title card → `BrutalistHesitantWriter`.
  Writer types "Three AI judges agree. That means it's verified, right?", hesitates on
  "verified", corrects to "consensus" — the reel's actual wrong guess (agreement among AI
  judges is mistaken for verification), picked up in B02 and falsified by B03's order-swap
  demo.
- **Close:** `OutroCTA` + `@HumanitariansAI`, Liam sign-off, instead of source's
  `NikBearBrownOutro`/`ClaudeTitleOutro` (the source sheet had both, inconsistently).
- **Voice:** unchanged — Liam, Kokoro `am_onyx` (the source already used `am_onyx`).
- **Facts/argument kept:** the ensemble-theory independence requirement; the three
  documented LLM-as-judge biases (positional, verbosity, self-enhancement); the
  positional-bias order-swap demo (source's B05/B06 terminal beats) — promoted to the
  reel's anchor, planted at B03 and paid off at B08; the audit-pairing fix (retrieval /
  code execution / validator, in place of an LLM-on-LLM check); the summary claim that
  more AI agreement is more shared consensus, not more verification. The source's
  Bishop-textbook citation for the ensemble-theory result was dropped from the narration
  (kept as the underlying fact — cross-checking requires independent failure modes — but
  stated generically rather than by section number, appropriate for a general-audience
  Plain-register explainer; QUESTION.md documents this).
- **New content this redo added, not present in source:** ONE-FLAG LAW required a single
  inference flag somewhere in the reel; the source made no such caveat, so B07 adds one —
  a check only counts as independent if it doesn't itself quietly run on the same kind of
  model underneath (a search index or validator built by an AI can reintroduce the exact
  blind spot it was meant to catch). BOTH-DIRECTIONS LAW required stating what a negative
  result (disagreement) does not prove either; B08 adds this (disagreement between
  correlated judges doesn't confirm either verdict).

## NO-GENAI / NO-PANTRY LAW

No source beat kept in this build was AI-VIDEO, pantry, or a human-drop slot (the
source's B00 was already `NikBearBrownOpen`/REMOTION, and its ASK/CHANGE beats were
`NikBearBrownTerminalAsk`/REMOTION — no puppet, no generated video anywhere in the
source). Every beat in this reel is REMOTION (B00, BCRY, BHTF, BOUT) or bespoke
GRAPHIC/Manim (B01–B08), built fresh in the humanitarians palette
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`).

## Two real defects found and fixed during Gate V (not just re-run)

1. **B03's "picks A" / "picks B" captions rendered with a visible inserted gap** ("pi cks
   A" / "pi cks B") on first Manim render, caught via frame pull at the beat's mid-clip
   timestamp. This is the Pango/Montserrat glyph-shaping defect class documented in the
   `claude-constitution-honesty-standard` precedent's BUILD-LOG (there it was a space
   *collapse*; here the same underlying "pi" letter-pair shaping fragility produces an
   inserted gap instead) — `weight=BOLD` was already set and did not clear it. Root-caused
   by rewording rather than fighting the font: renamed the captions "WINNER: A" / "WINNER:
   B" (same meaning, avoids the "pi"-initial word), re-rendered, reverified via frame pull
   — no gap, clean kerning.
2. **B06's "MODEL BLIND SPOTS" dashed-circle label visually collided with the MATH RESULT
   pill** (text printing directly over the pill's border) on first Manim render, caught via
   frame pull. The decorative dashed-circle overlay was cut entirely — the three-row
   pairing table plus the footer line convey the same point without the layout collision.
   Re-rendered and reverified via frame pull — no overlap, clean margins.

Also cleared during the same Gate V / Gate T pass, all via direct fixes (not exemptions):
B01/B04/B06's sub-captions bumped from font_size 16–18 to 20–24 (four beats had a
min-size §8.1 FAIL, smallest measured 8–16px against the 20px floor); B01's checkmark
enlarged; B07's cramped "built by\nan AI" label (squeezed inside a radius-0.4 circle,
also a min-size FAIL) moved outside and below the circle as a single normal-size line.

## GATE T (pixel type-check) — 6 FAILs → 0

First run: 6 beats FAILed (B01/B04/B06/B07 min-size; B03/B05 kerning; B01/B04 bbox-
overlap). After the font-size/layout fixes above, min-size cleared to 0 and bbox-overlap
dropped to 3 (B04, B06, B07) with kerning still failing on 2 (B03, B05) — all five
verified by direct frame pull to be the same documented false-positive classes already
established in `type_check.py`:

- **B04/B06/B07 bbox-overlap:** the flagged blob in every case is a RoundedRectangle
  pill/card's own border ring enclosing its own centered interior label (STYLE pill;
  FACTUAL CLAIM pill; the VALIDATOR card's two stacked lines) — the identical
  label-inside-a-card pattern documented for `B02_FiveProperties`/`B03_HookMechanism`/
  `NWLB01Scene`/`NWLB04Scene` and ~15 other precedents. Verified by frame pull: every
  label sits cleanly inside its own box with visible margin, no real text-on-text overlap.
- **B03/B05 kerning:** multi-element compound peak bands (order-swap panel: answer cards +
  TERRA ring + "WINNER: A/B" caption at a shared y-band; Venn overlap: two-line "SHARED
  TRAINING, SHARED BLIND SPOTS" caption + arrow + "their agreement lives here" label at a
  nearby y-band) — the same false-positive mechanism documented for `S07Scene`/`S08Scene`/
  `NWLB02Scene`/`NWLB06Scene`/`TPB02Scene`. Font is named (`SANS='Montserrat'`) throughout;
  structural Pango check passed. Verified by frame pull at t=dur*0.6 for both beats: all
  text renders correctly kerned, fully legible, no gap or overlap defect.

Added `CFB04Scene`/`CFB06Scene`/`CFB07Scene` to `BBOX_OVERLAP_EXEMPT_PATTERNS` and
`CFB03Scene`/`CFB05Scene` to `KERNING_EXEMPT_PATTERNS` in `runtime/scripts/type_check.py`,
each with a comment documenting the verification, per house convention. GATE T: PASS on
the re-run.

## Gates

- **TIMING LAW (B00):** narration 32 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **12.80s** (≥9s floor, ≥8s render floor, comfortable margin). The
  correction ("verified" → "consensus") verified fully typed and settled by end-of-clip
  via frame grab at t=11s.
- **GATE AUDIO:** PASS, mean_volume **-23.8 dB** (well above the -40 dB floor), max_volume
  -2.9 dB.
- **Gate V (frame QC):** every GRAPHIC beat (B01–B08) checked at mid-beat timestamps
  before and after fixes; two real defects found and fixed at the root (B03 ligature
  reword, B06 layout collision, both detailed above). Full-cut 4-second-spaced frame
  sweep (43 frames, contact-sheeted) across the whole 172.9s master, plus direct review
  of the four Remotion beats (B00, BCRY, BHTF, BOUT) — all legible, safe inset, no text
  overlap, Humanitarians AI skin correct throughout (composer card, subscribe chip, outro
  title all read cleanly).
- **GATE T (pixel type-check):** FAIL (6 beats) → FAIL (5 beats, after font/layout fixes)
  → PASS (after root-causing/exempting the remaining false positives per the defect log
  above).
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output (12/12
  beats, no violations).
- **Motion histogram:** WARNING, graphic 8/12 (66%, over the ~40% pantry cap).
  Non-blocking and structural for this skill: B00 (writer), BCRY, BHTF, BOUT are REMOTION
  by the hai-simple spine itself, and at 8 body beats this 12-beat reel necessarily runs
  higher than 40% on the graphic side. Same disposition as the honesty-standard and
  corrigibility-dial precedents' identical histogram warning.

## Output

`behind-the-model--claude-liam-correlated-failure-research.mp4` — 172.9s, 3840×2160,
12/12 beats real (no slate), audible narration throughout (mean -23.8 dB). This is the
review cut (COMPLETION LAW satisfied: newer than `beat_sheet.json`, mean_volume verified
via ffprobe/compile GATE AUDIO). `compile.py` forces a 4K master by default ("4K LAW"),
so no separate low-res pass exists for this cut.

## Delivery

Master born natively 3840x2160 via `compile.py`'s 4K LAW, copied directly to `-4k.mp4`
(no separate 4K re-render needed). Delivered via `deliver.py --push`: staged
`DELIVERY/behind-the-model--claude-liam-correlated-failure-research/` (4K mp4 +
description) for the Drive sync, and committed the text artifacts (README.md,
beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md, CARRY-OUT.md, QUESTION.md — no
mp3/mp4) to
`humanitarians-youtube/claude-bear/behind-the-model--claude-liam-correlated-failure-research/`.
Playlist: **Behind the Model** (direct family-prefix match in `playlists.json`).
