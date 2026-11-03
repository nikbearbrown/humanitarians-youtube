# BUILD-LOG — The Asymmetry That Flips: Why Checking AI Is Harder Than Running It

## Metadata
- **Candidate**: Candidate 13 — The Asymmetry That Flips: Why Checking AI Is Harder Than Running It
- **Source**: `computational-skepticism-for-ai/chapters/01-the-skeptics-toolkit.md`
- **Slug**: `asymmetry-that-flips`
- **Chassis**: `course-skepticism` / `hai-simple` (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **Register**: Plain (explain the mechanism clearly, then stop)
- **Voice**: Liam (`am_onyx`, in for Bear)
- **Visuals**: Manim (Balance scale with weight morph and accumulating debt blocks) + Remotion (Hesitant Writer open, quote, your turn, outro)

## Narrative Structure & Audit
1. **Cold Open**: B00 (Hesitant writer corrects misconception: in classical CS checking is cheap, but with generative AI checking is what costs everything).
2. **Stakes First**: B01, B02 (Classical solve-verify asymmetry in digital cryptography: $\mathcal{O}(2^n)$ solving vs $\mathcal{O}(n^k)$ verifying; $10^9:1$ leverage that built modern software engineering).
3. **Anchor Planted**: B03 (The foundation of digital security: public key systems, digital signatures, cryptographic proofs).
4. **Wrong Guess & Falsification**: B04, B05 (The naive assumption that AI output is just cheap software; falsified by the reality that verifying 400 lines of generative output demands deep human domain expertise).
5. **Epistemic Mechanism (Morph Move)**: B06, B07, B08 (The scale inverts: 15ms / $0.001 solve weight drops while 300s / $25.00 human verify weight piles up; unverified outputs accumulate into silent epistemic debt).
6. **Limit & Automated Judges**: B09, B10 (The limit of automated judges: LLM-as-a-judge duplicates statistical blind spots one layer up rather than restoring formal asymmetry).
7. **Both Directions**: B11 (Direction 1: Where asymmetry holds — deterministic specs, test suites, compilers), B12 (Direction 2: Where asymmetry flips — natural language reasoning, open-ended analysis).
8. **Carry-Out**: BCRY ("Model outputs cost milliseconds and fractions of a cent while verifying them takes scarce human expertise — unverified outputs pile up looking like successes, so systems must be designed so the check a human can afford reveals what matters.")
9. **Your Turn**: BHTF (Prompt to audit deployed AI pipelines for generation vs verification costs and unverified debt).
10. **Outro**: BOUT (Series restatement + @HumanitariansAI skin).

## Quality & Gate Verification
- **Gate T (Type Lock)**: PASS — 16/16 beats checked with 0 failures; all font sizes ≥ 20px floor, high-contrast dark plates for terracotta accents.
- **Audio Synthesis**: Synthesized via Kokoro `am_onyx` (Liam, in for Bear); measured durations written back to `beat_sheet.json`.
- **Manim Render**: 12 custom scenes rendered at 24fps (B01–B12) implementing the kinetic scale balance and morphing debt moves.
- **Remotion Render**: 4 custom Remotion compositions rendered at 4K/24fps with `--scale=2`: B00 (`BrutalistHesitantWriter`), BCRY (`WantQuote`), BHTF (`ClaudeComposerAsk`), BOUT (`OutroCTA`).
- **Compilation**: Assembled via `compile.py` to 4K (`3840×2160`), 24 fps, total runtime 195.17s.
- **Gate Audio**: PASS — `mean_volume: -23.8 dB`, `max_volume: -2.9 dB` (audible threshold > -40 dB verified via volumedetect).
- **Gate V**: PASS — Visual inspection of frame sequence verified branding, typography (`EB Garamond`, `Helvetica Neue`), palette (`#FAF9F5`, `#3D3929`, `#D97757`), margins, safe insets, and WCAG contrast.
- **Delivery**: Packaged and delivered via `deliver.py --push`.
