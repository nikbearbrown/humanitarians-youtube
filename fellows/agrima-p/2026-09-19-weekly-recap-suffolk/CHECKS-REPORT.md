# CHECKS-REPORT — weekly-recap-suffolk

## Chassis

User asked for a "CLI Explainer" by name — built on the `cli-explainer`
skill's required story spine (cold open -> PROBLEM -> ASK -> CODE -> OUTPUT
-> CHANGE -> CODE -> OUTPUT -> SUMMARY -> NEXT STEPS -> OUTRO), matching the
precedent set by both this user's earlier `weekly-recap` and
`weekly-recap-catbot` projects (same skill, different weeks' content — built
in its own folder here, not overwriting either prior build).

## Disclosed deviations (carried forward from the earlier weekly-recap builds)

1. **Voice/branding** — af_bella (Kokoro) + @HumanitariansAI instead of the
   skill's default Teardown register / am_onyx voice / @NikBearBrown handle,
   per the user's explicit request for "the most natural-sounding female
   voice."
2. **Render pipeline** — `vox_run.sh` / `vox_compile.py` / `type_check.py`
   (the skill's documented tooling) do not exist anywhere in this toolkit
   install (re-verified: not found under runtime/scripts or runtime/qc for
   this build). Rendered instead through run.sh / compile.py /
   static_scene_check.py / manim_layout_audit.py / final_frame_check.py, the
   same pipeline used on every other reel this session.
3. **Self-intro placement** — "Hi, I'm Agrima" stays folded into B00's own
   narration (cli-explainer's own reference-example convention), NOT split
   into a dedicated B00B beat. That B00B pattern belongs to this user's
   ai-explainer-chassis builds (a different skill with a different
   convention) — matching the precedent already set by both earlier
   weekly-recap builds.

## THE ACTUAL-CODE LAW

`weekly_recap_v1.py` and `weekly_recap_v2.py` are both genuine, runnable
Python scripts — both were actually executed before writing the CODE/OUTPUT
beats' content; nothing in B03/B04/B06/B07 is invented output.

## GATE A (static pre-flight)

- B01_NotAHighlightReel: WARN (text-only, no tracked shapes — expected)
- B04_FlatWeek: CLEAN
- B07_SplitWeek: CLEAN
- B08_TheLesson: WARN (text-only, no tracked shapes — expected)

Zero ERROR across all four scenes.

## GATE B (real pixel-level layout audit)

- B01_NotAHighlightReel: 5 snapshots -> CLEAN
- B04_FlatWeek: 6 snapshots -> CLEAN
- B07_SplitWeek: 8 snapshots -> CLEAN
- B08_TheLesson: 5 snapshots -> CLEAN

All four scenes CLEAN on the real pixel-level check, zero errors, zero
warnings.

## Duration

Estimated ~140s across 11 beats (2:20), within the user's requested 1-3
minute range for the 16:9 cut. Real durations are the Kokoro mp3 lengths,
measured before rendering, per this toolkit's audio-first principle.
