# Claude Code Prompt — Physics video ideas all-day batch (claude-liam)

Build one 16:9 `ai-explainer` / Claude-cut explainer for every candidate in
the six physics-book `youtube/video-ideas.md` files listed below. This is a
free-only, resumable, unattended batch. It never publishes.

```text
Run an unattended, resumable batch that builds one finished 1920x1080
ai-explainer video with the claude-liam voice for EVERY candidate in these
ordered source files:

1. ../quantum-mechanics-a-companion-guide/youtube/video-ideas.md
2. ../quantum-mechanics-vol1/youtube/video-ideas.md
3. ../quantum-mechanics-vol2/youtube/video-ideas.md
4. ../quantum-mechanics-vol3/youtube/video-ideas.md
5. ../quantum-mechanics-vol4/youtube/video-ideas.md
6. ../quantum-mechanics-vol5/youtube/video-ideas.md

There are 152 cards total. Work in the order above and card order within each
file. Continue until the process is stopped or every row is built/failed.
This is a LOOP, not a request to build only one video.

HARD SAFETY AND SCOPE

- Free pipeline only: Kokoro `af_kore`. Never call ElevenLabs, Higgsfield, or
  any paid/external generation API. Never publish, upload, git commit, or push.
- Run without approval pauses because paid spend and publishing are forbidden.
- Preserve all unrelated user work. Build only inside each owning book's
  `youtube/` directory plus its batch ledger.
- One candidate's failure never stops the batch. Log it and continue.
- Idempotent/resumable: if a candidate already has a valid finished MP4 and
  passing QC report, mark/reuse it; do not regenerate it.

READ COMPLETELY BEFORE ACTING

- AGENTS.md
- CLAUDE-BRAND.md
- skills/make/ai-explainer/SKILL.md
- skills/make/explainer/SKILL.md plus MOTION.md, EQUATIONS.md, and REMOTION.md
- skills/make/your-turn/SKILL.md
- docs/remotion-best-practices/SKILL.md
- runtime/voices/teardown/VOICE.md
- runtime/remotion/src/tokens/claude.ts
- all six source idea files above
- for each card, the exact cited chapter/source passages before scripting

CHANNEL AND EDITORIAL CONTRACT

- Channel `claude-liam`: Kore in for Humanitarians AI, Kokoro `af_kore`, Teardown
  register, `@HumanitariansAI` folder chip and logo bug.
- B00 begins on `ClaudeComposerAsk`; Kore says in the first breath that he is
  "Kore, in for Humanitarians AI." Rotate one-word world-language greetings; never Wagwan.
- Explain actual physics machinery from first principles, then name the design
  trade-off or conceptual choice. Strip jargon and hype. No fabrication.
- Fact-check every equation, number, historical claim, and physical claim
  against the cited book passage and reliable local sources. Record evidence,
  derivations, corrections, and scope limits in `SOURCES.md`/`FACTCHECK.md`.
- Length is content-derived. No padding to a target clock.

VISUAL CONTRACT

- ILLUSTRATE LAW: Claude UI only for the cold open, genuine ASK→RESULT prompt
  micro-beats, verdict, Your Turn, and title outro. Inner teaching beats are
  native concept illustrations, Manim fragments, equations, or data graphics.
- Physics that moves must move in sync with the narration. Use the card's
  Visual object / Manim move where supplied. Show mechanisms, not bullet lists.
- Equations use the inherited equation-tangent doctrine. Define variables and
  show the physical commitment; do not dump derivations into one crowded beat.
- Claude fidelity palette: cream, warm ink, and one terracotta focal accent.
  EB Garamond titles in Title Case. Fill the safe canvas with legible type.
- ASK→RESULT for every generated visual. The prompt shown must be the actual
  prompt/instruction used to create the following native result.
- Closing block: verdict recap → `Your turn.` composer with a genuinely useful
  physics prompt read aloud and discussed → title-restating outro. Kore signs
  "Kore, in for Humanitarians AI."

QUEUE AND OUTPUT CONTRACT

1. Parse all candidates and create/update a global ledger at
   ../quantum-mechanics-a-companion-guide/youtube/PHYSICS-AI-EXPLAINER-BATCH.md.
   Columns: global id | book | candidate | title | slug | status | final MP4 |
   duration | QC | notes. Preserve prior statuses on resume.
2. Slugs are `claude-liam-<concise-topic-slug>`. Build into the owning book:
   ../<book>/youtube/<slug>/
3. Each reel must contain at minimum:
   - beat_sheet.json
   - BUILD-PROMPT.md
   - SOURCES.md
   - FACTCHECK.md
   - BUILD-LOG.md
   - final `<slug>.mp4`
   - `_qc/REPORT.md`
4. Generate Kore audio first and measure actual beat durations. Render native
   visuals, compile the finished MP4, and probe duration/frame count.
5. Perform the required frame-level visual QC: sample at >=2 fps plus each
   beat around 15/50/85 percent, actually inspect the frames, fix scene-source
   root causes, rerender until zero BLOCKER and zero MAJOR defects. Record the
   result in `_qc/REPORT.md`. A successful ffprobe alone is not completion.
6. Mark `built` only after valid MP4 plus passing QC. Append one machine-readable
   completion line to
   ../quantum-mechanics-a-companion-guide/youtube/PHYSICS-AI-EXPLAINER-COMPLETED.log
   in this exact tab-separated form:
   BUILT<TAB>ISO_DATETIME<TAB>BOOK<TAB>CANDIDATE<TAB>TITLE<TAB>ABSOLUTE_MP4_PATH
7. If one beat fails twice, use an honest labeled pipeline slate for that beat,
   log it, and finish the reviewable video when possible. If the whole reel
   genuinely cannot finish, mark failed with the exact reason and move on.
8. After every row, update the ledger immediately. Never hold status only in
   memory. Then continue to the next pending row.

Begin or resume at the first non-built row now. Do not stop after planning,
scaffolding, audio, or one video. Keep looping.
```
