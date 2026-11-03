# FACTCHECK.md -- claude-liam-sers-transformer-fix

Verified directly against the two source texts provided for this video: the
original team draft of Section 4.2 (Transformer Architectures) and the
current, revised version. Two claims about external studies (Wang et al.
and Sineesh & Kamsali) are verified against the author's own documented
edit summary, not independently re-checked against the primary papers
themselves -- this is noted explicitly below rather than implied as
independently confirmed.

## Claims verified directly against the two draft texts

**1. "The original draft summarized three transformer studies and offered
no closing recommendation."**
Status: SUPPORTED. The original text (as provided) ends immediately after
describing Hajikhani et al.'s SERSFormer-2.0 and the computational-cost
tradeoff paragraph -- there is no sentence anywhere in the original that
states when a transformer should actually be chosen over a CNN. The
current version adds an explicit closing paragraph doing exactly this
("the case for using a transformer architecture in SERS-ML rests more on
architectural fit...").

**2. "The original draft stated Wang et al.'s 100% identification rate
with no context on what it meant."**
Status: SUPPORTED. The original text reads: "reporting 100% positive
identification rate in the tested conditions [U-49]" -- no elaboration on
what "tested conditions" means follows anywhere in the original.

**3. "The original draft never addressed whether a transformer actually
outperforms a CNN on comparable SERS data."**
Status: SUPPORTED. The original text lists three transformer studies
(Wang et al., Zhang et al./TMNet, Hajikhani et al.) with no mention, in
any form, of a direct comparison against CNN performance on the same
data. The current version adds this observation explicitly, twice, and
then closes it with the Sineesh & Kamsali citation.

## Claims verified against the author's own edit documentation only

**4. "Wang et al.'s 100% figure was obtained on a validation set of 75
spectra, under two laser power levels and a narrow range of integration
times."**
Status: Reported by the author as confirmed by going back to the Wang et
al. source paper directly. Not independently re-verified against that
paper by this fact-check. Flagged here as author-reported, not
independently confirmed.

**5. "Sineesh & Kamsali (2026), published in *Digital Discovery*, directly
compared five deep learning architectures including a transformer on
Raman spectral classification, with the transformer finishing last, more
than five percentage points behind the best model, and found a
validation-to-test generalization gap across multiple architectures."**
Status: Reported by the author as a real, peer-reviewed benchmark found
during the second revision pass. Not independently re-verified against
the published paper by this fact-check. Flagged here as author-reported,
not independently confirmed. The video explicitly states this benchmark
uses general Raman data, not SERS-specific data -- this scoping caveat is
carried through faithfully from the author's own description and is
repeated on screen (B05's caveat line) rather than omitted.

## Summary

Three claims about the actual difference between the original and current
draft (items 1-3) are independently verifiable by comparing the two texts
directly, and check out. Two claims about the content of external sources
cited within the revision (items 4-5) rely on the author's own account of
having gone back to those sources -- this fact-check did not re-locate and
re-read those primary papers itself, and says so plainly rather than
implying a level of verification that didn't happen.
