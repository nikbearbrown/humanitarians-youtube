# SHOTLIST — How Kafka Handles Millions of Events

Typed work order for the canonical 16:9 reel. `beat_sheet.json` remains the source of truth for narration, timing, lane/source, and render provenance.

## Delivery target

- Canonical master: 3840×2160, 16:9, 24 fps.
- Vertical derivative: full-length 2160×3840, 9:16, composed separately by the toolkit vertical workflow.
- Audio-first: visual timing follows measured Kokoro beat durations.
- Brand: @HumanitariansAI.
- Visual rule: use Claude UI only where the interface/code itself is the subject; explanatory body beats illustrate Kafka concepts directly.

## Beat work order

### B00 — INTRO

- **Lane:** REMOTION
- **Render source:** `ClaudeComposerAsk`
- **Work order:** Cold open. Claude composer receives the scaling question; output resolves to the three mechanisms that the reel will unpack. Keep it a genuine interface moment, not a generic title slide.
- **Narration anchor:** I'm Akshay. Imagine an app producing millions of events: orders, clicks, payments, sensor readings. If every producer waits for every downstream service, traffic spikes can turn one slow consumer into a system-wide failure. Kafka changes the shape of that problem. It puts a durable event log in the middle, then lets producers and consumers scale independently. So how does that architecture keep up when the event count explodes?

### B01 — PROBLEM

- **Lane:** MANIM
- **Render source:** `B01_DirectFanoutFails`
- **Work order:** Show one API fanning out synchronously to inventory, fraud, analytics, email, and billing. Animate a slowdown in one dependency propagating back into the API queue.
- **Narration anchor:** Start without Kafka. The API receives an order and immediately calls inventory, fraud detection, analytics, email, and billing. At low traffic, it looks fine. At high traffic, each dependency adds latency and another failure point. If fraud detection slows down, the API starts backing up. Producers and consumers are tightly coupled, and one spike propagates through the whole chain.

### B02 — BUFFER

- **Lane:** MANIM
- **Render source:** `B02_DurableLog`
- **Work order:** Insert Kafka between producers and consumers. Animate append-to-log, acknowledgement, consumer lag, retained records, then catch-up without blocking the producer.
- **Narration anchor:** Now put Kafka in the middle. Producers append events to a topic and can move on after Kafka acknowledges the write. Consumers read those events at their own pace. A temporary consumer slowdown no longer has to stop the producer. Kafka is not just passing messages through; it retains records for a configured period, which means consumers can fall behind and catch up later.

### B03 — PARTITIONS

- **Lane:** MANIM
- **Render source:** `B03_Partitions`
- **Work order:** Split one topic into multiple ordered partition lanes. Route same-key records to one lane while other keys flow in parallel. Emphasize order within a partition, not across the whole topic.
- **Narration anchor:** The first big scaling idea is partitioning. A Kafka topic is split into multiple partitions. Each partition is its own ordered log. Records with the same key can be routed to the same partition, preserving order for that key, while different partitions can be handled in parallel. More partitions create more lanes for throughput, although they also add coordination and operational cost.

### B04 — PRODUCER

- **Lane:** REMOTION
- **Render source:** `ClaudeCodeBeat`
- **Work order:** Show the actual producer code from the beat sheet. Highlight bootstrap servers, topic, key=user_id, and produce(). Keep code readable at 4K and animate emphasis rather than dumping extra prose.
- **Narration anchor:** A producer does not need to choose a broker for every event. It connects to the cluster, learns the metadata, and sends each record to the broker that currently leads its partition. Here the event key is the user ID. That gives related events a stable partitioning rule, which is useful when ordering per user matters.

### B05 — BROKERS

- **Lane:** MANIM
- **Render source:** `B05_Brokers`
- **Work order:** Distribute partition leaders/replicas across three brokers. Animate network/disk load spreading horizontally as brokers host different partitions.
- **Narration anchor:** Partitions are spread across Kafka brokers. Broker one might lead partitions zero and three, broker two partitions one and four, and broker three partitions two and five. Now network traffic, disk writes, and reads are distributed across machines instead of concentrating on one server. Kafka scales horizontally by adding brokers and balancing partition replicas across them.

### B06 — CONSUMERS

- **Lane:** MANIM
- **Render source:** `B06_ConsumerGroups`
- **Work order:** Show six partitions and a consumer group. Assign at most one consumer per partition in the group; then add a seventh consumer and visibly leave it idle.
- **Narration anchor:** On the read side, Kafka uses consumer groups. Within one group, a partition is assigned to at most one consumer at a time. If this topic has six partitions, up to six consumers in the same group can actively process those partitions in parallel. Add a seventh consumer and it sits idle until the assignment changes. That is why partition count sets the ceiling for parallelism inside a consumer group.

