# What Distributed Training Actually Looks Like

**Series:** STEM Explainer
**Status:** Complete

---

## About the Video

Training a large model on one GPU quickly runs into two limits: not enough memory, and not enough time. Distributed training solves this by spreading the work across several GPUs.

There is more than one way to split that work:

- **Data parallelism:** each GPU holds a full copy of the model and trains on a different batch of data.
- **Model parallelism:** the model itself is split across GPUs, for when it is too large to fit on one.

Either way, the GPUs need to stay in sync by sharing what they have learned after each step. A communication pattern called **all-reduce** makes this possible.

This video explains what each approach looks like, when to use which, and where the slowdowns hide.

## Key Takeaways

- **The model weights are the small part.** For a 7-billion-parameter model, the optimizer and gradients take up most of the memory, for a total of 112 GB. That is more than one 80 GB GPU can hold.
- **Data parallelism is the easy option,** but every step needs a sync across all GPUs.
- **Ring all-reduce keeps that sync efficient,** because each GPU sends about the same amount of data however many GPUs there are.
- **Model parallelism makes room for larger models,** at the cost of some idle time.
- **The real limit is communication.** Moving data between GPUs matters more than raw computing power.

## Video Outline

| # | Section | What it covers |
|---|---|---|
| 1 | Opening | What most explanations of distributed training leave out |
| 2 | One GPU Isn't Enough | How much memory a 7B model really needs |
| 3 | Data Parallelism | Same model on every GPU, with different data |
| 4 | All-Reduce | How GPUs share results without a bottleneck |
| 5 | Model Parallelism | Splitting the model by layer, and the idle time that causes |
| 6 | The Full Stack | How real training combines all three approaches |
| 7 | Summary | The main ideas in one place |
| 8 | Your Turn | A prompt for viewers to try with their own model |
| 9 | Outro | Closing title |

## Project Structure

```
README.md               — this file
beats.json              — summary of each scene
beat_sheet.json         — full scene-by-scene plan, with narration and timings
narration/              — narration audio for each scene
visuals/                — visuals for each scene
short/beat_sheet.json   — scene plan for the short version
FRICTIONAL.md           — friction log
REPORT.md               — video report
```

