# BUILD-PROMPT

Build one CLI video reel for the claude-liam brand (Liam, in for Bear; footer @NikBearBrown; Kokoro am_onyx).

Source idea: physics-electromagnetism/youtube/cli-ideas.md — Candidate 05 (score 10/10):
"Maxwell's Equations Consistency Checker: Light Falls Out"

Required spine:
- B00 INTRO: Claude terminal "Bonjour, Liam" (ClaudeComposerAsk cold open)
- B01 PROBLEM: Ampère contradiction → displacement current → wave equation → c (slate)
- B02 ASK: the actual Claude prompt for maxwell_check.py
- B03 CODE: the real generated Python (ClaudeCodeBeat)
- B04 OUTPUT: Manim — Gaussian wave packet propagating at c with tracking dot
- B05 CHANGE: revision prompt to add two-pulse superposition
- B06 OUTPUT: Manim — two pulses pass through each other unchanged
- B07 SUMMARY: the lesson in one beat (slate)
- B08 NEXT STEPS: "Your turn." handoff with square-wave dispersion prompt
- B09 OUTRO: ClaudeTitleOutro @NikBearBrown

Constraints:
- brand: claude-liam, engine: kokoro, voice: am_onyx, NOT ElevenLabs
- Show ACTUAL code the artifact is built from (ACTUAL-CODE LAW)
- SPARK-LINE LAW: B02 greeting="The ask,", B05 greeting="The change,"
- Scaffold NEW folder only — no existing files modified or deleted
- GATE P before audio (PEDAGOGY.md with VERDICT: PASS)
- GATE F paperwork required (FACTCHECK.md, SHOTLIST.md, PROMPTS.md)
- Output: [slug]-slate.mp4 and [slug].mp4
- Never publish
