# Beat 1 — What is ECIS

**Visual type:** Remotion
**Duration:** ~20 seconds
**Follows:** Claude-branded intro bookend

## What the viewer sees

**The pipeline (0-10s):**
The architecture builds from left to right as the narration describes each component:

A transcript document icon enters from the left. It splits into chunks. The chunks flow into four reader nodes arranged vertically: Keyword (blue), FinBERT (teal), NER (orange), LLM (purple). Each node lights up as the narration names it.

Arrows from all four converge into the Triangulator node on the right. A single signal exits: direction + confidence badge.

**The scorecard (10-16s):**
The signal flows into an append-only log icon (a padlock stamps onto it). A timeline extends right with three checkpoints: 30, 90, 180 days. A market chart appears beside each checkpoint. The signal gets graded: green checkmark or red X at each horizon.

**Transition (16-20s):**
On "That is the foundation" the full architecture settles into a compact overview. On "Here is what it learned this week" the view zooms into the system, transitioning to Beat 2.

## Technical notes

- This is a condensed version of Episode 1's full architecture beat, built in 20 seconds instead of spread across 7 beats
- New viewers should understand: four readers, one triangulator, pre-registered scoring
- Returning viewers get a quick refresher without feeling like a repeat
- Build the architecture left-to-right in sync with the narration, each component appearing as it is named
- Keep node shapes and colors consistent with all previous episodes
