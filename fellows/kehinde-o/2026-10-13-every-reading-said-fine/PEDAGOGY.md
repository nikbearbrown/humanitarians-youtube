# Pedagogy Review

## Topic
Every Reading Said Fine: why a deteriorating patient is invisible to any single
measurement (built on my own real-time-vitals-pipeline repo)

## Learning Objective
The viewer leaves understanding that a measurement carries no direction, so
checking a value one reading at a time cannot see a trend. They can apply the
"line up the last five" question to any number they monitor.

## Audience
General audience. No clinical or statistics background assumed. The warning score
is described as "points per parameter, added up" before any notation appears.

## The ONE Idea
A reading tells you where someone is. It cannot tell you which way they are going.
Over 1,800 readings of a real deterioration, 62 percent still scored as normal.

## Math Gate (docs/MATH-TYPESETTING.md)
B03 uses TypesetMath with two structured SVG rows, not formula strings:
- The warning score as a sum of per-parameter scores, with the score set shown
- The standard score (x minus the mean, over the standard deviation) with the
  flagging threshold

Algebra check: in row one, p is bound by the summation and each term is drawn from
a four-value set, which matches the published MEWS bands implemented in
`mews_calculator.py`. Row two is the ordinary z-score; the threshold of three
standard deviations is the Shewhart rule as implemented in `anomaly_detector.py`.

## Evidence Gate (docs/EXECUTABLE-EVIDENCE.md)
No figure is taken from the repo README. Every number was computed in this session
by importing the repo's own `VitalsSimulator` and `calculate_mews_from_dict` and
scoring 1,800 readings for one deteriorating patient at seed 42:
- SpO2 98 to 80, an 18 point fall
- 1,117 of 1,800 readings scored 2 or below, which is 62.1 percent
- 24 of 1,800 readings reached the immediate-review threshold, which is 1.3 percent
- Peak score 6; the test suite runs 101 passing tests, verified by running it

## Restraint Gate
- All patients are synthetic. The video says so on screen in the conditions line.
  No real patient data exists in this project and no clinical claim is made.
- This is not a medical device and the video does not present it as one.
- No claim that this would have caught a real deterioration earlier than a
  clinician. The measured claim is what the scores did on simulated data.
- A screenshot of the project's interface was considered for one beat and dropped,
  because at 1440px wide it would have needed a 2.7x upscale and the build
  requires 4K at source.

## VERDICT: PASS
