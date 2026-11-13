# FACTCHECK — dynamodb-hot-partition

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | DynamoDB hashes the partition key to choose a partition | TRUE | AWS DynamoDB developer guide — partitions and data distribution |
| 2 | Same partition key value → same partition | TRUE (for the item collection; DynamoDB may split hot item collections by sort key, but sustained single-key throughput stays bounded) | AWS developer guide |
| 3 | Per-partition limit ≈ 1,000 write units/s (and 3,000 read units/s) | TRUE | AWS — partition throughput limits |
| 4 | 1 write unit = one write per second of an item up to 1 KB | TRUE | AWS — write capacity units |
| 5 | Table-level spare capacity cannot remove a per-partition limit | TRUE | AWS — hot partitions |
| 6 | Adaptive capacity shifts throughput toward busy partitions but cannot exceed per-partition maximums | TRUE | AWS — adaptive capacity |
| 7 | Write sharding with suffixes (e.g. #0–#9) spreads writes; reads must query all shards and merge | TRUE | AWS — "Using write sharding to distribute workloads evenly" |
| 8 | 10,000 / 10 = 1,000 per shard, exactly at the limit; more shards give headroom | COMPUTED (asserted in build) | arithmetic |
| 9 | Partition key "2026-10-23" and 10,000 w/s table capacity | Illustrative scenario from the fellow's brief | — |
