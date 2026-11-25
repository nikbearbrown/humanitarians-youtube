# 2026-10-29 - What Is RLHF? (STEM/AI concept video)

**Week covered:** 2026-10-24 - 2026-10-30

**Video:** `what-is-rlhf.mp4` (16:9) · `what-is-rlhf-short.mp4` (9:16)

**YouTube:** Not yet published.

## Result

A concept video on reinforcement learning from human feedback, the training stage that turns a pretrained text predictor into an assistant.

- **It opens on the InstructGPT result.** People preferred a 1.3B-parameter model over the 175B-parameter GPT-3, despite 100x fewer parameters.
- **It walks the three stages as OpenAI published them:**
  1. supervised fine-tuning on labeller demonstrations;
  2. a reward model trained on labeller rankings;
  3. reinforcement learning with PPO and a drift penalty.

  It notes that ChatGPT used the same methods.
- **It covers how Anthropic's Constitutional AI and RLAIF replace some human labels with AI feedback.** It ends on what that does not remove: humans still write the principles, and the feedback is only as good as the judging model.

---

## The built reel

| | |
|---|---|
| 16:9 master | `what-is-rlhf.mp4`: 3840×2160, 24fps, 162.69s |
| 9:16 short | `short/what-is-rlhf-short.mp4`: 2160×3840, 24fps, 167.19s; all 9 beats plus a silent end card; no channel-title overlay in the short's beat sheet |
| review cut | `what-is-rlhf-slate.mp4` |
| beats | 9: 4 Remotion bookends (B00A, B00, B05, B06) and 5 Manim content beats (B01, B02, B03, B04, B04B) |
| voice | Kokoro `af_bella` |
| build | 9 of 9 beats filled (`STATUS.md`) |
| gates | GATE P: `PEDAGOGY.md` signed `VERDICT: PASS` · GATE V master: 18 frames, 0 BLOCKER, 11 MAJOR · GATE V short: 20 frames, 0 BLOCKER, 8 MAJOR |

---

## Figure → beat map

| Beat | Act | Scene | Duration | What it argues |
|---|---|---|---|---|
| B00A | Intro | `ClaudeComposerAsk` | 12.61s | Presenter summary |
| B00 | Intro | `ClaudeComposerAsk` | 19.54s | Cold open: a model 100x smaller was preferred, because of how it was trained |
| B01 | Method | `B01_SupervisedFineTuning` | 22.63s | Stage 1: supervised fine-tuning on labeller demonstrations |
| B02 | Method | `B02_RewardModel` | 19.46s | Stage 2: a reward model trained on labeller rankings |
| B03 | Method | `B03_PPOOptimization` | 25.39s | Stage 3: RL with PPO and the drift (KL) penalty; ChatGPT used the same methods |
| B04 | Change | `B04_ConstitutionalAI` | 21.42s | Constitutional AI: no human data on harmlessness; self-critique against principles |
| B04B | Change | `B04B_RLAIF` | 22.44s | RLAIF: an AI judge in place of the human ranker; comparable to RLHF; the limits |
| B05 | Next steps | `ClaudeComposerAsk` | 15.06s | Handoff: write one preference label yourself |
| B06 | Outro | `ClaudeTitleOutro` | 4.14s | Title restate |

Manim scenes are in [scenes.py](./scenes.py).

## Things not to get wrong

1. **"The difference wasn't parameters or data" was not used.** RLHF is itself new data (demonstrations and rankings), and ChatGPT started from a newer GPT-3.5-series model. The video says the smaller model "wasn't bigger or better read" and rests the claim on the InstructGPT comparison.
2. **Constitutional AI removes human data on harmlessness, not all human feedback.** That matches Anthropic's wording. The video doesn't claim Claude is trained with no human feedback at all.
3. **RLAIF is "comparable" to RLHF, not "better".** That matches the 2023 study's wording.
4. **The limits are stated.** B04B ends on them: humans still write the principles, and AI feedback is only as good as the model giving it. The first half is sourced (Bai et al. 2022); the second is framed as a limitation, not a finding.
5. **The PPO drift penalty comes from the InstructGPT paper body, not its abstract.**
6. **ChatGPT's training is sourced to OpenAI's "Introducing ChatGPT" post.** The page returned 403 to an automated fetch, so its content was corroborated through Wikipedia's ChatGPT article.
7. **"Ranking is faster than writing" is a practical point from the method's design.** It is not a measured claim.
8. **The B02 answer letters and ranking are illustrative.** No scene shows an invented score or metric.

See [PEDAGOGY.md](./PEDAGOGY.md) for the full evidence table and sources.

## Known defects

From the build's Gate V reports (`_qc/REPORT.md` for the master and `short/_qc/REPORT.md` for the short):

- **Master:** 11 MAJOR `underfill` flags (content fills less than 55% of the safe area) on B01, B02, B03, B04, B04B, B06. No BLOCKERs.
- **Short:** 8 MAJOR `underfill` flags on B01, B03, B04, B04B, B06, END. No BLOCKERs.

## Files

- [README.md](./README.md): this page.
- [NARRATION.md](./NARRATION.md): the approved narration, one paragraph per beat.
- [beat_sheet.json](./beat_sheet.json): the edit: 9 beats, narration, scene per beat, measured audio durations, build stamp, and the source list in its metadata note.
- [scenes.py](./scenes.py): the five Manim content scenes (B01, B02, B03, B04, B04B).
- [PEDAGOGY.md](./PEDAGOGY.md): act structure, evidence table with sources, friction protected, `VERDICT: PASS`.
