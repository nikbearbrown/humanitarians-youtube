# PROMPTS — Why Did the AI Say No?

No open slots: every beat is filled by Remotion or Manim from this folder.

## B80 — viewer prompt (shown and read aloud)
> Here's my script (credit_reasons.py). Train a second boosted model with a different seed and data split. Does
> Applicant A get the same top 3 reasons? How often do the top 3 change across 20 seeds? Show the numbers.

(The narration reads a shorter version: retrain the black box with a different seed; does Applicant A keep the same
top three reasons?)

## Production prompts (AI contribution record)
- Brief for this week: an AI-in-finance explainer, "Why Did the AI Say No?", on explainable AI in lending: when an
  AI credit model denies a loan the lender must give specific reasons; show how a decision splits into per-feature
  contributions (reason codes) and why a black-box model makes that harder. Anchor on ECOA / Regulation B adverse-
  action notices and CFPB Circular 2022-03, optionally the SHAP paper; seed-locked experiment on synthetic
  applicants with plain features and no protected attributes; a logistic scorecard vs a gradient-boosted model;
  Applicant A's top 3 reasons from each; agreement; one counterfactual. 16:9 film and native 9:16 Short. Keep it
  simple: one idea, big visuals, at most one short formula. No legal advice.
- Claude (Claude Code) tried to read the regulation and the circular (official sites blocked; regulation read from a
  GitHub mirror of the official eCFR bulk data, circular from search summaries — see FACTCHECK.md), wrote and ran
  the experiment twice, wrote the script, beat sheets and Manim scenes, and checked frames.
