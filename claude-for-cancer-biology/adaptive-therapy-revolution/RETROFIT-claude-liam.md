# Retrofit note — adaptive-therapy-revolution → claude-explainer (Liam)

**What changed vs the original nbb/Onda cut**

- **Terminal swap:** every `NikBearBrownTerminalAsk` (dark Onda terminal) → `ClaudeComposerAsk` (the cream Claude composer). Cold open is now the composer, per the cold-open law — never a brand card.
- **Real, runnable prompts:** B02 (research) and B06 (revision) are literal Claude prompts you can paste and run; `adaptive_audit.py` (B04) runs as-is with `python3`.
- **Script + visualization discussion:** B04 walks through the analysis script; B05 shows its output as a one-page `ClaudeWindow` artifact (the PFS table). ASK→RESULT is honored — B02 ask → B03 evidence, B06 ask → B07 table.
- **Paper/table slots for you to fill** (drop a PNG, it auto-animates; empty = slate):
  - `media/B01.png` — MTD-vs-adaptive schematic or Gatenby 2009 competition figure
  - `media/B03.png` — Zhang 2017 Kaplan-Meier PFS curve (+ `media/B03.source.txt`)
  - `media/B07.png` — revised drug-holiday table, or Strobl 2021 cost-of-resistance figure
- **"Your turn." handoff (B09)** + **title-restate outro (B10)**, both composer/outro scenes.
- **Liam voice:** kokoro `am_onyx`, IN-FOR-BEAR law applied — B00 first breath "this is Liam, in for Bear," outro "Liam, in for Bear." Greeting `Namaste, Liam` (Hindi; Wagwan stays Bear's).
- **Honesty fix:** original said the trial "doubled" PFS; sources show 27.0 vs 16.8 mo (~1.6×), so Liam says the real numbers.

**Spine (11 beats):** B00 ASK · B01 PROBLEM(slot) · B02 RESEARCH-ASK · B03 EVIDENCE(slot) · B04 SCRIPT · B05 TABLE(artifact) · B06 REVISION-ASK · B07 CATCH(slot) · B08 VERDICT(artifact) · B09 HANDOFF · B10 OUTRO.

**Not done (needs you / a build pass):** GATE P sign-off, audio (`generate_audio.py` in am_onyx), the three media slots, and the Remotion render. This is a beat-sheet retrofit only — no audio spent.
