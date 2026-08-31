# REPLACE LOG — slots needing better media

**Empty. All three entries below were RESOLVED, not replaced.**

An earlier compile logged B05, B07 and B10 here because their clips were being
slowed 3.2–3.3× to fill their beats:

    B05: clip  9.0s slowed 3.3x into 29.7s beat — extreme slow-mo
    B07: clip  7.9s slowed 3.2x into 24.9s beat — extreme slow-mo
    B10: clip 10.4s slowed 3.3x into 34.0s beat — extreme slow-mo

The cause was not bad media. The scenes were simply paced for a shorter beat than
the measured narration, so `compile.py` was stretching them. Fixed at the source
with the `Paced` base class in `scenes.py` — see `BUILD-LOG.md` § "The defect
GATE V could not see". Every slot now lands within 0.05 s of its beat and the
compiler reports no fit factor at all, in either aspect.

Nothing here needs a pantry replacement.
