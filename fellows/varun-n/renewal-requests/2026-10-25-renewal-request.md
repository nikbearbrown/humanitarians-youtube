# Fellowship Renewal Request - Varun Nayyar

**Name:** Varun Nayyar
**Project:** Medhavy
**Current agreement end date:** October 31, 2026
**Reporting period:** August 1 to October 23, 2026 (Weeks 1-12). Week 13 (October 24 to 30) is in progress at time of writing and will be finalized before the current agreement ends.
**Requested renewal dates:** November 1, 2026 to February 8, 2027

---

## Completed Results

**1. Physics (mechanics) video series: 30 of 30 buildable concepts built, 21 published or scheduled as Shorts**
Rebuilt the textbook video pipeline in a new visual style after the first videos were not approved, then built every buildable concept as a 4K long-form video with a matching 4K vertical Short. The format was approved by the faculty reviewers on September 25. As of October 25, 21 Shorts are published or scheduled and 9 are waiting to be posted. Personal contribution: directing the build and each format decision (visual style, question-card opening, 4K by upscaling, speed settings); watching the videos to catch defects (text overlaps, caption sync drift, a mispronounced term, a QC report that claimed a fix that was not done); giving the review feedback that produced the final intro/outro transition; and publishing the Shorts. Claude Code built the scenes and ran the parallel build agents.
Evidence: the Published Shorts index below (YouTube link and code for each of the 21). The code for 11 of them was merged in [PR #182](https://github.com/nikbearbrown/humanitarians-youtube/pull/182) on October 23, 2026; the other 10 are in [PR #296](https://github.com/nikbearbrown/humanitarians-youtube/pull/296), open and awaiting review.

**2. 12 weekly project-progress videos (Weeks 1-12), 4K, 16:9 and 9:16**
One progress video per week, each with a beat sheet, README and Frictional log, built through a spec-to-video pipeline (beat sheet, narration, render, compile with automatic frame checks) following the Humanitarians AI Brutalist/fellows-folder specification. From Week 2 on, each video includes an animated visual. Personal contribution: supplying each week's account, reviewing every video in both orientations, and approving the format.
Evidence: the Weekly Evidence Index below. Weeks 1-8 were merged in [PR #182](https://github.com/nikbearbrown/humanitarians-youtube/pull/182) on October 23, 2026. Weeks 9-12 are delivered and in [PR #296](https://github.com/nikbearbrown/humanitarians-youtube/pull/296), open and awaiting review.

**3. Pipeline and channel: intro/outro integration, free open-source narration, faster rendering, channel maintenance**
The new studio intro and outro were not made by me; the professor approved them at the October 5 meeting. At my direction they are used for all new Shorts after the original six (long-form videos carry none), and Claude Code integrated them into the pipeline. After my feedback that the intro felt abrupt, the transition was rebuilt and 23 Shorts waiting for review were re-stitched. Narration moved to a free local voice model (no paid API); GPU narration was tested (about 6.5x faster, kept opt-in because it is not bit-identical), 4K encodes moved to the GPU, and a GPU renderer that benchmarked about 23% slower was rejected. On September 22 the faculty reviewers also assigned me maintenance of the Medhavy AI YouTube channel, and about ten videos that were not explainer-style were unlisted (my count). Personal contribution: deciding where the intro and outro apply, the review feedback on the transition, the benchmarking decisions, and the listening checks.
Evidence: Frictional logs for Weeks 8, 10, 11 and 12 in the index below. The channel maintenance is not stored in the GitHub repository (done in YouTube Studio).

---

## What I Learned This Term

Each point comes from the takeaway recorded in that week's log.

- **Review is what makes automation safe.** An unattended batch of videos saved time but let overlaps through (Week 5), and a QC report once claimed a fix that had not been made (Week 7). I now watch every video in both orientations before it is shown to anyone.
- **Check files with tools, not names.** A supplied "4K" outro turned out to be 478 by 850 pixels (Week 8); I now check media with ffprobe.
- **Measure before changing tools.** Benchmarks showed GPU encoding about twice as fast but a GPU renderer about 23% slower, so I kept one and rejected the other (Week 8).
- **Work within a hardware limit.** Native 4K ran out of memory, so rendering at 1080p and upscaling delivered 4K without raising the limit (Week 4).
- **Parallel work needs locks.** Running every job at once crashed the Linux environment; letting one job of each kind run at a time fixed it (Week 12).
- **Read what a commit will delete.** Git showed 15 deletions that were not real, and committing would have made them real (Week 9).
- **Scope an exception instead of changing the system.** A reviewer's white-background preference was handled with an override limited to one sample, leaving the brand theme intact (Week 2).
- **Report quiet weeks as quiet.** The logs for quiet weeks (Weeks 6 and 10) say so plainly rather than inventing activity.

---

## Degree Relevance and Supervision

This work applies MS in Business Analytics coursework in Python, AI tools, and process and quality measurement, for example render benchmarks and a recount that corrected the project's scope from 29 to 31 storyboards.

**Supervisor:** the supervising professor on the Medhavy team (real name included in the private email only, per the naming policy for public documents)

---

## Next Period (November 1, 2026 to February 8, 2027)

**Deliverable 1:** Finish the mechanics Shorts: publish the remaining Shorts and add their code and READMEs to the repository.
**Target date:** November 5, 2026

**Deliverable 2:** Add the long-form videos to the physics textbook.
**Target date:** end of November or the first week of December 2026

**Deliverable 3:** An agentic or machine-learning task. The task has not been decided yet; I will request it from the supervising professor and agree its target date with them.

---

## Outstanding Issues

- 9 Shorts are still to be posted (as of October 25), each needing its code, README and description added.
- All 30 long-form videos are built; none are published yet.
- Week 13 is in progress.
- [PR #182](https://github.com/nikbearbrown/humanitarians-youtube/pull/182) merged on October 23, 2026 (Weeks 1-8 and the first 11 Shorts projects). [PR #296](https://github.com/nikbearbrown/humanitarians-youtube/pull/296) (Weeks 9-12 and 10 further Shorts projects) is open and awaiting review. Their links below point to the author's fork, pinned to commit `01892c11`, and will be re-pinned once it is merged.
- A few minor visual items on the unposted Shorts (for example a plain-text label where a symbol should be) will be fixed before they are posted.
- 15 repository files with colons in their names break Windows git checkouts; a pull request to the upstream repository has not been opened yet.
- Otherwise: none known at this time.

---

## Weekly Evidence Index

| Week / dates | Video links | Log and work evidence |
|---|---|---|
| Week 1 (Aug 1 to 7) | [Progress video](https://drive.google.com/drive/folders/1hYKIKDLXuYgiiLtRhk87uI-tOiU6_Uba?usp=drive_link) | [Progress log](https://github.com/nikbearbrown/humanitarians-youtube/blob/b5256c4bd11da7d50e1b270034ddd16f76be24dc/fellows/varun-n/2026-08-07-progress-starting-over/FRICTIONAL.md) |
| Week 2 (Aug 8 to 14) | [Progress video](https://drive.google.com/drive/folders/1tUDKcFGVOw_hjeM4w1splmMjQHlk7LyV?usp=drive_link) | [Progress log](https://github.com/nikbearbrown/humanitarians-youtube/blob/b5256c4bd11da7d50e1b270034ddd16f76be24dc/fellows/varun-n/2026-08-14-progress-white-background/FRICTIONAL.md) |
| Week 3 (Aug 15 to 21) | [Progress video](https://drive.google.com/drive/folders/1vsn2xoy_peWtEiVNaWghNCMh95rUWOYI?usp=drive_link) | [Progress log](https://github.com/nikbearbrown/humanitarians-youtube/blob/b5256c4bd11da7d50e1b270034ddd16f76be24dc/fellows/varun-n/2026-08-21-progress-captions-that-froze/FRICTIONAL.md) |
| Week 4 (Aug 22 to 28) | [Progress video](https://drive.google.com/drive/folders/100WD0doh52QfMKIL7drI_UAheDu-9Eqv?usp=drive_link) | [Progress log](https://github.com/nikbearbrown/humanitarians-youtube/blob/b5256c4bd11da7d50e1b270034ddd16f76be24dc/fellows/varun-n/2026-08-28-progress-chapter-four-and-4k/FRICTIONAL.md) |
| Week 5 (Aug 29 to Sep 4) | [Progress video](https://drive.google.com/drive/folders/10dxAaahsvSpdPLV8l9HLKyEUDZfOUJ3i?usp=drive_link) | [Progress log](https://github.com/nikbearbrown/humanitarians-youtube/blob/b5256c4bd11da7d50e1b270034ddd16f76be24dc/fellows/varun-n/2026-09-04-progress-chapter-five-batch/FRICTIONAL.md) |
| Week 6 (Sep 5 to 11) | [Progress video](https://drive.google.com/drive/folders/1SiVfyHll3pdT0NMVuLqZpPzd2vQs7yr1?usp=drive_link) | [Progress log](https://github.com/nikbearbrown/humanitarians-youtube/blob/b5256c4bd11da7d50e1b270034ddd16f76be24dc/fellows/varun-n/2026-09-11-progress-a-holiday-week/FRICTIONAL.md) |
| Week 7 (Sep 12 to 18) | [Progress video](https://drive.google.com/drive/folders/1ZU0hr_4M29cxLYbHZihy7KdpQ5XgMvtj?usp=drive_link) | [Progress log](https://github.com/nikbearbrown/humanitarians-youtube/blob/b5256c4bd11da7d50e1b270034ddd16f76be24dc/fellows/varun-n/2026-09-18-progress-rejected-and-reframed/FRICTIONAL.md) |
| Week 8 (Sep 19 to 25) | [Progress video](https://drive.google.com/drive/folders/1dMw7_uXmNP45qJi-Gg6mowrQaZ55w50T?usp=drive_link) | [Progress log](https://github.com/nikbearbrown/humanitarians-youtube/blob/b5256c4bd11da7d50e1b270034ddd16f76be24dc/fellows/varun-n/2026-09-25-progress-format-approved/FRICTIONAL.md) |
| Week 9 (Sep 26 to Oct 2) | [Progress video](https://drive.google.com/drive/folders/19A1wKo6MpK9S_cHgMdVU_dr4XG1qgyQ1?usp=drive_link) | [Progress log](https://github.com/Omega-84/humanitarians-youtube/blob/01892c11127a031fbaf95c6c714d7ebdea17803b/fellows/varun-n/2026-10-02-progress-six-shorts-live/FRICTIONAL.md) (PR #296, open) |
| Week 10 (Oct 3 to 9) | [Progress video](https://drive.google.com/drive/folders/1bgMYgqKGNpYaM4TzAXWWUV4KBxaF6Rfn?usp=drive_link) | [Progress log](https://github.com/Omega-84/humanitarians-youtube/blob/01892c11127a031fbaf95c6c714d7ebdea17803b/fellows/varun-n/2026-10-09-progress-intro-outro-approved/FRICTIONAL.md) (PR #296, open) |
| Week 11 (Oct 10 to 16) | [Progress video](https://drive.google.com/drive/folders/1LAjbBkIIQiOwJBjZa8qnOdBfn5fbYnJ7?usp=drive_link) | [Progress log](https://github.com/Omega-84/humanitarians-youtube/blob/01892c11127a031fbaf95c6c714d7ebdea17803b/fellows/varun-n/2026-10-16-progress-chapter-six-rebuilt/FRICTIONAL.md) (PR #296, open) |
| Week 12 (Oct 17 to 23) | [Progress video](https://drive.google.com/drive/folders/1b25mFmxBPPMbZY_uBvW6Bxk5xeRermmJ?usp=drive_link) | [Progress log](https://github.com/Omega-84/humanitarians-youtube/blob/01892c11127a031fbaf95c6c714d7ebdea17803b/fellows/varun-n/2026-10-23-progress-thirty-of-thirty/FRICTIONAL.md) (PR #296, open) |

*Week 13 (October 24 to 30) is in progress and will be added once complete, before the current agreement ends October 31.*

## Published Shorts (mechanics series)

| Short | Textbook section | YouTube | Code |
|---|---|---|---|
| Is A Ball Still Accelerating At Its Peak? | Physics Vol. 1, section 3.3 | [Short](https://www.youtube.com/shorts/FnK4-yRPOww) | [code](https://github.com/nikbearbrown/humanitarians-youtube/tree/b5256c4bd11da7d50e1b270034ddd16f76be24dc/claude-for-physics/medhavy-ball-still-accelerating) |
| Which Falls Faster? | Physics Vol. 1, section 3.5 | [Short](https://www.youtube.com/shorts/DZUhKz6_h-g) | [code](https://github.com/nikbearbrown/humanitarians-youtube/tree/b5256c4bd11da7d50e1b270034ddd16f76be24dc/claude-for-physics/medhavy-ball-and-feather) |
| Is A Turning Car Still Accelerating? | Physics Vol. 1, section 4.2 | [Short](https://www.youtube.com/shorts/LSLtAWZWCyc) | [code](https://github.com/nikbearbrown/humanitarians-youtube/tree/b5256c4bd11da7d50e1b270034ddd16f76be24dc/claude-for-physics/medhavy-car-turning) |
| Why Does Rain Hit You From The Front? | Physics Vol. 1, section 4.5 | [Short](https://www.youtube.com/shorts/MBVrHeQRKJE) | [code](https://github.com/nikbearbrown/humanitarians-youtube/tree/b5256c4bd11da7d50e1b270034ddd16f76be24dc/claude-for-physics/medhavy-rain-relative-motion) |
| What Really Stops A Sliding Puck? | Physics Vol. 1, section 5.2 | [Short](https://www.youtube.com/shorts/nJUA8plGrOQ) | [code](https://github.com/nikbearbrown/humanitarians-youtube/tree/b5256c4bd11da7d50e1b270034ddd16f76be24dc/claude-for-physics/medhavy-inertia-puck) |
| Did She Lose Five-Sixths Of Her Mass? | Physics Vol. 1, section 5.4 | [Short](https://www.youtube.com/shorts/byO4NcbLcXc) | [code](https://github.com/nikbearbrown/humanitarians-youtube/tree/b5256c4bd11da7d50e1b270034ddd16f76be24dc/claude-for-physics/medhavy-weight-vs-mass) |
| How Does Anything Ever Move? | Physics Vol. 1, section 5.5 | [Short](https://www.youtube.com/shorts/e9wJXusS31g) | [code](https://github.com/nikbearbrown/humanitarians-youtube/tree/b5256c4bd11da7d50e1b270034ddd16f76be24dc/claude-for-physics/medhavy-horse-cart-paradox) |
| What Force Pulls A Car Around A Curve? | Physics Vol. 1, section 6.3 | [Short](https://www.youtube.com/shorts/s9J_UCMhq14) | [code](https://github.com/nikbearbrown/humanitarians-youtube/tree/b5256c4bd11da7d50e1b270034ddd16f76be24dc/claude-for-physics/medhavy-centripetal-friction) |
| Why Can't A Particle Pass Certain Points? | Physics Vol. 1, section 8.4 | [Short](https://www.youtube.com/shorts/zS_nQV0kLv0) | [code](https://github.com/Omega-84/humanitarians-youtube/tree/01892c11127a031fbaf95c6c714d7ebdea17803b/claude-for-physics/medhavy-pe-diagram-forbidden-zones) (PR #296, open) |
| Why Is The Crumpling Car Safer? | Physics Vol. 1, section 9.2 | [Short](https://www.youtube.com/shorts/U1Fjb2Cnnis) | [code](https://github.com/nikbearbrown/humanitarians-youtube/tree/b5256c4bd11da7d50e1b270034ddd16f76be24dc/claude-for-physics/medhavy-crumple-zones) |
| What Is Conserved When Blocks Stick Together? | Physics Vol. 1, section 9.4 | [Short](https://www.youtube.com/shorts/sGacVdCKzoU) | [code](https://github.com/Omega-84/humanitarians-youtube/tree/01892c11127a031fbaf95c6c714d7ebdea17803b/claude-for-physics/medhavy-inelastic-collision) (PR #296, open) |
| How Does A Rocket Accelerate In Empty Space? | Physics Vol. 1, section 9.7 | [Short](https://www.youtube.com/shorts/qTdUwJyLN5E) | [code](https://github.com/Omega-84/humanitarians-youtube/tree/01892c11127a031fbaf95c6c714d7ebdea17803b/claude-for-physics/medhavy-rocket-propulsion) (PR #296, open) |
| How Fast Is The Bottom Of A Rolling Wheel? | Physics Vol. 1, section 11.1 | [Short](https://www.youtube.com/shorts/YM1C4FW05t8) | [code](https://github.com/Omega-84/humanitarians-youtube/tree/01892c11127a031fbaf95c6c714d7ebdea17803b/claude-for-physics/medhavy-rolling-wheel) (PR #296, open) |
| Why Doesn't A Spinning Top Fall Over? | Physics Vol. 1, section 11.4 | [Short](https://www.youtube.com/shorts/S-CTuRPawiQ) | [code](https://github.com/Omega-84/humanitarians-youtube/tree/01892c11127a031fbaf95c6c714d7ebdea17803b/claude-for-physics/medhavy-gyroscope-precession) (PR #296, open) |
| Why Does Speeding Up A Satellite Slow It Down? | Physics Vol. 1, section 13.4 | [Short](https://www.youtube.com/shorts/oaxugEl4JZs) | [code](https://github.com/Omega-84/humanitarians-youtube/tree/01892c11127a031fbaf95c6c714d7ebdea17803b/claude-for-physics/medhavy-orbit-energy-paradox) (PR #296, open) |
| How Can A Small Push Lift A Car? | Physics Vol. 1, section 14.3 | [Short](https://www.youtube.com/shorts/zERIfq1IIEI) | [code](https://github.com/Omega-84/humanitarians-youtube/tree/01892c11127a031fbaf95c6c714d7ebdea17803b/claude-for-physics/medhavy-hydraulics) (PR #296, open) |
| Does Faster Water Mean Higher Pressure? | Physics Vol. 1, section 14.6 | [Short](https://www.youtube.com/shorts/P5afwrxSxrQ) | [code](https://github.com/nikbearbrown/humanitarians-youtube/tree/b5256c4bd11da7d50e1b270034ddd16f76be24dc/claude-for-physics/medhavy-bernoulli) |
| Does A Heavier Pendulum Swing Slower? | Physics Vol. 1, section 15.4 | [Short](https://www.youtube.com/shorts/xefDv4V43VI) | [code](https://github.com/Omega-84/humanitarians-youtube/tree/01892c11127a031fbaf95c6c714d7ebdea17803b/claude-for-physics/medhavy-pendulum-mass-independence) (PR #296, open) |
| How Can Tiny Footsteps Sway A Bridge? | Physics Vol. 1, section 15.6 | [Short](https://www.youtube.com/shorts/7Twet2H-scs) | [code](https://github.com/Omega-84/humanitarians-youtube/tree/01892c11127a031fbaf95c6c714d7ebdea17803b/claude-for-physics/medhavy-resonance) (PR #296, open) |
| Why Do Two Notes Make A Pulsing Sound? | Physics Vol. 1, section 17.6 | [Short](https://www.youtube.com/shorts/firMQzFG_us) | [code](https://github.com/nikbearbrown/humanitarians-youtube/tree/b5256c4bd11da7d50e1b270034ddd16f76be24dc/claude-for-physics/medhavy-beats) |
| Does A Moving Siren Sound Like A Moving Listener? | Physics Vol. 1, section 17.7 | [Short](https://www.youtube.com/shorts/pGvD1T_9INM) | [code](https://github.com/Omega-84/humanitarians-youtube/tree/01892c11127a031fbaf95c6c714d7ebdea17803b/claude-for-physics/medhavy-doppler-asymmetry) (PR #296, open) |

---

*Prepared following the Humanitarians AI renewal request format. This request should be sent as a link to both hr@humanitarians.ai and bear@humanitarians.ai, Monday to Wednesday during business hours, before the current agreement's October 31, 2026 end date. Renewals require approval; agreements are not backdated.*
