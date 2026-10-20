# PROMPT — "How Apps Find a Song's Tempo"

The brief, and how each constraint was resolved.

## Constraints given

Rohan, 2026-10-17:

> Its saturday. Build this weeks brutalist videos and submit. For progress, we started making good
> progress towards building a proof of concept for our video for homes of hope. … and for the other
> video, do a stem explainer. gie me suggestions and ill pick

Offered four topics (how apps find a song's BPM, recommended; why a dhol sounds like a dhol; how AI
singers pronounce words; how a key change lifts a chorus), he chose **BPM**. Then:

> test it on westerm groovers. no indian stuff.

Hours for the week: 20.

## How each constraint was resolved

| Constraint | Resolution |
|---|---|
| A STEM topic, his pick | tempo detection: onsets, autocorrelation, choosing the beat |
| Western grooves only | eight Western styles (rock, funk, house, hip hop, slow ballad, drum and bass, waltz, jazz swing); no Indian percussion anywhere in this reel |
| Latest Brutalist | merged 9 upstream commits (Remotion 4.0.535 / React 19) before building (BUILD-LOG §1) |
| Required opening line, AI disclosure | B00, verbatim; disclosure on screen |
| Executable evidence | `tempo.py` builds and tests the detector, cross-checked against librosa; every number is the run's |
| Typeset math | B03's autocorrelation and BPM rule through `typeset_math.py` |
| 4K, both aspects, native 9:16 | 3840×2160 and 2160×3840; every scene has its own phone layout |
| LOGO LAW (new this week) | librosa's own logo, downloaded with Rohan's approval, shown wherever librosa is named on screen |
| No recordings | all grooves synthetic (`grooves.py`) |
| No surname; no person icons | narration "Row-Haan", on screen "Rohan V."; no person appears; no researcher named on screen or in narration |
