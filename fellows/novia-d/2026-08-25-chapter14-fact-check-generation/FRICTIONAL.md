# Frictional Log — Fact-Check Generation (Chapter 14)

**Written:** 2026-10-12 (reconstructed from `BUILD-LOG.md` and the beat sheet in this folder; later than the week of the work)

## 2026-08-25

**What I was working on:** First Brutalist explainer for the cancer-textbook fact-check: Chapter 14, four-move workbook (count → split → editorial → reread of the AI-only pile). Voice Bella (`af_bella`). Greeting Hello Novia.

**What I tried, and what I expected:** A clean 16:9 compile from the editorial-report counts (138 sentences; 92 AI-only / 46 web-flagged; 8 editorial findings). Expected the Claude cream scenes and the count bars to lock to audio on the first pass.

**Where it resisted, and what I did next:** GATE B failed the first B04 pass — counts sat on the bar track (`TEXT_ON_CURVE`). Moved the counts to the right of the track and took the strokes off; re-audit came back clean. GATE V on the slate flagged title-safe edge-bleed from burn-in timecode (false positive). Clean master: 0 BLOCKER; looked at frames, not a content defect.

**What Claude contributed, what I accepted/changed/rejected:** Claude drafted the beat sheet and Manim from the editorial report. I kept the four-move spine and the report counts; I did not invent a CONFIRMED/CONTRADICTED split of the 46 flagged sentences. Voice and greeting stayed Bella / Hello Novia.

**What I understand now, and what I still don't:** The method video is the record of how Chapter 14 was checked, not a substitute for the JSON data model that came later. Still open at the time: the one-row workbook could not hold several sources per sentence — that became video 2.

Evidence in this folder: `BUILD-LOG.md`, `beat_sheet.json`, `SHOTLIST.md`.
