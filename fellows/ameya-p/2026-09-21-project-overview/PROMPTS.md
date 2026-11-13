# PROMPTS — 2026-09-21-project-overview (Fine-Tuning Platform)

This reel does not call any generative image or video models. All beats are
Remotion scenes rendered from source props, plus one locally-typeset equation
(matplotlib mathtext, not an image generator). The two visible composer
prompts are:

## B00 — the cold-open ASK typed into the composer

> Quick gut check on the fine-tuning platform. What does it actually build,
> and what's the one thing we haven't nailed down yet?

Runs on top of `ClaudeComposerAsk`. Folder chip reads `Fine-Tuning Platform`.
Output lines under the composer:

- 5-stage SFT pipeline
- RL calibration: open question

## B06 — the YOUR TURN prompt for the viewer

> Here are my model's per-decision confidence scores and outcomes. Bin them
> by confidence and show me where stated confidence and actual accuracy
> diverge most.

Rendered by `ClaudeComposerAsk`, greeting `Your turn.`, runningText
"checking your own model's confidence…". Narration reads the prompt aloud
verbatim.

## Beat-prefixed instruction cards

None. This reel's visuals are pure Remotion compositions plus one locally
rendered math SVG (B04, `runtime/scripts/typeset_math.py` — no LaTeX, no
external service). No image/video generators are called; no pantry assets
were needed.
