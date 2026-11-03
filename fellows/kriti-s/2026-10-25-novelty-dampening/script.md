# Novelty Dampening in Agent Memory — Diversity Without Deletion — script (narration as rendered)

Voice: Kokoro `am_onyx`

Narration copied word for word from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

### B00 · ASK
> Hello!, this is Liam, in for Kriti. Why does your agent keep retrieving the exact same generic memory?

### B01 · RETRIEVAL_TRAP
> In standard semantic search, high similarity scores trap the agent in repetitive recall loops.

### B02 · CROWDING_OUT
> One generic episode dominates retrieval, crowding out specialized experiences that actually solve the task.

### B03 · NOVELTY_DAMPENING
> To restore diversity, we apply Novelty Dampening, penalizing episodes that have been accessed repeatedly.

### B04 · THE_FORMULA
> The formula divides baseline similarity by one plus alpha times log of one plus access count.

### B05 · ALPHA_TUNING
> Alpha controls penalty strength, set to zero point one five for balanced, non-destructive dampening.

### B06 · LOG_DYNAMICS
> Because dampening scales logarithmically, early accesses face mild friction while chronic overuse drops steeply.

### B07 · SURFACING_TAIL
> As overused memories slide down the rank list, relevant long-tail episodes naturally surface.

### B08 · SOFT_PENALTY
> Crucially, useful memories are never deleted or excluded; their bar to surface simply rises.

### B09 · DIVERSITY_RESULT
> The result is higher retrieval entropy, broader context coverage, and fewer repetitive agent traps.

### B10 · PRACTITIONER_DIRECTIVE
> If your agent repeats failed actions, audit your retrieval counts before fine-tuning embeddings.

### B11 · OUTRO
> Novelty dampening. Diversity without deletion. Liam, in for Kriti.
