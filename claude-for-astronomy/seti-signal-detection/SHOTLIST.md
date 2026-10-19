# SHOTLIST — *The Signal We Imagined.*

Ep. 13 · `seti-signal-detection` · 14 beats · 420 words
Channel `claude-hai`, Pragmatist register, Kokoro `af_bella`, $0.00.

**ILLUSTRATE LAW.** The Claude UI appears at **B00, B11, B12, B13 only**.
All ten inner beats illustrate their own concept as reel-local Manim
(`scenes.py`). No composer wallpaper.

**Aspect.** One `scenes.py` lays out both cuts. `frame_height = 8.0` either
way; only the horizontal extent changes — x ±6.15 landscape, ±1.80 portrait.
Portrait is **not a crop**. The rule — *anything the narration speaks stays
on screen; the on-screen-only extras are what portrait loses.*

---

## Plates

All seven come from `assets/gen_seti.py`, which runs the real de-Doppler
search. Plates carry **imagery only** — every label and counter is vector
type in `scenes.py`.

| Plate | px | ratio | What it is |
|---|---|---|---|
| `waterfall.png` | 1500×700 | 0.467 | One dynamic spectrum: interference vertical, the injected signal traced in terracotta |
| `three.png` | 1552×420 | 0.271 | The same field under three hypotheses |
| `three_v.png` | 760×940 | 1.237 | The same three, stacked, for portrait |
| `recall.png` | 1560×780 | 0.500 | Recall, three hypotheses × two searches |
| `edge.png` | 1560×780 | 0.500 | Recall against the search's lower drift limit — the cliff |
| `compare.png` | 1560×780 | 0.500 | Morphology search against the cadence test |
| `cadence.png` | 1150×478 | 0.416 | Six integrated traces: three pointed at, three pointed away |

**Plate geometry.** `ph = pw × (ih/iw)`. The landscape figure band is 4.30
units, so the 0.50-ratio plates run at pw 6.4–6.6. `three.png` is 0.271 — at
portrait's 3.44 units its three panels would be 1.1 units across and the lean
of the marked track, which is the whole content, stops being readable, so
portrait loads `three_v.png` instead.

---

## Beats

| # | Act | Lane | Scene | The shot |
|---|---|---|---|---|
| B00 | COLD OPEN | ask | `ClaudeComposerAsk` | Composer types the ask; `sweeping 49 drift rates across 512 channels…`; three result lines |
| B01 | FRAME | manim | `B01_Presenter` | Row one STRUCK (twelve episodes / things that exist), row two boxed (this one / nobody has found it) |
| B02 | FRAME | manim | `B02_OneBreath` | WE HAVE NEVER DETECTED ONE → SO YOU ASSUME A FORM → **AND THEN YOU FIND IT**, the third accented and underlined |
| B03 | THE STAKES | manim | `B03_BLC1` | A frequency axis; one terracotta tone at 982 MHz, named; then **26 ink look-alikes** appear around it and the terracotta tone turns ink |
| B04 | THE MECHANISM | manim | `B04_TheData` | `waterfall.png`; interference named as *us*; the leaning track traced; chip — *and you cannot see it* |
| B05 | THE MECHANISM | manim | `B05_TheAssumption` | Drawn **natively**: a fan of trial tracks sweeps the box, one lights terracotta, a bracket closes around the range, a vertical track outside it greys |
| B06 | THE MECHANISM | manim | `B06_Three` | `three.png` / `three_v.png`; the three hypotheses named |
| B07 | THE RESULT | manim | `B07_BlindSpot` | `recall.png`; the middle ink bar ringed **flat on the axis**; counters **0 of 80** then **80 of 80** |
| B08 | THE RESULT | manim | `B08_TheEdge` | `edge.png`; the cliff marked; chip at its foot — **0.06 Hz/s** |
| B09 | THE FIX | manim | `B09_OtherTest` | `cadence.png`; left column named *pointed at the star*, right *pointed away*; a peak three times, flat three times |
| B10 | THE TELL | manim | `B10_TheTell` | `compare.png`; the middle ink bar flat again beside a terracotta bar at **0.76** |
| B11 | VERDICT | ask | `ClaudeVerdictArtifact` | Five artefact lines, the fifth accented |
| B12 | HANDOFF | ask | `ClaudeComposerAsk` | `Your turn.`; the prompt types itself; three grading lines |
| B13 | OUTRO | ask | `ClaudeTitleOutro` | Title restate, terracotta period, rule, handle, subline |

**B05 is drawn natively** rather than from a plate, so the fan of trial
tracks sweeps *on the spoken phrase* and the bracket closes around it as the
voice names the assumption. A plate could not time that.

---

## Colour contract

Terracotta `#D97757` is the ONE accent and marks **what the assumption
decides** — the injected signal's track, the recall that appears the moment
the search is widened, and the cadence test, which does not depend on the
guess at all. Ink marks **what is there regardless** — the interference
standing vertical at zero drift, and the morphology search's own score.

The load-bearing moment is B07: the ink bar for the drift-corrected signal
lies **flat on the axis at zero** while the terracotta bar beside it stands
at full height. Same signal, same data, one number changed. The zero bar is
drawn as a visible zero-height mark, not omitted — a missing bar reads as a
rendering fault rather than a measured nothing.

Accented text is `#A44A32`. `#B9B4A0` is strokes and fills only.

---

## Band plan (both aspects)

| | landscape | portrait |
|---|---|---|
| title | +3.02 | +3.14 |
| hairline | +2.66 | +2.84 |
| figure | +2.40 … −1.90 | +2.62 … −2.02 |
| closing line | −2.50 | −2.42 |
| citation | −3.20 | −2.95 |
| wordmark bug | −3.12 | −3.28 |

---

## Portrait reductions

Dropped at 9:16, all on-screen-only, none of it spoken:

- **B03** — the ledger chip and the Parkes/Proxima card.
- **B04** — the `time ↓` axis label; the three remaining labels centre
  instead of hanging off the plate's edge.
- **B05** — the two-row side column; the closing line changes to *never
  looked for*, which the voice does say.
- **B07** — the two sub-labels under the counters. Both counters stay,
  because the voice speaks both numbers.
- **B08** — the `recall` axis label and the explanatory note.
- **B10** — the ink/terracotta key.

Nothing the narration speaks is dropped in either aspect.

---

## PPT TEST

No beat could be exported as a static slide. Type struck on the spoken
contrast (B01); a card typing itself (B02); one tone standing alone and then
being surrounded by twenty-six identical ones before turning ink (B03); a
track traced across a field the viewer is told they cannot see (B04); a fan
of trial tracks sweeping and a bracket closing around them (B05); a bar
ringed flat on its axis while a counter reads zero (B07); a curve followed
off a cliff (B08); six traces where three have a peak and three do not (B09).
**No two consecutive beats share a visual scheme.**
