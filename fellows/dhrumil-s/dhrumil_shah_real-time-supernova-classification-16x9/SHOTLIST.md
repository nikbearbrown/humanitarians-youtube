# SHOTLIST — Seven Million Alerts a Night (16:9)

Typed work order for the landscape cut, one block per beat. **Every shot is a pipeline shot** — no
archival stills, stock, screen recordings, AI-generated imagery or human-supply slots.

**Canvas** 3840 × 2160 (16:9) · **30 fps** · **4,914 frames / 163.80 s** · **16 beats**
**Clock** measured Kokoro `am_onyx` narration — `audio/timings.json`, identical to the 9:16 cut and
imported by the composition. Exact frame in/out per beat: `beat_sheet.json` and
`storyboard/STORYBOARD.md`.

This is a **native recomposition**, not a crop or letterbox of the vertical film. Where the 9:16 cut
stacks, this one sets things side by side; where the vertical arithmetic runs downward, this one
runs left to right.

---

## Standing rules (every beat)

- **Ground:** `#04060C` deep-sky gradient, 16×9 coordinate grid, starfield drifting *sideways*.
- **Title-safe area:** 200 px left/right, 110 px top/bottom (~5%). No text sits outside it.
- **Band plan:** chrome rail y=110 · pipeline rail y=212 · content y=390–1690 · captions
  y=1726–1946 · source line y=1984.
- **Two columns:** a **left title column** (x=200, 1160 px wide) carries the eyebrow, the two-line
  serif headline, and the beat's supporting text anchored to its foot; the **stage** (x=1480, 2160 px
  wide) carries the mechanism.
- **Full width:** chrome rail (presenter · title · NN/16), six-stage pipeline rail, caption band,
  source line.
- **One accent per frame:** amber = the candidate; cyan = instrument/detection; crimson = rejected;
  green only from B13.
- **Entrances:** one spring (damping 24, stiffness 110, mass 0.9) — fade plus 34 px lift.
- **Type:** Georgia headlines (110 px), Segoe UI captions (70 px) and body, Consolas chrome and
  numerals.
- **Captions:** same phrases at the same frames as the 9:16 cut; mobile line breaks joined and
  re-wrapped to a 3000 px landscape measure.
- **Transitions:** hard cut on the measured beat boundary.

---

## B00 · PRESENTER INTRODUCTION · VO 11.47 s · 01 / 16

| | |
|---|---|
| **Narration** | "Hi, I am Dhrumil Shah, and this video is about how artificial intelligence helps astronomers sort millions of nightly sky alerts, to find the exploding stars that are actually worth a telescope's time." |
| **Left column** | `WELCOME` · **Hi, I'm / Dhrumil Shah.** · amber-ruled `THIS VIDEO, IN ONE LINE` summary · `AI IN ASTRONOMY & SPACE SCIENCE` |
| **Stage** | the six pipeline stages listed top to bottom (205 px rows): marker, `01 SCAN`, gloss — joined by a drawing cyan spine |
| **Composition logic** | who and what on the left; how, as a route, on the right |
| **Animation** | greeting 0.2 s · summary 2.6 s · stage rows from 5.0 s at 13-frame intervals with the spine drawing · series tag 9.6 s |
| **Sound** | quiet D-minor chord; one soft rising blip per stage row |
| **Out** | cut into the cold open |

## B01 · COLD OPEN — the flood · VO 10.69 s

| | |
|---|---|
| **Left column** | `Real-time transient astronomy` · **Seven million / alerts a night.** (amber) · italic pull-quote "Somewhere in that flood, a star has finished exploding." |
| **Stage** | a 300 px counter racing to `7,000,000` over a full-width progress rule · `CHANGES REPORTED IN ONE NIGHT` / `AT FULL SURVEY OPERATIONS` |
| **Full frame** | 560-point amber ignition field over a 340-star field, no grid |
| **Animation** | counter frames 22→200 on a 0.55 power curve; ignition sweep frames 14→210; pull-quote 4.0 s |
| **Sound** | alert ticks densifying with the counter |

## B02 · THE PROBLEM · VO 8.81 s

| | |
|---|---|
| **Left column** | **No one can read / seven million.** · closing line "So nothing in this pipeline can wait for a person." |
| **Stage** | `1 / sec` → `81 days` between rules · `DERIVED` flag + `7,000,000 ÷ 86,400 s = 81.0 days` |
| **Background** | landscape dark candidate sheet (`sheet_26x14_dark`) drifting 380 px left under horizontal and vertical darkening gradients |
| **Animation** | stat row 0.87 s; DERIVED row 2.1 s, never before its figure |
| **Sound** | 1 Hz tick |

