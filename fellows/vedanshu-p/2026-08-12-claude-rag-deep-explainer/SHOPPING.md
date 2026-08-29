# SHOPPING.md — claude-liam-rag-deep-explainer (Gate D2)

Written after audio lock (Kokoro `am_onyx`; total **6:11** — `beat_sheet.json`
`actual_duration_s` per beat is ground truth). Seven slots, all STILLS, all
**Tier 1** (generic/illustrative — this chapter names no real person,
building, or artifact, so none of these need a rights escalation). Drop
files into `pantry/` with the exact names below.

**Tier 0 note:** this toolkit checkout has no `pantry_search.py` / local
stock library (`svg/svg/images/`) to check first — confirmed absent, not
skipped. Every entry below goes straight to Tier 1 sourcing.

Treatment (desat ~80%, contrast ~1.15, cream seat, grain, warm-ink vignette)
is the machine's — supply CLEAN plates, don't pre-stylize. Ken Burns crops
in: the resolution floor is a floor, not a suggestion.

---

## [x] B02 — the help desk, establishing (Act I, run R1 opener) · window 10.67s

- **File:** `pantry/B02.png` · **Tier 1**
- **Camera:** run R1 opens wide (focus [0.50, 0.45], scale 1.3×), eases
  toward B03's tighter framing. **Floor: ≥2000px long edge.**
- **GEN PROMPT:** "A tidy office desk in the mid-afternoon, a laptop open to
  a chat-style help-desk interface (screen content abstract/illegible), a
  coffee mug, natural window light, documentary photograph, three-quarter
  angle, shallow depth of field, no visible logos, no readable text, no
  people's faces, no watermark."
- **Stock alternatives:** any generic "person using laptop, office, chat
  app" stock photo — verify the SPECIFIC photo's license page.
- **FILLED:** Pexels photo 6278751, "A Laptop Beside a Coffee Cup on Wooden
  Table" by Artem Podrez —
  https://www.pexels.com/photo/a-laptop-beside-a-coffee-cup-on-wooden-table-6278751/
  (Pexels License, no attribution required). Blank/blown-out laptop screen
  (no fabricated chat UI), coffee cup+saucer, blurred office interior with
  natural window light, three-quarter angle, no logos/text/people/watermark.
  6144x3456 source. See `pantry/B02.source.txt`.

## [x] B03 — the help desk, close on the answer (Act I, run R1 closer) · window 9.54s

- **File:** `pantry/B03.png` · **Tier 1**
- **Camera:** continues R1 from B02's handoff — push to 1.3×+ tight on the
  screen (focus [0.55, 0.40]). Same desk/light/palette family as B02.
  **Floor: ≥2000px.**
- **GEN PROMPT:** "Close-up on a laptop screen showing an abstract chat
  bubble with placeholder confident-looking text (no real readable words),
  same desk and lighting as a wide office establishing shot, documentary
  photograph, shallow focus, no logos, no watermark."
- **FILLED:** same source plate as B02 (Pexels 6278751, Artem Podrez),
  supplied at full resolution (6144x3456) UNCROPPED — the beat's own
  kenburns shot config (focus [0.55, 0.40]) does the tight push at render
  time, so no manual pre-crop was used (an earlier pre-cropped pass
  triggered compile.py's "still under output 3840x2160" upscale warning;
  reverted). Screen reads blank/overexposed in-frame; no chat text was
  fabricated. See `pantry/B03.source.txt`.

## [x] B09 — the archive / library shelves (Act II, standalone) · window 9.1s

- **File:** `pantry/B09.png` · **Tier 1**
- **Camera:** slow push, focus [0.50, 0.50]. **Floor: ≥2000px long edge.**
- **GEN PROMPT:** "A room of library or archive shelving, rows of books or
  document boxes, soft even light, indexed/organized look, documentary
  photograph, wide angle, no readable spine text, no people, no watermark."
- **Stock alternatives:** any generic "library stacks" / "archive room"
  stock photo — verify the specific photo's license.
- **FILLED:** Pexels photo 590493, "Light Inside Library" by Janko Ferlic —
  https://www.pexels.com/photo/blur-book-stack-books-bookshelves-590493
  (Pexels License, no attribution required). Wide library corridor, warm
  hanging bulbs, shallow/soft focus throughout — spine text small, angled,
  and out of sharp focus at full resolution (5013x4634); no people, no
  logos, no watermark. Rejected an Unsplash "Sächsisches Staatsarchiv
  Dresden" candidate for having clearly legible glowing shelf-label plaques
  as the frame's focal point. See `pantry/B09.source.txt`.

## [x] B19 — the server room, establishing (Act IV, run R2 opener) · window 10.1s

- **File:** `pantry/B19.png` · **Tier 1**
- **Camera:** run R2 opens wide (focus [0.50, 0.50], scale 1.2×), eases
  toward B20's close push. **Floor: ≥2000px.**
