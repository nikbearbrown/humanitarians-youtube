# Frictional log — Explainer: The Target That Moved

## 2026-09-08 — a model that was worse than random, and why

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp (`Medhavy_Kehinde/STEM Topic/the-target-that-moved/`)
- **Report:** [REPORT.md](REPORT.md)
- **Source project:** https://github.com/Kenny0bi/Deep-Q-learning-lunarlander
- **Paired report:** [Fact-Checking Chapter 2](../2026-09-08-chapter-2-review/)

**What I was working on.** An explainer built on my own deep Q-learning agent for
LunarLander, about why it failed and what fixed it.

**What I tried, and what I expected.**
- I expected to present a working agent and explain how Q-learning works.
- When it did not work, I expected the answer to be "needs more training".

**Where it resisted, and what I did next.**
- **The trained model was worse than random, and I only found out by measuring
  properly.** Over 100 fresh episodes with exploration off, the saved model scored
  a mean reward of -391. A policy that picks a thruster at random scores -213 on
  the same environment. Nearly twice as bad as guessing. Until I ran the random
  baseline I had no way to know that, because -391 on its own just looks like a
  low score.
- **More training would not have helped.** The agent computes its learning target
  using the same network it is updating, so every update moves the target it is
  aiming at. Freezing a copy of the network to supply the target is the fix, and
  it is a one-line change that I had left out.
- **This became the video.** The honest version is not "here is how DQN works" but
  "here is a bug that looks like undertraining and is not". That is more useful and
  it is what actually happened.
- The overview beat carried the same trigger-word bug as weeks 1 and 2; rebuilt
  later.

**What Claude contributed, and what I did with it.**
- Mine: the agent, the failure, the random-policy baseline, and the diagnosis.
- Claude's: the beat sheet, and pressing for the measured comparison to be on
  screen rather than described.
- Accepted: opening the video by admitting the model was worse than random. It is
  the strongest thing in it.
- Evidence: the repository above, and the evaluation numbers quoted in the beat
  sheet.

**What I understand now, and what I still do not.**
- Understood: a metric with no baseline is not a measurement. -391 meant nothing
  until -213 existed beside it.
- Understood: "train it longer" is the default explanation for a bad model and is
  often wrong. A diverging target does not converge with more steps.
- Not resolved: I did not retrain to convergence with the fix in place, so the
  video reports the diagnosis rather than a repaired result.
