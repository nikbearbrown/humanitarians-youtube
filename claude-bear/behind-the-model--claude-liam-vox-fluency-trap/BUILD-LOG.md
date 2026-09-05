# BUILD LOG — hai-simple/behind-the-model--claude-liam-vox-fluency-trap

Redo of `anthropics/youtube/behind-the-model/claude-liam-vox-fluency-trap`
("Why a Polished Output Is Not Evidence the Work Is Correct", Teardown-register
vox-editorial 9-beat spine, `register: "Teardown"`, `voice: "am_onyx"` already)
as `hai-simple` (Plain register, Humanitarians AI skin). Source folder
untouched. Built from scratch — the target reel dir contained only
SUBJECT.json at the start of this invocation.

## What changed vs. source (per redo contract)

- **Register:** Teardown (vox-editorial "fluency ≠ accuracy" 9-beat spine) →
  Plain (hai-simple's writer-open + one-idea-per-beat body + carry-out +
  your-turn + outro spine). Source's content beats (polished summary with
  broken citations, training objective, uncorrelated confidence, agent report
  ≠ evidence, Carlos example, verification practice, recap) recompressed and
  expanded into 8 body beats (B01–B08) carrying the same facts and argument.
- **Cold open:** source's `ClaudeComposerAsk` cold open (the question typed as
  a command) → `BrutalistHesitantWriter`. Writer types "A polished, confident
  answer from Claude means it's correct — right?", hesitates on "correct",
  corrects to "fluent" — the reel's actual wrong guess (confidence read as
  proof of correctness), picked up in B02 and falsified by B03's
  three-citation case.
- **Close:** `OutroCTA` + `@HumanitariansAI`, Liam sign-off, instead of source's
  `ClaudeTitleOutro`/`@NikBearBrown` skin.
- **Voice:** unchanged — Liam, Kokoro `am_onyx` (the source already used
  `am_onyx`).
- **Facts/argument kept:** a polished summary can carry a citation that
  doesn't exist, one that says the opposite, one from an unrelated field, and
  reading it start to finish catches none of that; training targets fluency
  (coherence), not accuracy; high-confidence prose is structurally
  uncorrelated with correctness — the true and the invented paragraph come
  from the same process; an agent's own "I checked" report is not evidence
  unless a tool actually opened the source; Carlos's policy-brief example
  (five reports, two read, three locked, one caught wrong on spot-check); the
  practice of checking at least one claim yourself; the closing line that a
  polished output is not evidence the work is correct.
