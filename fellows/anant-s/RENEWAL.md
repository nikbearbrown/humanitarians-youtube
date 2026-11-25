# Renewal Request — Anant S.

- **Role:** AI Engineer
- **Supervisor:** SanajanaRao
- **Current agreement:** 10/21/2026 to 11/28/2026
- **Requested period:** 11/30/2026 to 1/23/2027
## What the current period produced

**STEM AI explainer series: eight films, complete.** Each is a 3840×2160 master made with the brutalist.art toolkit and runs about 29.5 minutes in total. Every figure below comes from the toolkit's own checks.

- **Eight topics, one format.** Attention, Bayes' theorem, softmax and temperature, RAG, nonlinearity, overfitting, backpropagation and gradient descent.
    - Every film uses the same ai-explainer spine: an ask typed into Claude, a one-line summary written and corrected on screen, a Manim lesson with real numbers, a verdict recap, a "Your turn" prompt and a title outro.
    - Three films first built in other formats (TL;DR and show-tell) were rebuilt to match the series.
- **Checked, not eyeballed.** Every final passed:
    - GATE V (frames), GATE T (type), the bookend check, the master check and loudness (about −24.7 LUFS);
    - a check written for this series that samples every 2 seconds for review labels or a bottom strip.
    - Hand review of every beat still caught one defect the gates missed: Bayes B12 rendered blank. It was fixed before delivery.
- **Evidence behind every number.** Each film has a fact-check, a sources list and a runnable demo that produces the numbers shown on screen.

**RL Environment video reviews.** 81 videos from 11 fellows were reviewed against the brutalist.art format.

- 23 were sent for approval.
- 2 were sent back for changes.
- Fixes were emailed to fellows: 4K, the "B0x REMOTION" footer, and the project name.

**Toolkit on Windows.** With Claude Code, the brutalist.art pipeline was set up and made to run on Windows. This covered npx resolution, LF line endings, UTF-8 output, fonts and a frame-quantized Manim clock. Two text-size bugs in shared components were fixed: ClaudeDefinitions and the TL;DR cards were set at 48 px, which failed the 41 px floor. Five small tools were written for the series:

- `render_queue.sh`: renders one film at a time, through every gate;
- `check_no_labels.py`: the label and bottom-strip check;
- `pad_silence.py`: lead and tail silences;
- `qc_sheets.py`: contact sheets for hand review;
- `convert_to_ai_explainer.py`: the format conversion.

### Evidence

| Week | Work | Drive | Log |
|---|---|---|---|
| [25–31 Oct](./2026-10-30-attention-one-head-at-a-time/) | Attention, One Head at a Time | [folder](https://drive.google.com/drive/folders/15iGSsUDIPzx1JctBB2fqOnfMBC_9GrnE) | [log](./2026-10-30-attention-one-head-at-a-time/FRICTIONAL.md) |
| [25–31 Oct](./2026-10-30-bayes-theorem/) | Bayes' Theorem: The Positive That's Usually Wrong | [folder](https://drive.google.com/drive/folders/15iGSsUDIPzx1JctBB2fqOnfMBC_9GrnE) | [log](./2026-10-30-bayes-theorem/FRICTIONAL.md) |
| [1–7 Nov](./2026-11-06-softmax-and-temperature/) | Softmax and Temperature, Explained | [folder](https://drive.google.com/drive/folders/1w-Bz0R9QjZE2HX4Egg_fujYbSnVPtRb2) | [log](./2026-11-06-softmax-and-temperature/FRICTIONAL.md) |
| [1–7 Nov](./2026-11-06-how-rag-works/) | How RAG Works | [folder](https://drive.google.com/drive/folders/1w-Bz0R9QjZE2HX4Egg_fujYbSnVPtRb2) | [log](./2026-11-06-how-rag-works/FRICTIONAL.md) |
| [8–14 Nov](./2026-11-13-why-networks-need-a-bend/) | Why Neural Networks Need a Bend | [folder](https://drive.google.com/drive/folders/1SlLqr6rzO6sGKukxhy-S5gk-9tCDSl9a) | [log](./2026-11-13-why-networks-need-a-bend/FRICTIONAL.md) |
| [8–14 Nov](./2026-11-13-overfitting/) | Overfitting, When a Perfect Score Lies | [folder](https://drive.google.com/drive/folders/1SlLqr6rzO6sGKukxhy-S5gk-9tCDSl9a) | [log](./2026-11-13-overfitting/FRICTIONAL.md) |
| [15–21 Nov](./2026-11-20-backpropagation/) | Backpropagation, One Error at a Time | [folder](https://drive.google.com/drive/folders/1zudlUZG4n6vUShgp1M1VU1pwPly0YjMR) | [log](./2026-11-20-backpropagation/FRICTIONAL.md) |
| [15–21 Nov](./2026-11-20-gradient-descent/) | Gradient Descent, One Step at a Time | [folder](https://drive.google.com/drive/folders/1zudlUZG4n6vUShgp1M1VU1pwPly0YjMR) | [log](./2026-11-20-gradient-descent/FRICTIONAL.md) |
| 25 Oct – 21 Nov | RL Environment video reviews (81 videos) | [tracker](https://docs.google.com/spreadsheets/d/1ovAQ1N19bqlFgjhSuC8Aw4wnvSKzbTsFxt5qtOYzaY4/edit) | - |

Weekly hours: [HOURS.md](HOURS.md). Each video folder has its own Frictional log, listed in [README.md](README.md).

## Plan for the requested period

1. **Two STEM AI explainers a week**, in the same ai-explainer format, each with its fact-check, sources and evidence demo.
1. **RL Environment reviews** continue weekly: clear the reviewed-but-pending queue and keep the tracker current.
1. **A 9:16 Short for each film**, built as its own beat sheet as the toolkit requires. The reference fellow ships one per explainer.

Reporting continues the same way: a dated Frictional log per video folder, weekly hours, and the review tracker.

## Open items I am carrying

- Replace the Drive copies, which are the earlier labelled review cuts (`-slate.mp4`), with the clean masters.
- Add YouTube links for the RL Environment videos uploaded so far; the tracker does not record them.
- Send the 56 reviewed RL Environment videos that are still pending through the approval step.
