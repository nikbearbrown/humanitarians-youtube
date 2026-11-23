# PROMPTS - How Database Sharding Scales Horizontal Storage

## Project

Creator: Akshay Chavan  
Channel: @HumanitariansAI  
Format: Brutalist technical explainer  
Topic: Database Sharding & Horizontal Data Partitioning  
Landscape master: 3840x2160  
Portrait master: 2160x3840  
Frame rate: 24 fps  
Narration engine: Kokoro  
Voice: am_onyx  

## Creative direction

Create a high-contrast system-design explainer illustrating how Database Sharding partitions monolithic databases across independent shared-nothing clusters to scale storage and throughput infinitely.

Use clean geometric components: CLIENTS, MONOLITH DATABASE, RESOURCE EXHAUSTION METRICS, INDEPENDENT SHARDS (0 to 3), SHARD KEY ATTRIBUTES, RANGE VS HASH PARTITIONING COMPARISON, QUERY ROUTER / COORDINATOR, SCATTER-GATHER FAN-OUT, PARTITION REBALANCING SPLIT, and HIGH AVAILABILITY REPLICA TOPOLOGY.

Maintain a dark Brutalist visual style with large typography, simple geometric boxes and cards, strong contrast, and restrained accent colors (`#111111` BG, `#F2EEE8` FG, `#C46F4B` ACCENT, `#78A083` GOOD, `#B65C5C` BAD, `#5C8BB6` BLUE, `#5D584F` BORDER).

Keep title, primary architecture diagram, annotations, and caption areas visually separated.

Use fixed component positions whenever possible so the viewer can follow the architectural progression between beats.

Do not allow arrows to pass through boxes, labels, titles, captions, or other arrows.

Keep all text well inside safe margins (Title safe insets: Landscape `[192, 3648]`, `[108, 2052]`; Portrait `[108, 2052]`, `[192, 3302]`).

Keep diagrams readable at 4K YouTube viewing sizes with explicit font sizes.

## Beat plan

B00 - Monolithic database bottleneck: single node resource exhaustion under extreme scale (RAM 98%, Disk IOPS 100%, CPU choke).  
B01 - Horizontal sharding architecture: dividing monolithic dataset row-by-row across independent shard nodes.  
B02 - Shard key selection: choosing user ID / tenant ID as the routing key to partition tables cleanly.  
B03 - Range vs hash partitioning: comparing contiguous range sequential buckets against uniform hash dispersion.  
B04 - Direct query routing: coordinator router evaluating shard key to route query directly to authoritative shard.  
B05 - Cross-shard scatter-gather: the latency penalty when queries lack shard keys, requiring broadcast and in-memory merge.  
B06 - Shard splitting and live rebalancing: dividing overloaded partitions and migrating slices without stopping writes.  
B07 - High-availability sharded topology: production architecture pairing each horizontal shard with primary-replica sets.  
B08 - Branded Humanitarians AI closing card.

## Production constraints

- Landscape source resolution: 3840x2160.
- Portrait source resolution: 2160x3840.
- Frame rate: 24 fps.
- Use native Manim graphics for B00-B07.
- Use native Remotion graphics for B08.
