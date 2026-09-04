# PEDAGOGY — A Stale ECG Is Worse Than No ECG

Narration sign-off record. What each beat teaches, why it sits where it sits,
and what a viewer can do afterwards that they could not do before.

**Source:** `mimic-research` (Dhruvi Shah) — `results/results.json`,
`results/within_patient.json`, `PAPER.md`, `README.md`.
**Register:** Pragmatist (HAI) — method, when it applies, when it does not.
**Voice:** Kokoro `af_bella`. **Channel:** @HumanitariansAI.

---

## The one thing

> **A model that consumes "whatever is on file" inherits the age of that file,
> and age is not in the feature vector.**

Everything else in the reel is scaffolding for that sentence. If a viewer
remembers nothing else, the reel worked.

---

## The teaching arc

| Beat | Move | What the viewer gains |
|---|---|---|
| B00 | Pose the question, land it answered | The honest-looking null: +0.0021. Sets up the trap |
| B01 | **Falsify the aggregate** | An average over heterogeneous conditions is a mixture, not a measurement |
| B02 | Name the method before showing it | Why patient-level resampling, not admission-level — leakage |
| B03 | Show the real loop | Correlated bins let you *test* a difference instead of eyeballing four intervals |
| B04 | The finding | Sign change: fresh helps, stale harms. Underpowered bins are labelled, not read |
| B05 | **Attack your own result** | Case mix is a live alternative explanation, and the reel says so before the viewer does |
| B06 | The ablation | Fit once, vary one input — the difference between a comparison and an experiment |
| B07 | The finding survives | Same patients, same labels; only ECG age varies. Confound removed |
| B08 | Mechanism + **negative result** | Train/deploy mismatch; and the obvious fix did not work |
| B09 | Transfer | A concrete procedure to run against the viewer's own model |
| B10 | Close | Where to go next |

**Framework before examples** ✓ (B02–B03 establish the method before B04 shows a
result). **Worked example** ✓ (B03/B06 are real source). **Falsifiability** ✓
(B05 names the confound; B08 reports the failed mitigation). **Scaffolded task**
✓ (B09 is a runnable procedure, not a slogan). **Bookends** ✓.

---

## Narration decisions, and why

**Numbers are spoken as words, printed as figures.** "Four and a half
thousandths" in the voice; `+0.0046` on screen. Verified necessary: a
whisper round-trip on a probe clip showed the voice reads `0.8574` as
"0, 8574", `MIMIC-IV` as "Mimicroman 4", and `AUROC` as "OROC". The
constraint is recorded in the beat sheet metadata so a future editor does not
reintroduce it.

**"Underpowered, not null" is said aloud, not just drawn.** The hatched bars
carry the visual signal, but the distinction is the single most misreadable
thing in the piece — a viewer who reads the 1–30 day bar as "also helps" has
learned something false. B04's narration spends ~8 seconds on it. The
non-monotonicity is deliberately *not* explained in the reel; it is in
`README.md` and would cost 20 seconds to do honestly.

**The revision is real, not staged.** B05's objection (case mix) is the actual
methodological reason the within-patient design exists in the source project.
The reel does not invent a strawman to knock down.

**The negative result is kept.** B08 could have ended on "and here is the fix."
There isn't one yet. Cutting that beat would make a better-feeling video and a
dishonest one.

**No clinical advice.** The reel never tells anyone what to do with a patient.
It is about model evaluation. The word "should" does not appear in any beat
about care.

---

## What is deliberately NOT taught

- **The waveform question.** These are report + measurement features, so the
  effect bounds ECG value from below. Stated in the source, cut from the reel
  for time — a viewer who wants it goes to `PAPER.md`.
- **The equity finding.** Medicaid 23.0% vs Private 16.8% stale-ECG exposure is
  a strong result and was scoped out to keep one finding, proven twice. It is
  the obvious candidate for a second reel.
- **Absolute effect size framing.** ~0.005 AUROC is small. The reel says the
  sign change is the finding, not the magnitude, but does not litigate clinical
  significance — that is beyond what the source claims.

---

## The 9:16 cut

Doctrine caps a Short at 3:00; the parent is 4:18. Dropped: B05–B07 (the
revision cycle), B08, B08B.

**Pedagogical cost, stated plainly:** the Short shows the sign change but *not*
the confound removal. A viewer who watches only the Short has seen a correlation
and been told it is one, with the outro pointing at the long for the design that
rules out case mix. That is an acceptable trade for the format — it is not an
equivalent artifact, and it is not represented as one.

---

## Sign-off

| Gate | State |
|---|---|
| Every claim traced to source | ✓ — `SOURCES.md` |
| Numbers verified against JSON, not prose | ✓ — four bins + decay test re-read from `results.json` |
| Corrections logged | ✓ — 5 defects, incl. 2 that survived an mp4 probe |
| Underpowered bins labelled, not read | ✓ — B01 and B04 |
| Negative result retained | ✓ — B08B |
| Credentialed data protected | ✓ — aggregates only, no row-level anything |
| **Human narration review** | ☐ **PENDING — Dhruvi Shah** |

The last row is not mine to tick.
