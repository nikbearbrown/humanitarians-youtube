# Name It, Own It, Date It. — the RAID log (cli-explainer)

A **cli-explainer** made for **Sanjana**, produced with the Brutalist video toolkit and
watermarked **@HumanitariansAI**. Narrated by **Liam** (local Kokoro `am_onyx` voice).

**Topic (project management):** turning a messy project status update into a clean **RAID log** —
**R**isk, **A**ssumption, **I**ssue, **D**ependency — each item *typed, owned, and dated*, with the
gaps (no owner or no date) flagged. The point isn't listing worries; it's **classifying** them.

---

## The files

| File | What it is | Use |
|---|---|---|
| `RAIDLog-NameItOwnItDateIt-16x9-4K.mp4` | 16:9 landscape master, 3840 × 2160 (4K) | main video |
| `RAIDLog-NameItOwnItDateIt-9x16-4K.mp4` | 9:16 vertical master, 2160 × 3840 (4K) | Shorts / Reels |
| `BEATSHEET-16x9.json` / `BEATSHEET-9x16.json` | Shot-by-shot scripts | Source / re-edit |
| `PROOF-REVIEW-RESULTS.md` | Self-review (production gate + teaching rubric) | QA record |
| `README.md` | This file | — |

- 24 fps · AAC stereo · H.264 (`yuv420p`, `+faststart`). Force **2160p** on YouTube for true 4K.

## What's in the video

Opening line: *"Hi, this is Liam for Sanjana, and this video is about using a Gen A I tool to turn
a messy project status update into a clean RAID log…"* Then:

1. **The problem** — ask AI to "list the risks" and it calls everything a risk, including the
   things already on fire.
2. **The frame (before any example)** — R/A/I/D defined, plus the rule: **no owner or no date → it
   isn't tracked, it's just a worry.**
3. **Pass 1 — "list the risks"** — the real naive code, and its flat one-pile output (7 lines, all
   "risk", no owner/date).
4. **Pass 2 — "classify"** — the real `raid.py` sorts each line into its lane and flags the gaps.
5. **The result** — four lanes, every item owned and dated; two "already-happening" lines re-typed
   from Risk to **Issue**, a Dependency pulled out of "risks", and two unowned assumptions flagged.
6. **Limits** — the model can mis-type vague wording and can't invent an owner; verify tense and
   ownership.
7. **Your turn, Sanjana** — a copy-paste prompt to run on your own status update each week.

## How it was built

- **Executable evidence:** `../src/raid.py` run against `../src/status_update.txt`; the on-screen
  board is its real output (see `../FACTCHECK.md`).
- **Dual-aspect** native-4K render (Remotion), one terracotta accent used structurally for the
  gaps only, Claude palette throughout.

## Branding

- **@HumanitariansAI** in the intro composer chrome, a corner watermark throughout, and the
  outro card.

## Source

- `../beat_sheet.json`, `../src/`, `../FACTCHECK.md`, `../SOURCES.md`, `../PROMPTS.md`,
  `../SHOTLIST.md`, `../vertical/`
