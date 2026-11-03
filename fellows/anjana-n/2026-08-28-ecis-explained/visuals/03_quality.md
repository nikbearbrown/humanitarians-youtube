# Beat 3 — How Clean

**Visual type:** Remotion
**Duration:** ~12 seconds

## What the viewer sees

**Noisy chunk (0-6s):**
A chunk card appears on the left side of the screen. It looks messy:
- Red-highlighted text shows boilerplate language mixed into real content
- A sentence ends abruptly mid-word with "..."
- Two different speaker labels are visible within the chunk: "CEO" and "Analyst"

Four horizontal score meters animate in beside the chunk, each labeled and filling to a level:
- Boilerplate ratio: fills to 0.35 — amber
- Token count: fills to 0.72 — light green
- Section completeness: fills to 0.50 — amber (cut mid-sentence)
- Speaker transitions: fills to 0.40 — amber (multiple speakers)

The four meters visually merge into a single combined bar: "Quality: 0.49" in amber.

**Clean chunk (6-9s):**
A second chunk card appears on the right side. Clean text, single speaker, complete sentences. No highlights or issues.

Its four meters fill high:
- Boilerplate: 0.05 — green
- Token count: 0.95 — green
- Completeness: 0.98 — green
- Transitions: 1.0 — green

Combined: "Quality: 0.94" in bright green.

**The comparison (9-12s):**
Both chunks flow toward the triangulator node (shown as a compact icon between them). The clean chunk's arrow is thick and bright. The noisy chunk's arrow is thin and faded — almost invisible.

Label: "Quality gates the signal, not the data."

## Technical notes

- The messy chunk should look visually noisy — mixed colors, broken text, multiple labels
- The clean chunk should look calm and clean by contrast
- The four meters should animate in sequence, each filling in ~0.5 seconds
- The merge from four meters to one combined score should feel like a calculation completing
- Arrow thickness difference at the end is the payoff — the triangulator barely listens to the noisy chunk
