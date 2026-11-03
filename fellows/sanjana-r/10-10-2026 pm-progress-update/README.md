# The Last Mile — Humanitarians AI Fellows Progress Record

A Claude-styled (cream + terracotta) brutalist **explainer** with voiceover — a
first-person progress record of Sanjana's video-review week of **Oct 4–10, 2026**, that
also teaches a reusable craft check: the **last mile** between a *finished* video and a
*shipped* one. Customized for Sanjana · @HumanitariansAI.

## The masters (both true 4K, 24 fps, with audio)

| File | Aspect | Resolution | Length | Use |
|---|---|---|---|---|
| `The-Last-Mile__16x9_4K_YouTube.mp4` | 16:9 landscape | 3840×2160 | ~3:35 | Main YouTube video |
| `the-last-mile-short/The-Last-Mile__9x16_Short.mp4` | 9:16 vertical | 2160×3840 | ~0:46 | YouTube Shorts |

Intro & outro use the Claude scenes (ClaudeComposerAsk, EB Garamond serif). The intro
opens with Sanjana's spoken hello ("Hi, I'm Sanjana…"). The outro is a **custom
@HumanitariansAI title card** (the house ClaudeTitleOutro is hardcoded to @NikBearBrown, so
an HAI reel ships its own). The body uses a **new visual language** vs the prior films: a
film-strip throughput counter, an export-style progress checklist, and literal 16:9 / 9:16
screen panes that *show* the portrait defect rather than describe it.

**Audio:** Kokoro `af_bella` voiceover (local, free, no account). Narration is the master
clock — the visuals are cut to the voice. Beat boundaries use cross-dissolve-through-cream
transitions.

**Native 4K flat-vector render** (Manim + Remotion) — do not run Topaz/upscaling. Judge at
forced 2160p, not "Auto."

## The week on record (all figures from Sanjana's October review log)
- **85 videos reviewed** · **13 fellows** · **1 project: Mycroft** · **100% on GitHub**
- **14 reviews: 12 uploaded for the professors / 2 Needs Modifications**
- The two sent back (the film's falsifiability cases): a stray toolkit **footer** baked in,
  and a broken **9:16** with overlapping text — both passing the old gate.
- Also this week: planning calls with Akshay & Jainil (Oct 6); created 4 videos for the
  weekly upload (Oct 8).

## What it teaches (THE LAST MILE — the flow)
The rule: **content done is not the same as shipped.** Before a fellow video reaches the
professors, check how the *file* plays:
1. **CLEAN FINISH?** — no leftover toolkit footer/watermark baked into the render.
2. **PORTRAIT HOLDS?** — the 9:16 is its own layout, not a squeezed 16:9 — no overlapping text.
3. **ON GITHUB?** — code + assets committed.
4. **Three pass → uploaded for the profs.** Any fail → back to the fellow with a mail.
5. **Worked example** — a clean submission clears all three.
6. **The trap** — two finished-looking videos each fail a *different* check, both passing
   the old gate; the last mile is the only thing that catches them.
7. **Your turn** — run your own last mile before you submit (copyable prompt in the video).

## Companion files
- `beat_sheet.json` — the 10-beat structure (audio-first, conform-to-audio)
- `build_sheet.py` — authoring script that emits the beat sheet
- `scenes.py` — the Manim concept scenes (16:9); `…-short/scenes_short.py` for 9:16
- `add_transitions.py` — cross-dissolve-through-cream pass
- `SHOTLIST.md` · `SOURCES.md` · `FACTCHECK.md` · `PROMPTS.md` — shot plan, no-fabrication audit, on-screen prompts
- `CHECKS-REPORT.md` · `BUILD-LOG.md` — gate report + build notes
- `PROOF-REVIEW.md` — self-assessment against the PROOF rubric
- `description.txt` — ready-to-paste YouTube description

## Delivery / next steps
- Delivered to this folder (**not pushed to GitHub**, per the user's instruction).
- Rendered with the **brutalist.art** Remotion + Manim toolkit · Kokoro `af_bella` voice.
