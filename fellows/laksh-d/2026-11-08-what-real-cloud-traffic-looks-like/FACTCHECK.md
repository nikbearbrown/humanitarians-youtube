# FACTCHECK: What Real Cloud Traffic Looks Like

Source of truth: lakshdhamija/rl-autoscaler @ 8b126bd and the runs recorded in `evidence/`
(`demo_stdout.txt` = `python scripts/demo.py`, `evidence.json` = `evidence/make_evidence.py`). Checked 2026-11-08.
"Training days" = days 1-10 of the 14 training apps; bursts are the repo's `traffic.find_bursts` (a minute above
1.5 x the median of the previous 30 minutes).

| Claim (beat) | Verdict | Source / derivation | Fix |
|---|---|---|---|
| Real web app from Microsoft's public Azure Functions trace (B02) | ✓ | app 9aba8d35, `data/azure2019_http_apps.*` (Azure Functions Trace 2019, CC-BY 4.0) | |
| Traffic rises and falls once a day (B02) | ✓ | days 2-4 of 9aba8d35, per minute (`evidence.json` hero3_min); one peak and one trough per day | "morning/night" avoided: trace clock is not local time |
| Minute-to-minute noise about 15% (B00, B03, B07, B08) | ✓ | `demo_stdout.txt` real (training days) noise 0.14 (median over apps of calm-minute std / trailing median); B03's app 38ee9fad measures 0.142 | "about" |
| B03 hour shown | ✓ | 38ee9fad day 3, 14:00-15:00, with its trailing 30-minute median and a +/-15% band (`evidence.json` noise_hour) | |
| About 24 bursts per app per day (B00, B04, B08) | ✓ | `demo_stdout.txt` 23.9 bursts/day | |
| Typical burst almost twice normal load (B04: "1.9x") | ✓ | median height 1.88 x the trailing median | |
| Typical burst lasts one minute (B04); "most one minute long" (B08) | ✓ | median length 1 minute; 56.5% of training bursts are 1 minute (`find_bursts`) | |
| 72% of bursts peak in the very first minute (B00, B04, B08) | ✓ | `demo_stdout.txt` 72%; `evidence.json` peak_dist[0] = 0.718 (3,351 bursts) | |
| Only about a third rise at all in the minute before (B04 "1 in 3") | ✓ | `evidence.json` rise_before = 0.333: share of training bursts whose previous minute is more than 15% (one noise width) above the trailing 30-minute median | definition chosen here; matches the figure in the narration brief |
| B04 example bursts | ✓ | e7a26f46 t=3681 (2.06x), e8cb71e1 t=4672 (1.78x), ec941895 t=1530 (1.80x), each 1 minute long and peaking in minute 0 | |
| In one app, 73% of bursts return at the same time on another day (B05) | ✓ | 9aba8d35, 26 training-day bursts, 73.1% have a burst within 5 minutes of the same time on another day (`traffic.repeat_share` rule) | |
| "Random timing would give far fewer" (B05) | ✓ (qualitative) | random times for the same 26 bursts: 10% with the repo's 3-draw estimate (seed 0), 17% averaged over 200 draws | **The brief's "5% by chance" did not reproduce here**, so no chance number is stated |
| B05 right panel "random (made up)" | ✓ labelled | constructed comparison: same days, uniform random minutes, seed 0 | labelled as made up |
| Reacting is too slow for one-minute bursts (B06) | ✓ | Kubernetes rule 5.47% late on held-out apps (`demo_stdout.txt`); boot delay 3 minutes | |
| Spare servers all day works but costs about twice as much (B06) | ✓ | fixed for the day's peak: 39,445 server-min/day, 0.07% late vs 19,986 for the Kubernetes rule; 39,445 / 19,986 = 1.97 | |
| Planning from yesterday gets most of the benefit for far less (B06) | ✓ | 1.17% late at 24,488: removes 80% of the late requests the spare-server plan removes (4.30 of 5.40 points) for 23% of its extra cost (4,502 of 19,459 server-min/day) | |
| 5 held-out apps, 65 unseen days (B06) | ✓ | `demo_stdout.txt` | |
| My first made-up traffic used 5% noise and slowly ramping bursts (B07) | ✓ | the first generator (`synthetic_day`: noise 0.05, ramps of 3-10 minutes) was replaced before the first commit, so it is not in the repo history. B07's top panel is a **redrawn illustration** (real daily shape + 5% noise + one 10-minute ramp), labelled "made-up (redrawn)" | |
| Real: about 15% noise, jumps in one minute (B07) | ✓ | as above (noise 0.14, 72% peak in first minute) | |
| The generator copies each real app's statistics (B07) | ✓ | `traffic.FittedTraffic`: copies one real training app per episode | |
| Generator noise 16%, two thirds peak in the first minute (B07) | ✓ | `demo_stdout.txt` fitted synthetic: noise 0.16, 67% | |
| B07 bottom panel | ✓ | one day from `FittedTraffic(train_series())`, seed 3 | |
| Data credit | ✓ | Shahrad et al., Serverless in the Wild, USENIX ATC 2020; CC-BY 4.0 (B02) | |
| AI disclosure (B00) | ✓ | narration is Kokoro af_bella; analysis from Laksh's project, built with help from Claude Code | |
