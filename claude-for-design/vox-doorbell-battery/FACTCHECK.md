# FACTCHECK — vox-doorbell-battery

Source of record: `books/embedded-ai/chapters/01-chapter-when-ai-meets-constrained-hardware.md`

## The doorbell anecdote — TREAT AS TEACHING ANECDOTE, NOT NEWS

The chapter opens with a dated story (Nov 12, 2019; unnamed "well-known
home-security company"; 48-hour battery vs six-month spec; 12,000 first-month
returns; feature rolled back by December). The company is never named and the
event is not independently cited in the chapter. **Status: textbook teaching
anecdote, possibly composite.** The film's narration deliberately never names
a company or product line, and B01 says "late 2019" rather than the specific
date. Do not add a brand, logo, or recognizable product design to any plate.

Claims carried into the film on this basis:
- B01: six-month spec → 48-hour reality ("two days" in B09) — anecdote figures.
- B10: 12,000 returns first month; December rollback — anecdote figures.

If the underlying incident is ever pinned to a real product, revisit B01/B10
wording and add the citation here.

## The cascade arithmetic — chapter worked example, illustrative

B07–B09 transplant the chapter's worked numbers (its wristband example) as
the illustrative calculation, never attributed to the doorbell vendor:
- 15 mA active vs 5 µA sleep → ×3,000 ratio. Film says "thousands of times" — OK.
- 3.4 s inference per 30 s window → ~11% duty cycle. Film: "a few seconds of
  inference every thirty" and "awake a tenth of the time" — OK.
- Average ≈ 1.7 mA (µA-scale sleep floor → mA-scale average). Film: "jumps
  from microamps to milliamps" — OK.
- 220 mAh coin cell at 1.7 mA ≈ 130 h ≈ 5 days (chapter). Film avoids
  restating this as the doorbell's number; B09's "six months becomes two
  days" is the anecdote's own ratio, not this calculation. Keep the two sets
  of figures from blending on screen — no digits on B08/B09 bars.

## Rendering honesty checks

- B08: the µA-vs-mA drawing must respect ×1000 scale (axis-break tildes,
  log-scale honesty) — an exaggerated or flattened ratio is a false claim.
- B10: isotype = 24 squares × 500 units = 12,000 exactly; caption states the
  unit. One mark = one unit-bundle, reading order, count-up in the beat window.
- All AI plates (B01, B03, B07, B11, B04 prop if generated): synthetic —
  disclosure line required in credits block.
