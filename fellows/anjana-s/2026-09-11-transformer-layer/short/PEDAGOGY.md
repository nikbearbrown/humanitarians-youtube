# PEDAGOGY — What Happens Inside a Transformer Layer (9:16 Short derivative)

This is a derivative cut of `anjana-s/2026-09-11-inside-a-transformer-layer`,
produced by `runtime/scripts/shorts.py` — same signed script, same evidence,
reformatted to 9:16 and shortened to fit the 3:00 Shorts cap (223.8s parent →
~175s). The parent's GATE P sign-off (`PEDAGOGY.md`, `VERDICT: PASS`) covers
every beat's content; nothing here re-argues that evidence.

## What's different from the parent — and why the auto-plan was overridden

The cap-check auto-plan wanted to drop **B02 (self-attention)** and **B04
(residual + layer norm)** — two of the four operations the video is named
after, and its two longest beats. Rejected: a video whose thesis is "every
layer does the same four things" cannot ship a Short that shows two of them.

Re-cut manually with `--drop B01 B06 B07`, which keeps all four operations —
attention (B02) → feed-forward (B03) → residual + norm (B04) → the stacking
close (B05):

- **B01 (the hook) dropped.** The twelve-block stack and the "microscope in"
  move are reprised at the start of B05, so the Short still gets the stack.
- **B06 (the verdict recap) dropped.** A restatement of B02–B04.
- **B07 (the handoff) dropped.** Standard for this series' Shorts.
- **B08's outro narration was rewritten** — the only new text, the only audio
  regenerated. The auto-generated draft spliced two truncated narration
  fragments with the segment title. Rewritten to name what was cut, and kept
  deliberately short because this cut runs within a few seconds of the cap.
- **6 beats rewired to portrait `916` compositions** via the Onda check. The
  feed-forward beat's 48-cell expansion strip, which fits across the 16:9
  frame, wraps onto two rows of 24 in portrait; the residual/norm data-flow
  runs top-to-bottom with the bypass arcs on the left.
- **Endcard generated with `--handle ""`** at cut time — the durable fix.

## Evidence discipline

No new factual claims. The two flagged simplifications in the parent
(single-head attention, post-norm placement) carry over unchanged.

VERDICT: PASS
