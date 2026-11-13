# PEDAGOGY — claude-code-explained

**Prepared by:** Claude (agent) · **Date:** 2026-10-01
**Skill:** `cli-explainer` (`skills/make/cli-explainer/SKILL.md`)

This is **GATE P** — `generate_audio_kokoro.py` checks it before any narration is generated. An
agent never signs its own gate: everything below is my checklist; `VERDICT` stays `PENDING` until
you sign it.

## Required-elements checklist

1. **12-beat spine** (INTRO → PROBLEM → MECHANISM → CLI→CODE→OUTPUT → CLI→CODE→OUTPUT → SUMMARY →
   NEXT STEPS → OUTRO). **CHECK: satisfied** — B00–B11 in `beat_sheet.json`.
2. **REVISION LAW** — ≥1 revision cycle. **CHECK: satisfied** — B06→B07→B08 (the Manim coordinate
   fix) after B03→B04→B05 (the composer layout fix). Kept in the 9:16 too (full-length, approved).
3. **ACTUAL-CODE LAW** — **CHECK: satisfied.** B04 = `ClaudeComposerAsk916.tsx` lines 46, 50–51,
   87–92 (comment lines 47–49 trimmed). B07 = `short/scenes.py` lines 27–34, verbatim. Each ask
   plausibly produces its code; each code plausibly produces its output.
4. **Output beats are motion.** **CHECK: satisfied** — B01, B02, B05, B08, B09 Manim; the rest
   Remotion. No stills.
5. **NO FABRICATION.** **CHECK: satisfied** — every number traces to a v2 file; see `FACTCHECK.md`
   (10 claims). No model version numbers on screen or in narration (DOUBLE-CHECK LAW).
6. **HANDOFF LAW.** **CHECK: satisfied** — B10 reads the prompt aloud and says why its middle
   clause (what you'll verify, and how) is the part that matters.
7. **Branding (PM).** **CHECK: satisfied on paper** — B00 narration starts with the exact phrase
   "Hi, I am Supriya and this video is about…"; "Supriya" on every beat (composer `folderLabel`,
   code `handle`, Manim corner handle, outro `handle`, endcard). Rendering of the code-beat chip
   depends on the Gate 3 prop change.
8. **Length.** ~170s estimated (420 words at the measured 2.56 words/s) → full-length 9:16 under
   the 180s cap with the endcard.
9. **No paid services.** **CHECK: satisfied** — Kokoro, Manim, Remotion, all local.

## For you to check before signing

- [ ] Read the 12 blocks in `NARRATION-SCRIPT.md` aloud-ish: does the Teardown voice land, and is
      the B00 phrase exactly what the PM wants?
- [x] B01 says "an earlier vertical cut of mine" for the v1 trailer (built in the other
      `brutalist-art` checkout). Accurate framing?
- [x] B03 compresses the v2 story: the plan *assumed* portrait-readiness and the standalone render
      disproved it. Fair to how it happened?
- [x] B07's explanation of the Gate B blind spot is understandable to someone who has never used
      Manim?
- [ ] The handoff prompt (B10) is one you'd actually want viewers to paste.

Reviewer notes (2026-10-01): B01 and B03 confirmed fair as written; B07 confirmed accessible for
a general audience. Three TTS fixes applied before signing: B01 "four K" spelled out and
"kilobits a second"; B05 bitrates spelled out in full with "kilobits a second".

## VERDICT: PASS

Signed: Supriya Kushwaha (human, author)
Date: 2026-10-01
