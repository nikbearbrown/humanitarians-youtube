# BUILD-PROMPT — claude-liam-connect-linkedin ("Claude, Gated.")

Standalone rebuild prompt. State when written: beat_sheet.json authored
(13 beats, standard ai-explainer — NOT skill-teardown), Kokoro am_onyx
audio GENERATED and MEASURED (mp3/ + timings.json; actual_duration_s is
ground truth), PEDAGOGY.md ends VERDICT: PASS, SOURCES.md logs every claim
(two hard facts web-verified). What remains: visuals → conform → render → QC.

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace.

```text
Build the visuals and final cut for the EXISTING reel
youtube/claude-liam-connect-linkedin ("Claude, Gated." — an ai-explainer
of how to connect Claude to LinkedIn, claude-liam channel). This is a
STANDARD ai-explainer (vox-style middle), NOT the skill-teardown modifier.
Free pipeline only: no ElevenLabs, no higgsfield, no publishing, no git
commit or push. Run without approval pauses. 16:9 only.

HARD CONSTRAINT — THE CLOCK IS LOCKED. Narration audio already exists
(mp3/beat-*.mp3) and actual_duration_s in beat_sheet.json is measured
ground truth. Do NOT regenerate audio, edit narration_text, or touch mp3/.
Conform every beat's visuals to its existing audio duration.

READ COMPLETELY BEFORE ACTING

- AGENTS.md, CLAUDE-BRAND.md
- skills/make/ai-explainer/SKILL.md (house + frame laws; ignore the
  skill-teardown modifier section — this reel is a standard explainer)
- skills/make/explainer/SKILL.md (and its MOTION.md / REMOTION.md)
- skills/make/your-turn/SKILL.md
- docs/remotion-best-practices/SKILL.md
- runtime/remotion/src/tokens/claude.ts and tokens/layout.ts (SAFE)
- youtube/claude-liam-connect-linkedin/beat_sheet.json, PEDAGOGY.md, SOURCES.md
- youtube/claude-liam-theme-factory/ and youtube/claude-liam-algorithmic-art/
  — exemplars: copy the composition pattern, ClaudeComposerAsk /
  ClaudeCodeBeat / ClaudeVerdictArtifact / ClaudeTitleOutro usage, and the
  per-beat media/ flow.

FORMAT

- 1920x1080 (16:9), 30 fps. Per-beat mp4s in media/, named by beat id,
  conformed to actual_duration_s (+0.4 s tail). Assemble with
  runtime/scripts/compile.py; render Remotion only via
  runtime/scripts/remotion_scenes.py, foreground, --concurrency=1.

THE BEATS (narration + durations are in the sheet)

- B00 ClaudeComposerAsk cold open — props in sheet; ask answered.
- B01 LinkedInTrustBoundary — the Connectors Directory with NO first-party
  LinkedIn; a trust boundary line: you → a third-party stranger's server.
- B02 LinkedInThreeLanes — three labeled lanes: Publishing · Analytics ·
  Outreach. Neutral at this beat (they diverge in B03).
- B03 LinkedInAsymmetry — the thesis: Publishing + Analytics lanes turn
  green ("official API"); the Outreach lane hits a wall ("no public
  scope, any price"). Reveal lands on the spoken "wall."
- B04 LinkedInApiSurface — rebuilt surface table: rows = personal posting
  (self-serve), company posting/analytics (AUDIT), member reading
  (CLOSED), outreach (NO PATH); columns = access process + compliance.
  True to SOURCES.md; no invented scopes on screen.
- B05 LinkedInDetectionStack — left: cookie extraction (li_at) → Voyager
  replay; right: the detection layers (extension signatures, fingerprint,
  datacenter-IP, timing). "undetectable" stamped as a warning label, not
  a feature. Framing is consumer-warning, never an evasion how-to.
- B06 LinkedInLegalSplit — two columns: CFAA (public data, hiQ 9th Cir.)
  vs Contract (User Agreement bans bots → suspension). hiQ settlement
  stamp: "$500K · algorithms destroyed · Dec 2022". Verbatim-safe.
- B07 LinkedInRedFlags — three vendor "safety" claims flipped to their
  real meaning (caps/timing = under detection thresholds; multi-account
  rotation = the risk spread across your accounts).
- B08 ClaudeComposerAsk (compliant-path ask) — props in sheet.
- B09 ClaudeCodeBeat — Onda code-block, the real POST /rest/posts curl
  from the sheet (keep it as-is; the version header was intentionally
  dropped — do not re-add a dated Linkedin-Version). ASK→RESULT with B08.
- BVDT ClaudeVerdictArtifact — artifactLines in sheet; enlarged card.
- BHTF ClaudeComposerAsk handoff — greeting "Your turn.", typing on,
  command = the classify-my-need prompt in the sheet.
- BOUT ClaudeTitleOutro — "Claude, Gated." · @NikBearBrown · "Liam, in for Bear."

LAWS THAT BITE HERE

- REBUILD LAW: no screenshots of LinkedIn, its Developer Portal, or any
  vendor page — every surface is a native rebuilt graphic in the fidelity
  palette. Only numbers/facts in SOURCES.md appear on screen.
- ILLUSTRATE LAW: Claude UI only in B00, B08, BHTF, BVDT, BOUT; B09 is an
  Onda code-block; every other beat is a C3/pattern illustration.
- SHOW-DON'T-TELL: the green/wall split (B03), the CFAA-vs-contract split
  (B06), and each flip (B07) animate on the spoken word.
- FILL-THE-CANVAS, SPARK-LINE (≤4 words), LOGO LAW (NBB bug lower-right;
  full-size on BOUT), one terracotta accent per beat, SAFE inset — all bind.

ASSEMBLE, QC, REPORT

1. Implement the seven LinkedIn* scenes in remotion-src/ (adapt the
   exemplar pattern; props match each component's zod schema). Render
   per-beat media/*.mp4 conformed to the locked durations.
2. python3 runtime/scripts/compile.py youtube/claude-liam-connect-linkedin
3. VISUAL QC LAW: frames at 2 fps + each beat at ~15/50/85%, READ the
   PNGs, 9-point rubric, _qc/REPORT.md, re-render until zero BLOCKER/MAJOR.
4. ffprobe the final mp4. Report per-beat durations, total runtime, QC
   findings, file path, and the beat → timestamp table.

Any scene failing twice → labeled PIPELINE slate, logged in BUILD-LOG.md,
keep going. Never publish.
```
