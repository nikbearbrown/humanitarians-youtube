# Beat 3 — Smarter Penalties

**Visual type:** Remotion
**Duration:** ~12 seconds

## What the viewer sees

**Abstention calibration (0-7s):**
Two vote panels side by side on a dark background.

Panel 1 ("Close vote"):
Three extraction rows stacked vertically:
- Pass 1: "maintained, 0.80"
- Pass 2: "maintained, 0.78"
- Pass 3: "raised, 0.75"

A "2/3 agree" tag. The spread between majority (0.80) and minority (0.75) is small. A thin downward arrow nudges confidence: 0.80 to 0.77. Small penalty. Green border.

Label: "Small spread. Small penalty."

Panel 2 ("Wide vote"):
Three rows:
- Pass 1: "maintained, 0.80"
- Pass 2: "maintained, 0.82"
- Pass 3: "raised, 0.20"

A "2/3 agree" tag. The spread is massive (0.80 vs 0.20). A thick downward arrow pushes confidence hard: 0.80 to 0.62. Large penalty. Amber border.

Label: "Large spread. Large penalty."

**Section weighting (7-12s):**
A transcript document splits horizontally into two labeled sections:
- Top section: "Prepared Remarks" with a bright green weight badge "1.0"
- Bottom section: "Q&A" with an amber weight badge "0.8"

A signal extracted from prepared remarks shows its full confidence. The same signal from Q&A shows 0.8 scaling applied. A brief equation: 0.75 x 0.8 = 0.60.

Label: "Rehearsed vs spontaneous."

## Technical notes

- The two vote panels should be easy to compare at a glance
- The spread visualization is the key insight: same 2/3 vote, different penalty
- The arrow thickness represents penalty size
- Section weighting is simpler, just a split and two badges
