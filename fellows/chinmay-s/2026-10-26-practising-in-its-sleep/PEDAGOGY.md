# PEDAGOGY.md — Practising In Its Sleep (GATE P)

**Reel:** `hai-practising-in-its-sleep` · 18 beats · Bella (`af_bella`) · Humanitarians AI
**Audience:** children / complete beginners; watchable by an adult without condescension.
**Source:** a from-scratch World Models notebook, 51 cells, NumPy only.

---

## 1. This reel teaches.

The notebook builds a VAE, a memory network and a controller evolved **entirely inside
the model's own dream**, on a 16×16 Catch game — and then tests whether that controller
works in the real game. It is careful work: it states its baselines first, probes whether
information survives compression, and compares against a cheat that sees the true state.

## 2. The argument, and the assertions that protect it

Three of the nine guards encode the reel's claims, so a re-run that failed to reproduce
them breaks the build instead of letting the narration lie:

```python
assert NN_R2 > 0.9 > LIN_R2       # the ball IS still in the 8 numbers, just not linearly
assert Z_MEM > Z_ONLY * 1.5       # memory must roughly double the catch rate
assert Z_MEM > GREEDY             # the dreamer must beat the sighted cheat
```

Parsed values:

```
baselines   random 28.1% · greedy chaser 60.8% · oracle 100.0%
VAE         256 pixels -> 8 numbers (32x), 99.3% rebuilt with every square correct
probe       ball x: linear R² 0.19, nearest-neighbour R² 1.00
dream       picture only 39.2% · picture + memory 78.5% · after one loop 83.5%
planning    8 plans 71% · 24 plans 82% · 64 plans 83%
```

## 3. The pedagogical spine

The reel is built around one idea a child can feel, introduced before any machinery:
**a single frame cannot show motion.** B03 shows one frame, then two futures that are
equally consistent with it. Everything afterwards — why memory is needed, why the
memory-equipped player doubles the score, why it beats a cheat with perfect eyesight —
is a consequence of that one observation.

The closing beat turns it back on the viewer: catching a ball yourself uses the same
trick, because your eyes also only deliver snapshots.

## 4. How the hard ideas are carried

| Real concept | What a child sees |
|---|---|
| partial observability | one frame, two possible futures |
| VAE / latent compression | squeezing 256 squares into 8 numbers and back |
| latent probing (linear vs kNN R²) | "hidden, but not lost — just not in a tidy order" |
| MDN-RNN next-state prediction | a memory whose only job is guessing the next picture |
| dreaming / rollout in latent space | feeding its own guesses back in, playing a game that isn't there |
| training a controller in the model | practising with the real game switched off |
| the value of recurrent state | same practice, memory nearly doubles the score |
| MPC | imagine several plans, pick the best |
| the data-collection loop | better play → better experience → better dream |

No equations on screen. "Latent", "VAE", "rollout" and "model-based" never appear in the
narration.

## 5. Honesty notes

- Figures come from the notebook's **final summary board** (cell 45), not the per-run logs,
  so they are internally consistent. The training logs show slightly different end-of-run
  values (e.g. 39.5% / 75.7%) because those are single evaluations; the board's 39.2% /
  78.5% are the notebook's own reported summary.
- The game boards in the animation are drawn parametrically. The *dynamics* shown (a ball
  falling with horizontal drift, a 3-wide paddle) match the notebook's game; the specific
  frames are not a replay of its arrays.
- B10 calls the greedy chaser a "cheat" because it reads the true ball position rather
  than pixels. That is the notebook's own framing of it as a privileged baseline.
- No training was re-run. All figures are the notebook's recorded run.

## 6. A process change in this build

Twice in this series a dense scene shipped with narration too short to read it. The build
script now **audits that itself**: any scene in the `DENSE` set with under 12 seconds of
projected narration fails the build. This run reports `[audit] all dense scenes >= 12.0s`.

The same build also caught a parsing bug of mine: `"greedy chaser (sees the true ball, no
memory)"` contains the word "memory", so a loose selector picked the wrong row. The
`Z_MEM > GREEDY` assertion failed with `(60.8, 60.8)` and surfaced it immediately.

## 7. Verdict

```
VERDICT: PENDING — awaiting human sign-off.
```

Generated with `--no-gate`, on the record.
