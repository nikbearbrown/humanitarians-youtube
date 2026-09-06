# SOURCES — From Annotated Data to Training a Computer Vision Model (Episode 4)

| Source | How it is used | Notes |
|---|---|---|
| Swara's Episode 4 script (this reel's source text) | Core narrative: training concept, YOLO, pipeline, evaluation, generalization, full vision | Quoted and condensed, not invented |
| [runtime/remotion/src/Root.tsx](../../runtime/remotion/src/Root.tsx) | Verified composition registry for the Remotion patterns | Ensures the pattern IDs are the registered names |
| [videos/loon-metadata-pipeline](../loon-metadata-pipeline) / [videos/loon-annotation-tool](../loon-annotation-tool) | Prior episodes in the same series | Register, persona, and schema precedent |

## Corrections and honesty log
- The reel stays qualitative except for one number, and that one is explicitly
  illustrative: "Loon — 92% confidence" appears in the source script itself as
  a hypothetical future example ("a future result might look something like"),
  never as a measured result. It is labeled "(illustrative)" on screen.
- The reel states plainly that no production-ready loon detection model exists
  yet, and that the current goal is the complete pipeline, not a finished model.
- The variability list (altitude, lighting, water reflections, camera angle,
  weather, distance to the birds) and the evaluation checklist (missed
  detections, incorrect detections, location accuracy, held-out test images)
  are quoted directly from the source script.
- Both pipeline diagrams shown on screen are the source script's own stated
  processes, reused verbatim rather than paraphrased into something new.
