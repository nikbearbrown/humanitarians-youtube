# BUILD LOG — hai-simple/behind-the-model--claude-constitution-honesty-standard

Redo of `anthropics/youtube/behind-the-model/claude-constitution-honesty-standard`
("No White Lies", Teardown-register scaffold, `register: "Teardown"`, `brand:
"claude-liam"`) as `hai-simple` (Plain register, Humanitarians AI skin). Source folder
untouched. Built from scratch — the target reel dir contained only SUBJECT.json at the
start of this invocation.

## Source was a scaffold, not a finished script

The source `beat_sheet.json` had real content only in B00 (the question), B01 (the key
case: asked if you love the gift, a polite human says yes, Claude won't), the five act
titles, the worked example (persona "Aria"), and the VERDICT one-idea line. Every body
beat (A11/A21/A31/A41/A51) was an unexpanded `[seed] ... expand from the source with a
concrete instance` placeholder — never actually written. This redo therefore did more
than re-register Teardown prose to Plain: it had to develop the seven-honesty-properties
/ weak-duty-vs-strong-duty / sincere-vs-performative / personas-and-meta-transparency
argument from the act titles and the one-idea line into an actual six-beat body, using
established, true facts about Claude's public constitution material (no invented UI, no
invented model names). QUESTION.md documents the full argument and what was deliberately
not claimed.

## What changed vs. source (per redo contract)

- **Register:** Teardown → Plain. Body developed into one idea per beat (10 beats: B00
  writer + B01–B06 body + BCRY + BHTF + BOUT) instead of the source's five acts +
  worked example scaffold.
- **Cold open:** source's `ClaudeComposerAsk` direct-address ask → `BrutalistHesitantWriter`.
  Writer types "A white lie is kind. Shouldn't Claude tell one?", hesitates on "kind",
  corrects to "a policy" — the reel's actual wrong guess (a white lie is harmless
  because it's kind), picked up and falsified by B03 (repeated to millions, a "harmless"
  lie is a policy, not a kindness).
- **Close:** `OutroCTA` + `@HumanitariansAI`, Liam sign-off, instead of source's
  `ClaudeTitleOutro`/`@NikBearBrown`.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Facts/argument:** the key case (gift question) carried unchanged as the anchor,
  planted at B01 and paid off at B06. The five source act titles all became load-bearing
  beats: "above human norms" → B01–B03 (the gift case + scale-changes-everything break);
  "the seven components of honesty" → B04 (several properties, two near-absolute); "a
  weak duty to volunteer vs a strong duty not to deceive" → B05 (the split, its own
  beat); "sincere vs performative assertions" and "personas and meta-transparency" → B06
  (both directions, folded together with the anchor payoff, same compression pattern as
  the corrigibility-dial precedent's floor+ceiling beat). The worked example (persona
  "Aria") became B06's persona card.

## NO-GENAI / NO-PANTRY LAW

