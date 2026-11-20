# Pedagogy Review

## Topic
The Patients Who Left Early: censoring in survival analysis, measured on my own
synthetic cancer cohort where every patient's true survival time is known

## Learning Objective
A patient who leaves a study early is evidence, not missing data: they survived at
least that long. The viewer leaves understanding why dropping them makes survival look
worse, and how the Kaplan-Meier estimate keeps what they tell us.

## Audience
General audience. No statistics background assumed. Censoring is described by who it
is (people who moved away or were still alive when the study closed) before it is named.

## Key Findings Reported
Measured by running github.com/Kenny0bi/cancer-survival-prediction's own generator
(5,000 patients, seed 42), with a subclass that keeps each true event time and was first
proven to reproduce the repo's output exactly.
- 1,458 of 5,000 patients (29 percent) are censored.
- True median survival 51.4 months. Dropping the censored: 32.8. Counting them as deaths
  at censoring: 43.4. Kaplan-Meier: 51.1.
- Of the 425 censored before five years, 286 were truly alive at five years.

## Accuracy Gate
See FACTCHECK.md. The Kaplan-Meier implementation was checked against a hand-computed
example before use; the equation on screen is the product-limit form it implements.

## Restraint Gate
- Synthetic patients only. No real patient data is used anywhere.
- Kaplan-Meier assumes censoring is independent of outcome. That holds here by
  construction (study close and random dropout); the video does not claim it always holds.
- The link to the textbook work is an analogy of lesson, not a technical equivalence.
- The narration is an AI voice. The outro says so on screen.

## Takeaway
When a number is averaged over people, ask who was left out because they had not
finished yet, and which way leaving them out pushed the number.

## VERDICT: PASS
