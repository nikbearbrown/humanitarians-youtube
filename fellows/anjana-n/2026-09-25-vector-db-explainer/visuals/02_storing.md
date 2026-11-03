# B02 — Storing Embeddings

## Composition type
Remotion

## Layout
Dark stage. 2D vector space with labeled dots clustering by meaning.

## Elements

### Vector space
- A 2D scatter plot (no axis labels, clean coordinates).
- Dots represent embedded text snippets.

### Positive cluster (upper right)
- Blue dots (#4A90D9): "quarterly revenue rose," "sales beat expectations," "exceeded guidance."
- Dots cluster tightly together.

### Negative cluster (lower left)
- Red dots (#E74C3C): "missed earnings target," "lowered full-year outlook," "revenue declined."
- Dots cluster tightly together.

### Labels
- Each dot has a small text label connected by a thin line.
- Annotation near one dot: "each dot = a vector of 768 numbers."

### Distance indicator
- A dashed line between the two clusters showing they are far apart.

## Animation sequence
1. Empty 2D space appears (0.5s).
2. Positive cluster dots appear one by one with labels (2.5s).
3. Negative cluster dots appear one by one (2.5s).
4. "768 numbers" annotation fades in (1s).
5. Dashed distance line between clusters (1s).

## Palette
- Positive cluster: #4A90D9 (blue)
- Negative cluster: #E74C3C (red)
- Annotation: #95A5A6 (muted grey)
- Background: #1A1A2E
