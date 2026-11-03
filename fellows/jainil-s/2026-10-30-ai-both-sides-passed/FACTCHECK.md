# FACTCHECK — Both Sides Passed

Every claim with its verdict. Rows citing the script are reproducible by
running `boundary_evidence.py`, which ships here.

| # | Beat | Claim as made | Verdict | Source |
|---|---|---|---|---|
| 1 | B02 | Producer emits 5,000 events and checks fields, types, positive timestamps; consumer runs the same kind of check on input | **VERIFIED** | Script construction, `in_stage_checks` |
| 2 | B02 | Both pass | **VERIFIED** | Script: in-stage checks return clean for 6 of 7 defects, and for the clean batch |
| 3 | B03 | Seven defects, all ordinary integration failures | **VERIFIED (constructed)** | Listed in the script. They are *chosen*, not sampled from incidents — stated as such in the reel and in `SOURCES.md` |
| 4 | B03 | Each stage's own checks catch exactly one of seven | **VERIFIED** | Script, 1/7 |
| 5 | B03 | The one caught is the string amount, because it changes a type | **VERIFIED** | Script: it is the only defect that alters a Python type; the type assertion fires |
| 6 | B03 | A boundary contract catches six | **VERIFIED** | Script, 6/7 |
| 7 | B03/B04 | Adding a shape profile catches all seven | **VERIFIED** | Script, 7/7 |
| 8 | B04 | A +5:30 shift is about 0.001% of an epoch-millisecond timestamp | **VERIFIED** | 19,800,000 / 1.76e12 = 0.0011% |
| 9 | B04 | The range check therefore waved it through | **VERIFIED** | Tolerance is ±0.1% on the median; the shift is ~100× smaller |
| 10 | B04 | The hour-of-day distribution moved, TVD 0.42 | **VERIFIED** | Script output for that defect |
| 11 | B05 | Google built a production data-validation system, described 2019, deployed in TFX, detecting anomalies in pipeline data including training/serving skew | **VERIFIED — PARAPHRASE** | Breck et al., SysML 2019. **Not a quotation.** See `SOURCES.md` for why |

## Claims considered and cut

| Claim | Why it was cut |
|---|---|
| Any real-world rate ("most pipeline bugs are like this") | The catalogue is constructed. There is no frequency result here |
| "Boundary checks catch everything" | 7/7 is against a catalogue written by the same person who wrote the checks. A defect nobody imagined is not in it, and the reel does not imply otherwise |
| "Petabytes per day", "hundreds of product teams" | Appear in secondary summaries of the Google paper. Not read in the paper, so not stated |
| Quotation marks around the B05 content | The abstract could not be obtained verbatim. The card is labelled as paraphrase instead |

## Changed during the build

**The shape check caught nothing on the first run, and the reason was my data,
not the method.** The first version generated timestamps uniformly across the
day. A timezone shift of a uniform distribution is still uniform, so the
hour-of-day profile was unchanged and the check scored 6/7 rather than 7/7. The
generator was corrected to give events a realistic daily rhythm — quiet
overnight, peak early afternoon — which is what real event streams have, and
the check then caught it with TVD 0.42.

This is worth stating plainly: the shape check is not magic. It works when the
data has a shape. The reel says that in the narration rather than presenting
7/7 as unconditional.
