# Friction Log: What Fine-Tuning a Language Model Actually Changes

**Week:** Week 22, November 22 – 28, 2026

## 1. Date and focus
A video on fine-tuning language models:
- what pre-training already provides
- continued pre-training
- task fine-tuning
- parameter-efficient methods (LoRA and QLoRA)
- when domain data matters more than model size

## 2. What was tried, and what was expected
- The brief's "tiny" adapters were expected to be easy to draw.
- The three methods were expected to be clear as three separate pictures.
- The narration was expected to fit 45 to 70 words per section.

## 3. Where things got stuck, and what was done next
- **Adapters too small to draw:** at true scale, the trained part is 0.14% of the model, under three pixels wide. The scene shows both a to-scale bar.
- **One model, three methods:** all scenes use the same layer stack, so the methods differ only in how much each layer changes. On average, that is all layers for continued pre-training, about half for task fine-tuning, and none for adapters.
- **Ending:** the video ends on the title card instead of fading to dark.
- **Length:** all five sections ran long, and they were kept as written.

## 4. What Claude contributed, and what was kept or changed
- **Original work:** concept, brief and main narration.
- **Claude:**
  - assembled the video using the video generation tool created by Humanitarians AI
  - wrote the opening, summary, viewer prompt and outro
  - raised the adapter scale issue
- **Accepted:** the to-scale bar alongside the not-to-scale diagram, the shared layer stack, and leaving out accuracy numbers.
- **Kept as written:** all narration.

## 5. What is understood now, and what is still open
**Understood:**
- The concepts: pre-training, continued pre-training, task fine-tuning, LoRA and QLoRA, and the trade-off between domain data and model size.

**Open:**
-  None