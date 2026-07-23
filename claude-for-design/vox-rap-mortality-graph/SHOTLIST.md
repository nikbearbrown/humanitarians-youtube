# SHOTLIST — vox-rap-mortality-graph

Calling Bullshit (Vox Style), film two. Plan approved + Gate F green
2026-07-06. Histogram: GRAPHIC 7 · CARD 5 · STILL 2 (14 beats, max run 2 —
clean rotation). Color law: **crimson = the censor window**, **navy = the
data**, **golden highlighter = the rap bar** (the pen, once, A04).

`pantry` law applies: beat-prefixed files, ai slots need disclosure sidecars.

---

## AI slots (the image budget — 2 stills)

### A01 — STILL·ai · the era as an object (cold open, kenburns)
```
hyperrealist still-life photograph in the style of editorial documentary photography — a 1980s portable boombox cassette player and a dynamic stage microphone lying beside it on a worn concrete stoop step, boombox occupying the left two-thirds in three-quarter view, microphone cable coiled loosely in the foreground; brushed metal, black plastic, chrome grille; flat overcast daylight, no dramatic shadows, no golden hour; shallow background of a brick wall falling to soft blur; no people, no hands, no text, no brand logos, no labels --ar 16:9
```
Sidecar `A01.source.txt` with the ai-disclosure line. `shot.focus` on the
boombox grille.

### A07 — STILL·ai · the survivor (kenburns)
```
hyperrealist environmental portrait in the style of editorial documentary photography — a Black man in his mid-fifties, generic face with no famous likeness, gray in his beard, seated at a home-studio mixing desk with both hands on the faders, looking down at the console in concentration; desk fills the lower third, subject centered; warm practical lamp light from the right mixed with flat window light; acoustic foam panels falling to soft blur behind; no text on screens, no logos, no labels --ar 16:9
```
MUST read generic — regenerate if it resembles any identifiable artist.
Sidecar `A07.source.txt`. `shot.focus` on the hands on the faders.

---

## CARD slots (design system, Manim)

- **A02** — CALLING BULLSHIT · THE RAP MORTALITY GRAPH · "a lie the data told itself"
- **A05** — THE QUESTION · WHO CAN BE IN A DEAD-MUSICIANS DATASET? · (no sub)
- **A10** — THE MECHANISM · RIGHT-CENSORING · "the window hides the living"
- **A13** — TO BE FAIR · SHE FLAGGED IT · "but no caveat survives a screenshot"
- **A14** — THE RULE · ASK HOW OLD THE CATEGORY IS · "before you mourn it" (outro law pads this beat)

---

## GRAPHIC slots (vox_scenes.py — written after audio lock, to measured durations)

| beat | scene | motion | what |
|---|---|---|---|
| A03 | A03_TheChart | drawon | navy genre bars draw up; representative values, unlabeled beyond genre names (FACTCHECK A03) |
| A04 | A04_RapBar | annotate | golden highlighter sweeps the rap/hip-hop bars |
| A06 | A06_GenreAges | drawon | genre-age timeline: century-long ink bars vs rap's short bar |
| A08 | A08_LivingVanish | annotate | isotype rows: navy (alive) squares fade from the young genre's row |
| A09 | A09_CensorLine | drawon | THE beat: lifespan bars on a timeline; crimson line slams at 'today'; crossing bars vanish |
| A11 | A11_JazzCentury | isotype | jazz's century fills with ink deaths at all ages; rap's four decades mostly navy survivors |
| A12 | A12_ChopTheWindow | drawon | null model: identical lifespans, chopped window, derived averages fall — "most", never "all" |

Desk preflight applies (16:9 ±6.4/±3.5; margin arithmetic in scene comments).

## Order of operations

1. **Audio lock** (paid, ~280 words): `generate_audio.py` → `vox_align.py`.
2. I write `vox_scenes.py` to the measured durations (free) → Gate A.
3. `vox_run.sh` → watchable cut with slates in A01/A07 → Gate B.
4. Generate the 2 stills (per-step go-ahead) → pantry → rebuild.
5. `vox_short.py` → portrait relayouts for A03/A09/A11; A13 card likely
   survives vertical; decide drops at the short gate.
