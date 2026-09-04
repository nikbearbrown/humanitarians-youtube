# NARRATION-GATE-P — stale-ecg

**GATE P — narration sign-off.** Every narration line, reviewed against the
source before the reel is called done.

| | |
|---|---|
| Reel | *A Stale ECG Is Worse Than No ECG* |
| Skill / register | cli-explainer · Pragmatist (HAI) |
| Voice | Kokoro `af_bella` (Bella), local, free |
| Locked runtime | 16:9 — 4:18 (258.01s) · 9:16 — 2:34 (154.09s) |
| Source | `mimic-research` — `results/results.json`, `results/within_patient.json`, `README.md`, `PAPER.md` |
| **Status** | **PENDING — awaiting Dhruvi Shah** |

> GATE P is a human signature. The rows below are an agent's review, prepared so
> the human review is fast — they are not the signature. Nothing here counts as
> approval.

---

## Per-beat narration review

Legend — **Claim**: does the line assert something checkable? **Traced**: does
that assertion resolve to source? **Register**: Pragmatist (method-forward, no
hype, states its own limits)?

| Beat | Claim | Traced | Register | Reviewer note |
|---|---|---|---|---|
| B00 | 0.8574 → 0.8595 | ✓ `results.json → overall` | ✓ | Question posed, not answered. Deliberate. |
| B01 | "+0.0021 over 144,668 admissions"; "hiding a sign flip" | ✓ `design.n_admissions`; sign flip verified against all four bins | ✓ | "Nobody ships a change that small" is rhetorical framing of a real number, not a claim about anyone's practice. |
| B02 | Patients recur → admission-level split leaks | ✓ `README` §Evaluation; `StratifiedGroupKFold` in `analyze.py` | ✓ | States the method before the result. |
| B03 | "correlated bins… a quantity you can put an interval on" | ✓ code shown computes contrast + slope in one replicate loop | ✓ | Describes exactly what the visible code does. No overstatement. |
| B04 | +0.0046 / −0.0048; both intervals clear zero; middle two underpowered | ✓ all four rows re-read from `by_staleness` | ✓ | **The load-bearing beat.** ~8s spent on "underpowered, not null". Non-monotonicity not raised — see below. |
| B05 | Case mix could produce the pattern | ✓ `README` §"more than a correlation" | ✓ | The reel raises the objection against itself before the viewer can. |
| B06 | "fit once, vary one input" | ✓ code shown reuses the fitted model across lags | ✓ | Reads the code's own comment honestly. |
| B07 | 40,764 / 16,157 / 1,262; +0.0056 → −0.0051 | ✓ `within_patient.json` | ⚠ | "The line crosses into negative territory somewhere around two weeks" — **interpolation between measured lags, not a measured crossing point.** Hedged with "somewhere around". Flagged for human judgement. |
| B08 | Train/deploy mismatch; reverse-training falsifier | ✓ `README` §"why it happens" | ✓ | Mechanism stated as mechanism, with its falsifier. |
| B08B | "did not clearly work… every interval crossed zero" | ✓ `within_patient.json → mitigations` | ✓ | Negative result retained. Was the easiest beat to cut and the most important to keep. |
| B09 | Handoff prompt | n/a | ✓ | Prompt is read aloud and motivated, per HANDOFF LAW. |
| B10 | Sign-off | n/a | ✓ | — |
| B10 (9:16) | "the full video removes the confound" | ✓ accurate description of what was cut | ✓ | Hand-written; replaced auto-stitched text. |

---

## Points requiring human judgement

1. **B07's "around two weeks."** The within-patient design measures four lags
   (0, 30, 180, 365 days → median ECG ages 0.2, 139, 334, 508 days). The
   zero-crossing is *interpolated* between the first two points, not measured.
   The narration hedges ("somewhere around"), and the chart draws a straight
   segment between measured points rather than a fitted curve. **Decide whether
   the hedge is enough or the phrase should go.**

2. **Non-monotonicity is not mentioned.** The 1–30 day bin's point estimate
   (+0.0053) sits nominally *above* the fresh bin (+0.0046) on 436 deaths.
   `README.md` addresses this directly and rests the decay claim on the
   continuous slope and the within-patient result instead. The reel handles it
   by marking the bin underpowered and saying the middle cannot be read — it
   does not explain the ordering. **Honest omission or gap?** Doing it properly
   costs ~20s.

3. **Register check.** Pragmatist was applied because @HumanitariansAI is
   Bella's channel. A methods paper suits it. If the intended audience is a
   general YouTube one rather than practitioners, Teardown (Liam, `am_onyx`)
   is the alternative — one metadata line, then regenerate audio and recompile
   both cuts, since every duration shifts.

---

## Standing checks

- [x] **No fabrication.** Every figure spoken or shown resolves to the source JSON. Three fabrication-class defects were caught and fixed during build — see `BUILD-LOG.md` §Corrections.
- [x] **No clinical advice.** The reel is about model evaluation. No beat tells anyone what to do with a patient. The word "should" appears in no beat about care.
- [x] **Credentialed data protected.** Aggregates only, consistent with the PhysioNet DUA. No patient-level data, no row-level records, no identifiers.
- [x] **Limits stated in-reel.** Underpowered bins labelled as such; the failed mitigation reported as a negative result; case-mix confound named before it is removed.
- [x] **TTS fidelity.** Narration verified by whisper round-trip — the voice says what the script means (`MIMIC-IV`, `AUROC` and bare decimals all rewritten after the probe showed them mangled).
- [x] **Captions match narration.** 85 cues (16:9) / 52 (9:16), word-aligned from the actual mp3s, 0 fallbacks.

---

## Signature

```
GATE P — narration approved for this cut

Reviewer:  ______________________     Date: __________

[ ] Approved as-is
[ ] Approved with the fixes noted below (requires audio regen + recompile)
[ ] Not approved

Notes:
```

**If any narration line changes, the audio for that beat must be regenerated and
both cuts recompiled** — narration is the master clock, so a wording change moves
every downstream beat. `SOURCES.md` and this file are updated in the same pass.
