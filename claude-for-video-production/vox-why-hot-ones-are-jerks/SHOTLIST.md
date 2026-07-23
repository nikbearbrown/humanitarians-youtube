# SHOTLIST — vox-why-hot-ones-are-jerks

Converted from `physics/why-hot-ones-are-jerks` (audio reused; doodle INTRO
dropped — wrong brand). Heuristic types audited and REPLACED 2026-07-06 —
nothing remains needs_review. Series pilot: **Calling Bullshit (Vox Style)**.

Shot-type histogram: GRAPHIC 19 · CARD 2 · STILL 1 (22 beats, 71.9s).
GRAPHIC-heavy accepted by the schrodinger-film precedent: the film IS one
evolving diagram — the same seeded scatter carried through cuts, fades, and
tilts — and the motion axis rotates (drawon / isotype / annotate) even where
the type does not.

Color law for this film: **crimson = the cuts** (the filters), **navy = the
trend lines** (the data's voice), **golden highlighter = the surviving band**
— the one editor's-pen voice, used exactly once.

`pantry` law applies: beat-prefixed files only; ai slots need disclosure
sidecars.

---

## AI slot (the whole image budget — 1 still)

### A01 — STILL·ai · the awkward date (cold open, kenburns)
PROMPT LAW (aspects/stock-styles.md): object, size, geometry, distribution,
material, light, ground, exclusions.
```
hyperrealist photograph in the style of editorial documentary photography — two people in their late twenties on a stilted first date at a small round café table, seated across from each other, both leaning slightly back, phones face-down on the table between them, one glancing sideways; table fills the lower third, subjects centered with clear space between them; ceramic cups, wooden table, plain café wall falling to soft blur behind; flat overcast window light from the left, no golden hour; faces generic, no famous likeness; no text, no signage, no labels --ar 16:9
```
Generic subjects, generated, DISCLOSED: sidecar `A01.source.txt` with the
ai-disclosure line. Set `shot.focus` on the empty space between the two.
Until it lands: slate (pass 1 stays watchable).

---

## CARD slots (design system, Manim)

- **A17** — eyebrow CALLING BULLSHIT · title BERKSON'S PARADOX · sub "how filters invent patterns" (mid-film title card; the name lands as the reveal)
- **A22** — eyebrow THE RULE · title ASK WHO GOT FILTERED OUT · sub "before you trust a pattern" (closer; outro law pads this beat's mp3 — rerun `vox_outro.py` after any audio change)

---

## GRAPHIC slots (vox_scenes.py — render via vox_run, measured durations)

| beat | scene | motion | what |
|---|---|---|---|
| A02 | A02_Axes | drawon | ink axes on newsprint — the film's one diagram begins |
| A03 | A03_LabelX | annotate | serif 'attractive' + navy hairline |
| A04 | A04_LabelY | annotate | serif 'nice' + navy hairline |
| A05 | A05_Cloud | isotype | 120 seeded squares count up in the audio window |
| A06 | A06_FlatLine | drawon | navy flat trend — the premise, drawn |
| A07 | A07_PoolAgain | drawon | same-seed redraw: same people, now a dating pool |
| A08 | A08_CutLow | drawon | crimson cut, lower-left |
| A09 | A09_FadeLow | annotate | corner ghosts + crimson hatch |
| A10 | A10_CutHigh | drawon | crimson cut, upper-right |
| A11 | A11_FadeHigh | annotate | corner ghosts + crimson hatch |
| A12 | A12_Band | annotate | GOLDEN HIGHLIGHTER over the surviving band (the pen, once) |
| A13 | A13_BandAlone | drawon | survivors alone (same seed) |
| A14 | A14_Tilt | drawon | navy trend tilts down |
| A15 | A15_YourPool | annotate | terracotta chip 'in YOUR pool' |
| A16 | A16_Ghosts | annotate | the two crimson cuts return at 40% |
| A18 | A18_GoogleQuote | annotate | paraphrase card: Google's contest-coder finding + attribution (FACTCHECK row A18 — no invented verbatim quote) |
| A19 | A19_MiniScatter | drawon | hired-pool scatter, navy down-trend |
| A20 | A20_HiringBar | drawon | crimson hiring cutoff |
| A21 | A21_GateFunnel | isotype | squares enter wide, few exit — the gate makes the pattern |

Desk preflight applies: explicit safe-area arithmetic in scene comments +
Gate A static check (16:9 ±6.4/±3.5).

## Order of operations

1. `vox_run.sh` — Gate A → render all 21 scenes to measured durations →
   Gate B → slate in A01 → outro → review compile. Watchable immediately.
2. Generate the A01 still (cheap, one image, per-step go-ahead) → pantry →
   rebuild (one slot recompiles).
3. `vox_short.py` after the master — portrait relayouts for A05/A12/A21;
   consider dropping A18 (dense quote card) in the Short.
