# What a Retrieval Pipeline Looks Like in Production

## Description
Most RAG tutorials stop at "embed, store, retrieve." A production retrieval pipeline has six stages, each with its own latency cost: embedding the query, searching the index, rewriting the query when initial results are weak, reranking candidates with a cross-encoder, filtering by metadata, and assembling the final context — all within a latency budget measured in milliseconds. This video walks through each stage and the trade-offs that shape a real system.

## Project structure
```
README.md            — this file
script.md            — full narration + visual direction
beats.json           — beat sheet with timings
narration/           — one .txt per beat
visuals/             — one .md per beat (visual briefs)
audio/               — placeholder for generated audio
```


## Beats as rendered

The five authored beats are the body. Four skeleton beats were added around
them per the `ai-explainer` structure. Durations are measured from the Kokoro
MP3s, which are the master clock; nothing was timed by hand.

| Beat | Pattern | Title |
|------|---------|-------|
| B00 | `ClaudeComposerAsk` | The Ask (cold open) |
| B01 | `RetrievalStages` | The Six Stages |
| B02 | `RetrievalSearch` | Embedding and Search |
| B03 | `RetrievalRewrite` | Query Rewriting |
| B04 | `RetrievalRerank` | Reranking and Filtering |
| B05 | `RetrievalBudget` | The Latency Budget |
| B06 | `ClaudeVerdictArtifact` | Verdict |
| B07 | `ClaudeComposerAsk` | Your Turn |
| B08 | `ClaudeTitleOutro` | Title outro |

## Delivery

Both orientations at 4K:

| Cut | Composition | Master | Runtime |
|-----|-------------|--------|---------|
| 16:9 | 3840×2160 | `retrieval-pipeline-explainer.mp4` | 228.1s (3:48) |
| 9:16 | 2160×3840 | `short/retrieval-pipeline-explainer-short.mp4` | 169.2s (2:49) |


## Rebuild

From the toolkit root:

```sh
python3 runtime/scripts/generate_audio_kokoro.py /retrieval-pipeline-explainer
python3 runtime/scripts/remotion_scenes.py      /retrieval-pipeline-explainer 
./art final /retrieval-pipeline-explainer
```

