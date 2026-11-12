# WSJF: What To Build Next — explainer video

A short **AI × Project Management** explainer made for **Sanjana**, produced with the
Brutalist video toolkit and watermarked **@HumanitariansAI**.

The film teaches **WSJF — Weighted Shortest Job First**, the backlog-prioritization
formula from SAFe, by *building it with Claude on screen*: it shows the prompt, the
real Python code it generates, and the backlog **re-sorting itself** as the output —
then revises the formula once and shows the ranking change. Narrated by **Liam**
(local Kokoro `am_onyx` voice).

---

## The files

| File | What it is | Use |
|---|---|---|
| `WSJF-ProjectManagement-16x9-4K.mp4` | 16:9 landscape master, 3840 × 2160 (4K) | YouTube main video |
| `WSJF-ProjectManagement-9x16-4K.mp4` | 9:16 vertical master, 2160 × 3840 (4K) | YouTube Shorts / Reels / TikTok |
| `BEATSHEET-16x9.json` | The 16:9 beat sheet (shot-by-shot script) | Source / re-edit |
| `BEATSHEET-9x16.json` | The 9:16 beat sheet | Source / re-edit |
| `PROOF-REVIEW-RESULTS.md` | Skeptical self-review of both cuts (score /12, gate, punch list) | QA record |
| `README.md` | This file | — |

- **Frame rate:** 24 fps · **Audio:** AAC stereo · **Codec:** H.264 (`yuv420p`, `+faststart`)
- Both are self-contained masters, ready to upload. On YouTube, force **2160p** in the
  quality menu to see true 4K (the "Auto" setting serves a soft transcode right after upload).

## What's in the video

Opening line: *"Hi, this is Liam for Sanjana, and this video is about WSJF — Weighted
Shortest Job First."* Then:

1. **The problem** — backlogs get ordered by the loudest voice or by raw business value,
   so the biggest feature goes first and the quarter is spent on the wrong thing.
2. **The framework** (shown before any example) — **WSJF = Cost of Delay ÷ Job Size**,
   where **Cost of Delay = Business Value + Time Criticality + Risk Reduction**.
3. **Build it with Claude** — the prompt → the real `wsjf.py` code → the backlog
   animating into ranked order (value ÷ size): the cheap "Checkout bug fix" jumps to #1,
   the big "New onboarding flow" sinks despite its high value.
4. **The revision** — Cost of Delay isn't just value. Add time-criticality and risk
   reduction, re-rank, and the urgent/risky "API rate limiting" leaps from #4 to #2.
5. **The method + its limits** — one formula for any backlog, plus two honest caveats:
   WSJF is **blind to dependencies**, and it's only as good as your estimates.
6. **Your turn** — a copy-paste prompt the viewer can run on their own backlog.

The rankings on screen are **real**: they're computed by `../src/wsjf.py` from
`../src/backlog.csv` (run `python3 -I wsjf.py` in `src/` to reproduce them).

## Branding

- **@HumanitariansAI** appears in the intro composer, as a low-opacity corner watermark
  throughout, and on the closing title card.
- Visual style: the Claude desktop-app palette (cream page, warm ink, one terracotta accent).

## Source & reproduction

This folder holds the finished masters. The source lives one level up:

- `../beat_sheet.json` — the shot-by-shot script (the whole film is derived from it)
- `../src/wsjf.py`, `../src/backlog.csv` — the real, runnable WSJF code and data
- `../FACTCHECK.md`, `../SOURCES.md`, `../SHOTLIST.md` — claims, references, shot list
- `../vertical/` — the 9:16 companion's own beat sheet

Credits: Weighted Shortest Job First — Scaled Agile Framework (SAFe); Cost of Delay —
Reinertsen, *The Principles of Product Development Flow*.
