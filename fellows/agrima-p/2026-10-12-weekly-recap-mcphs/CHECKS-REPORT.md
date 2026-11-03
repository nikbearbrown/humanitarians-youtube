# CHECKS-REPORT — weekly-recap-mcphs

## Chassis

CLI Explainer (cli-explainer chassis), same story spine as the earlier
weekly-recap builds: cold open → problem → ask → code → output → change →
code → output → body → handoff → outro. Self-intro "Hi, I'm Agrima" is in
B00's own narration, per that chassis's convention. The body (B08–B12) is the
guest-lecture summary the user asked for, about half the runtime.

## Disclosed deviations

1. **Voice/branding** — af_bella (Kokoro) + @HumanitariansAI, per the user's
   earlier requests, not the skill's default voice/handle.
2. **Pipeline** — run.sh / compile.py / static_scene_check.py /
   manim_layout_audit.py / final_frame_check.py, as on every reel this session.
3. **Revision cycle** — v1 → v2 tags each item by category and prints a count
   (not a DONE/NEXT split: the lecture has already been given, so nothing is
   upcoming).
4. **No slide images** — the presentation PDF could not be rendered to images
   on this machine (no PDF renderer installed; Edge's headless viewer returned
   a blank page). Text was extracted with pdftotext and every visual is
   generated. The user allowed slide visuals only "where they help".
5. **Lecture share** — the lecture beats are ~59% of the runtime (101 s of
   172.6 s) against "about half": the user's brief lists seven topics, and the
   narration was trimmed twice to hold the total under 3:00.

## Instructions followed (verified, not assumed)

- A word/name scan of every beat's narration, on-screen props and
  visual_intent, scenes.py and the paperwork found no mention of any
  individual's name, background or identity, and no jokes about anyone; the
  narration says "the team". Excluded slides (2, 3, 7, 8) are not used.
- No photos of children; the Homes of Hope India / Wilkes topics use icons and
  on-screen text only. Third-party people named in the PDF are not named.

## GATE A / GATE B (before any pipeline run)

GATE A: zero ERROR (B01 text-only WARN, expected). GATE B: all eight scenes
CLEAN. One fix: in B11 the "what it tracks" label touched its card's border
(the two lake/right cards were too short for their contents); both were made
taller. Preview frames of all seven card scenes were viewed.

## Duration

First narration pass measured 184.4 s (over the "no longer than about 3
minutes" limit); two trims of the lecture beats (keeping every topic) brought
the measured mp3 total to **172.58 s (2:52.6)**.
