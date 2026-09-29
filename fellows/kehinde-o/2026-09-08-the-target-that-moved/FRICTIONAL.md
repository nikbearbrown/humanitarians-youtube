# Frictional Log -- The Target That Moved

**Date:** September 8, 2026
**Fellow:** Kehinde Obidele
**Work:** Brutalist video (STEM/AI explainer, Week 2)

## What I set out to do

Produce a STEM/AI explainer video for Week 2, built on my own deep Q-learning agent for LunarLander. The title "The Target That Moved" is literal: the agent computes its learning target using the same network it is updating, so the target moves every time it learns. The video is about why that made a trained model score worse than random, and why the fix is a frozen target network rather than more training.

## What I expected

I expected the Brutalist workflow to be smoother this time, having completed one
video already. On the content side I expected to present a working agent and
explain how deep Q-learning works.

## Where it resisted

The agent did not work, and I only found out how badly by measuring it properly.
Over 100 fresh episodes with exploration turned off, the trained model scored a
mean reward of -391. A policy that picks a thruster at random scores -213 on the
same environment. The trained network was nearly twice as bad as guessing. On its
own -391 just looks like a low score; it means nothing until the random baseline
sits beside it.

My first instinct was that it needed more training. It did not. The agent computes
its learning target using the same network it is updating, so every update moves
the target it is aiming at. More steps do not converge on a target that keeps
running away.

On production, the 9:16 render needed thinking about differently. Content that
works in landscape does not always read the same in portrait, especially
text-heavy frames, and the fix is to re-lay it out rather than to crop in.

## What I did next

I rebuilt the video around the failure rather than around the algorithm. The
honest version is not "here is how deep Q-learning works" but "here is a bug that
looks exactly like undertraining and is not". The fix is a frozen copy of the
network supplying the target, which is a small change I had left out.

I adjusted the visual descriptions in the beat sheet so the portrait cut is a
re-layout rather than a crop.

## What Claude or another person contributed

Claude helped structure the beat sheet and pressed for the measured comparison to
be shown on screen rather than described. The agent, the failure, the random-policy
baseline and the diagnosis are mine.

## What I accepted, changed, or rejected

I accepted opening the video by admitting the model was worse than random; it is
the strongest thing in it. I rejected the original framing that would have
presented a working result, because that is not what happened.

## Result

Week 2 STEM/AI explainer completed. Both aspect ratios rendered. Uploaded to
Google Drive, source files committed to GitHub. The video reports the diagnosis
rather than a repaired result: I did not retrain to convergence with the target
network in place.
