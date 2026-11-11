# Myelin: Teaching Agents Habits

**Fellow:** Nidhi Grover<br>
**Project:** Iacon Autonomics (RL Environment project)<br>
**Week:** Week 5 (2026-10-21 – 2026-10-27)<br>
**Type:** Weekly progress update<br>
**Format:** 16:9 + 9:16<br>
**Voice:** Kokoro `af_bella`<br>
**Brand:** `claude-hai` (@HumanitariansAI)

**Video:** [Myelin Project Update (16:9)](https://www.youtube.com/watch?v=uJVnuI_coE8)<br>
**9:16 Short:** [Myelin Project Update (9:16)](https://www.youtube.com/watch?v=lUVcYpOzTpo)

## What this video covers
The initial plan for Myelin ([myelin](https://github.com/nidhi-humanitarians/myelin)), a habit compiler for AI agents. Agents repeat the same decisions: in public customer-service agent traces (tau-bench), one booking lookup appears over 1,400 times. Myelin's plan is to mine an agent's past logs for decisions that repeat at least 50 times, have a strong model write a small Python function for each, and test it in a sandbox with no network and no model. Each function answers "unsure" when it isn't sure, and must agree with the model at least 98% of the time on later, unseen sessions. It would be compared against a semantic cache, a small classifier and a small local model. The planned deliverables are the habit compiler (a Python package) and a dashboard mapping compiled habits. Only call counts are measured so far; any savings are targets.

**Takeaway:** Compile the habits, and keep the model for the hard parts.

## Files in this folder
- `SCRIPT.md`: narration script
- `beat_sheet.json` / `vertical/beat_sheet.json`: Brutalist source for 16:9 and 9:16
- `scenes.py` / `vertical/scenes.py`: Manim scenes
- `SHOTLIST.md`, `FACTCHECK.md`, `PROMPTS.md`: planning, fact-check (trace counts re-counted from the raw files) and prompts
- `TYPECHECK.md`, `layout_audit.md`, `STATUS.md`: QC and build status
- `final/myelin-habits.verified.json` / `vertical/final/myelin-habits-vertical.verified.json`: verification records for the final renders

No MP4 or MP3 in this folder. Renders are on YouTube/Drive; rebuild from `beat_sheet.json` and `scenes.py` with [Brutalist](https://github.com/nikbearbrown/brutalist.art).

## Sources
Myelin [design specification](https://github.com/nidhi-humanitarians/myelin/blob/main/docs/DESIGN_SPECIFICATION.md); tau-bench agent trajectories (GPT-4o and Claude 3.5 Sonnet) in the myelin repository's `data/historical_trajectories`.

## Process log
[FRICTIONAL.md](FRICTIONAL.md)
