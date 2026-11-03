# BUILD-PROMPT — verifying-private-ai-valuations

The single paste-ready Claude Code prompt that rebuilds this reel end to end.
Run from the `brutalist.art` toolkit root. Free/local — no API key, no spend.

---

```
Rebuild the reel at
D:/study_other/humanitarians-youtube/fellows/om-mali/2026-08-08-Verifying-Private-AI-Valuations

Skill: ai-explainer, channel claude-hai. Read skills/make/ai-explainer/SKILL.md in full first.
Use the .venv interpreter (.venv/Scripts/python3.exe) and put .venv/Scripts on PATH so run.sh
resolves python3 to it.

1. GATE CHECK
   - FACTCHECK.md: all 20 rows must read CONFIRMED. Stop if any row regressed.
   - PEDAGOGY.md: must contain "VERDICT: PASS". If it says PENDING, STOP and tell the human
     what they are being asked to sign (the file lists it) — do not sign it yourself and do not
     pass --no-gate for a final cut.
   - CHECKS-REPORT.md must exist before the first compile.

2. AUDIO — the master clock
   python3 runtime/scripts/generate_audio_kokoro.py <reel>
   Kokoro am_onyx (the fellow's persistent voice — never change it silently).
   Then write each beat's measured actual_duration_s into its shot.remotion.props
   as durationInSeconds, so every scene re-times to its real narration instead of
   being center-cut or freeze-padded.

3. RENDER
   python3 runtime/scripts/remotion_scenes.py <reel>
   Ten beats, all Remotion, zero slates. The six reel-local scenes live in
   runtime/remotion/src/PrivateAiValuations.tsx (registered in Root.tsx under the
   PrivateAiValuations folder). Never hand-roll `npx remotion render`.

4. COMPILE
   ./art run <reel>          # review cut + GATE L + GATE V
   ./art final <reel>        # clean 4K master, only once GATE P reads PASS

5. VISUAL QC — LOOK at frames, never trust the mp4 probe
   Sample at >=2fps plus each beat at ~15/50/85% of its span, actually Read the PNGs,
   and audit the 9-point rubric from CLAUDE-CODE-VISUAL-QC-CHECK.md: edge bleed, title-safe
   margins, container overflow, collision, offscreen anchors, legibility, brand bug placement,
   aspect, and CANVAS FILL. Log every defect and fix in _qc/REPORT.md. Fix root causes in the
   scene source and re-render until zero BLOCKER and zero MAJOR remain.

6. REPORT — never publish. The master stays in the reel folder.

Laws that bind hardest on this reel:
- REBUILD LAW — the three PNGs in pantry/ are REFERENCE ONLY. Never slot them as media.
- DOUBLE-CHECK LAW — no figure on screen that is not traceable to a FACTCHECK.md row.
  B02 deliberately shows <valUSD> and <balance> as TAG NAMES because no confirmed
  numerator/denominator pair exists. Do not "improve" this by inventing plausible numbers.
- ILLUSTRATE LAW — the Claude UI appears at B00, B07, B08, B09 only.
- SHOW-DON'T-TELL — every body beat must MOVE. The cut this replaced failed exactly here.
```

---

## Why this reel exists twice

There is an earlier cut of the same week's work in `_previous-build/`, built 2026-08-08 by the
Mycroft repo's own tooling. It is kept as the before-picture, not as a fallback. If you need to
compare, `_previous-build/beat_sheet.prev.json` is the original 6-beat sheet.
