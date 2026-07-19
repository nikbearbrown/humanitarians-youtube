# BUILD-PROMPT — claude-liam-vercel-mcp ("Claude, Trusted.")

Standalone rebuild prompt. State when written: beat_sheet.json authored
(13 beats, standard ai-explainer — NOT skill-teardown), Kokoro am_onyx
audio GENERATED and MEASURED (mp3/ + timings.json; actual_duration_s is
ground truth), PEDAGOGY.md ends VERDICT: PASS, SOURCES.md logs every claim
(all core facts verified against the live vercel.com docs + tools reference).
What remains: visuals → conform → render → QC.

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace.

```text
Build the visuals and final cut for the EXISTING reel
youtube/claude-liam-vercel-mcp ("Claude, Trusted." — an ai-explainer of
Claude + Vercel's official MCP server, claude-liam channel). STANDARD
ai-explainer (vox-style middle), NOT the skill-teardown modifier. Free
pipeline only: no ElevenLabs, no higgsfield, no publishing, no git commit
or push. Run without approval pauses. 16:9 only.

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
- youtube/claude-liam-vercel-mcp/beat_sheet.json, PEDAGOGY.md, SOURCES.md
- youtube/claude-liam-google-workspace/, youtube/claude-liam-connect-linkedin/,
  youtube/claude-liam-theme-factory/ — exemplars: copy the composition
  pattern, ClaudeComposerAsk / ClaudeVerdictArtifact / ClaudeTitleOutro
  usage, and the per-beat media/ flow.

FORMAT

- 1920x1080 (16:9), 30 fps. Per-beat mp4s in media/, named by beat id,
  conformed to actual_duration_s (+0.4 s tail). Assemble with
  runtime/scripts/compile.py; render Remotion only via
  runtime/scripts/remotion_scenes.py, foreground, --concurrency=1.

THE BEATS (narration + durations are in the sheet)

- B00 ClaudeComposerAsk cold open — props in sheet; ask answered.
- B01 VercelOfficial — "official / first-party" badge, mcp.vercel.com,
  OAuth, a short supported-clients row (Claude Code + Claude Desktop
  highlighted). Tone: this one is clean — the tension is scope creep, not
  access.
- B02 ClaudeComposerAsk (setup ask) — props in sheet (npx add-mcp).
  Answered: detected client + the two-companies plan-gate note.
- B03 VercelDiagnose — failed build → Claude calls get_deployment_build_logs
  / get_runtime_logs → surfaces the error (e.g. missing env var). The
  low-risk, high-value core. Green/positive framing.
- B04 VercelAccountEquivalent — the OAuth grant = "the same access as your
  Vercel user account" (verbatim chip). Tool clusters fan out from one
  grant: read (logs) … write (toolbar) … deploy … buy_domain. The same
  key opens all of them. Spark: "Not a guest pass."
- B05 VercelBuyDomain — THE THESIS. The buy_domain schema as a form:
  required PII fields (first/last name, address, city, state, postal,
  phone, email, country) light up, a real-money price tag, and
  expectedPrice shown as a price-check field NOT a confirm button.
  Verbatim-safe. Spark: "Price-check ≠ confirm." The demo NEVER completes
  a purchase.
- B06 VercelSafeguardGap — two boxes: "connection consent" (protected,
  green check, confused-deputy) vs "per-tool confirm before buy_domain"
  (absent, dark). Animate the gap. Do NOT imply a per-tool confirm exists.
- B07 VercelOwnGuidance — a REBUILT doc-excerpt card (styled quote, not a
  screenshot): the prompt-injection example verbatim, then the pull-quote
  "Always enable human confirmation in your workflows." Framed as the
  vendor's own candor.
- B08 VercelMitigations — two panels: vercel mcp --project (blast-radius
  shrink) and the deployment-protection bypass token (scoped, revocable
  credential — the GOOD pattern, contrast to buy_domain). Spark: "Narrow.
  Revocable. Yours."
- BVDT ClaudeVerdictArtifact — artifactLines in sheet; enlarged card.
- BHTF ClaudeComposerAsk handoff — greeting "Your turn.", typing on,
  command = the verify-against-live-docs prompt in the sheet.
- BOUT ClaudeTitleOutro — "Claude, Trusted." · @NikBearBrown · "Liam, in for Bear."

LAWS THAT BITE HERE

- REBUILD LAW: NO screenshots of the Vercel dashboard, docs, or console —
  the B07 doc excerpt is a REBUILT styled quote card. Only facts/quotes in
  SOURCES.md on screen. Do NOT put a tool COUNT on screen (the source's
  "13" is stale; the surface is ~24 and drifting) — show clusters, not a number.
- ACCURACY: the buy_domain beat never shows a completed purchase; B06
  never implies a per-tool confirmation step exists.
- ILLUSTRATE LAW: Claude UI only in B00, B02, BHTF, BVDT, BOUT; every other
  beat is a C3/pattern illustration.
- SHOW-DON'T-TELL: the tool-cluster fan-out (B04), the PII form filling +
  price tag (B05), the present-vs-absent safeguard boxes (B06) animate on
  the spoken word.
- FILL-THE-CANVAS, SPARK-LINE (≤4 words), LOGO LAW (NBB bug lower-right;
  full-size on BOUT), one terracotta accent per beat, SAFE inset — all bind.

ASSEMBLE, QC, REPORT

1. Implement the seven Vercel* scenes in remotion-src/ (adapt the exemplar
   pattern; props match each component's zod schema). Render per-beat
   media/*.mp4 conformed to the locked durations.
2. python3 runtime/scripts/compile.py youtube/claude-liam-vercel-mcp
3. VISUAL QC LAW: frames at 2 fps + each beat at ~15/50/85%, READ the
   PNGs, 9-point rubric, _qc/REPORT.md, re-render until zero BLOCKER/MAJOR.
4. ffprobe the final mp4. Report per-beat durations, total runtime, QC
   findings, file path, and the beat → timestamp table.

Any scene failing twice → labeled PIPELINE slate, logged in BUILD-LOG.md,
keep going. Never publish.
```
