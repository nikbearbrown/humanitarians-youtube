# SOURCES — stale-ecg

Every figure spoken or shown in this reel traces to a file in this repository.
No number on screen was estimated, rounded for effect, or carried over from
memory. Where the source file and the write-up disagreed, the disagreement is
logged below with the resolution.

## Primary sources

| Source | Used for |
|---|---|
| `results/results.json` | B00 headline AUROCs, B01 aggregate split, B04 all four bins + CIs + MDE |
| `results/within_patient.json` | B07 within-patient points + CIs, B08B both mitigation contrasts |
| `README.md` | framing, mechanism narrative, decay-test phrasing |
| `src/analyze.py` | B03 code beat — `cluster_bootstrap()`, verbatim |
| `src/within_patient.py` | B06 code beat — `oof_cross_lag()`, verbatim |

## ACTUAL-CODE LAW — what the code beats show

Both CODE beats show real source, trimmed only by deleting lines, never by
rewriting them. No pseudocode, no prose restyled as code. The inline comment
shown in B06 ("Reusing the fitted object is what makes this a clean ablation")
is the author's own comment from the file, not narration dressed up as one.

## DOUBLE-CHECK LAW — corrections made during the build

**1. Bootstrap p-value.** `results.json` stores
`decay_test.bootstrap_p_no_decay: 0.0`. A p-value of exactly zero is not a
reportable quantity: with 1,000 replicates and zero exceedances the correct
statement is `p < 0.001`. `README.md` already says `p < 0.001`. The reel uses
the README's phrasing. *(Worth fixing at the source — the JSON writer should
emit `<1/N` rather than `0.0`.)*

**2. Mitigation intervals — a fabrication caught before render.** The first
draft of `EcgVerdictPanel` carried confidence bounds for the "tell the model
the ECG's age" remedy that were inferred from the README's range of point
estimates (+0.0007 to +0.0013) rather than read from the results file. That
range is a spread of point estimates ACROSS lags, not a confidence interval,
and using it as one would have invented precision that no bootstrap produced.
Replaced with the verbatim contrast at the stalest lag:

| Remedy | Contrast at lag 365 (median 508 d) | Source |
|---|---|---|
| Gap supplied as a feature | +0.0007 [−0.0019, +0.0031] | `within_patient.json` → `freshness_aware[3].aware_minus_blind` |
| Training age mix matched to deployment | +0.0032 [−0.0018, +0.0078] | `within_patient.json` → `training_mix_remedy[3].pooled_minus_freshtrained` |

Both cross zero. The panel is stamped INCONCLUSIVE — NOT SOLVED for this reason.

**3. Underpowered bins are never drawn as nulls.** `EcgStalenessBars` renders
the two middle bins hatched with an explicit "underpowered / no conclusion"
label, driven by the `powered_for_fresh_effect` flag already computed in
`analyze.py`. A bin whose interval spans zero because its MDE (0.0080, 0.0065)
exceeds the effect it would need to detect must not read as a measured null.
The narration states this rather than letting the shape imply a trend.

**4. Non-monotone bins not smoothed.** The 1–30 day bin sits nominally above
the fresh bin (+0.0053 vs +0.0046). The chart plots it as it is, and the
narration does not narrate a smooth decline across the four bars — the decay
claim rests on the continuous slope and the within-patient result, per the
README's own caution.

## Data use

MIMIC-IV and MIMIC-IV-ECG are credentialed PhysioNet resources under a Data Use
Agreement. Only aggregate results appear in this reel: cohort counts, AUROCs,
and bootstrap intervals. No patient-level record, waveform, identifier, date, or
row-level value appears in any frame or in the narration.

## TTS normalization (verified, not assumed)

Narration was probe-tested through Kokoro `af_bella` and transcribed back with
faster-whisper to confirm what the voice actually says. Three tokens failed and
are banned from narration text in this reel:

| Written | Spoken as | Written instead |
|---|---|---|
| `MIMIC-IV` | "Mimicroman 4" | avoided in speech; on screen only |
| `AUROC` | "OROC" | avoided in speech; on screen only |
| `0.8574` | digit string | "point eight five seven four" / "thousandths" |

`ECG` reads correctly and is used as-is.
