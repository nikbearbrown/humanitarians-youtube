# B05 — Putting It Together

## Composition type
Remotion

## Layout
Dark stage. Two-level nested diagram showing all three parallelism strategies combined. Fade to title card.

## Elements

### Inner level: Single node (tensor parallel)

#### Node box
- A large rounded rectangle labeled "Node."
- Contains four GPU cards connected by thick horizontal bars.
- Bars labeled "NVLink: 900 GB/s."
- Each GPU holds a slice of the same layer (quarter of the weight matrix).
- Color: #4A90D9 (blue) for GPUs, #F1C40F (gold) for NVLink bars.
- Label below: "tensor parallel (within node)."

### Mid level: Pipeline across nodes

#### Three node boxes
- Three copies of the node box arranged left to right.
- Node 1: "layers 1–24."
- Node 2: "layers 25–48."
- Node 3: "layers 49–72."
- Arrows connect the nodes left to right.
- Arrows labeled "network: 100 Gb/s."
- Color: #95A5A6 (grey) for inter-node arrows.
- Label below: "pipeline parallel (across nodes)."

### Outer level: Data parallel replicas

#### Bracket
- A large bracket below the three-node pipeline.
- Label: "data parallel — replica 1."

#### Second replica
- A faded duplicate of the entire three-node pipeline below the first.
- Label: "data parallel — replica 2."
- Connected to replica 1 by dashed gradient sync arrows.
- Gradient sync label: "all-reduce."
- Color: #E67E22 (orange) for sync arrows.

### Bandwidth annotations
- Inside nodes: "NVLink: 900 GB/s" — #F1C40F (gold).
- Between nodes: "network: 100 Gb/s" — #95A5A6 (grey).
- Small note: "bottleneck: inter-node bandwidth."

### Title card
- Diagram fades.
- Centered text: "What Distributed Training Actually Looks Like."
- Color: #EAEAEA.
- Fade to dark.

## Animation sequence
1. Single node appears with four GPUs and NVLink bars (1.5s).
2. "tensor parallel" label appears (0.5s).
3. Two more nodes appear, forming the pipeline with inter-node arrows (2s).
4. "pipeline parallel" label appears (0.5s).
5. Second replica fades in below with bracket and gradient sync arrows (2s).
6. "data parallel" labels appear on both replicas (0.5s).
7. Bandwidth annotations fade in (1s).
8. Hold on full diagram (0.5s).
9. Fade to title card (2s).
10. Hold, fade to black (0.5s).

## Palette
- GPU cards: #4A90D9 (blue)
- NVLink bars: #F1C40F (gold)
- Layer groups: #9B59B6 (purple)
- Inter-node arrows: #95A5A6 (grey)
- Gradient sync arrows: #E67E22 (orange)
- Replica brackets: #EAEAEA
- Title text: #EAEAEA
- Background: #1A1A2E
