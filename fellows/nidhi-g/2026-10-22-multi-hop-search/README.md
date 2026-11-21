# Multi-Hop Search: Connecting the Pieces

**Fellow:** Nidhi Grover<br>
**Project:** Iacon Autonomics (RL Environment project)<br>
**Week:** Week 4 (2026-10-14 – 2026-10-20), completed late (2026-10-22)<br>
**Late note:** This is the Week 4 STEM/AI video. The approach was reworked and the video recreated, so the final version was completed after Week 4; see [FRICTIONAL.md](FRICTIONAL.md).<br>
**Type:** STEM/AI topic (follows [Stuff It or Search It?](../2026-10-22-stuff-or-search/))<br>
**Format:** 16:9 + 9:16<br>
**Voice:** Kokoro `af_bella`<br>
**Brand:** `claude-hai` (@HumanitariansAI)

**Video:** [Multi Hop Search (16:9)](https://www.youtube.com/watch?v=rZhI6hPbIOs)<br>
**9:16 Short:** [Multi Hop Search (9:16)](https://www.youtube.com/watch?v=LtSznIq6a4Q)<br>
**Renders (Drive):** [Multi Hop RAG as a solution](https://drive.google.com/drive/folders/1F9S9nrZLlIegFSwHQeWrjB-UXb9l2836)

## What this video covers
Methods that connect scattered facts instead of retrieving once and answering: iterative retrieval, where each finding shapes the next search; question decomposition (Self-Ask); interleaved reasoning and retrieval (IRCoT); and entity graphs that link facts across chunks (GraphRAG). It then shows my early agentic-search work ([agentic-repl](https://github.com/nidhi-humanitarians/agentic-repl)), an agent that writes `grep`/`read_lines` code to follow the trail (one question, one run). It covers why answers need line-level citations in fields like insurance, healthcare and law, the privacy benefit of searching locally, the cost of extra hops, and the benchmarks used to measure all this (HotpotQA, MuSiQue, BABILong).

**Takeaway:** Retrieve, read, retrieve again, and cite every line.

## Files in this folder
- `SCRIPT.md`: narration script
- `beat_sheet.json` / `vertical/beat_sheet.json`: Brutalist source for 16:9 and 9:16
- `scenes.py`: Manim scenes
- `SHOTLIST.md`, `FACTCHECK.md`, `PROMPTS.md`: planning, fact-check and prompts
- `CHECKS-REPORT.md`, `TYPECHECK.md`, `layout_audit.md`, `STATUS.md`: QC and build status
- `final/multi-hop-search.verified.json`: verification record for the final render

No MP4 or MP3 in this folder. Renders are on YouTube/Drive; rebuild from `beat_sheet.json` and `scenes.py` with [Brutalist](https://github.com/nikbearbrown/brutalist.art).

## Sources
Press et al., Self-Ask (arXiv 2210.03350); Trivedi et al., IRCoT, ACL 2023; Edge et al., GraphRAG (arXiv 2404.16130); Yang et al., HotpotQA, EMNLP 2018; Trivedi et al., MuSiQue, TACL 2022; Kuratov et al., BABILong, NeurIPS 2024.

## Process log
[FRICTIONAL.md](FRICTIONAL.md)