## B03 · SCAN · VO 9.91 s

| | |
|---|---|
| **Left column** | `STAGE 01 — SCAN` · **The same sky, / again and again.** · `LEGACY SURVEY OF SPACE AND TIME` · `TEN YEARS · ~1,000 POINTINGS PER NIGHT` |
| **Stage** | 8×3 footprint grid with caption row · widening beam cone · observatory silhouette |
| **Animation** | sweep index 0→24 over frames 26–230; fresh tiles flash cyan, then settle |
| **Sound** | soft shutter per tile group |

## B04 · REFERENCE & NEW · VO 8.70 s

| | |
|---|---|
| **Left column** | `STAGE 01 — SCAN` · **Every image has / an ancestor.** · synthetic-data tag |
| **Stage** | template (820 px) **left**, new visit (820 px) **right**, double-headed registration arrow with `ALIGNED` / `PIXEL FOR PIXEL` between |
| **Composition logic** | before → after as a left-to-right reading order — the landscape equivalent of the vertical cut's stacking |
| **Animation** | template 0.5 s · marker 1.4 s · new visit 1.9 s |
| **Sound** | two image-load blips; alignment click |

## B05 · SUBTRACT · VO 10.24 s

| | |
|---|---|
| **Left column** | `STAGE 02 — SUBTRACT` · **Only what / changed survives.** · `≥ 5σ` flag · `POSITIVE OR NEGATIVE FLUX — BOTH COUNT` |
| **Stage** | new visit (500) − template (500) → difference plate (880, amber) with reticle and ×3 zoom inset |
| **Composition logic** | the arithmetic reads left to right as a written equation |
| **Animation** | operands 0.4 s · arrow 1.5 s · difference plate 1.8 s · reticle frames 86–132 · zoom inset frames 128–164 |
| **Sound** | subtraction whoosh; detection ping on lock |

## B06 · WHAT COULD IT BE · VO 10.73 s

| | |
|---|---|
| **Left column** | `STAGE 02 — SUBTRACT` · **A dot is not / a discovery.** · synthetic-data tag |
| **Stage** | row 1: supernova · variable star · active nucleus (420 px zoomed stamps) — amber `LOOK ALIKE` rule "Three different causes. One indistinguishable dot." — row 2: asteroid (cyan) · cosmic ray · subtraction artifact (crimson) |
| **Animation** | row 1 from 0.4 s; rule 2.1 s; row 2 from 2.7 s |
| **Sound** | six placement ticks |

## B07 · ALERT — the packet · VO 11.88 s

| | |
|---|---|
| **Left column** | `STAGE 03 — ALERT` · **It packages it / instead of judging.** · template and difference cutouts + "The packet carries the pixels too — so a classifier never has to trust a number alone." |
| **Stage** | five-row packet table (key / value) beside a 340 px countdown ring: `60 SECONDS` · `REQUIREMENT` · `≥98% OF A VISIT'S ALERTS, OUT OF THE DATA FACILITY` |
| **Animation** | rows every 16 frames from 0.47 s; ring sweeps frames 30→300; cutouts 5.0 s |
| **Sound** | data blip per row; ping as the ring closes |

## B08 · THE STREAM · VO 8.35 s

| | |
|---|---|
| **Left column** | `STAGE 03 — ALERT` · **A public stream, / caught by seven.** · `FULL-STREAM COMMUNITY BROKERS — INDEPENDENT OF THE OBSERVATORY` |
| **Stage** | 300 packets falling down seven lanes onto the broker rule (ALeRCE in amber) · `~1,000` · `7` · `Public` |
| **Animation** | independent phases/speeds; packets brighten to cyan in the last 28% of descent |
| **Sound** | wash of quiet data pulses |

## B09 · CLASSIFY — two models · VO 11.10 s

| | |
|---|---|
| **Left column** | `STAGE 04 — CLASSIFY` · **Answer now, / or answer better.** · italic "Brokers run both. Speed and certainty are a schedule, not a choice." |
| **Stage** | two full-width blocks: MODEL 01 stamp classifier (three 180 px cutouts → CNN → SN/AGN/VS/ASTEROID/BOGUS) · MODEL 02 light-curve classifier (mini light curve → balanced random forest → hierarchical taxonomy) |
| **Animation** | block 01 0.4 s; block 02 2.1 s; light curve draws frames 140–230 with six detections |
| **Sound** | fast bright texture, then slower lower texture |

