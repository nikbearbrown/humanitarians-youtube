# Search, Don't Read.

**Fellow:** Nidhi Grover<br>
**Project:** Iacon Autonomics (RL Environment project)<br>
**Week:** Week 4 (2026-10-14 – 2026-10-20)<br>
**Type:** Weekly progress update<br>
**Format:** 16:9 + 9:16<br>
**Voice:** Kokoro `af_bella`<br>
**Brand:** `claude-hai` (@HumanitariansAI)

**Video:** [Multi Hop Reasoning Project Update (16:9)](https://www.youtube.com/watch?v=q5kbQpRghHs)<br>
**9:16 Short:** [Multi Hop Reasoning Project Update (9:16)](https://www.youtube.com/watch?v=ZPdHuFTseyM)<br>
**Renders (Drive):** [Change of project + Initial Scoping](https://drive.google.com/drive/folders/1GWB5gZtdz8Hx1Ed03l8L9s7Oxz_3ZWhX)

## What this video covers
My first steps in research on agentic search. I started on a Kaggle competition about post-training Google's Gemma as a developer agent (literature review on RLVR, PostTrainBench and HumanEval). That project was scoped beyond what the fellowship could take on, and I was reassigned. The new question: how well can an agent search a document far too long to read by writing code? I built a small test repository ([agentic-repl](https://github.com/nidhi-humanitarians/agentic-repl)), a Pi-style agent loop with a Python REPL and search helpers (`grep`, `read_lines`), and tested it on one BABILong qa2 question at 128k tokens (~275 pages). On the first run it answered correctly, citing the lines it used.

**Takeaway:** Agents don't read long documents; they search them with code. Ask for the lines behind every answer.

**Next steps shown:** connect Earendil's Pi agent, test longer documents and more BABILong tasks, stricter scoring, sandbox the code, then fine-tune toward 2,000-page books.

## Files in this folder
- `SCRIPT.md`: narration script
- `beat_sheet.json` / `vertical/beat_sheet.json`: Brutalist source for 16:9 and 9:16
- `scenes.py`: Manim scenes
- `SHOTLIST.md`, `FACTCHECK.md`, `PROMPTS.md`: planning, fact-check and prompts
- `CHECKS-REPORT.md`, `TYPECHECK.md`, `layout_audit.md`, `STATUS.md`: QC and build status
- `final/search-dont-read.verified.json`: verification record for the final render

No MP4 or MP3 in this folder. Renders are on YouTube/Drive; rebuild from `beat_sheet.json` and `scenes.py` with [Brutalist](https://github.com/nikbearbrown/brutalist.art).

## Sources
Kuratov et al., BABILong, NeurIPS 2024 Datasets & Benchmarks (arXiv 2406.10149).

## Related
- Week 4 STEM/AI video (completed late): [Multi-Hop Search: Connecting the Pieces](../2026-10-22-multi-hop-search/)

## Process log
[FRICTIONAL.md](FRICTIONAL.md)
