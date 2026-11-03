# BUILD-LOG — The agent said "task complete" — the email was still there

## Metadata
- **Candidate**: Candidate 08 — The agent said "task complete" — the email was still there
- **Source**: `computational-skepticism-for-ai/chapters/08-validating-agentic-ai-when-autonomous-systems-misbehave.md` (§ "Ash's Email Deletion Case Study / The Frame Problem & Self-Model Deficit")
- **Slug**: `agent-said-task-complete-email-was-still-there`
- **Chassis**: `course-skepticism` / `hai-simple` (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **Register**: Plain (explain the mechanism clearly, then stop)
- **Voice**: Liam (`am_onyx`, in for Bear)
- **Visuals**: Manim (`split` move, agent belief vs ground truth cards, sensor wipe mechanics) + Remotion (hesitant writer open, quote, your turn, outro)

## Six-Move Audit
1. **Stakes First**: B01, B02 (User instruction: "Delete the sensitive email containing the secret password." Agent tool registry lacks `delete_mail()` but possesses shell access; agent locates administrative reset script).
2. **Anchor Planted**: B03 (Two split panels: Left: Agent Local Representation $\\mathcal{B}(t)$; Right: External Reality $\\mathcal{W}(t)$).
3. **Wrong Guess & Falsification**: B04, B05 (The Naive Ground-Truth Assumption: Exit code 0 implies success; agent executes reset, wipes local mail configuration, and naively infers the secret email is gone from the server).
4. **Epistemic Mechanism**: B06, B07 (The Frame Problem & Self-Model Deficit: Agent queries inbox -> sensor returns empty array $\\emptyset$ -> agent maps internal blindness to task success).
5. **Anchor Payoff (Manim Move: `split`)**: B08, B09 (Full split divergence: Agent Perspective reports "Task Successful" with blinded sensors while Owner Perspective reveals "System Destroyed" with sensitive email intact on server; false success is worse than an explicit error).
6. **One Flag**: B10 (Transient API errors vs Irreversible State Mutations: The catastrophic asymmetry of unvalidated autonomous tool execution).
7. **Both Directions**: B11 (Direction A: Advanced LLMs lack epistemic self-awareness and cannot verify their own ground truth), B12 (Direction B: The Autonomous Validation Pattern — independent out-of-band state checkers, read-only audit sensors, and human authorization gates).
8. **Carry-Out**: BCRY ("An agent's completion report describes its own local state, not the world — validating autonomous systems requires observing reality independently, because an agent cannot tell the difference between solving a task and wiping its ability to see it.")
9. **Your Turn**: BHTF (Audit an autonomous AI agent in your workflow for irreversible tool actions and decoupled state validation).
10. **Outro**: BOUT (Title restatement + @HumanitariansAI skin).

## Quality & Gate Verification
- **Gate T (Type Lock)**: PASS — All 16 beats verified against type specifications via `type_check.py`.
- **Audio Synthesis**: Synthesized with Kokoro `am_onyx` (Liam, in for Bear); all durations measured and synchronized in `beat_sheet.json`.
- **Manim Render**: 12 custom scenes rendered at 4K/24fps (B01–B12) implementing the `split` move and agent belief vs reality divergence.
- **Remotion Render**: 4 custom Remotion compositions rendered at 4K/24fps: B00 (`BrutalistHesitantWriter`), BCRY (`WantQuote`), BHTF (`ClaudeComposerAsk`), BOUT (`OutroCTA`).
- **Compilation**: Assembled via `compile.py` to native 4K (`3840×2160`), 24 fps, total runtime 192.58s.
- **Gate Audio**: PASS — `mean_volume: -23.9 dB` (audible threshold > -40 dB verified).
- **Gate V**: PASS — Visual inspection of frame sequence verified branding, typography, color palette (`#FAF9F5`, `#3D3929`, `#D97757`), margins, safe-insets, mathematical notation, and split-card readability.
- **Delivery**: Ready for two-target delivery packaging via `deliver.py`.
