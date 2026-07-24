# BUILD-PROMPT — Claude, Peer-Reviewed.

**Reel:** `claude-liam-coding-agents-social-sciences`
**Channel:** claude-liam · Kokoro `af_kore` · @HumanitariansAI
**Built:** 2026-07-17

---

Build one 16:9 claude-explainer video titled **"Claude, Peer-Reviewed."** covering
Anthropic's **"Coding agents in the social sciences"** (May 27, 2026) by Lyttelton,
Massenkoff, Wilmers. Survey of 1,260 quantitative social scientists, Feb–Mar 2026.

**Channel:** claude-liam — Kokoro `af_kore`, @HumanitariansAI folder chip, Teardown
register (Feynman × MKBHD), Kore in for Humanitarians AI. Greeting: "Hej, Kore" (Swedish).

**Free pipeline only:** Kokoro voice, no ElevenLabs, no higgsfield, no publishing,
no git commit or push. Run without approval pauses.

**Spec:** 1920×1080 (16:9), 30 fps, audio-first.

**All 6 report figures REBUILT as native animated Remotion graphics.** No screenshots.

**Output:** `brutalist-art/youtube/claude-liam-coding-agents-social-sciences/`

---

## Story (Teardown register)

Hook: 81% tried AI. 20% use coding agents. That 20% posts 73% more working papers.
And it's not who you'd hope: economists in, education out; juniors in, tenured out;
men at 2× the rate of women.

Act 1 — Chat vs Agent: the distinction that carries the report (B01)
Act 2 — Discipline gradient (B02) + who adopts (B03)
Act 3 — What they use it for: code, not prose (B04)
Act 4 — The productivity ladder and last mile (B05) — centerpiece
Act 5 — The expectations paradox (B06)

---

## Figures

### B01 — CodingAgentsFig1Loop
Phase 1: chatbot loop (4 nodes) vs agent loop (6 nodes, RUN in terracotta).
Phase 2: stat band — 81% / 20% (terracotta) / 86% Claude Code.

### B02 — CodingAgentsFig2Gradient
Dumbbell chart. 8 disciplines, agent (terracotta filled) vs AI use (open circle).
Reference rules at 19% / 81%. Terracotta ring on Communication (86% AI / 6% agent).

### B03 — CodingAgentsFig3Who
Two-phase horizontal bars. Phase 1: AI-use (nearly equal by gender, 81/78).
Phase 2: agent-use (gender gap explodes: 22 vs 9, terracotta). All p<0.05.

### B04 — CodingAgentsFig4Use
Paired bars (agent users / other AI users) in cascade rank order, 6 use cases.
Terracotta on Draft prose bar; annotation: "slop panic is here."

### B05 — CodingAgentsFig5Ladder
Horizontal dot-whisker. Ladder climbs: +9*, +33**, +73** (terracotta peak).
Then falls flat: +3, -6 (second terracotta "last mile" annotation).

### B06 — CodingAgentsFig6Paradox
Left panel: two rising lines vs use cases (terracotta gap fill).
Right panel (phase 2): paired bars non-agent / agent. Stat chips.

---

## Closing block (B07–B09)

**B07 VERDICT** — `ClaudeVerdictArtifact`
**B08 YOUR TURN** — `ClaudeComposerAsk` greeting="Your turn."
Prompt: "Here's my research question and a description of my dataset. Plan the full
analysis pipeline, then split it honestly: which steps could you run autonomously
as a coding agent, and which decisions should stay mine?"
**B09 OUTRO** — `ClaudeTitleOutro` — "Claude, Peer-Reviewed." / @HumanitariansAI / Kore, in for Humanitarians AI.

---

## Required outputs

- `beat_sheet.json` ✓
- `claude-liam-coding-agents-social-sciences.mp4` ✓ (247.3s, 1920×1080)
- `SOURCES.md` ✓
- `BUILD-PROMPT.md` ← this file
- `_qc/REPORT.md` ✓
