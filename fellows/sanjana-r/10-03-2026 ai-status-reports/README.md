# AI Status Reports: Trust, but Verify — Humanitarians AI Fellows Explainer

A Claude-styled (cream + terracotta) brutalist **explainer** with voiceover, teaching when
to trust an AI-written project status report — and the three checks to run before you
forward one to a stakeholder. Customized for Sanjana · @HumanitariansAI.

## The masters (both true 4K, 24 fps, with audio)

| File | Aspect | Resolution | Length | Use |
|---|---|---|---|---|
| `AI-Status-Reports__16x9_4K_YouTube.mp4` | 16:9 landscape | 3840×2160 | ~4:13 | Main YouTube video |
| `ai-status-reports-short/AI-Status-Reports__9x16_Short.mp4` | 9:16 vertical | 2160×3840 | ~0:43 | YouTube Shorts |

Intro & outro use the Claude scenes (ClaudeComposerAsk, EB Garamond serif). The intro
opens with Sanjana's spoken hello ("Hi, I'm Sanjana…"). The outro is a **custom
@HumanitariansAI title card** (the house ClaudeTitleOutro is hardcoded to @NikBearBrown, so
an HAI reel ships its own). The body is a concept-illustration run in the Claude palette
(status-report cards with a green ON TRACK badge, verification stamps, red failure stamps,
and an AI-drafts → gate → you-sign router).

**Audio:** Kokoro `af_bella` voiceover (local, free, no account). Narration is the master
clock — the visuals are cut to the voice. Beat boundaries use cross-dissolve-through-cream
transitions.

**Native 4K flat-vector render** (Manim + Remotion) — do not run Topaz/upscaling. Judge at
forced 2160p, not "Auto."

## What it teaches (THE SIGN-OFF — the flow)
The rule: the AI drafts the status, **you sign it**. Before it reaches a stakeholder:
1. **AI drafts** — it reads the board and writes the status prose fast.
2. **Check SOURCED?** — every claim points to a real ticket or date, not confident filler.
3. **Check CURRENT?** — the board behind it isn't stale (a status is only as true as its board).
4. **Check COMPLETE?** — you add the off-board risk the AI can't see (the vendor, the sick engineer, the call).
5. **All three pass → SIGN & SEND** to the stakeholder.
6. **Any fail → fix first** — never forward a confident paragraph with no sources.
7. **The trap** — an "all green, on track" report can fail all three at once (unsourced guess, 10-day-stale board, invisible blocker): the sign-off catches it.
8. **Your turn** — have the AI draft the status, tag every claim with its source, and separately list what it could NOT verify; that second list is your checklist.

This is a concept explainer — the example sprints shown are illustrative, not real project
data (see `FACTCHECK.md`).

## Companion files
- `beat_sheet.json` — the 10-beat structure (audio-first, conform-to-audio)
- `build_sheet.py` — authoring script that emits the beat sheet
- `scenes.py` — the Manim concept scenes (16:9); `…-short/scenes_short.py` for 9:16
- `add_transitions.py` — cross-dissolve-through-cream pass
- `SHOTLIST.md` · `SOURCES.md` · `FACTCHECK.md` · `PROMPTS.md` — shot plan, no-fabrication audit, on-screen prompts
- `CHECKS-REPORT.md` · `BUILD-LOG.md` — gate report + build notes
- `PROOF-REVIEW.md` — self-assessment against the PROOF rubric (**12/12, production gate PASS**)
- `description.txt` — ready-to-paste YouTube description

### Fellow folder README template (what a fellow copies into their own folder)
```
# <Firstname Lastname> — Fellow

Beat sheet & script are in this folder.
The final videos live on Google Drive:

[▶ Watch on Google Drive](https://drive.google.com/…/your-folder)
```

## Delivery / next steps
- Delivered to this folder (**not pushed to GitHub**, per project convention).
- Open item (confirm with Professor Brown): whether explainer MP4s live in a
  `Tutorials/`-style Drive subfolder or the general finished folder.
- Rendered with the **brutalist.art** Remotion + Manim toolkit · Kokoro `af_bella` voice.