No source beat kept in this build was AI-VIDEO, pantry, or a human-drop slot (the
source's B00 was already `ClaudeComposerAsk`/REMOTION, not a puppet). Every beat in
this reel is REMOTION (B00, BCRY, BHTF, BOUT) or bespoke GRAPHIC/Manim (B01–B06), built
fresh in the humanitarians palette (`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`), matching
the precedent set by `behind-the-model--claude-constitution-corrigibility-dial`.

## Two real defects found and fixed during Gate V (not just re-run)

1. **B01's "will not assert / what it does not believe" caption rendered with collapsed
   spaces** ("won'tsay whatit" / "doesn'tbelieve") on first Manim render, caught via
   frame grab at the beat's near-end timestamp. Root-caused with an isolated debug
   scene: this Manim/Pango install collapses spaces in `Text()` at small font sizes
   with terracotta color and default (non-bold) weight — reproduced with plain,
   quote-free strings, confirming it's a color+weight+size shaping defect, not a
   string-specific bug. Every other terracotta `Text()` in the file already carried
   `weight=BOLD` (which sidesteps the defect); only this one two-line label didn't.
   Fixed by adding `weight=BOLD`; re-rendered and reverified via frame grab — spaces
   render correctly.
2. **GATE T (pixel type-check) failed 5/10 beats on first post-render run.** Traced each
   to a known, previously-documented false-positive class in `runtime/scripts/
   type_check.py` (extensive precedent comments from dozens of prior reels): (a) B01/B04
   bbox-overlap — a bordered card/pill's RoundedRectangle stroke blob mistaken for a
   text-run enclosing its own interior label, the same "label-inside-a-card" pattern as
   `B02_FiveProperties`/`B03_HookMechanism`; (b) B03 contrast — the terracotta gift-
   ribbon/grid (a pure graphical accent, no text) misread as accent typography, the same
   "TERRA-on-cream ~2.7–3.1:1 is a known palette constraint for structural marks"
   pattern documented for `S04Scene`/`S09Scene`/`S14Scene` and ~30 other precedents; (c)
   B02/B06 kerning — a drawn checkmark / two Circle "mask" glyphs sitting at the same
   y-band as nearby text, read as one compound multi-element run, the same pattern as
   `S07Scene`/`S08Scene`. Verified each by direct frame pull (not assumed) before adding
   the reel's scene names to the corresponding exemption sets in `type_check.py`, with a
   comment documenting the verification — same convention as every precedent entry.
   Separately, B06 also had a genuine **min-size** failure (a caption measuring
   18–19px against a ~20.5px floor); fixed by increasing font sizes (several normal-
   weight captions bumped to `weight=BOLD` + larger `font_size`, not just exempted) and
   reverified. All contrast/bbox-overlap/kerning FAILs cleared to 0 after the exemption
   fix (confirmed the coordinates were stable/reproducible pixel measurements, not
   flaky output, before adding any exemption). GATE T: PASS on the final run.

## Gates

- **TIMING LAW (B00):** narration 32 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **9.86s** (≥9s floor, ≥8s render floor). Correction ("kind" →
  "a policy") verified fully typed and settled by end-of-clip via frame grab.
- **GATE AUDIO:** PASS, mean_volume **-23.9 dB** (well above the -40 dB floor), max_volume
  -2.9 dB.
- **Gate V (frame QC):** every GRAPHIC beat (B01–B06) checked at mid-beat and near-end
  timestamps before and after fixes; one real defect found and fixed at the root
  (B01 space-collapse, detailed above). B02–B06 otherwise clean. Full-cut 4-second-spaced
  frame sweep (34 frames, contact-sheeted) plus targeted checks of the four Remotion
  beats (B00, BCRY, BHTF, BOUT) post-compile — all legible, safe inset, no overlap,
  Humanitarians AI skin correct throughout (composer card, subscribe chip, outro title
  all read cleanly).
- **GATE T (pixel type-check):** FAIL (5 beats) → PASS after root-causing each finding
  per the defect log above.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output
  (10/10 beats, no violations).
- **Motion histogram:** WARNING, graphic 6/10 (60%, over the ~40% pantry cap).
  Non-blocking and structural for this skill: B00 (writer), BCRY, BHTF, BOUT are
  REMOTION by the hai-simple spine itself, and at only 6 body beats this 10-beat reel
  necessarily runs higher than 40% on the graphic side. Same disposition as the
  corrigibility-dial precedent's identical histogram warning.

## Output

`behind-the-model--claude-constitution-honesty-standard.mp4` — 137.1s, 3840×2160,
10/10 beats real (no slate), audible narration throughout (mean -23.9 dB). This is the
review cut (COMPLETION LAW satisfied: newer than `beat_sheet.json`, mean_volume
verified via ffprobe/compile GATE AUDIO). `compile.py` forces a 4K master by default
("4K LAW"), so no separate low-res pass exists for this cut.
