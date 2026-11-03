# PEDAGOGY — From Annotated Data to Training a Computer Vision Model (Episode 4)

This reel is a Pragmatist-register explainer for the National Loon Center series,
following the dataset, metadata, and annotation episodes. The one idea: labeled
annotation data is what teaches a YOLO-style detector to find loons, but the
model is only as good as the annotations and evaluation behind it — and there is
no production-ready detector yet, only the pipeline being established for one.

## Act structure
- B00 open — recap the series so far, frame this episode's move into training
- B01 layered thesis — how training turns labeled examples into recognition
- B02 chip-grid — what an object detector like YOLO actually returns (box + confidence)
- B03 source-flow — annotations to a trained, evaluated detector
- B04 binary decision — consistent vs. inconsistent annotations, and what each does to the model
- B05 chip-grid — what evaluation on unseen images must check
- B06 layered thesis — why real-world condition diversity is required to generalize
- B07 source-flow — the complete system vision, footage to researcher application
- B08 verdict artifact — the honest state of the pipeline
- B09 handoff — the next-episode prompt
- B10 title-restatement outro

## Illustrate-law check
- The Claude composer appears only at the open, the handoff, and the framing.
- Every body beat illustrates its concept through a visual state change.
- No two consecutive body beats share the same pattern.

## Evidence and honesty note
- The "Loon, 92% confidence" example is explicitly illustrative — the source
  script itself frames it as "a future result might look something like," never
  as a real measured result. The on-screen chip is labeled "(illustrative)" so
  it can't be misread as an actual metric.
- No other numbers appear anywhere in the reel.
- It states plainly that no production-ready loon detection model exists yet,
  and that the current goal is establishing the complete pipeline, not shipping
  a finished model.
- The variability list (altitude, lighting, water reflections, camera angle,
  weather, distance) and the evaluation list (missed/incorrect detections,
  location accuracy, held-out test images) are quoted directly from the source
  script, not invented.
- The two pipeline diagrams (images -> annotations -> dataset prep -> training
  -> evaluation -> detection; and raw footage -> metadata -> annotation ->
  training dataset -> model -> detection -> researcher application) are the
  source script's own stated processes, reused verbatim.

## Human review checklist
- Confirm the narration sounds like an episode of an ongoing series, not a hard pitch.
- Confirm the honest "no production model yet" framing survives to the verdict beat.
- Confirm the illustrative confidence-score example reads as illustrative on screen.
- Confirm the handoff prompt sets up the next episode (YOLO training internals).

Review the narration above, then replace the blank below with the word that
means approved, and save.

VERDICT: PASS     — reviewer: Swara     date: 2026-09-05
