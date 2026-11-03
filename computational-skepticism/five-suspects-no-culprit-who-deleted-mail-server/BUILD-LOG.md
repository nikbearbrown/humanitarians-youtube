# BUILD-LOG — Five Suspects, No Culprit: Who Deleted the Mail Server?

## Metadata
- **Candidate**: Candidate 10 — Five Suspects, No Culprit: Who Deleted the Mail Server?
- **Source**: `computational-skepticism-for-ai/chapters/12-accountability-who-is-responsible-when-the-system-fails.md`
- **Slug**: `five-suspects-no-culprit-who-deleted-mail-server`
- **Chassis**: `course-skepticism` / `hai-simple` (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **Register**: Plain (explain the mechanism clearly, then stop)
- **Voice**: Liam (`am_onyx`, in for Bear)
- **Visuals**: Manim (5-node contribution chain with counterfactual trace move) + Remotion (hesitant writer open, quote, your turn, outro)

## Six-Move Audit
1. **Stakes First**: B01, B02 (Documented Agents of Chaos §16.5 incident where privileged mail server deletion tool is triggered on unauthorized conversational prompt; 5 suspects convened for incident review).
2. **Anchor Planted**: B03 (The five-node contribution chain: Request → Defaults → Tool Auth → Deployment Scopes → Execution).
3. **Wrong Guess & Falsification**: B04, B05 (Single-culprit fallacy isolating one actor; falsified by testing sufficiency (0/5 sufficient alone) vs necessity (5/5 necessary to outcome)).
4. **Epistemic Mechanism (Trace Move)**: B06, B07, B08 (Counterfactual trace toggling: Stranger off → no request; Model off → refusal; Framework off → unsigned tool blocked; Deployer off → permission denied; Agent off → execution invariant halts; All 5 lit simultaneously → signal traces through full circuit to wipe server).
5. **Anchor Payoff**: B09 (100% Necessity across all nodes, 0% Sufficiency → Responsibility distributes across the entire topology).
6. **One Flag**: B10 (Upstream architectural regime such as cryptographic credentials and least-privilege scoping vs fragile downstream prompt policing).
7. **Both Directions**: B11 (Direction A: Hunting for a single culprit creates structural blindness), B12 (Direction B: Distributed responsibility requires active human ownership of every link).
8. **Carry-Out**: BCRY ("When every party's choice is necessary and none is sufficient, responsibility distributes across the entire chain.")
9. **Your Turn**: BHTF (Prompt to audit the five contribution nodes of an autonomous tool-calling pipeline).
10. **Outro**: BOUT (Title restatement + @HumanitariansAI skin).

## Quality & Gate Verification
- **Gate T (Type Lock)**: PASS — All 16 beats checked against type specifications with 0 failures.
- **Audio Synthesis**: Synthesized with Kokoro `am_onyx` (Liam, in for Bear); measured durations written back to `beat_sheet.json`.
- **Manim Render**: 12 custom scenes rendered at 24fps (B01–B12) implementing the kinetic `trace` move across the 5-node contribution chain.
- **Remotion Render**: 4 custom Remotion compositions rendered at 4K/24fps with `--scale=2`: B00 (`BrutalistHesitantWriter`), BCRY (`WantQuote`), BHTF (`ClaudeComposerAsk`), BOUT (`OutroCTA`).
- **Compilation**: Assembled via `compile.py` to 4K (`3840×2160`), 24 fps, total runtime 199.00s.
- **Gate Audio**: PASS — `mean_volume: -23.8 dB`, `max_volume: -3.0 dB` (audible threshold > -40 dB verified via ffmpeg).
- **Gate V**: PASS — Visual inspection of frame sequence verified branding, typography (`EB Garamond`, `Helvetica Neue`), palette (`#FAF9F5`, `#3D3929`, `#D97757`), margins, safe insets, and contrast.
- **Delivery**: Packaged and delivered via `deliver.py --push`.
