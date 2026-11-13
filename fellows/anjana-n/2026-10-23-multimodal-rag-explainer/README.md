# Multi-Modal RAG: Retrieving Images, Tables, and Code

## Series
Standalone STEM Explainer

## Concept
Standard RAG embeds text and retrieves text. But real documents contain tables, charts, diagrams, and code blocks — content that loses its meaning when flattened to plain text. Multi-modal RAG treats each content type on its own terms: layout-aware chunking preserves table structure, vision models embed charts as images, code blocks keep their syntax, and structured extraction converts visual content into retrievable representations before anything hits the vector store.

## Voice
Kokoro TTS — am_onyx

## Rendering
Remotion (motion graphics) via toolkit

## Project structure
```
README.md            — this file
script.md            — full narration + visual direction
beats.json           — beat sheet with timings
narration/           — one .txt per beat
visuals/             — one .md per beat (visual briefs)
audio/.gitkeep       — placeholder for generated audio
```
