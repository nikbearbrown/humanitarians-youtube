# BUILD LOG — hai-simple/behind-the-model--claude-liam-verification-matrix

Redo of `anthropics/youtube/behind-the-model/claude-liam-verification-matrix`
("Verification Matrix: Match the Check to the Output", Teardown-register 5-beat
CLI-audience spine, `register: "Teardown"`, `voice: "am_onyx"` already) as
`hai-simple` (Plain register, Humanitarians AI skin). Source folder untouched.
Built from scratch — the target reel dir contained only SUBJECT.json at the
start of this invocation.

## What changed vs. source (per redo contract)

- **Register:** Teardown (fluency-is-not-signal / edit-vs-audit / risk-tiered-gate /
  VERDICT spine) → Plain (hai-simple's writer-open + one-idea-per-beat body +
  carry-out + your-turn + outro spine). Source's four content beats (fluency ≠
  accuracy signal, edit vs. audit, risk-tiered gate, the one-sentence verdict)
  recompressed and expanded into 8 body beats (B01–B08) carrying the same facts
  and argument.
- **Cold open:** source's `ClaudeComposerAsk` cold open (paper-summarization-agent
  ask) → `BrutalistHesitantWriter`. Writer types "If Claude's output reads clean,
  I've verified it — right?", hesitates on "verified", corrects to "edited" — the
  reel's actual wrong guess (proofreading for clarity is mistaken for verifying
  accuracy), picked up in B02 and falsified by B03's fabricated-citation case.
- **Close:** `OutroCTA` + `@HumanitariansAI`, Liam sign-off, instead of source's
  `ClaudeTitleOutro`/`@NikBearBrown` skin.
- **Voice:** unchanged — Liam, Kokoro `am_onyx` (the source already used `am_onyx`).
- **Facts/argument kept:** fluency is a training habit, not an accuracy signal —
  a fabricated citation reads with the same confidence as a real one; editing asks
  "is this clear" while auditing asks "is this true, traceable, supported by the
  source"; the matrix's per-output-type rules (citation → open the source, number →
  recompute + check the denominator, claim → trace to one sentence); the
  risk-tiered gate (light / moderate / strict) matching depth to consequence, with
  a client-facing email landing at strict because the downstream consequence is
  the delegator's; the one-sentence verdict — no verification path, no delegation.
- **New content this redo added, not present in source:** ANCHOR LAW required one
  running example planted early and paid off late — the source had no single
  recurring visual across its four beats, so this redo invents the fabricated-
  citation card (real journal, right year, plausible title, not one typo) as the
  anchor, planted at B03 and paid off at B08 run back through the matrix and
  logged. WRONG-GUESS LAW required the guess to be stated and then falsified by a
  concrete case — the source states "editing ≠ auditing" as a flat claim; this
  redo turns it into a falsifiable guess (a clean read-through feels like enough)
  broken by the fabricated-citation case. ONE-FLAG LAW required a single inference
  flag — the source made no such caveat, so B07 adds one: the matrix assumes the
  primary source is reachable; when it isn't (paywalled, private data), the honest
  move is downgrading confidence, not skipping the check. BOTH-DIRECTIONS LAW
  required stating what a positive result (all checks passed) does and does not
  prove, and what a negative result (one failed check) does not prove — B08 adds
  both directions, which the source's four-beat spine did not separate.
- **Dropped:** none of the source's substantive content — the source was already
  compact (4 content beats); this redo expands rather than cuts.

## Six-move audit (Plain register, `simple`/`hai-simple` Step 2)

| Move | Beat |
|---|---|
| 1 stakes | B01 |
| 2 wrong guess (+ falsified by a case) | B02 states it; B03 falsifies it |
| 3 mechanism | B04, B05, B06, B08 (one-flag at B07) |
| 4 anchor (planted / paid off) | B03 → B08 |
| 5 both directions | B08 |
| 6 carry-out | BCRY |

## Build

- **Audio first:** `generate_audio_kokoro.py` — 12/12 beats generated, $0.00, measured
  durations written back into `beat_sheet.json` (ground truth). B00 measured 9.17s
  (TIMING LAW: ≥8s render floor met, narration 28 words + `lead_silence_s` 0.8).
- **GRAPHIC beats (B01–B08):** authored as Manim scenes (`scenes.py`, classes
  `VMB01Scene`–`VMB08Scene`), Humanitarians palette (`#F3EBDD`/`#2F2A26`/`#E4572E`/
  `#1F4E5F`), rendered via `render_scenes.py` against the measured `actual_duration_s`
  for each beat. All 8 rendered clean on first pass.
- **REMOTION beats (B00, BCRY, BHTF, BOUT):** rendered via `remotion_scenes.py`
  (foreground; the tool's automatic 120s backgrounding kicked in twice for the
  longer batch runs — each time the invoking process was polled to completion in
  the foreground of this session before any further step, so no render was ever
  left orphaned or unsupervised). B00 verified: `media/B00.mp4` = 9.2s (≥8s floor),
  late-frame pull at t=8.5s confirms the correction ("verified" → "edited") fully
  typed and settled on screen.
- **Compile:** `compile.py` → 12/12 beats real (no slate), 4K LAW forced the master to
  3840×2160 natively, 148.6s. `GATE AUDIO: PASS` mean_volume **-24.0 dB** (well above
  the -40 dB floor), max_volume -2.9 dB.

## Gate T (pixel type-check) — fixes and exemptions

First pass: **FAIL (5 beats)**.
- **B01** — bbox-overlap: the CITATION/CLAIM/NUMBER pills' RoundedRectangle border
  (closed-ring blob) enclosed its own centered label text-run — the same
  box+interior-label false-positive class as `RVB01Scene`/`B02_FiveProperties`
  precedent. Verified by frame pull: all three pills read cleanly, labels centered,
  no real text-on-text overlap. Added `VMB01Scene` to `BBOX_OVERLAP_EXEMPT_PATTERNS`.
