# FACTCHECK — vox-missing-mnar

Source: `computational-skepticism-for-ai/chapters/05-data-validation-reconstructing-the-epistemic-frame-behind-a-dataset.md`

## Terms table

| Term | Definition used in video | Chapter reference |
|---|---|---|
| MNAR (Missing Not At Random) | Missingness probability depends on the value itself — high earners less likely to report income | Line 135 |
| MCAR | Missing completely at random — probability independent of observed and unobserved data | Line 131 |
| MAR | Missing at random — depends on observed variables but not the missing value itself | Line 133 |
| Imputation bias | Standard imputation of MNAR data produces estimates biased in the direction of the missing values | Line 135 |
| MNAR detection | Requires reasoning about why values would be absent — not detectable by standard EDA from within the data | Lines 135, 287 |

## Claim-by-claim check

| Beat | Claim | Chapter support | Status |
|---|---|---|---|
| B02 | High earners don't report income; imputing from visible produces systematically low distribution | Line 135: "High earners are less likely to report their income...MNAR is the hard case — standard imputation produces biased estimates" | PASS |
| B04 | Three types of missing data: MCAR, MAR, MNAR | Lines 131, 133, 135 | PASS |
| B05 | MNAR looks like other types from inside the dataset | Lines 135, 287 | PASS |
| B07 | Imputing MNAR with visible mean/median bakes in bias; more data = more confidently wrong | Line 135: "the bias is exactly in the direction you cannot measure" | PASS |
| B08 | Quote (condensed) | Line 135: exact | PASS |
| B09 | Standard EDA does not detect MNAR; requires reasoning outside the data | Lines 135, 287: "Standard EDA does not detect MNAR; you detect it by thinking carefully about who would not report this value and why." | PASS |
| B10 | Quote verbatim | Line 135: exact | PASS |
| B11 | Ask not how many but why; imputing from visible = permanently baked bias | Lines 135, 287 | PASS |

## B12 — THE EXAMPLE beat (illustrative)

| Claim | Status |
|---|---|
| Clinical trial: 200 patients, 43 drop out before final measurement | illustrative — made-up scenario |
| Dropouts primarily had severe side effects in week 2 | illustrative |
| Completers show avg 4.2-pt pain reduction | illustrative |
| Imputing from completers produces too-optimistic result | mechanism-accurate (line 135) |
| Worst responders are missing — MNAR mechanism | mechanism-accurate (line 135) |

All specific numbers (200, 43, 4.2) are invented and illustrative. The mechanism (MNAR: missing because of value) is chapter-accurate.

## VERDICT: PASS
