# PROMPTS.md -- claude-liam-sers-transformer-fix

This reel has no open slots requiring human-supplied or externally
generated media. Every beat resolves entirely through the pipeline's own
renderers:

- B00, B01, B06, B07, B08 -- rendered via Remotion (ClaudeComposerAsk,
  BrutalistHesitantWriter, ClaudeVerdictArtifact, ClaudeTitleOutro), driven
  entirely by props authored directly in beat_sheet.json. No external
  image, video, or AI-generation prompt was needed for any of these beats.

- B02, B03, B04, B05 -- rendered via custom Manim scenes
  (B02_TheMissingVerdict, B03_QualifyingTheClaim, B04_TheGapIdentified,
  B05_ClosingTheGap) written directly in scenes.py for this reel. No
  external asset or generation prompt was needed; all four are fully
  procedural, deterministic diagrams.

No pantry media, no historical images, no AI-video generation requests, and
no screen captures were required anywhere in this build.
