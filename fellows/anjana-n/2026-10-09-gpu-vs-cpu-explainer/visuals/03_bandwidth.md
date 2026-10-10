# B03 — Memory Bandwidth

## Elements

### Top pipeline: CPU memory

#### Tube
- A moderate horizontal tube stretching across ~70% of screen width.
- Tube color: #4A90D9 (blue) outline, dark fill.
- Label above tube: "CPU: DDR5."

#### Data packets
- Small squares flowing through the tube left to right, evenly spaced.
- Flow speed is steady.
- Packets colored #4A90D9.

#### Throughput meter
- A horizontal bar gauge to the right of the tube.
- Fill level low.
- Label: "~100 GB/s."
- Gauge color: #4A90D9.

#### Destination
- The tube feeds into a simplified CPU chip icon.

### Bottom pipeline: GPU memory

#### Tube
- A wider horizontal tube, ~3x the height of the CPU tube.
- Tube color: #27AE60 (green) outline, dark fill.
- Label above tube: "GPU: HBM2e."

#### Data packets
- Dense stream of squares flowing rapidly, nearly touching.
- Flow speed is fast.
- Packets colored #27AE60.

#### Throughput meter
- A horizontal bar gauge to the right of the tube.
- Fill level high.
- Label: "~2 TB/s."
- Gauge color: #27AE60.

#### Destination
- The tube feeds into a simplified GPU chip icon.

### Ratio badge
- Between the two meters, a large "20x" in gold (#F1C40F).

### Label
- Centered below both pipelines: "memory bandwidth determines sustained throughput."
- Color: #EAEAEA.

## Animation sequence
1. CPU tube appears, data packets begin flowing (2s).
2. CPU meter fills, "~100 GB/s" appears (1s).
3. GPU tube appears below — wider — packets flow rapidly (2s).
4. GPU meter fills high, "~2 TB/s" appears (1s).
5. "20x" badge animates between the meters (2s).
6. Label fades in below (2s).

## Palette
- CPU tube/packets: #4A90D9 (blue)
- GPU tube/packets: #27AE60 (green)
- Meter outlines: matching tube color
- Ratio badge: #F1C40F (gold)
- Label: #EAEAEA
- Tube interiors: #1E1E2E
- Background: #1A1A2E
