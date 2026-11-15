# PROMPTS - How Consistent Hashing Scales Distributed Systems

## Project

Creator: Akshay Chavan  
Channel: @HumanitariansAI  
Format: Brutalist technical explainer  
Topic: Consistent Hashing & Distributed System Partitioning  
Landscape master: 3840x2160  
Portrait master: 2160x3840  
Frame rate: 24 fps  
Narration engine: Kokoro  
Voice: am_onyx  

## Creative direction

Create a high-contrast system-design explainer illustrating how Consistent Hashing distributes data across dynamic server clusters, bounds remapping to K/N during topology changes, and prevents catastrophic cache stampedes.

Use clean geometric components: CLIENTS, HASH FUNCTION, CIRCULAR HASH RING, SERVER NODES (A, B, C, D), DATA KEYS, CLOCKWISE ROUTING ARCS, HOTSPOT IMBALANCE, and VIRTUAL NODES (Vnodes).

Maintain a dark Brutalist visual style with large typography, simple geometric boxes and rings, strong contrast, and restrained accent colors (`#111111` BG, `#F2EEE8` FG, `#C46F4B` ACCENT, `#78A083` GOOD, `#B65C5C` BAD, `#5C8BB6` BLUE, `#5D584F` BORDER).

Keep title, primary architecture diagram, annotations, and caption areas visually separated.

Use fixed component positions whenever possible so the viewer can follow the architectural progression between beats.

Do not allow arrows to pass through boxes, labels, titles, captions, or other arrows.

Keep all text well inside safe margins.

Keep diagrams readable at 4K YouTube viewing sizes.

## Beat plan

B00 - Naive modulo hashing chaos: hash(key) % N causes catastrophic full-cluster remapping on node addition/crash.  
B01 - Consistent hash ring concept: mapping keys and servers onto a circular 360-degree keyspace [0, 2^32 - 1].  
B02 - Clockwise key routing: hashing keys to positions on the ring and walking clockwise to the first custodian server node.  
B03 - Minimal movement on node addition: adding Server D only remaps the arc between its predecessor and itself (K/N keys).  
B04 - Graceful node removal: when Server B fails, its keys route clockwise to Server C without affecting Server A.  
B05 - Hotspot dilemma with non-uniform rings: small server counts create uneven arc lengths and load hotspots.  
B06 - Virtual nodes (Vnodes) balanced distribution: interleaving multiple virtual tokens per physical machine balances load evenly.  
B07 - Distributed architecture payoff: four core pillars of consistent hashing resilience and horizontal scale.  
B08 - Branded Humanitarians AI closing card.

## Production constraints

- Landscape source resolution: 3840x2160.
- Portrait source resolution: 2160x3840.
- Frame rate: 24 fps.
- Use native Manim graphics for B00-B07.
- Use Remotion ClaudeTitleOutro for B08.
- Gate T typography floor: 41px minimum.
- Gate V safe title insets: Landscape [192, 3648], [108, 2052]; Portrait [108, 2052], [192, 3302].
