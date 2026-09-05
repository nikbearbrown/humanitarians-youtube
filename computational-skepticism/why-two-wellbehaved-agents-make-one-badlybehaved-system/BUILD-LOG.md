# BUILD-LOG — Why Two Well-Behaved Agents Make One Badly-Behaved System

## Metadata
- **Candidate**: Candidate 19 — Why Two Well-Behaved Agents Make One Badly-Behaved System
- **Source**: `computational-skepticism-for-ai/chapters/08-validating-agentic-ai-when-autonomous-systems-misbehave.md`
- **Slug**: `why-two-wellbehaved-agents-make-one-badlybehaved-system`
- **Chassis**: `course-skepticism` / `hai-simple` (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **Register**: Plain (explain the mechanism clearly, then stop)
- **Voice**: Liam (`am_onyx`, in for Bear)
- **Visuals**: Manim (relay chain of agents passing document with kinetic accumulate move) + Remotion (hesitant writer open, quote, your turn, outro)

## Six-Move Audit
1. **Stakes First**: B00, B01, B02 (Agent A 98% accurate on 10,000 isolated test records, Agent B 97% accurate; chained together in production, the system fails on ~30% of customer runs).
2. **Anchor Planted**: B03 (The three-stage relay chain [Agent A] → [Handoff Document Payload] → [Agent B] → [System Output Action]).
3. **Wrong Guess & Falsification**: B04, B05 (The Addition Fallacy assuming independent coin flips 2% + 3% ≈ 5% failure; falsified because Agent B does not evaluate clean ground truth—it conditions on Agent A's output as unverified reality).
4. **Epistemic Mechanism (Accumulate Move)**: B06, B07, B08 (Kinetic accumulate move: B06 introduces 1 subtle upstream error token in the handoff document; B07 shows Agent B conditioning and spawning 3 dependent derived hallucinations; B08 explodes into 7 operational failure blocks halting the pipeline).
5. **Anchor Payoff**: B09 (Comparison: Isolated benchmark 98%/97% vs Connected relay failure 29.4% — demonstrating the unseen interaction term).
6. **One Flag**: B10 (Typed schema interfaces that throw exceptions and halt cascades immediately vs natural language context passing where downstream LLMs rationalize false premises, supercharging cascades).
7. **Both Directions**: B11 (Direction A: 99% isolated accuracy provides zero guarantee of system safety in unchecked chains), B12 (Direction B: Boundary invariants verifying contracts against world state protect the pipeline).
8. **Carry-Out**: BCRY ("Downstream agents treat upstream outputs as ground truth, so errors do not add—they compound.")
9. **Your Turn**: BHTF (Paste-ready prompt for viewers to audit an agent pipeline by injecting a subtle upstream error and evaluating whether Agent B catches or elaborates on it).
10. **Outro**: BOUT (Title restatement + @HumanitariansAI skin).

## Quality & Gate Verification
- **Gate T (Type Lock)**: PASS — All 16 beats checked against type specifications with 0 failures.
- **Audio Synthesis**: Synthesized with Kokoro `am_onyx` (Liam, in for Bear); measured durations written back to `beat_sheet.json`.
- **Manim Render**: 12 custom scenes rendered at 24fps (B01–B12) implementing the kinetic `accumulate` move across the agent relay chain.
- **Remotion Render**: 4 custom Remotion compositions rendered at 4K/24fps with `--scale=2`: B00 (`BrutalistHesitantWriter`), BCRY (`WantQuote`), BHTF (`ClaudeComposerAsk`), BOUT (`OutroCTA`).
- **Compilation**: Assembled via `compile.py` to 4K (`3840×2160`), 24 fps, total runtime 205.10s.
- **Gate Audio**: PASS — `mean_volume: -23.8 dB`, `max_volume: -2.8 dB` (audible threshold > -40 dB verified via ffmpeg).
- **Gate V**: PASS — Visual inspection of frame sequence verified branding, typography (`EB Garamond`, `Helvetica Neue`), palette (`#FAF9F5`, `#3D3929`, `#D97757`, `#4A7C59`), margins, safe insets, and contrast.
- **Delivery**: Packaged and delivered via `deliver.py --push`.
