# Explainer — Every Reading Said Fine

**Week:** 13 Oct 2026
**Type:** STEM / AI explainer

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1YZ3bLjWZ74sSdhdx4vC9X8MTLOykNk_6?usp=drive_link (`Medhavy_Kehinde/STEM Topic/every-reading-said-fine/`)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)

## What it covers

One idea: a threshold that is correct on every individual reading can still miss a
patient who is deteriorating, because deterioration lives in the trend and a threshold
only ever sees the instant.

The worked example is my own streaming pipeline,
`github.com/Kenny0bi/real-time-vitals-pipeline`. Twelve synthetic patients, one reading
per second, each scored with the Modified Early Warning Score: five parameters, 0 to 3
points each, five or more means immediate clinical review.

Over 1,800 generated readings for a patient whose oxygen saturation fell from 98 to 80,
a drop of eighteen points:

- 1,117 readings, 62.1 percent, still scored two or below
- 24 readings, 1.3 percent, crossed the immediate-review threshold
- the peak score reached 6

The threshold was not broken. It fired correctly, 24 times, on a patient who had been
sliding for most of an hour. The answer in the project is not a lower threshold, which
buys false alarms, but two rules that watch the patient against themselves: a Shewhart
rule at three standard deviations from that patient's own rolling mean, and a sustained
drift rule on five or more consecutive readings moving one way.

Every number in the video was computed by running the repo's own simulator and scorer
in this session at seed 42, not read off its README.

## Why this topic, this week

It pairs with the Chapter 9 audit. Both are about the same failure: a check that is
correct on each item in isolation and still misses the thing you care about. The
textbook pipeline flagged 145 sentences and 30 carried checkable assertions. The warning
score fired on 24 readings out of 1,800 and the patient was deteriorating through nearly
all of them. Threshold logic in both cases, and the same blind spot.

## Limits

- Every patient is synthetic. There is no real patient data anywhere in the project,
  and the video says so on screen, not only in the description.
- This is not a medical device, not deployed, and not evidence that this would catch a
  real deterioration earlier than a clinician would.
- The 62.1 percent figure is one patient at one seed. It demonstrates the shape of the
  problem; it is not an estimate of how often MEWS misses deterioration in practice.
- MEWS is a published and validated score. The video is not an argument that it is bad.
  It is an argument that a point-in-time score and a trend detector answer different
  questions.
- The anomaly rules are demonstrated on simulated deterioration, where I know the ground
  truth because I generated it. That is the easy case.
