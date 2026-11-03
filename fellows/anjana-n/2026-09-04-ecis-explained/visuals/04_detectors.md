# Beat 4 — New Detectors

**Visual type:** Remotion
**Duration:** ~12 seconds

## What the viewer sees

Three detector cards appear in rapid sequence, each with a quick visual demo. ~4 seconds each.

**Negation detection (0-4s):**
A chunk of text appears: "We do not expect to raise guidance this quarter."

The phrase "do not expect to raise" highlights in red. A negation flag icon appears beside the chunk.

A routing diagram shows: the chunk bypasses the fast-pass lane entirely. An arrow routes it directly to "Full LLM extraction" skipping the shortcut. Label: "Negation detected. Fast-pass bypassed."

**Keyword density (4-8s):**
Two chunks side by side.

Chunk A: text with multiple guidance phrases highlighted in blue ("raising guidance," "revenue outlook," "increasing forecast"). A density meter fills high: 0.85 (green). Label: "Strong lexical support."

Chunk B: plain text with no highlights, just a small FinBERT sentiment tag attached. Density meter barely fills: 0.05 (red). Label: "Sentiment only. No lexical backing."

Chunk A's arrow to the triangulator is thick. Chunk B's is thin and faded.

**Duplicate detection (8-12s):**
Two transcript document icons appear, identical. Both show matching labels: "#a7f3..."

The second transcript approaches a gate. Stamp: "DUPLICATE." It greys out and fades. A small counter: "Skipped. Compute saved."

The first transcript continues through the pipeline normally. Label: "Same filing. Caught. Skipped."

## Technical notes

- Each detector gets exactly ~4 seconds, keep them tight and rhythmic
- The negation highlight in red should feel like a warning flag
- Keyword density's side-by-side comparison mirrors Beat 3 of Episode 4 (chunk quality)
- Duplicate detection is the simplest visual, just two matching and a rejection
- This beat moves fast, like an upgrade montage
