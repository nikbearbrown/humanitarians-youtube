# What Real Cloud Traffic Looks Like

- **Week:** 2–8 Nov 2026 · **Group:** RL Environment
- **Type:** STEM explainer, built from the measurements in my project
- **Code:** [lakshdhamija/rl-autoscaler](https://github.com/lakshdhamija/rl-autoscaler), commit [8b126bd](https://github.com/lakshdhamija/rl-autoscaler/commit/8b126bd)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **This week's project update:** [Why Autoscalers Need Yesterday's Traffic](../2026-11-08-week1-project-update/README.md)
- **Beat sheets:** [landscape](beat_sheet.json) · [vertical](vertical/beat_sheet.json)

## This week's contribution

What does real per-minute web traffic look like, and what does that mean for autoscaling? Measured on 14 real web apps from the Azure Functions Trace 2019:

- traffic rises and falls once a day;
- from one minute to the next it moves by about 15%;
- a typical app has about 24 bursts a day; a typical burst is 1.9 times the normal load and lasts one minute;
- 72% of bursts peak in their first minute, and only about a third rise at all in the minute before;
- many bursts return at the same time on another day (73% in one app).

What it means: reacting is too slow for one-minute bursts, keeping spare servers all day costs about twice as much, and planning from yesterday's pattern gets most of the benefit for far less. Made-up test traffic (5% noise, slow ramps) is too smooth.

Takeaway: before you trust a test, measure your real traffic's noise, bursts per day and how fast bursts peak, then make your test traffic match.

## Human and AI work

- **Laksh D.:** chose the topic from this week's project findings; the measurements come from his project; reviewed this video.
- **Claude Code:** wrote the narration, the beat sheets and `scenes.py`; rendered both versions and ran the toolkit checks.
- **Voice:** Kokoro `af_bella`, an AI voice. The video says so in its first beat.
- **Corrected during the build:** an earlier figure of "5% by chance" for repeating bursts did not reproduce (random timing gives about 10% to 17%), so the video says only that random timing gives far fewer. The first made-up generator is not in the repository history, so its chart is a redrawn version and is labelled "redrawn".

## Reproduce

- **Toolkit:** brutalist.art commit `3a6d3979`, checked 2026-11-08 (Fellow Tier `ai-explainer` with the `hai` persona).
- **Source:** `lakshdhamija/rl-autoscaler` at `8b126bd`. Data: Azure Functions Trace 2019, CC-BY 4.0, Shahrad et al., USENIX ATC 2020.
- **Numbers on screen:** `evidence/make_evidence.py` computes every number and curve from the repository and writes `evidence/evidence.json`. A burst "rises before" when its previous minute is more than 15% above the trailing 30-minute median.
- **Build:** copy this folder into a reel folder, then `./art run <reel>` for a review cut and `./art final <reel>` for the master. The vertical version uses `vertical/beat_sheet.json` with the same `scenes.py`.
- **Checks:** [FACTCHECK.md](FACTCHECK.md), [SOURCES.md](SOURCES.md).

## Watch and review

| Version | Resolution | Length | SHA-256 |
|---|---|---|---|
| Landscape | 3840×2160 | 2:15 | `fd0a4827d5f4549b9bff625e45d2d888bacdb2d51b5af6a2240a40cfdff353be` |
| Vertical | 2160×3840 | 2:15 | `cdc17632e6f7c6a0b80d4bf5c388904e82280f7ed033fa3a29fdb2d66f819d3d` |

- **Files:** `RealCloudTraffic_LakshDhamija.mp4` (landscape) and `RealCloudTraffic_LakshDhamija-vertical.mp4` in `Week1-Nov-2/` of the [project Drive folder](https://drive.google.com/drive/folders/1IqLdBcMUEMXJP-JBYhMP7OVyV81zTXX3?usp=drive_link).
- **PM review:** pending.
