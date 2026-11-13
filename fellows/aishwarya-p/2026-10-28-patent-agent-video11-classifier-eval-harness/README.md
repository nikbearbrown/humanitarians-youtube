# 2026-10-28 - Measuring the Classifier (patent agent progress video 11)

**Week covered:** 2026-10-24 - 2026-10-30

**Video:** `patent-agent-video11-classifier-eval-harness.mp4` (16:9) · `patent-agent-video11-classifier-eval-harness-short.mp4` (9:16)

**YouTube:** Not yet published.

**Process log:** [FRICTIONAL.md](./FRICTIONAL.md)

## Result

The Mycroft patent reader includes a classifier that labels each independent patent claim's protection scope (breadth: broad or narrow; posture: defensive, offensive or exploratory). Its readings had been coming back narrow and defensive. Reading a few outputs by hand can't tell whether that comes from the patents or from the prompt. This week built the tools to measure it.

- **An evaluation harness now exists.** It scores the classifier against hand labels with:
  - accuracy;
  - Cohen's kappa;
  - a majority-class baseline;
  - a collapse check that flags any single answer covering 80% or more of the output.
- **The harness was tested offline first.** A fake classifier that always says narrow/defensive scored kappa 0.00 on both dimensions, and both collapse warnings fired. No API calls were made.
- **One query instead of sixteen.** The patents table isn't partitioned or clustered, so a one-patent lookup scans 127.6 GB (~$0.73). The pool query scanned 161.8 GB (~$0.92 at list price) and returned 160 candidates in a single query.
- **The data changed the plan.** 147 of the 160 candidates have only 1-3 independent claims; 13 have 4 or more (57 / 46 / 44 / 8 / 5).
- **The test set is 50 independent claims from 16 patents.** That's 2 per CPC section A-H, at most 4 per patent.

**Not finished:** the 50 claims had not been labelled by hand. Labelling was paused for project lead review, so there is no accuracy number in this week's work.

---

## The built reel

| | |
|---|---|
| 16:9 master | `patent-agent-video11-classifier-eval-harness.mp4`: 3840×2160, 24fps, 185.49s |
| 9:16 short | `short/patent-agent-video11-classifier-eval-harness-short.mp4`: 2160×3840, 24fps, 176.70s; 7 beats plus a silent end card; B00A is not in the short; no channel-title overlay in the short's beat sheet |
| review cut | `patent-agent-video11-classifier-eval-harness-slate.mp4` |
| beats | 8: 4 Remotion bookends (B00A, B00, B05, B06) and 4 Manim content beats (B01-B04) |
| voice | Kokoro `af_bella` |
| build | 8 of 8 beats filled (`STATUS.md`) |
| gates | GATE P: `PEDAGOGY.md` signed `VERDICT: PASS` · GATE V master: 16 frames, 0 BLOCKER, 9 MAJOR · GATE V short: 16 frames, 0 BLOCKER, 8 MAJOR |

---

## Figure → beat map

| Beat | Act | Scene | Duration | What it argues |
|---|---|---|---|---|
| B00A | Intro | `ClaudeComposerAsk` | 13.29s | Presenter summary |
| B00 | Intro | `ClaudeComposerAsk` | 14.12s | Cold open: same answer every time, and reading outputs can't say why |
| B01 | Problem | `B01_EvalHarness` | 41.10s | The harness: kappa, baseline, collapse check |
| B02 | Method | `B02_OneQueryNotSixteen` | 37.58s | One query for 160 candidates; the final 16 picked locally |
| B03 | Finding | `B03_IndependentClaimFinding` | 43.13s | 147 of 160 patents have 1-3 independent claims; how the 16 were picked |
| B04 | Honest gap | `B04_WhatsNotDoneYet` | 18.65s | Labelling paused for lead review; no accuracy number yet |
| B05 | Next steps | `ClaudeComposerAsk` | 13.27s | Handoff: check a data assumption against a real sample |
| B06 | Outro | `ClaudeTitleOutro` | 4.35s | Title restate |

Manim scenes are in [scenes.py](./scenes.py).

## Things not to get wrong

1. **There is no accuracy number in this week's work.** The harness is built and the data is real, but the claims were not labelled yet. Whether the classifier is stuck on narrow/defensive was still open. B04 says so. See [PEDAGOGY.md](./PEDAGOGY.md), Friction protected.
2. **"$0.92" is the list price, not a confirmed charge.** The project may be inside BigQuery's free tier, in which case the actual charge was $0. The narration says "ninety-two cents at list price".
3. **Kappa 0.00 is a test of the harness, not a result about the real classifier.** It came from a fake always-narrow/defensive classifier on synthetic labels.
4. **The 50-claim set has a selection rule that may skew it.** Only patents with 3 or more independent claims were eligible, which may favour broadly drafted patents. B03 states the rule.
5. **"About five independent claims per patent" was the plan's assumption, not a documented figure.** It was inferred from the plan of ~50 claims from 8-10 patents. The narration says "assumed".
6. **Sizes are decimal GB.** 161.8 GB is the decimal figure. An earlier draft used the GiB figure; the video and scenes use GB throughout.

## Known defects

From the build's Gate V reports (`_qc/REPORT.md` for the master and `short/_qc/REPORT.md` for the short):

- **Master:** 9 MAJOR `underfill` flags (content fills less than 55% of the safe area) on B01, B02, B03, B04, B06. No BLOCKERs.
- **Short:** 8 MAJOR `underfill` flags on B01, B02, B03, B04, B06, END. No BLOCKERs.

From [FRICTIONAL.md](./FRICTIONAL.md):

- **The short's automatic plan dropped B03 and garbled the outro.** The short was rebuilt dropping B00A instead, keeping the original outro.
- **The channel handle overlay caused an edge-bleed BLOCKER in portrait.** `channel_title` was removed from the short's beat sheet only, and `compile.py` was not changed.

## Files

- [README.md](./README.md): this page.
- [NARRATION.md](./NARRATION.md): the approved narration, one paragraph per beat.
- [beat_sheet.json](./beat_sheet.json): the edit: 8 beats, narration, scene per beat, measured audio durations, build stamp.
- [scenes.py](./scenes.py): the four Manim content scenes (B01-B04).
- [PEDAGOGY.md](./PEDAGOGY.md): act structure, evidence table, friction protected, `VERDICT: PASS`.
- [FRICTIONAL.md](./FRICTIONAL.md): the process log for this work.
