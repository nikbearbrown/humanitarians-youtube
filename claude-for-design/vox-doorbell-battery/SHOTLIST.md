# SHOTLIST — vox-doorbell-battery

Typed work order. Drop media into `media/` as `B01.png` / `B01.mp4` etc.;
`media/<beat>.mp4` beats `media/<beat>.png` beats greybox placeholder. AI
plates need no sidecar but ship with the synthetic-disclosure credit line;
any archive substitution requires `B<nn>.source.txt` or the STAND-IN X stays.
GRAPHIC beats render from this reel's `vox_scenes.py` after audio lock.

Shot-type histogram: GRAPHIC 5 · COMPOSITE 3 · CARD 2 · STILL 1 · DOCUMENT 1
(12 beats). Rhythm: B05–B06 GRAPHIC pair broken by B07 COMPOSITE; B08–B10 is a
3-beat GRAPHIC run — accepted, it is the evidence run (arithmetic → verdict →
isotype), precedent vox-wave-function. No other runs >2.

Accents: dusty blue `#5B7B9C` vs terracotta `#D35F43`; golden highlighter
`#F5D061` is the single annotation voice. Isotype mark: square.

---

## AI plate slots (YOURS — generate, drop in media/)

### B01 — STILL·ai · the dead doorbell (cold open, kenburns)
```
Suburban American front door in flat overcast November light, sleek modern smart video doorbell mounted on the door frame, indicator light dark and dead, shallow depth of field, muted colors, editorial documentary photograph, in the style of Edward Burtynsky, hyper-realist, clean sharp focus --ar 16:9
```

### B03 — COMPOSITE·ai · teardown plate (chips land at assembly)
```
Product teardown photograph shot from directly above, disassembled smart video doorbell laid flat on gray studio background, opened casing, exposed circuit board and lithium battery pouch arranged in a neat grid, knolling style, soft even studio lighting, editorial product photography, photoreal --ar 16:9
```
Remotion chips (assembly plane, not baked): 'HARDWARE — unchanged' · 'BATTERY —
unchanged' · terracotta 'FIRMWARE v2.1 — +person detection'.

### B07 — COMPOSITE·ai · processor macro (duty-cycle strip at assembly)
```
Extreme macro photograph of a small ARM microcontroller chip centered on a compact circuit board from a smart doorbell, dark PCB, fine solder detail, shallow depth of field, moody studio lighting, photoreal --ar 16:9
```
Remotion overlay: awake/asleep timeline strip, lower third; terracotta AWAKE
blocks on dusty-blue ASLEEP floor; 'DUTY CYCLE = awake ÷ total' chip.

### B11 — COMPOSITE·ai · the doorbell again, closer (moral beat)
```
Close editorial photograph of a modern smart video doorbell on a door frame, camera lens dark and unlit, late autumn overcast light, slight low angle, muted desaturated palette, documentary product photography, photoreal --ar 16:9
```
Remotion chips: 'MODEL — correct' (blue) · 'HARDWARE — correct' (blue) ·
'DESIGN — wrong' (terracotta).

Optional archive texture substitutions (would flip slot to `archive`, sidecar
mandatory):
- https://www.loc.gov/free-to-use/  (doorways, houses)
- https://archive.org/details/prelinger?query=doorbell+home+electronics
- https://commons.wikimedia.org/w/index.php?search=smart+doorbell&title=Special:MediaSearch&type=image

## Prop document (YOURS or generated)

### B04 — DOCUMENT·own · "INTEGRATION TEST REPORT" prop sheet
Design (or generate) an aged-paper test-report sheet: typewriter serif,
three checklist rows — MODEL ACCURACY · RUNS ON PROCESSOR · FITS IN MEMORY —
each with an empty checkbox, and a conspicuous blank fourth-row gap at the
bottom of the page. No brand names.
```
Scanned single page of a vintage-style engineering test report, typewriter serif text on slightly aged off-white paper, three checklist line items with empty checkboxes, generous blank space at the bottom of the page, top-down flat scan, high resolution document photograph --ar 16:9
```
REMOTION PLANE: golden highlighter sweep + hand-drawn tick per row, keyed to
'accuracy' / 'processor' / 'memory'. Regions in `annotations.json`,
needs_review until the sheet is in hand.

## GRAPHIC beats (MACHINE'S — vox_scenes.py after audio lock)

### B05 — `B05_CascadeMemory`
Cascade spine: three slots (MEMORY / LATENCY / POWER), serif + hairline
underlines. Memory bar rises, stops under budget line, 'PASS' stamp on cue.
viz.note: textbook numbers (240 KB vs 256 KB) stay off-screen per card
exclusions — the shape is the claim.

### B06 — `B06_CascadeLatency`
Same frame, transform-don't-cut. Latency bar under the line, 'PASS' on cue,
memory bar dimmed.

### B08 — `B08_CurrentArithmetic`
Sliver vs column (asleep µA vs awake mA, ×1000-scale honesty, hand-drawn axis
tildes), then time-weighted average sweep with golden highlighter.
VERIFY (FACTCHECK.md): 15 mA / 5 µA / 3.4 s per 30 s / ~1.7 mA average —
ch 1 worked example.

### B09 — `B09_CascadeFail`
Cascade returns; POWER bar overshoots the line; orange hand-drawn ring on the
overshoot; 'SIX MONTHS' struck through, 'TWO DAYS' stamped.

### B10 — `B10_ReturnsIsotype`
24 charcoal squares count up in reading order (1 square = 500 returned units),
keyed to the audio window; ink X strikes 'PERSON DETECTION' chip on 'rolled
back'. VERIFY: 12,000 returns / December rollback = textbook anecdote figures.

## Cards (MACHINE'S)

- **B02** — eyebrow EMBEDDED AI · title WHY A PERFECT MODEL KILLED THE
  DOORBELL · sub "the calculation nobody ran"
- **B12** — eyebrow EMBEDDED AI · title THE THIRD BUDGET · sub
  "memory · latency · power"