- **B03** — kerning: the "SOURCE: NOT FOUND" reveal card's colon-plus-space
  punctuation narrowed the inter-glyph gap analyser's expected advance — identical
  text and identical false-positive class as `RVB03Scene` precedent. Verified by
  frame pull: renders as one continuous, legible run, no glyph defect. Added
  `VMB03Scene` to `KERNING_EXEMPT_PATTERNS`.
- **B06** — real defects, fixed in `scenes.py`: (1) min-size — the LIGHT/MODERATE/
  STRICT tier-pill font sizes (16/17/18) sat under the 20px floor; bumped all three
  to font_size=20 and widened the pills to fit. (2) bbox-overlap — the "client
  email" card's docking animation moved it to `strict.get_center()`, landing
  directly on top of the STRICT pill's own label text (confirmed by frame pull —
  visibly garbled overlapping text). Root-caused and fixed: the client card now
  docks beside the STRICT pill (`next_to(strict, RIGHT)`) instead of on top of it.
  Verified by frame pull: STRICT label reads cleanly, client-email card sits
  beside it with clear separation.
- **B07** — min-size: a literal `Line()` strikethrough drawn across the "VERIFIED"
  text bisected the glyphs into two horizontal bands, each registering as a
  separate sub-floor text-run (~10px) to the blob detector — a real rendering
  defect, not just a false positive (the strike-through-through-glyphs technique
  is fragile under pixel analysis). Root-caused and redesigned: replaced the
  literal strikethrough with a small drawn X-mark beside the VERIFIED pill,
  followed by `Transform(verified, unconfirmed)` morphing the whole pill —
  no text is ever bisected. Verified by frame pull: both states read cleanly,
  transform reads as a clear downgrade, not a mid-glyph cut.
- **B08** — real defects, fixed in `scenes.py`: (1) min-size — `card_lbl` ("THE
  ANCHOR RETURNS") and `log_lines` sat at font_size=15, under the 20px floor;
  bumped both to font_size=20, widened `log_box` to fit. (2) contrast — the
  "SOURCE: NOT FOUND" log line in TERRA (`#E4572E`) on cream measured 2.74:1,
  under the 4.5:1 WCAG floor for body-sized text (unlike the same string inside a
  TERRA-bordered card at B03, where the border already carries the accent
  moment); switched the log-line text to INK per the checker's own suggested fix,
  keeping the TERRA accent on the card border only.

Re-run after fixes: **GATE T: PASS** (0 FAILs across all 9 checks, 12 beats).

## Frame QC catch: leaked component placeholder ("Fable 5")

After Gate T passed, a full-cut frame sweep (contact-sheeted, ~6s spacing, 25
frames across the 148.6s master) surfaced a real defect Gate T's pixel checks
don't catch: the BHTF `ClaudeComposerAsk` beat omitted the `modelLabel` prop,
so it silently fell back to the component's demo default, **"Fable 5"** — an
internal placeholder name, not a Claude model, and not something that should
ever appear in a published-style Claude explainer. Cross-checked against other
built `hai-simple` reels in this same directory (`financial-services--*`,
`knowledge-work-plugins--*`): all of them explicitly set
`modelLabel: "Opus 4.8"`. Fixed by adding that same value to BHTF's props,
re-rendered BHTF only via `remotion_scenes.py --only BHTF --force`, and
recompiled. Verified by frame pull: composer card now reads "Opus 4.8", not
"Fable 5". (Flagging for the source `simple`/`hai-simple` chassis: the
`risk-tiered-verification` sibling reel built earlier in this run has the same
un-set `modelLabel` and likely carries the same leaked default — worth a
follow-up pass across the `behind-the-model--*` batch.)

## Gate V (frame QC)

Full-cut sweep at 6-second spacing (25 frames, contact-sheeted) across the whole
148.6s master, covering every beat at least once: all beats legible, safe inset, no
text overlap, Humanitarians AI skin correct throughout (composer card — now
correctly reading "Opus 4.8" — subscribe chip, outro title all read cleanly),
consistent palette across all 8 Manim beats and all 4 Remotion beats.

- **Motion histogram:** WARNING, graphic 8/12 (66%, over the ~40% pantry cap).
  Non-blocking and structural for this skill: B00 (writer), BCRY, BHTF, BOUT are
  REMOTION by the hai-simple spine itself, and at 8 body beats this 12-beat reel
  necessarily runs higher than 40% on the graphic side. Same disposition as prior
  `behind-the-model--*` hai-simple redos' identical histogram warning.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output
  (12/12 beats, no violations).

## Output

`behind-the-model--claude-liam-verification-matrix.mp4` — 148.6s, 3840×2160,
12/12 beats real (no slate), audible narration throughout (mean -24.0 dB). This is
the review cut (COMPLETION LAW satisfied: newer than `beat_sheet.json`, mean_volume
verified via ffprobe volumedetect). `compile.py` forces a 4K master by default
("4K LAW"), so no separate low-res pass exists for this cut.

## Delivery

Master born natively 3840x2160 via `compile.py`'s 4K LAW, copied directly to `-4k.mp4`
(no separate 4K re-render needed). Delivered via `deliver.py --push`: staged
`DELIVERY/behind-the-model--claude-liam-verification-matrix/` (4K mp4 +
description) for the Drive sync, and committed the text artifacts (README.md,
beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md, CARRY-OUT.md — no
mp3/mp4) to
`humanitarians-youtube/claude-bear/behind-the-model--claude-liam-verification-matrix/`.
Playlist: **Behind the Model** (direct family-prefix match in `playlists.json`).