### B07 — OFFSETS

- **Lane:** MANIM
- **Render source:** `B07_Offsets`
- **Work order:** Represent offsets as numbered positions in a partition. Animate commit, restart/resume, then an intentional rewind/replay. Do not imply automatic end-to-end exactly-once behavior.
- **Narration anchor:** How does a consumer know where it is? With offsets. Every record has a position inside its partition. After processing, a consumer can commit the next offset it should read. If the process restarts, it resumes from the committed position. Because retention keeps older records, a team can also intentionally rewind and replay events. The exact delivery guarantee depends on how producers, consumers, commits, and downstream writes are configured; Kafka does not magically make every application exactly-once.

### B08 — CONSUMER CODE

- **Lane:** REMOTION
- **Render source:** `ClaudeCodeBeat`
- **Work order:** Show the actual consumer loop. Highlight group.id, disabled auto-commit, poll, process, and commit. Visual emphasis should reinforce the failure window between processing and committing.
- **Narration anchor:** In code, the consumer joins a group, subscribes to the topic, polls records, processes them, then commits progress. Here auto-commit is disabled so the application controls when progress is recorded. In production you would also design idempotency, retries, and error handling around this loop, because failures can happen between processing a record and recording its offset.

### B09 — FAILURE

- **Lane:** MANIM
- **Render source:** `B09_Rebalance`
- **Work order:** Kill one consumer, show group coordination/rebalance, reassign its partitions, and resume from committed offsets. Include a short coordination pause rather than implying zero interruption.
- **Narration anchor:** Now kill a consumer. Kafka's group coordination detects that the member is gone and the group rebalances. The failed consumer's partitions are reassigned to surviving members, which resume from committed offsets. A rebalance causes a temporary coordination pause, so modern Kafka applications try to keep processing predictable and avoid unnecessary churn, but the work itself is not permanently tied to one machine.

### B10 — REPLICATION

- **Lane:** MANIM
- **Render source:** `B10_Replication`
- **Work order:** Show leader and follower replicas across brokers. Fail the leader broker and promote an eligible in-sync replica. Keep configuration-dependent durability language visually neutral.
- **Narration anchor:** Kafka also protects partition data with replication. One replica is the leader and other replicas copy it on different brokers. Producers and consumers normally talk to the leader. If that broker fails, an eligible in-sync replica can become the new leader. Replication improves availability and durability, but the actual loss and availability behavior still depends on settings such as replication factor, acknowledgements, and in-sync replica requirements.

### B11 — SCALE

- **Lane:** MANIM
- **Render source:** `B11_FullScale`
- **Work order:** Assemble the complete architecture: producers → partitioned topic → distributed brokers/replicas → consumer group. Animate concurrent flow to make the scaling mechanism legible as many parallel lanes.
- **Narration anchor:** So the millions-of-events story is not one magic switch. Producers batch and append efficiently. Topics split traffic across partitions. Partition leaders are distributed across brokers. Consumer groups divide partitions across workers. Offsets let workers resume and replay. Replicas give partitions failover options. Together, those mechanisms let the pipeline spread storage, network traffic, and processing across many machines.

### B12 — TRADEOFFS

- **Lane:** MANIM
- **Render source:** `B12_Tradeoffs`
- **Work order:** Show four failure/limit motifs: too few partitions, too many partitions, consumer lag, and a hot key. End on capacity dimensions: disk, network, retention, replication, downstream throughput.
- **Narration anchor:** There are tradeoffs. Too few partitions cap parallelism. Too many partitions increase metadata, file handles, recovery work, and rebalancing complexity. Slow consumers accumulate lag. Hot keys can overload one partition. And Kafka still needs capacity planning for disk, network, retention, replication, and downstream systems. The architecture scales because work is partitioned—not because limits disappear.

### B13 — OUTRO

- **Lane:** REMOTION
- **Render source:** `ClaudeTitleOutro`
- **Work order:** Title-restate outro with @HumanitariansAI and Akshay Chavan. Keep the final frame stable and clean for QC; no new technical claims.
- **Narration anchor:** The mental model is simple: Kafka turns one overloaded pipeline into many ordered lanes. Partitions create the lanes, brokers host them, consumer groups divide the work, offsets track progress, and replicas keep copies available for failover. That's how Kafka can be designed to handle event streams at very large scale.

## Acceptance notes

- Every Manim beat must render from this reel’s `scenes.py` into its matching beat slot.
- Remotion beats must use the pattern + props declared in `beat_sheet.json`.
- Do not hand-time visuals before audio measurement; recompile against actual beat durations.
- Final master must contain no slates/placeholders and must pass the toolkit QC/final gates.
