# PEDAGOGY AUDIT — claude-liam-songbird
# "Claude, Sequenced." | songbird skill teardown
# Auditor: Claude Sonnet 4.6 | 2026-07-18

## Criteria (6-point rubric for skill-teardown modifier)

### 1. DOES NOT PARAPHRASE
B05 names WHY the Entry–Beat–Exit law governs every clip prompt chain — without it, each clip is a disconnected moment and the chain reads as a grab-bag rather than a continuous experience. The continuity lanes (visual: space/light/character/camera; musical: key/tempo/groove) are what let a viewer follow a chain of ten AI-generated clips as one film, not ten unrelated generations.
B06 names WHY the parameter rule appends the style string verbatim to every prompt — if a style string is altered or dropped mid-chain, consecutive clips diverge in look and the chain breaks visual coherence. The rule is mechanical, not creative: it enforces that one decision applies across all generations.
B07 names WHY session state resets on "new song" — mixing material from two songs without an explicit reset produces prompts that inherit the wrong continuity lanes (wrong key, wrong groove, wrong character state). The reset is the boundary that keeps each session coherent.
**SCORE: PASS**

### 2. REGISTER APPLIED
Every beat follows Teardown. Three mechanisms each described and judged. The self-demo produces a real plug output — one spoken-word cliffhanger for the Brutalist META-SERIES, tightening a conflict without resolving it.
**SCORE: PASS**

### 3. SELF-DEMO FEASIBLE AND EXECUTED
B03/B04 demonstrate the `plug` engine — one sentence that tightens a conflict without resolving it, then the CTA. Input: "the Brutalist META-SERIES builds every video in this series using the very skills it's teaching." Output: a genuine plug line written per the plug rules (noir/cinematic/soulful; never summarize; never answer the question). No paid APIs required. Not faked.
**SCORE: PASS**

### 4. ILLUSTRATE LAW SATISFIED
UI beats: B00 · B03 · BVDT · BHTF · BOUT = 5.
Illustration beats: B01 (Anatomy) · B02 (Pipeline) · B04 (Code) · B05/B06/B07 (Mechanism) = 6.
No two consecutive inner beats share same type.
**SCORE: PASS**

### 5. HANDOFF INVOKES THE SKILL
BHTF command: "./art songbird" with two forcing questions:
does every prompt in the chain carry an Exit pointing at the next Entry, and does the style string append verbatim to every prompt line? These target the two most common failures: prompts that each look finished but don't connect to adjacent clips, and style parameters that drift or disappear by the third prompt.
**SCORE: PASS**

### 6. VERBATIM QUOTES CITED
Three quotes from SKILL.md:
- "Never disconnected moments — every chain is one continuous experience." (the sequencing law)
- "appends to EVERY prompt line EXACTLY as written — never altered, never dropped mid-chain" (the parameter rule)
- "A session never mixes material from two songs without an explicit reset." (session-state logic)
**SCORE: PASS**

**VERDICT: PASS**
