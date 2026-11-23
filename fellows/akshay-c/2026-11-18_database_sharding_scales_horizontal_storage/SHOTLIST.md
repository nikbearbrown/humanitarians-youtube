# SHOTLIST - How Database Sharding Scales Horizontal Storage

| Beat | Act | Visual Subject | Motion Type | Primary Source |
|---|---|---|---|---|
| B00 | PROBLEM | Monolithic DB Bottleneck: Single server resource exhaustion (CPU, RAM, Disk IOPS) under massive scale | annotate | manim |
| B01 | SHARDING_CONCEPT | Horizontal Partitioning: Monolithic table dividing row-by-row across 4 independent shard nodes | annotate | manim |
| B02 | SHARD_KEY | Shard Key Extraction: Table schema isolating User ID as the deterministic routing key | annotate | manim |
| B03 | STRATEGY_COMPARE | Range vs Hash Partitioning: Side-by-side comparison of sequential ranges vs uniform hash distribution | annotate | manim |
| B04 | QUERY_ROUTING | Query Coordinator: Router inspecting shard key and directing query directly to single target shard | annotate | manim |
| B05 | SCATTER_GATHER | Scatter-Gather Penalty: Non-key queries fanning out to all shards and merging partial results | annotate | manim |
| B06 | REBALANCING | Shard Splitting: Overloaded shard splitting into twin balanced partitions and migrating live | annotate | manim |
| B07 | ARCHITECTURE | Production Topology: High-availability architecture pairing each shard with primary-replica nodes | hold | manim |
| B08 | OUTRO | Branded Humanitarians AI closing title card | hold | remotion |
