# BUILD-PROMPT

Build one CLI video reel for the claude-liam brand (Liam, in for Bear; footer @NikBearBrown; Kokoro am_onyx).

Source idea: physics-electromagnetism/youtube/cli-ideas.md — Candidate 01 (score 9/10):
"Build the Faraday Cage: How Much Shielding Does a Copper Box Provide?"

Required spine:
- B00 INTRO: Claude terminal "Bonjour, Liam" (ClaudeComposerAsk cold open)
- B01 PROBLEM: why MRI rooms use copper; what skin depth means
- B02 ASK: the actual Claude prompt for faraday_cage.py
- B03 CODE: the real generated Python (ClaudeCodeBeat)
- B04 OUTPUT: Manim — skin depth + attenuation log-log with MRI markers
- B05 CHANGE: revision prompt to add material comparison
- B06 OUTPUT: Manim — copper vs aluminum vs stainless steel
- B07 SUMMARY: the lesson in one beat
- B08 NEXT STEPS: "Your turn." handoff with extension prompt
- B09 OUTRO: ClaudeTitleOutro @NikBearBrown

Constraints:
- brand: claude-liam, engine: kokoro, voice: am_onyx, NOT ElevenLabs
- Show ACTUAL code the artifact is built from (ACTUAL-CODE LAW)
- Scaffold NEW folder only — no existing files modified or deleted
- GATE P before audio (PEDAGOGY.md with VERDICT: PASS)
- GATE F paperwork required (FACTCHECK.md, SHOTLIST.md, PROMPTS.md)
- Output: [slug]-slate.mp4 and [slug].mp4
- Never publish
