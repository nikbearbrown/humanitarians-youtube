# PROMPT — "How Pitch Correction Works"

The brief, and how each constraint was resolved.

## Constraints given

Rohan, 2026-10-05:

> i forgot to submit the videos last friday. its now monday. lets make one update video about
> what we did, the full setup guide, and one video about any stem topic. and then as usual we
> need to update all docs and everything as per the latest requirements. frictional log, hours,
> etc etc. all the new things that we need to conform to.

Asked to pick the topic from four (text-to-speech, recommended; pitch correction; beat
detection; voice cloning), he chose **pitch correction**.

## How each constraint was resolved

| Constraint | Resolution |
|---|---|
| Any STEM topic | Pitch correction: audio, and directly useful to Lyrical Literacy fellows who sing over Suno tracks |
| Latest Brutalist | `git fetch` + merge of three upstream commits before building (BUILD-LOG §1) |
| Required opening line, AI disclosure | B00, verbatim; disclosure on screen |
| Executable evidence | `pitch_demo.py` does the detection, correction and re-measurement; every number is the run's |
| Typeset math | B03's rule and worked example through `typeset_math.py` |
| 4K, both aspects, native 9:16 | 3840×2160 and 2160×3840; every scene has its own phone layout |
| No surname | narration "Row-Haan", on screen "Rohan V." |
| Late submission | stated in README, FRICTIONAL and the email; the folder keeps the week's date |
