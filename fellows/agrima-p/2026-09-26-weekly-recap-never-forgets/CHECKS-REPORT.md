# CHECKS-REPORT — weekly-recap-never-forgets

## Chassis

User asked for a "CLI Explainer" by name — built on the `cli-explainer`
skill's required story spine (cold open -> PROBLEM -> ASK -> CODE -> OUTPUT
-> CHANGE -> CODE -> OUTPUT -> SUMMARY -> NEXT STEPS -> OUTRO), matching the
precedent set by this user's earlier `weekly-recap`, `weekly-recap-catbot`,
and `weekly-recap-suffolk` projects (same skill, different weeks' content —
built in its own folder here, not overwriting any prior build).

**Structural difference from the prior weekly-recap builds:** this week's
three items (article published, four videos produced, one meeting attended)
are all already-done — the kickoff names no upcoming/next-week item. So the
v1->v2 CHANGE beat is NOT a DONE/NEXT split (unlike every prior weekly-recap
build); it's a flat-list-to-tagged-and-counted revision instead. This is a
genuinely different but equally real code change, chosen because it's the
only honest revision available given this week's actual content shape.

## Disclosed deviations (carried forward from the earlier weekly-recap builds)

1. **Voice/branding** — af_bella (Kokoro) + @HumanitariansAI instead of the
   skill's default Teardown register / am_onyx voice / @NikBearBrown handle,
   per the user's explicit request for "the most natural-sounding female
   voice."
2. **Render pipeline** — `vox_run.sh` / `vox_compile.py` / `type_check.py`
   (the skill's documented tooling) do not exist anywhere in this toolkit
   install. Rendered instead through run.sh / compile.py /
   static_scene_check.py / manim_layout_audit.py / final_frame_check.py, the
   same pipeline used on every other reel this session.
3. **Self-intro placement** — "Hi, I'm Agrima" stays folded into B00's own
   narration (cli-explainer's own reference-example convention), NOT split
   into a dedicated B00B beat. That B00B pattern belongs to this user's
   ai-explainer-chassis builds (a different skill with a different
   convention) — matching the precedent already set by every prior
   weekly-recap build.

## THE ACTUAL-CODE LAW

`weekly_recap_v1.py` and `weekly_recap_v2.py` are both genuine, runnable
Python scripts — both were actually executed before writing the CODE/OUTPUT
beats' content; nothing in B03/B04/B06/B07 is invented output.

## GATE A (static pre-flight)

- B01_NotAHighlightReel: WARN (text-only, no tracked shapes — expected)
- B04_FlatWeek: CLEAN
- B07_TaggedWeek: CLEAN
- B08_TheLesson: WARN (text-only, no tracked shapes — expected)

Zero ERROR across all four scenes.

## GATE B (real pixel-level layout audit)

- B01_NotAHighlightReel: 5 snapshots -> CLEAN
- B04_FlatWeek: 6 snapshots -> CLEAN
- B07_TaggedWeek: 6 snapshots -> CLEAN
- B08_TheLesson: 5 snapshots -> CLEAN

All four scenes CLEAN on the real pixel-level check, zero errors, zero
warnings. Also spot-checked via a real low-quality render + pulled
confirmation frames for B04 and B07 (including a close zoom on the
"Meetings" tag chip, the tightest-fitting label) before proceeding to the
full pipeline — all fully contained, no overflow.

## Duration

Estimated ~97s across 11 beats (1:37), within the user's requested 1-3
minute range. Real durations are the Kokoro mp3 lengths, measured before
rendering, per this toolkit's audio-first principle.
