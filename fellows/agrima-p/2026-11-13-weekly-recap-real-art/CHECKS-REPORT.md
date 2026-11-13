# CHECKS-REPORT — weekly-recap-real-art

## Chassis

User asked for a "CLI Explainer" (1–3 minutes, no longer than 3). Built on the
`cli-explainer` spine: B00 cold open with intro → PROBLEM → ASK → CODE → OUTPUT (x4
parts, part four in two beats) → CHANGE → CODE → OUTPUT → LESSON → HANDOFF → OUTRO,
matching `weekly-recap-foundation-search` and the earlier recaps. Total 140.6 s (2:21).
The 16:9 carries the required revision cycle; the 9:16 keeps every beat (the recap is
under the 3:00 Shorts cap).

## Disclosed deviations

1. **Voice/branding** — af_bella (Kokoro) + @HumanitariansAI instead of the skill's
   default voice and handle; this was the user's request.
2. **Register** — professional, polite, simple (user request), not the Teardown
   register; no overhyping; CatBot and DogBot is called an early-stage plan throughout.
3. **Output beat is five beats** — the "run" output is split into one beat per part
   (B04–B06) and two for the new project (B07 the idea and first step, B08 what comes
   next), so each part has the screen to itself and the narration does not move too fast.
4. **Revision** — v1 → v2 adds a status to each part and prints a count (published,
   produced, saved, planning), because the new project is a plan and the honest update
   says so.
5. **New-project length** — the request asked for "about 40 seconds"; B07 + B08 measure
   44.1 s (32.4 + 11.7). Trimmed once from 46.3 s; further cuts would have dropped
   details the user listed.
6. **Pipeline** — run.sh / compile.py / static_scene_check.py /
   manim_layout_audit.py / final_frame_check.py, as on every reel this session.
7. **Visuals** — all generated; no footage, no photos of real animals, shelters or
   people, no real platform logos (user instruction). The map is a generic panel
   labeled "generic map -- not to scale".
8. **Self-reported claims** — every item is the user's own account; see FACTCHECK.md.
   The GitHub claim is the user's statement and was not yet true for this week's new
   files at build time.
9. **Hard limits honored** — the video does not say the demo is built and does not say
   any shelter has agreed to take part; the steps carry "planned" tags and the section
   carries an "Early-stage plan" label.

## PROOF GATE

15 beats classify SHOW (Manim beats name their on-screen artifact in `visual_intent`)
or CARD/CODE bookends (Remotion composer/code/outro). Arc: framework ✓ (B01
four-part checklist) · worked example ✓ (B04–B08, one per part) · falsifiability ✓
(B09–B11: the status revision makes the in-planning part visible) · scaffolded viewer
task ✓ (B13 handoff prompt) · four bookends ✓ · no-source-no-verdict ✓ (FACTCHECK.md:
all items are the user's self-report).

## GATE A / GATE B (before any pipeline run)

GATE A: zero ERROR on all eight scenes (B12 WARN: text-only, expected). GATE B: all
eight CLEAN. Fixes found by the gates and by viewing preview frames: B07 and B08 first
failed the "shapes never change" check (everything was revealed by opacity; switched to
plain fade-ins), a "one pilot shelter" label touched the map panel (panel moved), and
by eye: the "made with Brutalist" chip ran into the B05 heading, the B07 bottom row's
cards touched each other, the CatBot and DogBot labels sat at different heights, and
the B08 subtitle crowded the heading (each re-spaced).
