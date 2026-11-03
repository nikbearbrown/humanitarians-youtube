# PROMPTS - How Database Indexing Searches Millions of Records in Milliseconds

## Project

Creator: Akshay Chavan
Channel: @HumanitariansAI
Format: Brutalist technical explainer
Topic: Database Indexing & B-Trees
Landscape master: 3840x2160
Portrait master: 2160x3840
Frame rate: 24 fps
Narration engine: Kokoro
Voice: am_onyx

## Creative direction

Create a high-contrast system-design explainer illustrating how database indexes use B-Tree structures to achieve millisecond query lookups across millions of rows.

Use clean geometric components: TABLE DISK BLOCKS, ROOT PAGE, BRANCH PAGES, LEAF PAGES, LINKED CHAINS, and SECONDARY POINTERS.

Maintain a dark Brutalist visual style with large typography, simple geometric boxes, strong contrast, and restrained accent colors.

Keep title, primary architecture diagram, annotations, and caption areas visually separated.

Use fixed component positions whenever possible so the viewer can follow the architectural progression between beats.

Do not allow arrows to pass through boxes, labels, titles, captions, or other arrows.

Keep all text well inside safe margins.

Keep diagrams readable at YouTube viewing sizes.

## Beat plan

B00 - Full table scan: Sequential O(N) scan across millions of disk blocks creating disk bottlenecks.
B01 - B-Tree index structure: Hierarchical multi-way balanced tree with Root, Branch, and Leaf nodes.
B02 - Fast tree traversal: Pointer-guided search resolving queries in 3-4 I/O hops instead of millions of scans.
B03 - Doubly linked leaf nodes: Horizontal chaining enabling efficient range queries and sequential scans.
B04 - Clustered vs Secondary indexes: Physical row ordering vs secondary key pointers.
B05 - Composite indexes: Multi-column indexing and the Leftmost Prefix Rule.
B06 - The write penalty: Maintenance cost, tree rebalancing, and page splits on writes.
B07 - Architecture payoff: Targeted indexing strategy, covering indexes, and optimal throughput.
B08 - Branded Humanitarians AI closing card.

## Production constraints

- Landscape source resolution: 3840x2160.
- Portrait source resolution: 2160x3840.
- Frame rate: 24 fps.
- Use native Manim graphics for B00-B07.
- Use ClaudeTitleOutro / ClaudeTitleOutro916 for B08.
- Preserve protected title and caption zones.
- Keep the primary architecture in the central region.
- Container strokes: #5D584F (luminance < 130).
- Minimum font size: >= 26pt (ensuring >= 41px physical height).
- B08 is the branded Humanitarians AI outro and must not be omitted.
