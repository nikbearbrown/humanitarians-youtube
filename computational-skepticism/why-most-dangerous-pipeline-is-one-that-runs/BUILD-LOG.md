# BUILD-LOG — Why the Most Dangerous Pipeline Is the One That Runs Perfectly

## Metadata
- **Candidate**: Candidate 29 — Why the most dangerous pipeline is the one that runs perfectly
- **Source**: `computational-skepticism-for-ai/chapters/09-delegation-trust-and-the-supervisory-role.md` (§ "Delegation, Trust, and the Supervisory Role / The Delegation Map")
- **Slug**: `why-most-dangerous-pipeline-is-one-that-runs`
- **Chassis**: `course-skepticism` / `hai-simple` (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **Register**: Plain (explain the epistemic mechanism, then stop)
- **Voice**: Liam (`am_onyx`, in for Bear)
- **Visuals**: Manim (`trace` move, six-box clinical triage pipeline, delegation map items 1–4 vs 5–8, asymmetric failure surface) + Remotion (`BrutalistHesitantWriter` open, `WantQuote` carry-out, `ClaudeComposerAsk` your turn, `OutroCTA` outro)

## Six-Move Audit
1. **Open / Hesitant Writer**: B00 (Naive question typed: "When an AI pipeline runs with zero errors, doesn't that mean it succeeded?" → hesitated → corrected: "A broken pipeline halts. An unsupervised pipeline runs.").
2. **Stakes First**: B01, B02 (Loud exceptions vs silent failures: Syntactic crashes halt execution immediately; epistemic failures run cleanly with exit code 0 while producing active harm).
3. **Wrong Guess & Falsification**: B03, B04 (Items 1 to 4: Standard engineering contracts govern execution syntax vs Items 5 to 8: Supervisory additions govern epistemic truth and failure routing).
4. **Epistemic Mechanism**: B05 (The Asymmetric Failure Surface: Syntactic execution vs semantic correctness).
5. **Anchor Planted**: B06 (The Six-Box Clinical Pipeline: Ingest, Context, Infer, Format, Audit, Dispatch — kinetic tracking dot traces through stages 1 to 4 with all monitors lighting bright green).
6. **Anchor Payoff (Manim Move: `trace`)**: B07 (Tracing Stages 5 & 6: The missing supervisory guardrails allow fluent-but-wrong output to dispatch into real-world patient records with exit code 0).
7. **Limits & Both Directions**: B08 (The False Equivalence: Delegation is not an unverified partition of labor), B09 (Direction A: Valid schema ⇏ true output), B10 (Direction B: Syntactic crash ⇏ bad supervision; failing loudly is safety working), B11 (The Calibrated Supervisory Contract: items 5–8 specified with testable handoffs).
8. **Carry-Out**: BCRY ("The failure that costs you is the one that does not stop the pipeline.")
9. **Your Turn**: BHTF (Claude composer prompt auditing critical automated pipeline steps against items 1 through 8).
10. **Outro**: BOUT (Title restatement + @HumanitariansAI skin).

## Quality & Gate Verification
- **Gate T (Type Lock)**: PASS — All 15 beats verified via `type_check.py` (0 FAILs). Resolved contrast and minimum font run size across Manim scenes; avoided en-dash ligature thin-run artifacts; maintained ink distance thresholds.
- **Audio Synthesis**: Kokoro `am_onyx` (Liam, in for Bear); measured durations synchronized into `beat_sheet.json`.
- **Manim Render**: 11 custom scenes rendered at 1080p24 (B01–B11) with Gate T compliance, implementing the `trace` kinetic move across the 6-stage pipeline.
- **Remotion Render**: 4 custom Remotion compositions rendered at 4K/24fps: B00 (`BrutalistHesitantWriter`), BCRY (`WantQuote`), BHTF (`ClaudeComposerAsk`), BOUT (`OutroCTA`).
- **Compilation**: Conformed and compiled via `compile.py` to 4K (`3840×2160`), 24 fps, total runtime 204.83s.
- **Gate Audio**: PASS — `mean_volume: -23.8 dB` (> -40 dB audible threshold verified; peak -2.9 dBTP).
- **Gate V**: PASS — Visual inspection of sampled frames verified layout, typography, cream ground (`#FAF9F5`), warm ink (`#3D3929`), terracotta accent (`#D97757`), safe-insets, pipeline tracking dots, and UI prompt styling.
- **Delivery**: Ready for two-target delivery packaging via `deliver.py --push`.
