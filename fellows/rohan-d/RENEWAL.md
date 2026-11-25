# Renewal Request — Rohan D.

- **Role:** AI Engineer
- **Supervisor:** Nik Bear Brown
- **Current agreement:** 6 November — 30 November
- **Requested period:** 1 December — 31st January

> DRAFT. The figures below come from the build records in this repository. Replace the bracketed parts with your own facts; nothing here claims approvals or Drive links that were not recorded.

## What the current period produced

Two tasks this month: **(1) one video per week** and **(2) reviewing other fellows' videos.**

**Reviews of other fellows' videos: 32 videos reviewed over 7 review days** (9 Nov – 23 Nov), about 16 hours at 0.5 h per video, each logged with status, a GitHub check and review comments in the review log.

**Nine STEM and AI explainer films, each rendered in landscape (3840×2160) and native vertical (2160×3840).** Every figure on screen is recomputed in code, with a fact-check table per film.

- **A TL;DR on a paper:** *Why Attention Divides By The Square Root* (Vaswani et al., section 3.2.1), with a fact-check of 17 claims and a speech-to-text check of the narration.
- **Seven explainers in the format of the reference films:** cross-entropy, overfitting, momentum, convolution, embeddings, batch normalization and k-means, each built around worked numbers (for example overfitting: a line scores 0.074 on fresh points, a degree-7 curve 0.221; k-means: inertia 4 against 16 from two starts).
- **One more:** dropout (10,000 masks average 35.98 against 36).
- **Tooling work:** a local build chain on this Mac (Miniforge, Manim, Remotion, Kokoro), a standing rule that no review label or footer appears in any video, and a series resume file that records progress between sessions.
- **Checks:** every film passed frame QC (0 blockers, 0 majors) and the type-size check; each master carries a verification receipt.

### Evidence

| Week | Work | Drive | Commit | Log |
|---|---|---|---|---|
| [9–13 Nov](./2026-11-13-tldr-attention-scaling/) | Why Attention Divides By The Square Root | [folder](https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link) | [add commit] | [log](./2026-11-13-tldr-attention-scaling/FRICTIONAL.md) |
| [9–13 Nov](./2026-11-13-cross-entropy/) | Cross-Entropy, One Surprise at a Time | [folder](https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link) | [add commit] | [log](./2026-11-13-cross-entropy/FRICTIONAL.md) |
| [9–13 Nov](./2026-11-13-overfitting/) | Overfitting, One Memorized Point at a Time | [folder](https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link) | [add commit] | [log](./2026-11-13-overfitting/FRICTIONAL.md) |
| [16–20 Nov](./2026-11-20-momentum/) | Momentum, One Remembered Step at a Time | [folder](https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link) | [add commit] | [log](./2026-11-20-momentum/FRICTIONAL.md) |
| [16–20 Nov](./2026-11-20-convolution/) | Convolution, One Window at a Time | [folder](https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link) | [add commit] | [log](./2026-11-20-convolution/FRICTIONAL.md) |
| [16–20 Nov](./2026-11-20-embeddings/) | Embeddings, One Angle at a Time | [folder](https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link) | [add commit] | [log](./2026-11-20-embeddings/FRICTIONAL.md) |
| [23–27 Nov](./2026-11-27-batch-norm/) | Batch Normalization, One Rescale at a Time | [folder](https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link) | [add commit] | [log](./2026-11-27-batch-norm/FRICTIONAL.md) |
| [23–27 Nov](./2026-11-27-kmeans/) | K-Means, One Reassignment at a Time | [folder](https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link) | [add commit] | [log](./2026-11-27-kmeans/FRICTIONAL.md) |
| [23–27 Nov](./2026-11-27-dropout/) | Dropout, One Silenced Unit at a Time | [folder](https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link) | [add commit] | [log](./2026-11-27-dropout/FRICTIONAL.md) |

Weekly hours: about 20 per week across three weeks of November, about 60 in total ([HOURS.md](HOURS.md)). Weekly Frictional logs: one per work folder, listed in [README.md](README.md).

## Plan for the requested period

[Draft — edit to your real plan.]
1. The weekly project-update video required by the guide, with the opening line "Hi, I am [your name] and this video is about …".
2. A listening and timing review of the nine films, fixing delivery and pacing.
3. More explainers in the same format, with the Drive and GitHub submission done each week.

Reporting continues as it has: a dated Frictional log per work folder and a landscape and vertical render for each film.

## Open items I am carrying

- Narration delivery and animation timing are not yet judged by ear on any film.
- The required opening line ("Hi, I am Rohan, and this video is about machine learning.") is recorded here but not yet spoken in the nine films.
- Drive links and commit links are not yet added. Hours are in [HOURS.md](HOURS.md) and in the Word work report.
- In the portrait cuts of batch normalization and embeddings, formulas are shown as text because the typeset equations failed the type-size check at that frame size.
