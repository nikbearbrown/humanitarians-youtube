# CHECKS-REPORT — weekly-recap-we-ask

## Chassis

User asked for a "CLI Explainer" (about 3 minutes, no longer). Built on the
`cli-explainer` spine: B00 cold open with intro → ASK → CODE → OUTPUT (x4 parts) → CHANGE →
CODE → OUTPUT → closing line → HANDOFF → OUTRO, matching `weekly-recap-real-art` and the
earlier recaps. The PROBLEM beat of the earlier recaps is dropped so the recap stays well
inside the 3-minute limit; the intro, the checklist idea and the four parts are all still
there. Total 146.1 s (2:26). The 16:9 carries the required revision cycle; the 9:16 keeps
every beat.

## Disclosed deviations

1. **Voice/branding** — af_bella (Kokoro) + @HumanitariansAI instead of the skill's
   default voice and handle; this was the user's request.
2. **Register** — professional, polite, simple (user request), not the Teardown
   register; no overhyping; the Homes of Hope work is called ongoing, not finished.
3. **Pacing** — the brief asked for about 30 to 40 seconds per part. Measured: writing
   37.9 s, video production 21.6 s, weekly meeting 9.4 s, Homes of Hope 20.1 s. The
   writing part uses its full allotment; the others are shorter because the user's own
   summaries are two to three sentences (and part four may give no detail beyond
   "ongoing"), and padding them to 30 seconds would have made the recap feel padded,
   which the user's revision prompt warns against. The whole recap is under the limit.
4. **Output beat is four beats** — the "run" output is split into one beat per part
   (B03–B06) so each part has the screen to itself and the narration does not move too
   fast; all four are Manim SHOW beats timed to the audio.
5. **Revision** — v1 → v2 adds a status to each part and prints a count (published,
   produced, attended, ongoing), because the Homes of Hope work is ongoing and the honest
   update says so.
6. **Pipeline** — run.sh / compile.py / static_scene_check.py /
   manim_layout_audit.py / final_frame_check.py, as on every reel this session.
7. **Visuals** — all generated; no footage, no photos of children or real people, no
   real platform or company logos (user instruction).
8. **Self-reported claims** — every item is the user's own account; see FACTCHECK.md.

## PROOF GATE

13 beats classify SHOW (Manim beats name their on-screen artifact in `visual_intent`) or
CARD/CODE bookends (Remotion composer/code/outro). Arc: framework ✓ (the four-part
checklist in B00/B01) · worked example ✓ (B03–B06, one per part) · falsifiability ✓
(B07–B09: the status revision makes the ongoing part visible) · scaffolded viewer task ✓
(B11 handoff prompt) · four bookends ✓ · no-source-no-verdict ✓ (FACTCHECK.md: all items
are the user's self-report; no survey numbers are used).

## GATE A / GATE B (before any pipeline run)

GATE A: zero ERROR on all six scenes (B10 WARN: text-only, expected). GATE B: all six
CLEAN. Two fixes found by viewing preview frames: in B03 the "mock article header"
caption sat on top of the takeaway chip (moved into the article card), and in B06 the
"Supports marginalized girls in India" line touched the three support chips (moved up).
