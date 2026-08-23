# Beat 1 — The Hook

**Visual type:** Remotion
**Duration:** ~8 seconds
**Follows:** Claude-branded intro bookend

## What the viewer sees

"BERT" appears center screen, bold, large. Below it, the full name fades in: "Bidirectional Encoder Representations from Transformers." That fades and is replaced by a simpler label: "A language model that reads context."

**First test (0-4s):**
A sentence appears: "The market reacted positively."
BERT processes it — a brief pulse animation. A green "POSITIVE ✓" tag appears beside it. Correct. Easy.

**Second test (4-8s):**
The sentence changes to: "Revenue missed estimates by a narrow margin."
BERT processes it — same pulse. It tags it "POSITIVE" — but a red "✗" stamps over the tag. Wrong.

A small annotation appears below: BERT read "narrow margin" as positive. In finance, this sentence is cautious.

## Technical notes

- The two tests should feel like a quick demo — pass/fail
- The red X on the second test is the hook — the model failed on financial language
- Keep the BERT label minimal — don't over-explain the architecture here, that comes later
- Dark background, clean typography