- **New content this redo added, not present in source:** ANCHOR LAW required
  one running example planted early and paid off late — this redo makes the
  source's own three-citation summary (originally just a scene-setting
  example) the reel's anchor, planted at B03 (each card snapping from
  confident to broken) and paid off at B08 (the same three cards returning,
  now logged as confirmed). WRONG-GUESS LAW required the guess to be stated
  and then falsified by a concrete case — B02 states it ("polished = solid
  sourcing?"), B03 falsifies it with the three-citation case. ONE-FLAG LAW
  required a single inference flag — the source made no such caveat, so B06
  adds one: an agent's own "checked" report is only real evidence if a tool
  actually opened the file, and you can't tell which case you're in from the
  fluent prose alone. BOTH-DIRECTIONS LAW required stating what a positive
  result (checks passed) does and does not prove, and what a negative result
  (one failed check) does not prove — B08 adds both directions, which the
  source's flat recap did not separate.
- **Dropped:** none of the source's substantive content — the source's nine
  beats (including its cold open and recap) map onto this redo's twelve.

## Six-move audit (Plain register, `simple`/`hai-simple` Step 2)

| Move | Beat |
|---|---|
| 1 stakes | B01 |
| 2 wrong guess (+ falsified by a case) | B02 states it; B03 falsifies it |
| 3 mechanism | B04, B05, B07, B08 (one-flag at B06) |
| 4 anchor (planted / paid off) | B03 → B08 |
| 5 both directions | B08 |
| 6 carry-out | BCRY |

## Build

- **Audio first:** `generate_audio_kokoro.py` — 12/12 beats generated, $0.00,
  measured durations written back into `beat_sheet.json` (ground truth). B00
  measured 9.75s (TIMING LAW: ≥8s render floor met, narration 30 words +
  `lead_silence_s` 0.8).
- **GRAPHIC beats (B01–B08):** authored as Manim scenes (`scenes.py`, classes
  `FTB01Scene`–`FTB08Scene`), Humanitarians palette (`#F3EBDD`/`#2F2A26`/
  `#E4572E`/`#1F4E5F`), rendered via `render_scenes.py` against the measured
  `actual_duration_s` for each beat. All 8 rendered clean on the first pass.
- **REMOTION beats (B00, BCRY, BHTF, BOUT):** rendered via `remotion_scenes.py`
  (foreground — the tool's automatic 120s backgrounding kicked in once; the
  invoking process was polled to completion via `TaskOutput(block=true)` in
  the foreground of this session before any further step, so no render was
  ever left orphaned or unsupervised). B00 verified: `media/B00.mp4` = 9.77s
  (≥8s floor), late-frame pull at t=9s confirms the correction
  ("correct" → "fluent") fully typed and settled on screen, still mid-typing
  "right?".
- **Compile:** `compile.py` (foreground, polled via `TaskOutput(block=true)`
  after its own 120s auto-background) → 12/12 beats real (no slate), 4K LAW
  forced the master to 3840×2160 natively, 147.2s. `GATE AUDIO: PASS`
  mean_volume **-23.9 dB** (well above the -40 dB floor), max_volume -2.9 dB.

## Gate T (pixel type-check) — fixes and exemptions

First pass: **FAIL (5 beats)**.
- **B01** — bbox-overlap: the CITATION/CLAIM/NUMBER pills' RoundedRectangle
  border (closed-ring blob) enclosed its own centered label text-run — the
  same box+interior-label false-positive class as `VMB01Scene`/`B01Scene`
  precedent. Verified by frame pull: all three pills read cleanly, labels
  centered, star mark clear above each box, no real text-on-text overlap.
  Added `FTB01Scene` to `BBOX_OVERLAP_EXEMPT_PATTERNS`.
- **B03** — two issues: (1) min-size — real defect, fixed in `scenes.py`: the
  `_citation_card` helper's journal/title text sat at font_size 15–16, under
  the 20px floor; bumped both to font_size=20 and widened the card
  (3.2→3.7 units) and tightened row spacing (buff 0.5→0.35) to keep three
  cards inside the safe frame. Also bumped the "DOES NOT EXIST"/"SAYS
  OPPOSITE"/"WRONG FIELD" fail-labels from font_size=16 to 20. (2) kerning —
  false positive: the citation cards' journal/title text is wrapped in
  literal quote marks (e.g. `"Longitudinal Patterns"`), the same
  punctuation-driven false-positive class as `VMB03Scene`'s "SOURCE: NOT
  FOUND" precedent. Added `FTB03Scene` to `KERNING_EXEMPT_PATTERNS`. Verified
  by frame pull after the font-size fix: all three cards and labels render
  cleanly, no overlap, no glyph defect.
- **B04** — kerning false positive: the standalone "?" mark above the
  ACCURACY bar is a single-character `Text()` run with no adjacent glyph
  pair, which the kerning gap analyser treats as a degenerate/false gap.
  Verified by frame pull: the question mark renders as one clean glyph.
  Added `FTB04Scene` to `KERNING_EXEMPT_PATTERNS`.
- **B06** — kerning false positive: the clipboard label `"CHECKED"` is
  wrapped in literal quote marks, same punctuation-driven class as B03/
  `VMB03Scene`. Verified by frame pull: renders as one continuous, legible
  run. Added `FTB06Scene` to `KERNING_EXEMPT_PATTERNS`.
- **B08** — min-size, same real defect as B03 (shared `_citation_card`
  helper): bumped the three "CONFIRMED: …" stamp labels from font_size=14 to
  20, plus the same card-width/row-spacing fix inherited from the B03 change.
  Verified by frame pull: all three cards and stamps read cleanly, no
  overlap.

Re-run after fixes: **GATE T: PASS** (0 FAILs across all 9 checks, 12 beats).

## Gate V (frame QC)

Full-cut sweep at 6-second spacing (25 frames, contact-sheeted) across the
whole 147.2s master, covering every beat at least once: all beats legible,
safe inset, no text overlap, Humanitarians AI skin correct throughout
(composer card reads "Opus 4.8" — `modelLabel` set explicitly, no leaked
component placeholder — subscribe chip, outro title all read cleanly),
consistent palette across all 8 Manim beats and all 4 Remotion beats. The
B03/B08 anchor pair (three citation cards) is visually recognizable as the
same object in both appearances, per ANCHOR LAW.

- **Motion histogram:** WARNING, graphic 8/12 (66%, over the ~40% pantry cap).
  Non-blocking and structural for this skill: B00 (writer), BCRY, BHTF, BOUT
  are REMOTION by the hai-simple spine itself, and at 8 body beats this
  12-beat reel necessarily runs higher than 40% on the graphic side. Same
  disposition as prior `behind-the-model--*` hai-simple redos' identical
  histogram warning.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py`
  output (12/12 beats, no violations).

## Output

`behind-the-model--claude-liam-vox-fluency-trap.mp4` — 147.2s, 3840×2160,
12/12 beats real (no slate), audible narration throughout (mean -23.9 dB).
This is the review cut (COMPLETION LAW satisfied: newer than
`beat_sheet.json`, mean_volume verified via ffprobe volumedetect). `compile.py`
forces a 4K master by default ("4K LAW"), so no separate low-res pass exists
for this cut.
