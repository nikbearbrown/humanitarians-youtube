# PROMPTS — How Kafka Handles Millions of Events

Beat-prefixed build prompts for the currently open visual slots. These are production prompts, not narration. `beat_sheet.json` remains authoritative.

## 16:9 canonical reel prompts

### B00

Render the beat_sheet.json ClaudeComposerAsk exactly as specified. The composer should ask how Kafka can move millions of events without making every producer wait for every consumer, then resolve to three concise outputs: durable log, partitions, consumer groups. Preserve @HumanitariansAI branding and a clean 3840×2160 composition.

### B01

Create a Manim systems diagram of a backend API synchronously calling inventory, fraud detection, analytics, email, and billing. Start healthy, then slow fraud detection; animate queue/backpressure spreading upstream until the API is visibly congested. Minimal labels, moving requests, no decorative stock imagery.

### B02

Create a Manim explanation of Kafka as a retained append-only event log between producers and consumers. Show producers appending and receiving acknowledgement while one consumer slows, lag grows, records remain in the log, and the consumer later catches up. Do not depict Kafka as a transient pass-through queue only.

### B03

Create a Manim topic split into several ordered partitions. Animate records with keys; records sharing one key must go to the same partition while other keys distribute across other partitions. Make parallelism obvious while preserving per-partition ordering. Include a brief visual cue that more partitions add coordination cost.

### B04

Render the ClaudeCodeBeat from beat_sheet.json using the provided producer.py code exactly. Animate focus on bootstrap.servers, topic orders, key=event.user_id, value, then p.flush(). The teaching point is stable key-based partition routing and producer interaction with cluster metadata.

### B05

Create a Manim three-broker Kafka cluster. Place partition leaders across brokers and show replica copies on other brokers. Animate write/read traffic distributed across machines, then visually reinforce horizontal scaling by adding capacity without implying unlimited throughput.

### B06

Create a Manim consumer-group assignment demo with six topic partitions. Assign six consumers in one group one partition each, then add a seventh consumer and show it idle. Make the rule unmistakable: within a group, a partition is assigned to at most one consumer at a time.

### B07

Create a Manim partition with records labeled by offsets. Animate a consumer processing records and committing the next position, crashing/restarting and resuming from committed progress, then rewinding to replay retained records. Include a small caution cue that delivery semantics depend on surrounding configuration/application behavior.

### B08

Render the ClaudeCodeBeat from beat_sheet.json using the provided consumer.py code exactly. Animate focus on group.id, enable.auto.commit=False, subscribe, poll, process, and commit. Visually mark the process→commit failure window and keep text large enough for a 4K YouTube master.

### B09

Create a Manim consumer-group rebalance. Begin with partitions assigned across several consumers. Remove one consumer, show a brief coordination pause, then reassign its partitions to surviving consumers and resume from committed offsets. Do not imply perfectly interruption-free failover.

### B10

Create a Manim replication/failover diagram. Show a partition leader and follower replicas on separate brokers. Fail the leader broker, then promote an eligible in-sync replica. Keep the visual claim conditional: durability/availability depend on replication and acknowledgement settings.

### B11

Create the culminating Manim architecture showing multiple producers, a partitioned Kafka topic distributed across brokers with replicas, and a consumer group processing partitions in parallel. Animate many events simultaneously so the viewer sees how storage, network, and processing are spread across machines.

### B12

Create a Manim tradeoffs beat with four short animated cases: too few partitions limiting parallelism; too many partitions increasing coordination/recovery burden; a slow consumer building lag; and a hot key overloading one partition. Finish with disk/network/retention/replication/downstream capacity as constraints.

### B13

Render the beat_sheet.json ClaudeTitleOutro exactly: “How Kafka Handles Millions of Events.” with @HumanitariansAI and “with Akshay Chavan · Backend Engineering”. Hold a stable clean final frame for QC.

## Portrait composition note

For the full-length 9:16 derivative, preserve the same conceptual sequence but re-layout each scene for 2160×3840. Do not crop the 16:9 master. Stack producers/topic/consumers vertically where useful, reduce simultaneous labels, and keep all primary text inside portrait-safe margins.
