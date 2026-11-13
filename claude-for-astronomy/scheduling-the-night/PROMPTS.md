# PROMPTS — Ep. 17, *scheduling-the-night*

## No image-generation prompts were used.

**Nothing in this reel is generated imagery.** There is no FLUX, no
nano-banana, no diffusion model, no stock art, and no paid API call of any
kind. This is a Fellow Tier build: total spend **$0.00**.

Every frame is one of:

1. **Manim vector drawing** — `scenes.py`, 10 classes, rendered twice (16:9
   and 9:16).
2. **A plate computed from the simulation** — `assets/gen_sched.py` draws all
   five PNGs with PIL directly from the arrays `assets/sched.py` produced.
   They are plots, not pictures.
3. **Remotion components** — `ClaudeComposerAsk`, `ClaudeVerdictArtifact`,
   `ClaudeTitleOutro`, rendered via `runtime/scripts/remotion_scenes.py`.

Narration is **Kokoro TTS `af_bella`**, local, free.

---

## Seeds and parameters — everything needed to reproduce the plates

```
assets/sched.py
  LAT_DEG        -30.0      site latitude
  NIGHT_H         8.0       hours
  BLOCK_MIN      30.0       N_BLOCK = 16
  ALT_MIN_DEG    20.0       pointing floor
  T_EXP / T_READ / T_SETTLE / T_FILTER   30 / 2 / 1 / 120 s
  V_ALT, A_ALT    3.5       deg/s, deg/s^2
  V_AZ,  A_AZ     7.0       deg/s, deg/s^2
  BANDS          ("g","r")
  CM             g 24.42  r 24.44
  KM             g 0.21   r 0.10
  MSKY_DARK      g 22.26  r 21.20
  SEEING_ZENITH   0.70     arcsec, scaled by X^0.6
  VISITS_PER_SET  2        one g AND one r = one request set

assets/gen_sched.py
  SEED          1717       the night (Fibonacci-sphere field placement)
  N_SETS         450       request sets -> the night is oversubscribed
  TIME_LIMIT     120.0 s   HiGHS budget; it does NOT close (see FACTCHECK F13)
  REL_GAP        1e-3
  BONUSES       (0.0, 0.25, 0.5, 1.0, 2.0, 5.0, 20.0)
  TOUR_BLOCK       8       the mid-night block drawn in tour.png
  plate size   1560 x 780 px, all five
```

Reproduce with:

```
python -I assets/gen_sched.py
```

It prints six claims, asserts each, and writes **nothing** if any fails.

## Solver

`scipy.optimize.milp` → **HiGHS**, which ships with SciPy. Free, no licence,
no key. ZTF's published implementation uses Gurobi; this does not, and the
difference is recorded in `SOURCES.md` under "What is MINE, not theirs."

## One knob that exists in no paper

`run_greedy(..., finish_bonus=…)` multiplies the score of any field already
holding one half of its pair. It is mine, and it exists so B09 can **attack
this episode's own claim** with a measurement instead of conceding or
ignoring the obvious objection. See FACTCHECK F12.

## Fonts

EB Garamond (bundled, `runtime/fonts/EB_Garamond`). No glyph outside the
font's coverage is used — the reel spells out `ALLOWED` / `FORBIDDEN` and uses
a struck row rather than tick or cross marks, because EB Garamond has no check
character and Ep. 09 rendered one as stray digits on screen.
