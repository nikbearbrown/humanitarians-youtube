# B01 — Order Matters

## Composition type
Remotion

## Layout
Dark stage. Left: shuffled tabular data. Right: time series in order, then shuffled.

## Elements

### Left: Tabular dataset
- A small table with five rows and three columns (generic labels: "ID," "A," "B").
- Rows shuffle animation — rows swap positions.
- The table looks the same after shuffling (no pattern lost).
- Label below: "shuffle a table — nothing changes."
- Color: #95A5A6 (grey) for the table.

### Right: Time series

#### Ordered state
- A line chart with ~20 data points connected by a blue (#3498DB) line.
- Clear wave pattern visible — peaks and troughs.
- X-axis: time (t1 through t20).
- Label: "in order — pattern visible."

#### Shuffled state
- The same data points, but x-positions scrambled randomly.
- The line zig-zags chaotically — no pattern.
- Color: #E74C3C (red) line.
- Label: "shuffled — signal gone."

### Bottom annotation
- "The sequence itself is the signal."
- Color: #F1C40F (gold).

## Animation sequence
1. Table appears on left (1s).
2. Table rows shuffle — table looks the same (1.5s).
3. "shuffle a table — nothing changes" label (0.5s).
4. Ordered time series line draws on right (2s).
5. "in order — pattern visible" label (0.5s).
6. Points scatter to random positions — line turns red and chaotic (2s).
7. "shuffled — signal gone" label (0.5s).
8. Bottom annotation in gold (1.5s).

## Palette
- Table: #95A5A6 (grey)
- Ordered series: #3498DB (blue)
- Shuffled series: #E74C3C (red)
- Annotation: #F1C40F (gold)
- Background: #1A1A2E
- Text: #EAEAEA
