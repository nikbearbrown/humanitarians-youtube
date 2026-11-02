# Novelty Dampening in Agent Memory — Diversity Without Deletion — Beat Sheet

**Slug:** `claude-liam-novelty-dampening` · **Voice:** Kokoro `am_onyx`

Generated from [`beat_sheet.json`](beat_sheet.json), which is the source of truth: edit the JSON, not this table. Start times add up each beat's rendered duration.

## 12 beats, 1:16 (76.0s)

| # | Act | Start | Dur | Pattern | Motion | Narration |
|---|---|---|---|---|---|---|
| B00 | ASK | 0:00 | 6.4s | ClaudeComposerAsk | type-on | Hello!, this is Liam, in for Kriti. Why does your agent keep retrieving the exact same generic memory? |
| B01 | RETRIEVAL_TRAP | 0:06 | 6.3s | BrutalistHesitantWriter | hesitant-type | In standard semantic search, high similarity scores trap the agent in repetitive recall loops. |
| B02 | CROWDING_OUT | 0:13 | 7.2s | CwcSplitMechanism | split | One generic episode dominates retrieval, crowding out specialized experiences that actually solve the task. |
| B03 | NOVELTY_DAMPENING | 0:20 | 6.9s | CwcMemoryTimeline | illustrate | To restore diversity, we apply Novelty Dampening, penalizing episodes that have been accessed repeatedly. |
| B04 | THE_FORMULA | 0:27 | 6.5s | CwcConceptCard | card-in | The formula divides baseline similarity by one plus alpha times log of one plus access count. |
| B05 | ALPHA_TUNING | 0:33 | 6.4s | CwcConceptCard | card-in | Alpha controls penalty strength, set to zero point one five for balanced, non-destructive dampening. |
| B06 | LOG_DYNAMICS | 0:40 | 6.8s | CwcTwoLayerEval | evaluate | Because dampening scales logarithmically, early accesses face mild friction while chronic overuse drops steeply. |
| B07 | SURFACING_TAIL | 0:47 | 6.2s | CwcMemoryRetrieval | flow | As overused memories slide down the rank list, relevant long-tail episodes naturally surface. |
| B08 | SOFT_PENALTY | 0:53 | 6.1s | CwcMemorySchema | schema-slide | Crucially, useful memories are never deleted or excluded; their bar to surface simply rises. |
| B09 | DIVERSITY_RESULT | 0:59 | 6.2s | CwcConceptCard | card-in | The result is higher retrieval entropy, broader context coverage, and fewer repetitive agent traps. |
| B10 | PRACTITIONER_DIRECTIVE | 1:05 | 5.9s | CwcConceptCard | card-in | If your agent repeats failed actions, audit your retrieval counts before fine-tuning embeddings. |
| B11 | OUTRO | 1:11 | 5.0s | ClaudeTitleOutro | outro-card | Novelty dampening. Diversity without deletion. Liam, in for Kriti. |
