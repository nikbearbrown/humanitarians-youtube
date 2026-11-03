# B05 — ChromaDB Optimization and Grafana

## Composition type
Remotion

## Layout
Dark stage. Top half: ChromaDB before/after. Bottom half: Grafana dashboard mockup.

## Elements

### Top half: ChromaDB Optimization

#### Before (left)
- A scatter of dots representing exemplars in embedding space.
- Several pairs of dots almost overlapping (near-duplicates circled in red).
- The dots are unevenly distributed: many in the "raised" region, few in the "maintained/none" boundary.

#### After (right)
- The same space, now cleaner.
- Near-duplicate dots removed (circles gone).
- New dots added in the maintained/none boundary region (highlighted with a subtle green glow).
- More even distribution across all regions.
- Label: "after: deduplicated, boundary exemplars added."

#### HNSW parameters
- Small floating labels near the after panel: "ef_construction: 200," "M: 32," "ef_search: 100."
- A small recall metric: "recall@10: 0.94."

### Bottom half: Grafana Dashboard Mockup

Four panels in a 2x2 grid, styled like dark-theme Grafana:

#### Top-left: Reader Health
- A time-series line chart. Green line hovering at ~95% (reader success rate).
- Y-axis: 0-100%. Label: "reader success rate."

#### Top-right: Extraction Latency
- Three time-series lines for p50 (thin blue), p95 (medium blue), p99 (thick blue).
- The p95 line spikes in one segment.
- A small alert bell icon glows orange on the spike.
- Label: "latency percentiles."

#### Bottom-left: Signal Throughput
- A bar chart with 6-8 bars representing batches.
- Bars stacked by direction: blue (raised), red (lowered), grey (maintained).
- Label: "signals per batch."

#### Bottom-right: Data Completeness
- A small heatmap grid (tickers as rows, data sources as columns).
- Cells are green (complete) or red (missing).
- Label: "completeness by ticker."

## Animation sequence
1. "Before" exemplar scatter appears with duplicate circles (2s).
2. "After" scatter replaces it: duplicates removed, boundary dots glow green (2s).
3. HNSW parameter labels and recall metric fade in (1s).
4. Grafana panels appear one by one in the 2x2 grid:
   - Reader health line draws (1s).
   - Latency lines draw, alert bell on spike (1s).
   - Throughput bars grow upward (1s).
   - Completeness grid fills with checks and gaps (1s).
5. Hold full dashboard (1s).

## Palette
- Duplicate circles: #E74C3C (red)
- Boundary exemplars: #27AE60 (green glow)
- HNSW labels: #95A5A6 (muted grey)
- Grafana panel borders: #2C3E50 (dark slate)
- Grafana panel backgrounds: #1E1E2E (slightly lighter than main background)
- Reader health line: #27AE60 (green)
- Latency lines: #4A90D9 shades (blue)
- Alert bell: #E67E22 (orange)
- Throughput raised: #4A90D9 (blue), lowered: #E74C3C (red), maintained: #95A5A6 (grey)
- Completeness green: #27AE60, red: #E74C3C
- Background: #1A1A2E
