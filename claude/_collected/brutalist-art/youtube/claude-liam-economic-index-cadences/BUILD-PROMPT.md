# BUILD-PROMPT — Claude on the Clock

**Reel:** `claude-liam-economic-index-cadences`  
**Channel:** claude-liam · Kokoro `am_onyx` · @NikBearBrown  
**Built:** 2026-07-17

---

Build one 16:9 claude-explainer video titled **"Claude on the Clock"** covering
Anthropic's Economic Index **Cadences** report (June 2026) by Massenkoff, Lyubich,
Sacher, Hitzig, Zhang, Heller, McCrory.

**Channel:** claude-liam — Kokoro `am_onyx`, @NikBearBrown folder chip, Teardown
register (Feynman × MKBHD), Liam in for Bear (say so in B00 narration and outro,
greet "Ciao, Liam").

**Free pipeline only:** Kokoro voice, no ElevenLabs, no higgsfield, no publishing,
no git commit or push. Run without approval pauses.

**Spec:** 1920×1080 (16:9), 30 fps, audio-first.

**All 10 report figures REBUILT as native animated Remotion graphics.** No screenshots.

**Output:** `brutalist-art/youtube/claude-liam-economic-index-cadences/`

---

## Figures (beat B01–B10)

### B01 — Usage Patterns (Fig 1 cluster)
Two-phase: hourly ribbon (5 clusters: 5am early birds, 7am commute, 10am work block,
6pm personal-use peak 2.3× terracotta, 8pm evening) → weekly stacked bars Mon–Sun
(Sat/Sun terracotta at 48%/49%).
Spark: *The workday has a heartbeat. The weekend has a different one.*

### B02 — Tax-Day Spike
Time-series line chart US vs rest-of-world Apr 1–20; US spikes Apr 14 to ~8×;
terracotta vertical rule Apr 15 "US filing deadline"; RoW flat grey.
Spark: *Real work. Tax season proves it.*

### B03 — Artifact Mix
Phase 1 ranked bars: Explanations 17%, Documents 15%, Guidance 11%, then smaller.
Big stat: 93% of conversations produce a named artifact (terracotta).
Phase 2: three group bucket cards (conversational ~1/3, written ~1/3, code ~1/6).
Spark: *93% of the time, something real gets made.*

### B04 — Wage vs Tokens (Compute tracks value)
Phase 1: scatter log-implied, named points Marketing mgrs ~$80/hr vs Editors ~$37/hr
~2.5× gap; pharmacist outlier ring in terracotta; dashed best-fit.
Phase 2: four tercile stat cards — tokens 2.07×, output 1.34×, user turns 1.53×
(terracotta), extended thinking 34% vs 31%.
Spark: *Compute tracks the value of work.*

### B05 — Short Leash (autonomy gap)
Paired horizontal bars per output type (6 types), chat vs Claude Code on 1–5 scale.
Terracotta callout +0.37. Phase 2: blog post comparison (13 rounds vs 1 prompt) +
Sonnet counter-argument (+0.26). 26 of 31 output types Claude Code runs autonomously.
Spark: *The product sets the leash length.*

### B06 — Rising Tide (expectations)
Two scatter panels (observed exposure + Eloundou et al. 2023); grey dots today + orange
dots 12 months; parallel best-fit lines; constant-gap bracket in terracotta (label it).
Stat chips: ~6 in 10 expect higher AI share; >1/3 expect most/nearly all. N=9,700.
Spark: *A rising tide. Same increment everywhere.*

### B07 — Job Anxiety by Perspective
Two stacked-bar panels: responsibilities change (Self 46%, Peer 39%, Junior 55%,
Senior 39%) then job loss (Self 9%, Peer 17%, Junior 40%, Senior 20%). Very Likely
(solid) + Likely (tint) stacks. Junior bars in terracotta. Values †digitized from
report Fig 3.5.
Spark: *It'll happen to someone junior.*

### B08 — Delegation Paradox
Phase 1: 6 bars all positive — Pay +4.7pp, Security +4.0, Finding a job +4.5,
Meaning +3.5, Autonomy +2.9, Human interaction +3.8 — with CI whiskers.
Change per +1 SD (22pp) of automation share.
Phase 2: trend lines — "AI increases market value of my skills" (57%) RISES
(terracotta); "I learn more with AI" (68%) FLAT. Values †digitized from Figs 3.6+3.7.
Spark: *Delegate more. Expect better. Not worse.*

### B09 — Gender Differences
4 horizontal bars women − men in outcome SDs, occupation-controlled, CI whiskers:
Work-use share −0.09, Claude Code share −0.24 (6.3pp), Automation share −0.33 (7.3pp),
Total active mins +0.24 (terracotta — the one positive bar). Women = 12% of sample.
Values †digitized from report Fig 3.8.
Spark: *More time. More iterative. More collaborative.*

### B10 — Dream Big (10-year survey)
Three theme bars rising like a skyline: Augmentation >52%, Automation ~51%,
Shared prosperity ~33%. Caveats chip top-right (30% computer & math, 12% women,
self-report). No terracotta accent — all three bars are the landing.
Spark: *Not replacement. Not rescue. Collaboration.*

---

## Closing block (beats B11–B13)

**B11 VERDICT** — `ClaudeVerdictArtifact`
Five findings:
1. Usage mirrors the workweek: weekday backend work, weekend quant trading and agent design.
2. 93% of conversations produce a named artifact; compute spend tracks occupational wage.
3. The product sets the leash length — Claude Code runs autonomously across 26 of 31 output types.
4. Expected progress is a rising tide — the same increment regardless of current exposure.
5. Those who delegate the most are the most optimistic on all six dimensions of job quality.

**B12 YOUR TURN** — `ClaudeComposerAsk` greeting="Your turn."
Prompt: "What share of my work tasks could you do entirely on your own today — and which
ones should I never hand over? Interview me, then give me your honest split."

**B13 OUTRO** — `ClaudeTitleOutro`
Title: "Claude on the Clock." Handle: @NikBearBrown  
Subline: "Liam, in for Bear."

---

## Required outputs

- `beat_sheet.json` ✓
- `claude-liam-economic-index-cadences.mp4` ✓ (297.4s, 1920×1080, 7136 frames)
- `SOURCES.md` ✓
- `BUILD-PROMPT.md` ← this file
- `_qc/REPORT.md` ✓
