# The Review Gate — My Two Weeks at Humanitarians AI (Fellows Progress Record)

A Claude-styled (cream + terracotta) brutalist **progress record** with voiceover, showing
the two-week Fellows video-review pipeline as a repeatable quality gate: how 88 fellow
videos were checked, what passed, and what bounced back. Customized for Sanjana ·
@HumanitariansAI.

## The masters (both true 4K, 24 fps, with audio)

| File | Aspect | Resolution | Length | Use |
|---|---|---|---|---|
| `The-Review-Gate__16x9_4K_YouTube.mp4` | 16:9 landscape | 3840×2160 | ~3:21 | Main YouTube video |
| `the-review-gate-short/The-Review-Gate__9x16_Short.mp4` | 9:16 vertical | 2160×3840 | ~0:45 | YouTube Shorts |

Intro & outro use the Claude scenes (ClaudeComposerAsk, EB Garamond serif). The intro
opens with Sanjana's spoken hello ("Hi, I'm Sanjana…"). The outro is a **custom
@HumanitariansAI title card** (the house ClaudeTitleOutro is hardcoded to @NikBearBrown,
so an HAI reel ships its own). The body is a concept-illustration run in the Claude palette
(gate stations, stat tiles, a project ranking, a segmented approval bar, a GitHub
compliance arc, and the fix-loop).

**Audio:** Kokoro `af_bella` voiceover (local, free, no account). Narration is the master
clock — the visuals are cut to the voice. Beat boundaries use cross-dissolve-through-cream
transitions.

**Native 4K flat-vector render** (Manim + Remotion) — do not run Topaz/upscaling. Judge at
forced 2160p, not "Auto."

## What it teaches (THE REVIEW GATE — the pipeline flow)
Every fellow video clears three checks before a professor sees it:
1. **Intake** — a fellow's batch lands for review (88 videos, 22 fellows, 8 projects across Sep 16–30).
2. **Check 1 — 4K on both cuts?** the 16:9 AND the 9:16 short are true 4K (not HD, not zoomed).
3. **Check 2 — right branding?** the @HumanitariansAI handle, not a leftover @NikBearBrown.
4. **Check 3 — code on GitHub?** committed, with correct dimensions.
5. **3 pass → APPROVED** — uploaded to YouTube for Prof. Nina to review.
6. **Any fail → back to the fellow** with an email saying exactly what to fix.
7. **The fix loop** — fellow re-uploads, re-checked, approved (e.g. Deepa 16, Harshitha 8, Neelabh 1).

The two-week scoreboard (all verified from the tracker): **88 reviewed · 78 approved /
10 sent back · 71 of 88 (~81%) on GitHub.** Data source: `September Videos` sheet, Sep 16–30.

## Companion files
- `beat_sheet.json` — the 10-beat structure (audio-first, conform-to-audio)
- `build_sheet.py` — authoring script that emits the beat sheet
- `scenes.py` — the Manim concept/data scenes (16:9); `…-short/scenes_short.py` for 9:16
- `add_transitions.py` — cross-dissolve-through-cream pass
- `SHOTLIST.md` · `SOURCES.md` · `FACTCHECK.md` · `PROMPTS.md` — shot plan + every number traced to the tracker
- `CHECKS-REPORT.md` · `BUILD-LOG.md` · `BUILD-PROMPT.md` — gate report, build notes, paste-ready rebuild prompt
- `PROOF-REVIEW.md` — self-assessment against the PROOF rubric (**11/12, production gate PASS**)
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
- Open item (confirm with Professor Brown): whether progress-record MP4s live in a
  `Tutorials/`-style Drive subfolder or the general finished folder.
- Rendered with the **brutalist.art** Remotion + Manim toolkit · Kokoro `af_bella` voice.
