# SHOTLIST - How Database Indexing Searches Millions of Records in Milliseconds

| Beat | Act | Visual Subject | Motion Type | Primary Source |
|---|---|---|---|---|
| B00 | PROBLEM | Full table scan sequentially scanning millions of unindexed disk blocks with slow I/O | annotate | manim |
| B01 | SOLUTION | B-Tree index architecture: Root node, Branch nodes, and Leaf nodes hierarchy | annotate | manim |
| B02 | LOOKUP | Fast tree traversal: Key comparison navigating 3-4 hops from Root to target Leaf | annotate | manim |
| B03 | LEAF_CHAIN | Doubly linked leaf nodes: Horizontal chain traversal enabling rapid range queries | annotate | manim |
| B04 | CLUSTERED_VS_SECONDARY | Clustered table row storage versus Secondary index key pointers | annotate | manim |
| B05 | COMPOSITE_INDEXES | Composite index hierarchy and the Leftmost Prefix evaluation rule | annotate | manim |
| B06 | WRITE_TRADEOFF | The write penalty: Node page split overhead during INSERT and UPDATE operations | annotate | manim |
| B07 | PAYOFF | Production indexing strategy: Selective indexing, covering indexes, and high throughput | hold | manim |
| B08 | OUTRO | Branded Humanitarians AI closing title card | hold | remotion |
