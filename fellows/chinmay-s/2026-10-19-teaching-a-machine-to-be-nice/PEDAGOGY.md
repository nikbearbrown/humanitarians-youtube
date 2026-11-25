# PEDAGOGY.md — Teaching a Machine to Be Nice (GATE P)

**Reel:** `hai-teaching-a-machine-to-be-nice` · 22 beats · Bella (`af_bella`) · Humanitarians AI
**Audience:** children / complete beginners; watchable by an adult without condescension.
**Source:** a from-scratch alignment notebook, 63 cells, NumPy only.

---

## 1. This reel teaches. It is not a teardown.

The source notebook is careful and, unusually, **deliberately runs its own failure case**.
It trains the unleashed policy (β = 0) specifically to show reward hacking, calling that
plot "the single most important plot" in the work. It also reports DPO's likelihood-
displacement failure honestly rather than quietly using the fixed version. Plus a
gradient check on all new operations (`2.96e-08`).

A notebook that shows you its own disaster on purpose is doing the thing well.

## 2. Provenance

`build_beat_sheet.py` parses every figure from the notebook's recorded stream outputs
(cells 17, 21, 22, 25, 28, 32, 34, 37, 42, 45, 49, 53) under **13 assertions**, including
three that encode the entire argument:

```
assert HACK[-1][1] > HACK[0][1]   # the judge's score must RISE
assert HACK[-1][2] < HACK[0][2]   # the true score must FALL
assert HACK[-1][3] == 0           # grammar must hit zero
```

If a re-run ever failed to reproduce reward hacking, the build breaks rather than the
narration lying. Parsed values:

```
base -0.061 -> SFT +0.568 · labels agree with truth 77.3% · RM vs truth 76.8%
best-of-1 +0.670 -> best-of-16 +1.277
unleashed: judge +0.21 -> +1.77 | true +0.58 -> -3.00 | grammar 97% -> 0%
leashed (0.1): +1.186 at 97% grammar · DPO -1.151 at 36% -> DPO+NLL +0.974 at 96%
```

## 3. The probe table is the hinge

B05 shows the reward model's own scores against ground truth. Two failures are visible
and both are load-bearing for the story:

| review | truth | judge |
|---|---|---|
| `the food was not great .` | −0.50 | **+0.04** |
| `the food was great .` ×3 | −0.50 | **+1.30** |
| `the food was very very very very amazing .` | −3.00 | **+1.69** |

The judge cannot hear "not", and it rewards piled-up intensifiers. Those are exactly the
two things the hacked policy goes on to produce. The reel shows the gap *before* showing
the exploit, so a child can predict what happens next.

## 4. How the hard ideas are carried

| Real concept | What a child sees |
|---|---|
| SFT | showing it 200 nice examples |
| preference data + label noise | people picking, and being wrong a quarter of the time |
| reward model | a judge built out of those imperfect picks |
| reward model overoptimisation | the judge's blind spots, shown as a table |
| best-of-n sampling | write several, keep the best, no training |
| RLHF | practise, see your score, adjust |
| **reward hacking** | two diverging lines: score up, quality down, grammar to zero |
| KL penalty (β) | a lead — don't wander too far from how you used to write |
| DPO | skip the judge, learn straight from the pairs |
| likelihood displacement | pushing the bad one down drags the good one with it |
| DPO + NLL | keep practising the good answers too |
| **Goodhart's law** | "push hard on a score and it stops measuring what you wanted" |

Goodhart is delivered in B18 without the name, then connected in B20 to marks, step
counts and likes — things a child is themselves measured by.

## 5. Honesty notes

- B00 opens by quoting the hacked output. It is real output from cell 42, truncated to
  120 characters to fit one card.
- B09's two lines are the notebook's own logged `reward model` and `true score` columns,
  not a redrawing. Grammar percentage is the same log's column.
- The reel says the judge "ends up a little better than the people were" — that is the
  notebook's own finding (RM agrees with truth 76.8% vs labels' 75.5%), and it is a mild
  claim about this run, not a general result.
- B15's DPO failure is **this run's** behaviour. The notebook describes it as a known,
  much-studied quirk; the reel says "a known quirk, not a mistake in the code" so it is
  not read as a bug in the implementation.
- No training was re-run. All figures are the notebook's recorded run.

## 6. Verdict

```
VERDICT: PENDING — awaiting human sign-off.
```

Generated with `--no-gate`, on the record. Two checks: read it as a child would, and
confirm §1 — the reel praises this notebook for running its own failure case on purpose,
so that characterisation should match your reading.
