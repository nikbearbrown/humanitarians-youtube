# BUILD-PROMPT — claude-liam-google-workspace ("Claude, Grounded.")

Standalone rebuild prompt. State when written: beat_sheet.json authored
(12 beats, standard ai-explainer — NOT skill-teardown), Kokoro am_onyx
audio GENERATED and MEASURED (mp3/ + timings.json; actual_duration_s is
ground truth), PEDAGOGY.md ends VERDICT: PASS, SOURCES.md logs every claim
(core facts verified against the live support.claude.com article). What
remains: visuals → conform → render → QC.

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace.

```text
Build the visuals and final cut for the EXISTING reel
youtube/claude-liam-google-workspace ("Claude, Grounded." — an
ai-explainer of Claude's Gmail / Calendar / Drive connectors, claude-liam
channel). STANDARD ai-explainer (vox-style middle), NOT the skill-teardown
modifier. Free pipeline only: no ElevenLabs, no higgsfield, no publishing,
no git commit or push. Run without approval pauses. 16:9 only.

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
- youtube/claude-liam-google-workspace/beat_sheet.json, PEDAGOGY.md, SOURCES.md
- youtube/claude-liam-connect-linkedin/, youtube/claude-liam-theme-factory/,
  youtube/claude-liam-algorithmic-art/ — exemplars: copy the composition
  pattern, ClaudeComposerAsk / ClaudeVerdictArtifact / ClaudeTitleOutro
  usage, and the per-beat media/ flow.

FORMAT

- 1920x1080 (16:9), 30 fps. Per-beat mp4s in media/, named by beat id,
  conformed to actual_duration_s (+0.4 s tail). Assemble with
  runtime/scripts/compile.py; render Remotion only via
  runtime/scripts/remotion_scenes.py, foreground, --concurrency=1.

THE BEATS (narration + durations are in the sheet)

- B00 ClaudeComposerAsk cold open — props in sheet; ask answered.
- B01 WorkspaceFirstParty — a "first-party / native" badge; the three
  connectors (Gmail, Calendar, Drive) light up as real, free, on-every-plan.
- B02 WorkspaceAsymmetry — THE THESIS. Calendar column = full read/write
  (create/update/delete, availability, attendees); Gmail column = a
  ceiling at "draft," the send action visibly blocked. Metaphor cue:
  "keys" (calendar) + "pen" (draft) but no "stamp" (send). Verbatim chip:
  "cannot send emails on your behalf." Reveal lands on "the stamp."
- B03 WorkspaceScopeVsTool — OAuth consent screen shows a send-email scope
  (granted) next to Claude's actual tool list (no send call). Animate the
  gap: scope box ticks, the "send" tool stays dark. Spark: "Granted ≠ used."
  Framing: WHY Google shows a scope Claude doesn't use — never assert send.
- B04 ClaudeComposerAsk (setup ask) — props in sheet (the availability
  request). Ask answered by Calendar automatically.
- B05 WorkspaceCapabilityTour — three panels: Calendar (event created,
  not just read) · Drive (upload + folder + save-output-back, beyond
  search) · Gmail (draft composed, sitting UNSENT in drafts). Tag: every
  action needs explicit chat approval; no background access.
- B06 WorkspaceAdminFix — an "Access blocked" wall, then the Google Admin
  console path (admin.google.com → Security → API controls → third-party
  app access → add Claude → Trusted → ~15 min). Card is generic enough to
  survive a menu rename; re-verify the exact path against the live doc.
  Note the Team/Enterprise Owner-enables-first layer.
- B07 WorkspaceTrainingCarveout — connector data visibly walled off from
  training; a copy-paste action carries text OUT of the wall into "your
  message," which then follows plan rules. Verbatim chip: "We do not train
  our models on your Gmail, Drive, or Calendar connector data." Spark:
  "The wall has a copy-paste gap."
- B08 WorkspaceLimits — known-limits card: attachment metadata not content;
  some advanced Gmail filters unsupported; multi-call complex queries;
  Google rate limits; Drive text-only / no Doc comments.
- BVDT ClaudeVerdictArtifact — artifactLines in sheet; enlarged card.
- BHTF ClaudeComposerAsk handoff — greeting "Your turn.", typing on,
  command = the verify-against-the-docs prompt in the sheet.
- BOUT ClaudeTitleOutro — "Claude, Grounded." · @NikBearBrown · "Liam, in for Bear."

LAWS THAT BITE HERE

- REBUILD LAW: NO screenshots of Gmail, Calendar, Drive, the OAuth consent
  screen, or the Google Admin console — every surface is a native rebuilt
  graphic in the fidelity palette. Only facts/quotes in SOURCES.md on screen.
- ACCURACY: never show or imply Claude sending an email. The Gmail panel
  always ends at an UNSENT draft. B03 shows the send tool dark/unused.
- ILLUSTRATE LAW: Claude UI only in B00, B04, BHTF, BVDT, BOUT; every other
  beat is a C3/pattern illustration.
- SHOW-DON'T-TELL: the calendar/gmail ceiling split (B02), the scope-vs-tool
  gap (B03), the copy-paste crossing the wall (B07) animate on the spoken word.
- FILL-THE-CANVAS, SPARK-LINE (≤4 words), LOGO LAW (NBB bug lower-right;
  full-size on BOUT), one terracotta accent per beat, SAFE inset — all bind.

ASSEMBLE, QC, REPORT

1. Implement the seven Workspace* scenes in remotion-src/ (adapt the
   exemplar pattern; props match each component's zod schema). Render
   per-beat media/*.mp4 conformed to the locked durations.
2. python3 runtime/scripts/compile.py youtube/claude-liam-google-workspace
3. VISUAL QC LAW: frames at 2 fps + each beat at ~15/50/85%, READ the
   PNGs, 9-point rubric, _qc/REPORT.md, re-render until zero BLOCKER/MAJOR.
4. ffprobe the final mp4. Report per-beat durations, total runtime, QC
   findings, file path, and the beat → timestamp table.

Any scene failing twice → labeled PIPELINE slate, logged in BUILD-LOG.md,
keep going. Never publish.
```
