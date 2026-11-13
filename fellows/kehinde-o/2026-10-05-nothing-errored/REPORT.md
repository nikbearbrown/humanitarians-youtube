# Explainer — Nothing Errored

**Week:** 5 Oct 2026
**Type:** STEM / AI explainer

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp (`Medhavy_Kehinde/STEM Topic/nothing-errored/`)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)

## What it covers

How you find out that a working model has quietly stopped working, built on my own
loom repo and a simulated year of production: drift detection by population
stability index, and a canary gate that makes a replacement earn the swap on live
traffic.

## Why this topic, this week

It argues the same thing as the Chapter 6 report from the other side. There, a
citation link resolved perfectly and still failed, because the fact behind it was
not readable. Here, a model answers every request and is wrong, because the world
it was trained on moved. In both cases the surface check passes and the thing you
care about has failed.

## Limits

- The year is simulated on synthetic caregiver logs. It is not a clinical system,
  it is not deployed, and the video makes no claim about real patients.
- No claim that this platform competes with managed MLOps tooling. The measured
  claim is what the run did.
- Whether these thresholds hold on real traffic is not something this project
  shows.
- Figures come from the repo's committed run record rather than its README, which
  is stale on one figure.
