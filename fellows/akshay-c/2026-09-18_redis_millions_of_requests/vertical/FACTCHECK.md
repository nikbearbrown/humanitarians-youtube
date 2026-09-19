# Fact Check

- Kafka topics are divided into partitions; ordering is defined within a partition, not globally across a multi-partition topic.
- Keys can be used by the producer partitioner to keep related records routed consistently, subject to partitioner/configuration behavior.
- Within one consumer group, a partition is assigned to at most one consumer at a time; one consumer may own multiple partitions.
- More consumers than partitions means some consumers in that group have no partition assignment.
- Kafka consumers track positions using offsets; committed offsets are commonly used as recovery points.
- Kafka retains records according to topic retention/compaction policies, so reading is not inherently destructive.
- Consumer-group membership changes can trigger partition reassignment/rebalancing.
- Partitions may be replicated. A leader handles normal reads/writes while follower replicas copy the log; eligible in-sync replicas can be elected when leadership changes.
- Replication, acknowledgements, minimum in-sync replicas, producer idempotence/transactions, consumer commits, and downstream side effects all affect durability/delivery semantics. The script deliberately avoids saying "Kafka automatically guarantees exactly-once for every application."
- "Millions of events" is presented as an architectural scaling scenario, not a universal benchmark. Actual throughput depends on hardware, record size, compression, batching, partitions, replication, network, disk, configuration, and workload.
