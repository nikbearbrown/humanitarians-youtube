# BUILD-LOG — hints-not-answers

Physics Engine series, 11 of 12. Built 2026-10-31.

## Order of work

1. Read the tutor-mode and Physics Engine mode code and docs at
   `jashshah127/humanitariansai@2dc4aa4`; every figure ledgered in SOURCES.md.
2. Beat sheet (11 beats), PEDAGOGY.md, SOURCES.md; scenes typechecked.
3. GATE P: standing approval from Param Madan in chat → Kokoro `af_bella` audio;
   checked with faster-whisper (tiny.en).
4. Preview stills of all 9 scenes before the 4K render — clean.
5. Rendered at `--scale=2` (3840x2160); `./art final` → 4K master.

## What broke, and the fix

- **Voice:** "no second A.I. call" made Kokoro insert a sentence break after "A.I.";
  narration changed to "no second model call" (B05), regenerated and re-checked.
- **Render timeouts:** 5 beats timed out under background-QoS throttling overnight;
  added `--timeout=300000` to the Remotion render call and re-ran the missing beats.
- **Not claimed:** no student has used tutor mode yet (B06 says so).
- **Project code not executed** (auto-mode permission check); results are repo-reported.

## Credits

Host and credit line supplied by Param Madan: "Video by Param Madan · Engine by
Jash Shah, Harsh Gujarati, Atharva & Param Madan". GitHub contributors on the
source repo: jashshah127, harshgujarati, Addy-9595.
