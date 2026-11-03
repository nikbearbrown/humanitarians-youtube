# PEDAGOGY.md — The Variable That Vanished (GATE P)

**Reel:** `hai-the-variable-that-vanished` · 26 beats · Bella (`af_bella`) · Humanitarians AI
**Source:** a notebook on SES → health causality (45 cells).
**Target:** ~6 minutes.

---

## 1. The thesis

The notebook's statistics are correct and its data preparation is careful. The failure is
that it never names its **estimand**, so the adjusted model silently answers a different
question than the title asks — and a structural zero gets reported as "a smaller effect."

## 2. How every number was obtained

`build_beat_sheet.py` re-runs the notebook's data-generating process verbatim at
`np.random.seed(42)`, refits both models, and **asserts** the values the narration speaks.
If the reproduction ever drifts, the build fails rather than the video going stale.

```
edu total   = 6.202 points/level      adj = +0.047 (p = 0.821)
income      naive 0.000353 → adj 0.000143   true 0.00015
dead edge   signal 0.000506 vs noise 0.05   ratio 99×   r = +0.0821
```

## 3. The three findings

**① Over-adjustment on the headline variable.** In the generator, `Education` does not
appear in the `health_score` equation at all — its entire influence is carried by income,
environment, diet, exercise, smoking and access. The causal-aware model adjusts for all of
them, so education's coefficient collapses from a true total effect of **6.20** to
**+0.047, p = 0.821**. The notebook reads this as "*Income and Education still help, but
their direct effects are smaller*." It is not smaller; it is zero by construction, and it
was guaranteed before any data existed.

**② A causal edge that exists only in prose.** `access = 0.2 + 0.00000001 * income + ...`
At mean income (~50,600) that term contributes **0.000506**, against noise with SD **0.05**
— about **99× larger**. The DAG and the code comment both assert income → access; the
simulated data contains essentially none of it.

**③ The notebook cannot run top to bottom.** Cell 24 reads `df_clean`; cell 27 creates it.
A fresh kernel raises `NameError`.

## 4. Where the reel gives credit, deliberately

This is a critical video, so the fair parts are stated explicitly rather than buried:

- **B01** affirms the premise — asking whether SES→health is causal is the right question.
- **B12–B13** show the same adjustment *working* on income: naive `0.000353` → adjusted
  `0.000143` against a true `0.00015`. Education genuinely confounds income, and adjusting
  for it genuinely recovers the parameter.
- **B14** states the actual lesson: the technique is sound, and what a control does depends
  entirely on where it sits in the graph.

The reel never says the notebook is bad, and never says the author is careless.

## 5. Limits of this critique

- The analysis is of the **simulated** dataset only. Nothing here speaks to real SES/health
  epidemiology, and the reel does not claim otherwise.
- Because the data is simulated, "true effect" means *true in the generator*. That is a
  strong claim inside the notebook and no claim at all outside it.
- The reel does not re-run the missingness or imputation path (cells 16–27). Those could
  shift the third decimal; they cannot move a 6.20 to a 0.047.
- `IdxStatement` and `ClaudeCodeBeat` are reused from earlier reels; the eight `Causal*`
  scenes are new.

## 6. Verdict

```
VERDICT: PENDING — awaiting human sign-off.
```

Audio was generated with `--no-gate`, on the record. GATE P is a human signature and
Claude must not forge one. This reel criticises a specific piece of work: read §3 against
the notebook and §4 for fairness, then replace this block with `VERDICT: PASS` and a date.
