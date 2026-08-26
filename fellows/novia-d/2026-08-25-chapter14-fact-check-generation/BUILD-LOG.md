# BUILD-LOG — chapter14-second-read

Title: **Fact-Check Generation**. Topic chip: **CANCER TEXTBOOK · CHAPTER 14**.
Greeting: **Hello Novia**. Voice: **af_bella**. Duration: **179.8s (2:59)**.

Workbook counts from `14_factcheck_report_ai_only_editorial.md`. Spine is the four-move method: count → split → editorial → reread.


## Counts (from the editorial report, not invented)

- 138 sentences
- 92 AI-only / 46 web-flagged
- AI-only by file: Intro 8, Components 33, Stroma 13, Inflammation 17, ECM 16, Summary 5
- 8 editorial findings
- 5 of 92 hallucination flags; most significant: IL-17 → IL-23 reversed
- Did not invent a CONFIRMED/CONTRADICTED split of the 46

## Pipeline

- Kokoro `am_echo` — 11 beats, 218.2s, $0.00
- GATE A/W/L clean. GATE B: first B04 pass failed TEXT_ON_CURVE (counts sat on the bar track); counts moved to the right of the track, strokes off. Re-audit CLEAN.
- Manim B04/B07 held to audio so compile does not slow-mo fade-ins.
- `./art run --height 1080` — 11/11 filled
- Masters:
  - `chapter14-second-read.mp4` (clean, 218.2s)
  - `chapter14-second-read-slate.mp4` (review labels)
- GATE V on the **slate** flags title-safe edge-bleed from burn-in timecode (false positive). On the **clean** master: 0 BLOCKER, 6 MAJOR underfill on ClaudeScienceLayerStack / ClaudeWindow / ClaudeTitleOutro (same Claude cream-space pattern as `tumor-is-a-neighborhood`). Looked at frames; not a content defect.