- **GEN PROMPT:** "A modest server room or training-rig setup, a rack of
  humming equipment with status LEDs, cables, cool ambient light,
  documentary photograph, wide angle, no readable labels, no logos, no
  watermark."
- **FILLED:** Pexels photo 5203849, "Black Server Racks" by Brett Sayles —
  https://www.pexels.com/photo/black-server-racks-5203849/ (Pexels License,
  no attribution required). Wide aisle of perforated server-rack doors,
  cables overhead, red/blue/green LEDs through the mesh. Checked at full
  resolution (4024x6048) plus a zoomed crop of the door/handle area
  specifically for hidden nameplates — none found. Rejected a "Network
  rack" candidate (Pexels 17323801) for a bright, legible "NETWORK-2" rack
  label. See `pantry/B19.source.txt`.

## [x] B20 — the clock / job queue (Act IV, run R2 closer) · window 8.2s

- **File:** `pantry/B20.png` · **Tier 1**
- **Camera:** continues R2 from B19's handoff — push to a wall clock or a
  job-queue status indicator near the racks (focus [0.60, 0.45]). Same
  visual family as B19. **Floor: ≥2000px.**
- **GEN PROMPT:** "Close-up on a wall clock or a small status monitor
  showing an abstract progress/queue indicator, positioned near server
  racks, cool light, documentary photograph, shallow focus, no readable
  text beyond abstract progress marks, no watermark."
- **FILLED:** Pexels photo 5050305, "High Angle Shot of Network Switch" by
  Brett Sayles —
  https://www.pexels.com/photo/high-angle-shot-of-network-switch-5050305/
  (Pexels License, no attribution required). Shallow-focus close-up on
  blinking green/blue/white status LEDs and cabling, cool light — reads as
  an abstract progress/status indicator; same photographer/shoot family as
  B19, distinct photo. No readable text/logos at full resolution
  (4630x3081). Rejected a patch-panel candidate (Pexels 6466143) for
  legible "PBI" brand text and "DMM-1701IM"/"Reset"/"Alarm" labels. See
  `pantry/B20.source.txt`.

## [x] B28 — the help desk, resolved (Act VI, run R3 opener) · window 8.9s

- **File:** `pantry/B28.png` · **Tier 1**
- **Camera:** run R3 opens in the SAME visual family as B02/B03 (same
  desk/light/palette — this is the "same scene, now calm" beat), wide
  (focus [0.50, 0.45], scale 1.3×). **Floor: ≥2000px.**
- **GEN PROMPT:** reuse B02's prompt verbatim (or the same photo, re-cropped)
  for visual continuity with the opening.
- **FILLED (reused, as instructed):** identical file to `pantry/B02.png`
  (Pexels 6278751, Artem Podrez) — copied verbatim per this entry's own
  instruction. The compiler's shot.focus (same as B02's) renders the R3
  framing; no new sourcing needed. See `pantry/B28.source.txt`.

## [x] B29 — the corrected answer, with source (Act VI, run R3 closer) · window 8.9s

- **File:** `pantry/B29.png` · **Tier 1**
- **Camera:** continues R3 from B28's handoff — push to the screen, now
  showing the corrected answer with a visible (abstract) source citation
  line (focus [0.55, 0.40]). Same family as B28/B03. **Floor: ≥2000px.**
- **GEN PROMPT:** "Close-up on a laptop screen showing an abstract chat
  bubble with a confident answer AND a smaller citation/source line beneath
  it (no real readable words), same desk and lighting as B28, documentary
  photograph, shallow focus, no logos, no watermark."
- **FILLED (reused):** identical file to `pantry/B03.png` (same plate,
  Pexels 6278751, Artem Podrez). A distinct close-up laptop-screen photo
  was searched for but no honest candidate kept the same desk/light family
  without fabricating readable UI content or introducing a mismatched
  second desk, so B03's plate is reused — the compiler's own shot.focus
  differs from B03's. See `pantry/B29.source.txt`.

---

## Not yours (pass 1 builds while you shop)

Manim beats (B05 B08 B10 B14 B15 B21 B26 B31), all Remotion beats (including
the two new `DeepQuoteCard` instances at B11/B16), the bookends, the slate
previz, `_qc/REPORT.md`. The seven slots above render as labeled slates
until pantry files land.

## Status

- [x] B02 · [x] B03 (run R1, same visual family) — Pexels 6278751
      (Artem Podrez), B03 uses the same full-resolution plate uncropped
- [x] B09 (standalone) — Pexels 590493 (Janko Ferlic)
- [x] B19 · [x] B20 (run R2, same visual family) — Pexels 5203849 +
      5050305 (both Brett Sayles, same shoot family, distinct photos)
- [x] B28 · [x] B29 (run R3, same visual family as B02/B03) — reused
      B02/B03 files verbatim, per this doc's own reuse instruction
- All 7 pantry files landed 2026-08-19; `pantry.py` intake + `compile.py`
  both ran clean. Final master compiled with 35/35 slots filled, zero
  slates. Review cut no longer waiting on this doc.
