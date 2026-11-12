# CHECKS-REPORT — weekly-recap-foundation-search

## Chassis

User asked for a "CLI Explainer" (1–3 minutes). Built on the `cli-explainer` spine:
B00 cold open with intro → PROBLEM → ASK → CODE → OUTPUT (x4 parts) → CHANGE → CODE →
OUTPUT → LESSON → HANDOFF → OUTRO, matching `weekly-recap-brand-check` and the earlier
recaps. The 16:9 carries the required revision cycle; the 9:16 keeps every beat (the
recap is under the 3:00 Shorts cap).

## Disclosed deviations

1. **Voice/branding** — af_bella (Kokoro) + @HumanitariansAI instead of the skill's
   default voice and handle; this was the user's request.
2. **Register** — professional, polite, simple (user request), not the Teardown
   register; no overhyping; the outreach is called ongoing, not finished.
3. **Output beat is four beats** — the "run" output is split into one beat per part
   (B04–B07) so each part has the screen to itself and the narration does not move
   too fast; all four are Manim SHOW beats timed to the audio.
4. **Revision** — v1 → v2 adds a status to each part and prints a count (not a
   role/count revision), because the outreach is ongoing and the honest update says so.
5. **Pipeline** — run.sh / compile.py / static_scene_check.py /
   manim_layout_audit.py / final_frame_check.py, as on every reel this session.
6. **Visuals** — all generated; no footage, no photos, no people, no real platform
   logos (user instruction).
7. **Self-reported claims** — every item is the user's own account; see FACTCHECK.md.
   The GitHub claim is the user's statement and was not yet true for this week's
   foundation-search files at build time.

## PROOF GATE

14 beats classify SHOW (Manim beats name their on-screen artifact in `visual_intent`)
or CARD/CODE bookends (Remotion composer/code/outro). Arc: framework ✓ (B01
four-part checklist) · worked example ✓ (B04–B07, one per part) · falsifiability ✓
(B08–B10: the status revision makes the ongoing part visible) · scaffolded viewer
task ✓ (B12 handoff prompt) · four bookends ✓ · no-source-no-verdict ✓
(FACTCHECK.md: all items are the user's self-report).

## GATE A / GATE B (before any pipeline run)

GATE A: zero ERROR on all seven scenes (B11 WARN: text-only, expected). GATE B: all
seven CLEAN. Two fixes found by looking at preview frames: in B05 the "Weekly work
recap" label ran into the 16:9 tile (label shortened to "Weekly recap"); in B07 the
heading and the "GitHub" label touched the folder icon (icon and labels re-spaced).
