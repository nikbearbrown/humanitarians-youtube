# PEDAGOGY AUDIT — vox-missing-mnar

## Act structure check

| Required act | Present | Beat(s) |
|---|---|---|
| COLD OPEN (concrete case, no thesis) | YES | B01–B02 |
| THE QUESTION (on screen AND narration) | YES | B03 |
| THE PROBLEM | YES | B04–B05 |
| THE MECHANISM | YES | B06–B08 |
| THE IMPLICATION | YES | B09–B11 |
| THE EXAMPLE (16:9 full cut, right before RECAP) | YES | B12 |
| RECAP endcard (question→answer + topic) | YES | B13 |

## Question on screen check
B03 card copy: "If the missing data is missing because of what it contains — how do you detect it?"
B03 narration: "If you can only see the data that's present — and the missing data is missing precisely because of what it contains — how do you detect a bias you can't see from inside the data?"
Both on screen (card) and in narration. ✓

## Concrete case before thesis
B02 introduces the income survey scenario (high earners don't report → imputed distribution too low) before explaining MCAR/MAR/MNAR taxonomy. ✓

## Exclusions honored
- No formal MCAR/MAR definition in detail (mentioned but not formalized)
- No imputation-method catalog
- No missingno tooling
- No join-failure case

## THE EXAMPLE beat (B12)
B12 presents a clinical trial (pain medication, 200 patients): 43 patients drop out after severe side effects in week 2. Completers show avg 4.2-pt pain reduction — but the worst responders are missing. Imputing from completers produces a systematically too-optimistic result. All numbers illustrative, labeled in FACTCHECK.md. Different domain from the income survey cold open. ✓

## Topic check
B01 scene: "COMPUTATIONAL SKEPTICISM" eyebrow (TEAL text, DISPLAY font) ✓
B13 endcard card.topic: "COMPUTATIONAL SKEPTICISM" — no book title, no chapter number on screen ✓
B13 narration: no book title or chapter number ✓

## Length check
Estimated total: ~183s ≈ 3:03. Within 5:00 cap. ✓

## Concepts derived from source
"Missing not at random (MNAR): The probability of being missing depends on the value itself. High earners are less likely to report their income...MNAR is the hard case — standard imputation produces biased estimates, and the bias is exactly in the direction you cannot measure. Standard EDA does not detect MNAR; you detect it by thinking carefully about who would not report this value and why." (line 135). ✓

VERDICT: PASS
