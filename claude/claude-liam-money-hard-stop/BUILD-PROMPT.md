# BUILD-PROMPT — claude-liam-money-hard-stop ("Claude, Paused.")

Standalone rebuild prompt. State when written: beat_sheet.json authored
(11 beats, standard ai-explainer — NOT skill-teardown), Kokoro am_onyx
audio GENERATED and MEASURED (mp3/ + timings.json; actual_duration_s is
ground truth), PEDAGOGY.md ends VERDICT: PASS, SOURCES.md logs the claims
(reused from the verified Vercel reel). What remains: visuals → conform →
render → QC.

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace.

```text
Build the visuals and final cut for the EXISTING reel
youtube/claude-liam-money-hard-stop ("Claude, Paused." — an ai-explainer
on the money hard-stop rule, claude-liam channel). STANDARD ai-explainer
(vox-style middle), NOT the skill-teardown modifier. Free pipeline only:
no ElevenLabs, no higgsfield, no publishing, no git commit or push. Run
without approval pauses. 16:9 only.

HARD CONSTRAINT — THE CLOCK IS LOCKED. Narration audio already exists
(mp3/beat-*.mp3) and actual_duration_s in beat_sheet.json is measured
ground truth. Do NOT regenerate audio, edit narration_text, or touch mp3/.
Conform every beat's visuals to its existing audio duration.

READ COMPLETELY BEFORE ACTING

- AGENTS.md (the HARD STOP money rule at the top IS this video's subject),
  CLAUDE-BRAND.md
- skills/make/ai-explainer/SKILL.md (house + frame laws; ignore the
  skill-teardown modifier section — this reel is a standard explainer)
- skills/make/explainer/SKILL.md (and its MOTION.md / REMOTION.md)
- skills/make/your-turn/SKILL.md, docs/remotion-best-practices/SKILL.md
- runtime/remotion/src/tokens/claude.ts and tokens/layout.ts (SAFE)
- youtube/claude-liam-money-hard-stop/beat_sheet.json, PEDAGOGY.md, SOURCES.md
- youtube/claude-liam-vercel-mcp/ (the companion reel — reuse its
  VercelBuyDomain look for B02 where it helps), youtube/claude-liam-google-workspace/,
  youtube/claude-liam-theme-factory/ — exemplars for the composition
  pattern and per-beat media/ flow.

FORMAT

- 1920x1080 (16:9), 30 fps. Per-beat mp4s in media/, named by beat id,
  conformed to actual_duration_s (+0.4 s tail). Assemble with
  runtime/scripts/compile.py; render Remotion only via
  runtime/scripts/remotion_scenes.py, foreground, --concurrency=1.

THE BEATS (narration + durations are in the sheet)

- B00 ClaudeComposerAsk cold open — props in sheet; ask answered (the rule).
- B01 MoneyToolLadder — a rung ladder read → write → SPEND, all reached
  through ONE OAuth grant/door. The SPEND rung carries the terracotta
  accent. Reveal the rungs as narration names them.
- B02 MoneyBuyDomainCase — the buy_domain schema as a form: PII fields +
  a real-money price tag + a conspicuously ABSENT confirm button. Reuse
  the Vercel reel's VercelBuyDomain treatment. Never shows a completed
  purchase. Spark: "Real money. No confirm."
- B03 MoneyThreeFailures — three panels: prompt injection (hidden
  instruction in read data), confused deputy (connect-consent ≠ act-
  consent), autopilot (batch / skip-permissions, no human watching). Each
  lights as named; end with all three "plugged" by one rule token.
- B04 MoneyVendorSaysSo — a REBUILT styled quote card (not a screenshot):
  "Always enable human confirmation in your workflows." — attributed to
  Vercel's own security docs. Spark: "Official ≠ safe on autopilot."
- B05 MoneyIrreversible — a two-way door (reads/writes, swings back) vs a
  one-way door (spend, no return). Money leaving + a name stamped on a
  registration, no undo. Reveal on "doesn't swing back."
- B06 MoneyHardVsSoft — soft confirm = the agent rubber-stamping its own
  request (a loop) vs hard stop = a human gate the run pauses at. Make the
  loop visibly circular and the hard stop a real barrier. Spark: "The
  human is the gate."
- BVDT ClaudeVerdictArtifact — artifactLines in sheet; enlarged card.
- BHTF ClaudeComposerAsk handoff — greeting "Your turn.", typing on,
  command = the audit-your-tools prompt in the sheet.
- BOUT ClaudeTitleOutro — "Claude, Paused." · @NikBearBrown · "Liam, in for Bear."

LAWS THAT BITE HERE

- REBUILD LAW: no screenshots. The B04 vendor line is a rebuilt quote card.
- ACCURACY: buy_domain is a capability, never a completed purchase on
  screen. Only the verified quote/fact set in SOURCES.md appears.
- ILLUSTRATE LAW: Claude UI only in B00, BHTF, BVDT, BOUT; every inner beat
  is a C3/pattern illustration.
- SHOW-DON'T-TELL: the ladder rungs (B01), the three failure panels (B03),
  the one-way door (B05), and the self-approval loop vs human gate (B06)
  all animate on the spoken word.
- FILL-THE-CANVAS, SPARK-LINE (≤4 words), LOGO LAW (NBB bug lower-right;
  full-size on BOUT), one terracotta accent per beat (natural home: the
  SPEND rung / the one-way door / the human gate), SAFE inset — all bind.

ASSEMBLE, QC, REPORT

1. Implement the six Money* scenes in remotion-src/ (adapt the exemplar
   pattern; props match each component's zod schema). Render per-beat
   media/*.mp4 conformed to the locked durations.
2. python3 runtime/scripts/compile.py youtube/claude-liam-money-hard-stop
3. VISUAL QC LAW: frames at 2 fps + each beat at ~15/50/85%, READ the
   PNGs, 9-point rubric, _qc/REPORT.md, re-render until zero BLOCKER/MAJOR.
4. ffprobe the final mp4. Report per-beat durations, total runtime, QC
   findings, file path, and the beat → timestamp table.

Any scene failing twice → labeled PIPELINE slate, logged in BUILD-LOG.md,
keep going. Never publish.
```
