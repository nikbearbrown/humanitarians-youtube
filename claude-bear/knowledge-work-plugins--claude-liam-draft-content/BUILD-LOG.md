# BUILD-LOG — knowledge-work-plugins--claude-liam-draft-content

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-draft-content/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `draft-content`
partner-built skill — marketing content drafting: blog posts, social media,
email newsletters, landing pages, press releases, case studies —
channel-specific formatting and SEO recommendations; already fully built —
no SCRIPT.md; source `beats[*].narration_text` served as the locked script,
and the source's own `source_skill` metadata confirms the underlying
`SKILL.md` is not present on this machine). Built entirely fresh this
invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: a Claude
skill is a folder Claude reads before it works; the SKILL.md file holds the
entire instruction set in plain language; Claude reads the file, then acts —
the file is the program; the instructions live in a Steps section, run in
order, start to finish, no branching unless a step says otherwise; and this
particular skill, draft-content, has one job — draft marketing content for
six named channels (blog, social, email, landing page, press release, case
study) with channel-specific formatting and SEO recommendations, written for
three named moments (writing any marketing content, generating headline or
subject-line options, adapting a message for a specific platform, audience,
and brand voice), with nothing to say outside those three moments. B00
replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "talent" -> "file" — the newcomer's
wrong guess that running the skill gives Claude some new general writing
talent, corrected toward the actual mechanism: a skill is one file, scoped
to one job). Register re-registered Teardown -> Plain: the source's B03
"what it gets right: repeatable results / what it bites: anything outside
the spec" verdict pairing was stripped to a plain scope statement (three
named moments, nothing outside them), per the NO JUDGMENT register check.
BVDT's verdict facts (repeatable same-input/same-output execution, and the
file-only limit) were merged into the single BCRY carry-out sentence rather
than kept as a separate bulleted artifact card, per CARRY-OUT LAW. BHTF's
prompt kept the source's structure (ask Claude to draft a piece of
marketing content and explain its plan before acting — the same
artifact-vs-world/Plato move the source's own LENS-AUDIT.md had flagged)
but was rewritten into one genuinely paste-ready sentence, since the source
string was an awkward truncated quote ("I want to draft blog posts, social
media, email newsletters, landing pages, press releases. Read the
draft-content skill and walk me through what you will do before you do
it.") that reads as a request for six channels at once, not a single
runnable task. Close re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01 and B02 kept as one
beat each, content essentially unchanged since the source text was already a
plain factual description, not Teardown judgment; B03's verdict pairing
compressed to a plain scope statement; BVDT folded into BCRY; BHTF kept,
reworded to be genuinely runnable; BOUT kept. Full audit in SCRIPT.md's
"Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no substitution
beyond B00's mandated cold-open swap. B01-B03 reuse the source's own generic
`SkillTeardownAnatomy`/`SkillTeardownPipeline`/`SkillTeardownMechanism`
components unchanged — `./art scenes --check` confirmed all patterns used in
this sheet (`BrutalistHesitantWriter`, `SkillTeardownAnatomy`,
`SkillTeardownPipeline`, `SkillTeardownMechanism`, `WantQuote`,
`ClaudeComposerAsk`, `OutroSeries`) are RENDERABLE before slating, so no new
component authoring or GATE L punt was needed.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); all 7 beats rendered via `remotion_scenes.py` (foreground; the
full-sheet run exceeded the tool's 120s timeout and was moved to background
by the harness automatically — blocked on it via `TaskOutput` before
proceeding, per the COMPLETION LAW's foreground-render rule, never treating
a backgrounded render as "handled" without waiting on it).

`type_check.py` (GATE T) passed clean on the first run: **PASS, 0 FAILs.**

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result (first pass): `knowledge-work-plugins--claude-liam-draft-content.mp4`,
7/7 beats filled real (no slate), 86.6s, 3840x2160 (native 4K —
`compile.py`'s 4K LAW). GATE AUDIO: PASS, mean_volume -24.1 dB.

**Gate V (visual QC) caught a real defect in B00, fixed at the root:**
pulling frames across B00's window showed the typing performance did not
finish before the clip ended — at t=8.5s (0.1s before the 8.6s clip end)
only "this skill" had rendered, missing the final "do?" B00's original text
prop ("Claude got a\nnew writing talent.\nWait — what does\nthis skill
actually do?") carried two extra words ("writing" and "actually") beyond
the sibling reel's proven-safe text length
(`knowledge-work-plugins--claude-liam-design-mcp-workflow`'s "Claude got a\n
new ability.\nWait — what does\nthis skill do?"), and
`BrutalistHesitantWriter`'s typing performance is paced independently of
the audio track — it does not compress to fit the beat's duration, so extra
characters simply get cut off. Fixed by shortening the on-screen text to
"Claude got a\nnew talent.\nWait — what does\nthis skill do?" (dropping
"writing" and "actually," matching the sibling's exact proven-safe length)
while `narration_text` kept its fuller phrasing unchanged. Re-rendered B00
only (`--only B00 --force`), confirmed by re-pulling frames: by t=6.0s the
full corrected question "Claude got a new file. Wait — what does this
skill do?" is completely typed and holds legibly through t=8.3s, comfortably
inside the 8.6s clip with >2s of buffer. Recompiled (`--force`); GATE T and
GATE AUDIO re-run clean after the fix.

**Gates (final, post-fix):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840x2160 h264, audio present, duration 86.581667s; mp4
  mtime (1788474443) newer than beat_sheet.json mtime (1788474354)
- Gate V (visual): pulled frames across B00 (t=1.2s "Claude got a" typing,
  t=4.0s "talent" mid-type doomed in terracotta pre-deletion, t=6.0s full
  corrected question complete and legible, t=8.3s still legible, well
  before the 8.6s clip end — confirms the fix), B01-B02 (anatomy/pipeline
  cards legible, correct skill name "draft-content"), B03 (scope card,
  10-word on-screen body clean, no wordy-card violation), BCRY (carry-out
  sentence + sparkline read clean), BHTF (correct topic/title/
  @HumanitariansAI handle, paste-ready prompt text legible), and BOUT
  (`OutroSeries`: correct eyebrow "DRAFT-CONTENT · @HumanitariansAI",
  correct title restate, underline draws in, no truncation). No blockers.
- **Known library quirk, not a defect I introduced (same as the
  design-mcp-workflow sibling):** `OutroSeries` (and `OutroCTA`) hardcode
  `tokens/vox.ts` (`CREAM: '#FFFFFF'`, flat white, not warm cream; `CRIMSON:
  '#C8102E'`, not the humanitarians terracotta), so BOUT renders on flat
  white with a red-orange underline rather than the reel's `#F3EBDD` cream
  ground and `#E4572E` terracotta used everywhere else. Pre-existing
  library limitation (no palette prop on `OutroSeries`/`OutroCTA`), not
  introduced by this build — logged for visibility, not fixed (fixing it
  means patching a shared library component, outside this reel's scope).
- B00 TIMING LAW: `actual_duration_s` 8.58s + `lead_silence_s` 0.8s = 9.38s
  video window (>=9s target met); the "talent" -> "file" correction lands
  on screen by t~4.0s-6.0s and the full corrected question stays legible
  for the remainder of the clip.

Metadata file written:
`knowledge-work-plugins--claude-liam-draft-content.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) is an exact key match in the map, resolving
directly to "Extending Claude — Skills, Plugins & Connectors" (no fallback
needed). Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
