# BUILD-PROMPT — Kokoro: All 28 English Voices (The Full Roster)

COMPANION REFERENCE CUT to youtube/kokoro-free-voices (the short film). This one is for
people who want to hear the full 28 before casting. beat_sheet.json is ALREADY AUTHORED
(30 beats: EL intro + 28 roster + Heart's close) — do not re-author. PEDAGOGY.md carries
VERDICT: PASS. No chapter_number: it rides outside the chapter order as a reference.

Standing rules #1–#4 (EXAMPLES-CAMPAIGN.md) apply. Prereq: Phase A of the short film's
BUILD-PROMPT (kokoro-onnx + model files) must already be done — if not, do it first.

## Build

1. FACTCHECK: python3 runtime/scripts/generate_audio_kokoro.py --list-voices — confirm
   all 28 sheet voices exist and the English count is exactly 28. Grades came from
   hexgrad/Kokoro-82M VOICES.md 2026-07-13 — re-verify; correct sheet + cards on any
   drift. Write FACTCHECK.md.
2. Audio: generate_audio.py --only B00 (the only paid beat; record cents in BUILD-LOG),
   then generate_audio_kokoro.py for the rest ($0.00). LISTEN to a handful across the
   grade range — the rough ones stay rough (that is the point of a graded sampler), but
   a mispronounced NAME gets a spoken-form fix in that beat's narration text.
3. Author ONE new Remotion component: KokoroRosterCard (name, code, group, grade,
   index, topic — zod schema, house palette; the grade chip color follows the grade:
   teal A/B, ink C, red D/F; a small 916 variant KokoroRosterCard916 while you are in
   there, for the short). Register both in Root.tsx. 28 instantiations render from
   props via remotion_scenes.py (FOREGROUND — rule #3; props match zod — rule #4).
4. ./art run youtube/kokoro-all-28-english-voices → qc-sheet BY LOOKING (rule #2):
   30/30, every card's name/grade/index correct against the roster table in the sheet,
   B00/B99 correct. GATE: review cut + any rough-voice notes; WAIT for human approval.
5. After approval: ./art final (master staged AFTER final), <slug>.srt, publish
   unlisted to the Brutalist playlist (NO chapter slot). DESCRIPTIONS CROSS-LINK BOTH
   WAYS: this video's description links the short film ("the story version"); after
   publish, add this video's URL to the short film's description ("hear all 28").
   YouTube CHAPTER MARKERS in the description: one per voice (timestamp + name +
   grade), section headers at the four group boundaries — that is what makes this cut
   usable as a reference. Append to PUBLISH-LOG.md; findings to CAMPAIGN-FEEDBACK.md.
