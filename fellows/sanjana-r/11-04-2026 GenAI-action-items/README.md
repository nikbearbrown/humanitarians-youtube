# Who Does What, By When — explainer video

A short **Gen AI Tools in Management** explainer made for **Sanjana**, produced with the
Brutalist video toolkit and watermarked **@HumanitariansAI**.

The film teaches how to use a Gen AI tool to turn a **meeting transcript into ranked,
owned, dated action items** — by building it with Claude on screen: the prompt, the real
Python, and the actions **sorting themselves** while the gaps (no owner / no date) get
flagged. Narrated by **Liam** (local Kokoro `am_onyx` voice).

---

## The files

| File | What it is | Use |
|---|---|---|
| `GenAI-Meetings-ActionItems-16x9-4K.mp4` | 16:9 landscape master, 3840 × 2160 (4K) | YouTube main video |
| `GenAI-Meetings-ActionItems-9x16-4K.mp4` | 9:16 vertical master, 2160 × 3840 (4K) | YouTube Shorts / Reels / TikTok |
| `BEATSHEET-16x9.json` | The 16:9 beat sheet (shot-by-shot script) | Source / re-edit |
| `BEATSHEET-9x16.json` | The 9:16 beat sheet | Source / re-edit |
| `PROOF-REVIEW-RESULTS.md` | Skeptical self-review of both cuts (score /12, gate, punch list) | QA record |
| `README.md` | This file | — |

- **Frame rate:** 24 fps · **Audio:** AAC stereo · **Codec:** H.264 (`yuv420p`, `+faststart`)
- On YouTube, force **2160p** in the quality menu to see true 4K (Auto serves a soft transcode).

## What's in the video

Opening line: *"Hi, this is Liam for Sanjana, and this video is about using a Gen AI tool to
turn a messy meeting into a ranked list of who does what, by when."* Then:

1. **The problem** — meetings end and nothing moves; the easy AI move ("summarize") gives a
   tidy paragraph nobody owns.
2. **The framework** (before any example) — a real action item = **owner + task + due**,
   triaged by **priority = impact + urgency**. The rule: *no owner or no date → not an action yet.*
3. **Pass 1 — summarize** — the prompt → the naive code → five topics with no owners, no dates.
4. **Pass 2 — extract + triage** — revise the prompt → the real triage code → the actions
   ranked by priority, with the two gaps (SSL cert has no owner; interviews have no owner or
   date) flagged in terracotta.
5. **The method + its limits** — one move for any meeting, plus the honest caveats: the tool
   only hears what was said, and every action should trace to a line (no source, no verdict).
6. **Your turn** — a copy-paste prompt to run on the viewer's own meeting.

The actions and priorities on screen are **real** — computed by `../src/actions.py` from
`../src/transcript.txt` (run `python3 -I actions.py` in `src/` to reproduce them).

## Branding

- **@HumanitariansAI** appears in the intro composer, as a low-opacity corner watermark
  throughout, and on the closing title card.
- Visual style: the Claude desktop-app palette (cream page, warm ink, one terracotta accent
  used only to flag the gaps).

## Source & reproduction

Finished masters are in this folder. Source lives one level up:

- `../beat_sheet.json` — the shot-by-shot script
- `../src/actions.py`, `../src/transcript.txt` — the real, runnable extraction + triage and the meeting
- `../FACTCHECK.md`, `../SOURCES.md`, `../SHOTLIST.md` — claims, references, shot list
- `../vertical/` — the 9:16 companion's own beat sheet

Credits: action-item discipline (owner + task + due) — standard meeting-notes / GTD practice;
impact × urgency triage — Eisenhower-style prioritization.