## B10 · LIGHT CURVE · VO 10.07 s

| | |
|---|---|
| **Left column** | `STAGE 04 — CLASSIFY` · **The shape is / the evidence.** · three-item legend · illustrative-shapes note |
| **Stage** | one 2030 × 1110 px plot: BRIGHTNESS vs TIME — DAYS TO WEEKS |
| **Animation** | supernova frames 26–132 · variable star 140–216 · asteroid point 224–268 |
| **Sound** | low blip on the asteroid point |

## B11 · PROBABILITIES · VO 10.49 s

| | |
|---|---|
| **Left column** | `STAGE 04 — CLASSIFY` · **A distribution, / not a verdict.** · `ILLUSTRATIVE VALUES` flag + note |
| **Stage** | four bars (Supernova 86 · AGN 7 · Variable star 4 · Artifact 3) **beside** the `WHAT IS ACTUALLY PUBLISHED` panel (`~90%` accuracy, balanced test set · `81%` recall, TNS-confirmed SNe) |
| **Composition logic** | invented output and cited evidence sit in separate, visibly bordered columns |
| **Animation** | flag lands first (0.33 s); bars and numerals grow together frames 22–110; panel 3.2 s |
| **Sound** | four soft descending fills |

## B12 · RANK · VO 8.70 s

| | |
|---|---|
| **Left column** | `STAGE 05 — RANK` · **Sorting is the / contribution.** · illustrative-queue note |
| **Stage** | 13-row queue where `DIA3412778 · 0.86` lifts from row 9 to row 1 · beside `3,412` Alerts that sank and `#1` Reached a human tonight |
| **Animation** | hero row rises frames 40–150; lower rows fade by position; stats 5.3 s |
| **Sound** | whoosh; ping at first place |

## B13 · FOLLOW-UP · VO 10.14 s

| | |
|---|---|
| **Left column** | `STAGE 06 — FOLLOW-UP` · **Then something / else must look.** · pull-quote with **what it actually is** in green · illustrative-spectrum note |
| **Stage** | dome slewing on a fixed pier (left) beside a 1300 px spectrum drawing BLUE → RED with `ABSORPTION FEATURES → COMPOSITION · VELOCITY · REDSHIFT` |
| **Animation** | dome +26° → −12° frames 18–108; spectrum frames 118–232; first green in the film |
| **Sound** | dome rumble; sustained chord |

## B14 · THE LIMIT · VO 9.21 s

| | |
|---|---|
| **Left column** | `THE LIMIT` · **A ranking is not / a confirmation.** (amber) · amber-ruled pull-quote |
| **Stage** | `EACH DOT ≈ 1,000 SUPERNOVAE RUBIN MAY FIND` · 50×20 dot field, 30 lit green · `~1,000,000` Supernovae expected · `~30,000` Planned spectra (TiDES) |
| **Animation** | dots reveal in index order frames 18–120; stats 3.0 s; pull-quote 4.7 s |
| **Sound** | score only |

## B15 · CLOSE · VO 6.93 s + 1.58 s tail

| | |
|---|---|
| **Composition** | centred: pulsing amber point at y=700; one-line title **Seven Million Alerts a Night.**; italic closing line; amber rule; `DHRUMIL SHAH`; series tag |
| **Animation** | point pulses on a slow sine; title 0.2 s; line 0.87 s; presenter card 1.8 s |
| **Sound** | resolution chord |
| **Out** | held tail, end of film |

---

## How the two cuts differ, beat by beat

| Beat | 9:16 arrangement | 16:9 arrangement |
|---|---|---|
| B00 | greeting → summary → stage list, stacked | greeting + summary left, stage list right |
| B04 | template above new visit | template left of new visit |
| B05 | operands above the result | operands → result, left to right |
| B07 | table + ring, cutouts beneath | table + ring on stage, cutouts in the left column |
| B11 | bars above the published panel | bars beside the published panel |
| B12 | queue above stats | queue beside stats |
| B13 | dome, spectrum, quote stacked | dome beside spectrum; quote in the left column |
| B14 | 40×25 dot field | 50×20 dot field (same 1,000 dots, same 30 lit) |
| all | starfield drifts down | starfield drifts sideways |

Narration, claims, on-screen wording, source lines, colours, timing and sound are the same in both.
