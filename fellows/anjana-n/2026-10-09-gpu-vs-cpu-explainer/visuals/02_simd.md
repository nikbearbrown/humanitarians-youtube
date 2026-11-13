# B02 — One Fast vs Many Wide

## Elements

### Left side: CPU

#### Chip outline
- A rectangular chip outline, labeled "CPU" at top.
- Inside: 8 large squares in a 2x4 grid, each representing a core.
- Each core glows blue (#4A90D9).
- Cores are visibly large with space between them.

#### Sequential processing
- A queue of 16 small operation tokens (tiny gold squares) lines up to the left of the chip.
- One core lights up brighter, processes one token (the token enters the core, a checkmark appears, the token exits right).
- Then the next token enters the same core.
- Other cores are idle (dimmed).
- A clock at the bottom ticks once per operation.

#### Note
- Small text below the chip: "up to 128 cores on server chips."

#### Label
- Below: "optimized for complex sequential tasks."

### Right side: GPU

#### Chip outline
- A rectangular chip outline, labeled "GPU" at top.
- Inside: a dense grid of ~100 small dots (simplified representation of thousands of cores).
- Each dot is green (#27AE60).

#### Parallel processing
- The same 16 operation tokens appear — they ALL enter the chip simultaneously.
- ALL dots light up at once. All 16 tokens get checkmarks in a single clock tick.
- The clock at the bottom ticks once — and everything completes.

#### Label
- Below: "optimized for parallel throughput."

### SIMD badge
- Centered between the two sides, a floating badge: "SIMD: single instruction, multiple data."
- Badge: #F1C40F (gold) text on a dark card.

## Animation sequence
1. CPU chip with 8 cores appears (1s).
2. Operation queue lines up, tokens process one by one — 4 ticks shown (3s).
3. GPU chip with dense core grid appears (1s).
4. Same tokens enter GPU — all cores light up simultaneously (2s).
5. All tokens complete in one tick (1s).
6. Labels appear below each chip (1s).
7. SIMD badge fades in at center (1s).

## Palette
- CPU cores: #4A90D9 (blue)
- CPU chip outline: #2C3E50
- GPU cores: #27AE60 (green)
- GPU chip outline: #2C3E50
- Operation tokens: #F1C40F (gold)
- Checkmarks: #EAEAEA
- SIMD badge: #F1C40F text on #2C3E50
- Clock: #95A5A6
- Background: #1A1A2E
