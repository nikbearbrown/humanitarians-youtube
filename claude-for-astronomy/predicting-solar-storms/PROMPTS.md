# PROMPTS — *The Same Sunspot, Twice.*

Ep. 12 · `predicting-solar-storms`

**No image-generation prompts exist for this reel, and that is not an
omission.** REBUILD LAW requires every figure to be a native animated
graphic; nothing here is a generated still, a stock image, a photograph, or a
redrawn published plot. There is no FLUX prompt, no nano-banana prompt, no
pantry request, and no step that could spend money.

What stands in place of image prompts:

| Beat | Visual | Where it comes from |
|---|---|---|
| B01, B02 | kinetic type, cards, rules | drawn in `scenes.py` |
| B03 | 49 isotype squares + the date card | drawn in `scenes.py`; the counts are NASA's and *Space Weather*'s |
| B04 | `regions.png` | `assets/gen_solar.py` |
| B05 | `split.png` / `split_v.png` | the same regions, split two ways |
| B06 | `nearest.png` | measured nearest-neighbour distances |
| B07 | bars drawn natively | the medians printed by the generator |
| B08 | `scores.png` | measured TSS, 12-run medians |
| B09 | `spread.png` | every run, not just the median |
| B10 | `control.png` | the fingerprint sweep |
| B00, B11, B12, B13 | Claude UI | shipped Remotion compositions, props in `beat_sheet.json` |

**The Starlink beat is an isotype count, never a satellite picture.** Forty-
nine squares, thirty-eight of which change colour and fall. The number is
the point, and a rendering of a satellite would be decoration.

---

## The two prompts that ARE in the reel

### B00 — the cold-open ask

> Machine learning models forecast solar flares from sunspot measurements,
> and they report strong skill scores. How is that skill measured, and is
> the number real?

`runningText`: `splitting 20,228 rows from 350 regions...`

Result lines, which land answered (COLD OPEN LAW — the ask is never left
hanging):

- every region in the test set was also in training
- the flexible model 'wins' - 0.48 against 0.36
- split it honestly and it drops 75%

### B12 — the handoff (HANDOFF LAW)

Greeting fixed to `Your turn.`, `runningText`: `paste this into Claude...`

> Here is how I split my data into training and test sets. Tell me what could
> appear on both sides of that split, how much it could be inflating my
> score, and the cheapest way to find out.

Grading lines on screen:

- grade it: does it name the unit that repeats, not just 'rows'
- grade it: does it propose a split you could actually run
- grade it: does it predict which direction the score moves

**The prompt is read aloud verbatim and then discussed**, per HANDOFF LAW.

Why this prompt and not "learn more about space weather": the transferable
skill is recognising *the unit that repeats* in your own data — the patient,
the user, the sensor, the active region — and the first grading line is the
one that makes it bite. A model that answers "rows could appear on both
sides" has not understood the question; the answer has to name the thing that
generates many near-identical rows.

The third line matters too. An honest split should *lower* the score, and a
viewer who is told which direction to expect can tell a real diagnosis from a
reassuring one.

---

## Verdict artefact lines (B11, on screen)

Five lines, not four. A four-line `ClaudeVerdictArtifact` card sits almost
exactly on GATE V's bbox-fill floor and the verdict flips on encoder noise
(logged in Ep. 10).

1. A sunspot region is measured every hour for days, so one region is dozens
   of nearly identical rows.
2. Shuffle the rows before splitting and every region in the test set is also
   in the training set.
3. A flexible model then recognises the region instead of forecasting the
   flare — and scores 0.48 to the simple model's 0.36.
4. Split by region and it falls to 0.12. Three quarters of its skill was the
   split.
5. The fix is one line, and it costs nothing: split by region, not by row.

---

## Greeting

`Hi, HAI` — SKILL.md limits the HAI persona to the shortest forms (Hi · Ola ·
Hej · Ciao). All four are in use, so the lexicon cycles least-recently-used
first: Hej (03), Ciao (04), Ola (05), Hi (08), Hej (09), Ciao (10), Ola (11).
Least recently used is Hi, last seen at Ep. 08.
