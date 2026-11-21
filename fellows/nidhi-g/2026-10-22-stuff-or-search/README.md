# Stuff It or Search It?

**Fellow:** Nidhi Grover<br>
**Project:** Iacon Autonomics (RL Environment project)<br>
**Week:** Week 3 (2026-10-07 – 2026-10-13), made late (built 2026-10-22)<br>
**Late note:** This is the Week 3 STEM/AI video. It was produced after Week 3 because Brutalist setup issues blocked video production that week; see [Brutalist, Installed.](../2026-10-12-brutalist-installed/) and [FRICTIONAL.md](FRICTIONAL.md).<br>
**Type:** STEM/AI topic (continues in [Multi-Hop Search](../2026-10-22-multi-hop-search/))<br>
**Format:** 16:9 + 9:16<br>
**Voice:** Kokoro `af_bella`<br>
**Brand:** `claude-hai` (@HumanitariansAI)

**Video:** [Why RAG fails for complex texts (16:9)](https://www.youtube.com/watch?v=bgagiyyImeI)<br>
**9:16 Short:** [Why RAG fails for complex texts (9:16)](https://www.youtube.com/watch?v=d2JUcrWpTSc)<br>
**Renders (Drive):** [Why RAG fails](https://drive.google.com/drive/folders/1-d6nHCMpkS1S755G1alkAUjW_PHJAS36)

## What this video covers
Why the two easy fixes for answering questions over long documents fall short. Stuffing the whole document into the prompt buries the relevant lines, costs more on every question, and runs into limits: effective context is shorter than advertised (RULER), and models lose information in the middle (Lost in the Middle), with look-alike text acting as a distractor. Basic RAG splits facts across chunks, misses the deciding second hop (the BABILong football example), ignores event order, and can't follow in-document references like "see section 4.2".

**Takeaway:** Both shortcuts find pieces. Neither connects them. That's the job of multi-hop search.

## Files in this folder
- `SCRIPT.md`: narration script
- `beat_sheet.json` / `vertical/beat_sheet.json`: Brutalist source for 16:9 and 9:16
- `scenes.py`: Manim scenes
- `SHOTLIST.md`, `FACTCHECK.md`, `PROMPTS.md`: planning, fact-check and prompts
- `CHECKS-REPORT.md`, `TYPECHECK.md`, `layout_audit.md`, `STATUS.md`: QC and build status
- `final/stuff-or-search.verified.json`: verification record for the final render

No MP4 or MP3 in this folder. Renders are on YouTube/Drive; rebuild from `beat_sheet.json` and `scenes.py` with [Brutalist](https://github.com/nikbearbrown/brutalist.art).

## Sources
Kamradt, Needle in a Haystack (2023); Hsieh et al., RULER, COLM 2024 (arXiv 2404.06654); Liu et al., Lost in the Middle, TACL 2024 (arXiv 2307.03172); Kuratov et al., BABILong, NeurIPS 2024 (football example from my recorded run in [agentic-repl](https://github.com/nidhi-humanitarians/agentic-repl)).

## Process log
[FRICTIONAL.md](FRICTIONAL.md)
